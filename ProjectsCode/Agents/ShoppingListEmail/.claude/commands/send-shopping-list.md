# Send Shopping List to Belinda

Read Victor's shopping list and send it to Belinda via email.

1. Read the shopping list from: `/Users/vic-gini/Documents/Victor L Obsidian Vault/Shopping list.md`

2. Parse all unpurchased items (lines with `- [ ]`) and group by category (`## Heading`)

3. Format an email:
   - **To:** belinda@argonautexpeditions.com
   - **From:** victor.lang22@gmail.com
   - **Subject:** "Vic Shopping List - Week of [MMM d, YYYY]" (use today's date)

4. Email body format:
```
Date: [Today's date]

Hi Belinda,

Here's my shopping list for this week:

[List all unpurchased items grouped by category]

---

## Standing Instructions

1. Don't buy fresh food, meat, vegetables, fruit (I'll buy these myself) unless specifically noted
2. Please get my permission before spending more than $500 HKD on any single item
3. Where possible, use my accounts which have credit cards saved - iHerb, HKTVMall, Amazon. Taobao may not be possible due to 2 Factor Authentication.
4. For items with quality variation, please ask before buying - I prefer higher quality items that last, especially for health-related items (food-grade, plastics, cookware with heat/food contact)
5. Don't buy the cheapest option - aim for quality at reasonable price
6. You will be reimbursed for any purchases you make on my behalf using your own credit card

---

Please reply with:
- Questions or options for items needing clarification
- What was purchased with details (store, date, price)

Thanks!
Victor
```

5. Show me a preview of the email and ask for confirmation before sending

6. After I confirm, send the email using `mcp__gmail-workspace__send_gmail_message`
