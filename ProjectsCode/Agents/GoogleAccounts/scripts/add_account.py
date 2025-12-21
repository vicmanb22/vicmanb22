#!/usr/bin/env python3
"""
Add a new Google account via OAuth flow.

This script performs the initial OAuth authentication for a new Google account
and saves the credentials. It also adds the account to the registry.

Usage:
    python3 add_account.py --email new.account@gmail.com --type personal
    python3 add_account.py --email work@company.com --type work --label "Work Account"

Prerequisites:
    You need a Google Cloud OAuth client credentials file (client_secret.json).
    This can be obtained from the Google Cloud Console.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow


CREDENTIALS_DIR = Path.home() / '.google_workspace_mcp' / 'credentials'
ACCOUNTS_FILE = Path(__file__).parent.parent / 'accounts.json'

# Default scopes for Gmail and Calendar
DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events'
]


def load_accounts() -> dict:
    """Load the accounts registry."""
    if not ACCOUNTS_FILE.exists():
        return {"accounts": []}
    with open(ACCOUNTS_FILE, 'r') as f:
        return json.load(f)


def save_accounts(data: dict) -> None:
    """Save the accounts registry."""
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def add_to_registry(email: str, account_type: str, label: str, services: list) -> None:
    """Add account to the registry."""
    data = load_accounts()

    # Check if already exists
    for account in data['accounts']:
        if account['email'] == email:
            print(f"Account {email} already in registry, updating...")
            account['type'] = account_type
            account['label'] = label
            account['services'] = services
            save_accounts(data)
            return

    # Add new account
    data['accounts'].append({
        'email': email,
        'type': account_type,
        'label': label,
        'services': services,
        'added': datetime.now().strftime('%Y-%m-%d')
    })
    save_accounts(data)
    print(f"Added {email} to registry")


def run_oauth_flow(client_secrets_file: str, scopes: list, port: int = 8080):
    """Run OAuth flow with client secrets file."""

    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)

    print(f"\nOpening browser for Google authentication...")
    print(f"If the browser doesn't open, visit: http://localhost:{port}")
    print("After authentication, you'll be redirected back.\n")

    creds = flow.run_local_server(
        port=port,
        authorization_prompt_message="Please visit this URL to authorize: {url}",
        success_message="Authentication successful! You can close this tab.",
        open_browser=True
    )

    return creds, flow.client_config


def save_credentials(email: str, creds, client_config: dict) -> None:
    """Save credentials to file."""
    CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
    creds_file = CREDENTIALS_DIR / f"{email}.json"

    # Extract client info from config
    client_info = client_config.get('installed', client_config.get('web', {}))

    creds_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": client_info.get('client_id'),
        "client_secret": client_info.get('client_secret'),
        "scopes": list(creds.scopes) if creds.scopes else [],
        "expiry": creds.expiry.isoformat() if creds.expiry else None
    }

    with open(creds_file, 'w') as f:
        json.dump(creds_data, f, indent=2)

    print(f"Credentials saved to: {creds_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Add a new Google account via OAuth"
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Email address of the account to add'
    )
    parser.add_argument(
        '--type',
        choices=['personal', 'work'],
        default='personal',
        help='Account type (default: personal)'
    )
    parser.add_argument(
        '--label',
        help='Human-readable label for the account'
    )
    parser.add_argument(
        '--client-secrets',
        required=True,
        help='Path to client_secret.json from Google Cloud Console'
    )
    parser.add_argument(
        '--services',
        nargs='+',
        default=['gmail', 'calendar'],
        help='Services to enable (default: gmail calendar)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Local port for OAuth callback (default: 8080)'
    )

    args = parser.parse_args()

    # Check client secrets file exists
    if not Path(args.client_secrets).exists():
        print(f"Error: Client secrets file not found: {args.client_secrets}", file=sys.stderr)
        print("\nTo get this file:")
        print("1. Go to Google Cloud Console > APIs & Services > Credentials")
        print("2. Create an OAuth 2.0 Client ID (Desktop app)")
        print("3. Download the JSON file")
        sys.exit(1)

    label = args.label or args.email

    print(f"Add Google Account")
    print(f"=" * 40)
    print(f"Email: {args.email}")
    print(f"Type: {args.type}")
    print(f"Label: {label}")
    print(f"Services: {', '.join(args.services)}")

    try:
        creds, client_config = run_oauth_flow(args.client_secrets, DEFAULT_SCOPES, args.port)
    except Exception as e:
        print(f"\nError during OAuth flow: {e}", file=sys.stderr)
        sys.exit(1)

    save_credentials(args.email, creds, client_config)
    add_to_registry(args.email, args.type, label, args.services)

    print(f"\nAccount added successfully!")
    print(f"  Token expires: {creds.expiry}")


if __name__ == '__main__':
    main()
