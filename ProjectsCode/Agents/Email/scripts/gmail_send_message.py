#!/usr/bin/env python3
"""Send an email via Gmail API.

New capability (not in MCP - was denied).

Usage:
    python3 gmail_send_message.py --email victor.lang22@gmail.com --to "recipient@example.com" --subject "Hello" --body "Message body"
    python3 gmail_send_message.py --email victor.lang22@gmail.com --to "a@x.com" --cc "b@x.com" --subject "Hi" --body "Text" --html "<p>HTML</p>"
    python3 gmail_send_message.py --email victor.lang22@gmail.com --to "a@x.com" --subject "Re: Thread" --body "Reply" --thread-id "abc123" --in-reply-to "<msgid>"
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


def create_message(
    sender: str,
    to: str,
    subject: str,
    body: str,
    cc: str = None,
    bcc: str = None,
    html_body: str = None,
    in_reply_to: str = None,
    references: str = None
) -> str:
    """Create a base64url encoded email message.

    Args:
        sender: Sender email address
        to: Recipient email address(es), comma-separated
        subject: Email subject
        body: Plain text body
        cc: CC recipients, comma-separated
        bcc: BCC recipients, comma-separated
        html_body: Optional HTML body (creates multipart/alternative)
        in_reply_to: Message-ID being replied to
        references: References header for threading

    Returns:
        Base64url encoded message string
    """
    if html_body:
        # Create multipart message with both plain and HTML
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))
    else:
        # Simple plain text message
        msg = EmailMessage()
        msg.set_content(body)

    msg['To'] = to
    msg['From'] = sender
    msg['Subject'] = subject

    if cc:
        msg['Cc'] = cc
    if bcc:
        msg['Bcc'] = bcc
    if in_reply_to:
        msg['In-Reply-To'] = in_reply_to
    if references:
        msg['References'] = references

    # Encode as base64url
    if html_body:
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    else:
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    return raw


def send_message(
    service,
    sender: str,
    to: str,
    subject: str,
    body: str,
    cc: str = None,
    bcc: str = None,
    html_body: str = None,
    thread_id: str = None,
    in_reply_to: str = None,
    references: str = None
) -> dict:
    """Send an email message.

    Args:
        service: Gmail API service
        sender: Sender email address
        to: Recipient email address(es)
        subject: Email subject
        body: Plain text body
        cc: CC recipients
        bcc: BCC recipients
        html_body: Optional HTML body
        thread_id: Thread ID for replies
        in_reply_to: Message-ID being replied to
        references: References header for threading

    Returns:
        Dict with sent message info
    """
    raw = create_message(
        sender=sender,
        to=to,
        subject=subject,
        body=body,
        cc=cc,
        bcc=bcc,
        html_body=html_body,
        in_reply_to=in_reply_to,
        references=references
    )

    message_body = {'raw': raw}
    if thread_id:
        message_body['threadId'] = thread_id

    request = service.users().messages().send(
        userId='me',
        body=message_body
    )

    result = retry_with_backoff(request.execute)

    return {
        'id': result.get('id'),
        'threadId': result.get('threadId'),
        'labelIds': result.get('labelIds', [])
    }


def main():
    parser = argparse.ArgumentParser(
        description='Send an email via Gmail'
    )
    add_common_args(parser)
    parser.add_argument(
        '--to',
        required=True,
        help='Recipient email address(es), comma-separated'
    )
    parser.add_argument(
        '--subject',
        required=True,
        help='Email subject'
    )
    parser.add_argument(
        '--body',
        required=True,
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
        help='Thread ID for replies'
    )
    parser.add_argument(
        '--in-reply-to',
        help='Message-ID being replied to'
    )
    parser.add_argument(
        '--references',
        help='References header for threading'
    )

    args = parser.parse_args()

    try:
        service = get_gmail_service(args.email)
        result = send_message(
            service,
            sender=args.email,
            to=args.to,
            subject=args.subject,
            body=args.body,
            cc=args.cc,
            bcc=args.bcc,
            html_body=args.html,
            thread_id=args.thread_id,
            in_reply_to=args.in_reply_to,
            references=args.references
        )
        output_success({'message': result})

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
