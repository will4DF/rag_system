---
title: Custom Skills for Bolt Agents | Beta
url: https://help.element451.com/en/articles/14846841-custom-skills-for-bolt-agents-beta
collection: Bolt AI
---

Custom Skills let you teach Bolt Agents how to handle institution-specific scenarios. Define when a skill should fire, what the agent should do, and which deterministic tools it can use — across Messenger, SMS, Email, and Voice.

# Overview

Bolt Agents come with a set of [system skills](https://help.element451.com/en/articles/8993380-bolt-agent-skills) — Inquiry Flow, Schedule Appointments, Start an Application, and so on — that work the same way for every institution. **Custom Skills** let you go further: build your own skills that teach an agent how to handle the scenarios that are specific to your school.

A Custom Skill is two things together:

* A **condition** — when this skill should fire, including hard channel and time-of-day restrictions plus a natural-language description of the trigger.
* An action — what the agent should do when the skill fires, written in plain language with optional @-mentions for configured tools, such as transferring a call, sending an event registration link, or handing the conversation to another Bolt Agent.

Skills apply to **all inbound conversations** — direct messages on Messenger, SMS, Email, or Voice, replies inside a Bolt Agent Job, and conversations handed off from another agent.

### When to use a Custom Skill

Reach for a Custom Skill when:

* A scenario doesn't map to a system skill (mental-health questions, athletic recruiting, transfer credit evaluation, a specific scholarship program).
* You need a configured action — for example, "always transfer the call to this number during business hours" or "always send the registration link for this event." Until @Share Entity is available, document sharing relies on natural-language instructions rather than a configured entity action.
* You want different behavior on different channels or different times of day.
* You need the agent to follow a specific script (especially common over Voice).
* You want one general agent to route conversations into specialized agents based on what the student is asking about.

---

# Anatomy of a Custom Skill

Every Custom Skill has the same shape. Here's what each piece does.

## 1. Name & Description

A short, descriptive name (e.g. *Financial Aid Inquiry Handler*, *After-Hours Voice Routing*) and an optional description explaining what the skill is for. Both are internal — students never see them.

## 2. Availability (channels & schedule)

In the Conditions tab, the Availability section contains the channel and schedule restrictions. These hard gates run before the agent evaluates the trigger. If a conversation does not match them, the skill is skipped.

* **Channels**: Pick which of **Messenger**, **SMS**, **Email**, **Voice**, and **WhatsApp** the skill should fire on. Default is all channels.
* **Schedule**: Optionally restrict the skill to specific times of day in a chosen timezone. Choose *Business hours only*, *After hours only*, or define a custom schedule.

Use availability when you need predictability — for example, a "transfer to admissions counselor" skill that's only available 9–5 Eastern, with a separate "after-hours" skill that texts a callback link instead.

## 3. Trigger

A natural-language description of *when* the skill applies. The agent uses this to decide whether the skill matches the current conversation.

Good triggers describe the student's intent or situation in plain English:

* *"Student asks about financial aid, scholarships, or FAFSA."*
* *"Caller wants to schedule or learn about a campus tour."*
* *"Student mentions mental health, counseling, or feeling overwhelmed."*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381401420/a90b1e422220e0f4818589e53492/image.png?expires=1784333700&signature=206efa9fd5b2225a3f7c84bca86ce146ae88158882180c6341a9a4f1cf2998b8&req=diMvF81%2BnIVdWfMW1HO4za1OZEMQzlI86Rr5LSOG5GJf9RbJCB2m88JfIQsw%0AHfAwju9nJFqXCHcMWs8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381401420/a90b1e422220e0f4818589e53492/image.png?expires=1784333700&signature=206efa9fd5b2225a3f7c84bca86ce146ae88158882180c6341a9a4f1cf2998b8&req=diMvF81%2BnIVdWfMW1HO4za1OZEMQzlI86Rr5LSOG5GJf9RbJCB2m88JfIQsw%0AHfAwju9nJFqXCHcMWs8%3D%0A)

## 4. Action

