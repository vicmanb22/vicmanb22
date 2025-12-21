---
description: Start a new Daily Anchor session for the Planning Agent
---
1. Create and open the Daily Anchor file
   // turbo
   ```bash
   # Paths
   VAULT_ROOT="/Users/vic-gini/Library/Mobile Documents/com~apple~CloudDocs/Documents/Victor L Obsidian Vault"
   # Confirmed template location
   TEMPLATE="$VAULT_ROOT/_Notes/5. Templates 2/Daily Anchor Template.md"
   TARGET_DIR="$VAULT_ROOT/_Planning/1. Daily Anchor"
   
   # Date logic
   DATE=$(date "+%Y-%m-%d")
   TARGET_FILE="$TARGET_DIR/Daily Anchor - $DATE.md"
   
   # Check if file exists
   if [ -f "$TARGET_FILE" ]; then
       echo "File already exists: $TARGET_FILE"
   else
       # Ensure dir exists
       mkdir -p "$TARGET_DIR"
       # Check if template exists before copying
       if [ ! -f "$TEMPLATE" ]; then
           echo "Error: Template not found at $TEMPLATE"
           exit 1
       fi
       # Copy template
       cp "$TEMPLATE" "$TARGET_FILE"
       echo "Created new Daily Anchor: $TARGET_FILE"
   fi
   
   # Open the file
   open "$TARGET_FILE"
   ```
