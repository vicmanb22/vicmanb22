# Technical Specifications for Website Copy

Developer-ready specifications to include with copy deliverables. These guide implementation of animations, interactions, mobile adaptations, and visual hierarchy.

---

## Animation Specifications

### Entry Animations

**Purpose:** Draw attention to content as it enters viewport.

| Animation Type | Best For | CSS/Implementation |
|---------------|----------|-------------------|
| Fade in | Text blocks, testimonials | `opacity: 0 → 1`, `transition: 0.3s ease` |
| Slide up | Feature cards, CTAs | `transform: translateY(20px) → translateY(0)` |
| Slide in from left/right | Before/after, comparisons | `transform: translateX(±30px) → translateX(0)` |
| Scale up | Icons, images, logos | `transform: scale(0.9) → scale(1)` |
| Stagger | Lists, card grids | Sequential delay: 0.1s between items |

**Timing Guidelines:**
- Duration: 0.2s - 0.4s (faster = more professional)
- Easing: `ease-out` for entries, `ease-in-out` for transforms
- Stagger delay: 0.05s - 0.15s between items
- Don't animate more than 3-4 elements simultaneously

### Scroll-Triggered Animations

**Purpose:** Reveal content as user scrolls down page.

```
Trigger: When element enters viewport (Intersection Observer)
Threshold: 0.1 - 0.2 (trigger when 10-20% visible)
Animation: [Same as entry animations]
Once: true (don't re-animate on scroll up)
```

**Section-Specific Recommendations:**

| Section | Recommended Animation |
|---------|----------------------|
| Hero | None (already visible) or subtle parallax on image |
| Social proof bar | Slide up with stagger on logos |
| Problem section | Fade in |
| Solution steps | Stagger slide up (numbered steps) |
| Features | Card grid with stagger |
| Testimonials | Fade in or slide up |
| Pricing | Scale up on cards |
| CTA section | Subtle pulse on button after scroll |

### Micro-Interactions

**Purpose:** Feedback and delight on user actions.

| Element | Interaction | Specification |
|---------|-------------|---------------|
| Buttons | Hover | `transform: translateY(-2px)`, `box-shadow` increase |
| Buttons | Click | `transform: scale(0.98)`, brief press state |
| Cards | Hover | Subtle lift, shadow increase |
| Links | Hover | Underline animation, color shift |
| Form fields | Focus | Border color change, subtle glow |
| Checkboxes | Check | Satisfying checkmark animation |
| Toggle switches | Toggle | Smooth slide with color transition |

---

## Interactive Elements

### Expandable Content

**Accordions (FAQ, Features)**
```
Behavior:
- Click header to expand/collapse
- Smooth height transition (0.3s)
- Rotate chevron indicator
- Optional: Close others when opening new (single-expand mode)
- Keyboard accessible (Enter/Space to toggle)

Mobile:
- Full-width touch targets
- Minimum 44px tap height
```

**Tabs**
```
Behavior:
- Click tab to show content
- Active tab indicator (underline or background)
- Fade transition between content (0.2s)
- Keyboard navigable (arrow keys)

Mobile:
- Consider converting to accordion on mobile
- Or scrollable tab bar with visible overflow indicator
```

**Read More/Less**
```
Behavior:
- Truncate at [X] lines with gradient fade
- Click to expand full content
- Toggle text: "Read more" ↔ "Show less"
- Smooth height transition
```

### Forms

**Field Interactions:**
```
Focus states:
- Border color change (brand color)
- Subtle glow or shadow
- Label animation (float above)

Validation:
- Real-time validation on blur
- Clear error messaging below field
- Success indicator (green check)
- Error indicator (red border, icon)

Submit button:
- Loading state with spinner
- Disable during submission
- Success state before redirect
```

**Multi-Step Forms:**
```
- Progress indicator (steps or percentage)
- Smooth transition between steps
- Save progress (if long form)
- Back button always available
- Summary before final submit
```

### Hover States (Desktop Only)

**Cards:**
```
On hover:
- Lift effect: translateY(-4px)
- Shadow increase: spread and blur
- Optional: Reveal additional info or CTA
- Transition: 0.2s ease
```

**Images:**
```
On hover:
- Subtle zoom: scale(1.02) with overflow hidden
- Or overlay with text/CTA
- Or caption reveal
```

---

## Mobile Considerations

### Copy Length Adjustments

| Element | Desktop | Mobile |
|---------|---------|--------|
| Headlines | Up to 80 characters | 40-50 characters max |
| Subheadlines | 2-3 lines | 1-2 lines |
| Body paragraphs | 3-4 sentences | 2-3 sentences |
| CTA buttons | Full text | Shorter or icon + text |
| Feature descriptions | Full | Consider collapsible |

### Touch Targets

