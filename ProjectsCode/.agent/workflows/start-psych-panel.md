---
description: Start a Psychological Panel session with full context access (Profile, Journals, Anchors)
---

1. Find and load the User Profile and Recovery Plan
// turbo
# Find the latest Profile (sort by name/date descending to get the newest)
PROFILE_PATH=$(find "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Private Journal/Other" -name "*Comprehensive Profile of Victor.md" | sort -r | head -n 1)
RECOVERY_PATH=$(find "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Private Journal/Other" -name "Family Recovery Plan.md" | head -n 1)

echo "Loading Context..."
echo "Reading Profile: $PROFILE_PATH"
if [ -f "$PROFILE_PATH" ]; then cat "$PROFILE_PATH"; else echo "No Profile found."; fi

echo "Reading Recovery Plan: $RECOVERY_PATH"
if [ -f "$RECOVERY_PATH" ]; then cat "$RECOVERY_PATH"; else echo "No Recovery Plan found."; fi

2. Find and load the Journals (Current and Previous Month)
// turbo
CURRENT_MONTH=$(date +%B)
PREV_MONTH=$(date -v-1m +%B)
YEAR=$(date +%Y)
PREV_YEAR=$(date -v-1m +%Y)

# Use glob to find the files matching "Journal - YYYY-MM [MonthName].md"
# We use * for the day/wildcard part just in case, though the format is usually Journal - YYYY-MM Month.md
CURRENT_JOURNAL=$(find "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Private Journal/Journals" -name "Journal - $YEAR-* $CURRENT_MONTH.md" | head -n 1)
PREV_JOURNAL=$(find "/Users/vic-gini/Documents/Victor L Obsidian Vault/_Private Journal/Journals" -name "Journal - $PREV_YEAR-* $PREV_MONTH.md" | head -n 1)

echo "Reading Current Journal ($CURRENT_MONTH): $CURRENT_JOURNAL"
if [ -f "$CURRENT_JOURNAL" ]; then cat "$CURRENT_JOURNAL"; else echo "No current journal found."; fi

echo "Reading Previous Journal ($PREV_MONTH): $PREV_JOURNAL"
if [ -f "$PREV_JOURNAL" ]; then cat "$PREV_JOURNAL"; else echo "No previous journal found."; fi

3. Find and load the latest Daily Anchor
// turbo
# Find the latest daily anchor in the _Planning directory
ANCHOR_PATH=$(find "/Users/vic-gini/ProjectsCode/Agents/Planning/_Planning/1. Daily Anchor" -name "Daily Anchor - *.md" | sort -r | head -n 1)
echo "Reading Latest Anchor: $ANCHOR_PATH"
if [ -f "$ANCHOR_PATH" ]; then cat "$ANCHOR_PATH"; else echo "No Daily Anchor found."; fi

4. Initialize the Psychological Panel Prompt
// turbo
PANEL_PROMPT="/Users/vic-gini/ProjectsCode/Agents/My Psychologist/psychology-panel.md"
echo "Initializing Panel Prompt..."
if [ -f "$PANEL_PROMPT" ]; then cat "$PANEL_PROMPT"; else echo "Error: Psychological Panel prompt file not found!"; fi

echo "----------------------------------------------------------------"
echo "Psychological Panel Context Fully Loaded."
echo "I have read:"
echo "- Profile & Recovery Plan"
echo "- Journals ($PREV_MONTH & $CURRENT_MONTH)"
echo "- Latest Daily Anchor"
echo ""
echo "I am ready to analyze with DEPTH and COMPREHENSIVENESS."
echo "How can the panel help you today?"
