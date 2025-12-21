# Start FileOrganizer Session

Run this at the beginning of each file organization session.

## Steps

1. **Load context**
   - Read action-log.md to see recent operations
   - Read reliability-log.md to see success patterns

2. **Check for manual corrections**
   - Verify last 10 organized files are still at logged destinations
   - Report any files that were moved by user after organization

3. **Report findings**
   ```
   ## Session Start - [Date]

   **Recent Activity:**
   - Last session: [date] - [outcome]
   - Files organized recently: [count]

   **Correction Check:**
   - Files verified: [count]
   - Manual corrections detected: [count]

   [If corrections found:]
   | File | I Put It | You Moved To | Suggested Learning |
   |------|----------|--------------|-------------------|

   **Ready to organize. What would you like to work on?**
   ```

4. **Update reliability log** if corrections found
