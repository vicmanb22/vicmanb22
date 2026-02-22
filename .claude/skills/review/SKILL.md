# Review Skill

**Purpose:** Structured, interactive code and architecture review with tradeoff analysis and user decision points.

## When to Use

Use this skill when:
- User says `/review`, "review this code", "review this plan"
- User wants a structured evaluation before making changes
- User wants tradeoff analysis on architectural or implementation decisions

**Invocation:**
```
/review
/review <path-to-files-or-directory>
/review <plan-or-document>
```

## Engineering Preferences

Apply these preferences when evaluating code and presenting recommendations:

- **DRY is important** — flag repetition aggressively
- **Well-tested code is non-negotiable** — rather have too many tests than too few
- **"Engineered enough"** — not under-engineered (fragile, hacky) and not over-engineered (premature abstraction, unnecessary complexity)
- **Handle more edge cases, not fewer** — thoughtfulness > speed
- **Explicit over clever** — always

## Workflow

### Phase 1: Scoping

Before any review work, ask the user what to review:

1. **Target scope:** What should I review? Options:
   - Full codebase or project
   - Specific directory or files
   - Recent diff / uncommitted changes
   - A plan or design document

2. **Review type:** Use AskUserQuestion to determine the review type:
   - **Code** — reviewing source code, scripts, or implementation
   - **Document** — reviewing plans, specs, session logs, or directory structures
   - **Architecture** — reviewing system design, data flow, or component boundaries

3. **Review depth:** Use AskUserQuestion to offer:
   - **BIG CHANGE:** Work through interactively, one section at a time, with up to 4 top issues per section
   - **SMALL CHANGE:** Work through interactively, ONE key issue per review section

### Phase 2: Review

Work through each section in order. **Do not skip ahead.** Complete one section, get user feedback, then move to the next.

Use the section definitions matching the selected **review type**:

#### Code Review Sections

**Section 1: Architecture**
Evaluate:
- Overall system design and component boundaries
- Dependency graph and coupling concerns
- Data flow patterns and potential bottlenecks
- Scaling characteristics and single points of failure
- Security architecture (auth, data access, API boundaries)

**Section 2: Code Quality**
Evaluate:
- Code organization and module structure
- DRY violations — be aggressive here
- Error handling patterns and missing edge cases (call these out explicitly)
- Technical debt hotspots
- Areas that are over-engineered or under-engineered relative to engineering preferences above

**Section 3: Tests**
Evaluate:
- Test coverage gaps (unit, integration, e2e)
- Test quality and assertion strength
- Missing edge case coverage — be thorough
- Untested failure modes and error paths

**Section 4: Performance**
Evaluate:
- N+1 queries and database access patterns
- Memory-usage concerns
- Caching opportunities
- Slow or high-complexity code paths

#### Document Review Sections

**Section 1: Structure & Organization**
Evaluate:
- Overall document/directory structure and naming conventions
- Information architecture — is content findable?
- Staleness — are files current or abandoned?
- Duplication — are there redundant or superseded files?

**Section 2: Content Quality**
Evaluate:
- Accuracy and completeness of content
- Consistency of format, terminology, and conventions
- Missing context or ambiguous sections
- DRY violations across documents

**Section 3: Validation & Completeness**
Evaluate:
- Cross-references — do links, paths, and references resolve?
- Status tracking — are statuses accurate and up-to-date?
- Acceptance criteria or checklists — are they complete?
- Superseded content still present alongside current versions

**Section 4: Discoverability & Usability**
Evaluate:
- Can someone find what they need quickly?
- Are indexes, tables of contents, or summaries adequate?
- Naming conventions — do filenames convey content?
- Onboarding — could a new reader navigate without help?

#### Architecture Review Sections

Use the Code Review sections but weight Section 1 (Architecture) heavily and merge Sections 3-4 into a single "Operational Concerns" section covering testability, observability, and performance characteristics.

### Phase 3: Issue Presentation

For **every** specific issue (bug, smell, design concern, or risk):

1. **Number each issue** (Issue 1, Issue 2, etc.) across all sections
2. **Describe the problem concretely** with file and line references
3. **Present 2–3 options** using letters (A, B, C), including "do nothing" where reasonable
4. For each option, specify:
   - Implementation effort
   - Risk
   - Impact on other code
   - Maintenance burden
5. **Give an opinionated recommendation** mapped to engineering preferences, and make the recommended option always the **first option** (Option A)
6. **Use AskUserQuestion** with option labels that clearly identify issue NUMBER and option LETTER (e.g., "1A: Extract shared helper (Rec)", "1B: Do nothing")
7. **After each section**, pause and ask for feedback before moving to the next section

### Phase 4: Findings Persistence

Write findings to a review file as the review progresses:

- **Location:** `in-progress/reviews/review-YYYY-MM-DD-<short-description>.md`
- **Create the file at the start** of Phase 2
- **Update after each section** with findings and user decisions
- **Format:**

```markdown
# Review: <target description>
**Date:** YYYY-MM-DD
**Scope:** <what was reviewed>
**Depth:** BIG CHANGE | SMALL CHANGE

## Architecture
### Issue 1: <title>
**Problem:** <description with file:line references>
**Decision:** Option <letter> — <summary>
**Rationale:** <why this was chosen>

## Code Quality
...

## Summary
- Total issues found: N
- Decisions made: N
- Action items: <list>
```

## Do NOT

- Assume priorities on timeline or scale — ask
- Skip sections or batch multiple sections together
- Present issues without concrete file and line references
- Recommend an option without explaining why it maps to engineering preferences
- Proceed to the next section without user feedback
