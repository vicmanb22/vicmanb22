# How to Automate ANY Service Business with Agentic Workflows (A-Z)

**Date:** December 2, 2025
**Source:** YouTube - https://www.youtube.com/watch?v=Uj-1we7Rew4
**Speaker:** Nick (Leftclick / Maker School)

---

## Summary

This video walks through building a digital service business operated by agentic workflows. It covers lead acquisition, proposal generation, and automated onboarding in a single cohesive system that runs on autopilot.

---

## Introduction
**[0:00]**

Hey, today I'm going to show you how you can automate the fulfillment of more or less any digital services company using agentic workflows. I'm going to be doing this on my own business as a demo. We're Leftclick. We do primarily B2B outbound marketing and cold email.

But I want you guys to know you can do this for any business or any industry so long as it does most of its work on the internet or with some sort of digital data, which I think most businesses are nowadays.

Anyway, if you guys don't know what agentic workflows are, I'm going to walk you through things at a very high level and then I'm also going to run you through how a typical cold email agency works before running you through how to automate the hell out of this sort of thing using agentic workflows so you guys can sell these things to other people or use them to automate your own business. Whatever situation you're in, this is the video for you. Let's do it.

---

## Overview
**[0:42]**

So, two major things I need to explain to you.

### What Are Agentic Workflows?

First, what are agentic workflows? Well, if you guys have ever built any sort of workflow before, you've probably heard of Make.com, n8n, Microsoft Power Automate, or one of these many drag-and-drop platforms.

Now, the way these work is these platforms handle both the **function** and then they also handle the **logic**. And so, in this case, you could see there are functions like "on create user form submission," you know, "is manager," "add to channel," or "update profile"—and then also logic. So the direction that the data will flow and then sort of the logic of true/false, how to route it, and so on and so forth. Okay? And that's just a given across any one of these drag-and-drop platforms.

Well, the way that agentic workflows work is a little bit different. With agentic workflows, what you do is you take all of the functions, you decouple them from all of the logic and the routing, and then you just give all the functions to AI, which we assume is just much better at using and building tools than us. And then we just say, "Hey, here's what I want to do. Can you do it using these functions?" And as long as you're smart about how you set it up, it can do a brilliant job.

### The DOE Framework

Now, the framework that I recommend using for this sort of stuff—because you do typically have to use a framework. As I'm sure you guys are aware, AI can make mistakes, and in business applications, it's important to constrain those mistakes as much as possible. But the framework that I recommend is one called **DOE**, which hopefully is easy to understand:

- **D** stands for **Directive** — That's *what to do*. We just store a bunch of instructions in very high-level files like this.
- **O** stands for **Orchestration** — That's where we basically give the agent this info and say, "Hey, you can orchestrate fulfillment of this however the heck you want."
- **E** stands for **Execution** — Typically the execution is in the form of, I don't know, some Python scripts or something like that.

Now, I should make it clear—I don't actually know how to read most of this code. I don't worry about most of this code. That is the AI's job. The AI is much better at coding than I probably would ever be, even given a decade of learning. And so I just let these large language models which are optimized for coding do the coding for me if necessary and then call the tools that they just built.

If what you're looking at here is very intimidating, that's okay. IDEs or these windows that you guys are seeing—this integrated development environment—are not very beginner-friendly. But I don't want to focus on all the technicals here. I want to show you guys how even if you have zero programming knowledge or any understanding of how any of this stuff works, you could still get up and running and automate most of the work of a digital services agency.

---

## How Service Businesses Work (Leftclick)
**[3:04]**

The second thing you need to understand is what my specific business model does. So in our case, we are Leftclick, which is a B2B outbound marketing/cold email company. So obviously we do a lot of stuff. We don't just do this, but for the most part this is the most profitable thing and so this is most of what I do. So that's how I'm branding this business.

To make a long story short, okay, we will get customers that simply want to increase their top of funnel—the number of leads that enter their business in a given time. And we help them do so by coming up with really hacky cold email campaigns, okay? And then reaching out to people that have never heard of us or our clients in order to book a meeting with them for services rendered.

And so we work for a variety of different sorts of businesses. We've worked from small to mid-size all the way up to multi-billion dollar portfolio companies. And we just do more or less the same thing every time.

But as I'm sure you can imagine, as with delivery of any good service, it does take a fair amount of time to fulfill. And so naturally, I've been slowly chunking away at automating more and more of it over time. It wasn't until I saw agentic workflows and really started to understand them that I realized that you could now automate basically all of any digital services agency if you approach it the right way.

### The Leftclick Process: Step by Step

So, how does Leftclick actually work? Well, I will just give all of the sauce to you here. This is everything that we do inside of our company in order to go from start to finish:

#### 1. Sales Call with Prospect

We'll begin with a sales call with our prospect. And so, these are always recorded. The reason why they're recorded is because then we have a whole transcript that we can pump into some sort of proposal.

#### 2. Proposal Generation

Okay, a proposal for services looks something like this. So, this is us sending a proposal to this business here. We scroll down. You can see that we give them some problem areas:

