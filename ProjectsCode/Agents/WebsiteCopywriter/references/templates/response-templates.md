# Response Templates

Standard response formats for the Website Copywriter agent. Use these templates to ensure consistent, professional output.

---

## New Project Welcome

Use when a user initiates a new website copy project.

```markdown
## Welcome! Let's Create Your Website Copy

I'm your website copywriter agent. I'll help you create high-converting copy, working section by section with multiple options to choose from.

**First, let's set up your project:**

1. What should we name this project? (e.g., "AcmeCorp Website" - I'll create a folder for it)

**Then, tell me about your business:**

2. What is the primary conversion goal? (leads, sales, signups, bookings)
3. What problem does your product/service solve?
4. What makes you different from competitors?

**Your target audience:**

5. Who is your ideal customer?
6. What pain points drive them to seek a solution?
7. What objections might they have?

**Brand & Technical:**

8. Do you have brand guidelines or tone preferences?
9. What platform will this be built on? (Webflow, WordPress, etc.)
10. Is this a new site, redesign, or migration?

**Existing Assets:**

11. Current website URL?
12. Sites you admire (for inspiration)?
13. Existing content to port over? (blogs, SEO, backlinks)
14. SEO data available? (GSC, GA, SEMRush)

**Social Proof:**

15. Testimonials, client logos, awards available?

**Competitors:**

16. Main competitor URLs?

Once I have this info, I'll create your project folder with a `references/` subfolder where you can drop in any additional materials (brand guidelines, content docs, SEO exports, etc.).
```

---

## Returning to Existing Project

Use when continuing work on an existing project.

```markdown
## Welcome Back!

I see we're working on [Project Name]. Let me check the current state:

**Existing copy files:**
- [List of pages in /copy folder with status]

**Recent additions to references:**
- [Any new files in references/ since last session]

**Open questions that would improve copy:**
- [Critical] [Question and why it matters]
- [Important] [Question and why it matters]

**What would you like to work on?**

1. Continue with [next incomplete page]
2. Revise/improve [existing page]
3. Start a new page
4. Answer some open questions
5. Review and update based on new reference materials
6. Something else?
```

---

## Section Copy Presentation

Use when presenting copy options for a section.

```markdown
## [Section Name] - Copy Options

**Target Keywords:** [primary keyword], [secondary keywords]
**Header Level:** [H1/H2/H3]
**Awareness Level:** [Which buyer awareness stage this targets]
**Reference:** Based on [framework/principle] (see `references/[path]`)

---

### Option A: [Strategic Approach Name]

**Headline:**
[Headline copy]

**Subheadline/Body:**
[Body copy]

**CTA:** [Call-to-action text]

**Strategic Reasoning:**
[Why this approach works - psychology, audience fit, brand alignment]

**Best for:** [When to choose this option]

---

### Option B: [Strategic Approach Name]

**Headline:**
[Headline copy]

**Subheadline/Body:**
[Body copy]

**CTA:** [Call-to-action text]

**Strategic Reasoning:**
[Why this approach works - psychology, audience fit, brand alignment]

**Best for:** [When to choose this option]

---

### Option C: [Strategic Approach Name]

**Headline:**
[Headline copy]

**Subheadline/Body:**
[Body copy]

**CTA:** [Call-to-action text]

**Strategic Reasoning:**
[Why this approach works - psychology, audience fit, brand alignment]

**Best for:** [When to choose this option]

---

## Technical Specifications

**Animations:**
- [Entry animation suggestions]
- [Scroll trigger suggestions]

**Interactive Elements:**
- [Hover states, expandables, etc.]

**Mobile Considerations:**
- [Copy length notes]
- [Layout adjustments]

**A/B Testing Candidates:**
- [Element to test]: [Hypothesis]

---

**Which direction resonates most? I can also blend elements from multiple options.**
```

---

## Final Page Delivery

Use when delivering completed page copy.

```markdown
## [Page Name] - Final Copy

**File saved to:** `[path/to/page-name-copy.md]`

---

### SEO Meta Recommendations

**Title Tag:** [60 characters max]
**Meta Description:** [155 characters max]
**Target Keywords:** [keyword list]
**Header Hierarchy:**
- H1: [main headline]
- H2s: [section headers]

---

### Page Content

[Full compiled copy organized by section with headers]

---

### Technical Implementation Notes

**Animations & Interactions:**
[Compiled specs for developers]

**Mobile Adaptations:**
[Any mobile-specific copy or layout notes]

**Form Specifications:**
[If applicable - fields, validation, success messaging]

---

### A/B Testing Recommendations

| Priority | Element | Test Hypothesis |
|----------|---------|-----------------|
| High | [Element] | [Hypothesis] |
| Medium | [Element] | [Hypothesis] |
| Low | [Element] | [Hypothesis] |

---

### Cross-Page Considerations

**Internal Linking:**
[Suggested links to other pages]

**Messaging Consistency:**
[Notes on alignment with other pages]

**Next Steps:**
[Recommended follow-up work]

---

**Remember:** You can invoke me anytime to continue working on this project, add new pages, or revise existing copy.
```

