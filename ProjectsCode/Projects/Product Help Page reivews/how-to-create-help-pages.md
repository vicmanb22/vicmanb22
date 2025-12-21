# How to Create Help Pages for Verified Metrics

A comprehensive guide for creating high-quality help pages that serve VCs, PE firms, and lenders.

---

## Your Goal

Create help pages that enable financially sophisticated users to quickly understand and use Verified Metrics features with confidence.

**A good help page:**
- ✅ Gets users to their answer in <2 minutes
- ✅ Shows realistic examples they'll actually encounter
- ✅ Uses professional screenshots that build credibility
- ✅ Provides interpretation guidance (what good looks like, red flags)
- ✅ Reduces support tickets by addressing common issues upfront

**Key principle**: Our audience (VCs, PE firms, lenders) are detail-oriented professionals. Quality matters more than speed.

---

## The Process (Overview)

| Step | What | Who | Time |
|------|------|-----|------|
| 1. Record | Session with product specialist | Marketing + Product | 30-45 min |
| 2. Transcribe | Get transcript | Marketing | 5 min |
| 3. Generate | Create draft with AI | Marketing | 15 min |
| 4. Refine | Add screenshots, edit copy | Marketing | 45-60 min |
| 5. Review | Quality check | Product + Marketing | 15 min |
| 6. Create Video | Produce YouTube walkthrough | Marketing | 2-3 hours |

**Total time**: ~4-5 hours per help page

---

## Step 1: Record the Session

### Setup Requirements

- **Screen recording software** (Loom, QuickTime, or similar)
- **Demo company environment** with realistic data
- **Product specialist** who knows the feature deeply
- **Marketing facilitator** to ask user-focused questions

### Marketing's Role: Ask the Right Questions

Your job is to guide the product specialist to explain features the way users need to hear them. Use this question framework:

| Question Type | Example Questions | Why It Matters |
|--------------|------------------|----------------|
| **Context** | "Who typically uses this feature?" "When would someone need this?" | Helps users know if it applies to them |
| **Prerequisites** | "What data do they need first?" "Are there any setup steps?" | Prevents users from getting stuck |
| **Process** | "Walk me through this step by step" "What do you click first?" | Creates the actual tutorial |
| **Interpretation** | "What should they look for in the output?" "What's a red flag?" | Enables users to act on insights |
| **Troubleshooting** | "What usually goes wrong?" "How do you fix [X]?" | Reduces support tickets |
| **Next steps** | "What would they typically do after this?" | Guides workflow integration |

### Recording Best Practices

| Do ✅ | Don't ❌ |
|------|---------|
| Use realistic demo company name (e.g., "CloudForward Technologies") | Use fake-looking names ("sell.verifiedmetrics.com", "VM Demo", "test.com") |
| Walk through real user workflows | Jump around or skip steps |
| Pause to explain why something matters | Rush through without context |
| Show actual data that looks professional | Use obviously fake or incomplete data |
| Mention what good vs. bad looks like | Only show the happy path |
| Clean screen (close personal bookmarks, unnecessary tabs) | Record with cluttered browser |

### Minimum Recording Requirements

Before ending the recording session, verify you captured:

