# Process Shopping Replies from Belinda

Search Gmail for Belinda's replies and update the shopping list with purchased items.

1. Search Gmail for recent emails from Belinda:
   - Query: `from:belinda@argonautexpeditions.com newer_than:14d`
   - Use `mcp__gmail-workspace__search_gmail_messages` then `mcp__gmail-workspace__get_gmail_message_content`

2. Read each email and look for purchase confirmations:
   - Patterns: "Purchased [item]", "Bought [item]", "Got [item]", "[item] done"
   - Extract: item name, store, date, price (if mentioned)

3. Read the current shopping list from: `/Users/vic-gini/Documents/Victor L Obsidian Vault/Shopping list.md`

4. Match Belinda's confirmations to unpurchased items (`- [ ]`)

5. Show me what was found:
   - List each detected purchase with details
   - Ask me to confirm which items to mark as purchased

6. After I confirm, update the shopping list:
   - Change `- [ ]` to `- [x]`
   - Add note after item: ` - Purchased from [Store], [Date] [Belinda]`
   - Move the completed item to the `## Completed` section at the bottom

7. Report summary of changes made
