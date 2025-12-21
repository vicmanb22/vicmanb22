# Accessibility Best Practices for Website Copy

Ensuring website copy is accessible to all users, including those using assistive technologies. Reference WCAG 2.1 AA standards.

---

## Why Accessibility Matters for Copy

1. **Legal compliance:** ADA, Section 508, EAA (European Accessibility Act)
2. **Larger audience:** 15-20% of population has some disability
3. **Better SEO:** Accessibility practices improve search visibility
4. **Better UX for everyone:** Clear, well-structured content helps all users
5. **Brand reputation:** Demonstrates inclusivity and care

---

## Content Structure

### Heading Hierarchy
- [ ] **One H1 per page:** Clearly identifies the page topic
- [ ] **Logical order:** Never skip heading levels (H1 → H3 without H2)
- [ ] **Descriptive headings:** Communicate what follows
- [ ] **Scannable:** Users can understand page structure from headings alone

**Screen reader experience:** Users often navigate by headings. Poor hierarchy makes content impossible to navigate.

### Paragraph Structure

**Research Foundation:** Yoast recommends paragraphs under 200 words. For web, 50-100 words (2-4 sentences) is optimal. Mobile requires even shorter paragraphs—see `references/best-practices/mobile-copy.md`.

- [ ] **Short paragraphs:** 2-4 sentences (50-100 words) for desktop; 2-3 sentences for mobile
- [ ] **One idea per paragraph:** Don't overload
- [ ] **Front-load key information:** Important points first
- [ ] **Use whitespace:** Visual breathing room aids comprehension

### Lists
- [ ] **Use actual lists:** `<ul>`, `<ol>` — not formatted text that looks like a list
- [ ] **Consistent structure:** Parallel construction within lists
- [ ] **Appropriate type:** Ordered for sequences, unordered for non-sequential items

---

## Readability

### Reading Level
- [ ] **Target:** 8th grade reading level for general audiences
- [ ] **Tool:** Hemingway App, Flesch-Kincaid score
- [ ] **Why:** Lower reading level = broader accessibility

**How to improve readability:**
- Shorter sentences (under 25 words)
- Common words over jargon
- Active voice over passive
- Concrete language over abstract

