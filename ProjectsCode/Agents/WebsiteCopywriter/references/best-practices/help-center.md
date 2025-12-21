# Help Center & Documentation Copy Best Practices

Guidelines for writing help center articles, knowledge base content, and support documentation that ranks in search and AI answer engines.

**Related References:**
- AEO deep dive: `references/interviews/aeo-guide-ethan-smith-jeanne-dewitt-grosser.md` (Part 6)
- Accessibility: `references/best-practices/accessibility.md`
- SEO checklist: `references/best-practices/seo-checklist.md`
- Wes Kao's frameworks: `references/interviews/wes-kao-website-copy-communication-guide.md`

---

## Why Help Centers Matter

1. **AEO goldmine:** Help centers answer the exact questions buyers ask LLMs
2. **Long-tail SEO:** Capture specific, high-intent queries
3. **Reduced support load:** Self-service deflects tickets
4. **Trust building:** Comprehensive docs signal product maturity
5. **Conversion support:** Prospects research before buying

---

## Structure Principles

### URL Structure

**Research Foundation:** Subdomains perform worse than subdirectories for SEO/AEO. (Source: Ethan Smith, Graphite)

| Structure | Example | Recommendation |
|-----------|---------|----------------|
| Subdomain | help.yoursite.com | ❌ Avoid |
| Subdirectory | yoursite.com/help/ | ✓ Preferred |
| Deep subdirectory | yoursite.com/docs/help/ | ✓ Acceptable |

### Information Architecture

```
/help/
├── getting-started/
│   ├── quick-start/
│   ├── first-steps/
│   └── common-setup-issues/
├── features/
│   ├── [feature-name]/
│   └── [feature-name]/
├── integrations/
│   ├── [integration-name]/
│   └── [integration-name]/
├── troubleshooting/
│   ├── error-messages/
│   └── common-issues/
├── billing/
└── faq/
```

---

## Article Structure

### Apply Wes Kao's Frameworks

Use these frameworks from `references/interviews/wes-kao-website-copy-communication-guide.md`:

1. **Bottom Line Up Front:** Answer first, explain later
2. **Start Before the Bear:** Skip preamble, jump to solution
3. **Super-Specific How:** Detailed steps, not concepts

### Standard Article Template

```markdown
# [How to / Fix / Troubleshoot] [Specific Task]

[1-2 sentence summary of what this article covers and the solution]

## Quick Answer
[The answer in 1-3 sentences for scanners]

## Step-by-Step Instructions

### Step 1: [Action]
[Instructions with screenshot if applicable]

### Step 2: [Action]
[Instructions]

### Step 3: [Action]
[Instructions]

## Troubleshooting

### If [problem], try:
- [Solution 1]
- [Solution 2]

### Still stuck?
[Contact support CTA or escalation path]

## Related Articles
- [Link to related article 1]
- [Link to related article 2]

## FAQ

### [Common question about this topic]?
[Answer]
```

---

## Writing Guidelines

### Clarity Over Brevity

| Instead of | Use |
|------------|-----|
| Navigate to Settings | Click **Settings** in the top menu |
| Configure the integration | Enter your API key in the API Key field |
| Ensure proper setup | Check that the green checkmark appears |

### Action-Oriented Language

- ✓ **Start with verbs:** Click, Enter, Select, Copy, Paste
- ✓ **Be specific:** "Click the blue Save button" not "Save your changes"
- ✓ **One action per step:** Don't combine multiple actions

### Formatting for Scannability

- **Bold** UI elements: Click **Settings**, then **Integrations**
- Use `code formatting` for: file paths, code snippets, API values
- Number steps sequentially
- Use callout boxes for warnings and tips

### Reading Level

- Target 6th-8th grade reading level
- Avoid jargon unless your audience expects it
- Define technical terms on first use
- Use simple sentence structures

---

## AEO Optimization

### Why Help Centers Win at AEO

Help center content answers the hyper-specific questions people ask LLMs:

- "Does [product] support [feature]?"
- "How do I [accomplish task] in [product]?"
- "Can [product] integrate with [tool]?"
- "[Product] vs [competitor] for [use case]"

### Key Strategies

**1. Cover the Long Tail**

Mine questions from:
- Sales call transcripts
- Support tickets
- Community forums (Reddit, Discord)
- Social media mentions
- Chatbot conversation logs
- G2/Capterra reviews

