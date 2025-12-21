# The N8N Killer? AGENTIC WORKFLOWS: Full Beginner's Guide

**Date:** November 25, 2025
**Source:** YouTube - https://www.youtube.com/watch?v=bA-WmidVSGo
**Speaker:** Nick (Maker School / Leftclick)

---

## Summary

This course breaks down agentic workflows in a practical, business-focused way, showing you exactly how to build reliable, self-improving automations that handle real work end to end. You'll learn the DOE structure, set up agents in Antigravity, and watch them evolve into autonomous systems that run core tasks for you. It's a full beginner's path to turning agents into effective money machines.

---

## Introduction
**[0:00]**

Welcome to the most comprehensive course on agentic workflows ever created—absolutely free. Up until recently, the term "agent" was associated primarily with a ton of hype and very little in the way of actual business value. But today, the tech is now good enough that agentic workflows are definitively here, and they are without a doubt the future of workflow building.

Now, I'm not exaggerating when I say these will quickly run the entire economy. So, if you've been looking for a way to start learning about agentic workflows to automate business processes and potentially generate a lot of revenue either for yourself or maybe the companies that you work with, you guys are in the right place.

My name is Nick. I've scaled two agencies to over $160,000 in combined revenue. I also lead the most profitable AI automation community out there. It's called Maker School and it generates nearly $300,000 a month in profit. I say this to make it clear—I'm no stranger to revenue or profit. And this course has been created with all that in mind. My goal here was not just to teach you guys technology for technology's sake, but to show you how to use these things in an actionable way that helps you make real money. So, it's a lot less on the hypothetical and a lot more on the immediately applicable.

This course will guide you through three things:

1. **First**, I'm going to show you guys some practical examples of agentic workflows so you can see what's possible like right now. I'm going to frontload this because I think a lot of people have no idea how powerful these things are yet and I want you to see them for yourself.

2. **Second**, I will show you how to build an agent environment that does something called separation of concerns using a simple framework called DOE (or DO for short). That stands for **Directive, Orchestration, and Execution**.

3. **Third**, I'm going to show you guys how to create what are called self-annealing agentic workflows—which are workflows that maintain and improve themselves over time.

We will set up an agentic workflow environment in a popular IDE called Antigravity. You don't need to know any programming or have really any workflow building background. I'm going to guide you guys through everything from start to finish. And by the end, you will have an agentic business operating system that lets you do most of your economically valuable work, probably dozens of times faster than usual through a simple text box.

I've also added timestamps for everything in the description. So feel free to watch this over multiple sessions if you want. That's how I designed it. And if you'd like, please consider bookmarking this video right now so you guys can easily come back to it later.

Ready? Let's get started.

---

## Practical Example 1: Lead Generation, Enrichment & Personalization
**[2:28]**

Okay, so next I'm going to show you a few live production-grade examples of real agentic workflows that are running in my business right now. These are not "hello world" beginner examples. These are flows that are actually generating me revenue and saving quite frankly dozens of hours of manual labor every week. They also operate with a level of reliability that most people think is impossible with current AI.

So, first some background into my businesses so we're all on the same page. My main company is called Leftclick. It is basically a souped-up sales and marketing agency. We use AI to generate leads for a variety of businesses, primarily through outbound marketing, which means cold email. I also run a dental marketing business that does around $2 million a year. And this is similar, although they generate opportunities the other way via inbound marketing, which is mostly ads and PPC.

So, first I'm going to show you a simple system that I put together in less than 15 minutes start to finish that automates a very common task that we used to do pretty much every day. To make a long story short, we are going to start by scraping a bunch of leads and then getting a bunch of email addresses and then doing some enrichment and then some AI personalization on top. And I'm going to start all of this with literally just a single message. It's going to take me a few seconds.

The IDE we're going to be using here, as mentioned, is Antigravity, which is Google's recent agentic platform. And I don't want you guys to focus as much on the code or the way the workspace is set up—just the example, because you guys will be able to build something like this at the end of the course.

Out here in my Antigravity IDE, I have three panels:

- **On the left-hand side**, I have an explorer. This is just a file explorer similar to any that you guys have probably used on a Mac or a PC. I just want you guys to ignore literally everything here except for the **directives** and the **execution** folders.

**Directives** are where we store high-level instructions surrounding how to do a task. **Execution** is where we have the tool layer where it'll actually go and call specific scripts that it itself has generated in order to do a task.

Now, it's not very important that you know exactly how all this stuff works right now. I'm just doing a demonstration. But essentially inside of "scrape leads," we just have high-level instructions that guide it through a process. Then inside of scrape_leads.py, we have a script that actually does the scraping.

