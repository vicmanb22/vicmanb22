#!/usr/bin/env python3
"""Unsubscribe from email sender using various methods.

Attempts unsubscribe in order of preference:
1. RFC 8058 one-click POST (List-Unsubscribe-Post header)
2. Mailto (List-Unsubscribe mailto: URL)
3. Body link parsing (find unsubscribe link in HTML body)
4. Manual fallback (returns link for user to click)

Usage:
    python3 gmail_unsubscribe.py --email victor.lang22@gmail.com --message-id abc123
    python3 gmail_unsubscribe.py --email victor.lang22@gmail.com --message-id abc123 --dry-run
"""

# Suppress warnings before any other imports
import warnings
warnings.filterwarnings('ignore')

import argparse
import json
import logging
import re
import sys
import urllib.request
import urllib.error
from email.mime.text import MIMEText
from pathlib import Path
import base64

# Suppress Google API discovery cache warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from utils import (
    extract_body_from_payload,
    parse_email_address,
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def get_list_unsubscribe_headers(headers: list) -> dict:
    """Extract List-Unsubscribe and List-Unsubscribe-Post headers.

    Args:
        headers: List of {'name': ..., 'value': ...} dicts

    Returns:
        Dict with 'url', 'mailto', 'has_one_click', 'post_body' keys
    """
    result = {
        'url': None,
        'mailto': None,
        'has_one_click': False,
        'post_body': None
    }

    for h in headers:
        name = h.get('name', '').lower()
        value = h.get('value', '')

        if name == 'list-unsubscribe':
            # Parse URLs from header like: <mailto:unsub@example.com>, <https://example.com/unsub>
            urls = re.findall(r'<([^>]+)>', value)
            for url in urls:
                if url.startswith('mailto:'):
                    result['mailto'] = url
                elif url.startswith('http'):
                    result['url'] = url

        elif name == 'list-unsubscribe-post':
            # RFC 8058: "List-Unsubscribe=One-Click"
            if 'List-Unsubscribe=One-Click' in value:
                result['has_one_click'] = True
                result['post_body'] = 'List-Unsubscribe=One-Click'

    return result


def find_unsubscribe_links_in_body(html: str) -> list:
    """Find unsubscribe links in HTML body.

    Args:
        html: HTML content of email body

    Returns:
        List of unsubscribe URLs found
    """
    if not html:
        return []

    links = []

    # Look for href attributes containing 'unsubscribe'
    pattern = r'href=["\']([^"\']*(?:unsubscribe|opt-out|optout|remove)[^"\']*)["\']'
    matches = re.findall(pattern, html, re.IGNORECASE)

    for url in matches:
        # Validate it's a proper URL
        if url.startswith('http') and url not in links:
            links.append(url)

    return links


def execute_rfc8058_unsubscribe(url: str, post_body: str, timeout: int = 30) -> dict:
    """Execute RFC 8058 one-click unsubscribe via HTTP POST.

    Args:
        url: The unsubscribe URL
        post_body: POST body (usually "List-Unsubscribe=One-Click")
        timeout: Request timeout in seconds

    Returns:
        Dict with success status and message
    """
    try:
        data = post_body.encode('utf-8')
        req = urllib.request.Request(
            url,
            data=data,
            method='POST',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Gmail-Subscription-Manager/1.0'
            }
        )

        with urllib.request.urlopen(req, timeout=timeout) as response:
            status_code = response.getcode()
            if 200 <= status_code < 300:
                return {
                    'success': True,
                    'method': 'post',
                    'message': f'Unsubscribe request sent successfully (HTTP {status_code})'
                }
            else:
                return {
                    'success': False,
                    'method': 'post',
                    'message': f'Unexpected response code: {status_code}'
                }

    except urllib.error.HTTPError as e:
        return {
            'success': False,
            'method': 'post',
            'message': f'HTTP error: {e.code} {e.reason}'
        }
    except urllib.error.URLError as e:
        return {
            'success': False,
            'method': 'post',
            'message': f'URL error: {str(e.reason)}'
        }
    except Exception as e:
        return {
            'success': False,
            'method': 'post',
            'message': f'Error: {str(e)}'
        }


