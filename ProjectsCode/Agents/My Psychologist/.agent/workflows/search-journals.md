---
description: Search for specific topics across private journals, anchors, and decisions
---

1. Execute the search command.
   - **Instruction**: Run the following grep command to search for the query provided by the user or agent.
   - Replace `{{query}}` with the search term.
   - The command searches:
     - `_Private Journal` (Recursive)
     - `^Decisions`
     - `_Planning` (Recursive)
   - Run command: `grep -r "{{query}}" "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Private Journal" "/Users/vic-gini/Documents/Victor L Obsidian Vault/^Decisions" "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Planning"`