Obviously the model could try and do all of this stuff itself with the base tools that it has access to, but that's where you run into issues where the model is so flexible that it doesn't actually accomplish the stated business need reliably enough. What we do instead is we create temporary scripts. If those scripts are good, then the model keeps them and then it adds complexity over time.

Okay, cool. Next up, we have this middle panel here which just stores some high-level access to various things—Agent Manager, Edit Coding, Line Code with Agent, etc.

**On the right-hand side**, we actually communicate with the agent. So, said I wanted to scrape some leads. I'm just going to scrape 200 realtors in the United States. And look at that—I even didn't spell "United States" correctly, but that's okay. I trust that the model with this framework will be able to do what I asked it to do.

So, it looks like the very first thing it's doing is analyzing directives and execution. It's then going through scraping all the information. Now, it's going to open up these thought processes, and you don't necessarily need to look at them—that's not necessarily relevant. This thought process here is just what the agent is going through. And it's feeding its outputs back to its inputs over and over and over.

This is the task implementation plan that is generated. It's basically going to start by reading this stuff, then create a plan. There we go. Then it's going to do some execution steps and then give some verification. Then at the end, we're going to have a Google Sheet with a bunch of leads, which is pretty great.

Now, at this point, you can do a couple of things. I mean, what I do is I just open this in the right-hand side of my Mac and then I'll just have something on the left-hand side of my Mac and it'll just do that work. And then when the agent is done doing the task, which may take 5 or 10 minutes—I mean, we're getting to really long time scales here—it will present me the results and then I can do whatever the heck I want with it.

Alternatively, we can look at what the agent is doing a little bit more under the hood. So very first thing that it's going to be doing is—if I go to a scraping platform here—now I know for a fact it's running this on a service called Apify because that was some of the logic that I built into the high-level directive.

And so I can actually go and I can verify that we have indeed scraped what looks like 25 initial prospects. We scrape 25 initial prospects because that's part of the directive. The directive says, "Hey, I want you to assemble a big list of what you think are realtors using a bunch of filters. If you find that more than 85% of these are in our target market, then I want you to keep them and then run a full scrape. If they're not 85% or more within our target market, then I want you to redo your filters, sort of self-anneal until you find the right set of filters that actually accomplishes that stated task."

And so that's what we did over here. We ran a test scrape, found 25 leads. It then went through and verified how many of those leads were actually in our target market. It accomplished this and realized more than 85% were. And now it's gone through and it's actually found those 200 leads.

So, as you see, we received a console notification saying the leads are now ready in the dataset. Now, what it's doing is it's going to present them to me. Okay, it's now delivering me that information. You can see it right over here. So, we actually have the Google Sheet that contains all of those leads.

And as part of my request, it's even going through and enriching lead email addresses using another service. Now, this may seem pretty complex, but I want you guys to know all that I needed to do in order to get a workflow that did all of this totally autonomously was I gave it a brief bullet-point description, and then I spent maybe 5 or 10 minutes going back and forth with it, having it construct a script that does this.

Now, as a result, we ended up getting 178 out of the 200 emails. And I'm just rechecking this. We've taken those 178 now to 193 because we've done, as I mentioned, some enrichment using another platform.

On the right-hand side here, it just crafted a new column called "casual company name." This is just part of my cold email copywriting SOP within the company. When we send an email out to people, we don't use their company name because that would be kind of silly. You know, "The Balserac Group of AB and Co-Realtors," for instance, is very long. Could you imagine saying, "Hey, Pete, love the Balserac Group of AB and Co-Realtors." No.

Realistically, if we're sending a cold email, we wanted to say something like "Balserac Group." And as you guys could see over here, we've actually done that. It's gone through and it's crafted a casual version of that company name—"Balserac"—just using logic that I had previously baked in.

Now coming back to it, we can see that we now have the results and it's actually formatted it in a very brief overview message that I've asked it to do. It said it scraped 200 realtors for the United States, enriched 15 additional email addresses. We casualized 191 company names. Then we even have access to the Google Sheet.

So I'm opening up that Google Sheet again. It's the same thing that we had earlier, but just for posterity's sake. And all of our information is right here.

How long did that whole process take me? Very, very little time. I now have the data in a format that I can do basically whatever the heck I want with.

---

## Practical Example 2: Post-Sales Call Proposal Generator
**[8:08]**

Okay, let's take a look at another example. This time we're going to be automating the process of a post-sales call proposal and email. You can absolutely build this stuff procedurally like through old-school drag-and-drop, Make.com, n8n, etc. But it's a lot less flexible and the system typically needs to be maintained and updated pretty regularly. With agentic workflows, instead, you just build it once and it will continue to improve itself reliably over time, which is wild.

Okay, so let me show you guys a second example. Now, hypothetically, let's say I wanted it to generate a proposal for me. This should illustrate just to what degree you can use these sorts of things as basically assistants in your business.