def parse_mailto_url(mailto: str) -> dict:
    """Parse mailto URL into components.

    Args:
        mailto: mailto URL like "mailto:unsub@example.com?subject=Unsubscribe"

    Returns:
        Dict with 'to', 'subject', 'body' keys
    """
    result = {'to': None, 'subject': 'Unsubscribe', 'body': ''}

    if not mailto.startswith('mailto:'):
        return result

    # Remove mailto: prefix
    rest = mailto[7:]

    # Split address and params
    if '?' in rest:
        address, params = rest.split('?', 1)
    else:
        address = rest
        params = ''

    result['to'] = address

    # Parse query params
    if params:
        for param in params.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                key = key.lower()
                # URL decode
                value = urllib.request.unquote(value)
                if key == 'subject':
                    result['subject'] = value
                elif key == 'body':
                    result['body'] = value

    return result


def execute_mailto_unsubscribe(service, mailto: str, from_email: str) -> dict:
    """Send unsubscribe email via Gmail API.

    Args:
        service: Gmail API service
        mailto: mailto URL with unsubscribe address
        from_email: Sender email address (for reference)

    Returns:
        Dict with success status and message
    """
    try:
        parsed = parse_mailto_url(mailto)

        if not parsed['to']:
            return {
                'success': False,
                'method': 'mailto',
                'message': 'Invalid mailto URL - no recipient address'
            }

        # Create the email message
        message = MIMEText(parsed['body'] or f'Please unsubscribe this email address.')
        message['to'] = parsed['to']
        message['subject'] = parsed['subject']

        # Encode for Gmail API
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

        # Send the message
        request = service.users().messages().send(
            userId='me',
            body={'raw': raw}
        )
        result = retry_with_backoff(request.execute)

        return {
            'success': True,
            'method': 'mailto',
            'message': f'Unsubscribe email sent to {parsed["to"]}',
            'message_id': result.get('id')
        }

    except Exception as e:
        return {
            'success': False,
            'method': 'mailto',
            'message': f'Failed to send unsubscribe email: {str(e)}'
        }


def execute_link_unsubscribe(url: str, timeout: int = 30) -> dict:
    """Execute unsubscribe via GET request to body link.

    Args:
        url: The unsubscribe URL
        timeout: Request timeout in seconds

    Returns:
        Dict with success status and message
    """
    try:
        req = urllib.request.Request(
            url,
            method='GET',
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
        )

        with urllib.request.urlopen(req, timeout=timeout) as response:
            status_code = response.getcode()
            if 200 <= status_code < 300:
                return {
                    'success': True,
                    'method': 'link',
                    'message': f'Unsubscribe link visited successfully (HTTP {status_code})',
                    'note': 'Some sites require confirmation - check your email'
                }
            else:
                return {
                    'success': False,
                    'method': 'link',
                    'message': f'Unexpected response code: {status_code}'
                }

    except urllib.error.HTTPError as e:
        # Some unsubscribe pages return 302 redirect which is fine
        if e.code in [301, 302, 303, 307, 308]:
            return {
                'success': True,
                'method': 'link',
                'message': f'Unsubscribe link visited (redirected)',
                'note': 'Some sites require confirmation - check your email'
            }
        return {
            'success': False,
            'method': 'link',
            'message': f'HTTP error: {e.code} {e.reason}'
        }
    except Exception as e:
        return {
            'success': False,
            'method': 'link',
            'message': f'Error: {str(e)}'
        }