---

## Research Summary

Use after completing research phase.

```markdown
## Research Complete - Strategic Recommendations

### Key Insights

**From Agent Knowledge Base:**
- [Relevant framework insights]
- [Best practices that apply]

**From Project References:**
- [Brand guidelines considerations]
- [SEO opportunities identified]

**From Competitor Analysis:**
- [What competitors do well]
- [Gaps and opportunities]

**From Industry Research:**
- [Industry-specific best practices]
- [Trends to consider]

### Recommended Page Structure

Based on research, I recommend this section order for [page type]:

1. **[Section]** - [Why it goes here]
2. **[Section]** - [Why it goes here]
3. **[Section]** - [Why it goes here]
...

### Keyword Strategy

**Primary Keywords:**
- [Keyword] (volume: X, difficulty: Y)

**Secondary Keywords:**
- [Keyword list]

**Competitor Gaps:**
- [Underserved terms to target]

### Ready to Begin?

Shall I start with the [first section]? I'll present 2-3 options with different strategic approaches.
```

---

## Project Setup Confirmation

Use after creating project folder structure.

```markdown
## Project Created: [Project Name]

I've set up your project folder at:
`/Users/vic-gini/ProjectsCode/Projects/[ProjectName]/`

**Folder Structure:**
```
[ProjectName]/
├── copy/                    # Your approved copy files will go here
├── references/
│   ├── brand/              # Add brand guidelines, style guides
│   ├── content/            # Add existing content to reference
│   ├── competitors/        # Add competitor URLs, notes
│   ├── seo/                # Add keyword data, analytics exports
│   └── README.md           # Instructions for adding materials
├── README.md               # Project overview
└── open-questions.md       # I'll track unanswered questions here
```

**Next Steps:**

1. **Add reference materials** (optional but helpful):
   - Drop any brand guidelines into `references/brand/`
   - Add SEO data to `references/seo/`
   - Include competitor URLs in `references/competitors/`

2. **Ready to start?**
   - I'll begin with research, then we'll work through sections one by one
   - Each section will have 2-3 options to choose from

Let me know when you're ready, or if you need to add materials first!
```

---

## Revision Request Response

Use when user requests changes to presented copy.

```markdown
## Revision: [Section Name]

**Your feedback:** [Summarize what they asked for]

**Changes made:**
- [Change 1]
- [Change 2]

---

### Updated Option [X]

**Headline:**
[Revised headline]

**Subheadline/Body:**
[Revised body copy]

**CTA:** [Revised CTA]

**What changed:**
[Brief explanation of how revisions address feedback]

---

Does this better capture what you're looking for? [If this is revision 3+, add: "We've refined this section a few times now - shall we finalize and move to the next section, or is there a specific element that still isn't working?"]
```

---

## Open Questions Update

Use when updating the open-questions.md file.

```markdown
## Open Questions Updated

I've added the following to your project's `open-questions.md`:

**Critical (blocking progress):**
- [Question] - *Why it matters: [explanation]*

**Important (would significantly improve copy):**
- [Question] - *Why it matters: [explanation]*

**Nice to Have:**
- [Question] - *Why it matters: [explanation]*

You can answer these anytime by:
1. Telling me directly in our conversation
2. Adding documents to the `references/` folder
3. Editing the `open-questions.md` file directly

I'll proceed with [what you can do with available info] and incorporate answers as you provide them.
```

---

## Session Wrap-Up

Use when ending a work session.

```markdown
## Session Summary

**What we accomplished:**
- [Completed items]

**Current state:**
- [Page]: [Status - complete/in progress/not started]
- [Page]: [Status]

**Saved files:**
- `[path/to/file1.md]`
- `[path/to/file2.md]`

**Still needed:**
- [Outstanding items]
- [Open questions that would help]

**To continue:**
Just invoke me again and I'll pick up where we left off. I'll automatically check for any new materials you've added to the `references/` folder.
```
