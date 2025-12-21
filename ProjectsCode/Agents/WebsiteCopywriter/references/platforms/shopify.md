# Shopify Platform Guide

Copy and implementation considerations for Shopify stores.

---

## Platform Overview

**Best for:** E-commerce businesses of all sizes, product-focused sites
**Strengths:** Powerful e-commerce features, app ecosystem, reliable hosting, built-in payments
**Limitations:** Theme customization constraints, monthly fees, transaction fees (non-Shopify Payments)

---

## Shopify Plans

| Plan | Key Features |
|------|--------------|
| Basic | 2 staff accounts, basic reports |
| Shopify | 5 staff accounts, professional reports |
| Advanced | 15 staff accounts, advanced reports, lower card rates |
| Plus | Enterprise features, unlimited staff, checkout customization |

**Copy implication:** Some features (like checkout customization) only available on higher plans.

---

## Native Features to Leverage

### Product Pages
Shopify product pages include:
- Product title
- Description (short and/or long)
- Variants (size, color, etc.)
- Images with alt text
- SEO title and description
- Tags and collections

### Collections
Group products by:
- Category
- Season
- Sale
- Best sellers
- Custom conditions

**Copy needed:** Collection titles and descriptions.

### Pages
Standard CMS pages for:
- About us
- Contact
- FAQ
- Policies
- Custom landing pages

### Blog
Built-in blog for content marketing:
- Posts with rich text
- Categories (tags)
- SEO fields
- Comments (optional)

### Checkout
Shopify checkout includes:
- Order summary
- Shipping options
- Payment fields
- Trust signals

**Customization limited** (especially on non-Plus plans).

---

## Shopify-Specific Copy Considerations

### Character Limits

| Field | Limit |
|-------|-------|
| Product title | 255 characters |
| Product description | No limit (but keep scannable) |
| Collection title | 255 characters |
| Collection description | No limit |
| SEO title | 70 characters |
| Meta description | 320 characters (155 recommended) |
| Alt text | 512 characters |
| Page title | 255 characters |
| Blog post title | 255 characters |

### Product Description Best Practices

**Short description (if theme supports):**
- 2-3 sentences
- Key benefit focus
- Appears near price/buy button

**Long description:**
- Features and benefits
- Use cases
- Materials/specifications
- Size guide (if applicable)
- Care instructions (if applicable)

### Formatting Options
Shopify rich text editor supports:
- Headings (H1-H6)
- Bold, italic
- Lists (ordered/unordered)
- Links
- Tables
- Images (embedded)

**HTML supported** for advanced formatting.

---

## E-commerce Copy Elements

### Product Page Copy

**Required elements:**
```markdown
## Product: [Product Name]

### Title
[Product name, include key identifier/descriptor]

### Short Description
[2-3 sentences, appears above fold near price]

### Full Description
[Comprehensive product info, benefits, features]

### SEO
- **Title Tag:** [70 chars max]
- **Meta Description:** [155 chars]

### Media
- **Images:** [List images needed with descriptions]
- **Alt Text:** [Alt text for each image]

### Variants
[If applicable: sizes, colors, etc. with any variant-specific copy]

### Add-On Copy
- **Add to Cart:** [Button text if customizable]
- **Out of Stock:** [Messaging]
- **Quantity Limit:** [If applicable]
```

### Collection Page Copy

```markdown
## Collection: [Collection Name]

### Title
[Collection name]

### Description
[1-2 paragraphs explaining the collection]

### SEO
- **Title Tag:** [70 chars]
- **Meta Description:** [155 chars]

### Sorting/Filters
[Any specific filter labels if customizable]
```

### Cart Page Copy

| Element | Example Copy |
|---------|--------------|
| Empty cart | "Your cart is empty. Continue shopping to find something you love." |
| Cart title | "Your Cart" or "Shopping Bag" |
| Subtotal label | "Subtotal" |
| Shipping note | "Shipping calculated at checkout" |
| Checkout button | "Proceed to Checkout" |
| Continue shopping | "Continue Shopping" |

### Checkout Copy (Limited on Non-Plus)

| Element | Example |
|---------|---------|
| Contact heading | "Contact information" |
| Shipping heading | "Shipping address" |
| Shipping method | "Shipping method" |
| Payment heading | "Payment" |
| Complete order | "Pay now" / "Complete order" |

**Trust signals:**
- "Secure checkout"
- "Your payment is protected"
- Money-back guarantee messaging