### Plain Language Guidelines
- [ ] Use simple, familiar words
- [ ] Avoid jargon unless audience expects it (and define when used)
- [ ] Define acronyms on first use
- [ ] Use contractions (they're more conversational)
- [ ] Write directly to the user ("you" not "users")

**Examples:**
| Instead of | Use |
|------------|-----|
| Utilize | Use |
| Facilitate | Help |
| Commence | Start |
| In order to | To |
| At this point in time | Now |
| Leverage | Use |

### Sentence Structure
- [ ] Vary sentence length (but keep average under 20 words)
- [ ] Active voice preferred ("We built this" not "This was built by us")
- [ ] Clear subject-verb-object structure
- [ ] Avoid double negatives

---

## Link Text

### Descriptive Links
- [ ] **Link text describes destination:** Not "click here" or "read more"
- [ ] **Makes sense out of context:** Screen readers can navigate by links
- [ ] **Indicates file type if applicable:** "(PDF, 2MB)"

**Bad examples:**
- "Click here to learn more"
- "Read more"
- "Here"
- "Link"

**Good examples:**
- "Download our pricing guide (PDF, 2MB)"
- "Learn more about our project management features"
- "Read the full case study: How Acme increased conversions by 40%"

### Link Behavior
- [ ] **Indicate new windows:** If link opens new tab, warn user: "opens in new tab"
- [ ] **Consistent behavior:** Same type of link behaves the same way
- [ ] **Underlined or visually distinct:** Don't rely on color alone

---

## Image Alt Text

### When to Use Alt Text
- [ ] **Informative images:** Describe what the image conveys
- [ ] **Functional images:** Describe the action (for buttons, links)
- [ ] **Decorative images:** Empty alt="" (don't skip, use empty)

### Alt Text Guidelines
- [ ] **Concise:** 125 characters or less
- [ ] **Descriptive:** What does the image communicate?
- [ ] **No "image of" or "picture of":** Screen readers already announce images
- [ ] **Include text in images:** If image contains text, include it in alt

**Examples:**
| Image | Good Alt Text |
|-------|---------------|
| Team photo | "The Acme team at our San Francisco office" |
| Product screenshot | "Dashboard showing real-time project status and team activity" |
| Client logo | "Stripe" (just the company name) |
| Decorative background | alt="" (empty, not omitted) |
| Graph showing growth | "Chart showing 40% revenue growth from Q1 to Q4 2024" |

### Complex Images
For charts, graphs, infographics:
- [ ] Provide brief alt text
- [ ] Include detailed description in surrounding text or link to long description
- [ ] Consider data tables as alternative

---

## Color and Contrast

### Text Contrast
- [ ] **Normal text:** 4.5:1 contrast ratio minimum (WCAG AA)
- [ ] **Large text (18px+ or 14px bold):** 3:1 ratio minimum
- [ ] **Tool:** WebAIM Contrast Checker

### Don't Rely on Color Alone
- [ ] **Error states:** Don't just turn text red; add icon or text description
- [ ] **Required fields:** Don't just use red asterisk; add "(required)"
- [ ] **Links:** Underline or other indicator besides color
- [ ] **Charts/graphs:** Use patterns, labels, or shapes in addition to color

### Color Blind Considerations
- 8% of men have some color blindness
- Red/green distinction is most common issue
- Use tools like Color Oracle to test

---

## Form Accessibility

### Labels and Instructions
- [ ] **Every field has a label:** Visually connected and programmatically associated
- [ ] **Required fields marked:** "(required)" not just asterisk
- [ ] **Format hints provided:** "Phone: (555) 555-5555"
- [ ] **Error messages specific:** "Email must include @" not just "Invalid"

### Error Handling
- [ ] **Errors identified clearly:** Not just color change
- [ ] **Error messages next to fields:** Not just at top of form
- [ ] **Suggestions for correction:** "Did you mean example@gmail.com?"
- [ ] **Don't clear form on error:** Preserve user input

### Form Copy Guidelines
- [ ] Clear, action-oriented labels ("Full Name" not "Name")
- [ ] Helpful placeholder text (but not as replacement for labels)
- [ ] Success messaging confirms completion
- [ ] Progress indicators for multi-step forms

---

## Button and CTA Accessibility

### Button Text
- [ ] **Descriptive action:** "Start Free Trial" not just "Submit"
- [ ] **Unique on page:** Each button text should be distinct (screen readers list buttons)
- [ ] **Communicates outcome:** What happens when I click?

**Avoid:**
- "Submit"
- "Click Here"
- "Go"
- "Yes"

**Better:**
- "Create My Account"
- "Download Free Guide"
- "Start 14-Day Trial"
- "Send Message"

### Button States
- [ ] **Focus visible:** Clear outline when tabbed to
- [ ] **Hover state:** Visual feedback on mouse over
- [ ] **Active/pressed state:** Shows button is being clicked
- [ ] **Disabled state:** Clearly different (but still readable)

---

## Multimedia

### Video
- [ ] **Captions:** For deaf/hard of hearing users
- [ ] **Transcripts:** Full text version available
- [ ] **Audio descriptions:** For blind users (describe visual content)
- [ ] **No autoplay:** Or provide controls to stop
- [ ] **Accessible player:** Keyboard navigable controls

### Audio
- [ ] **Transcripts:** Full text version of audio content
- [ ] **No autoplay:** User controls when it starts
- [ ] **Controls accessible:** Can be operated by keyboard

### Animation
- [ ] **Pause control:** Users can stop animations
- [ ] **No flashing:** Avoid flashing more than 3 times per second
- [ ] **Respect prefers-reduced-motion:** CSS media query
- [ ] **Not essential:** Information conveyed without animation too

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Tables

### When to Use Tables
- [ ] For tabular data (comparisons, schedules, data)
- [ ] Not for layout purposes

### Table Accessibility
- [ ] **Caption:** Describe what the table contains
- [ ] **Headers:** Use `<th>` for column/row headers
- [ ] **Scope:** Specify row or column header scope
- [ ] **Summary:** For complex tables, provide description

### Table Copy Guidelines
- Concise cell content
- Consistent formatting within columns
- Clear header labels
- Mobile consideration: may need alternative display

---

## Cognitive Accessibility

### Reduce Cognitive Load
- [ ] Clear, consistent navigation
- [ ] Predictable layouts
- [ ] Focused content (one idea per section)
- [ ] Visual hierarchy guides attention
- [ ] White space for breathing room

### Memory Considerations
- [ ] Don't rely on user remembering information from previous pages
- [ ] Provide context reminders
- [ ] Confirmation pages summarize what was entered
- [ ] Clear feedback on actions

### Attention Considerations
- [ ] Minimize distractions
- [ ] Important content is prominent
- [ ] Progress indicators show where user is
- [ ] Ability to save and return later (long processes)

---

## Testing Checklist

### Automated Testing
- [ ] Run WAVE (wave.webaim.org) or axe DevTools
- [ ] Check color contrast (WebAIM Contrast Checker)
- [ ] Validate HTML structure

### Manual Testing
- [ ] **Keyboard navigation:** Tab through entire page, all interactive elements reachable?
- [ ] **Screen reader test:** Use VoiceOver (Mac), NVDA (Windows), or JAWS
- [ ] **Zoom test:** 200% zoom, is content still usable?
- [ ] **Heading structure:** Review with h123 bookmarklet or screen reader

### User Testing
- [ ] Test with actual users who have disabilities
- [ ] Include various assistive technologies
- [ ] Document and address feedback

---

## Quick Reference: Copy-Specific Actions

| Element | Accessibility Action |
|---------|---------------------|
| Headlines | Proper hierarchy, descriptive |
| Links | Descriptive text, not "click here" |
| Buttons | Clear action, unique text |
| Images | Alt text or empty alt for decorative |
| Form labels | Associated with fields, "(required)" |
| Error messages | Specific, near field, not color-only |
| Reading level | 8th grade or lower |
| Paragraphs | Short, one idea each |
| Color usage | Don't rely on color alone |
| Video/audio | Captions, transcripts |

---

## Resources

- **WCAG Guidelines:** w3.org/WAI/standards-guidelines/wcag/
- **WebAIM:** webaim.org (articles, tools)
- **A11y Project:** a11yproject.com (checklist, resources)
- **Hemingway App:** hemingwayapp.com (readability)
- **Color Contrast Checker:** webaim.org/resources/contrastchecker/