> "Right now, your team is spending 15 hours per week manually tracking shipments across 12 different carrier portals. That's about $30,000 annually in labor costs just to paste tracking numbers."

Right? So, that's one of their problems. There's another problem here about their invoice reconciliation process, another problem here about their customer reply times, and so on and so forth.

What we do after that is we try to very adeptly give them a solution as well. So okay, like you know, your initial problem was your 15 hours per week manually tracking shipments. Your solution is a unified dashboard that pulls real-time data from 12 carriers automatically.

This is an example proposal. This isn't anything that I've actually sent. I just wanted to give you guys some intuition as to what a real proposal looks like.

We obviously try and make ourselves look as cool as humanly possible—hence the Hormozi and Sam Ovens shot. We give some high-level scope steps. So run them through how things work and then finally we talk about the amount of money that they're investing.

So pretty common, right? Most businesses will do something like this.

#### 3. Contract Signing and Payment

After we send the proposal, they then have to sign the proposal and pay.

#### 4. Welcome Emails

After that, okay, we will normally send them some sort of welcome email. And so, you know, if you have multiple people in your business, you'll send from multiple addresses just so that you can imply that, you know, there are a lot of people really stoked about you beginning to work with us.

So here's a quick example:

> **Subject: Welcome to Leftclick, Kelly**
>
> Hey Kelly, just saw the agreement go through. Had to rush over and formally welcome you. I and the rest of the team are super excited to have you and [Company]. Thanks for filling out your agreement so promptly. Over the course of the next 30 minutes, here's what you're going to receive. Stay tuned for more on this. Thank you very much and appreciate you coming on board.

Again, pretty standard stuff. You're obviously going to want to welcome people to an agency if they just paid your agency a bunch of money, right?

#### 5. Kickoff Call

So, once they're in your business, they're onboarded. You have to have some sort of kickoff call. Now, on the kickoff call, you chat details about the project.

So, in our case, we're cold email, right? In your case, maybe you're doing ads or something. So, here's where you chat about the creatives and the copy and whatnot.

But in our case, we're cold email. And so, in cold email, the most important thing to do is to figure out what offers are permissible—which offers you can run.

An **offer**, to make a long story short, is just something like:

> "I'll get you five customers in the next 90 days, or you don't pay a cent. I'll continue working for free until I achieve that."

That's pretty great. It's an offer in so far that we are offering something that sounds really good. And it is because it sounds really good and we're guaranteeing some form of results that people say yes.

So that's what we do on the offer. Once we're done with that, because it's recorded, we can extract the details via that transcript as well.

#### 6. Lead Generation

And now starts, if you think about it, sort of like our fulfillment process. Okay. So the fulfillment process starts by doing some lead generation, aka by scraping lead databases.

So there are a variety of different lead databases you can use. In our case, we use one called **Apify** pretty often. This one here provides us with about $1.50 per 1,000 leads. We get a bunch of email addresses over here. These are real emails from real people, which I'm not going to obviously show you, but hopefully you get the idea. Then over here we have company names, company websites, and stuff like that.

The reason why that's valuable is now we have sort of targets. Okay, once we have these targets, so to speak, we will enrich their details. Not all of those records had emails, so we want to get as many of those emails as humanly possible.

#### 7. Lead Enrichment and Casualization

And then also, we want to add some form of personalized flair to every row because we're going to use this data in our cold email campaigns and we don't want it to seem really boring.

So, when I say "casualize leads," for instance, this business over here is called "HotSchedules.com Incorporated." Well, if you're sending a cold email campaign, a lot of the time you use things like the company name in your copy. You'll say, "Hey, I'm a big fan of [Company Name]."

So, let's say I'm this fellow over here and I'm getting a cold email from me and it's like:

> "Hey Sam, real big fan of HotSchedules.com, Space Incorporated, period."

What is he going to be thinking on the other end of the line? He's probably going to be thinking that this is BS cold outreach, right?

So, what we do is we casualize this. We rewrite this using natural language processing and using AI really in a way that he probably refers to his own company—just to minimize the possibility of, you know, somebody clicking off our email because they think it's spam.

#### 8. Campaign Generation

Once we're done with that, we actually generate the campaigns. When I say "generate" here, I mean like we write the copy based off of previous high performers. And then we'll actually create some split-tested offers.

So, this is an example of one that I actually ran on YouTube. I believe like a month and a half or two months ago where I actually offered people:

> "Hey [First Name], know this is out of left field. If I could help you connect to more people looking for PPC in exchange for commission on closed revenue, would you be open? I work mostly on performance and have a big network. Media buy would be variable, probably $5K/month or up. Let me know if you're open to a chat in the next 4 days. I can ring you."

Okay, so this is like a very casual sort of campaign. We wrote this for people that were looking for obviously PPC, which means ad buy services. You don't have to understand what all that stuff means if you're new to this, but we're just sending emails to people and offering them some sort of lead gen services.

Okay, so we generate a bunch of these and then we actually have to manage the replies.

