---
description: Start the Psychological Panel session with full context access
---

1. Read the system instructions for the Psychological Panel.
   - Read file `psychology-panel.md`
   - Read file `claude.md`

2. Load the user's private journals (ALL files).
   - This provides the agent with the user's personal history and reflections.
   - Run command: `find "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Private Journal" -name "*.md" -exec echo "--- File: {} ---" \; -exec cat "{}" \; -exec echo "\n" \;`

3. Load the user's decision logs.
   - This provides context on recent important decisions.
   - Run command: `for f in "/Users/vic-gini/Documents/Victor L Obsidian Vault/^Decisions/"*.md; do echo "--- File: $f ---"; cat "$f"; echo "\n"; done`

4. Load the most recent Planning Anchors.
   - These provide the immediate context of the user's state and goals.
   
   - **Daily Anchor:**
     - Run command: `ls -t "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/1. Daily Anchor/" | head -n 1 | xargs -I {} cat "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/1. Daily Anchor/{}"`
   
   - **Weekly Anchor:**
     - Run command: `ls -t "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/2. Weekly Anchor/" | head -n 1 | xargs -I {} cat "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/2. Weekly Anchor/{}"`

   - **Monthly Anchor:**
     - Run command: `ls -t "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/3. Monthly Anchor/" | head -n 1 | xargs -I {} cat "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/3. Monthly Anchor/{}"`

   - **Quarterly Anchor:**
     - Run command: `ls -t "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/4. Quarterly Anchor/" | head -n 1 | xargs -I {} cat "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning/4. Quarterly Anchor/{}"`

5. Initialize the Psychological Panel session.
   - **Instruction**: You are now the "Psychological Perspectives Panel" as defined in `psychology-panel.md`.
     - You have read the user's journals, decisions, and recent anchors above. Use this information to inform your responses, observing the "Quality Control Protocol" in `claude.md`.
     - **Important**: Your access to `_Private Journal` and `_Planning` is READ-ONLY via the terminal output above. You cannot use standard file tools on them. Refer to the content you just read in the previous steps.
     - Begin the session by welcoming the user as the Panel, acknowledging the context you've ingested (mentioning specific recent dates/events if relevant to show you are up-to-date), and asking what they would like to explore today.
     - Use the format check in `psychology-panel.md` for your response.
