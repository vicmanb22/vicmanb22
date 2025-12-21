# Reliability Log

**Agent:** transcript-extractor
**Current Phase:** 1 (LLM-Driven)
**Target Reliability:** 85%+ validation accuracy

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Transcripts Processed | 0 |
| Extractions Validated | 0 |
| Validation Successes | 0 |
| Validation Failures | 0 |
| Success Rate | N/A |

## Phase Quality Gates

- **Phase 1 (20-25 transcripts):** Target 85%+ accuracy on 3-4 samples
- **Phase 2 (15-20 transcripts):** Target 85%+ accuracy on 2-3 samples
- **Phase 3 (15-20 transcripts):** Target 80%+ accuracy on 1-2 samples

## Extraction Log

[Will be populated as extractions are validated]

### Validation Entry Template

```markdown
### [Date] - [Company] - [ICP]
**Outcome:** [Success/Partial/Failure]
**Validation Score:** [X]/7 (85% = 6/7)
**Task Type:** [Phase 1 Discovery/Demo extraction]
**What Happened:** [Description of extraction quality]
**Root Cause:** [If not success - why? Paraphrased quotes? Missing pain points? Incorrect use case tags?]
**Pattern Detected:** [Yes/No - If 3+ similar issues, flag for improvement]
**Extraction Quality Signals:** [High/Medium/Low - Did transcript have quantifications, examples, emotional reactions?]
```

## Detected Patterns

### Failure Patterns

[Will detect after 3+ similar failures]

**Example Failure Pattern:**
```markdown
### Pattern: Paraphrasing Instead of Verbatim Quotes
**Occurrences:** [X] transcripts
**Impact:** Validation failures (quotes not verbatim)
**Root Cause:** LLM tendency to "improve" readability
**Proposed Fix:** Add to system prompt: "CRITICAL: Copy quotes exactly as written, including grammar errors and informal language."
**Status:** [Pending Approval/Implemented]
```

### Success Patterns (Codification Candidates)

[Will detect after 3+ similar successes - candidates for Python scripts]

**Example Success Pattern:**
```markdown
### Pattern: High Accuracy on Discovery Calls with Quantified Metrics
**Occurrences:** [X] transcripts
**Success Rate:** [X]%
**What's Working:** Transcripts where participants volunteer specific numbers are easier to extract accurately
**Codification Opportunity:** Create script to auto-tag quantified metrics (regex for $X, Xk, X weeks, X months)
**Benefit:** Reduce LLM hallucination risk on numeric data
**Status:** [Under Consideration/In Development/Deployed]
```

## Improvement Proposals

### Pending Approval

[None yet]

**Proposal Template:**
```markdown
### [Date] - [Improvement Title]
**Problem:** [What's going wrong]
**Frequency:** [How often - X failures out of Y attempts]
**Proposed Solution:** [How to fix - directive change, prompt refinement, etc.]
**Expected Impact:** [Improvement in accuracy/efficiency]
**Risks:** [Any downsides]
**Status:** Pending Approval
```

### Implemented

[None yet]

**Implementation Template:**
```markdown
### [Date] - [Improvement Title]
**Problem:** [What was going wrong]
**Solution:** [What was changed]
**Results:** [Before vs After accuracy]
**Lessons:** [What we learned]
```

## Phase Transition History

[Will track transitions from Phase 1 (LLM-Driven) to Phase 2 (Code-Driven)]

**Current Phase:** 1 (LLM-Driven)

**Phase 2 Criteria:**
- Extraction workflow has been executed 3+ times with consistent success
- Workflow is repeatable and deterministic
- Cost-benefit analysis supports codification (frequency * time savings > development cost)

**Phase 2 Candidate Workflows:**
- [None identified yet - need to complete Phase 1 first]

## Notes

- Validation sampling strategy: 15% for Phase 1-2, 10% for Phase 3
- Golden Quote criteria: 3 of 4 attributes (Specific, Emotional, Relatable, Actionable)
- High-priority transcripts for human review: DD Debriefs, all 4 Founders transcripts, Unknown ICP/Persona
