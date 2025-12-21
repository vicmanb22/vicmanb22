#!/usr/bin/env python3
"""OAuth token management for Google Calendar API scripts.

This module re-exports auth functions from GoogleAccounts.
All authentication logic is centralized in GoogleAccounts/scripts/auth.py.

Usage:
    from auth import get_calendar_service
    service = get_calendar_service('victor@verifiedmetrics.com')
"""

import importlib.util
from pathlib import Path

# Load GoogleAccounts auth module directly to avoid circular import
GOOGLE_ACCOUNTS_AUTH = Path('/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/scripts/auth.py')
spec = importlib.util.spec_from_file_location("google_accounts_auth", GOOGLE_ACCOUNTS_AUTH)
_ga_auth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_ga_auth)

# Import functions from loaded module
get_gmail_service = _ga_auth.get_gmail_service
get_calendar_service = _ga_auth.get_calendar_service
load_credentials = _ga_auth.load_credentials
refresh_if_needed = _ga_auth.refresh_if_needed
save_credentials = _ga_auth.save_credentials
get_credentials_path = _ga_auth.get_credentials_path
check_credentials = _ga_auth.check_credentials
load_accounts = _ga_auth.load_accounts
get_account = _ga_auth.get_account
CREDENTIALS_DIR = _ga_auth.CREDENTIALS_DIR

# Re-export for backward compatibility
__all__ = [
    'get_gmail_service',
    'get_calendar_service',
    'load_credentials',
    'refresh_if_needed',
    'save_credentials',
    'get_credentials_path',
    'check_credentials',
    'load_accounts',
    'get_account',
    'CREDENTIALS_DIR',
]

if __name__ == '__main__':
    # Delegate to GoogleAccounts auth.py for CLI usage
    import subprocess
    import sys
    result = subprocess.run(
        ['python3', str(GOOGLE_ACCOUNTS_AUTH)] + sys.argv[1:],
        capture_output=False
    )
    sys.exit(result.returncode)
