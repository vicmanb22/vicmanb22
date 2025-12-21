#!/usr/bin/env python3
"""Create or update a Gmail draft.

New capability (not in MCP - was denied).

Usage:
    # Create a new draft
    python3 gmail_create_draft.py --email victor.lang22@gmail.com --to "recipient@example.com" --subject "Draft" --body "Content"

    # Update an existing draft
    python3 gmail_create_draft.py --email victor.lang22@gmail.com --draft-id "abc123" --to "recipient@example.com" --subject "Updated" --body "New content"

    # Send a draft
    python3 gmail_create_draft.py --email victor.lang22@gmail.com --draft-id "abc123" --send
"""

import argparse
import base64
import json
import sys
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_gmail_service
from utils import (
    output_success,
    output_error,
    retry_with_backoff,
    add_common_args
)


def create_raw_message(
    sender: str,
    to: str,
    subject: str,
    body: str,
    cc: str = None,
    bcc: str = None,
    html_body: str = None
) -> str:
    """Create a base64url encoded email message."""
    if html_body:
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))
    else:
        msg = EmailMessage()
        msg.set_content(body)

    msg['To'] = to
    msg['From'] = sender
    msg['Subject'] = subject

    if cc:
        msg['Cc'] = cc
    if bcc:
        msg['Bcc'] = bcc

    return base64.urlsafe_b64encode(msg.as_bytes()).decode()


def create_draft(
    service,
    sender: str,
    to: str,
    subject: str,
    body: str,
    cc: str = None,
    bcc: str = None,
    html_body: str = None,
    thread_id: str = None
) -> dict:
    """Create a new draft.

    Args:
        service: Gmail API service
        sender: Sender email address
        to: Recipient email address(es)
        subject: Email subject
        body: Plain text body
        cc: CC recipients
        bcc: BCC recipients
        html_body: Optional HTML body
        thread_id: Thread ID for reply drafts

    Returns:
        Dict with draft info
    """
    raw = create_raw_message(
        sender=sender,
        to=to,
        subject=subject,
        body=body,
        cc=cc,
        bcc=bcc,
        html_body=html_body
    )

    message = {'raw': raw}
    if thread_id:
        message['threadId'] = thread_id

    draft_body = {'message': message}

    request = service.users().drafts().create(
        userId='me',
        body=draft_body
    )

    result = retry_with_backoff(request.execute)

    return {
        'id': result.get('id'),
        'message': {
            'id': result.get('message', {}).get('id'),
            'threadId': result.get('message', {}).get('threadId')
        }
    }


def update_draft(
    service,
    draft_id: str,
    sender: str,
    to: str,
    subject: str,
    body: str,
    cc: str = None,
    bcc: str = None,
    html_body: str = None
) -> dict:
    """Update an existing draft.

    Args:
        service: Gmail API service
        draft_id: ID of draft to update
        sender: Sender email address
        to: Recipient email address(es)
        subject: Email subject
        body: Plain text body
        cc: CC recipients
        bcc: BCC recipients
        html_body: Optional HTML body

    Returns:
        Dict with updated draft info
    """
    raw = create_raw_message(
        sender=sender,
        to=to,
        subject=subject,
        body=body,
        cc=cc,
        bcc=bcc,
        html_body=html_body
    )

    draft_body = {'message': {'raw': raw}}

    request = service.users().drafts().update(
        userId='me',
        id=draft_id,
        body=draft_body
    )

    result = retry_with_backoff(request.execute)

    return {
        'id': result.get('id'),
        'message': {
            'id': result.get('message', {}).get('id'),
            'threadId': result.get('message', {}).get('threadId')
        }
    }


def send_draft(service, draft_id: str) -> dict:
    """Send an existing draft.

    Args:
        service: Gmail API service
        draft_id: ID of draft to send

    Returns:
        Dict with sent message info
    """
    request = service.users().drafts().send(
        userId='me',
        body={'id': draft_id}
    )

    result = retry_with_backoff(request.execute)

    return {
        'id': result.get('id'),
        'threadId': result.get('threadId'),
        'labelIds': result.get('labelIds', [])
    }