But basically, I have a directive stored that's pretty high level that's just called "create proposal." It then guides you through a bunch of lower-level scripts like create_proposal, create_content_calendar, and stuff like that.

So, I'm just going to say "create a proposal." I'm not even going to give it any context. I've stored all of this stuff inside of the directives. In this way, we realistically are building like a co-worker, like an AI employee in our business.

Imagine if you just sent somebody a Slack message like, "Hey, create a proposal." Well, now we're going to get the results.

I'm using a different model here just to demonstrate that you can use whatever models you guys want. In this case, it's now Claude Sonnet 4.5. Although Gemini 3, as of the time of this video, is a really good model. You don't necessarily need to use like the best most cutting-edge models for this information.

And you can see it's still interpreted and understood all of my requests. It's even going as far as asking me a bunch of information. So, as you see, we have "structured info," "call transcript," or "quick details." So, I could actually provide like a call transcript, or I could have it check my Fireflies or whatever the heck. In this case, I'm going to give you guys a very brief company profile.

This is a real customer, but I'm going to be obscuring all their names and stuff like that, so we can generate a proposal that actually makes sense.

All right. And I've just copied and pasted over a bunch of high-level information here. I'm just going to put it in and press enter. Although, you know, hopefully you guys see there are a variety of different ways you could input this info. You could just do it through a call. You could just do some high-level basic details, whatever.

It's now taking all that information and it's actually going through and generating a proposal based off of my instructions. As you see here, we have a PandaDoc proposal task list now.

So, it's going to start by expanding the problems and benefits. The reason why I built this out is because I often just store very high-level understanding of what the client wants in my head. So, I will literally just be on a sales call and I'll just say, "Oh, you know, person wants $45,000 in cost savings for whatever platform."

So, what it does is it takes that information and it expands it based off the context of the company. It'll do a little bit of research into the business and understand what it needs in order to put something together that actually looks nice. It'll do so according to my tone of voice and everything like that.

Okay, it's now creating that PandaDoc proposal. It put together just a giant API request for me and it did so completely autonomously. I should note—like, I didn't have to actually do any of that information in the high-level instructions. I actually just gave it some very brief instructions like, "Hey, I want you to create proposals in PandaDoc for me and send follow-up emails. Could you create me a directive for it?"

It's now sending a follow-up email. It's doing this using an MCP (or Model Context Protocol) tool that I've installed. And now it's sending me a message saying, "Hey, we created a proposal successfully." We've also sent a follow-up email with a four-part implementation breakdown.

So, I'm just going to command-click this, open up this puppy, and as you guys can see, we have the proposal.

Now, I should note that it didn't produce everything in this proposal. I had a template set up here. So, it filled in all of the things in yellow. And this is just a proposal template that I've been using for a variety of purposes.

And as you can see, it's gone through and taken my very high-level details and then gone through and wrote a cool proposal:

> "Systems are innately high leverage, but this leverage can either work for you or against you in your case. And there are a few small persistent problems that are currently impacting growth. Right now, you're burning roughly $50K per year on outreach in Apollo. Legacy tools are built for a different era of sales. The platforms are expensive, clunky, don't talk to each other. And every dollar you spend here is a dollar that could be reinvested in growth. But instead, it's locked up in bloated enterprise contracts that don't deliver proportional value."

Right? I mean, obviously the prompt is, "Hey, write this value-based, talk about savings," and so on and so forth.

We do the same thing for solutions. We obviously have, you know, a bunch of templated information over here. We scroll all the way down to the bottom. You can see we also have the little investment section here that includes a bunch of information around how much money they're paying in month one, month two, month three and beyond.

So I mean, I used a hypothetical company name here and then an email address. But yeah, this stuff works in real production context. I use this all the time.

This was another system that I developed in something like 15 minutes or so. Very high-level instructions. You just give it a brief. You let it know about the self-annealing concept which I'll cover later on in this course and then voilà—it goes and it does things that are actually pretty economically valuable for you.

We're going to cover how to make stuff like this throughout the rest of the course. You guys are going to know how to build simple workflows like this in 15 minutes and essentially just have an AI companion/AI employee that goes out, does things for you, and then returns carrying the deliverable, hoisting it above their head and presenting it to you like a king. It's pretty sick.

---

## Stochasticity & DOE Framework
**[12:28]**

Okay, so hopefully it's clear. These agents are not just chatbots. They are basically universal interfaces that let you control software.

Now the catch is there's actually a fair bit going on behind the scenes that you didn't see. If you were to just open up ChatGPT or Claude Code and paste in a prompt asking it to do what I showed you, it will almost certainly fail. Maybe not the first time, but it'll eventually hallucinate. It'll get stuck in a loop. It might work once at the beginning and then fail the second or third times. Or maybe it'll tell you that, you know, "can't access a file" or whatever other edge failure case that comes up.