- [ ] Feature overview (what it does, who it's for)
- [ ] Complete step-by-step walkthrough
- [ ] What the output means and how to interpret it
- [ ] At least 2-3 common issues and how to fix them
- [ ] What users typically do next
- [ ] Any prerequisites or required data

---

## Step 2: Transcribe

Get a transcript of the recording using:
- Loom's built-in transcription
- Otter.ai
- ChatGPT (upload audio)
- Your recording tool's transcription feature

**Tip**: Clean transcription isn't critical — AI will extract the key information in the next step.

---

## Step 3: Generate Draft with AI

### What to Give the AI

Provide:
1. **The transcript** from Step 2
2. **The template** ([help-page-template.md](help-page-template.md))
3. **The prompt** below

### The AI Prompt

```
I have a transcript of a product walkthrough for Verified Metrics.
Please create a help page following the provided template.

TRANSCRIPT:
[Paste transcript here]

TEMPLATE:
[Paste help-page-template.md content here]

INSTRUCTIONS:
- Follow the template structure exactly
- Keep each step to 3 sentences maximum
- Include placeholders for [Screenshot] where visuals are needed
- Fill in the "Understanding Your Output" table with interpretation guidance
- Use the realistic demo company name from the transcript
- Include troubleshooting from common issues mentioned
- Write for VCs, PE firms, and lenders (financially sophisticated audience)
- Omit sections that don't apply (e.g., "Understanding Your Output" for simple login pages)
```

### Post-Generation Checklist

After AI generates the draft, verify:

- [ ] Page type identified (use case vs. general) with appropriate sections
- [ ] Steps are ≤3 sentences each
- [ ] "Understanding Your Output" table has all 4 columns (Output, What It Means, What Good Looks Like, Red Flags)
- [ ] Realistic demo company name used throughout
- [ ] Common issues section populated
- [ ] Clear completion signal in "What's Next"
- [ ] Professional tone appropriate for audience

---

## Step 4: Refine and Add Screenshots

### What Screenshots to Capture

Capture a screenshot for:
- **Every step** where users need to click, type, or select something
- **Key outputs** that users need to interpret
- **Common issue states** mentioned in troubleshooting

### Screenshot Technical Specifications

| Requirement | Standard | Why |
|-------------|----------|-----|
| **Resolution** | Minimum 1080p (1920×1080) | Ensures text is readable when zoomed |
| **Format** | PNG (not JPG) | Keeps UI text crisp and clear |
| **Annotations** | Arrows/highlights for clickable areas | Shows exactly where to interact |
| **Cropping** | Tight to relevant area | Focuses attention, improves readability |
| **Consistency** | Same zoom level throughout | Professional appearance |
| **Clean state** | No personal data, bookmarks, etc. | Maintains credibility |

### How to Create Quality Screenshots

1. **Capture**: Use screenshot tool (Cmd+Shift+4 on Mac, Snipping Tool on Windows)
2. **Annotate**: Add arrows/highlights using:
   - CleanShot X (Mac)
   - Snagit
   - Preview (Mac) or Paint (Windows)
3. **Crop**: Remove unnecessary chrome and whitespace
4. **Save**: As PNG at 1080p minimum
5. **Name**: Use descriptive names (e.g., `runway-step-1-select-model.png`)

### Screenshot Quality Checklist

Before adding a screenshot, verify:

- [ ] 1080p or higher resolution
- [ ] PNG format
- [ ] Arrow or highlight shows where to click/type
- [ ] Cropped to relevant area (text is large enough to read)
- [ ] No personal information visible
- [ ] Uses realistic demo company data
- [ ] Clean browser/app state (no unnecessary tabs or bookmarks)

### Content Refinement

As you add screenshots, also:

1. **Tighten the copy** - Remove redundancy, improve clarity
2. **Verify accuracy** - Test each step in a clean environment
3. **Check tone** - Professional but approachable
4. **Add specifics** - Replace vague language with exact button names, menu locations

---

## Step 5: Review (Quality Check)

Use the comprehensive [Quality Checklist](#quality-checklist) at the end of this document.

Key reviewer focus areas:
- **Product specialist**: Accuracy of steps and interpretation guidance
- **Marketing**: Clarity, user-friendliness, screenshot quality
- **Both**: Demo company data looks realistic and professional

---

## Step 6: Create YouTube Video

### Pre-Production

| Element | Requirements |
|---------|-------------|
| **Script** | Narration text based on help page steps (aim for 2-5 minutes) |
| **Screen recording** | Fresh recording with realistic demo company, 1080p minimum |
| **Voiceover** | British woman's voice (ElevenLabs or professional voice actor) |
| **Branding** | Verified Metrics intro/outro templates |

### Voice Requirements

- **Accent**: British English
- **Gender**: Female
- **Tone**: Professional, clear, confident
- **Pace**: Moderate (not rushed)
- **Tools**: ElevenLabs, Descript, or professional voice actor

### Video Structure

| Segment | Duration | Content |
|---------|----------|---------|
| **Intro** | 5 sec | Verified Metrics branded intro |
| **Overview** | 15-30 sec | What this video covers, who it's for |
| **Walkthrough** | 1-4 min | Step-by-step demonstration with narration |
| **Recap** | 10-15 sec | Key takeaways, what's next |
| **Outro** | 5 sec | Branded outro with support contact |

### YouTube Optimization

| Element | Best Practice |
|---------|---------------|
| **Title** | Feature name + benefit (e.g., "Runway Analysis - Find Your Cash Runway in Minutes") |
| **Description** | Full description from template below |
| **Tags** | Feature keywords, user types, use cases |
| **Thumbnail** | Branded with clear text overlay showing key benefit |
| **Captions** | Upload accurate SRT file |
| **Cards/End Screen** | Link to related videos and help.verifiedmetrics.com |

### YouTube Description Template

```
[Feature Name] - [One-sentence benefit]

In this video, you'll learn how to [primary action/goal].

Timestamps:
0:00 - Introduction
0:15 - [First major section]
[X:XX] - [Second major section]
[X:XX] - Recap and next steps

Who this is for: [User type from help page]
What you'll need: [Prerequisites from help page]
What you'll get: [Output from help page]

Read the full guide: https://help.verifiedmetrics.com/[page-url]

Need help? Contact support@verifiedmetrics.com

About Verified Metrics:
[Company description]

#VerifiedMetrics #[FeatureCategory] #[UserType]
```

### Video Production Checklist

Before publishing, verify:

- [ ] 1080p resolution minimum
- [ ] Realistic demo company used throughout
- [ ] British female voiceover
- [ ] 2-5 minute duration (not longer unless truly necessary)
- [ ] Branded intro and outro
- [ ] Clean screen (no personal bookmarks, tabs, or data)
- [ ] Clear narration synced with on-screen actions
- [ ] Accurate captions/subtitles uploaded
- [ ] YouTube title, description, tags optimized
- [ ] Thumbnail created and uploaded
- [ ] Cards and end screen configured

### Target Video Specs

- **Resolution**: 1920×1080 (1080p) minimum
- **Frame rate**: 30fps
- **Format**: MP4 (H.264)
- **Audio**: 128kbps minimum, stereo
- **File size**: <500MB for easier upload

---

## Demo Company Data Requirements

### Why Realistic Data Matters

Our audience (VCs, PE firms, lenders) are financially sophisticated professionals who:
- Review hundreds of companies annually
- Notice unrealistic financial patterns immediately
- Need to trust that examples reflect real-world scenarios

**Using fake-looking data undermines credibility.**

### Demo Company Standards

| Element | Good Example ✅ | Bad Example ❌ |
|---------|----------------|----------------|
| **Company name** | "CloudForward Technologies" | "sell.verifiedmetrics.com" |
| **Company name** | "Meridian Health Systems" | "VM Demo Company" |
| **Company name** | "Stellar Logistics Inc." | "test.verifiedmetrics.com" |
| **Revenue** | $2.4M growing to $3.8M | Exactly $1M flat every month |
| **Expenses** | Mix of categories with variation | Round numbers, same every period |
| **Growth rate** | 15-25% with some fluctuation | Exactly 20% every single month |
| **Margins** | 68% → 71% → 69% | Exactly 70% forever |

### Creating Realistic Demo Companies

**Financial Profile Guidelines:**

1. **SaaS Company** (for VC use cases):
   - Revenue: $2-5M ARR, growing 20-40% YoY
   - Gross margin: 65-80%
   - Burn rate: $100-300K/month
   - Runway: 12-18 months

2. **Manufacturing Company** (for PE/lender use cases):
   - Revenue: $10-50M, growing 5-15% YoY
   - Gross margin: 25-40%
   - EBITDA margin: 10-20%
   - Working capital cycles visible

3. **Services Company**:
   - Revenue: $5-20M, growing 10-25% YoY
   - Gross margin: 40-60%
   - Seasonality patterns
   - Headcount-driven expense growth

**Add realistic variation:**
- Revenue doesn't grow perfectly linearly
- Expenses occasionally spike (hiring, one-time costs)
- Margins fluctuate slightly quarter to quarter
- Seasonal patterns if applicable

---

## Quality Checklist

### Content Checks

- [ ] Title clearly states what feature/task this covers
- [ ] One-sentence description at top summarizes value
- [ ] "At a Glance" table complete (or intentionally omitted for general pages)
- [ ] Video embedded (or placeholder note if pending)
- [ ] Steps are numbered and in logical order
- [ ] Each step is ≤3 sentences
- [ ] Screenshots present for every major action
- [ ] "Understanding Your Output" table has 4 columns (or omitted if not applicable)
- [ ] Common issues section addresses real problems users encounter
- [ ] "What's Next" provides clear completion signal and next step
- [ ] Support contact information included

### Accuracy Checks

- [ ] Every step tested in clean environment
- [ ] Button names, menu locations are exact
- [ ] Prerequisites are complete (users won't get stuck)
- [ ] Output interpretation is accurate
- [ ] Troubleshooting solutions actually work
- [ ] Links to related pages are correct

### Clarity Checks

- [ ] No jargon without explanation
- [ ] Steps are actionable (not vague)
- [ ] Screenshots have arrows/highlights showing where to interact
- [ ] "What Good Looks Like" and "Red Flags" provide clear guidance
- [ ] Tone is professional but approachable
- [ ] Would work for someone who's never seen this feature before

### Professional Standards

- [ ] Realistic demo company name used throughout
- [ ] All screenshots are 1080p minimum, PNG format
- [ ] Screenshots show clean browser/app state
- [ ] No personal data visible in any screenshot
- [ ] Financial data looks realistic (not obviously fake)
- [ ] Consistent screenshot zoom level and style
- [ ] Professional formatting and spacing

### Before You Submit

- [ ] Product specialist has reviewed and approved
- [ ] All quality checklist items above are checked
- [ ] Help page URL slug is clear and SEO-friendly
- [ ] Page is categorized correctly (For Investors / For Companies / General)
- [ ] Related pages are linked in "What's Next"

### Handoff Requirements

When submitting for final review, provide:

1. Help page markdown file
2. All screenshots (organized in folder)
3. YouTube video (if completed)
4. Product specialist sign-off
5. Any notes about edge cases or limitations

---

## Success Metrics

Track these metrics to measure help page effectiveness:

### Leading Indicators (Check within first week)

| Metric | Target | What It Tells You |
|--------|--------|------------------|
| **Page views** | 25+ in first week | Users are finding the page |
| **Time on page** | 2-4 minutes average | Users are reading, not bouncing |
| **Video play rate** | 30%+ of page viewers | Video is appealing/useful |
| **Scroll depth** | 75%+ reach bottom | Content is engaging |

### Lagging Indicators (Check after 30 days)

| Metric | Target | What It Tells You |
|--------|--------|------------------|
| **Support tickets** | Decrease 30%+ for that feature | Page is answering questions |
| **Feature adoption** | Increase in users completing workflow | Page is enabling success |
| **Return visitors** | <20% return to same page | Users got answer first time |
| **Feedback score** | 4+ stars (if using rating widget) | Quality is high |

### Qualitative Signals

Watch for:
- ✅ Users citing the help page in support conversations
- ✅ Sales team sharing help pages with prospects
- ✅ Product team using help pages for internal training
- ✅ Reduced "how do I..." questions in community/Slack

### Red Flags

If you see these, investigate immediately:
- ⚠️ High page views but very short time on page (<1 min) → Users aren't finding what they need
- ⚠️ Support tickets increasing for that feature → Help page isn't addressing real issues
- ⚠️ Low video play rate (<10%) → Video thumbnail/title needs work
- ⚠️ Users repeatedly returning to same page → Missing key information

---

## Questions?

**Before reaching out, self-check:**

1. Did you follow the template structure exactly?
2. Did you use realistic demo company data?
3. Are all screenshots 1080p PNG with annotations?
4. Is the "Understanding Your Output" table complete (4 columns)?
5. Did product specialist review and approve?

**Still need help?**

- Process questions → Marketing team lead
- Product accuracy → Product specialist
- Technical issues → Engineering
- Video production → Video producer/marketing

---

## Appendix: Page Type Decision Tree

**Is this a page about analyzing financial data or using a financial model?**
- ✅ Yes → **Use case/analytical page** → Use full template
- ❌ No → Continue...

**Is this a page about a foundational feature (login, upload, invite, settings)?**
- ✅ Yes → **General/foundational page** → Use simplified template (omit "Understanding Your Output", minimal "At a Glance")
- ❌ No → Continue...

**When in doubt:** Use the full template and remove sections that don't apply during review.

---

## Document Version

- **Created**: 2025-12-09
- **Last Updated**: 2025-12-09
- **Owner**: Marketing
- **Reviewers**: Product, Engineering

---

**Remember**: Quality over speed. Our audience expects professional, accurate, trustworthy documentation. Take the time to get it right.