---

## SEO Considerations

### Shopify SEO Features
- Customizable title tags and meta descriptions
- Auto-generated sitemap
- 301 redirects via URL redirects
- Canonical URLs
- SSL included

### Shopify SEO Limitations
- URL structure has prefixes (/products/, /collections/, /pages/)
- Limited schema markup without apps
- Pagination can cause issues
- Duplicate content from variants/collections

### SEO Best Practices
- Optimize all product titles and descriptions
- Use descriptive collection names
- Add alt text to all images
- Create blog content for informational keywords
- Build internal links between products and content

---

## Shopify Theme Considerations

### Theme Sections
Modern Shopify themes (2.0+) use sections:
- Header
- Hero/Slideshow
- Featured collection
- Image with text
- Testimonials
- Newsletter
- Footer

**Copy implication:** Document copy for each section type.

### Theme Limitations
Copy implementation depends on theme:
- Some themes have limited text customization
- Animation options vary
- Mobile responsiveness is theme-dependent

**Before writing:** Review theme capabilities in demo/docs.

### Common Theme Areas

| Section | Copy Needed |
|---------|-------------|
| Announcement bar | Promo message, shipping threshold |
| Header | Logo alt, menu items, cart label |
| Footer | About text, newsletter CTA, policy links |
| Pop-ups | Email capture, exit intent |
| Product badges | Sale, new, bestseller labels |

---

## Shopify Apps for Extended Copy

### Email Marketing
**Klaviyo, Mailchimp, etc.:**
- Welcome series copy
- Abandoned cart emails
- Post-purchase emails
- Newsletter templates

### Reviews
**Judge.me, Yotpo, etc.:**
- Review request email copy
- Thank you page prompts
- Review display settings

### Upsell/Cross-sell
**ReConvert, Zipify, etc.:**
- Upsell offer headlines
- Cross-sell recommendations
- Post-purchase offer copy

### Loyalty Programs
**Smile.io, LoyaltyLion, etc.:**
- Points explanation
- Tier descriptions
- Reward descriptions

---

## Email and Notification Copy

### Shopify Notifications
Customize these in Settings > Notifications:

| Notification | Copy Elements |
|--------------|---------------|
| Order confirmation | Subject line, body, CTA |
| Shipping confirmation | Subject, tracking info framing |
| Delivery confirmation | Subject, review request |
| Abandoned checkout | Subject, reminder copy, CTA |
| Customer welcome | Subject, intro, next steps |
| Password reset | Subject, instructions |

### Email Best Practices
- Clear subject lines (under 50 chars)
- Branded header/footer
- Mobile-optimized formatting
- Clear CTAs
- Include contact info

---

## Conversion Optimization Elements

### Trust Signals
- Payment icons
- Security badges
- Money-back guarantee
- Free shipping threshold
- Customer count/reviews
- Social proof notifications

### Urgency/Scarcity
- Low stock indicators
- Sale countdown
- Limited edition messaging
- Cart reservation timer

### Copy for These Elements
Document messaging for:
- "Only X left in stock"
- "Sale ends in [countdown]"
- "Free shipping on orders over $X"
- "30-day money-back guarantee"

---

## Content Delivery Format

### Product Import Format
For bulk product uploads:
```csv
Handle, Title, Body (HTML), Vendor, Type, Tags, Published, Option1 Name, Option1 Value, Variant Price, Image Src, Image Alt Text, SEO Title, SEO Description
```

### Page Copy Format
```markdown
## Page: About Us

**URL Handle:** about-us

### SEO
- **Title:** About [Brand] | Our Story
- **Description:** [155 chars]

### Content
[Full page content with HTML formatting if needed]
```

---

## Shopify Limitations to Work Around

| Limitation | Workaround |
|------------|------------|
| URL structure | Can't change /products/, /collections/ prefixes |
| Checkout customization | Shopify Plus or post-purchase apps |
| Limited blog features | Blog app or link to external blog |
| Schema markup | SEO apps (JSON-LD for SEO, etc.) |
| Landing page flexibility | PageFly, Shogun, or custom theme sections |
| Multi-language | Translate & Adapt app or Langify |

---

## Resources

- **Shopify Help Center:** help.shopify.com
- **Shopify Blog:** shopify.com/blog
- **Shopify Theme Docs:** shopify.dev/themes
- **Shopify Email Templates:** shopify.com/blog/email-templates
