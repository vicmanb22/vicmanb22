#!/usr/bin/env python3
"""
Google Calendar OAuth Re-authentication Script

This script delegates to GoogleAccounts/scripts/reauth.py.
All re-authentication logic is centralized there.

Usage:
    python3 reauth.py --email victor.lang22@gmail.com
"""

import subprocess
import sys
from pathlib import Path

GOOGLE_ACCOUNTS_REAUTH = Path('/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/scripts/reauth.py')

if __name__ == '__main__':
    result = subprocess.run(
        ['python3', str(GOOGLE_ACCOUNTS_REAUTH)] + sys.argv[1:],
        capture_output=False
    )
    sys.exit(result.returncode)