#### 9. Automated Reply Management

What we have to do now is we set up automated reply systems to do most of the replies for us. This is working 50/50. It's something I'm experimenting with, but now we're doing this and typically this is a pretty laborious process.

We have to set up like an n8n workflow that looks something like this. You know, we have to set the variables, get the conversation history. We got to do a fair amount of work for this automated pipeline to work. And that's fun and all, but you know, it's still a fair amount of time.

#### 10. Lead Upload and QA

Then we upload new leads to the campaigns, do some sort of QA and final double check before sending, before finally auto-replying to handle all incoming responses intelligently.

#### 11. The Result: Positive Replies

And then what the client gets as a result of all this hard work that we've labored over for—I mean, at least 5 to 10 hours realistically if we want to do a really good job—is they get a big stream of positive replies in their inbox. People saying:

- "Hey, this sounds great. How do I book a meeting?"
- "Hey, sounds awesome. Are you free tomorrow at 2?"
- "Hey, I'd really like to explore more about this. Could you send me some more info?"

And stuff like that. And so that is our value. We provide revenue.

### The Cost Savings with Agentic Workflows

Okay. So I know that was a pretty prolonged explanation, but it is important that you understand everything that's going on in order to understand the value of a system like this.

Obviously, every time you bring somebody on to a service, you need to fulfill said service. And typically, you do so either yourself if you're a freelancer, a small to mid-size business, or you know, you pass it off to some fulfillment or back-end person. You know, if you're growing your agency and you have more than one person in it, and then they do it.

The thing is it obviously takes money in order to buy their time to do the thing. And so if you think about it, there's sort of two things that are going on here:

1. Every time you have to have somebody else do it for you, you spend **a lot of time** because they don't do the things immediately, right? It takes them a fair amount of time, might take a week or something like that.
2. And then second, you spend **a lot of money** because, you know, the cost of service accumulates. Maybe you pay them hourly, maybe you pay them a fixed amount per contract. Whatever the heck you do, there's some sort of cost to it, right?

This is why agentic workflows are so awesome because you can basically completely eliminate 99% of that.

**And so I can get the same thing that I used to get done for somewhere around $2,000 to $2,500 for less than $10.**

Less than $10. I can get the exact same thing done that I used to spend over two grand for.

Okay, incredible stuff. Without further ado, let me show you how to actually run this.

---

## Proposal Generation from Call Transcript
**[11:16]**

So I'm in my agentic workflow IDE over here and I'm just saying:

> "Hey, I just had a great call with a prospect. Grab the transcript then generate a proposal."

And so what I've done is somewhere in our directives and execution folders, I have stored some high-level instructions—very high-level instruction just saying, "Hey, if I ask you to generate a proposal, I want you to do some very simple things here. You know, I want you to generate a proposal using the company name and then the stuff we talked about in the transcript," and so on and so forth.

So, with just one message, what this has done is it said, "I'll look for the Executive Social sales call transcript and generate a proposal from it." So, it found a transcript on my computer, you know, and you don't have to have this on your computer. Obviously, if you're using Fireflies or Fathom or one of these recorders, it's on the internet. That's okay.

But, it found this and went and generated me a proposal for it in **less than 15 seconds**.

Hopefully, you guys are seeing how if I just had a call with somebody, okay, and I just said, "Hey, you know, I just had a call. Can you generate a proposal based off of this?" This can be pretty sexy.

### AI-Generated Proposal Content

All right, next it is automatically filling out a bunch of fields for me using artificial intelligence:

> "Right now your revenue follows a feast or famine pattern entirely dependent on Kelly's availability."

This is a call that I had where essentially Kelly is just on 24/7 doing everything. So she's very bottlenecked. This is her business and so on and so forth.

> "One month you sign three clients, the next month zero. This isn't sustainable—growth is chaos. The gap between your current three calls a month and the 7 to 10 a week you need represents roughly £400,000 in lost annual revenue opportunity."

That's pretty crazy. That's problem number one.

Now, in order to sell people, what you need to do is you don't just give them one problem, okay? You give them multiple problems and then you tie all of that stuff back to return on investment.

So, in Kelly's case, you know, I'm saying, "Hey, this is £400,000 that you're losing per year. This is £300,000 in missed recurring revenue." Right? I mean, how much money is that that she is pissing down the drain right now? That's where our services are going to come in handy.

Then, what we do is we just pitch Kelly on how to assist:

> "We'll build an AI-powered system that delivers 20 to 30 qualified calls monthly—up from your current two or three. In 60 days, you'll hit your annual call target because we discussed what her annual call target was. No more feast or famine. No more wondering where the next month's clients come from. You'll have a predictable pipeline that scales independently of Kelly's calendar."

That's very, very valuable to Kelly.

### The Rest of the Proposal

Next up, we have the rest of our templated proposal. So, you know, there's me looking all fly and whatnot. Then, we give a very high-level breakdown of how we are going to fulfill:

- So, you know, here's how we're going to do it.
- We're going to start by setting up all your no-code and automation platforms according to best practices.
- We give you a 30-minute weekly chat to review progress—like leads generated, calls booked.
- We're going to generate leads, send them to you via Slack for the rest of the week.
- We're going to communicate through Slack.
- We're going to iterate campaigns and so on and so on and so forth.

This is sort of like the scope in a way.

And then finally, we get to the actual investment amount, which in this case was:
- Just under **£10K** for the first month
- Just under **£7K** for the second month
- And then all future months are about **£5,000/month** or so

Okay, we do this because we've just found the three-month or more relationships are best for our clients. And because over a longer time scale, we're capable of delivering significantly more value.

Also, it weeds out a lot of tire kickers and people sort of at the bottom rung of the financial ladder that aren't willing to put their money where their mouth is, which just saves us so much time and energy down the line.

We have some agreements and so on and so forth. And then that's more or less it.

So, what we did is in—I mean, as you guys saw—a sentence, we generated more or less everything we needed in order for Kelly to, you know, be interested in working with us.

Now, I could obviously edit these if I wanted to, but I don't. I feel pretty confident in this.

Now, for the purposes of this demo, I'm just going to send this over to myself and I'm going to sign myself up.

What's really cool about this document is you can actually just charge money upfront. So, that's what I'm doing here. I actually have like an invoice buried in said document. You know, you can automate this. You could set this manually if you have some sort of pre-existing relationship or agreement with a client or whatever. Obviously, you can give them discounts. There are actually a lot of cool options here.

As much as I really dislike how PandaDoc is doing their like $2 per API call billing, it's really really cool to be able to have somebody sign a thing and then immediately get an invoice for the thing.

So if you think about it, our agentic workflow has now done two of these steps. Now obviously we can't spawn an AI agent to go to their house, hold a gun to their head, and say "pay the damn proposal." But in our case, we're just going to assume that they are also now interested and they want to move forward, so they pay.

---

## Automating Onboarding (Welcome Emails)
**[15:28]**

How do we take all of the stuff that, you know, we have to do next and then just automate the hell out of it? Well, it's simple.

I have a simple onboarding sequence and I'm simply going to ask it:

> "Hey, onboard this new customer."

Watch. So in future videos I'm going to show you guys how to use webhooks to automate this process as well—aka automate the very process of writing "great, onboard them" by waiting for an event to come in from the payment processor.

But for now I'm literally just going to say "great, onboard them." And we have a set of onboarding workflows set up that completely automate this process.

Okay, after a few seconds you can see it's now started a welcome email sequence. And so it sent messages to a variety of people. Here's some information around the client and what various emails we're sending and so on and so forth.

After that, we're then casualizing the company names like I talked about previously. That's just like running through all this information—the company names specifically—and then just turning them from like their official versions and their legal versions into the casual ones.

Then finally, it's even going and creating my Instantly campaigns for me by—and this is the really cool part—looking at the highest performing campaigns that I have ever written and then matching those campaigns to the information in the kickoff call transcript, okay, that I will have hypothetically had with this client.

Now, in my case, I'm going off of a demo kickoff call transcript because that hasn't happened yet. But just to run you guys through what is possible here, this is picking up information from a transcript that essentially is like—in our kickoff call, we asked them some questions like:

- "What offers are you comfortable running?"
- "What have you guys run before?"
- "What is your pricing?"
- So on and so forth.
- "Give me some details about your service."

We just talk about that with the customer on like a 30 to 45 minute call. It's very chill. It's literally just like, "Oh wow, that's really cool. Tell me more about this. Tell me more about that. Tell me more about that."

Then we just grab that whole transcript. Then we just give it over to this workflow and it'll automate that completely.

### The Welcome Email Sequence

So because I didn't want to show my actual mailbox here, I'm just opening this in new tabs. And because I didn't want to show the actual email addresses, I'm just doing this all for myself.

But this is the welcome email that we just sent 2 minutes ago. And then it's sort of spaced out a little bit, and I wanted to send them all immediately. So, I just told it, "Hey, send this like right now. Don't wait."

But usually we will send it from, you know, me. So, "Hey, I'm really excited to have you," and stuff like that.

Then after that, we'll send this from another person at our company a few minutes later saying, "Hey, Nick ran me through your company on our last call. So stoked to have you."

And then afterwards, we actually have a final pitch coming from our scheduling assistant, Sam, who does the bookings, that then sends them a calendar link that they can click on in order to book said kickoff with us.

### Why Automated Onboarding Matters

So, I mean, like all this stuff is self-contained. What I really like about doing this automatically is like the customer just paid us, right?

And so, what typically happens when a customer pays you is they're in the situation of **buyer's remorse**. Meaning, you know, in a service they've just paid you money. You have done absolutely nothing for them.

And so, what this does is it helps equivocate the scales a little bit. Instead of sort of like that seesaw being all the way over to you—you know, you just made all of this money and then they're up here and they're kind of sad, okay? And you're like, "Hell yeah, we got a bunch of money without having to do anything."

