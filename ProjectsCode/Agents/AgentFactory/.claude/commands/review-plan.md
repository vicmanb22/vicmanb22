# Review Plan

Review a plan or design using the "My Developer" technique to get unbiased, critical feedback.

## Usage

```
/review-plan
```

Then paste or describe the plan you want reviewed.

## Instructions

You are about to review a plan that "my developer" created. Your job is to provide honest, critical feedback as if you're protecting me from a potentially flawed plan.

**Do NOT:**
- Be overly positive or validating
- Say things like "Great job!" or "This looks good overall"
- Assume the plan is correct

**DO:**
- Look for weaknesses, gaps, and potential issues
- Question assumptions
- Identify risks and edge cases
- Suggest concrete improvements
- Be direct and specific

## Review Framework

When the user provides a plan, analyze it using these lenses:

### 1. Completeness
- Are there missing steps?
- Are edge cases handled?
- Is error handling addressed?

### 2. Complexity
- Is this over-engineered?
- Could it be simpler?
- Are there unnecessary abstractions?

### 3. Risk
- What could go wrong?
- What are the biggest failure modes?
- Is there a rollback plan?

### 4. Clarity
- Would another developer understand this?
- Are the steps actionable?
- Are there ambiguous terms?

### 5. Assumptions
- What assumptions is this plan making?
- Are those assumptions valid?
- What happens if they're wrong?

## Response Format

```
## Critical Review

### Summary
[One sentence assessment - be honest, not flattering]

### Major Concerns
1. [Concern 1 - specific and actionable]
2. [Concern 2 - specific and actionable]

### Minor Issues
- [Issue 1]
- [Issue 2]

### Missing Elements
- [What's not addressed that should be]

### Recommendations
1. [Specific change to make]
2. [Specific change to make]

### Verdict
[Should this plan proceed as-is, be revised, or be reconsidered entirely?]
```

## Example

**User:** "My developer's plan for adding user authentication: 1) Add login form 2) Store passwords in database 3) Create session on login"

**Response:**
```
## Critical Review

### Summary
This plan has a critical security flaw and lacks essential details.

### Major Concerns
1. **Storing passwords directly** - Passwords must be hashed (bcrypt, argon2), never stored in plain text. This is a dealbreaker.
2. **No logout mechanism** - How do sessions end?
3. **No password requirements** - What makes a valid password?

### Minor Issues
- No mention of "forgot password" flow
- No rate limiting for login attempts
- No session expiration defined

### Missing Elements
- HTTPS requirement
- CSRF protection
- Password hashing algorithm choice
- Session storage mechanism (cookies, tokens?)

### Recommendations
1. Add password hashing with bcrypt before storing
2. Define session expiration and refresh logic
3. Add rate limiting (e.g., 5 attempts per minute)
4. Specify CSRF token implementation

### Verdict
**Revise before proceeding.** The password storage issue is a blocker.
```
