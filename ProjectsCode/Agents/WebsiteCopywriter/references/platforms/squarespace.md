# Squarespace Platform Guide

Copy and implementation considerations for Squarespace sites.

---

## Platform Overview

**Best for:** Portfolios, creative businesses, small business sites, simple e-commerce
**Strengths:** Beautiful templates, all-in-one hosting, easy maintenance, built-in features
**Limitations:** Less flexible than code-based platforms, limited app ecosystem, template constraints

---

## Squarespace Plans

| Plan | Key Features |
|------|--------------|
| Personal | Basic site features, no e-commerce |
| Business | Unlimited pages, basic e-commerce, custom CSS |
| Basic Commerce | Full e-commerce, no transaction fees |
| Advanced Commerce | Subscriptions, abandoned cart, advanced e-commerce |

**Copy implication:** E-commerce features depend on plan level.

---

## Native Features to Leverage

### Page Types
- **Standard pages:** Custom layouts with blocks
- **Blog pages:** Posts with comments
- **Store pages:** Product listings
- **Portfolio pages:** Gallery-style layouts
- **Cover pages:** Full-screen landing pages

### Section-Based Design
Modern templates use sections:
- Each page built from stackable sections
- Templates provide section layouts
- Some customization within sections
- Limited ability to create completely custom layouts

### Built-in Features
- Contact forms
- Newsletter signup
- Social media integration
- SEO tools
- Analytics
- Scheduling (Acuity integration)

---

## Squarespace-Specific Copy Considerations

### Character Limits

| Element | Recommendation |
|---------|---------------|
| Site title | 60 characters |
| Page title | 60 characters |
| SEO description | 160 characters |
| Navigation items | 20-25 characters |
| Button text | 15-25 characters |

### Block Types
Squarespace content built with blocks:
- **Text blocks:** Main content
- **Image blocks:** Photos with captions
- **Button blocks:** CTAs
- **Quote blocks:** Testimonials, pullquotes
- **Form blocks:** Contact, signup
- **Video blocks:** Embedded video
- **Gallery blocks:** Image collections

**Copy implication:** Structure copy to match block format.

### Template Considerations
Each template has:
- Fixed layout options
- Pre-designed section types
- Specific font/color options
- Mobile behavior presets

**Before writing:** Know which template is being used.

---

## Content Structure for Squarespace

### Page Copy Format

```markdown
## Page: [Page Name]

**Page URL:** /[slug]
**Template Section:** [If applicable]

### SEO
- **Title Tag:** [60 chars]
- **Meta Description:** [160 chars]

### Navigation
- **Menu Label:** [How it appears in navigation]

### Content Sections

#### Section 1: [Section Type, e.g., "Hero Banner"]
- **Headline:** [Copy]
- **Subheadline:** [Copy]
- **Button Text:** [CTA]
- **Background:** [Image description or color]

#### Section 2: [Section Type]
- [Content formatted for section type]
```

### Blog Post Format

```markdown
## Blog Post: [Title]

**URL Slug:** /blog/[slug]
**Categories:** [Category tags]
**Excerpt:** [Summary for listings, ~150 chars]

### SEO
- **Title Tag:** [60 chars]
- **Meta Description:** [160 chars]

### Featured Image
[Image description, alt text]

### Content
[Full post content]

### Tags
[Tags for organization]
```

### Product Format (E-commerce)

```markdown
## Product: [Product Name]

**SKU:** [If applicable]
**Category:** [Product category]
**Price:** [Price]

### Product Images
[List images with descriptions and alt text]

### Description
[Product description - Squarespace uses simple formatting]

### SEO
- **Title:** [60 chars]
- **Description:** [160 chars]

### Variants
[If applicable: sizes, colors, options]
```

---

## SEO in Squarespace

### Built-in SEO Features
- Custom page titles
- Meta descriptions
- URL slugs
- Image alt text
- Auto-generated sitemap
- SSL included
- Mobile-responsive themes

### SEO Settings Location
- **Site-wide:** Settings > SEO
- **Per-page:** Page settings > SEO
- **Per-image:** Image settings > alt text
- **Per-product:** Product settings > SEO