We're at least providing the perception that like our whole team is getting together. We're really excited about this. We just had a call. We're kicking it off.

And so, I really like doing this in an automated fashion. I personally and anecdotally find that client satisfaction scores shot way the hell up when I started doing this.

And yeah, just a small part of our flow.

---

## Lead Scraping
**[18:26]**

Okay, from there, it's actually gone and then created us a Google Sheet that contains a bunch of leads that it just scraped for us.

Now, I mean, I can't make this up. It just did all the scraping for us.

In addition to doing all the scraping, it also ran multiple tests to determine whether or not these people were within our target markets. So, you know, went through the whole transcript of the kickoff call. It learned more about the business, did a little bit of background research, determined whether or not, you know, it was these sorts of leads or these sorts of leads.

It found out that like we're looking specifically for UK leads. And so, you can see there's a country column here that's "UK."

It then ran a few tests on the company size and so on and so forth. It adjusted the filters autonomously until it got us what we needed.

And you know, this is just a little test list. I only had it scrape 10 because I didn't want to burn through all my Apify credits, but this is a test list of what that output looks like.

We now have a list of leads. And if we go all the way over here to the right, you can see there's actually also a casual company name. So here it just says Lex, Castle, Pharaohs, Bray, Shaw, Mory, Keoop, and so on and so forth.

These are all casual versions of those names, which, you know, if we didn't customize would be kind of weird. They'd be things like "Lex Auto Lease." Well, I'll tell you what. When Lex refers to their company internally, they don't say, "Hey, how's Lex Auto Lease's revenue doing?" They're just saying, "Hey, so what's Lex's revenue these days?" Right?

### The Generated Campaigns

Then I go to Instantly and I open up these three campaigns. Okay:

1. **Offer One:** 15 meetings in 30 days
2. **Offer Two:** 3 new clients in 30 days
3. **Offer Three:** £100K revenue in 90 days

All offers that the customer is happy to make.

And the copy itself is actually pretty good:

> "Hey [First Name]. Quick question. [First Name], [Icebreaker]. Icebreaker is an AI-generated line here. I know this is out of left field, but I work specifically with partners at accounting and advisory firms in the UK. Basically, I build outreach systems that book qualified meetings with your ideal clients on autopilot. I've been doing this for 6 years now. I've worked with 60+ accounting firms specifically, mostly 3 to 10x growth in their LinkedIn presence and pipeline within the first few months.
>
> Here's my offer: I'll book you 15 qualified meetings in the next 30 days or you don't pay a thing. I'll handle everything. You just show up to the calls. Would this be of value? If so, happy to send over a quick video explaining how it works."

You know, is this going to win me any awards? No. So this is like a good 2 to 3% reply rate basis. And from there we can iterate.

Here's a very casual version that the AI actually just thought up. You know, as part of our directives, we say, "Hey, write a casual version and then write a formal version":

> "NGL (not going to lie), this might seem random, but hear me out. I have 200+ clients now. 60 of them are accounting firms. System's pretty dialed in at this point. Was looking into advisory firms in your area and [Company Name] caught my eye. Felt like you'd be a good fit for something I'm testing. I'll book you 15 meetings in the next 30 days. You pay nothing. Zero risk on your end. I cover all the costs up front."

Right. I mean, this is copy that this system just generated for our client completely autonomously based off previous high performers. It's not the same copy as the old one, but it's heavily based off of them because it's so like recent in the context. The copy quality is really good.

We did this two more times with two more offers, right? And over here as well. So, okay:

> "This might be the most aggressive cold email I've ever sent, but here goes..."

I mean, that might actually be pretty good. I don't know. We're going to have to test this.

It also did follow-up messages and so on and so forth, which is pretty crazy.

---

## Knowledge Bases
**[21:25]**

Last, but not least, and I think this is pretty cool—it's actually added a bunch of information into a **knowledge base** here, which is just a Google Sheet I'm using to store information about each company for an automated reply bot.

Essentially, when a reply comes in, we match the ID to the company and then we pull information from the knowledge base, which in our case is a bunch of offers, before then sending some reply examples.

And so, this in our case could be something that we completely automate. This could be something that we manually do. Maybe we manually write two or three reply examples and it just automates the rest.

Yeah, I mean, like the possibilities here are kind of unlimited.

---

## Automating Replies
**[22:01]**

Okay, so I just spent a few seconds updating this reply examples just so it's a little clearer and a little more in tune with what we actually do.

And now I'm just going to ask it to send a reply email, like a hypothetical one, to this email. And then I'll show you guys what the actual reply looks like.

So this is pretty similar to an actual reply received for some campaign that I was running a couple weeks ago. It was somebody that was like somewhat interested, but then they were very incredulous. They're like, "But like, actually, dude, like the guarantee is not..."

So, I'm just going to say:

> "Let's send an example reply to the Executive Social campaign just to show the automated reply bot."

Obviously I can't reply to the Instantly campaign myself. The webhook just takes forever to get back to you and stuff like that. I'm not like in the lead scrape. But I'll show you guys what this looks like conceptually so you guys see.

