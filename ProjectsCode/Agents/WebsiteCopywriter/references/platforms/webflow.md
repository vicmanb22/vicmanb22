# Webflow Platform Guide

Copy and implementation considerations for Webflow sites.

---

## Platform Overview

**Best for:** Design-focused marketing sites, portfolios, SaaS marketing pages, agency work
**Strengths:** Visual design freedom, native interactions/animations, CMS flexibility
**Limitations:** E-commerce is basic, complex web apps require external solutions

---

## Native Features to Leverage

### Webflow Interactions
Webflow has powerful built-in animation capabilities. Recommend:

**Scroll-triggered animations:**
- Elements animate on viewport entry
- Parallax effects on images/backgrounds
- Progress indicators based on scroll position

**Mouse interactions:**
- Hover states with complex transitions
- Cursor effects
- Button micro-interactions

**Page load animations:**
- Staggered entry for above-the-fold elements
- Logo/hero image reveal effects

**Copy implication:** Can promise sophisticated animations without custom code.

### Webflow CMS
Dynamic content management for:
- Blog posts
- Team members
- Testimonials
- Case studies
- FAQ items
- Product features

**Copy implication:** Content can be templated and dynamically populated. Design reusable copy structures.

### Webflow Forms
Native form builder with:
- Custom styling
- File uploads
- Conditional logic (via attributes)
- Integrations (Zapier, webhooks)

**Copy implication:** Forms can be styled to match brand perfectly. Recommend clear microcopy for fields.

### Webflow E-commerce
Basic e-commerce with:
- Product pages
- Cart functionality
- Checkout
- Stripe/PayPal integration

**Limitations:**
- Limited variants (3 options max per product)
- Basic inventory management
- No complex discount rules

---

## Webflow-Specific Copy Considerations

### Rich Text Fields
Webflow CMS rich text fields support:
- Headers (H2-H6)
- Paragraphs
- Lists (ordered/unordered)
- Links
- Images
- Block quotes
- Code blocks

**Copy delivery:** Markdown format converts well to Webflow rich text.

### Character Limits
Webflow doesn't have strict limits, but consider:
- **Short text fields:** Define max length for CMS items (e.g., 100 chars for testimonial excerpts)
- **Rich text:** No limit, but performance degrades with very long content
- **Alt text:** No character limit, but keep under 125 for accessibility

### CMS Collection Structure
When creating copy for CMS-driven sections, document:
- Field names and types
- Character/word limits
- Required vs. optional fields
- Image specifications

**Example testimonial structure:**
```
Collection: Testimonials
Fields:
- Quote (Rich text, required) - Full testimonial
- Excerpt (Plain text, 150 char max) - For cards
- Author Name (Plain text, required)
- Author Title (Plain text)
- Company (Plain text)
- Photo (Image, square, min 200x200)
- Logo (Image, optional)
- Featured (Switch) - For homepage display
```

---

## SEO Considerations

### Webflow SEO Features
- Custom title tags per page
- Meta descriptions per page
- Open Graph settings
- Sitemap auto-generation
- 301 redirects
- Clean URLs

**Copy delivery:** Include SEO meta recommendations with each page.

### Limitations
- No native schema markup editor (requires custom code embed)
- Limited structured data options
- hreflang requires custom code

### Best Practices
- Set SEO fields in page settings
- Use proper heading hierarchy
- Configure alt text on all images
- Set up redirects for URL changes

---

## Interactions Best Practices

### What Webflow Does Well
- Scroll-triggered element reveals
- Hover state animations
- Page transitions
- Parallax effects
- Loading animations
- Mouse-following elements

### Copy Implications for Interactions
Document recommended animations in tech specs:

```
Hero Section:
- H1: Fade up from bottom, 0.3s ease-out, 0.1s delay
- Subheadline: Fade up, 0.3s, 0.2s delay
- CTA: Scale from 0.9 to 1, 0.3s, 0.4s delay
- Background image: Subtle parallax on scroll
```

### Performance Considerations
- Too many simultaneous animations impact performance
- Heavy interactions affect page weight
- Test on mobile devices (interactions may need mobile variants)

---

## Webflow-Specific Recommendations

### Templates and Libraries
Recommend using:
- **Relume Library:** Pre-built sections that speed development
- **Finsweet solutions:** Extend Webflow functionality
- **Client-First:** Naming convention for maintainability

### Multi-Language Sites
Webflow doesn't have native multi-language. Options:
- Weglot (translation layer)
- Manual duplicate pages/folders
- Third-party CMS integrations

**Copy implication:** If multilingual needed, document translation workflow.

### Gated Content
For lead magnets and downloads:
- Forms can trigger "Thank You" page with download link
- Or use Zapier to send download via email
- Consider Memberstack for advanced gating

---

## Deliverable Format for Webflow

### Recommended Copy Delivery

**Page copy format:**
```markdown
## Page: Homepage

### SEO
- Title: [60 chars max]
- Meta Description: [155 chars max]
- OG Image: [recommend specifications]

### Hero Section
**H1 (class: hero-headline)**
[Headline copy]

**Subheadline (class: hero-subhead)**
[Subheadline copy]

**CTA Button (class: btn-primary)**
[Button text]

### [Next Section]
...
```

**CMS Collection format:**
```markdown
## Collection: Testimonials

### Item 1
- **Quote:** [Full quote]
- **Excerpt:** [Short version, 150 chars]
- **Author:** [Name]
- **Title:** [Job title]
- **Company:** [Company name]
- **Featured:** Yes/No
```

---

## Common Webflow Copy Scenarios

### Blog Setup
- CMS collection for posts
- Category taxonomy
- Author collection (for multi-author)
- Rich text for post body
- Excerpt for cards/listings

### Case Studies
- CMS collection with:
  - Client name
  - Industry
  - Challenge summary
  - Solution summary
  - Results (with metrics)
  - Full story (rich text)
  - Featured images

### Team Pages
- CMS collection with:
  - Name, title, photo
  - Bio (rich text or plain text)
  - Social links
  - Department/category
  - Order/sort field

---

## Webflow Limitations to Work Around

| Limitation | Workaround |
|------------|------------|
| No native comments on blog | Disqus, CommentBox, or remove |
| Limited search | Jetboost or Finsweet search |
| No password-protected pages | Memberstack |
| Complex filters | Jetboost or Finsweet filters |
| Multi-language | Weglot |
| Advanced e-commerce | Snipcart or Shopify integration |

---

## Resources

- **Webflow University:** university.webflow.com
- **Relume Library:** relume.io
- **Finsweet:** finsweet.com
- **Client-First:** finsweet.com/client-first