So if you're a hobbyist, that's usually fine. And you know, a 50% success rate is probably acceptable to you. But if you're a business and you make, I don't know, a million dollars a month, that is unacceptable. You cannot run a million-dollar-a-month operation on a system that only works most of the time.

If it even screws up literally 2%, that is not just 2% of your revenue. That problem could cost you 100% of your revenue. Consider what happens if you try automating a workflow using agents like this, but it's like to send an invoice or something and you send the wrong invoice to the wrong person. You could literally lose a giant client contract.

So, we don't need just the ability to do things. We need reliability and consistency. Basically, in businesses, we need a system that works every time exactly how we expect them to.

So, to make this work, we need to build a structure around the model that forces it to be reliable, which is what I'm going to talk about with you next.

### The Problem: Stochasticity

So, the problem is really called **stochasticity**, which is like non-deterministic outputs. If you guys were to ask an LLM to scrape leads from LinkedIn, you know, it might work the first time, but on the second or the third time, it may also fail. On the fourth, it may hallucinate a completely different task. And on the fifth, it may say, "Sorry, this is against regulations," or something like that.

To make a long story short, this is not something that is reliable enough for that predefined business pipeline that I just showed you.

The reason why is because in business, even a 1% rate of inaccuracy can lead to a revenue reduction of 50% or more. You know, this is not academic theory here. It's not just a business textbook. This is real life. If you guys send the wrong invoice, even 1% of the time, you don't hurt your business by 1%. You could completely destroy your whole client base.

And because LLMs are **probabilistic** (aka they guess the next token), and business logic is **deterministic** (which means you need the exact same output format basically every time), the two are at odds.

When you try and make an LLM do everything—which is planning, tool use, execution, formatting, whatever—the error rate compounds.

A good way to think about this is: if each step has a 90% success rate, a five-step task mathematically is:

**0.9^5 = 0.59**

To deconstruct all that for you: that just means that this task where each individual step may be quite likely to succeed, on net, only has a **59% success rate**, which is completely unacceptable for any real business operation.

### The Solution: DOE Framework

Okay, so to fix this, we don't just try and make the LLM smarter. What we do is we actually fundamentally change the architecture around the LLM and we take advantage of the LLM's built-in coding tools to do a bunch of the heavy lifting for us.

So instead of asking an LLM to do something directly, we're just going to ask it to create a standardized piece of code to do that thing—which is, you know, philosophically the same thing that people were doing 30 to 40 years ago. There's no difference. Then it just uses the code that it wrote to do the task itself.

This significantly mitigates the flexibility of the outputs and it also allows you to leverage what AI is fantastic at, which is **code** (because that's what everybody's making AI to do), while minimizing what it is bad at, which is **reliable, predictable flows**.

Okay, so how do we do this? Well, in order to make this happen, we need to split the work of the LLM into three distinct layers:

1. **The Directive Layer**
2. **The Orchestration Layer**
3. **The Execution Layer**

What's great about this is this is the exact same structure used by a lot of very successful human organizations. You will have:
- A **manager** (equivalent to the directive)
- An **employee** (equivalent to the orchestrator)
- **Tools** (equivalent to the execution)

### The Three Layers Explained

So, let me explain the structure in real context and then why this specific one is the key to, in my opinion, unlocking reliable agents.

#### 1. Directive Layer (The "What")

We start with the top, which is your **directive layer**. These include workflows, SOPs. For people that don't know what an SOP is, that just stands for **Standard Operating Procedure**.

And essentially what we do is we write all these out in some form of easily formattable text, which in our case is going to be **Markdown**. The specifics of Markdown aren't super important if you're not really sure what that means. Essentially, it's just a way that you can format and add some form of structure to text without having to consume a ton of tokens.

And what these are—these are high-level instructions that just guide an eventual orchestrator through what a process looks like.

An example might be a recipe, right? You are looking up a recipe on how to make, I don't know, some tofu or something like that. And step one says "add soy sauce, vinegar, and whatever to a container." These are high-level instructions, but all they do is they describe what the agent is going to do and define guardrails that an agent eventually goes down and chooses of its own accord.

Okay, so high-level instructions are where directives come into play.

#### 2. Orchestration Layer (The "Who")

From there, we obviously need something to actually go and take those high-level instructions and then reason over them. And that's where your **AI agent** comes into play.

Now, you notice that I also wrote "slash employee" over here. Why? The reason why is because this is actually a very similar structure to the way that most large organizations work. Most large organizations will have high-level directives written as workflows or SOPs in natural language. And then an employee will be responsible for digesting them, then converting them into more actionable tasks.

