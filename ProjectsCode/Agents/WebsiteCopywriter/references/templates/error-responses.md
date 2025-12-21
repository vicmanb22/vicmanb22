# Error Response Templates

Standardized responses for handling common issues and edge cases during website copy creation.

---

## Brand Guidelines Conflict

**When:** Brand guidelines conflict with conversion best practices.

```markdown
I notice the brand guidelines suggest [X], but conversion research indicates [Y] performs better.

Here are three approaches:

**Option A: Brand-First**
[Copy that strictly follows brand guidelines]
*Trade-off: May reduce conversion effectiveness*

**Option B: Conversion-First**
[Copy optimized for conversion, bending guidelines]
*Trade-off: May feel less "on-brand"*

**Option C: Balanced**
[Copy that honors the brand while incorporating the conversion principle]
*Trade-off: Compromise on both fronts*

Which approach fits your priorities? We can also discuss specific elements where you'd flex vs. hold firm.
```

---

## Missing SEO Data

**When:** User cannot provide SEO data (GSC, GA, keyword research).

```markdown
No problem - I can research relevant keywords using current search trends and competitor analysis.

**For this project, I'll:**
1. Research industry-relevant keywords via web search
2. Analyze competitor keyword targeting (if URLs provided)
3. Identify question-based queries people ask in your space
4. Recommend primary and secondary keywords for each page

**For future projects, these free tools can provide valuable data:**
- **Google Search Console** (free) - See what queries bring traffic
- **Google Analytics** (free) - Understand user behavior
- **Ubersuggest** (free tier) - Basic keyword research
- **AnswerThePublic** (limited free) - Question-based queries

**Paid options if you want deeper insights:**
- SEMRush, Ahrefs, or Moz for comprehensive keyword data

Shall I proceed with research-based keyword recommendations?
```

---

## Competitor Sites Inaccessible

**When:** WebFetch fails to analyze competitor URLs.

```markdown
I wasn't able to fully analyze [URL]. This sometimes happens with:
- JavaScript-heavy sites (content loads after page load)
- Sites with bot protection or access restrictions
- Regional restrictions or CDN issues

**I can still help by:**
1. Proceeding with industry best practices research
2. Using any competitive insights you can share manually
3. Analyzing any screenshots or notes you add to `references/competitors/`

**Could you help by:**
- Sharing screenshots of their key pages (homepage, pricing, etc.)?
- Noting their main value proposition and messaging approach?
- Listing what you think they do well vs. poorly?

Add any materials to `[project]/references/competitors/` and I'll incorporate them.
```

---

## Revision Loop Detection

**When:** User has requested 3+ revisions on the same section.

```markdown
We've now refined this section [X] times, and I want to make sure we're making progress toward copy you're happy with.

**Let me check:** Is there a specific element that's still not landing?

- **Headline** - Not capturing the right tone/benefit?
- **Body copy** - Missing something important?
- **CTA** - Not compelling enough?
- **Overall direction** - Need a completely different approach?

**Or** would it help to:
- See this section in context with the next section?
- Move forward and revisit this later with fresh eyes?
- Get input from someone else on your team?

Sometimes stepping back helps clarify what's not clicking. What would be most helpful?
```

---

## Unclear Request

**When:** User's request is ambiguous or lacks necessary detail.

```markdown
I want to make sure I create copy that hits the mark. Could you clarify [specific question]?

**For example:**
- [Provide concrete example of what you need to know]
- [Another example if helpful]

This will help me [explain how the information will be used].
```

---

## Section Skip Request

**When:** User wants to skip a recommended section.

```markdown
We can absolutely skip [section name].

**Just so you know:** This section typically helps with [specific benefit]:
- [Benefit 1]
- [Benefit 2]

**If you'd like to address that goal differently:**
- We could incorporate elements into [another section]
- Or revisit this later if you change your mind

Ready to move to [next section]?
```

---

## Reference Files Not Found

**When:** Expected reference files are missing from the project folder.

```markdown
I couldn't locate [specific reference file] in the project's `references/` folder.

**I'll proceed using:**
- My knowledge of [framework/principle]
- Industry best practices for [topic]
- The information you've provided directly

**To improve future recommendations, you could add:**
- [Specific file type] to `references/[subfolder]/`

For now, here's what I recommend based on available information...
```

---

## Platform Limitation

**When:** Recommended feature isn't supported on the target platform.

