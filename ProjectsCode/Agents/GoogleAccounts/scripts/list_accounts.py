#!/usr/bin/env python3
"""
List all registered Google accounts with their status.

Usage:
    python3 list_accounts.py
    python3 list_accounts.py --json
"""

import argparse
import json
import sys
from pathlib import Path

# Import from shared auth
from auth import load_accounts, check_credentials, get_credentials_path


def format_status(status: dict) -> str:
    """Format credential status for display."""
    if not status['success']:
        return f"ERROR: {status.get('error_type', 'UNKNOWN')}"

    if status.get('valid'):
        return "Valid"
    elif status.get('expired') and status.get('has_refresh_token'):
        return "Expired (can refresh)"
    elif status.get('expired'):
        return "Expired (needs reauth)"
    else:
        return "Invalid"


def main():
    parser = argparse.ArgumentParser(
        description="List all registered Google accounts"
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()

    accounts = load_accounts()

    if not accounts:
        print("No accounts registered.")
        print("\nTo add an account:")
        print("  python3 add_account.py --email your@email.com --client-secrets path/to/client_secret.json")
        sys.exit(0)

    results = []

    for account in accounts:
        email = account['email']
        status = check_credentials(email)

        result = {
            **account,
            'credentials_exist': get_credentials_path(email).exists(),
            'status': status
        }
        results.append(result)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"{'Email':<40} {'Type':<10} {'Status':<25}")
        print("-" * 75)

        for r in results:
            email = r['email']
            acc_type = r.get('type', 'unknown')
            status_str = format_status(r['status'])

            print(f"{email:<40} {acc_type:<10} {status_str:<25}")

        print()
        print(f"Total: {len(results)} accounts")


if __name__ == '__main__':
    main()