But anyway, in our case, for our purposes, that's where our little AI agent comes into play. So, our AI agent essentially gets to do a **reasoning loop**. And so, it is going to:

1. **Read** through our directive
2. **Choose** an action
3. **Execute** said action
4. **Evaluate** the results

This same loop here has been called a million different things. I'm going to leave it at read through, choose, execute, and evaluate. But as long as you understand that there is a sequential series of steps that any sort of software agent is going to follow, you guys know more than enough. Don't worry too much about various conventions or acronyms or whatever. Those aren't things that actually help you understand and make money.

Okay. So, these AI agents go through these reasoning loops. They coordinate and they're responsible for the ultimate task management. They function very similarly to maybe like a mid-level manager or something like that.

#### 3. Execution Layer (The "How")

Once you have chosen sort of what to do next, you need to execute and that's where the **execution layer** comes in.

And so essentially the AI agents/employees in your business will then go out and pick particular tools, usually tools that it's already developed, or it'll go and write tools in the form of **Python scripts**. At least that's my recommendation. There are a variety of different languages you can use for this, but Python scripts tend to be the best just because Python is the language that most of these large language models were trained on initially. There's an overabundance of Python code out there and Python's used as artificial and synthetic data for a lot of these as well. So they just tend to work really well with Python.

And then, you know, these produce some sort of output. Okay, this is the output. I don't know, could be maybe some numbers, could be some strings, whatever the heck the purpose of this Python script is. In the example that I showed you guys—could be a lead, could be a PDF.

And then that information actually loops back here to the orchestrator, the agent, which then reads the results and then can actually choose if it wants to go upstream and manipulate the very directive as well.

### The Orchestrator as "Glue"

So this orchestrator, you can kind of think of this as a **glue**.

Now, anybody here that's worked with traditional no-code or low-code platforms before, this orchestrator works very similarly to Make or n8n or Zapier or any one of these platforms.

All of these drag-and-drop platforms basically back in the day (and now) are nothing more than glue which routes business logic through nodes and then allows you to choose sort of what direction those things go based off of some preset logic.

And so the orchestrator in this case is the Make, n8n, Zapier, Lindy, Gumloop, etc. It's just now what we're doing is replacing that orchestration with AI agents.

So, agents are actually basically the **routers** and they're responsible for choosing what to do and when to do it.

What's really important here is there is **no code or any sort of executable written in the directive layer**. The directive layer is literally just a bunch of natural language prompts. When I say SOPs, I literally mean SOPs. They're the exact same type of standard operating procedure that you would find in any company, which is why this is so valuable.

If you take the DOE approach, you could literally take a pre-existing list of all of the standard operating procedures in a business and just drag and drop them into your IDE and boom—you've already accomplished one of the three main layers here. Literally just having a list of things to do.

You can then feed that into an agent, have the agent refine, and then convert that into lists of actionable tools so long as you provided things like API keys, connectors, and so on and so forth, which is much easier than it sounds.

### The Minecraft Analogy

So, I don't know if you guys have ever played a popular video game Minecraft before, but if you haven't, essentially what happens is you're this character and then, you know, there's a bunch of blocks around and you start off the game by just like beating a block and then, you know, the block outputs some wood or something like that.

And as you progress in the game, you can add a bunch of wood to your inventory and eventually put the wood together in specific forms and then, you know, instead of just having to punch a block with your hand like a savage, you know, you could kind of build yourself out some sort of hatchet. Okay. And it starts off as a wood hatchet, but then you can continue pumping down more and more of these wood blocks and eventually, you know, reinforce the hatchet and start attacking some stone or something.

I'm obviously butchering this. Anybody here that's actually played this game to any degree should know. Man, it's been a while since I've fought the Ender Dragon or whatever the heck it's called.

But, to make a long story short, I want you to think about tools kind of like a character in Minecraft. You start off with absolutely nothing in your execution folder. Okay? All you do is you give high-level instructions and then the agent will actually start making things like, you know, a pickaxe. Then it'll start making things like, I don't know, like a hatchet. It will start making things like, I don't know, some sort of sword or armor.

And what's really cool, okay, is once it's made these, it can then go back and reinforce these and then it can upgrade them. And eventually you can get to your little diamond fortification or whatever where your stuff is just really really good.

It can, you know, replace one-off endpoints with bulk endpoints or batch endpoints. It can economize the code so that it runs a million times faster than it did initially. It can go from like a Big O of N² all the way up to like an O of N or something. Like, the potential here is pretty unreal and once you build this environment or ecosystem, it just gets better and better and better.

### The Caveman Analogy

Another way to think about this is, I don't know, some sort of caveman let's say in prehistoric times. This is Mr. Sad Caveman because he doesn't have anything and there's some big saber-tooth tiger.