So it's running through the Instantly auto-reply directive now, which it would do every time it receives an automated reply. And now it's going to create a test to demonstrate said auto-reply system.

### Self-Annealing in Action

Okay. And here's why I really like systems like this built through agentic workflows. Because this workflow was not actually done perfectly the very first time.

There was an issue with one of the keys that I provided. And so because I provided a deprecated key, it ran into a couple of issues. If we just like scroll up a little bit—so I don't want to show the key itself—but yeah, I ran into a couple issues and it wasn't perfect.

So what it did is it actually just **self-annealed**. It found another key that I was using somewhere else and then it provided that key in the thing and then it updated its own documentation to reference the right key.

I mean, this is really cool. If I was running a procedural workflow—one that was like Make.com or n8n—that workflow would have just errored out.

This workflow almost healed, you know, it's like Wolverine or something like that. It gets shot and then the skin comes back.

It's really really cool when you zoom out a little bit and run multiple of these simultaneously.

### The Generated Reply

Anyway, assuming I got a message like this, this is what the system would generate using the workflow:

> "Yeah. Hey Kelly. Yes, seriously. If we don't deliver three new clients in 30 days, you don't pay. Simple as that. At £10,000 average contract sizes, £30K in new revenue against a £9,850 first month investment.
>
> We can take that risk because we've done this for 200 clients over 6 years, including 60 accounting firms in similar spaces.
>
> Is that worth a quick call to see if it makes sense for Executive Social?
>
> Nick"

So, what it did is it:
- Looked up a knowledge base for the campaign UID
- Used Claude with extended thinking to generate a reply
- Addresses the skepticism
- Does some ROI math
- Uses social proof
- Personalizes with the company name
- And then does a soft CTA to actually book a call

I mean, I like this because we are just like putting our money where our mouth is. We even talk about the amount of money that the contract is. I don't always do stuff like that, to be clear, but yeah, I mean I think the model did a pretty good job with what it needed to contend with.

### The Big Picture

And so I mean, like, think about this. We just set all of this up for a client completely autonomously in like 5 minutes.

I just said one thing and I said, "Hey, new client, onboard them." Then it just went through top to bottom and it:

1. Sent welcome emails
2. Scheduled our kickoff call
3. Extracted all those details
4. Began lead generation
5. Enriched and casualized the leads
6. Wrote three Instantly campaigns
7. Set up an automated reply system for the client
8. Even uploaded the leads

And all I really have to do, if you think about it, the only place where I actually need to spend any of my physical effort as somebody that runs the agency is right over here: **It's a QA and a final double check before sending.**

All I need to do is just quickly look things over one final time.

---

## QA & Final Double Check
**[24:52]**

Okay, so just going to do the QA here. It looks good. I mean, the copy itself looks good.

"Send next message in zero days" is probably off. Just going to double check that it's actually one day. Just going to preview this with some basic information here.

Seeing that we're not getting a name, it looks like. So, I just need to change one thing.

Okay. Just going to do some checking here. So, I'm always previewing. Let's head down here. Actually, prefill with the name.

Okay. Looks pretty reasonable to me. I mean, like it's kind of squashed together. That's not ideal, but still pretty solid. Just empty that out. And then use a real person.

Cool. Could save that.

How about the schedule? We obviously need to set it. So 9 to 5, right? I like doing a 7 AM to 7 PM. Personally, that's fine with me. Cool.

And yeah, with the leads and everything like that, rest of that's fine.

So let's just double check this, too. Guess we got an icebreaker here. That's fine. This one. We should probably preview these, too.

Cool. Cool. Let's add some spacing there.

So, I mean, like, consider how much time it would have taken me to do all of this before and then the amount of time it takes me now. I mean, right now, I'm literally just quickly running through adding a little bit of spacing.

And obviously, these are limitations that we can completely resolve with the agentic workflow.

So, yeah, that's pretty badass. So, why don't we just set this to resume?

Cool. And now we have an actual campaign that is running, which is wild.

---

## Comparing Time Needed
**[26:33]**

So yeah, that's about that.

**This whole process here previously might have taken between 5 to 10 hours, right? And now it takes maybe 30 seconds or so.**

Well, maybe 30 seconds is a little underestimation. Let's be reasonable here. Let's just say it's **1.5 minutes**. 30 seconds per campaign.

Not bad if I do say so myself.

Obviously we are automating the replies and stuff like that as well. So this whole fulfillment backend is now 100% possible with agentic automations.

### What's Changed with Agentic Workflows

You know, before agentic workflows you could do a lot of this stuff manually—not manually, rather like **procedurally**. So what I mean is:

- You could certainly begin lead generation. It's just you'd have to know the exact industry ahead of time. You'd also have to know all of the different filters and stuff like that ahead of time, right? You'd have to know the location filters. You have to know how to split those up. You'd have to know the company size filters and so on and so forth. **But now we just have AI do that.**

