# /schedule

Generate a calendar schedule showing upcoming events. **Default: Consolidated view across all accounts.**

## Usage

```
/schedule                      # Consolidated: all accounts, this week
/schedule today                # Consolidated: all accounts, today only
/schedule week                 # Consolidated: all accounts, this week
/schedule month                # Consolidated: all accounts, this month
/schedule --account victor@verifiedmetrics.com  # Single account only
```

## Options

- `today` / `tomorrow` / `week` / `month` - Time range
- `--account {email}` - Show single account only (skips consolidated)
- `--group-by date` - Group by date (default)
- `--group-by account` - Group by account

## Examples

- `/schedule` - Consolidated weekly schedule (default)
- `/schedule today` - All accounts, today only
- `/schedule --account victor.lang22@gmail.com` - Personal account only