The instructions the agent follows when the skill fires. Written in plain language, with optional `@`-mentions for deterministic tools.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381419079/1fd57cf7356f328954a83c49f05a/image.png?expires=1784333700&signature=81180d021bb65207453f9a3b0841675c6ef6521a65f3e140383e3c4ac30c8ef4&req=diMvF81%2FlIFYUPMW1HO4zYMI5JYwfjZQ6NJdrxlADLBRcnCnsdOEu%2Bc%2FfioV%0ArhFiBU7SbWeWkQh%2FW9E%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381419079/1fd57cf7356f328954a83c49f05a/image.png?expires=1784333700&signature=81180d021bb65207453f9a3b0841675c6ef6521a65f3e140383e3c4ac30c8ef4&req=diMvF81%2FlIFYUPMW1HO4zYMI5JYwfjZQ6NJdrxlADLBRcnCnsdOEu%2Bc%2FfioV%0ArhFiBU7SbWeWkQh%2FW9E%3D%0A)

Actions can mix natural-language guidance with structured logic:

Ask the caller which program they are interested in. If they mention nursing, offer to send the registration link using @Register for Event: Nursing Open House. If they want to talk to an advisor, use @Transfer Call for the admissions line*.*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381417336/1cb6e994f2de16f593aa0c81c733/CleanShot+2026-05-13+at+11_58_00%402x.png?expires=1784333700&signature=007a4728a14109508608cf619e80287d8b7b410cf67a8d560664964077d8370a&req=diMvF81%2FmoJcX%2FMW1HO4zSmiRBT7kLHizETf9KilSXk01aRdAPqYZXSj2vrF%0A58XNVMUCaEIdZFX1mgs%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381417336/1cb6e994f2de16f593aa0c81c733/CleanShot+2026-05-13+at+11_58_00%402x.png?expires=1784333700&signature=007a4728a14109508608cf619e80287d8b7b410cf67a8d560664964077d8370a&req=diMvF81%2FmoJcX%2FMW1HO4zSmiRBT7kLHizETf9KilSXk01aRdAPqYZXSj2vrF%0A58XNVMUCaEIdZFX1mgs%3D%0A)

---

# @-mentions: deterministic tools inside a skill

Typing @ in the Action field opens an autocomplete of tool actions the agent can take.  
​  
Each available tool opens a configuration sheet where you select its target, such as an event, Bolt Agent, or phone number. The resulting chip defines the configured action the agent can run when the action's authentication, permissions, confirmation, and product prerequisites are satisfied.

## Why some tools may not appear

The tools available in the `@` menu depend on the Element451 products and capabilities enabled for your institution.

For example, if Events is not enabled for your institution, `@Register for Event` will not be available. If Appointments is not enabled, `@Schedule Appointment` will not be available.

If a tool is available but you cannot see a specific event, appointment type, workflow, label, application, or other record inside the tool configuration sheet, that is usually related to your user permissions. Product access controls whether the tool is available. User permissions control which items you can view or select inside that tool.

If you expected a tool to be available but do not see it, contact your Element451 team or your institution's Element451 administrator.

## Feature required by tool

|  |  |
| --- | --- |
| Tool | Feature required |
| `@Transfer Call` | Voice, Conversations, or handoff capabilities, depending on channel |
| `@Register for Event` | Events |
| `@Create Task` | Tasks |
| `@Create Alert` | Cases / Alerts |
| `@Add Label` | Labels / People |
| `@Start Application` | Applications |
| `@Schedule Appointment` | Appointments |
| `@Enroll in Workflow` | Workflows |
| `@Enroll in Rule` | Rules / Workflows, depending on implementation |
| `@Hand Off to Agent` | Bolt Agents |

For `@Share Entity`, availability can depend on what kind of entity is being shared. For example, your institution may have Forms enabled but not Surveys, or Pages enabled but not Documents.

|  |  |  |
| --- | --- | --- |
| **Tool** | **What it does** | **You configure** |
| **@Transfer Call** | On Voice: transfers the call to a specific number. On chat/SMS: routes the conversation to the staff queue, like a standard human handoff. | One phone number per Transfer Call chip. If the number is blank, the transfer uses the line's default handoff number. For multiple destinations, create a separate focused Custom Skill for each destination. |
| **@Register for Event** | Currently, the tool will send a student a link to register for the event. In the future, the tool may have the ability to take an action and register the student for a specific event you've chosen. | The event |
| **@Create Task** | Creates a staff follow-up task linked to the student and conversation, with the agent's summary attached | Task type/template, assignee (team or individual), priority, and due date |
| **@Create Alert** | Create a Case Management alert linked to the contact for a reviewer to triage | The alert |
| **@Add Label** | Applies a label to the student's contact record — useful for segmentation and downstream automation | The label |
| **@Start Application** | Sends the student a link to start a specific admission application | The application |
| **@Schedule Appointment** | Books a specific appointment type for the student through a conversational flow | The appointment type |
| **@Enroll in Workflow** | Enrolls the student into a selected Element451 workflow based on the skill logic | The workflow |
| **@Hand Off to Agent** | Routes the conversation to a different specialized agent in your instance with conversation context | The target agent |

