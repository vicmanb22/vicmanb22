# Website Copywriter

A Claude Code agent for creating high-converting website copy and page structure.

## How to Use

Invoke the agent with `@website-copywriter` at any time to:
- **Start a new project** - The agent will create a project folder and guide you through discovery
- **Continue an existing project** - Pick up where you left off, work on new pages
- **Improve existing copy** - Revise and optimize pages you've already created
- **Incorporate new materials** - Update copy based on new reference materials you've added

## Project Structure

Each website project gets its own folder in `/Users/vic-gini/ProjectsCode/Projects/`:

```
/Users/vic-gini/ProjectsCode/Projects/[ProjectName]/
├── copy/                    # Final approved copy files
│   ├── homepage-copy.md
│   ├── pricing-copy.md
│   └── ...
├── references/              # Project-specific context (you add these!)
│   ├── brand/              # Brand guidelines, style guides
│   ├── content/            # Existing website content, blog posts
│   ├── competitors/        # Competitor analysis notes
│   ├── seo/                # Keyword research, GSC data, analytics
│   └── README.md
├── README.md               # Project overview
└── open-questions.md       # Unanswered questions tracker
```

### Open Questions Tracker

The `open-questions.md` file tracks discovery questions that:
- Weren't answered during discovery
- Received incomplete responses
- Arose during copy creation

**Categorized by priority:**
- **Critical** - Blocking progress on copy
- **Important** - Would significantly improve quality
- **Nice to have** - Would enhance but not essential

Review this file anytime and provide answers. The agent checks it each session and updates it as questions are resolved.

### Adding Reference Materials

Drop files into the project's `references/` folder anytime. The agent will read them during research:
- **brand/** - PDFs, docs with brand guidelines, tone of voice, terminology
- **content/** - Existing website copy, blog posts, marketing materials
- **competitors/** - Notes, screenshots, URLs of competitor sites
- **seo/** - Keyword spreadsheets, Search Console exports, analytics data

## Agent Architecture

### Main Agent
`@website-copywriter` - Orchestrates the copy creation process

### Subagents
The main agent can use specialized subagents for efficiency:

| Subagent | Purpose |
|----------|---------|
| `project-setup` | Creates new project folder structure |
| `competitor-analyzer` | Deep analysis of competitor websites |
| `seo-researcher` | Keyword research and SEO strategy |
| `copy-reviewer` | Reviews copy against frameworks and best practices |

## Reference Knowledge Base

The agent consults TWO reference sources:

### 1. Agent Knowledge Base

Located at `/Users/vic-gini/ProjectsCode/Agents/WebsiteCopywriter/references/`:

| Folder | Contents |
|--------|----------|
| `frameworks/` | Cialdini's 7 Principles, AIDA, PAS, Buyer Awareness Levels (all cross-referenced) |
| `best-practices/` | Headlines, CTAs, Social Proof, Landing Pages, Page Structure, Technical Specs, SEO Checklist, Accessibility, Mobile Copy, **Help Center** |
| `discovery/` | Discovery questions template |
| `templates/` | Response templates, error handling |
| `platforms/` | Webflow, WordPress, Shopify, Squarespace guides |
| `page-types/` | Homepage, Pricing, About, Product/Service guides |
| `interviews/` | Expert insights: AEO guide, **Wes Kao communication frameworks** |
| `case-studies/` | High-converting site examples |
| `industry/` | Industry-specific guidance |
| `glossary.md` | **Definitions of all terms and acronyms** |

### 2. Project-Specific References

Materials you provide in each project's `references/` folder.

**The agent cites sources** when making recommendations:
> "Using the PAS framework (see `references/frameworks/pas-framework.md`)..."
> "Based on your brand guidelines (see `[project]/references/brand/style-guide.pdf`)..."

## Agent Capabilities

| Capability | Description |
|------------|-------------|
| Project Setup | Creates folder structure (via subagent or manually) |
| Discovery | Gathers goals, audience, competitors, brand guidelines |
| Research | Consults frameworks, analyzes competitors, searches best practices |
| Copy Creation | Provides 2-3 variants per section with strategic reasoning |
| SEO Integration | Keyword optimization, meta descriptions, AEO considerations |
| Technical Specs | Animation suggestions, mobile considerations, A/B testing |
| Copy Review | Reviews against frameworks via subagent |
| Continuous Improvement | Return anytime to revise or add pages |

## Standard Section Order

For standard section order, see `references/best-practices/page-structure.md`. The file contains detailed guidance on section ordering, variations by page type, and mobile considerations.

## Platform Support

Platform-specific guides available for:
- **Webflow** - Native interactions, CMS, forms
- **WordPress** - Gutenberg, plugins, WooCommerce
- **Shopify** - E-commerce copy, product pages, checkout
- **Squarespace** - Template sections, limitations

## Page-Type Guides

Specialized guidance for:
- **Homepage** - Value proposition, conversion flow
- **Pricing** - Plan presentation, FAQ, objection handling
- **About** - Mission, story, team, values
- **Product/Service** - Features vs benefits, use cases

## Output Format

- One markdown file per page in `[project]/copy/`
- Naming convention: `[page-name]-copy.md`
- Includes: SEO meta, copy sections, technical specs, A/B testing notes

## Quality Standards

### Required
- Ask for goals before writing any copy
- Provide 2-3 variants per section (never just one)
- Include strategic reasoning for each variant
- Consult both agent and project references
- Include SEO considerations
- Suggest moving on after 3 revisions per section

### Forbidden
- Never proceed without understanding goals and audience
- Never provide only one option
- Never ignore brand guidelines if provided
- Never skip the discovery phase

## Maintaining Changelog & Plan

This project uses `CHANGELOG.md` and `PLAN.md` for tracking.

**⚠️ IMPORTANT: Always update CHANGELOG.md immediately and automatically after making ANY changes to project files — including templates, prompts, configuration files, system files, or any other project assets. Do NOT wait for the user to ask. This must happen automatically after every change.**

### When working on this project:
1. Check PLAN.md at the start to see current priorities
2. **Update CHANGELOG.md immediately after completing any changes** (under `## [Unreleased]`)
3. Move completed items from Current Focus to Completed in PLAN.md

### Changelog categories:
Added, Changed, Deprecated, Removed, Fixed, Security

### Entry format:
`- (YYYY-MM-DD HH:MM) Description of change`

### Plan sections:
- **Current Focus** - Active work (1-3 items max)
- **Backlog** - Future ideas
- **Completed** - Done items
