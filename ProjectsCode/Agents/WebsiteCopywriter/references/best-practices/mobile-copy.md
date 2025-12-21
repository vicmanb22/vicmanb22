# Mobile Copy Best Practices

Guidelines for writing copy that works on small screens. With 50%+ of web traffic on mobile, copy must be mobile-first.

---

## The Mobile Reality

- **Average mobile screen:** 375px wide (iPhone), 360px (Android)
- **Above the fold:** ~500-600px visible height
- **Attention span:** Even shorter on mobile than desktop
- **Context:** Often distracted, on-the-go, one-handed use
- **Connection:** May be slow or intermittent

---

## Headline Guidelines

**Cross-Reference:** For comprehensive headline guidance, see `references/best-practices/headlines.md`

### Length Constraints

**Research Foundation:** Mobile users scan even faster than desktop users. Front-load value in the first 3 words.

| Element | Desktop | Mobile Guideline | Research Source |
|---------|---------|-----------------|-----------------|
| H1 Headlines | 50-60 characters | 50 characters max | Buffer/Usability research |
| H2 Headers | 40-50 characters | 40 characters max | Mobile-first design |
| Subheadlines | 2-3 lines | 1-2 lines | Readability studies |

### Mobile Headline Strategies

**1. Front-load value**
Put the most important words first—they may be the only ones seen.

Desktop: `Streamline Your Workflow with Our Powerful Project Management Tools`
Mobile: `Streamline Your Workflow`

**2. Break strategically**
Write headlines that break naturally on small screens.

Bad break:
```
Streamline Your
Workflow with Our Tools
```

Good break:
```
Streamline Your Workflow
with Our Tools
```

**3. Test at 375px**
Always preview headlines at mobile width before finalizing.

---

## Body Copy Adjustments

**Cross-Reference:** For accessibility guidelines, see `references/best-practices/accessibility.md`

### Paragraph Length

**Research Foundation:** UX research (Baymard Institute) shows long text blocks are perceived as intimidating on mobile. Yoast recommends paragraphs under 200 words; for mobile, shorter is better.

| Context | Recommendation | Research Source |
|---------|---------------|-----------------|
| Mobile body copy | 2-3 sentences max (50-75 words) | Mobile UX research |
| Desktop body copy | 3-4 sentences max (75-100 words) | Readability studies |
| Ideal for scanning | 1-2 sentences per paragraph | Nielsen Norman Group |

**Note:** Accessibility guidelines (see `references/best-practices/accessibility.md`) recommend 3-4 sentences for general readability. For mobile-first design, start with 2-3 sentences and expand for desktop.

### Sentence Length
- Keep sentences under 20 words
- Avoid complex sentence structures
- One idea per sentence

### Scanning Pattern
Mobile users scan even more than desktop users:
- **Bold key phrases:** Help scanners catch important points
- **Use bullets:** Break up dense text
- **Short sections:** Each scrollable area has one clear message

### Example Adaptation

**Desktop version:**
```
Our project management software helps teams of all sizes collaborate
more effectively. With real-time updates, customizable workflows, and
powerful integrations, you'll spend less time managing tools and more
time doing meaningful work. Join over 10,000 teams who have transformed
their productivity.
```

**Mobile version:**
```
Collaborate more effectively with your team.

Real-time updates. Custom workflows. Powerful integrations.

**10,000+ teams** have transformed their productivity.
```

---

## CTA Button Copy

**Cross-Reference:** For comprehensive CTA guidance, see `references/best-practices/ctas.md`

### Character Limits

**Research Foundation:** Intuit Content Design guidelines recommend 2-4 words, 24 characters max for CTA buttons. Shorter CTAs also translate better across languages.

| Context | Recommendation | Research Source |
|---------|---------------|-----------------|
| Word count | 2-4 words optimal | Intuit UX, Tubik Studio |
| Character limit | 24 characters max | Intuit Content Design |
| Mobile ideal | 15-20 characters | Mobile-first UX |
| Minimum tap target | 44x44px (Apple HIG) | Apple Human Interface Guidelines |

### Mobile CTA Adaptations

| Desktop (can be longer) | Mobile (keep short) |
|-------------------------|---------------------|
| Start Your Free 14-Day Trial (29 chars) | Start Free Trial (16 chars) |
| Download the Complete Guide (27 chars) | Get the Guide (13 chars) |
| Schedule a Demo with Our Team (30 chars) | Book a Demo (11 chars) |
| Get Started for Free Today (26 chars) | Get Started Free (16 chars) |

### Button Placement
- **Primary CTA:** Above the fold, centered or full-width
- **Secondary CTA:** Clearly differentiated (ghost button, different color)
- **Sticky CTA:** Consider fixed bottom bar on long pages

---

## Form Copy for Mobile

### Label Optimization
- Keep labels short (above field, not beside)
- Use placeholder text as supplementary hint only
- Format hints essential: "MM/DD/YYYY"

