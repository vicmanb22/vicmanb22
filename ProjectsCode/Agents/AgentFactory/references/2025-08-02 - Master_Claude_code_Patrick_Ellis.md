# Master Claude Code: Proven Daily Workflows from 3 Technical Founders

**Source:** Patrick Ellis, YouTube  
**Video:** [Master Claude Code: Proven Daily Workflows from 3 Technical Founders (Real Examples)](https://www.youtube.com/watch?v=hOqgFNlbrYE)  
**Published:** August 2, 2025  
**Speakers:** Patrick Ellis, Anand Tyagi, Galen Ward

---

## Introduction

**Patrick:** If you're using Claude Code by just typing in prompts as though it's another ChatGPT, you're missing 90% of its value. Claude Code comes off deceptively as just another lightweight command line tool, but really, under the hood, it's much more than that. It's the first in a coming wave of highly powered AI agents. Understanding how to harness that power is critical, and I think it might be what's holding you back from being fully blown away by Claude Code's capabilities.

My name is Patrick. I'm a CTO and co-founder of an AI-native startup, and I've been using Claude Code since February. Earlier this week, I spoke to a group of founders in Seattle alongside my friends Anand and Galen about the core principles to employ and the tactical frameworks and tools to get the most out of Claude Code.

We'll cover a range of what we feel are the most valuable topics, including using MCPs to give "eyes" to Claude Code, using the double escape method and resume method to fork Claude Code context and spin up multiple instances, automated code review (one of my favorites and extremely helpful), a quick state of the union of the top code gen tools including Codex and others, the "My Developer" prompting trick that Galen demos towards the end of the talk—that was actually one of my biggest takeaways—and how we structure validation steps to ensure Claude knows what is good and what is bad output, among many others.

In the description, I've greatly detailed each section and the topics that we spoke through. So if you're already familiar with a topic, I'd highly recommend skipping through to what's interesting and relevant, as there are a lot of good gems in there, in my unbiased opinion. I've also linked the slides from all three of our talks so you can reference that. I hope this helps you unlock the next level out of Claude Code.

And with that, here's Anand to kick us off.

---

## Part 1: Core Concepts & GitHub Automation (Anand)

### When to Use Claude Code vs. Cursor

**Anand:** This is the main question that I get asked quite a lot: what's the difference between Claude Code and Cursor?

I think it sums up to this: Claude Code is really good at multi-step processing. You have a large task you want to get done, and it can break it down into subtasks and execute them one by one.

I use it for starting projects constantly. I post a new project every other couple of days just because I'm able to create a really good spec and planning document, which I'll get into later, give it to Claude Code, and just let Claude Code run freely. That's probably not great to do, but there are no stakes to these random side projects, and it's really good at that because of that reflective loop.

If there's a lot of complexity—what I mentioned just a minute before, where you have to pull in a lot of things from different files—it's good at doing that as well. And if you have a very long-running process, I tend to prefer Claude Code.

Cursor is still really good at solving specific problems and addressing very specific files or lines of code, because you can select those things very easily.

---

### The CLAUDE.md File: Your Project's Core Context

**Anand:** Let's go into the CLAUDE.md file. This file is your main context file. When you run `/init`—and we'll get into what that means in a sec—it will generate an overview of your codebase. It'll go through all your files, figure out how everything is set up, and make detailed notes about the startup processes and where everything is located.

I like the quote from the documentation: "Your CLAUDE.md files become a part of Claude's prompts." I mean, that's what literally happens. So they should be refined like any frequently used prompt. Effectively, think of it like a README built specifically for Claude Code.

The `/init` function is great, but I have my own set of commands that I run where I ask it to go through every file and first extract the file structure and the folder structure.

---

### Pro Tip: Create CLAUDE.md Files for Every Subfolder

**Anand:** Then, for each of those folders, I have a new CLAUDE.md file. So in each subfolder I have a CLAUDE.md file, and effectively you can create detailed notes—detailed READMEs—for every single subfolder, to the point where you can track every single function and file.

When Claude needs to do an operation, it's no longer grepping like crazy. You can have it just look at those CLAUDE.md files. As long as they're updated, it will drastically reduce how much cognitive load it's taking on.

**Audience Member:** Is the file more like the Cursor rules file? Like, how do I prompt?

**Anand:** It's kind of a mix. Cursor rules are effectively prompts that go into Cursor, right? But it's also a README of your entire codebase. So it can act as both.

Here's a good example of what I have in my actual Claude files. This is the main one. I have a backend and a frontend. So I say, "Here's how it's set up. My frontend has this kind of setup, my backend has this kind of setup." I have it cover the frontend structure, which actually then also has a much more detailed list in the frontend folder itself. Then I have my backend structure, which is in the backend folder but in more detail.

I can extract those up into my project folder or company folder. So it's easy for me to see, but also easy for running things cross-codebase or cross-repo—it's a lot easier to manage them.

Some other markdown files that aren't talked about as much but are very useful are things like the changelog. If you have a good changelog, it's easy for Claude to realize over time what changes were made and why. Every time you make a change, just ask it to update the changelog separately from the CLAUDE.md file. That gives it a good understanding of "here's why I changed it" and "here's why we shouldn't go back to doing this."

I use a `PLAN.md` file for every new project or every new task that I start. It's effectively the list of things that I actually want to get done in a single document.

---

### Incredible Feature: Integrating Claude with GitHub for an Automated AI Teammate

**Anand:** Now here's the one major thing that I want to touch upon that I think is really interesting: you can attach Claude Code into your GitHub repo.

This basically replaces—well, effectively it *is* Devin—but using your Anthropic key. It's super easy to set up. You just run this command; they automate everything for you. There really is no hassle.

Then you can go in and create an issue. I had some project I wanted to do, so I was like, "Create this component for the library," and I tag Claude like I would tag some developer. It goes in, creates the issue, creates this to-do list checklist, executes that. And later, when I'm actually like, "Hey, this wasn't that great," I can just tag it again in the PR like I would with an actual developer, and it'll go through and do that again.

I can do way more things using this process than I can just on my own computer running one agent—or even multiple agents—at the same time. It's extremely convenient.

Claude Code also has built-in commands like "review PR comments" that allow you to effectively automate the review process from your console, fetching the comments so that it can then operate in your local environment. These commands are built in. I would really recommend exploring them.

I could just run 30 different commands at the same time. I used Claude Code to say, "Here's a list of all the features I want to build. Generate PRs for every single one of these, and make sure you tag @claude at the end of it so that it will spin off the job."

And it was able to do that. This wasn't my phone—like, by the time I got home, it was all complete. It was just amazing.

**Audience Member:** With the integration with GitHub, or just on the CLI?

**Anand:** No, from the CLI. You can integrate it into GitHub. So it's effectively an app running there, but it is the Claude Code bot.

---

### How to Use Commands to Create Reusable, Shareable Workflows

**Anand:** Now we'll get to commands. A command is just a prompt. It's a prompt that you can save in a file, share amongst projects, share amongst your team. You can develop these very comprehensive step-by-step things, and you can actually run them just like you would the PR or the "install GitHub" commands that are built into Claude. You can write your own.

Why this is great is because you might have specific things you want your team to know. Or if somebody on your team is a Claude expert or an AI prompt expert and they write something amazing, you can now share that with the entire team. It's super easy to use.

You should really look into using commands, which allow you to create these comprehensive workflows just using a prompt that Claude can then easily follow.

This is, for example, a codebase analyze prompt that I can use to set up my really comprehensive analysis in a CLAUDE.md file. You can see it's super long, but it works. I even made a GitHub Action that can then be run right from your GitHub interface.

These are just all the commands that I've collected. Anyway, here's the website and QR code if you're interested. I've just made it really easy to add. Disclaimer: I made this, but I really do believe it's a really good way to share those ideas.

You can also launch subagents. If you're just starting off with Claude Code, don't even think about this yet, but you can basically run two things at the same time. It's pretty cool.

**Audience Member:** So the analyzer command was the command you were talking about to generate the CLAUDE.md files?

**Anand:** That's one I use to make a more comprehensive CLAUDE.md file. It can just be to analyze the codebase in general.

---

## Part 2: Agentic Systems & Advanced Setups (Patrick)

**Patrick:** Hey everybody, my name is Patrick. I have been using Claude Code since it came out back in February 24th, which feels like forever ago, but it's been amazing to see just the constant evolution of new features.

One of the coolest things I feel about Claude Code is how the Anthropic team very obviously works closely together on the ML and AI side—so the actual machine learning researchers that are doing the post-training and the fine-tuning—along with the actual product team. You see this close coupling with Claude Code that I think really sets it apart from any other experience.

I was just listening to the Cline founders on the Latent Space podcast—excellent recommendation, by the way, that podcast episode and just the podcast overall. They were talking about how Opus 4 and Sonnet 4 just so badly want to use bash commands to grep around, as Anand was speaking to. There's a whole realm of preferred bits of what Opus 4 and Sonnet 4 try to do that fit really well with Claude Code, given that the application and machine learning teams are speaking closely together.

So that's one reason why Claude Code is fantastic to use.

---

### Beyond Code Gen: Thinking of Claude as a Multi-Step Agentic Tool

**Patrick:** Let me speak a little to the fundamentals of Claude Code. What makes this more exciting and interesting—and thus all the hype recently—over a Cursor or other platform?

From my perspective, the biggest pieces here are that we're doing much more than just code gen. We're really working with one of the first in-production agentic tools that can do multi-step processing on the order of roughly an hour or so.

You can think a lot broader than just code gen in terms of applications for this, which I'll get to with a few of my favorite non-coding workflows in a second. But feeling the character, the nature of what helps these agents run for longer and get more accurate towards what we're actually trying to execute with them—all of these factors are really helpful lessons for us to be learning and internalizing now as we're building agentic workflows in other domains, in our own products, or using tools such as Gemini to summarize YouTube videos or whatever other workflows we might have.

So that's one amazing part of Claude Code. Claude is also fine-tuned for tools that Claude Code takes great advantage of. You've got the bash-type commands—being able to grep your codebase and use the GH (GitHub) CLI tool. But we also have the native tooling: web search, file search.

One of my favorite bits is this to-do list. Back in the day, I'd always create these PRDs [Product Requirements Documents], which is still a helpful workflow, but for most things, I can just defer to Claude Code doing the Shift+Tab, Tab to get it into planning mode, think through and iterate on the spec of what we're trying to accomplish, and then allow it to create a little to-do list to keep it on track.

Especially when it's handing off between different steps and using subagents to summarize different parts of the codebase or think through and do research, being able to pull that back and keep grounded in the to-do list—even if it's a little six-bullet to-do list—is super helpful.

---

### The Power of Reflection: How Claude Self-Corrects Its Own Mistakes

**Patrick:** A few other tools, such as its ability to reflect on what it's outputting, is an absolute game changer.

I see this happen quite a bit, where it'll work through something and be like, "Wait a second. This actually isn't the best approach to this," or "This assumption was mistaken." That ability, as you can imagine when you're trying to let it run on a task and come back in 15 minutes or whatever to verify the output, is super helpful. It's just one less touch point—and usually multiple less touch points—that you're having to go in and babysit the model for, in addition to the output just being much better with that reflection piece.

So there's a number of reasons why that pairing of Opus 4 specifically—but Sonnet 4 as well—with Claude Code is a really incredible and productive workflow.

One note too: when you're using Claude Code, if you run `/model`, you can choose Sonnet versus Opus. Just in case you're not aware of that, the default is Sonnet. Opus is four times more expensive, but if you're on the Max plan—which is a $100 or $200 a month plan, which I'd highly recommend—the amount of inference we get is ridiculous.

I mean, I would estimate if I'm fully using Claude in a month, it's on the order of $3,000 to $5,000 in terms of API costs, but it's $200 a month flat. So I don't know how long this is gonna be around or if they're gonna try to water it down like Cursor or others.

So I wanted to mention the different types of agents, just to give a quick overview. We've got, of course, chat-based agents, which we're all familiar with: ChatGPT, Gemini, etc. We also have these CLI and IDE-based agents. Claude Code of course being an example, Cursor, Windsurf, the brand new Kiro from AWS/Amazon, Cline, etc.

And then we have background agents, which are just starting to roll out over the last couple months. Codex, which also has a CLI tool, but of course with OpenAI's Pro plan, at least you can kick off agentic processes that will run anywhere from one to four different instances of O3. And I would also loop in the GitHub integration, which I won't belabor since Anand talked about it, but it's incredible.

---

### How to Supercharge the GitHub Integration by Modifying the YAML File

**Patrick:** One of our friends, Sam, just walked me through this absolutely mind-blowing workflow that he's got. He basically took the integration that you can build with Claude Code and GitHub, and then he modified the YAML file. Because basically what it's doing is creating a YAML file—that's a GitHub Action configuration file—and then you can add additional details.

You can modify the prompt that it's running. I would highly recommend uncommenting the model it uses so that you can use Opus instead of Sonnet—the default. It's in there as a default; you just have to uncomment it.

With this, you can add additional parameters, for example, basically sneaking MCPs into your config file, and also give it permission to use different bash tooling and then give it access to other configuration files like markdown files.

All this to say: just through that GitHub integration, there's a lot you can really squeeze out of it to essentially create, as Anand was saying, a Devin-type experience, but with much more control and with better models.

What's also so cool about this is, as Anand was saying, you can embed any process that you have internally around amazing ways to go about code review. And based on the user that's submitting the PR, you can change things up as well. So you could really get these parts of your workflow embodied within these commands or these runners.

That's one thing I love about Claude Code and also MCPs: being able to encapsulate these different workflows that we have internally. Even just as one dev it's helpful, but across the team, incredibly helpful to embody that knowledge and that ability to be super productive and hand that off to more junior folks. They don't have to understand all the underlying details.

---

### The Next Level: Understanding and Using Agent Swarms

**Patrick:** So we have background agents. The GitHub integration being what I would consider part of that. And then, kind of connected but separately and a little bit more advanced, is agent swarms.

These are really cool. It's basically spinning off a bunch of containers. Codex is essentially this, where you can go from one to four. If you have four of them running at the same time, you've got all these agents running and then they're coming up with a solution, and then you can compare—either manually or through LLM-as-judge.

My friend Sam was walking me through this workflow. He's got three Opus instances that kick off, and then they've got acceptance criteria that they can look at for what good code looks like—different style guides, examples of API documentation and API spec standards. It'll compare outputs against that, and an LLM will choose which version of those three outputs it likes the best, and then it'll automatically merge it in. Build a CI/CD pipeline, and then he can review it at that point.

So you can get pretty sophisticated with the swarm idea. That's a more basic version. At the AI Engineer World's Fair that a few of us went to down in SF about a month ago, we saw examples of hundreds of these containers being kicked off. Now, of course, that would bankrupt me with Opus 4, but it's exciting to think about.

And then of course, non-engineering agents as well, such as Manus, Deep Research, and others we're familiar with.

My favorite: Claude Code, both in the CLI and in headless mode. They've got an SDK for TypeScript and Python, and then of course in the CLI as well. You've got this little intelligence that you can pipe things into in your terminal. You can put it in your build pipeline; you can have it review and build all kinds of different stuff that's right where you're at or within your application.

I think kind of thinking about Claude Code not as just a code gen tool, but as this agent that you can deploy in a bunch of different contexts, is really powerful.

I also love Gemini CLI—very similar to Claude Code. Doesn't have the magic, but for other tasks, one of the coolest ones I found was somebody using Gemini to basically watch a YouTube video. They can see one frame a second, and they have the transcript as well through Google's first-party integration with their YouTube tool.

I do this all the time. Even before I watch like an hour-long talk, I'll just summarize it. Google.com will basically get a sense of what it's talking about. Or, like for this talk, there was one detail I remembered from a Claude talk, but I didn't want to go through the entire hour to try to find it. I just quickly asked, "Hey, I remember this point. Roughly speaking, where is the timecode for this?" And it pulled it up. Super helpful.

And this is just one workflow with YouTube, but super helpful. Another cool one, though, is with the Gemini CLI: you can take a tutorial and then have it try to execute and build that locally on your computer if it's something that would be doable from a command line or using different tools exposed to it. Very versatile.

---

### The Golden Rule of AI Agents: Context is EVERYTHING

**Patrick:** Okay, so what agents need for great performance: context.

Context is everything. Context truly is everything. As you guys probably know, "prompt engineering" just got rebranded to "context engineering," given that what we fit into the model, what we give them... The analogy I pulled from—I believe it was the Anthropic CPO, who's also the Instagram founder—but the way he was talking about it is: imagine you're Claude Code. You wake up, you're in this box, and all you have is what some person just handed you, i.e., the prompt. It's gonna be extremely hard to do anything productive with that if you've got limited context and limited tooling.

---

### A Checklist of Essential Context to Give Your Agent

**Patrick:** So giving the context of the codebase, architectural style, what our preferred libraries are, different UI mocks and style guides—I mean, anything that can help it understand examples of good output and bad output, what it needs to do, along with evals or ways to evaluate the output.

So again, examples of good and bad. Linters are super helpful. I just have it run ESLint every time it's doing anything 'cause that just saves me a ton of time. You just want to keep that agent loop going as long as you can and give it as much feedback in real time as possible.

Any standards—around commits and branching, for example—acceptance criteria, automated tests, and then also tools. Different MCPs are the easiest way to expose these, but also the built-in web search, bash, and GitHub CLI. There are a lot of other tools you can give these models to perform much better.

There's a lot beyond engineering too that these agents are great at. Second Brain, which is basically like a methodology around personal knowledge management and note-taking, can be really helpful. Along with different computer administrative tasks, like naming screenshots based off content, what's in there, organizing files automatically. Of course, you know, the pipe operator. There's an MCP for Blender, which is really fun to create 3D models. I haven't used it myself, but I've seen some amazing demos.

Getting close to time, so I'll just really quickly go through the rest of the slides here. Different types of MCPs that can be really helpful—these are the main categories of functioning. These are some of the best registries of MCPs where you can find them.

**Audience Member:** There's behaviors with React that are terrible for users that end up happening when you kind of just throw a lot of code together. Fixing it is hard, and I figured there's some way to do it. If you have some MCP that's gonna load it and then kind of output the progress in some format that could be read by an LLM, but I don't know what that is yet. I don't have a good solution to this.

**Patrick:** One thought, though, is maybe having it input breakpoints to get it to pause at different UI states and then take a screenshot. That's maybe one interesting approach, just to throw out there. But great question.

Alright, I'm out of time unfortunately. I'll share these slides, though. There's a lot of stuff in here that I'm really passionate about, but I want to make sure we have time here.

---

## Part 3: The Ultimate Prompting Framework (Galen)

### The Core Framework: Explore, Plan, Execute

**Galen:** So big picture—I can't believe we didn't cover this yet—this is what you want to do every time you are using Claude Code on the command line.

How many of you actually use Claude Code? Have used it? You've all used it. Okay. So you know this. Hopefully I'll give you something a little more interesting.

**Explore, Plan, Execute.** If you jump straight to execute, I do this sometimes—I'm like, "This is gonna be so easy"—Claude is dumb and it will screw it up.

I actually find that Sonnet 4 with "think hard" is better than Opus for a lot of tasks, and it's faster. But your task complexity may be different than mine.

---

### The Right Prompt to Force Claude to Build Deep Context

**Galen:** So my goal here is to make Claude spend tokens to build up context.

It can read the markdown file. Mine's never up to date. Or it reads it and starts... Imagine you read 300 lines about how someone's codebase works, and they're like, "Now build this." You're gonna mess something up.

So: "Prepare to work on this." Claude starts with an idea of what it's gonna work on, and it's like, "Okay..." It's just like you. All of you. You're like, "Okay," you start reading, and then you're like, "Okay, I know how to build this," and you stop reading and you're like, "I'm ready to build."

If you're like, "Read the code," it will read a little bit more. But if you're like, **"Prepare to discuss how our frontend works,"** Claude will spend 50,000 tokens over seven minutes just being like, "Okay..."

And then it'll give you a nice overview of how it works. And when you do that, Claude is much smarter.

If the overview's wrong: Escape. Escape, or `/clear`, start over. Don't try to correct. You can try to correct it—I do it sometimes—but you're just basically chewing through tokens in your context window trying to push back on a bad contractor. Just fire the contractor, get a new one if it is wrong.

**Audience Member:** What else do you put in there to make it right the second time?

**Galen:** Just rerun it and see. Just rerun it. It's gonna reuse a bunch of subagents. It's gonna get it right; it's gonna be right nine out of ten times. This is a great gambling game, and when you lose, you're not like, "Oh, why did I lose?" You're like, "No, I win almost all the time."

I make markdown files. I have Claude write them. Like, "Talk about how our architecture works for..." and then make a checklist of what we're working on. This is an old one. "Obviously don't write any code." This is like, "Maybe if you have a PR, consider the next one, review read relevant..."

But I actually think this is a lot better: **"We're gonna work on the document identification part of the app. Dig in, read relevant files, prepare to discuss the ins and outs of how it works."** Sometimes I'll follow up with questions just to make sure it actually has the context.

---

### CRITICAL TECHNIQUE: Using Double Escape (Esc Esc) to Fork a Conversation

**Galen:** And often I will double escape to remove that from the context if I think it's doing a good job—just because I burn... I like a lot of room in the context window.

So, double escape. How many of you use double escape with Claude? Okay, you should use this all the time.

So I just spent seven minutes building up context. This contractor's really good at this. I can double escape and just fork the conversation. I can have it do a bunch of work, double escape, and go back to this same point where they have all this context. Saves me money and time. Mostly, I won't get kicked out of my Max plan as quickly.

Mostly just like... I don't have to sit there and wait and maybe get a bad gamble. **If you get a smart Claude, you should keep it and reuse it over and over and over.**

So this is what it looks like. You double escape, and you can just go back to any previous conversation. This is a crazy branching multiverse.

---

### How to Use /resume to Create Multiple High-Context Agents

**Galen:** So you can open up a new tab. You just built up a bunch of context, open up a new tab, hit `/resume`, and you get all that context in the new tab in terminal. So you can do like five terminals, all with all of that exact amazing frontend or backend or API context. You can ask a couple of questions and start there—wherever you want.

Just don't do this and then start having it write three different things on the frontend.

**Audience Member:** Do you prefer git worktrees or just different directories? How do you go about that?

**Galen:** I prefer to not work on more than two tasks at a time because my brain gets fried. I end up with 15 tabs open. I go back to a tab, I'm like, "Wait, what's that tab?" And I'm like, "Oh my God, I cannot make this decision right now. Why did I even start down this path?"

I just have two worktrees, which is just your entire Git library in a parallel case. And I will just merge them into master. I just keep them open. They're just sitting there, 'cause I don't care. I don't use Git appropriately.

So plan—I don't use plan mode. The three to five times I've tried it, it didn't do as good a plan as me asking it to do a plan. I like "think hardest." This is where you really have to think. Claude needs to think hard to plan.

So this is my generic instruction: "Write the function names in one to three sentences about what they do. Write the test names—five to ten words about the behavior they cover." But really, a short overview. Because Claude's default for plan is often like, "Here's a bunch of code that I'm gonna write," and you're like... No, I want you to think higher level than that. I want you to tell me conceptually what you're doing. 'Cause when you start doing code like that, you're starting to get into the weeds and you're not thinking architecturally.

This is a different example. I have actually built up this whole system for adding new PDF types. I have a whole system where I basically take a PDF and throw it at Gemini, but I have different types and different verifications I wanna run on them. I just have it read a couple of guides, and then I just let this run.

So there's no context on this. I can just put this into GitHub and then I go to Claude and I'm like, "Do GH issue 140. Close it when you're done." And then I just hit auto-accept. Goodbye.

**Risk-based planning:** If it's small, don't overthink—just write the code. Medium to large, you've gotta break it into testable, deployable PRs. I think of this in terms of context windows. That's about a PR-sized chunk of work for me. And then high risk: I think you should take two or three shots at the plan. You should really work over it with Claude. I'm not making the plan again—I'm just looking at its plan and I'm like, "This smells bad. This is terrible. If an engineer came to me—you are an engineer, you're coming to me with this—I'm like, this is really complicated. You're gonna screw it up. It's gonna mess up the codebase."

---

### THE "MY DEVELOPER" PROMPT TRICK for Getting Unbiased Feedback

**Galen:** So once I've done the plan, I open up a new tab, pull up that same amazing context, but don't dive into the plan. Don't get... Once it's made the plan, it's not gonna critique itself.

But if you go back to the amazing context and you're like, **"Yo, my developer came up with this plan to do this,"** Claude's like, "Yeah, all right. Let me tell you about this plan. I am with you. I'm on your team, not on your developer's team."

If you're like, "I came up with this plan," it'll tell you a lot of nice stuff. It'll be like, "Great job! You did a great plan. Here are a couple little things you might do differently."

But in this case, it's gonna be like, "Yeah, your developer, you know... I don't know. I wouldn't have done it that way."

Try to get specific. If you're just like, "They made this plan," it's not gonna do a good job. So ask the questions you would ask yourself.

Get feedback on the plan. You can have two Claudes make the plan. You can have a third Claude decide between them. I tend to put them into markdown and have Claude work on them, and then I have it break them up into PR-sized chunks, and then we execute.

Those PR-sized chunks: you might as well use that same context that you've already built up because it's so valuable to have those 50,000 tokens about your database—sorry, your app—in the context window. It's gonna write much better code than if you just bring up a blank Claude with 200 lines of the CLAUDE.md.

So pull up that 50,000-token context window, say "work on PR one." This is my example prompt: "Think hard. Write elegant code that completes this."

---

### Pro Tip: Force Claude to Avoid Backwards Compatibility for Cleaner Code

**Galen:** This is a real big one: **it loves backwards compatibility,** which I don't. I'm like, "No." And it's like, "We'll have graceful fallbacks." And I'm like, "No, that's just junk. That will break."

And then it will gracefully fall back. When you say that, that means to me that the app is going to silently fail and I will not know about it because it will just start leaning on some old code that you should be deleting.

You can tell where I get frustrated with Claude. This is a little overkill sometimes—the testing—but I think linting, compiling, and writing corresponding tests is good.

For really simple stuff, I actually just say, "Do TDD." And it writes the test, writes the failing test, writes the code that makes the test pass. It does a great job. TDD is terrible when I did code—I remember trying it for like a week and being like, "I fucking hate TDD. This is worse than writing tests." But Claude loves it.

I like "think hard" or "think" for this. I have Claude write lots of scripts to check its own work. Like, I gave it a script to call Gemini with PDFs—or I had it write that script—and now I'm like, "Test to make sure that when you verify, like you created a new markdown file that verifies PDFs, make sure it actually works and it verifies with this one."

Or if you need to view a PDF file, Claude's terrible at that. It can't do it. Ask Gemini or ask Uninstruct [possibly referring to Unstruct]. It will give you a markdown file. Go look at that. Then you can read it and understand what's going on and figure out what to do.

This is a big question: to watch or not to watch? Do you like... Because Claude will make, in my case, like one out of ten to twenty times, it's gonna start copying code and just doing some dumb stuff. And I'm not gonna look at the commit. I'm gonna watch it as it goes, pretty much, or I'm not gonna watch it at all. I'm gonna be like, "Committed. It works. It's good."

So I've seen 200 lines of copied code go through. I have a weird config that's in five different places in my app, and I'm just like, every time I'm like, "God, could we just put this config into one place?" And it's like, "Oh yeah, here's a plan." And I'm like, "All right, you're stupid. Okay, this is harder than it looks, I guess."

"Return True" was a 3.7 problem. You will not get that anymore.

But usually, if you just hit go... You kind of get a feel for it. I have a feel for it now where I'm like, "This is an easy enough thing for Claude just to do. Go." Shift+Tab puts it on auto-complete.

---

### Why Claude Prefers Writing New Code vs. Editing Existing Code

**Galen:** I don't know if you all have heard how this came to be—like, why we have amazing coding agents now—but it's because of RL [reinforcement learning]. And it's because once the models, once you move up the tech tree enough where models can write good compilable code, you can actually then start to give them coding problems and figure out if... 

Basically, the way that they did thinking was they were just like, "Write a bunch of stuff." And at the end, if you get the right answer, you get a cookie, and we're gonna reward that circuit. And if you don't, you don't get a cookie.

So we got to GPT-4 and Claude 3.5-level models, and you could start actually turning thinking on. But because the models were good enough to get all the way through... The problem is you're creating software engineering problems, and they're verifiable. Like, write this code. Does it compile? Does it answer the right question at the end? Very easy to test back.

But does that make for good edits? No. **That makes for really good writing fresh new code—new methods.** Claude prefers that. I don't know if you've all noticed that. But in my case, I'm like, "Write this. Edit the code, figure out where you can edit." Because you really have to prompt that, 'cause Claude is still really tuned into, "Okay, I'm gonna write some new code. This is gonna be fun. We're gonna do a new method, guys."

Claude 3.7 was over-RL'd on just completing tasks, and they dialed that back. That's where the "return True" [bug] came from. But we still have this problem where Claude is just trying to finish tasks and get its cookie by writing new code, not by editing or elegantly integrating code.

So then I go back to the developer thing, right? I lean on the developer. I go back to that planner. So I have my planner tab open, and I'm just like, **"Yo, my developer just finished step two. Give them low-level feedback and high-level feedback."** If you don't say that, it's like, "They did a great job."

So I get feedback, and then I go back to the developer and I'm like, "Hey, I got this feedback. What do you think?" And it's like, "Well, that's good feedback. Yeah, I'll do it."

And this is the problem with Claude—I don't know if you've hit `/review` on Claude's own code. It's like, "This code's great." Review doesn't... Claude likes Claude's code.

I use this sometimes. But at the end, as I'm running out of my context window or we're finishing up the pull request, I say to Claude: **"Tell... Give the next... You're not working on the next step of this. Give advice to the next developer. Put it in the markdown file."** And Claude is usually like, "You're off to an excellent start here, but..." It can be helpful.

---

### Context Window Management: Why You Must AVOID /compact

**Galen:** Context window management. I'm sure... Do you all get this? I never compact anymore. **Compact is a waste of time.** It generates like a page and a half and tells Claude to read four files, and you end up with a very off-kilter, dumb Claude.

---

### A Better Method: How to Use /rewind to Preserve High-Quality Context

**Galen:** So I just try to rewind. Once I get to 5% [remaining context], I'm like, "Document what you've done, and we're rewinding back to 40%, and I'm gonna be like, 'Here's what I've done so far. Continue.'"

**Audience Member:** Sorry, so you rewind instead of wiping? What do you mean?

**Galen:** Yeah. I hate compact. I hate clear. Yeah, starting with clear—I mean, you could use clear, but then you don't have any context. And so you can use `/resume` to get that context back, or double escape.

**Audience Member:** So why not use... I mean, it is more expensive 'cause you're already—you have all that...

**Galen:** I don't know that you're actually getting charged for... You only pay for new tokens, right? So you're not getting charged. It's much more expensive for them, but for us, it's just new tokens, so it's great.

---

### Other Tips and Tricks

**Galen:** So you jumped straight to execution. Go ahead.

**Audience Member:** One more.

**Galen:** Oh yeah, yeah. Other tips and tricks.

---

### Easy Mode: Getting Claude to Solve Git Merge Conflicts

**Galen:** That's the problem with worktrees—I'm like, "All right, we're gonna do this over here. We're gonna do this over here, and we're gonna merge 'em." And I'm like, "Oh, Jesus. Now we have a merge conflict."

I'm just like, **"Claude, deal with Git."** And it's like, "Okay." And it gets it right every time. I'm like, "Oh, should I trust it?" And I'm like, "Eh, I don't know." Every time it works.

I skip the ceremony for simple tasks—just do it.

Claude loves to be enterprise-ready. You have to fight that because it's built by an enterprise for enterprises. So this is one of my... if it gave me a plan that's too bulky, I love this [referring to a prompt]. It's just totally right, and it cuts it in half and makes it a much better plan for me.

**Explore. Plan. Execute. Resume. My Developer.**

And then Claude made up this joke at the end for me. I didn't add this, but I like it.

[Laughter]

That's a good one. All right, so that's my talk.

---

## Closing

**Patrick:** I hope you found our talks helpful, and if you did, I'm sure you would enjoy one of these two videos on how to become AI-native as a software engineer and a founder, specifically within code gen tools like Claude Code.

And with that, don't forget to subscribe for more content like this. Thank you.

---

## Summary of Major Corrections

- **Misheard words corrected:** "GhatGPT" → "ChatGPT," "CPS" → "MCPs," "philanthropic" → "Anthropic," "Devon" → "Devin," "SCK" → "SDK," "gr" → "grep"
- **Capitalization fixed:** "claude code" → "Claude Code," "Cloud MD" → "CLAUDE.md" (as a filename)
- **Technical terms clarified:** "Klein" → "Cline," proper model names (Opus 4, Sonnet 4, Claude 3.5, etc.)
- **Speaker labels added** for Patrick, Anand, and Galen throughout
- **Section headers added** matching the video's chapter structure
- **Filler words removed** (um, uh, like) while preserving natural speech patterns
- **Run-on sentences broken up** and punctuation corrected throughout
- **Audience questions** formatted distinctly from speaker responses