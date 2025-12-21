# Email Digest Command

Generate an email digest.

**Usage:**
- `/digest` - Prompts for account selection
- `/digest {email}` - Digest for specific account

Use @digest subagent with the selected account.

**Accounts:** Read from `/Users/vic-gini/ProjectsCode/Agents/GoogleAccounts/accounts.json`

**Templates:**
- victor.lang22@gmail.com → `digest-personal.md` (5 categories)
- victor@verifiedmetrics.com → `digest-work.md` (10 categories)
- New accounts → `digest-default.md` (5 generic categories)

**Options:**
- `--days N` - Timeframe (default: 14)