### Field Reduction
Every field increases abandonment on mobile:
- Ask only what's essential
- Use progressive disclosure (multi-step)
- Enable autofill (proper input types)

### Mobile Form Copy Examples

**Desktop:**
```
Email Address: [                    ]
Please enter a valid email address
```

**Mobile:**
```
Email
[your@email.com          ]
```

### Error Messages
- Short and specific
- Appear near the field (not just at top)
- Red border + icon + text (not color alone)

---

## Section-by-Section Mobile Considerations

### Hero Section
- Headline: 40-50 characters
- Subheadline: 1-2 short lines
- CTA: Prominent, full-width or centered
- Image: Background or below text (not beside)
- Social proof teaser: Icons + number, not lengthy text

### Problem/Pain Section
- 3-4 pain points maximum
- Use icons to save text space
- Bullet format preferred over paragraphs

### Features Section
- Card layout: Stack vertically (not grid)
- One feature per screen "fold"
- Icon + headline + 1-2 sentence description
- Consider carousel if many features

### Social Proof
- One testimonial at a time (carousel/swipe)
- Shorter quotes: 2-3 sentences max
- Consider quote highlights/excerpts
- Logos: 3-4 visible, carousel for more

### Pricing Tables
- One plan visible at a time (tabs or accordion)
- Key features only (full comparison link)
- Recommend or highlight best option prominently
- CTA buttons always visible

### FAQ
- Accordion format (saves space)
- Short questions (5-8 words)
- Concise answers (3-4 sentences)
- Most asked questions first

---

## Mobile-Specific Elements

### Sticky Headers/Footers
**Sticky Header CTA:**
- Appears after scrolling past hero
- 44-48px height
- Short CTA text + button
- Dismissable or minimal

**Sticky Footer:**
- Works well for primary CTA
- Full-width button
- May conflict with browser UI (test carefully)

### Swipe Carousels
Good for:
- Testimonials
- Feature highlights
- Product images
- Plan comparisons

Guidelines:
- Visible pagination (dots or progress)
- At least partial next slide visible (cue to swipe)
- Consider auto-advance (with pause option)

### Collapsible Content
Use accordion/expandable for:
- FAQs
- Detailed feature descriptions
- Terms and conditions
- Long policy text

---

## Typography on Mobile

### Minimum Sizes
- **Body text:** 16px minimum (prevents zoom on iOS)
- **Small text:** 14px absolute minimum (captions, disclaimers)
- **Headlines:** 24-32px H1, 20-24px H2, 18-20px H3

### Line Length
- **Maximum:** 65-75 characters per line
- **Mobile typically:** 35-50 characters per line
- Too long = hard to track to next line

### Line Height
- **Body:** 1.5-1.6 line height
- **Headlines:** 1.2-1.3 line height
- **Buttons:** Generous padding, not tight

---

## Mobile-First Writing Process

### Step 1: Write for Mobile
Start with mobile constraints:
- Short headline (40-50 chars)
- 2-sentence body paragraphs
- Bullet points over paragraphs
- Short CTA (15-20 chars)

### Step 2: Expand for Desktop
Add richness for larger screens:
- Extended headline variant
- Additional context in body
- More features shown at once
- Fuller testimonial quotes

### Step 3: Test Both Versions
- Preview at 375px and 1440px
- Check line breaks
- Verify CTA prominence
- Test scroll length

---

## Mobile Copy Checklist

### Before Finalizing

**Headlines:**
- [ ] H1 under 50 characters
- [ ] H2s under 45 characters
- [ ] No awkward line breaks at 375px
- [ ] Most important words first

**Body Copy:**
- [ ] Paragraphs under 3 sentences
- [ ] Sentences under 20 words
- [ ] Key points in bold
- [ ] Bullet lists where possible

**CTAs:**
- [ ] Under 20 characters
- [ ] Action-oriented verbs
- [ ] Clear value proposition
- [ ] Above the fold on key pages

**Forms:**
- [ ] Minimum fields necessary
- [ ] Labels above fields (not beside)
- [ ] Clear error messages
- [ ] Success confirmation clear

**Overall:**
- [ ] Scannable structure
- [ ] One focus per scroll
- [ ] No walls of text
- [ ] Visual hierarchy guides reading

---

## Common Mobile Copy Mistakes

### Avoid

1. **Long headlines that wrap 3+ times**
2. **Dense paragraphs** that look like text walls
3. **Too many CTAs** competing for attention
4. **Horizontal scrolling** content or tables
5. **Pop-ups** that are hard to close
6. **Tiny tap targets** (under 44px)
7. **Hover-only information** (no hover on touch)
8. **Forms with many optional fields**
9. **Autoplaying video with sound**
10. **Fixed elements** that cover important content

### Test On Actual Devices

Emulators don't catch everything:
- Test on real iPhone and Android
- Try with one hand (reachability)
- Test on slow connection (3G simulation)
- Try with large text settings enabled
- Test in bright light (contrast matters)
