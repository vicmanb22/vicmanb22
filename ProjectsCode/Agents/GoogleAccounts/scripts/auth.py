#!/usr/bin/env python3
"""Shared OAuth token management for Google APIs.

This is the central auth library used by Email and Calendar agents.
Loads and refreshes OAuth tokens from the credentials directory.

Usage:
    # Import in other agent scripts:
    import sys
    sys.path.insert(0, '/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/scripts')
    from auth import get_gmail_service, get_calendar_service

    # Or run directly to check credentials:
    python3 auth.py --email victor@verifiedmetrics.com
    python3 auth.py --email victor@verifiedmetrics.com --show-path
"""

# Suppress warnings before any other imports
import warnings
warnings.filterwarnings('ignore')

import argparse
import json
import logging
import sys
from pathlib import Path

# Suppress Google API discovery cache warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# Credentials directory - shared with Google Workspace MCP
CREDENTIALS_DIR = Path.home() / '.google_workspace_mcp' / 'credentials'

# Accounts registry
ACCOUNTS_FILE = Path(__file__).parent.parent / 'accounts.json'


def get_credentials_path(email: str) -> Path:
    """Get the path to the credentials file for an email address."""
    return CREDENTIALS_DIR / f'{email}.json'


def load_accounts() -> list:
    """Load the accounts registry."""
    if not ACCOUNTS_FILE.exists():
        return []
    with open(ACCOUNTS_FILE, 'r') as f:
        data = json.load(f)
    return data.get('accounts', [])


def get_account(email: str):
    """Get account info from registry."""
    accounts = load_accounts()
    for account in accounts:
        if account['email'] == email:
            return account
    return None


def load_credentials(email: str) -> Credentials:
    """Load OAuth credentials for the specified email.

    Args:
        email: Google account email address

    Returns:
        Google OAuth Credentials object

    Raises:
        FileNotFoundError: If credentials file doesn't exist
        ValueError: If credentials file is invalid
    """
    creds_path = get_credentials_path(email)

    if not creds_path.exists():
        raise FileNotFoundError(
            f"Credentials not found for {email}. "
            f"Expected at: {creds_path}\n"
            f"Run: python3 add_account.py --email {email}"
        )

    with open(creds_path, 'r') as f:
        creds_data = json.load(f)

    creds = Credentials(
        token=creds_data.get('token'),
        refresh_token=creds_data.get('refresh_token'),
        token_uri=creds_data.get('token_uri', 'https://oauth2.googleapis.com/token'),
        client_id=creds_data.get('client_id'),
        client_secret=creds_data.get('client_secret'),
        scopes=creds_data.get('scopes', [])
    )

    return creds


def refresh_if_needed(creds: Credentials, email: str) -> Credentials:
    """Refresh credentials if expired.

    Args:
        creds: Credentials object
        email: Email for saving refreshed credentials

    Returns:
        Valid (possibly refreshed) credentials
    """
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            save_credentials(email, creds)

    return creds


def save_credentials(email: str, creds: Credentials) -> None:
    """Save refreshed credentials back to file.

    Args:
        email: Google account email address
        creds: Credentials object to save
    """
    creds_path = get_credentials_path(email)

    # Load existing data to preserve extra fields
    with open(creds_path, 'r') as f:
        creds_data = json.load(f)

    # Update with refreshed values
    creds_data['token'] = creds.token
    if creds.expiry:
        creds_data['expiry'] = creds.expiry.isoformat()

    with open(creds_path, 'w') as f:
        json.dump(creds_data, f, indent=2)


def get_gmail_service(email: str):
    """Get an authenticated Gmail API service.

    Args:
        email: Google account email address

    Returns:
        Gmail API service object
    """
    # Suppress stdout during import (googleapiclient prints error message on Python 3.9)
    import io
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        from googleapiclient.discovery import build
    finally:
        sys.stdout = old_stdout

    creds = load_credentials(email)
    creds = refresh_if_needed(creds, email)

    return build('gmail', 'v1', credentials=creds)


def get_calendar_service(email: str):
    """Get an authenticated Google Calendar API service.

    Args:
        email: Google account email address

    Returns:
        Calendar API service object
    """
    # Suppress stdout during import (googleapiclient prints error message on Python 3.9)
    import io
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        from googleapiclient.discovery import build
    finally:
        sys.stdout = old_stdout

    creds = load_credentials(email)
    creds = refresh_if_needed(creds, email)

    return build('calendar', 'v3', credentials=creds)


def check_credentials(email: str) -> dict:
    """Check the status of credentials for an email.

    Returns:
        dict with success, valid, expired, has_refresh_token, scopes, etc.
    """
    creds_path = get_credentials_path(email)

    if not creds_path.exists():
        return {
            'success': False,
            'error': f'Credentials not found at {creds_path}',
            'error_type': 'CREDENTIALS_NOT_FOUND'
        }

    try:
        creds = load_credentials(email)
        return {
            'success': True,
            'email': email,
            'valid': creds.valid,
            'expired': creds.expired if hasattr(creds, 'expired') else None,
            'has_refresh_token': bool(creds.refresh_token),
            'scopes': list(creds.scopes) if creds.scopes else [],
            'expiry': creds.expiry.isoformat() if creds.expiry else None
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': 'LOAD_ERROR'
        }


def main():
    parser = argparse.ArgumentParser(
        description='Validate and refresh Google OAuth credentials'
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Google account email address'
    )
    parser.add_argument(
        '--show-path',
        action='store_true',
        help='Show the credentials file path'
    )

    args = parser.parse_args()

    try:
        creds_path = get_credentials_path(args.email)

        if args.show_path:
            result = {
                'success': True,
                'email': args.email,
                'credentials_path': str(creds_path),
                'exists': creds_path.exists()
            }
            print(json.dumps(result, indent=2))
            sys.exit(0)

        # Load and validate credentials
        creds = load_credentials(args.email)

        # Check if refresh is needed
        was_expired = not creds.valid
        creds = refresh_if_needed(creds, args.email)

        result = {
            'success': True,
            'email': args.email,
            'token_valid': creds.valid,
            'was_refreshed': was_expired and creds.valid,
            'scopes': list(creds.scopes) if creds.scopes else []
        }

        if creds.expiry:
            result['expires_at'] = creds.expiry.isoformat()

        print(json.dumps(result, indent=2))
        sys.exit(0)

    except FileNotFoundError as e:
        result = {
            'success': False,
            'error': str(e),
            'error_type': 'CREDENTIALS_NOT_FOUND'
        }
        print(json.dumps(result, indent=2))
        sys.exit(3)

    except Exception as e:
        result = {
            'success': False,
            'error': str(e),
            'error_type': 'AUTH_ERROR'
        }
        print(json.dumps(result, indent=2))
        sys.exit(3)


if __name__ == '__main__':
    main()