## More tools coming after beta

A few additional tools are on the roadmap and will appear in the `@`-mention menu as they ship:

* **@Hand Off to Person** routes the conversation to a specific person or team, or to a dynamic destination like the student's Contact Owner
* **@Share Entity** sends a specific shareable resource to the student (documents, knowledge items, and similar), adapting delivery to the channel

## Authentication during Custom Skill actions

Some Custom Skill actions require a known contact, such as creating a record-linked task, booking an appointment, or continuing a sensitive process. If a visitor is anonymous, the agent can prompt them to authenticate with the existing email-code flow before continuing. After authentication succeeds, the conversation continues with the authenticated contact context. If authentication is not completed, the agent should not perform the record-linked action.

---

# Enabling skills on an agent

Custom Skills are managed in three places:

* **Instance level** — Skills can be created and available across the whole instance under **Engagement > Bolt Agents > Custom Skills**

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472713885/b50b770b12a2fc0adabcc79b7b02/CleanShot+2026-06-12+at+08_49_33%402x.png?expires=1784333700&signature=29ca1cb055c1f0912feb3b92eaf256dd838127254bbb358ddf4a171fd1f29f77&req=diQgFM5%2FnolXXPMW1HO4zTHGue3XRSsJCe%2Bzu%2FcMnj6oz3cj9LM6PWbyyxPW%0Anom7%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472713885/b50b770b12a2fc0adabcc79b7b02/CleanShot+2026-06-12+at+08_49_33%402x.png?expires=1784333700&signature=29ca1cb055c1f0912feb3b92eaf256dd838127254bbb358ddf4a171fd1f29f77&req=diQgFM5%2FnolXXPMW1HO4zTHGue3XRSsJCe%2Bzu%2FcMnj6oz3cj9LM6PWbyyxPW%0Anom7%0A)
* **Agent level** — Each agent has a list of skills you can enable or disable. The same skill can be on for one agent and off for another.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472718866/4afdb7bff134bb402fa3e1e9bd88/image.png?expires=1784333700&signature=7833e73bd3eb8e62aab8897a2e3121c4b1cac11fe66340d0df3c064c5c6aca62&req=diQgFM5%2FlYlZX%2FMW1HO4zZVEuw5Ht%2FSu6HY7voKDcSea23FLzb52PtmB4cFV%0AfL4B%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472718866/4afdb7bff134bb402fa3e1e9bd88/image.png?expires=1784333700&signature=7833e73bd3eb8e62aab8897a2e3121c4b1cac11fe66340d0df3c064c5c6aca62&req=diQgFM5%2FlYlZX%2FMW1HO4zZVEuw5Ht%2FSu6HY7voKDcSea23FLzb52PtmB4cFV%0AfL4B%0A)

  You are able to edit the custom skill here by clicking on the ellipsis more options menu

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472718414/0000f0098de90f23504181cdc3b0/CleanShot%2B2026-06-12%2Bat%2B08_47_40-402x.png?expires=1784333700&signature=fcb1636260e69223967fd3e4b7c924ec4967b7c595de774636d4dd05825f6783&req=diQgFM5%2FlYVeXfMW1HO4zS46vz0ig3Q8kHn0yYOVEsyKeiqqHlePSgXAXZNR%0A8ITm%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472718414/0000f0098de90f23504181cdc3b0/CleanShot%2B2026-06-12%2Bat%2B08_47_40-402x.png?expires=1784333700&signature=fcb1636260e69223967fd3e4b7c924ec4967b7c595de774636d4dd05825f6783&req=diQgFM5%2FlYVeXfMW1HO4zS46vz0ig3Q8kHn0yYOVEsyKeiqqHlePSgXAXZNR%0A8ITm%0A)
* **Agent Test Console -** Use the top row skills menu on an active or inactive Custom Skill to open the same editor without leaving the agent or testing flow.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472724439/12de606fb4557a00ff56d4b7398b/CleanShot+2026-06-12+at+08_54_04%402x.png?expires=1784333700&signature=18031118f89c4545a06e4d64e428b8d3671cad3cca007f0bf0fbf8e413d271ff&req=diQgFM58mYVcUPMW1HO4zYKI2r%2BuvJZ9ZgJIVaXdppPiMMC%2BY8nBGHGYsIjR%0Aau23%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472724439/12de606fb4557a00ff56d4b7398b/CleanShot+2026-06-12+at+08_54_04%402x.png?expires=1784333700&signature=18031118f89c4545a06e4d64e428b8d3671cad3cca007f0bf0fbf8e413d271ff&req=diQgFM58mYVcUPMW1HO4zYKI2r%2BuvJZ9ZgJIVaXdppPiMMC%2BY8nBGHGYsIjR%0Aau23%0A)

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472706845/5a42f4a65777bfa422a9d3a07ebc/CleanShot+2026-06-12+at+08_45_28%402x.png?expires=1784333700&signature=b1c1dc9a173bbab6c25fcf522cddaa71173cd6fb745e59e0a74292f90d5c845e&req=diQgFM5%2Bm4lbXPMW1HO4zSSY3D28e2sjNXI7IAZeJDTGN1Y7noL0islYR7gJ%0A7wYZ%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472706845/5a42f4a65777bfa422a9d3a07ebc/CleanShot+2026-06-12+at+08_45_28%402x.png?expires=1784333700&signature=b1c1dc9a173bbab6c25fcf522cddaa71173cd6fb745e59e0a74292f90d5c845e&req=diQgFM5%2Bm4lbXPMW1HO4zSSY3D28e2sjNXI7IAZeJDTGN1Y7noL0islYR7gJ%0A7wYZ%0A)

