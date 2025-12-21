# I Built a Business That AI Agents Run (Lovable Cloud)

**Source:** [Luuk Alleman - YouTube](https://www.youtube.com/watch?v=3MGaAb0kcyA)
**Published:** Oct 7, 2025

---

## Overview

A complete marketing agency built in Lovable Cloud that handles lead intake, brand research, content creation, and client delivery—all automated by AI agents. No meetings, no project managers, just agents working together like a real business.

---

## Table of Contents

1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Lead Intake & Client Onboarding](#lead-intake--client-onboarding)
4. [Content Creation Process](#content-creation-process)
5. [Quality Control & Delivery](#quality-control--delivery)
6. [Technical Setup](#technical-setup)
7. [Testing & Debugging](#testing--debugging)
8. [Final Results](#final-results)

---

## Introduction

Most AI agents are demos—they look cool in videos but can't do anything real. This project tests the limit by building an actual marketing agency with:

- Lead intake
- Brand research
- Content creation
- Client delivery

All run by an army of agents. If it works, it changes how we look at AI automation.

---

## System Architecture

The system follows this flow:

```
Landing Page → Request Form → Lead Agent → Account Creation → Payment → Brand Research → Content Scheduling → Content Creation → Quality Control → Delivery
```

### Key Components

1. **Landing Page** - Showcases the service (30 branded social media posts/month)
2. **Request Form** - Captures company info, social handles, content needs, brand assets, example posts
3. **Lead Agent** - First agent to interact; checks input, budget, and scores quality
4. **Account Creation** - Sets up client account, sends welcome email with credentials
5. **Payment** - Stripe checkout integration
6. **Brand Research Agent** - Scrapes posts, analyzes tone/style, extracts brand voice, stores in Mem0
7. **Content Scheduler** - Creates 30 post records with creation dates
8. **Cron Jobs** - Runs hourly to check if posts are due for creation
9. **Content Strategist Agent** - Retrieves brand voice, determines theme, creates brief
10. **Copywriter Agent** - Writes captions, adds hashtags, uses proven frameworks
11. **Visual Prompt Agent** - Creates image prompts including brand colors
12. **Image Generator Agent** - Calls the image generation API
13. **Quality Control Agent** - Reviews caption + image, checks brand alignment
14. **Delivery Agent** - Sends email notification, updates dashboard

---

## Lead Intake & Client Onboarding

### The Request Form (3 Steps)

**Step 1: Basics**
- Company name
- Contact name
- Email address
- Service tier selection

**Step 2: Brand Info**
- Instagram handle
- Company description
- Target audience description

**Step 3: Brand Assets**
- Logo upload
- Brand colors
- Example post URLs (LinkedIn/Instagram)
- Content themes and topics

### Lead Qualification

The Lead Agent evaluates:
- Is this person serious?
- Is this a brand we can help?
- Budget fit check

**Two outcomes:**
- **Approved** → Create account, send welcome email (within a minute of form submission)
- **Rejected** → Send rejection email

### Welcome Email Contents
- Login credentials (email + password)
- Dashboard URL
- Payment link
- What happens next

---

## Content Creation Process

### Brand Research Phase

After payment, the Brand Research Agent:

1. Scrapes last 10 Instagram and LinkedIn posts
2. Analyzes brand voice using Gemini
3. Stores results in:
   - Brand voice database table
   - Mem0 (memory for AI agents)

### Brand Voice Analysis Includes:
- Style description (e.g., "direct and educational")
- Content structure (problem → solution → call to action)
- Caption length preferences
- Vocabulary guidelines (words to avoid)
- Content themes

### Content Scheduling

- Creates 30 post records
- Sets "create content" date for each
- Status set to "scheduled"
- All done directly in Lovable (no Python required)

### Content Generation Flow

1. **Cron job** (runs hourly) checks if creation date is due
2. **Content Strategist Agent** retrieves brand voice from Mem0, determines theme, creates brief
3. **Copywriter Agent** writes caption with hashtags using proven frameworks
4. **Visual Prompt Agent** creates image prompt with brand colors
5. **Image Generator Agent** creates the image

---

## Quality Control & Delivery

### Review Process

The Quality Control Agent:
- Reviews caption + image together
- Checks brand alignment
- If revision needed → sends back to Copywriter Agent with feedback (loop repeats)
- If approved → proceeds to delivery

### Delivery

The Delivery Agent:
- Sends email notification ("Your post is ready")
- Updates dashboard
- Includes URL to the actual post
- Changes post status to "Ready for Client"

### Client Actions
- View content
- Copy caption
- Download image
- Request revision
- Mark as used

---

## Technical Setup

### Required API Keys

1. **Resend** - For email functionality
2. **Apify** - For Instagram/LinkedIn scraping
   - Go to apify.com → Settings → API and Integrations → Create new token
3. **Mem0** - For AI memory/brand voice storage
   - Create free account at mem0.ai → Dashboard → API Keys
4. **Stripe** - For payments (create test products for development)

### Service Tiers

- **Instagram Tier** - Instagram posts only
- **Multi-platform Tier** - Instagram + LinkedIn

### Database Schema

Lovable can auto-generate this, or you can define it manually.

---

## Testing & Debugging

### How to Debug Edge Functions

1. Go to Supabase dashboard
2. Navigate to Edge Functions
3. Check success rate
4. If something is failing, click on the function
5. Copy the logs
6. Paste error into Lovable for fixes

### Common Issues Fixed

- Resend API key configuration
- Input validation fixes
- Correct email sender address
- Stripe product setup for testing
- Instagram vs LinkedIn URL detection

### Testing Content Generation

Add a "Test Content" button to manually trigger post creation instead of waiting for the cron job. This allows rapid iteration on output quality.

### Iterative Improvement

The author generated 18 posts before reaching acceptable quality. Common issues encountered:

- Wrong logo appearing
- Spelling mistakes in images
- Post numbers appearing in content
- Robotic captions
- Background issues with logo overlay

AI image generation with text is still tricky but improving rapidly.

---

## Final Results

### What Got Built in 2 Hours

- Landing page with unique design
- Multi-step onboarding form
- Lead qualification system
- Automated welcome/rejection emails
- Stripe payment integration
- Client dashboard with:
  - 30-day content calendar
  - Status indicators (Scheduled/Generating/Ready)
  - Post preview and download
  - Revision request system
- Settings page for clients
- Automated content generation pipeline
- Email notifications for ready posts

### Dashboard Features

- Calendar view of all 30 posts
- Status icons: Scheduled, Generating, Ready/Delivered
- Recent posts section
- Click any day to view/manage that post
- Request revision with feedback

### Output Quality

Final posts include:
- On-brand imagery with logo
- Relevant captions with hashtags
- Call-to-action elements
- Proper formatting for the platform

---

## Resources

- **Prompt Library** - Contains all prompts used (linked in video description)
- **AI Prompt Writer** - Tool that rewrites prompts using correct API documentation for Apify actors, Mem0, etc.

---

## Key Takeaways

1. **80/20 Rule** - Lovable gets you from 0 to 80% quickly; the last 20% (monitoring and fine-tuning output) is most important
2. **Iterative Development** - Expect to debug and refine; every app builds differently even with the same prompt
3. **Scale Potential** - Once working, the system runs daily with no delays
4. **Fine-tuning Matters** - Partner with marketing specialists to improve prompts and strategies
5. **Current Limitations** - AI image text generation is still evolving but improving rapidly

---

## Tools & Technologies Used

- **Lovable** - No-code app builder
- **Supabase** - Backend/database (via Lovable)
- **Stripe** - Payments
- **Resend** - Email delivery
- **Apify** - Web scraping (Instagram/LinkedIn)
- **Mem0** - AI memory storage
- **Gemini** - Brand voice analysis
- **Image Generation API** - Post visuals
