# Inbox Cleanup Command

Clean up Promotions, Social, and Updates categories.

**Usage:**
- `/cleanup` - Prompts for account and category selection
- `/cleanup {email}` - Cleanup for specific account
- `/cleanup promotions` - Jump to Promotions category

Use @inbox-cleanup subagent.

**Categories:**
- **Promotions** - Marketing emails, deals, newsletters
- **Social** - Facebook, LinkedIn, Twitter notifications
- **Updates** - Receipts, confirmations, statements

**Quick Actions:**
- `keep #` - Skip/keep these senders
- `unsub #` - Unsubscribe from senders
- `delete all` - Delete all in category
- `archive all` - Archive all in category
- `next` - Move to next category

**Batch Syntax:**
- `unsub 1, 3, 5` - Specific senders
- `unsub 1-10` - Range of senders
- `unsub all except 1, 5` - All except specified
