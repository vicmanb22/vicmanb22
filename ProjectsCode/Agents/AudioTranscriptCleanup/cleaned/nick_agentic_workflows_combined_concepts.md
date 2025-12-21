# Nick's Agentic Workflows: Complete Learning Guide

**Source Videos:**
1. "The N8N Killer? AGENTIC WORKFLOWS: Full Beginner's Guide" (Nov 25, 2025)
2. "How to Automate ANY Service Business with Agentic Workflows (A-Z)" (Dec 2, 2025)

**Speaker:** Nick (Leftclick / Maker School)
- Scaled two agencies to $160,000+ combined revenue
- Runs Maker School (~$300,000/month in profit)
- Runs a dental marketing business (~$2M/year)
- Main company: Leftclick (B2B outbound marketing/cold email)

---

## Table of Contents

1. [What Are Agentic Workflows?](#1-what-are-agentic-workflows)
2. [The DOE Framework](#2-the-doe-framework-directive-orchestration-execution)
3. [The Stochasticity Problem](#3-the-stochasticity-problem)
4. [Self-Annealing Workflows](#4-self-annealing-workflows)
5. [The Complete Service Business Model](#5-the-complete-service-business-model-leftclick-case-study)
6. [Lead Generation & Enrichment](#6-lead-generation--enrichment-workflow)
7. [Proposal Generation](#7-proposal-generation-from-call-transcripts)
8. [Automated Onboarding](#8-automated-onboarding-sequence)
9. [Campaign Generation & Cold Email](#9-campaign-generation--cold-email-copy)
10. [Automated Reply System](#10-automated-reply-system)
11. [Knowledge Bases](#11-knowledge-bases)
12. [Meta Directives](#12-meta-directives)
13. [The 5-Step Automation Guide](#13-the-5-step-guide-to-automate-any-business)
14. [IDE Setup & Tools](#14-ide-setup--tools)
15. [Speed & Cost Analysis](#15-speed--cost-analysis)
16. [Key Principles & Philosophy](#16-key-principles--philosophy)

---

## 1. WHAT ARE AGENTIC WORKFLOWS?

### The Fundamental Shift

Traditional workflow platforms (Make.com, n8n, Zapier, Microsoft Power Automate) handle both **functions** and **logic** in a drag-and-drop interface:

**Traditional Approach:**
```
[Trigger] → [Function A] → [Logic: If/Then] → [Function B] → [Output]
     ↑                           ↑
     |                           |
  You define               You define
  the function           the routing logic
```

**Agentic Approach:**
```
[Functions A, B, C, D...] → [AI Agent] → [Output]
         ↑                       ↑
         |                       |
   You provide tools      AI handles ALL
   (or AI builds them)    routing & logic
```

### The Core Concept

With agentic workflows, you:
1. **Decouple functions from logic** — Take all the functions out of the routing
2. **Give functions to AI** — Assume AI is better at using and building tools than you
3. **Describe what you want** — "Hey, here's what I want to do. Can you do it using these functions?"

### Why Now?

Nick's claim: Until recently, "agent" was associated with hype and little business value. But now:
> "The tech is now good enough that agentic workflows are definitively here, and they are without a doubt the future of workflow building. I'm not exaggerating when I say these will quickly run the entire economy."

### What These Are NOT

These are not chatbots. Nick emphasizes:
> "These agents are not just chatbots. They are basically universal interfaces that let you control software."

---

## 2. THE DOE FRAMEWORK (Directive, Orchestration, Execution)

### Overview

DOE is Nick's recommended framework for building reliable agentic workflows. It's designed to constrain AI mistakes while leveraging AI strengths.

### The Three Layers in Detail

#### Layer 1: DIRECTIVE (The "What")

**Definition:** High-level instructions written in natural language that describe what needs to be done.

**Format:** Markdown files (.md) containing SOPs (Standard Operating Procedures)

**Key Characteristics:**
- Written like you're explaining to a new employee
- NO code whatsoever in this layer
- Defines guardrails and rules of engagement
- Describes the intent, goals, and boundaries

**Why Markdown?**
> "Markdown is just a way that you can format and add some form of structure to text without having to consume a ton of tokens."

**The Recipe Analogy:**
Think of directives like a recipe:
- Step 1: Add soy sauce, vinegar, and ingredients to container
- Step 2: Mix thoroughly
- Step 3: Heat for 10 minutes

These are high-level instructions that describe what to do without specifying exact implementation.

**Critical Insight:**
> "If you take the DOE approach, you could literally take a pre-existing list of all of the standard operating procedures in a business and just drag and drop them into your IDE and boom—you've already accomplished one of the three main layers."

#### Layer 2: ORCHESTRATION (The "Who")

**Definition:** The AI agent that reads directives, makes decisions, and routes tasks.

**The Reasoning Loop:**
The orchestrator continuously cycles through:
1. **READ** — Parse the directive and understand the task
2. **CHOOSE** — Select which action/tool to use next
3. **EXECUTE** — Run the selected action
4. **EVALUATE** — Assess the results
5. **LOOP** — Return to step 1 with new context

**Role in the System:**
- Acts as "glue" connecting directives to execution
- Functions like a mid-level manager
- Makes routing decisions dynamically
- Can go "upstream" and modify directives based on results

**The No-Code Platform Comparison:**
> "This orchestrator works very similarly to Make or n8n or Zapier. All of these drag-and-drop platforms are nothing more than glue which routes business logic through nodes. The orchestrator in this case is the Make, n8n, Zapier... It's just now what we're doing is replacing that orchestration with AI agents."

**Key Distinction:**
The orchestrator is NOT a file or folder—it's the LLM itself. Nick calls it "the big galaxy-brain intelligence" that reads directives, associates them with executables, and runs them in loops.

#### Layer 3: EXECUTION (The "How")

**Definition:** Deterministic code (typically Python scripts) that performs specific tasks reliably.

**Key Characteristics:**
- Scripts that run the same way every time
- Don't hallucinate—they either work or error out
- Can be caught and debugged when they fail
- Built by the AI, not necessarily by you

**Why Python?**
> "Python scripts tend to be the best just because Python is the language that most of these large language models were trained on initially. There's an overabundance of Python code out there and Python's used as artificial and synthetic data for a lot of these as well."

**The "You Don't Need to Code" Promise:**
Nick repeatedly emphasizes:
> "I don't actually know how to read most of this code. I don't worry about most of this code. That is the AI's job. The AI is much better at coding than I probably would ever be, even given a decade of learning."

### The Organizational Analogy

Nick maps DOE to traditional business structure:

| DOE Layer | Business Role | Function |
|-----------|--------------|----------|
| Directive | Manager | Sets strategy, writes SOPs, defines rules |
| Orchestration | Employee | Interprets instructions, makes tactical decisions |
| Execution | Tools | Machinery that does the actual work |

> "This is the exact same structure used by a lot of very successful human organizations."

### Folder Structure

```
workspace/
├── directives/
│   ├── scrape_leads.md
│   ├── create_proposal.md
│   ├── onboard_customer.md
│   ├── generate_campaigns.md
│   └── auto_reply.md
└── execution/
    ├── scrape_leads.py
    ├── enrich_leads.py
    ├── casualize_names.py
    ├── send_email.py
    └── create_pandadoc.py
```

**Note:** There's no "orchestration" folder because the orchestrator IS the LLM.

### DOE Summary Table

| Layer | Alias | Role | Contains | Key Property |
|-------|-------|------|----------|--------------|
| **Directive** | SOPs / Manager | The "What" | Markdown files with instructions | Natural language, no code |
| **Orchestration** | Agent / Employee | The "Who" | The LLM itself | Reasoning, routing, decisions |
| **Execution** | Code / Tools | The "How" | Python scripts | Deterministic, reliable |

---

## 3. THE STOCHASTICITY PROBLEM

### What Stochasticity Means

**Stochasticity** = Non-deterministic outputs. The same input can produce different outputs each time.

**The Core Conflict:**
- **LLMs are probabilistic** — They guess the next token based on probability
- **Business logic is deterministic** — You need the exact same output format every time

> "When you try and make an LLM do everything—which is planning, tool use, execution, formatting, whatever—the error rate compounds."

### Why This Kills Business Automation

Nick's example of cascading failures:

**Scenario:** Ask an LLM to scrape leads from LinkedIn
- Run 1: Works perfectly
- Run 2: Fails silently
- Run 3: Fails with different error
- Run 4: Hallucinates a completely different task
- Run 5: Says "Sorry, this is against regulations"

For hobbyists, 50% success rate might be acceptable. For businesses:
> "You cannot run a million-dollar-a-month operation on a system that only works most of the time."

### The Compounding Math

If each step has a 90% success rate:

| Steps | Calculation | Success Rate |
|-------|-------------|--------------|
| 1 step | 0.9^1 | 90% |
| 2 steps | 0.9^2 | 81% |
| 3 steps | 0.9^3 | 73% |
| 4 steps | 0.9^4 | 66% |
| 5 steps | 0.9^5 | **59%** |

> "This task where each individual step may be quite likely to succeed, on net, only has a 59% success rate, which is completely unacceptable for any real business operation."

### The Business Impact

Nick's stark warning:
> "In business, even a 1% rate of inaccuracy can lead to a revenue reduction of 50% or more. This is not academic theory. This is real life. If you send the wrong invoice, even 1% of the time, you don't hurt your business by 1%. You could completely destroy your whole client base."

**Example:** Automating invoice sending
- Send wrong invoice to wrong person
- Could lose a giant client contract
- 2% error rate ≠ 2% revenue loss
- 2% error rate could = 100% revenue loss

### The Solution: Architecture, Not Smarter AI

> "To fix this, we don't just try and make the LLM smarter. What we do is we actually fundamentally change the architecture around the LLM."

**The Key Insight:**
Instead of asking an LLM to DO something directly, ask it to CREATE CODE to do that thing:

```
Traditional: LLM → Direct Action → (Probabilistic) → Unreliable Output
DOE:         LLM → Creates Code → Code Executes → (Deterministic) → Reliable Output
```

> "A Python script does not hallucinate. It either works or it errors out. And if it errors out, we can catch it. All your agent has to do is decide when to run the thing."

### Flexibility vs. Determinism

Nick's diagram concept:

**Probabilistic (Bad for Business):**
- Arrows going all directions
- Flexible but uncertain outcomes
- Great for creative tasks
- Terrible for business pipelines

**Deterministic (Good for Business):**
- Clear, predictable paths
- If input X, then output Y
- Less flexible but reliable
- Essential for revenue-generating operations

> "Ultimately speaking, in a business, you don't want flexibility. In a business, you want determinism."

---

## 4. SELF-ANNEALING WORKFLOWS

### What Self-Annealing Means

Workflows that **maintain and improve themselves over time**. Unlike procedural workflows (build once, maintain forever), agentic workflows get better with use.

### The Improvement Curve

**First Run:** ~75% reliable (and that's okay)

Nick's progression:
| Run | Reliability | What Happens |
|-----|-------------|--------------|
| 1 | 75% | Initial build, some failures |
| 2 | 97% | Fixes major issues |
| 3 | 99% | Edge cases resolved |
| 4 | 99.99% | Near-perfect reliability |

> "It doesn't need to be 100% right the first time because this isn't running the workflow like once and then it forgets about it. This thing is just building a thing and then it's running the workflow and testing it and then you're going to use that information to build it again."

### The Minecraft Analogy (Detailed)

Nick uses Minecraft to explain tool evolution:

**Starting Point:**
- Empty execution folder
- No tools at all
- Like starting Minecraft with nothing

**Early Game:**
- Agent builds basic scripts (wooden pickaxe)
- Simple, functional, not optimized
- Gets the job done

**Mid Game:**
- Scripts get reinforced (stone tools)
- Error handling added
- Edge cases covered

**Late Game:**
- Optimized code (diamond tools)
- Batch endpoints instead of one-off calls
- O(n) instead of O(n²) complexity
- Maximum efficiency

> "Once it's made these, it can then go back and reinforce these and then it can upgrade them. And eventually you can get to your little diamond fortification where your stuff is just really really good."

**Specific Improvements Over Time:**
- Replace one-off endpoints with bulk/batch endpoints
- Economize code to run faster
- Improve Big O complexity
- Add caching and optimization

### The Caveman Analogy

**Scenario:** Caveman vs. saber-tooth tiger

**First Encounter:**
- Tries punching (ineffective)
- Finds rock, throws it (marginally better)
- Survives but barely

**Learning:**
- Goes home, makes a spear
- Basic, but functional

**Second Encounter:**
- Uses the spear
- Much more effective

**Over Time:**
- Spear gets reinforced
- Techniques improve
- Eventually: sophisticated weapons

> "As you eventually do this more and more and more, your spear is going to get better, more reinforced. It's going to be more capable."

### Real-World Self-Annealing Example

During Nick's demo, an API key was deprecated:

**In Procedural Workflow (Make/n8n):**
- Workflow errors out
- Requires manual intervention
- Dead in the water until fixed

**In Agentic Workflow:**
1. Detected the deprecated key failure
2. Searched for alternative keys in the system
3. Found another valid key stored elsewhere
4. Updated its own documentation to reference correct key
5. Continued execution successfully

Nick's reaction:
> "This workflow almost healed, you know, it's like Wolverine or something like that. It gets shot and then the skin comes back."

### The Testing Loop

The self-annealing process in action:

```
1. Agent attempts task
2. If failure:
   a. Analyze what went wrong
   b. Generate fix
   c. Update code/documentation
   d. Retry
3. If success:
   a. Store successful approach
   b. Apply learnings to future runs
4. Loop continues until stable
```

> "If it tests it once and then it doesn't figure it out, then it's just going to continue running until it does figure it out. And then boom, you now have your working workflow."

---

## 5. THE COMPLETE SERVICE BUSINESS MODEL (Leftclick Case Study)

### Business Overview

**Company:** Leftclick
**Type:** B2B outbound marketing / cold email agency
**Clients:** Small businesses to multi-billion dollar portfolio companies
**Value Proposition:** Increase top-of-funnel leads through cold email campaigns

### The 11-Step Fulfillment Process

Nick reveals "all the sauce" of how Leftclick operates:

#### Step 1: Sales Call with Prospect
- All calls are recorded
- Transcript becomes input for proposal
- Tools: Fireflies, Fathom, or similar

#### Step 2: Proposal Generation
- AI generates from call transcript
- Identifies problems and quantifies them
- Matches solutions to problems
- Includes pricing tiers

#### Step 3: Contract Signing
- Client signs proposal
- Payment processed
- PandaDoc with embedded invoicing

#### Step 4: Welcome Emails
- Automated sequence from multiple team members
- Addresses buyer's remorse
- Creates perception of team mobilization

#### Step 5: Kickoff Call
- 30-45 minute casual conversation
- Recorded for transcript extraction
- Discusses: offers, pricing, service details, previous campaigns

#### Step 6: Lead Generation
- Scrape from databases (Apify)
- Target: 3,000+ leads per client
- Test scrape → verify quality → full scrape

#### Step 7: Lead Enrichment
- Fill missing email addresses
- Use enrichment services
- Goal: maximize email coverage

#### Step 8: Lead Casualization
- Transform formal company names
- Make them sound natural in cold emails
- AI-powered NLP transformation

#### Step 9: Campaign Generation
- Multiple split-tested offers
- Formal and casual versions
- Based on historical high performers
- Follow-up sequences included

#### Step 10: Automated Reply System
- Knowledge base per campaign
- AI-generated contextual replies
- Handles objections, does ROI math

#### Step 11: QA and Launch
- Human reviews campaigns
- Minor adjustments (spacing, scheduling)
- Launch campaigns

### The Result for Clients

Stream of positive replies:
- "Hey, this sounds great. How do I book a meeting?"
- "Hey, sounds awesome. Are you free tomorrow at 2?"
- "Hey, I'd really like to explore more about this. Could you send me some more info?"

> "And so that is our value. We provide revenue."

### Time and Cost Transformation

**Before Agentic Workflows:**
- Time: 5-10 hours per client
- Cost: $2,000-2,500 per client fulfillment

**After Agentic Workflows:**
- Time: ~1.5 minutes (30 seconds per campaign)
- Cost: <$10 per client

> "I can get the exact same thing done that I used to spend over two grand for less than $10."

---

## 6. LEAD GENERATION & ENRICHMENT WORKFLOW

### The Complete Lead Scraping Process

#### Platform: Apify
- Cost: ~$1.50 per 1,000 leads
- Output: Company names, websites, email addresses
- Destination: Google Sheets

#### The Quality Control Protocol

Nick's directive includes built-in quality assurance:

```markdown
## Lead Scraping SOP

1. Generate filters based on kickoff call transcript
   - Industry
   - Location (country, region)
   - Company size
   - Other relevant criteria

2. Run TEST SCRAPE of 25 leads

3. Quality Check:
   - If >85% are in target market → Proceed to full scrape
   - If <85% are in target market → Adjust filters, retry test

4. Full Scrape:
   - Default minimum: 3,000 leads per client
   - Store in Google Sheets
   - Include all available data fields
```

#### Autonomous Filter Adjustment

The system self-corrects:
> "It found out that like we're looking specifically for UK leads. And so, you can see there's a country column here that's 'UK.' It then ran a few tests on the company size and so on and so forth. It adjusted the filters autonomously until it got us what we needed."

### Lead Enrichment

**Problem:** Not all scraped records have email addresses

**Solution:** Use enrichment services to fill gaps

**Example Results:**
- Initial scrape: 178/200 emails
- After enrichment: 193/200 emails
- Improvement: +15 additional emails

### Lead Casualization (Detailed)

#### Why Casualization Matters

**The Problem:**
Cold emails that use formal company names scream "automated spam":

> "Hey Sam, real big fan of HotSchedules.com, Space Incorporated, period."

**The Solution:**
Transform to how people actually refer to their companies:

| Original (Formal) | Casualized |
|-------------------|------------|
| HotSchedules.com Incorporated | HotSchedules |
| The Balserac Group of AB and Co-Realtors | Balserac Group |
| Lex Auto Lease | Lex |
| Castle Property Management Ltd. | Castle |

**The Test:**
> "When Lex refers to their company internally, they don't say, 'Hey, how's Lex Auto Lease's revenue doing?' They're just saying, 'Hey, so what's Lex's revenue these days?'"

#### Implementation
- AI uses NLP to identify the casual version
- Adds "casual_company_name" column to spreadsheet
- Used as variable in email templates

### Complete Lead Data Structure

After full processing, each lead contains:

| Field | Example |
|-------|---------|
| First Name | Sam |
| Last Name | Johnson |
| Email | sam@company.com |
| Company (Formal) | Lex Auto Lease |
| Company (Casual) | Lex |
| Website | lexautolease.com |
| Country | UK |
| Company Size | 50-200 |
| Industry | Automotive |
| Icebreaker | AI-generated personalized line |

---

## 7. PROPOSAL GENERATION FROM CALL TRANSCRIPTS

### The Workflow

**Input:** Sales call transcript (from recording service)

**Command Example:**
> "Hey, I just had a great call with a prospect. Grab the transcript then generate a proposal."

**Output:** Complete PandaDoc proposal ready for sending

**Time:** Less than 15 seconds

### What the AI Does

1. **Finds the transcript** — On computer or from cloud service (Fireflies, Fathom)
2. **Extracts key information:**
   - Company name
   - Contact details
   - Problems discussed
   - Goals mentioned
   - Budget indicators
3. **Generates proposal content:**
   - Problem statements (quantified)
   - Solutions matched to problems
   - ROI calculations
   - Scope breakdown
4. **Populates template** — Fills in yellow-highlighted fields
5. **Creates API request** — Sends to PandaDoc
6. **Sends follow-up email** — Uses MCP tool

### Proposal Structure

#### Section 1: Problems (Multiple)

The AI identifies and quantifies multiple problems:

**Example Problem 1:**
> "Right now your revenue follows a feast or famine pattern entirely dependent on Kelly's availability. One month you sign three clients, the next month zero. This isn't sustainable—growth is chaos. The gap between your current three calls a month and the 7 to 10 a week you need represents roughly £400,000 in lost annual revenue opportunity."

**Example Problem 2:**
> "Right now, you're burning roughly $50K per year on outreach in Apollo. Legacy tools are built for a different era of sales. The platforms are expensive, clunky, don't talk to each other."

**Key Technique:** Multiple problems + dollar quantification = compelling case

> "In order to sell people, what you need to do is you don't just give them one problem. You give them multiple problems and then you tie all of that stuff back to return on investment."

#### Section 2: Solutions

Each problem gets a matched solution:

**Problem → Solution Example:**
- Problem: 15 hours/week manually tracking shipments
- Solution: Unified dashboard that pulls real-time data from 12 carriers automatically

#### Section 3: Scope/How We Work

- Setup of no-code and automation platforms
- 30-minute weekly progress reviews
- Lead generation and delivery via Slack
- Campaign iteration process

#### Section 4: Investment

Nick's pricing model (3-month minimum):
| Month | Investment |
|-------|------------|
| Month 1 | ~£10K |
| Month 2 | ~£7K |
| Month 3+ | ~£5K/month |

**Rationale:**
> "Three-month or more relationships are best for our clients. Over a longer time scale, we're capable of delivering significantly more value. Also, it weeds out tire kickers and people at the bottom rung of the financial ladder that aren't willing to put their money where their mouth is."

### The Expansion Feature

Nick often stores only high-level notes. The AI expands them:

**Input:**
> "Person wants $45,000 in cost savings for whatever platform"

**Output:**
Full narrative about current inefficiencies, quantified losses, and how services address them.

> "What it does is it takes that information and it expands it based off the context of the company. It'll do a little bit of research into the business and understand what it needs in order to put something together that actually looks nice."

### PandaDoc Integration

**Feature:** Embedded invoicing
> "What's really cool about this document is you can actually just charge money upfront. I actually have an invoice buried in said document."

**Workflow:**
1. Client signs proposal
2. Invoice automatically generated
3. Payment processed
4. Triggers onboarding workflow

**Nick's complaint:**
> "As much as I really dislike how PandaDoc is doing their like $2 per API call billing, it's really really cool to be able to have somebody sign a thing and then immediately get an invoice for the thing."

---

## 8. AUTOMATED ONBOARDING SEQUENCE

### The Psychology: Buyer's Remorse

**The Problem:**
When a customer pays for a service, they immediately enter buyer's remorse:
- They gave you money
- You've done nothing yet
- The "seesaw" is tilted entirely in your favor

> "What typically happens when a customer pays you is they're in the situation of buyer's remorse. Meaning, in a service they've just paid you money. You have done absolutely nothing for them."

### The Solution: Immediate Perceived Activity

Create the perception that your entire team is mobilizing around their account.

### The Welcome Email Sequence

**Triggering the Sequence:**

Current (manual):
> "Hey, onboard this new customer."

Future (automated via webhook):
> Webhook from payment processor triggers sequence automatically

#### Email 1: Founder/Main Contact
**Timing:** Immediately after payment
**Sender:** Nick (founder)
**Content:**
> "Hey Kelly, just saw the agreement go through. Had to rush over and formally welcome you. I and the rest of the team are super excited to have you and [Company]. Thanks for filling out your agreement so promptly. Over the course of the next 30 minutes, here's what you're going to receive. Stay tuned for more on this. Thank you very much and appreciate you coming on board."

#### Email 2: Team Member
**Timing:** Few minutes later
**Sender:** Another team member
**Content:**
> "Hey, Nick ran me through your company on our last call. So stoked to have you."

#### Email 3: Scheduling Assistant
**Timing:** Shortly after
**Sender:** Sam (scheduling assistant)
**Content:** Calendar link to book kickoff call

### Why Multiple Senders Matter

> "If you have multiple people in your business, you'll send from multiple addresses just so that you can imply that there are a lot of people really stoked about you beginning to work with us."

**The Perception Created:**
- Whole team is aware of new client
- Multiple people are excited
- Activity is happening immediately
- Client is important

### The Result

> "I personally and anecdotally find that client satisfaction scores shot way the hell up when I started doing this."

### Complete Onboarding Workflow

What happens when Nick says "onboard this new customer":

1. **Welcome email sequence sent** — Multiple emails from different people
2. **Kickoff call scheduled** — Calendar link delivered
3. **Company names casualized** — For campaign use
4. **Lead scraping initiated** — Based on kickoff call context
5. **Leads enriched** — Missing emails filled
6. **Campaigns generated** — Multiple split-tested versions
7. **Knowledge base populated** — For auto-reply system
8. **Leads uploaded** — To Instantly platform

All automated. Only human step: Final QA before launch.

---

## 9. CAMPAIGN GENERATION & COLD EMAIL COPY

### What an "Offer" Is

**Definition:** A compelling promise that reduces perceived risk for the prospect.

**Example Offers:**
> "I'll get you five customers in the next 90 days, or you don't pay a cent. I'll continue working for free until I achieve that."

> "I'll book you 15 qualified meetings in the next 30 days or you don't pay a thing."

> "I'll book you 3 new clients in 30 days."

> "I'll help you generate £100K revenue in 90 days."

**Why Offers Work:**
> "It's an offer in so far that we are offering something that sounds really good. And it is because it sounds really good and we're guaranteeing some form of results that people say yes."

### Campaign Generation Process

#### Input: Kickoff Call Transcript

Questions extracted from transcript:
- "What offers are you comfortable running?"
- "What have you guys run before?"
- "What is your pricing?"
- "Give me some details about your service."

> "We just talk about that with the customer on like a 30 to 45 minute call. It's very chill. It's literally just like, 'Oh wow, that's really cool. Tell me more about this.'"

#### Output: Multiple Split-Tested Campaigns

For each client, the system generates:
- Multiple offer variations
- Formal AND casual versions of each
- Complete follow-up sequences

### Example Generated Campaigns

#### Campaign 1: Formal Version
> "Hey [First Name]. Quick question. [First Name], [Icebreaker]. I know this is out of left field, but I work specifically with partners at accounting and advisory firms in the UK. Basically, I build outreach systems that book qualified meetings with your ideal clients on autopilot. I've been doing this for 6 years now. I've worked with 60+ accounting firms specifically, mostly 3 to 10x growth in their LinkedIn presence and pipeline within the first few months.
>
> Here's my offer: I'll book you 15 qualified meetings in the next 30 days or you don't pay a thing. I'll handle everything. You just show up to the calls. Would this be of value? If so, happy to send over a quick video explaining how it works."

**Expected Performance:** 2-3% reply rate basis

#### Campaign 2: Casual Version
> "NGL (not going to lie), this might seem random, but hear me out. I have 200+ clients now. 60 of them are accounting firms. System's pretty dialed in at this point. Was looking into advisory firms in your area and [Company Name] caught my eye. Felt like you'd be a good fit for something I'm testing. I'll book you 15 meetings in the next 30 days. You pay nothing. Zero risk on your end. I cover all the costs up front."

#### Campaign 3: Aggressive Version
> "This might be the most aggressive cold email I've ever sent, but here goes..."

### The Learning Mechanism

Campaigns are generated based on **historical high performers**:

> "Looking at the highest performing campaigns that I have ever written and then matching those campaigns to the information in the kickoff call transcript."

> "It's not the same copy as the old one, but it's heavily based off of them because it's so recent in the context. The copy quality is really good."

### Directive Instructions for Tone

Nick's directive includes tone requirements:
> "As part of our directives, we say, 'Hey, write a casual version and then write a formal version.'"

### Platform: Instantly

Campaigns are created directly in Instantly:
- Multiple campaign variations
- Scheduled sequences
- Follow-up messages
- Lead upload automation

---

## 10. AUTOMATED REPLY SYSTEM

### The Challenge

Managing replies at scale is "a pretty laborious process":
- Setting up n8n workflows
- Configuring variables
- Getting conversation history
- Building response logic

### The Agentic Solution

#### Architecture

```
[Incoming Reply] → [Match to Campaign UID] → [Pull from Knowledge Base] → [AI Generate Reply] → [Send]
```

#### Components

1. **Campaign UID Matching** — Identify which campaign the reply belongs to
2. **Knowledge Base Lookup** — Pull relevant context for that campaign
3. **AI Reply Generation** — Claude with extended thinking
4. **Contextual Response** — Address specific concerns raised

### Reply Generation Process

What the AI does:
1. Looks up knowledge base for campaign UID
2. Uses Claude with extended thinking
3. Addresses specific skepticism/objections
4. Does ROI math relevant to the prospect
5. Uses social proof (client numbers, experience)
6. Personalizes with company name
7. Includes soft CTA to book call

### Example: Handling Skepticism

**Incoming Reply:**
Prospect was incredulous about a guarantee, essentially saying "but like, actually, the guarantee is not real..."

**Generated Response:**
> "Yeah. Hey Kelly. Yes, seriously. If we don't deliver three new clients in 30 days, you don't pay. Simple as that. At £10,000 average contract sizes, £30K in new revenue against a £9,850 first month investment.
>
> We can take that risk because we've done this for 200 clients over 6 years, including 60 accounting firms in similar spaces.
>
> Is that worth a quick call to see if it makes sense for Executive Social?
>
> Nick"

**What Made This Response Effective:**
- Directly addressed skepticism ("Yes, seriously")
- Concrete numbers (£10K contracts, £30K revenue, £9,850 investment)
- Social proof (200 clients, 6 years, 60 accounting firms)
- Personalization (company name: Executive Social)
- Soft CTA (worth a quick call?)

### Comparison to Procedural Approach

**n8n/Make Approach:**
- Rigid decision trees
- Pre-defined response templates
- Limited contextual awareness
- Breaks when edge cases appear

**Agentic Approach:**
- Dynamic decision-making
- Context-aware generation
- Handles novel objections
- "Flexible in a good way, not flexible in a bad way"

> "You guys can do that with like n8n procedurally if you wanted to, but it's way cooler when you do it completely automatically and then it also allows it to use decision-making live. So I find that the replies are just a lot more flexible."

---

## 11. KNOWLEDGE BASES

### What They Are

A structured repository of information that the auto-reply system draws from.

### Implementation

**Format:** Google Sheets (simple, accessible)

**Contents per Campaign:**
- Company information
- Offer details
- Pricing information
- Common objections and responses
- Reply examples
- Social proof elements

### How They're Used

```
1. Reply comes in via webhook
2. System identifies campaign UID
3. Pulls all relevant info from knowledge base
4. Feeds context to AI for reply generation
5. AI crafts personalized response
```

### Populating Knowledge Bases

**Automated:**
The onboarding workflow automatically adds:
- Company details from kickoff call
- Offer specifics
- Pricing tiers

**Manual (Optional):**
> "This could be something that we completely automate. This could be something that we manually do. Maybe we manually write two or three reply examples and it just automates the rest."

### The Flexibility

> "The possibilities here are kind of unlimited."

You can:
- Fully automate knowledge base population
- Manually seed with key examples
- Hybrid approach (auto-populate + manual refinement)

---

## 12. META DIRECTIVES

### What They Are

A top-level directive that orchestrates multiple sub-directives into a complete, end-to-end workflow.

### The Hierarchy

```
META DIRECTIVE: "Onboard New Customer"
│
├── DIRECTIVE 1: Send Welcome Emails
│   ├── Script A: send_founder_email.py
│   ├── Script B: send_team_email.py
│   └── Script C: send_calendar_link.py
│
├── DIRECTIVE 2: Process Kickoff Call
│   ├── Script A: extract_transcript.py
│   ├── Script B: identify_offers.py
│   └── Script C: extract_requirements.py
│
├── DIRECTIVE 3: Generate Leads
│   ├── Script A: scrape_leads.py
│   ├── Script B: enrich_emails.py
│   └── Script C: casualize_names.py
│
├── DIRECTIVE 4: Create Campaigns
│   ├── Script A: generate_copy.py
│   ├── Script B: create_instantly_campaign.py
│   └── Script C: upload_leads.py
│
└── DIRECTIVE 5: Setup Auto-Reply
    ├── Script A: populate_knowledge_base.py
    └── Script B: configure_webhook.py
```

### How to Create One

After building individual workflows for each component:

> "Hey, I have now had you build a process with all of these workflows. I just want you to combine them together into an onboarding workflow or a project fulfillment workflow or something like that."

### How It Works

1. Meta directive received (e.g., "onboard new customer")
2. Agent identifies sub-directives needed
3. Executes Directive 1 → Scripts A, B, C
4. Executes Directive 2 → Scripts A, B, C
5. Continues through all directives
6. Orchestrates completion of entire flow

> "This top-level directive—like the onboarding one—can just go top to bottom and then follow all of the directives that you've created."

### The Power of Meta Directives

**One command → Entire fulfillment pipeline:**
- Welcome emails sent
- Kickoff scheduled
- Details extracted
- Leads scraped
- Leads enriched
- Campaigns created
- Auto-reply configured
- Leads uploaded

**Human involvement:** Only QA before launch

---

## 13. THE 5-STEP GUIDE TO AUTOMATE ANY BUSINESS

Nick's framework for anyone to automate their digital services business:

### Step 1: Compile Your SOPs

**What are SOPs?**
Standard Operating Procedures — documents describing steps to produce a deliverable.

**How to Write Them:**
- Natural language
- "Monkey could understand" level of clarity
- Step-by-step format

**Example SOP: Lead Scraping**
```
1. Generate filters for lead list based on client requirements
   - Industry
   - Location
   - Company size

2. Test on sample of 25 leads

3. Quality check:
   - If >80% are good → proceed to full scrape
   - If <80% are good → retry with different filters

4. Run full scrape
   - Default minimum: 3,000 leads per client

5. Output to Google Sheets
```

**Scope:**
> "Realistically, you probably have like 20 or 30 SOPs across your company. You got to compile all of those SOPs just like this."

### Step 2: Send SOPs to Your AI Agent

**Setup:**
- Platform: Visual Studio Code
- AI: Claude Code (or similar)
- Config file: `CLAUDE.md`, `agents.md`, or `gemini.md`

**Input Methods:**
- Text (paste or type)
- Screenshot
- Voice recording (transcribed)
- Any format the AI can interpret

**Command Example:**
> "Hey, here's the screenshot. I'd like you to generate a new workflow for this. Store it in lead_scraping.md"

**Output:**
- Directive file created
- In-depth with all edge cases covered
- Same format as other directives

**Key Insight:**
> "Your SOPs don't even have to be that defined. These models will then help generate the SOPs for you."

### Step 3: Test Once

**What Happens:**
AI will request what it needs:
- API keys
- Credentials
- Environment variables (.env file)

**Don't Panic:**
> "What the heck does any of that mean? Well, guess what? You don't actually have to know. The AI will just guide you through it."

The AI provides:
- Step-by-step instructions
- Where to find API keys
- How to configure credentials

**First Run Expectation:**
~75% reliable — and that's perfectly fine.

### Step 4: Iterate Until Reliable

**The Improvement Loop:**
```
Run → Fail → Analyze → Fix → Run → Improve → Run → Perfect
```

**Reliability Progression:**
| Iteration | Reliability |
|-----------|-------------|
| 1 | 75% |
| 2 | 97% |
| 3 | 99% |
| 4 | 99.99% |

**Hands-Off Process:**
> "Your hands are off. Like, I'm not touching anything. I'm just having this continuously run, test, iterate, and then retry over and over and over again till it figures it out."

**Example from Demo:**
- Initial scrape had location format issue
- System detected failure
- Analyzed what went wrong
- Fixed the format
- Retried successfully
- Even built quality-check function on its own

### Step 5: Create Meta Directive

**When:** After all individual SOPs are converted to working directives

**Command:**
> "Hey, I have now had you build a process with all of these workflows. I just want you to combine them together into an onboarding workflow."

**Result:**
- Single command triggers entire pipeline
- Sub-directives execute in sequence
- Full automation achieved

### The End State

**Folder Structure:**
```
workspace/
├── directives/
│   ├── meta_onboarding.md      ← Master directive
│   ├── welcome_emails.md
│   ├── process_kickoff.md
│   ├── generate_leads.md
│   ├── create_campaigns.md
│   └── setup_autoreply.md
└── execution/
    ├── send_email.py
    ├── scrape_leads.py
    ├── enrich_leads.py
    ├── casualize_names.py
    ├── generate_copy.py
    ├── upload_to_instantly.py
    └── configure_webhook.py
```

**Usage:**
One command → Entire client onboarding automated

---

## 14. IDE SETUP & TOOLS

### Nick's Primary Setup

**IDE:** Visual Studio Code
**AI Integration:** Claude Code
**Config File:** `CLAUDE.md` in project root

> "If I open up my own instance for you, it looks something like this. I have a bunch of files on the left-hand side. Then in the middle here, I have like my little chat window where I can communicate with Claude Code."

### Alternative: Antigravity

**What it is:** Google's agentic IDE platform
**Status:** Newer, launched recently

**Layout:**
- Left panel: File explorer (directives, execution folders)
- Middle panel: Agent Manager, settings
- Right panel: Chat with agent

**Antigravity-Specific Features:**

1. **Agent Manager** (Command+E)
   - One-off chat box
   - Q&A without code view
   - Build specific agents for different purposes
   - Insert knowledge items

2. **Inbox**
   - Notifications from agent
   - Unique to Antigravity

3. **Playground**
   - New conversation instance
   - Not tied to specific workspace

4. **Remote Workspaces**
   - Run on other hardware
   - Future scalability option

5. **Browser Use** (Experimental)
   - Access web pages
   - Extract DOM elements
   - Browser automations
   - "Only works maybe 70-80% of the time"

### File Types in IDE

**Markdown (.md):**
- Directive files
- Human-readable instructions
- Icon: M with down arrow

**Python (.py):**
- Execution scripts
- Color-coded syntax
- Icon: Python logo

**Visual Indicators:**
- Green = Comments
- Blue = Variable definitions
- Purple = Logic/conditionals

### For No-Code Background

Nick's advice for people from Make/n8n background:
> "Look at all function definitions. So `define get_api_key` and I want you to just treat that like a single node on a graph."

**Translation:**
- `def get_api_key()` = One node
- `def fetch_campaign()` = Another node
- `def extract_sequences()` = Another node

Just arranged vertically instead of left-to-right visual.

### Tools & Platforms Summary

| Tool | Purpose | Cost/Notes |
|------|---------|------------|
| **VS Code + Claude Code** | Nick's primary IDE | Free/Subscription |
| **Antigravity** | Google's agentic IDE | Newer option |
| **Apify** | Lead scraping | ~$1.50/1,000 leads |
| **PandaDoc** | Proposals + invoicing | $2/API call |
| **Instantly** | Cold email campaigns | Subscription |
| **Fireflies/Fathom** | Call recording | Subscription |
| **Google Sheets** | Data storage, knowledge bases | Free |
| **n8n/Make/Zapier** | Procedural alternatives | Subscription |

---

## 15. SPEED & COST ANALYSIS

### Speed: Tools vs. Raw LLM

**Example Task:** Reverse sort a list of 10 items

**Using LLM Directly:**
- Must calculate massive matrix operations
- Token-by-token processing
- Slow and expensive

**Using Tool (Python Script):**
- Virtually instantaneous
- Single function call
- No token usage

**Order of Magnitude:**
> "The order of magnitude in the amount of time it would take to do the top thing (using an LLM) to bottom thing (using a tool) is something like 10,000 times if not 100,000 times."

### Cost Comparison: Human vs. Agentic

**Traditional Fulfillment:**
| Item | Cost |
|------|------|
| Human labor | $2,000-2,500 per client |
| Time | 5-10 hours |
| Turnaround | Days to a week |

**Agentic Fulfillment:**
| Item | Cost |
|------|------|
| Compute + API calls | <$10 per client |
| Time | ~1.5 minutes |
| Turnaround | Immediate |

**Savings:**
- Cost: 99.5%+ reduction
- Time: 99%+ reduction

### Token Economics

**With Raw LLM:**
- Every operation consumes tokens
- Simple tasks = expensive
- Scales poorly

**With Tools:**
- Code execution = no tokens
- CPU/server costs only
- "Effectively free" for computational tasks

> "You also have no token usage making this—while not actually free because you are going to be using your CPU and maybe some sort of server—it will be effectively free compared to just how much time, energy, and resources are being run in order to do silly requests like this using LLMs."

### What Changed with Agentic Workflows

**Before (Procedural):**

| Task | Requirement |
|------|-------------|
| Lead generation | Know exact industry, filters, locations ahead of time |
| Casualization | Set up all scripts and API calls manually |
| Campaigns | Feed to AI without contextual learning |
| Replies | Build rigid n8n workflows, limited flexibility |

**After (Agentic):**

| Task | How It Works |
|------|--------------|
| Lead generation | AI determines filters from context |
| Casualization | Automatic NLP transformation |
| Campaigns | Based on historical high performers + context |
| Replies | Dynamic, live decision-making |

---

## 16. KEY PRINCIPLES & PHILOSOPHY

### On Reliability

> "You cannot run a million-dollar-a-month operation on a system that only works most of the time."

> "In business, even a 1% rate of inaccuracy can lead to a revenue reduction of 50% or more."

> "A Python script does not hallucinate. It either works or it errors out. And if it errors out, we can catch it."

### On Coding

> "I don't actually know how to read most of this code. I don't worry about most of this code. That is the AI's job."

> "The AI is much better at coding than I probably would ever be, even given a decade of learning."

> "If what you're looking at here is very intimidating, that's okay."

### On SOPs and Directives

> "The directive layer is literally just a bunch of natural language prompts. They're the exact same type of standard operating procedure that you would find in any company."

> "You could literally take a pre-existing list of all of the standard operating procedures in a business and just drag and drop them into your IDE."

> "Your SOPs don't even have to be that defined. These models will then help generate the SOPs for you."

### On Self-Improvement

> "You just build it once and it will continue to improve itself reliably over time."

> "If it tests it once and then it doesn't figure it out, then it's just going to continue running until it does figure it out."

> "This workflow almost healed, you know, it's like Wolverine."

### On Business Value

> "I can get the exact same thing done that I used to spend over two grand for less than $10."

> "My goal here was not just to teach you guys technology for technology's sake, but to show you how to use these things in an actionable way that helps you make real money."

> "It's a lot less on the hypothetical and a lot more on the immediately applicable."

### On Flexibility vs. Determinism

> "Ultimately speaking, in a business, you don't want flexibility. In a business, you want determinism."

> "We take the inherently flexible probabilistic nature of LLMs and use it to create a bunch of deterministic pipelines."

### On the Future

> "I'm not exaggerating when I say these will quickly run the entire economy."

> "Agentic workflows are definitively here, and they are without a doubt the future of workflow building."

---

## APPENDIX: Quick Reference

### DOE Framework Summary

| Layer | Contains | Purpose |
|-------|----------|---------|
| Directive | .md files with SOPs | What to do |
| Orchestration | The LLM itself | Who decides |
| Execution | .py scripts | How it's done |

### Self-Annealing Progression

| Run | Reliability |
|-----|-------------|
| 1 | 75% |
| 2 | 97% |
| 3 | 99% |
| 4+ | 99.99% |

### Leftclick Process (11 Steps)

1. Sales call → 2. Proposal → 3. Signing → 4. Welcome emails → 5. Kickoff call → 6. Lead gen → 7. Enrichment → 8. Casualization → 9. Campaigns → 10. Auto-reply → 11. QA & Launch

### 5-Step Automation Guide

1. Compile SOPs
2. Send to AI agent
3. Test once
4. Iterate until reliable
5. Create meta directive

### Cost Comparison

| Method | Cost | Time |
|--------|------|------|
| Human | $2,000-2,500 | 5-10 hours |
| Agentic | <$10 | 1.5 minutes |

---

*Document compiled from Nick's two agentic workflow tutorials. For implementation, start with Step 1: Compile your SOPs.*
