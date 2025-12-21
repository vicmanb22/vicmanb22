#!/usr/bin/env python3
"""
Google OAuth Re-authentication Script

Opens a browser for fresh OAuth authentication and saves new credentials.
Use this when the refresh token has expired or been revoked.

Usage:
    python3 reauth.py --email victor.lang22@gmail.com
    python3 reauth.py --email victor@verifiedmetrics.com
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


CREDENTIALS_DIR = Path.home() / '.google_workspace_mcp' / 'credentials'


def load_existing_credentials(email: str) -> dict:
    """Load existing credentials file to get client_id, client_secret, and scopes."""
    creds_file = CREDENTIALS_DIR / f"{email}.json"

    if not creds_file.exists():
        print(f"Error: No existing credentials found at {creds_file}", file=sys.stderr)
        print("You need to have previously authenticated with this email.", file=sys.stderr)
        print("Run: python3 add_account.py --email {email}", file=sys.stderr)
        sys.exit(1)

    with open(creds_file, 'r') as f:
        return json.load(f)


def backup_credentials(email: str) -> Path:
    """Create a backup of existing credentials."""
    creds_file = CREDENTIALS_DIR / f"{email}.json"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = CREDENTIALS_DIR / f"{email}.backup.{timestamp}.json"

    shutil.copy(creds_file, backup_file)
    print(f"Backed up existing credentials to: {backup_file}")
    return backup_file


def run_oauth_flow(client_id: str, client_secret: str, scopes: list, port: int = 8080) -> Credentials:
    """Run the OAuth flow and return new credentials."""

    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"]
        }
    }

    flow = InstalledAppFlow.from_client_config(client_config, scopes)

    print(f"\nOpening browser for Google authentication...")
    print(f"If the browser doesn't open, visit: http://localhost:{port}")
    print("After authentication, you'll be redirected back.\n")

    creds = flow.run_local_server(
        port=port,
        authorization_prompt_message="Please visit this URL to authorize: {url}",
        success_message="Authentication successful! You can close this tab.",
        open_browser=True
    )

    return creds


def save_credentials(email: str, creds: Credentials, original_data: dict) -> None:
    """Save new credentials back to the credentials file."""
    creds_file = CREDENTIALS_DIR / f"{email}.json"

    new_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": list(creds.scopes) if creds.scopes else original_data.get("scopes", []),
        "expiry": creds.expiry.isoformat() if creds.expiry else None
    }

    with open(creds_file, 'w') as f:
        json.dump(new_data, f, indent=2)

    print(f"\nCredentials saved to: {creds_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Re-authenticate Google OAuth credentials via browser"
    )
    parser.add_argument(
        '--email',
        required=True,
        help='Email address to re-authenticate'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Local port for OAuth callback (default: 8080)'
    )
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='Skip backing up existing credentials'
    )

    args = parser.parse_args()

    print(f"Google OAuth Re-authentication")
    print(f"=" * 40)
    print(f"Email: {args.email}")

    existing = load_existing_credentials(args.email)

    client_id = existing.get('client_id')
    client_secret = existing.get('client_secret')
    scopes = existing.get('scopes', [])

    if not client_id or not client_secret:
        print("Error: Missing client_id or client_secret in credentials file", file=sys.stderr)
        sys.exit(1)

    if not scopes:
        print("Error: No scopes found in credentials file", file=sys.stderr)
        sys.exit(1)

    print(f"Scopes: {len(scopes)} configured")

    if not args.no_backup:
        backup_credentials(args.email)

    try:
        new_creds = run_oauth_flow(client_id, client_secret, scopes, args.port)
    except Exception as e:
        print(f"\nError during OAuth flow: {e}", file=sys.stderr)
        sys.exit(1)

    save_credentials(args.email, new_creds, existing)

    print("\nRe-authentication successful!")
    print(f"  New token expires: {new_creds.expiry}")


if __name__ == '__main__':
    main()