You know, saber-tooth tiger attacks him the first time. What's he going to do? He's going to try punching him. He's going to find a rock on the floor. He's going to throw it. Not all of these things are going to be hyper-effective, right?

So, what he does is, I don't know, goes and makes a spear. Next time you see a saber-tooth tiger, what are you going to do? You're going to pick up the spear. You're going to use that, right? As you eventually do this more and more and more, your spear is going to get better, more reinforced. It's going to be more capable.

So that in a nutshell is a good analogy for what is really going on here, especially in a self-annealing sort of situation.

### Why We Do This

Why do we do all of this? We do all of this to **reel in the inherently probabilistic nature of large language models**.

Essentially on the left-hand side is the way that most people view these things. And it's the reason why agents up until quite recently haven't really been able to be used in any sort of real business scenario. This delivers an uncertain outcome. And while it's a lot more flexible, as you can see, these arrows are sort of going all over the place.

Ultimately speaking, in a business, you don't want flexibility. In a business, you want **determinism**. You want a very simple and easily interpretable list of rules where if an input comes in here, we route it based off of some filter that we have.

And so what we do is we take the inherently flexible probabilistic nature of LLMs and use it to create a bunch of **deterministic pipelines** and then it just calls the specific pipeline that it wants while making it better and better and better over time.

### Speed Benefits

The last major point I'm going to make is **speed**.

The historical way that you get things done by calling LLMs with some sort of built-in tooling like HTTP requests or whatever is very slow. Okay. But when you use tools you can go very fast.

I mean, just as an example, imagine if you fed a list of 10 items, okay, into some sort of LLM and you said, "Hey, I want you to reverse sort this or something like that." So, I basically want you to take this list that's alphabetical and I want you to do this. I want you to take all the letters and I want you to reverse them.

If you did this within a large language model, it would actually have to calculate an enormously massive matrix—you know, series of arrays and matrices in order to do the simple task of just reversing or flipping this array.

Whereas if you created a specific tool like in Python to do this, you could do this virtually instantaneously.

The order of magnitude in the amount of time it would take to do the top thing (okay, using an LLM) to bottom thing (using a tool) is something like **10,000 times if not 100,000 times**.

Not to mention you also have no token usage making this—while not actually free because you are going to be using your CPU and maybe some sort of server if you want to host this elsewhere—it will be **effectively free** compared to just how much time, energy, and resources are being run in order to do silly requests like this using LLMs.

### Folder Structure

So now that you guys understand at a high level how the three-layer software architecture works, let me just run you through what it'll look like exactly within your integrated development environment.

Remember how earlier when I was showing you guys the lead scraping example, I hid a bunch of the additional folder structure and stuff like that? The reason why is because these are things that are specific to the development environment that you're using.

But regardless of the development environment you're using, you will always have the following folders. Let's just call this our **workspace** and just pretend that this is up at the very top. It's just like the big folder that contains all the other folders.

The folders that you will need in order to get this done in this way is you will need:

```
workspace/
├── directives/
│   ├── SOP1.md
│   └── SOP2.md
└── execution/
    ├── scrape_leads.py
    └── enrich_leads.py
```

Within **directives** are going to live all of your SOPs (Standard Operating Procedures in Markdown format).

Within your **execution** folder is going to live all of your executables (Python scripts).

Now, we only have directives and execution here. Notice how we don't have the orchestrator. The reason why is because **the orchestrator is the LLM**. And the LLM—sort of the big galaxy-brain intelligence over here—reads through the directives, associates them with specific executables, runs them (so actually executes these things in some sort of terminal prompt), and then it just loops back and forth and back and forth over and over and over again.

If you can understand what I've just put in front of you here at least at a high level without understanding any of the programming concepts or anything like that, you can build a very good agentic workflow.

### DOE Summary

Okay, so that's the **DOE** (or DO) framework:

| Layer | Alias | Role | Description |
|-------|-------|------|-------------|
| **Directives** | SOPs | The "What" | Intent, goals, rules of engagement |
| **Orchestration** | Agent | The "Who" | Decision maker, router |
| **Execution** | Code | The "How" | Reliable, deterministic machinery |

By pushing the heavy lifting onto those deterministic Python scripts (which is the execution) and then keeping the instructions really clear in Markdown (which are directives), we let the LLM do the one thing that it's actually really good at—which is being a **very intelligent router**.

That solves a reliability problem, meaning your scripts will run the same way basically every time because a Python script does not hallucinate. It either works or, you know, it errors out. And if it errors out, we can catch it. All your agent has to do is decide when to run the thing.

---

## IDE: Integrated Development Environments
**[29:15]**

