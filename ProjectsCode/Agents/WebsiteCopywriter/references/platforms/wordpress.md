# WordPress Platform Guide

Copy and implementation considerations for WordPress sites.

---

## Platform Overview

**Best for:** Content-heavy sites, blogs, membership sites, WooCommerce e-commerce
**Strengths:** Massive plugin ecosystem, SEO flexibility, content management, scalability
**Limitations:** Theme-dependent design, requires hosting management, security maintenance

---

## WordPress Variants

### WordPress.org (Self-Hosted)
- Full control and flexibility
- Requires hosting, maintenance, updates
- Access to all plugins and themes
- Custom development possible

### WordPress.com
- Managed hosting
- Limited plugin access (Business plan+ for plugins)
- Less flexibility but easier maintenance

**Copy implication:** Determine which variant and plan level—affects available features.

---

## Native Features to Leverage

### Gutenberg Block Editor
Modern block-based editor supports:
- Headings, paragraphs, lists
- Images, galleries, videos
- Buttons, columns, groups
- Custom blocks via plugins
- Reusable blocks for repeated content

**Copy implication:** Format copy to match block structure. Each element maps to a block.

### WordPress SEO (with Plugins)
With Yoast SEO or Rank Math:
- Title tag optimization
- Meta description editing
- Schema markup
- XML sitemaps
- Breadcrumbs
- Social media previews

**Copy implication:** Include full SEO recommendations—WordPress makes optimization easy.

### Custom Post Types
Beyond posts and pages:
- Testimonials
- Case studies
- Team members
- Products (WooCommerce)
- Portfolio items

**Copy implication:** Define content structure for each post type.

### Taxonomies
Categories and tags for:
- Blog organization
- Product filtering
- Content relationships

---

## WordPress-Specific Copy Considerations

### Theme Limitations
Copy implementation depends heavily on theme:
- **Page builders (Elementor, Divi, Beaver):** High flexibility
- **Block themes:** Good flexibility with Gutenberg
- **Classic themes:** May have fixed layouts

**Before writing:** Understand theme capabilities and any constraints.

### Character Limits

| Element | Typical Limit |
|---------|--------------|
| Post title | No hard limit, but 60 chars for SEO |
| Excerpt | 55 words (default), often customizable |
| Menu items | ~25 characters comfortable |
| Widget titles | Varies by theme |

### Media Library
- Images uploaded to central library
- Alt text required for each image
- Can specify image sizes for different contexts

---

## Plugin Ecosystem

### SEO Plugins
**Yoast SEO or Rank Math:**
- Copy delivery should include meta fields
- Both support keyword focus and readability analysis
- Schema markup built-in

### Page Builder Plugins
**Elementor, Divi, Beaver Builder:**
- Allow custom layouts without code
- Copy can specify more precise element positioning
- May have their own animation options

### Form Plugins
**Contact Form 7, Gravity Forms, WPForms:**
- Document form fields and copy
- Success/error messages
- Email notification copy

### E-commerce
**WooCommerce:**
- Product descriptions (short and long)
- Add to cart button text
- Checkout field labels
- Order confirmation copy
- Email templates

### Membership/LMS
**MemberPress, LearnDash:**
- Course descriptions
- Lesson content
- Membership level copy
- Access messaging

---

## SEO Considerations

### WordPress SEO Strengths
- Excellent permalink structure control
- Easy meta management with plugins
- Built-in XML sitemaps
- Schema markup support
- Mobile-responsive themes
- Fast hosting options

### Technical SEO Checklist
- [ ] SEO plugin installed and configured
- [ ] Permalinks set to "Post name"
- [ ] XML sitemap generated
- [ ] Robots.txt configured
- [ ] SSL certificate active
- [ ] Caching plugin for performance

### Copy-Level SEO
- Title tags (include in page settings)
- Meta descriptions
- Header hierarchy (H1-H6)
- Alt text for images
- Internal linking strategy

---

## Content Structure for WordPress

### Blog Posts

**Standard fields:**
```
- Title (H1)
- Permalink (slug)
- Featured image + alt text
- Excerpt (for archives)
- Categories
- Tags
- SEO title
- Meta description
- Body content (Gutenberg blocks)
```

**Copy delivery format:**
```markdown
## Blog Post: [Title]

**URL Slug:** /blog/[slug]
**Category:** [Category]
**Tags:** [Tag1, Tag2]

### SEO
- **Title Tag:** [60 chars]
- **Meta Description:** [155 chars]
- **Focus Keyword:** [Primary keyword]

### Featured Image
[Image description for sourcing, alt text]

### Excerpt
[2-3 sentence summary for archive pages]

### Content
[Full post content with headers, images, etc.]
```

### Pages

**Copy delivery format:**
```markdown
## Page: [Page Name]

**URL:** /[page-slug]
**Parent:** [If child page]
**Template:** [If specific template]

### SEO
- **Title Tag:** [60 chars]
- **Meta Description:** [155 chars]

### Content

#### [Section/Block 1]
[Content]

#### [Section/Block 2]
[Content]
```

### Custom Post Types

Document structure for each:
```markdown
## Post Type: Testimonials

### Fields
- **Quote** (Text area) - Full testimonial
- **Author** (Text) - Customer name
- **Company** (Text) - Company name
- **Rating** (Number, 1-5) - Star rating
- **Featured Image** - Customer photo

### Example Entry
[Sample content for each field]
```

---

## WooCommerce Considerations

### Product Copy

**Required for each product:**
```markdown
## Product: [Product Name]

**SKU:** [If applicable]
**Categories:** [Product categories]

### Short Description
[2-3 sentences, appears near price]

### Long Description
[Full product details, features, specifications]

### SEO
- **Title Tag:** [60 chars]
- **Meta Description:** [155 chars]

### Additional
- **Button Text:** [If custom, e.g., "Add to Cart"]
- **Sale Badge:** [If applicable]
```

### Shop Page Elements
- Product category descriptions
- Sale/promotion banners
- Empty cart messaging
- Related products heading

### Checkout Copy
- Field labels
- Help text
- Error messages
- Order summary
- Payment method descriptions
- Confirmation page

---

## Theme-Specific Considerations

### Common Theme Areas

| Area | Copy Needed |
|------|-------------|
| Header | Logo alt text, menu items |
| Footer | Widget content, copyright, links |
| Sidebar | Widget titles and content |
| 404 page | Error message, suggestions |
| Search results | No results message |
| Archive pages | Category/tag descriptions |

### Page Builder Sections
For Elementor/Divi/etc., document:
- Section purpose
- Content for each element
- Animation suggestions (if supported)
- Mobile adjustments

---

## WordPress Limitations to Work Around

| Limitation | Workaround |
|------------|------------|
| Limited design flexibility | Page builder plugin |
| Basic forms | Form plugin (Gravity, WPForms) |
| No native interactions | Animation plugins or custom CSS |
| Multi-language | WPML or Polylang |
| Performance issues | Caching, CDN, optimization plugins |
| Limited CMS structure | Advanced Custom Fields (ACF) |

---

## Maintenance Considerations

### Content Update Process
- WordPress admin access required
- Content can be scheduled
- Revisions tracked automatically
- Multiple user roles (Editor, Author, etc.)

### Copy Implications
- Train client on content updates
- Create style guide for ongoing content
- Document CMS field usage
- Consider editorial workflow needs

---

## Resources

- **WordPress.org:** wordpress.org/support/
- **Yoast SEO Academy:** yoast.com/academy/
- **Elementor Academy:** elementor.com/academy/
- **WooCommerce Docs:** woocommerce.com/documentation/