## Skill priority

When more than one skill could match an inbound message, priority decides which one wins. On the agent configuration page, drag enabled skills to reorder them — the skill higher in the list takes precedence over a lower one. Priority is per-agent, so the same skill can rank differently on different agents.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381374694/e6223afcaae01d72dfa9a6709c18/CleanShot+2026-05-13+at+11_45_07%402x.png?expires=1784333700&signature=b553e971054e0400e2e8c154e8d914320bded404fba9ce3433ce2aacdc3ded4b&req=diMvF8p5mYdWXfMW1HO4zRGUT8Y510Q02dcXyHmpcQ4qnOTRhvD2Qle1eJw%2B%0A73JkOCUBNAAcyC4RGuQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2381374694/e6223afcaae01d72dfa9a6709c18/CleanShot+2026-05-13+at+11_45_07%402x.png?expires=1784333700&signature=b553e971054e0400e2e8c154e8d914320bded404fba9ce3433ce2aacdc3ded4b&req=diMvF8p5mYdWXfMW1HO4zRGUT8Y510Q02dcXyHmpcQ4qnOTRhvD2Qle1eJw%2B%0A73JkOCUBNAAcyC4RGuQ%3D%0A)

A good rule of thumb: **more specific triggers go higher**. A "Mental Health Support" skill should sit above a generic "Student Support Questions" skill so the more specific one is chosen first.

---

# Testing your skill: the Agent Test Console

Every agent configuration page now has a **Test Agent** button that opens an embedded test console. Use it to simulate conversations across any channel, see exactly which skills fire, and iterate on your trigger and action text without touching live data.

## What the test console does