```markdown
The feature I recommended ([feature]) isn't natively supported on [platform].

**Here are alternatives that achieve similar conversion goals:**

**Option A: [Alternative approach]**
- How it works: [Explanation]
- Platform support: [Native/Plugin/Custom code]
- Trade-off: [Any limitations]

**Option B: [Another alternative]**
- How it works: [Explanation]
- Platform support: [Native/Plugin/Custom code]
- Trade-off: [Any limitations]

**Option C: [Simplified version]**
- How it works: [Explanation]
- Platform support: Native
- Trade-off: [Less sophisticated but fully supported]

Which approach works best for your implementation?
```

---

## No Social Proof Available

**When:** User has no testimonials, case studies, or logos to display.

```markdown
Social proof is one of the strongest conversion drivers, so let's work with what we have and plan for the future.

**For now, we can use:**
- **Founder story** - Your journey and why you started this
- **Process transparency** - Show how you work
- **Credentials** - Education, certifications, experience
- **Guarantees** - Risk reversal builds trust
- **Specificity** - Detailed descriptions signal expertise

**To build social proof over time:**
1. Ask current customers for testimonials (I can help draft the request)
2. Document results as you get them
3. Request permission to use client logos
4. Create before/after case studies

**For the copy, I'll:**
- Focus on other trust signals
- Create placeholder sections for when social proof becomes available
- Note where adding testimonials later would be highest impact

Shall I proceed with this approach?
```

---

## Incomplete Discovery Information

**When:** User provided partial answers to discovery questions.

```markdown
Thanks for that information! I have enough to get started, but a few gaps would help me create stronger copy:

**Still needed (high impact):**
- [Question] - *This affects [specific copy decisions]*

**Would be helpful:**
- [Question] - *This would strengthen [specific section]*

**I'll proceed with:**
- What you've shared
- Industry best practices for [gaps]
- Assumptions I'll note in the copy

I've added the unanswered questions to your project's `open-questions.md` file. You can provide answers anytime - just tell me or add documents to the `references/` folder.

Ready to start with research?
```

---

## User Wants to Start Writing Before Research

**When:** User wants to skip research and jump to copy creation.

```markdown
I can start writing immediately if you'd like - but a quick research phase (10-15 minutes) typically improves results significantly.

**What research gives us:**
- Keyword targets that balance search volume and competition
- Competitor messaging gaps we can exploit
- Industry-specific best practices
- Framework alignment (which psychological principles fit your audience)

**If you want to skip research:**
- I'll use general best practices
- We may need more revisions to dial in messaging
- SEO optimization will be based on assumptions

**Quick compromise:**
- I do rapid research while you add any reference materials
- We start section work in ~10 minutes with solid foundations

What's your preference?
```

---

## Multiple Stakeholders / Conflicting Feedback

**When:** User mentions they need to get approval from others, or provides conflicting direction.

```markdown
It sounds like there are multiple perspectives to consider here.

**To help navigate this:**

1. **Who has final approval?** Knowing the decision-maker helps prioritize feedback.

2. **Can you share the different viewpoints?** I can create variants that address each perspective.

3. **Are there non-negotiables?** Some elements might be fixed (brand guidelines, legal requirements) while others are flexible.

**I can help by:**
- Creating options that satisfy different stakeholders
- Providing rationale you can share with the team
- Identifying where compromises make sense

Would it help to have a few distinct options to present to the group?
```

---

## Copy Too Long / Too Short

**When:** User feels the copy length is wrong for the section.

```markdown
**If copy feels too long:**

You're right that conciseness often wins - especially on mobile. Let me tighten this:

[Shorter version]

**What I cut:**
- [Removed element and why it was expendable]
- [Another removed element]

The core message is preserved. Does this feel better?

---

**If copy feels too short:**

I can expand this to address more objections or add detail. Here's an enhanced version:

[Longer version]

**What I added:**
- [New element and why it helps]
- [Another addition]

Does this give it the substance you were looking for?
```

---

## User Provides Competitor Copy to "Match"

**When:** User wants copy similar to a competitor's.

```markdown
I can see why you like [competitor]'s approach - [specific thing they do well].

**However, I'd recommend we don't copy their style directly because:**
1. Your brand voice is [different in these ways]
2. Differentiation is key to standing out
3. What works for them may not work for your audience

**Instead, let me:**
- Apply the same *principle* they're using (e.g., specificity, social proof, urgency)
- Adapt it to your unique voice and value proposition
- Make it distinctly yours

Here's how we can capture that same energy while staying original:

[Copy that uses the same principle but is differentiated]

Does this capture what you liked about their approach?
```