**Minimum sizes:**
- Buttons: 44px x 44px minimum tap area
- Links in text: Add padding, consider 48px height
- Form fields: 48px height minimum
- Spacing between tap targets: 8px minimum

### Layout Adaptations

**Hero Section:**
```
Desktop: Side-by-side text and image
Mobile: Stack vertically (text above image)
         Or image as background with text overlay
```

**Feature Grid:**
```
Desktop: 3-4 columns
Tablet: 2 columns
Mobile: 1 column or horizontal scroll cards
```

**Testimonials:**
```
Desktop: 3-column grid or side-by-side
Mobile: Single testimonial with carousel/swipe
        Or stacked vertically
```

**Pricing Table:**
```
Desktop: Side-by-side comparison
Mobile: Tabs for each plan
        Or accordion
        Or horizontal scroll
```

### Mobile-Specific Features

**Sticky Elements:**
```
- Sticky header with CTA button
- Sticky footer CTA on long pages
- Progress indicator on long-form content
```

**Touch Gestures:**
```
- Swipe for testimonial carousel
- Pull to refresh (if applicable)
- Swipe to dismiss (overlays, notifications)
```

---

## Visual Hierarchy Notes

### What Should Draw the Eye

**Priority Order (typical landing page):**
1. Hero headline
2. Primary CTA button
3. Key benefit/value prop
4. Social proof highlight
5. Supporting content

### Typography Hierarchy

```
H1 (Hero headline):
- Largest size (32-48px mobile, 48-72px desktop)
- Bold weight
- Brand or high-contrast color
- One per page

H2 (Section headers):
- Medium-large (24-32px mobile, 32-40px desktop)
- Semi-bold or bold
- Consistent spacing above (48-72px)

H3 (Subsection headers):
- Medium (18-24px mobile, 24-28px desktop)
- Semi-bold
- Used for features, FAQs, etc.

Body:
- Standard (16-18px)
- Regular weight
- High readability (1.5-1.7 line height)

Small text:
- 14px minimum (never smaller)
- Captions, disclaimers, meta info
```

### Color for Emphasis

**CTA Buttons:**
- Primary: Brand's action color (often different from brand color)
- High contrast with background
- Consistent across site

**Accent Colors:**
- Use sparingly for key points
- Highlight pricing, key benefits, urgency elements
- Don't overuse (dilutes impact)

**Text Contrast:**
- Body text: WCAG AA minimum (4.5:1 ratio)
- Large text: 3:1 ratio minimum
- Tool: https://webaim.org/resources/contrastchecker/

---

## Performance Considerations

### Animation Performance

**Do:**
- Animate `transform` and `opacity` only (GPU-accelerated)
- Use `will-change` sparingly for known animations
- Keep animations under 0.4s
- Reduce motion for users who prefer it

**Don't:**
- Animate `width`, `height`, `margin`, `padding` (triggers reflow)
- Run multiple heavy animations simultaneously
- Use excessive JavaScript animations when CSS works

```css
/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Image Optimization

```
Hero images: Max 200KB after compression
Feature images: Max 100KB each
Logos/icons: SVG preferred, or <20KB PNG
Testimonial photos: 50KB max, lazy load
Background images: Consider CSS gradients instead
```

### Loading Priorities

```
Above the fold: Load immediately
- Hero image
- Primary CTA
- Logo

Below the fold: Lazy load
- Testimonial images
- Feature illustrations
- Video embeds (facade pattern)
```

---

## A/B Testing Implementation Notes

### Elements to Make Testable

When implementing, ensure these can be easily swapped:

1. **Headlines:** CMS-editable or feature-flagged
2. **CTA text:** Variable in code
3. **CTA colors:** CSS variable or theme toggle
4. **Hero image:** Content-managed
5. **Social proof order:** Draggable/configurable
6. **Pricing display:** Easily toggleable formats

### Test Tracking Setup

```
Recommend tracking:
- Scroll depth (25%, 50%, 75%, 100%)
- CTA clicks (primary, secondary, per section)
- Form interactions (start, abandon, complete)
- Video plays (start, 25%, 50%, 75%, complete)
- FAQ opens (which questions)
- Time on page
- Bounce rate
```

---

## Platform-Specific Notes

### Webflow
- Use native interactions for scroll animations
- CMS for testimonials, FAQs
- Form submissions via native or Zapier
- Consider Finsweet solutions for complex interactions

### WordPress
- Animation plugins: AOS, GSAP, Animate on Scroll
- Lazy loading via plugin or WP 5.5+ native
- Consider caching impact on dynamic elements

### Shopify
- Theme-dependent animation support
- Use Liquid for dynamic content
- Consider app ecosystem for advanced features

### Custom/React/Vue
- GSAP for complex animations
- Framer Motion (React)
- Intersection Observer for scroll triggers
- Component-level state for interactions