* **Channel simulation** — Pick Messenger, SMS, Email, or Voice. For Voice, you can test real-time audio behavior for inbound call simulations and outbound phone simulations. Outbound voice tests ask for a call goal before the simulated interaction begins. No real calls are placed during testing.
* **Full configuration** — The simulation uses every skill you have enabled, in priority order, with all your `@`-mention tools wired up. Channel and schedule controls are respected.
* **Response Details** — Every agent response has a collapsible panel showing which skills were evaluated, which one matched and why, which were skipped (wrong channel, outside schedule, condition didn't fit), and what tool actions *would* have executed.
* **No side effects** — No real contact records are created. No real transfers, registrations, or texts go out. Tool actions show up in the trace as *"would execute: @Transfer Call to 555-1234"* rather than actually executing.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468622261/358a8d7b39bcad61ebd858b7e6c6/CleanShot+2026-06-10+at+14_42_01%402x.png?expires=1784333700&signature=7fd03bd30292b81a28b57043eb51fdbd94cad7b6d48d5469479cb75bf7507eb7&req=diQhHs98n4NZWPMW1HO4zetHCu8ACgZexuwkCsxD4nEkl%2BCjqrbRzXpxsaVh%0AJ50Y1ND7TtY6kw5EttI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468622261/358a8d7b39bcad61ebd858b7e6c6/CleanShot+2026-06-10+at+14_42_01%402x.png?expires=1784333700&signature=7fd03bd30292b81a28b57043eb51fdbd94cad7b6d48d5469479cb75bf7507eb7&req=diQhHs98n4NZWPMW1HO4zetHCu8ACgZexuwkCsxD4nEkl%2BCjqrbRzXpxsaVh%0AJ50Y1ND7TtY6kw5EttI%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468625929/9b04a84d59f99aa8872c0ab248d3/CleanShot+2026-06-10+at+14_44_30%402x.png?expires=1784333700&signature=942e82882eb36a32f2fb1f5beec5131105a8db6ca9b3f79686892f2ab4f8fb04&req=diQhHs98mIhdUPMW1HO4zfhdlwqbCH6yWZj2RTctrbc6ooSUiVGBIfM91sr7%0AOtnCPbGuKfDwxbU7TWg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468625929/9b04a84d59f99aa8872c0ab248d3/CleanShot+2026-06-10+at+14_44_30%402x.png?expires=1784333700&signature=942e82882eb36a32f2fb1f5beec5131105a8db6ca9b3f79686892f2ab4f8fb04&req=diQhHs98mIhdUPMW1HO4zfhdlwqbCH6yWZj2RTctrbc6ooSUiVGBIfM91sr7%0AOtnCPbGuKfDwxbU7TWg%3D%0A)

## A typical testing workflow

1. Save your skill and enable it on the agent.
2. Click **Test Agent** on the agent config page.
3. Pick the channel you want to test (start with the most-used one).
4. Send a message that should trigger the skill. Confirm in the response detail that your skill matched.
5. Send a message that should *not* trigger it. Confirm the skill is correctly skipped.
6. Repeat across each channel the skill is enabled on.

## Monitoring live Custom Skill conversations

After a Custom Skill is live, use the Conversations filter found in **Engagement > Conversations > All conversations: Advanced Filtering** to spot-check real conversations where a specific Custom Skill triggered. Select the Custom Skill in the filter to review matching conversations and confirm the skill is behaving as expected.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472752823/7395bb04a52dfd70f0902bb453c9/CleanShot+2026-06-12+at+09_06_52%402x.png?expires=1784333700&signature=6ae39db8525d1e3b6d4ffc03e6b5dee4cfa9cb7b657a00c59376c8809392195d&req=diQgFM57n4ldWvMW1HO4zbOI0h0rzOyVf%2BU5QZsa93otdWeI3mCMh58JlmhF%0A497AUQclmm7w%2FzyyCRQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2472752823/7395bb04a52dfd70f0902bb453c9/CleanShot+2026-06-12+at+09_06_52%402x.png?expires=1784333700&signature=6ae39db8525d1e3b6d4ffc03e6b5dee4cfa9cb7b657a00c59376c8809392195d&req=diQgFM57n4ldWvMW1HO4zbOI0h0rzOyVf%2BU5QZsa93otdWeI3mCMh58JlmhF%0A497AUQclmm7w%2FzyyCRQ%3D%0A)

---

# Worked examples

A few patterns to model your own skills on. These are simplified — your actual skills will be longer and more specific to your institution.

## Example 1 — Financial Aid Inquiry Handler

**Goal:** When a student asks about financial aid, hand them tailored information and a way to get a person involved if they need one.

**Availability:** All channels. No schedule restriction.

**Trigger:**

*Student asks about financial aid, scholarships, FAFSA, payment plans, tuition cost, or how to afford school.*

**Action:**

*Ask the student which aspect of financial aid they need help with.*

* *If they mention FAFSA, explain that FAFSA is the first step for most need-based aid.*
* *If they mention scholarships, explain that scholarship options can depend on student type, program, academic profile, and deadlines. Ask whether they are a first-year, transfer, graduate, or continuing student.*
* *If they ask about tuition, cost, payment plans, or affordability, explain that final cost depends on program, residency, enrollment status, and aid eligibility.* *Ask whether they want help estimating cost, understanding payment options, or connecting with financial aid.  
  If the student wants to talk to a counselor or asks for a person, use `@Transfer Call`*
