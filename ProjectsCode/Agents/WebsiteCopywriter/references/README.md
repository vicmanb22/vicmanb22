# Website Copywriter Reference Knowledge Base

This folder contains reference materials that the website-copywriter agent consults when creating copy. The agent reads these files during its research phase and cites them when making recommendations.

## Folder Structure

```
references/
├── frameworks/           # Strategic copywriting frameworks (all cross-referenced)
│   ├── cialdini-principles.md      # 7 principles of persuasion
│   ├── buyer-awareness-levels.md   # Eugene Schwartz's 5 levels
│   ├── aida-framework.md           # Attention-Interest-Desire-Action
│   └── pas-framework.md            # Problem-Agitate-Solution
├── best-practices/       # Conversion & copywriting best practices
│   ├── headlines.md                # Research-backed headline guidelines
│   ├── ctas.md                     # Call-to-action optimization
│   ├── social-proof.md             # Testimonials, logos, reviews
│   ├── landing-pages.md            # Landing page optimization
│   ├── page-structure.md           # Section ordering and layout
│   ├── technical-specs.md          # Animations, interactions
│   ├── seo-checklist.md            # On-page SEO
│   ├── accessibility.md            # WCAG guidelines
│   ├── mobile-copy.md              # Mobile-first copy
│   └── help-center.md              # Help documentation best practices
├── discovery/            # Discovery phase resources
│   └── discovery-questions.md      # Comprehensive question template
├── templates/            # Response templates
│   ├── response-templates.md       # Standard response formats
│   └── error-responses.md          # Error handling templates
├── platforms/            # Platform-specific guides
│   ├── webflow.md
│   ├── wordpress.md
│   ├── shopify.md
│   └── squarespace.md
├── page-types/           # Page-specific guidance
│   ├── homepage.md
│   ├── pricing.md
│   ├── about.md
│   └── product-service.md
├── interviews/           # Expert insights
│   ├── aeo-guide-ethan-smith-jeanne-dewitt-grosser.md  # Answer Engine Optimization
│   └── wes-kao-website-copy-communication-guide.md     # Communication frameworks
├── case-studies/         # High-converting site examples
│   └── README.md
├── industry/             # Industry-specific guidance
│   └── README.md
├── glossary.md           # Definitions of all terms and acronyms
└── README.md             # This file
```

## How the Agent Uses These References

1. **Research Phase**: Agent uses `Glob: references/**/*.md` to find relevant files
2. **Reading**: Agent reads applicable frameworks and best practices
3. **Citation**: Agent cites sources when making recommendations

**Example citation:**
> "Using the PAS framework (see `references/frameworks/pas-framework.md`), I recommend leading with the problem before introducing your solution..."

## Adding New References

### Frameworks
Add new copywriting/marketing frameworks to `frameworks/`. Include:
- Framework name and origin
- Core principles or steps
- When to use it
- Examples

### Best Practices
Add topic-specific best practices to `best-practices/`. Include:
- Key principles with explanations
- Do's and don'ts
- Examples
- Sources/citations

### Interviews & Podcasts
Add synopses to `interviews/`. Include:
- Expert name and credentials
- Source (podcast, interview, article)
- Key insights (bulleted)
- Actionable takeaways

### Case Studies
Add site analyses to `case-studies/`. Include:
- Site URL and industry
- What they do well
- Specific techniques used
- Results (if available)

### Industry-Specific
Add industry guidance to `industry/`. Include:
- Industry name
- Unique considerations
- Regulatory/compliance notes
- Common objections and how to address them
- Successful patterns in that industry

## Cross-Referencing

All files are cross-referenced. When consulting a file, follow related references for deeper context:

**Framework → Framework connections:**
- PAS works best for "Problem-Aware" audiences (see buyer-awareness-levels.md)
- AIDA + Cialdini principles enhance each stage
- All frameworks reference each other's "When to Use" sections

**Best Practice → Framework connections:**
- Social proof references Cialdini's principles
- Headlines reference buyer awareness for targeting
- CTAs reference AIDA's Action stage

**Interview → Best Practice connections:**
- Wes Kao's MOO framework applies to objection handling across pages
- AEO guide Part 6 informs help-center.md

## Maintenance

- Keep files up to date with current best practices
- Add new insights as they're discovered
- Remove outdated information
- Maintain cross-references when adding new content
- Check glossary.md when introducing new terms
