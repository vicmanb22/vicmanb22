---
description: Start a new Weekly Plan session for the Planning Agent
---
1. Create and open the Weekly Plan file
   // turbo
   ```bash
   # Paths
   VAULT_ROOT="/Users/vic-gini/Library/Mobile Documents/com~apple~CloudDocs/Documents/Victor L Obsidian Vault"
   # Assuming same template location
   TEMPLATE="$VAULT_ROOT/_Notes/5. Templates 2/Weekly Plan Template.md"
   TARGET_DIR="$VAULT_ROOT/_Planning/2. Weekly Plans"
   
   # Date logic (Week number)
   YEAR=$(date "+%Y")
   WEEK=$(date "+%V")
   TARGET_FILE="$TARGET_DIR/$YEAR Week $WEEK.md"
   
   # Check if file exists
   if [ -f "$TARGET_FILE" ]; then
       echo "File already exists: $TARGET_FILE"
   else
       mkdir -p "$TARGET_DIR"
       if [ ! -f "$TEMPLATE" ]; then
           echo "Error: Template not found at $TEMPLATE"
           exit 1
       fi
       cp "$TEMPLATE" "$TARGET_FILE"
       echo "Created new Weekly Plan: $TARGET_FILE"
   fi
   
   open "$TARGET_FILE"
   ```