* *If their question is unclear or they're stuck, `@Create Task` for the Financial Aid team with a summary of the conversation.*
* *After clear financial aid intent, use @Add Label: Financial Aid Interested.*

## Example 2 — Campus Visit Scheduler

Goal: Help students who want to visit campus reach the correct event registration page.

**Availability:** All channels. No schedule restriction.

**Trigger:**

*Prospective student asks about visiting campus, taking a tour, an open house, or attending an info session.*

**Action:**

Tell the student about our upcoming Open House — date, time, and what is included. If they are interested, use @Register for Event: Spring Open House 2026 to send the registration link. After sending the link, add the @Add Label: Visit Interested label so the recruitment team can follow up. Do not state that registration is complete.

## Example 3 — Voice Call Routing (business hours vs. after hours)

Goal: Route inbound Admissions calls to the Admissions line during business hours and offer a callback or text-based help after hours. This pattern uses two skills working together.

### Skill A — Business Hours Voice Routing

**Availability:** Voice only. *Business hours only* (9 AM–5 PM, your timezone).

**Trigger:**

Caller explicitly asks to speak with Admissions or an admissions counselor.

**Action:**

Confirm that the caller wants Admissions, then use @Transfer Call: 555-100-2000. Create a separate Financial Aid Custom Skill with its own trigger, priority, and Transfer Call number.

### Skill B — After-Hours Voice Routing

**Availability:** Voice only. *After hours only*.

**Trigger:**

Caller explicitly asks to speak with Admissions or an admissions counselor.

**Action:**

*Apologize that our counselors are unavailable, and let the caller know we'll text them resources and a callback link. `@Create Task` for the Admissions team to call them back tomorrow morning.*

Because the two skills have non-overlapping schedules, only one ever fires for a given call.

---

# Best practices

* **One job per skill.** If a skill is doing two things, split it. Smaller skills are easier to reason about, troubleshoot, and reorder.
* **Use availability for the things you can't get wrong.** If something *must* only happen on Voice, set the channel restriction. Don't rely on the trigger description to enforce it.
* **Specific triggers go higher in priority.** A "Mental Health Support" skill should sit above a generic "Student Questions" skill so the specific one wins.
* **Use `@`-mentions whenever the action involves a specific entity.** Don't write "send them to a person" generically. Use `@Transfer Call` when a transfer or handoff should happen.
* **Test each channel separately.** Skills can behave differently on Voice vs. SMS vs. Messenger; the test console is fastest.
* Start small. One agent, two or three skills, watch how they behave on real conversations, expand from there. Your institution's Custom Skills catalog will grow naturally.

---

# Beta limitations and what's coming next

Custom Skills are launching in beta. A few capabilities are intentionally not in the first release:

* **@Share Entity** isn't available yet. Until it ships, share documents and resources through natural-language instructions in the action text
* **@Hand Off to Person** isn't available yet. For voice transfers, use **@Transfer Call.** For chat and SMS handoffs, the standard human handoff still works
* Prebuilt skill templates and a shared template library are not in the beta. Each institution creates and manages its own Custom Skills in its instance-level catalog.
* **Per-agent customization of an instance-level skill** (overriding the action text on one agent only) isn't in the beta. Skills are shared across agents, with priority ordering as the per-agent control

If your team has a use case that depends on one of these, let your CSM know — beta feedback drives the post-beta roadmap.

---

# Related articles

* [Bolt Agent Skills](https://help.element451.com/en/articles/8993380-bolt-agent-skills) — the system skills your agents already have.
* [Bolt Agent Handoffs](https://help.element451.com/en/articles/8993398-bolt-agent-handoffs) — how human handoffs work in conversations.
* [Bolt Agent Settings](https://help.element451.com/en/articles/8993375-bolt-agent-settings) — agent-level configuration.
* [Bolt Agent Teams](https://help.element451.com/en/articles/12068259-bolt-agent-teams) — group agents for inbound routing.
* [Playbook: Handling Inbound Communications](https://help.element451.com/en/articles/11993001-playbook-handling-inbound-communications-email-sms-live-chat) — channel-by-channel guidance.
* [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job) — for proactive (outbound) agent work.

---