- You could have done enrichment and casualization before, to be clear. Just would have taken a really long time because you would have had to set up, you know, all of the casualization scripts. You would have had to have the API calls and stuff like that all set up. **This just does it all automatically.**

- Same thing with the casualization. Same thing with the Instantly campaign generation. I mean, like, you could have fed that into AI anytime in the last year and maybe you received something similar, but with all of the context that it has from previous runs of the onboarding, right? So obviously capable of generating a lot higher quality copy, which is nice.

- **Automated reply system** — Hopefully I've shown you. You guys can do that with like n8n procedurally if you wanted to, but it's way cooler when you do it completely automatically and then it also allows it to use decision-making live. So I find that the replies are just a lot more flexible—if that makes sense—but flexible in a good way, not flexible in a bad way.

Same thing with all the rest of these steps.

Yeah, it's just really cool having agentic workflows do it for you.

---

## Step by Step Guide to Automate with Agentic Workflows
**[28:19]**

But you may be wondering, okay, great. So I just saw how to automate more or less the entire functioning of a cold email agency or B2B outbound marketing agency. How do I do something like that for myself?

Well, I'm just going to compile a very simple kind of step-by-step guide that anybody here can follow if they want to automate their work with agentic workflows. And it's very straightforward.

### Step 1: Compile Your SOPs

What you always start with, okay, is you start with **compiling your SOPs**.

Now, people here might not be familiar with SOPs, so let me be abundantly clear. That stands for **Standard Operating Procedure**. And a standard operating procedure is a pretty classic document in any sort of business. This just describes the steps that you take in order to produce some sort of deliverable or outcome.

So if we think about it in terms of the example I just showed you guys, right? An example—steps that I take in order to produce let's say like a lead list—is:

```
1. First I need to generate filters for a lead list filters
2. I then need to test on a sample (let's just say of 25 leads)
3. If greater than 80% (aka if more than 80% are good), proceed
   If less than 80% are good, retry with different filters
4. Scrape default (let's say every new client we get must have at least 3,000 leads)
```

This is an example of a natural language SOP and it's very simple, right? The whole idea here is you write this in terms that like a monkey could understand realistically. And a lot of the time when you're hiring and building out your business, this is the assumption you have to make unfortunately.

But yeah, what you do is you start by just compiling all of your SOPs. So this is a very specific part of one tiny little corner of my fulfillment process, right? Realistically, you probably have like 20 or 30 SOPs across your company. You got to compile all of those SOPs just like this.

### Step 2: Send These to Your AI Agent

Once you're done with that, okay, number two is you need to **send these to your AI agent**.

Now, the way that I'm doing all of this is I'm doing this in a platform called **Visual Studio Code**. Then I'm also using a platform called **Claude Code** with my Visual Studio Code.

Okay. So, if I open up my own instance for you, it looks something like this. I have a bunch of files on the left-hand side. Then in the middle here, I have like my little chat window where I can communicate with Claude Code. And then obviously I have some sort of framework or structure that are provided to the model to help it understand what I want to do.

Now I'm not going to go into the construction of the framework or the structure, but basically like one of these files here is always injected into every model run. And so like when you start with a new language model, this will basically just always store some sort of instructions like in a `CLAUDE.md`, `agents.md`, or `gemini.md`.

And so if you want to, you know, copy-paste this, just check out my recent 2-hour course on how to do all this stuff. And I actually give you guys this file—you guys can just stick that in the root of your project.

### Sending Your SOP to the Agent

Basically, what you do after you're done with that is all we need to do—and I'm actually just going to screenshot this even to show you guys how simple it is—all we need to do is say:

> "Hey, here's the screenshot. I'd like you to generate a new workflow for this. Store it in lead_scraping.md"

So, it's now going to generate a workflow based off of, in my case, the image that I provided. I didn't even provide text.

Hopefully, you guys see you could talk with the model. You could send it a voice recording for Christ's sake. You could transcribe your text like I'm doing here. There's a lot that you could do.

Oh, sorry. Let me click on this text box. Here's a quick example of how you could just transcribe your text. Bonkers, right? Like, I mean, that took me a half a second to say.

So obviously I recommend you guys have some sort of strong SOP for everything in your business. But your SOPs don't even have to be that defined. These models will then help generate the SOPs for you.

In my case, I already have some existing execution scripts. So it's going to try and create a directive based off of those. But I also want you to know you can generate directives without them.

This directive is stored right over here in `lead_scraping.md`. So as you can see, exact same format to the same ones that I showed you earlier—really in-depth, has all possible edge cases and so on and so forth. Very, very powerful.

And then it even gives us a little message saying, "Hey, you know, I made it."

### Step 3: Test This Once

Next up, what you have to do is you actually have to **test this**.

Okay, so test this once. And when you test this once, it's going to ask you for a bunch of things. If you've never done this sort of thing before, it's going to say, "Hey, you know, I need a bunch of API keys. I need a bunch of credentials, right? I need some stuff stored in a `.env`."

Right? What the heck does any of that mean? Well, guess what? You don't actually have to know. The AI will just guide you through it. It'll actually say, "Hey, you know, in order for this thing to work, we need access to these API keys. So, go find these API keys, put them back here. Quick step-by-step guide. Here you go."