def get_draft(service, draft_id: str) -> dict:
    """Get a draft by ID.

    Args:
        service: Gmail API service
        draft_id: ID of draft to retrieve

    Returns:
        Dict with draft info
    """
    request = service.users().drafts().get(
        userId='me',
        id=draft_id,
        format='full'
    )

    result = retry_with_backoff(request.execute)

    return {
        'id': result.get('id'),
        'message': result.get('message')
    }


def list_drafts(service, max_results: int = 100) -> dict:
    """List all drafts.

    Args:
        service: Gmail API service
        max_results: Maximum drafts to return

    Returns:
        Dict with drafts list
    """
    request = service.users().drafts().list(
        userId='me',
        maxResults=max_results
    )

    result = retry_with_backoff(request.execute)

    drafts = result.get('drafts', [])
    return {
        'drafts': drafts,
        'count': len(drafts)
    }


def main():
    parser = argparse.ArgumentParser(
        description='Create, update, or send Gmail drafts'
    )
    add_common_args(parser)

    # Draft ID for update/send operations
    parser.add_argument(
        '--draft-id',
        help='Draft ID (for update, send, or get operations)'
    )

    # Actions
    parser.add_argument(
        '--send',
        action='store_true',
        help='Send the draft (requires --draft-id)'
    )
    parser.add_argument(
        '--get',
        action='store_true',
        help='Get draft details (requires --draft-id)'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List all drafts'
    )

    # Message fields (for create/update)
    parser.add_argument(
        '--to',
        help='Recipient email address(es), comma-separated'
    )
    parser.add_argument(
        '--subject',
        help='Email subject'
    )
    parser.add_argument(
        '--body',
        help='Plain text email body'
    )
    parser.add_argument(
        '--cc',
        help='CC recipients, comma-separated'
    )
    parser.add_argument(
        '--bcc',
        help='BCC recipients, comma-separated'
    )
    parser.add_argument(
        '--html',
        help='HTML body (creates multipart message)'
    )
    parser.add_argument(
        '--thread-id',
        help='Thread ID for reply drafts'
    )
    parser.add_argument(
        '--max-results',
        type=int,
        default=100,
        help='Maximum drafts to list (default: 100)'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)

        # Determine operation
        if args.send:
            if not args.draft_id:
                output_error('--draft-id required for --send', 'INVALID_INPUT', exit_code=1)
            result = send_draft(service, args.draft_id)
            output_success({'sent': result})

        elif args.get:
            if not args.draft_id:
                output_error('--draft-id required for --get', 'INVALID_INPUT', exit_code=1)
            result = get_draft(service, args.draft_id)
            output_success({'draft': result})

        elif args.list:
            result = list_drafts(service, max_results=args.max_results)
            output_success(result)

        elif args.draft_id:
            # Update existing draft
            if not all([args.to, args.subject, args.body]):
                output_error('--to, --subject, and --body required for update', 'INVALID_INPUT', exit_code=1)
            result = update_draft(
                service,
                draft_id=args.draft_id,
                sender=args.email,
                to=args.to,
                subject=args.subject,
                body=args.body,
                cc=args.cc,
                bcc=args.bcc,
                html_body=args.html
            )
            output_success({'draft': result, 'action': 'updated'})

        else:
            # Create new draft
            if not all([args.to, args.subject, args.body]):
                output_error('--to, --subject, and --body required for create', 'INVALID_INPUT', exit_code=1)
            result = create_draft(
                service,
                sender=args.email,
                to=args.to,
                subject=args.subject,
                body=args.body,
                cc=args.cc,
                bcc=args.bcc,
                html_body=args.html,
                thread_id=args.thread_id
            )
            output_success({'draft': result, 'action': 'created'})

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