Right now, the vast majority of agentic workflows are going to be built in what's called an **Integrated Development Environment** or **IDE**. I've talked a little bit about Antigravity before and that is beyond the purpose of our course.

But I am sure that future agentic workflow builders will include dozens of different input methods and ways to build them that aren't in a terminal-style environment.

But Antigravity isn't the only IDE available and I want to run you guys through a brief little laundry list here.

What I'm going to do next is I'm going to break down how most IDEs work just so you guys are familiar with it from a bird's eye perspective and then also a couple of the tools we're going to be using. And then after that we're going to learn self-annealing before we actually set it up all in a real environment.

By the way, if you guys are already developers or you understand how IDEs work, you can skip through this section and then move on to the next one. And I should note, I'm not going to be giving you guys an academic or textbook definition of how an IDE works. We're just going to be working through it from a very practical perspective, aka what you actually need to know in order to get out there and build workflows and make money with these things.

If you guys want a much more in-depth review, there are a variety of resources. Basically, every IDE known to man—just search up the name of the IDE and then the word "tutorial" and the service that built the system will provide one.

---

## Antigravity: IDE Walkthrough
**[30:20]**

Okay, next up, I got a brief walkthrough for you of a typical integrated development environment. And I'm going to do this for two IDEs:

1. **Antigravity** (this one over here)
2. **Visual Studio Code** (this one over here)

I wanted to show you both because Antigravity is certainly the newer kid on the block. Just launched like within the last week, I believe. But Visual Studio Code has a much bigger user base. A lot more people are used to it.

Regardless, you'll see that the concepts are very similar and they map basically one to one.

### Antigravity Layout

Okay, so starting at the top left of Antigravity, as you see here, we have that **file explorer** that I was referencing earlier. This file explorer is very similar to just the base file explorer on your Mac or your PC. It's just a way that you can organize files.

Now, in order to get to these files, you do need to open a specific folder on your computer. And so, if you've just launched some sort of Antigravity IDE or maybe some sort of Visual Studio Code thing, you actually do need to create or open a folder in order to access what we are seeing here.

Okay. So in my case, you know, I opened up this workspace folder and that's why I see what I'm seeing on the left-hand side. So within that I have this `agent.claude.md` [possibly: `agent.claude.ve`] and then I have my directives, execution, tmp, and this is just the course that I'm actually recording for you guys right now as well as some additional files.

The specifics of the files aren't very important again because I want this to be programming agnostic. Depending on your background or whatever you will know what some of these mean and you won't. That's okay.

I want you guys to know that basically all of these were done completely automatically. I didn't actually like exert any control in choosing the structure. This is just something that the agent came up with after reviewing, you know, effective software architectures and stuff like that.

So the things that are ultimately important for us are the **directive folder** here and then the **execution folder** here.

### File Types and Visual Indicators

Okay. So now that you understand a high-level overview, just pay close attention to a few things.

Different file types typically have different sort of graphics and whatnot. They also have different file endings.

And so a **Markdown file**, for instance, if I click on my "scrape leads" here, it has that little M with a down arrow and then it's a `.md`, right?

The **Python script** on the other hand, you'll see changes a bunch of colors within and then it has this little—this is supposed to be a Python—with a `.py` at the end.

And so superficial information here, but you're already starting to see there's significantly more structure in code. It's almost like looking at a rainbow versus looking at, you know, the Markdown directive. And that's just because in code there are a lot more—I want to say like data types that you need to keep track of.

For instance:
- **Green** here are comments
- **Blue** might be variable definitions
- **Purple** might be some sort of logic

And so on and so forth. So, you don't actually need to know any of this stuff, but when most people are new to IDEs and programming and they download one of these things and they start poking around, they get really overwhelmed because it just looks super complicated.

### Working with Files

Okay, cool. So clearly what we do is we select files on the left-hand side here. Then we open them in the middle. So that's something that's worth taking a look at.

You have one open picker at a time, but you could actually open as many as you want. Just "open to the side" this one, "open to the side" this one, and so on and so forth, and it becomes pretty cramped.

You could use the same sorts of hotkeys that you normally use on, I don't know, like a Chrome instance or something. So in my case, I just hold Command+W, and then I can actually delete open windows. That's pretty useful.

On the right-hand side here, moving over a bit, you see that there's actually like a top-level overview of your code. This is marginally useful. I believe this is like a VS Code feature initially and now basically every platform has used it just because sometimes you can go very, very long with these big, big code files. So this just allows you to see the architecture at a glance and then, I don't know, quickly run through and then find a specific point in the code that you want.

I don't actually ever use this to be clear, but I just want to be able to explain what's going on under the hood so that if anybody's super intimidated, at least now you know.