And then we're good to go.

### Why Testing Matters

And once you're done with that, then you can actually test. And the reason why you test is because **AI is only going to get this right maybe like 75% of the time the first time**.

And that's okay. It doesn't need to be 100% right the first time because this isn't running the workflow like once and then it forgets about it. This thing is just building a thing and then it's running the workflow and testing it and then you're going to use that information to build it again.

So:
- If it's 75% reliable the first time
- The second time it's going to be 97% reliable
- The third time it's going to be 99%
- The fourth time it's going to be 99.99%

And so on and so on and so forth until it's basically about as close to 100% reliable as you could possibly want it to.

Keep in mind that you're going to have to run this a few times in order to get to that point. But that's the really cool part about AI and the structure and the framework here. If it tests it once and then it doesn't figure it out, then it's just going to continue running until it does figure it out.

And then boom, you now have your working workflow.

### Testing in Action

So, in my case, I'm going to say:

> "Great, run a test on 50 leads or something."

It's now asking me for some basic information. Let's just do real estate agencies and then let's do California.

It actually goes, updates some to-dos, makes a plan for you. It's really cool to use as a builder.

You guys can see here we have an issue. The very first issue is there was some problem with the initial scrape. It tried executing a tool that it had access to and the tool did not work correctly.

This loop will occur as many times as it needs to until it figures it out. It's trying to figure out, "Hey, you know, what's the location format? What am I doing wrong here?" And so on and so forth.

And your hands are off. Like, I'm not touching anything. I'm just having this continuously run, test, iterate, and then retry over and over and over again till it figures it out.

All right. And now it just continuously pushes. Looks like it actually made it work. It's now reading some test scrape file.

Now, it's going as far as actually analyzing the first 10 leads from the test scrape to see whether or not this is good. You can see it's actually going through and it is checking the quality of all these leads. I didn't even ask it to. It's just a function that it built itself.

Once it's done, it now gives me a report:

> "Hey, you know, we exceeded 96% as opposed to 80%. Do you want me to proceed with a full scrape of 5,000 real estate leads in California? I can start anytime."

Pretty great, huh?

I'm just going to say "you could stop here with the 50 test leads" so it doesn't waste some of my credits.

### Step 4: Rinse and Repeat

After you've tested it once, all you do is you just **rinse and repeat**.

So, get a different SOP—one from before—and then just:
1. Send it to the agent
2. Test it once
3. Rinse and repeat

Send it to the agent, test it once, rinse and repeat.

Eventually, what you'll do is you're going to populate—you know, in our case, because we're using the DOE framework—you're going to populate your **directives folder** with:

```
directives/
├── first_thing.md
├── second_thing.md
└── third_thing.md
```

And this way you're also going to populate your **executions folder** with all of your scripts, right? So it'll be:

```
execution/
├── script1.py
├── script2.py
└── script3.py
```

Over and over and over and over again.

### Step 5: Create a Meta Directive

And once you have this, it's actually really easy to go from here to like a fully streamlined solution.

You just have one final step after you're done exhausting all of your SOPs. You just **create a meta directive**.

And your meta directive is really simple. In it, you just say:

> "Hey, I have now had you build a process with all of these workflows. I just want you to combine them together into an onboarding workflow or a project fulfillment workflow or something like that."

And then voilà, you are done.

This thing is now a meta directive. This top-level directive—like the onboarding one that I showed you over here—where it can just go top to bottom and then follow all of the directives that you've created. Not necessarily the executions. And then it follows all the directives.

Once it has one directive, let's say the meta directive, it goes and it finds the three directives for like point 1, 2, and 3. Then it notices that each of these are composed of scripts A, B, and C. Okay? Same thing here—A, B, C. Same thing here—A, B, C.

And then it'll literally just orchestrate the completion of all of those...

---

## Summary of Corrections

### Terminology & Technical Terms Fixed:
- "nadn" → "n8n" (workflow automation tool)
- "Aentic" → "Agentic"
- "Ampify" → "Apify" (lead scraping service)
- "Mosy and Sam Ovenans" → "Hormozi and Sam Ovens" (business personalities)
- "NAN" → "n8n"
- "Panda do" → "PandaDoc"
- "av" → ".env" (environment file)

### Speaker Identification:
- Single speaker: **Nick** (Leftclick / Maker School founder)

### Structural Improvements:
- Added clear section headers with timestamps
- Created numbered step-by-step processes
- Formatted code/folder structure examples
- Added proper markdown formatting throughout
- Fixed run-on sentences and added paragraph breaks
- Standardized quotation and email example formatting
- Created clear visual hierarchy with headers and subheaders

### Content Notes:
- Original transcript was truncated at character limit; content ends mid-sentence at ~37 minutes
- Pricing appears to be in British Pounds (£) based on context (UK-focused campaigns)
- Some product names required verification against known services

### Unclear/Uncertain Items:
- None identified in this transcript