**2. Cross-Link Aggressively**

Help articles rarely link to each other. Fix this:
- Link to prerequisite articles
- Link to related features
- Link to troubleshooting from how-tos
- Create "See also" sections

**3. Answer Questions Directly**

LLMs extract answers from content. Make them extractable:

**Weak:**
> "The integration process involves several steps that vary depending on your configuration..."

**Strong:**
> "To integrate with Slack, go to Settings > Integrations > Slack and click Connect. The process takes about 2 minutes."

**4. Include Specific Details**

LLMs cite content with concrete information:
- Exact steps (numbered)
- Specific requirements (versions, plans)
- Time estimates ("takes 5 minutes")
- Error messages (exact text)

---

## SEO for Help Centers

### Title Optimization

| Type | Format | Example |
|------|--------|---------|
| How-to | How to [Task] in [Product] | How to Export Data in Acme |
| Troubleshooting | Fix [Error/Issue] | [Product] | Fix "Connection Failed" Error | Acme |
| Feature | [Feature Name] Guide | [Product] | API Integration Guide | Acme |

### Meta Descriptions

- 150-160 characters
- Include the question being answered
- Include the product name
- Action-oriented language

**Example:**
> "Learn how to export your data from Acme in CSV, Excel, or PDF format. Step-by-step guide with screenshots. Takes 2 minutes."

### Schema Markup

Use FAQ schema for question-answer content:
```json
{
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I reset my password?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "To reset your password..."
    }
  }]
}
```

Use HowTo schema for step-by-step guides:
```json
{
  "@type": "HowTo",
  "name": "How to Connect Slack to Acme",
  "step": [...]
}
```

---

## Content Categories

### Getting Started
- Quick start guide
- First-time setup
- Basic concepts
- Onboarding checklist

### Feature Documentation
- Feature overview
- Step-by-step usage
- Advanced options
- Best practices

### Integrations
- Setup instructions
- Supported features
- Troubleshooting
- Limitations

### Troubleshooting
- Common error messages
- Known issues
- Diagnostic steps
- When to contact support

### Billing & Account
- Pricing/plan details
- Upgrade/downgrade
- Cancellation
- Invoices and receipts

---

## Quality Checklist

Before publishing:

**Structure:**
- [ ] Answer appears in first 2 sentences
- [ ] Steps are numbered
- [ ] One action per step
- [ ] Troubleshooting section included
- [ ] Related articles linked

**Clarity:**
- [ ] UI elements in bold
- [ ] Code in `code formatting`
- [ ] Screenshots for complex steps
- [ ] Reading level checked (aim for 8th grade)

**SEO/AEO:**
- [ ] Title includes target question
- [ ] Meta description under 160 characters
- [ ] Internal links to related articles
- [ ] Schema markup applied (FAQ or HowTo)
- [ ] URL is descriptive and short

**Accessibility:**
- [ ] Alt text for all images
- [ ] Descriptive link text (not "click here")
- [ ] Proper heading hierarchy (H1 → H2 → H3)

---

## Common Mistakes

### Avoid

1. **Too much preamble:** "Welcome to our help center! We're here to help..."
2. **Vague instructions:** "Configure the settings as needed"
3. **Missing context:** Assuming knowledge the reader doesn't have
4. **Outdated screenshots:** UI that no longer matches
5. **Dead ends:** No next steps or related articles
6. **Walls of text:** Paragraphs instead of steps

### Fix

1. Start with the answer
2. Be specific: "Click Settings > API > Generate Key"
3. Define prerequisites at the top
4. Update docs with every UI change
5. Always include "What's next" or related articles
6. Use numbered steps and bullet points

---

## Measuring Success

### Key Metrics

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| Article views | Discoverability | Trending up |
| Time on page | Engagement/usefulness | 1-3 minutes |
| Bounce rate | Content match | Under 60% |
| Search exits | Failed to find answer | Minimize |
| Support ticket deflection | Self-service success | Track % |
| CSAT for docs | User satisfaction | 4+ out of 5 |

### Continuous Improvement

1. **Track searches with no results:** Create missing content
2. **Monitor support tickets:** Turn common questions into articles
3. **Collect feedback:** Add "Was this helpful?" to every article
4. **Review analytics:** Update low-performing articles
5. **Audit regularly:** Remove/update outdated content