### SEO Limitations
- Limited schema markup options
- No custom robots.txt
- URL structure has some constraints
- Limited technical SEO controls

---

## E-commerce Copy Elements

### Product Pages

**Elements to write:**
- Product title
- Product description (limited formatting)
- Variant names (Size: S, M, L, XL)
- Additional info sections
- Related products heading

### Cart and Checkout

| Element | Squarespace Default | Customization |
|---------|--------------------| --------------|
| Add to cart | "Add to Cart" | Customizable |
| Cart | "Cart" | Limited |
| Checkout | Squarespace Checkout | Limited styling, copy mostly fixed |

### Order Notifications
Customize in Settings > Commerce > Notifications:
- Order confirmation
- Shipping notification
- Refund notification
- Digital download delivery

---

## Form Copy

### Contact Form
Squarespace forms allow:
- Custom field labels
- Placeholder text
- Required field indicators
- Submit button text
- Success message
- Error messages (limited)

### Newsletter Signup
- Headline
- Description text
- Submit button text
- Success message

### Copy Format for Forms
```markdown
## Form: Contact

### Fields
1. **Name** (Text, required)
   - Label: "Your Name"
   - Placeholder: "Full name"

2. **Email** (Email, required)
   - Label: "Email Address"
   - Placeholder: "you@example.com"

3. **Message** (Text area, required)
   - Label: "How can we help?"
   - Placeholder: "Tell us about your project..."

### Submit Button
"Send Message"

### Success Message
"Thanks for reaching out! We'll be in touch within 24 hours."
```

---

## Template-Specific Sections

### Common Section Types

| Section Type | Copy Elements |
|--------------|---------------|
| Hero/Banner | Headline, subheadline, button, background |
| About | Heading, body text, image caption |
| Services | Service titles, descriptions, icons |
| Team | Names, titles, bios |
| Testimonials | Quotes, attribution |
| FAQ | Questions, answers |
| Contact | Intro text, form labels, contact info |
| CTA | Headline, body, button |
| Footer | Tagline, contact, social, legal links |

### Section Copy Format
```markdown
## Section: Services

**Section Type:** Gallery/Grid
**Columns:** 3

### Service 1
- **Title:** [Service name]
- **Description:** [2-3 sentences]
- **Icon/Image:** [Description]
- **Link:** [If applicable]

### Service 2
[Same format]

### Service 3
[Same format]
```

---

## Squarespace Limitations to Work Around

| Limitation | Workaround |
|------------|------------|
| Template constraints | Choose template carefully before starting |
| Limited animations | Custom CSS (Business plan+) |
| No advanced forms | Embed third-party forms (Typeform, etc.) |
| Blog limitations | Work within Squarespace blog structure |
| E-commerce features | May need to integrate with external tools |
| Multi-language | Manual duplication or third-party tools |
| Custom functionality | Code injection or embed blocks |

---

## Cover Pages

Cover pages are single-page landing pages with:
- Full-screen background
- Centered content
- Limited but beautiful layouts
- Good for campaigns, coming soon, events

**Copy elements:**
- Headline (short, impactful)
- Subheadline (optional)
- Body text (brief)
- Button CTA
- Logo (optional)

---

## Mobile Considerations

### Squarespace Mobile Behavior
- All templates responsive
- Some mobile-specific settings
- Content stacks vertically
- Some sections collapse differently

### Copy for Mobile
- Headlines may wrap differently
- Keep CTAs short
- Test in Squarespace mobile preview
- Consider what's above fold on mobile

---

## Content Management

### Who Updates Content
- Squarespace is user-friendly
- Clients often update their own content
- Content blocks make editing intuitive
- No technical knowledge required

### Copy Implications
- Write clear section labels
- Create style guide for ongoing content
- Note which sections are for client editing
- Keep formatting simple and replicable

---

## Resources

- **Squarespace Help Center:** support.squarespace.com
- **Squarespace Forum:** forum.squarespace.com
- **Squarespace Circle:** Designer/developer resources
- **Template Documentation:** Check specific template docs
