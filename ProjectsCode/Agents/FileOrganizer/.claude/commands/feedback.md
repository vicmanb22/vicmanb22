---
description: Provide feedback on agent actions or Hazel rule effectiveness
---

# Feedback

Provide feedback on file organization actions, Hazel rules, or naming decisions.

## Usage

```
/feedback
/feedback --last-action
/feedback --hazel-rule "Auto-organize Invoices"
/feedback --review-corrections
```

## Feedback Types

### 1. Action Feedback
Rate and comment on recent agent actions.

```
/feedback --last-action
```

**Prompts:**
- Was the action correct? (Yes / Partially / No)
- What was wrong? (Wrong category / Wrong entity / Wrong date / Wrong destination / Other)
- What should have happened instead?

### 2. Hazel Rule Feedback
Report issues with Hazel rules that are too liberal or incorrect.

```
/feedback --hazel-rule "Rule Name"
```

**Common issues:**
- Rule is too liberal (catches files it shouldn't)
- Rule is too strict (misses files it should catch)
- Rename pattern is wrong
- Destination folder is wrong

### 3. Correction Review
Review manual corrections you made after agent/Hazel actions.

```
/feedback --review-corrections
```

This triggers the manual move detection system (see below).

## Feedback Logging

All feedback is logged to `reliability-log.md`:

```markdown
### YYYY-MM-DD - Feedback: [Type]

**Related Action:** [Original action from action-log]
**Feedback:** [Correct/Partially Correct/Incorrect]
**Issue:** [Description of what was wrong]
**Correction:** [What should have happened]
**Pattern Detected:** [Yes/No]
**Proposed Fix:** [If pattern detected, what to change]
```

## Hazel Rule Adjustment

When feedback indicates a Hazel rule is problematic:

1. **Log the issue** in `hazel-rules-reference.md`
2. **Propose adjustment:**
   - Add exclusion condition
   - Tighten name matching
   - Add confirmation step
3. **Wait for user direction** before modifying

### Example: Too Liberal Rule

**User feedback:** "The invoice rule is catching expense reports too"

**Proposed fix:**
```
Current condition: Name contains "invoice"
Proposed condition: Name contains "invoice" AND NOT name contains "expense"
```

## Output Format

```
## Feedback Recorded

**Action:** [Description]
**Your Rating:** [Correct/Partially/Incorrect]
**Issue:** [What was wrong]

### Analysis

Based on your feedback, I've identified:
- **Pattern:** [If this is a recurring issue]
- **Root cause:** [Why this happened]

### Proposed Changes

1. [Specific change to agent behavior or Hazel rule]

**Would you like me to implement this change?**
```