def unsubscribe(service, message_id: str, dry_run: bool = False) -> dict:
    """Attempt to unsubscribe using the best available method.

    Args:
        service: Gmail API service
        message_id: Gmail message ID
        dry_run: If True, don't actually unsubscribe, just report what would happen

    Returns:
        Dict with success status, method used, and message
    """
    # Fetch the full message to get headers and body
    request = service.users().messages().get(
        userId='me',
        id=message_id,
        format='full'
    )
    message = retry_with_backoff(request.execute)

    payload = message.get('payload', {})
    headers = payload.get('headers', [])

    # Get sender info for reporting
    from_header = next((h['value'] for h in headers if h['name'].lower() == 'from'), '')
    sender = parse_email_address(from_header)

    # Get unsubscribe headers
    unsub = get_list_unsubscribe_headers(headers)

    # Get body for link parsing
    body = extract_body_from_payload(payload)
    body_links = find_unsubscribe_links_in_body(body.get('html', ''))

    # Build result with available methods
    result = {
        'message_id': message_id,
        'sender': sender['email'],
        'sender_name': sender['name'],
        'available_methods': [],
        'headers_found': {
            'list_unsubscribe_url': unsub['url'],
            'list_unsubscribe_mailto': unsub['mailto'],
            'has_one_click': unsub['has_one_click']
        },
        'body_links': body_links[:3] if body_links else []  # Limit to first 3
    }

    # Determine available methods
    if unsub['url'] and unsub['has_one_click']:
        result['available_methods'].append('post')
    if unsub['mailto']:
        result['available_methods'].append('mailto')
    if unsub['url'] and not unsub['has_one_click']:
        result['available_methods'].append('link_header')
    if body_links:
        result['available_methods'].append('link_body')

    if dry_run:
        result['dry_run'] = True
        if result['available_methods']:
            result['would_use'] = result['available_methods'][0]
            result['message'] = f"Would attempt unsubscribe via {result['available_methods'][0]}"
        else:
            result['would_use'] = 'manual'
            result['message'] = 'No automatic unsubscribe method available'
        return result

    # Try methods in priority order
    # 1. RFC 8058 POST
    if unsub['url'] and unsub['has_one_click']:
        exec_result = execute_rfc8058_unsubscribe(unsub['url'], unsub['post_body'])
        result.update(exec_result)
        if exec_result['success']:
            return result

    # 2. Mailto
    if unsub['mailto']:
        exec_result = execute_mailto_unsubscribe(service, unsub['mailto'], sender['email'])
        result.update(exec_result)
        if exec_result['success']:
            return result

    # 3. Link from header (GET request)
    if unsub['url'] and not unsub['has_one_click']:
        exec_result = execute_link_unsubscribe(unsub['url'])
        result.update(exec_result)
        if exec_result['success']:
            return result

    # 4. Body link fallback
    if body_links:
        exec_result = execute_link_unsubscribe(body_links[0])
        result.update(exec_result)
        if exec_result['success']:
            return result

    # 5. Manual fallback - return links for user
    result['success'] = False
    result['method'] = 'manual'

    if body_links:
        result['manual_link'] = body_links[0]
        result['message'] = 'Automatic unsubscribe failed. Please click the link manually.'
    else:
        result['message'] = 'No unsubscribe method found. Please open the email and unsubscribe manually.'

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Unsubscribe from email sender'
    )
    add_common_args(parser)
    parser.add_argument(
        '--message-id',
        required=True,
        help='Gmail message ID to use for unsubscribe'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would happen without actually unsubscribing'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)

        result = unsubscribe(
            service,
            args.message_id,
            dry_run=args.dry_run
        )

        if result.get('success', False) or result.get('dry_run', False):
            output_success(result)
        else:
            # Still output as success=False but don't exit with error code
            # since the script ran correctly, just unsubscribe failed
            print(json.dumps({'success': False, **result}, ensure_ascii=False, indent=2))
            sys.exit(0)

    except FileNotFoundError as e:
        output_error(str(e), 'CREDENTIALS_NOT_FOUND', exit_code=3)

    except Exception as e:
        error_type = 'API_ERROR'
        exit_code = 2

        error_str = str(e)
        if 'invalid_grant' in error_str.lower():
            error_type = 'AUTH_ERROR'
            exit_code = 3

        output_error(str(e), error_type, exit_code=exit_code)


if __name__ == '__main__':
    main()