There's also up here a **folder picker** which actually goes through and then shows you the specific folders and then more importantly the functions and the classes that you're in. And so I'm actually within this `fetch_campaign` function here. If I go to `get_api_key`, you'll see this now changes to `get_api_key`. Pretty wild.

But this is more or less what we're doing. We're creating a folder that contains a file and within that file are a bunch of subfolders almost. It's just these are called **functions**.

### Python Readability

Now, the good thing about Python is it is pretty readable. Not that you'll ever have to read it, but it is pretty readable if you ever did want to poke around. And when you add the right thing into your `gemini.md`, which I'll cover in a moment, it actually comments the code reasonably well. So, you can at least take a look at some of the code if necessary in order to get a high-level understanding of what's going on.

For people here that are more used to let's say no-code platforms like, you know, n8n or Make, I just want you to look at all function definitions. So `define get_api_key` and I want you to just treat that like a **single node on a graph**. That's basically what it is.

So this is your `get_api_key` node and maybe this one here is your `fetch_campaign` node. You know, this one here is your `extract_sequences` node and so on and so forth. It's just instead of it being nice and easy and visual left to right, obviously, this is laid out sort of top to bottom here in language that most people do not understand natively.

So, that's the main drawback right now. But, as I mentioned, future gen coding platforms are almost certainly going to all be drag and drop.

### Antigravity-Specific Features

Now, in Antigravity specifically, if we go to this middle panel here, you'll see that there are a couple of options.

If you hold **Command+E**, you'll open your **Agent Manager**. Your Agent Manager is basically just like a one-off chat box where you can talk to a model without actually having to look through, you know, all of your code and whatnot.

I mean, it'll still look through your code, but this just basically takes everything on the right-hand side, sticks it right in the middle. Then you can do Q&A. You can do whatever the heck you want with it, which is pretty nice.

You can also construct specific agents for different purposes, which is kind of neat. And you can even insert knowledge items into your Antigravity instance. So that if there are things that you know you specifically request pretty often that a model wouldn't really know, eventually the model will actually add that to a knowledge base so it'll constantly be able to consult this before answering your question.

Up at the top you have an **inbox**. That inbox contains basically all of the notifications that the agent has made for you. This is something that's Antigravity-specific and it's really cool. I really like it. It's one of the cool parts about this that I think a lot of other IDEs still have to catch up on.

And it's also a good example of these platforms moving more towards like agentic co-working than necessarily just building in code.

When you start a new conversation, by default, you start it in the **playground**. The playground is just a new conversation instance that is not tied to any particular workspace. But as you guys see here, you could also open a specific workspace that you guys have discussed with a model before if you want to.

They also have the ability to open **new remote workspaces**. So, this opens up the possibility to do things on other hardware later on, which is pretty cool.

### Browser Use Feature

There's also a **browser use** feature. So, as you can see here, if I click "always allow," it'll actually go and it'll request a specific web page that I've given it access to, and even pull in things like DOM elements (Document Object Model for those unaware) that allow you to do cool browser automations.

This is my website here, Leftclick, and it's going through, scrolling a page, extracting elements, basically giving me a bunch of information here. I just said, "Okay, go to Leftclick, tell me what's on it." That's kind of neat.

And if you're new to this feature, just head to the bottom left-hand corner of the Agent Manager and you'll get everything that you need in order to do that.

We're not going to be talking as much about that in this course just because it is unfortunately still sort of shaky. Only works maybe 70-80% of the time. Certainly not good enough for real enterprise business...

---

## Summary of Corrections

### Terminology & Technical Terms Fixed:
- "anti-gravity" → "Antigravity" (product name standardized)
- "ampify" → "Apify" (scraping service)
- "pandock" → "PandaDoc" (proposal software)
- "nadn" / "nan" → "n8n" (workflow automation tool)
- "lindy gum loop flow" → "Lindy, Gumloop" (separate tools)
- "techny's sake" → "technology's sake"
- "copyrightiting" → "copywriting"
- "self-anneeing" → "self-annealing"
- "MCP or model context protocol" → "MCP (or Model Context Protocol)"
- "big O of N squared" → "Big O of N²"

### Speaker Labels:
- Single speaker identified: **Nick** (Maker School / Leftclick founder)

### Structural Improvements:
- Added clear section headers with timestamps
- Formatted code examples and folder structures
- Created tables for framework summaries
- Added proper markdown formatting throughout
- Standardized quotation formatting
- Fixed run-on sentences and added paragraph breaks

### Unclear/Uncertain Items:
- [possibly: `agent.claude.ve`] - original audio unclear on exact filename
- Transcript was truncated at character limit; content ends mid-sentence at ~37 minutes

### Content Notes:
- Original transcript contained significant background noise artifacts
- Some product names required verification against known services
- Timestamp markers preserved from original source