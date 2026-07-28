---
title: Troubleshooting Custom Skills | Beta
url: https://help.element451.com/en/articles/15232472-troubleshooting-custom-skills-beta
collection: Bolt AI
---

Learn how to diagnose why a Custom Skill did not fire, fired at the wrong time, or produced an unexpected response.

# Overview

[Custom Skills](https://help.element451.com/en/articles/14846841-custom-skills-for-bolt-agents-beta) give Bolt Agents more precise instructions, but they still need clear triggers, correct availability settings, active agent configuration, and well-structured actions. When a skill does not behave as expected, start by checking whether it was available, enabled, evaluated, and matched.

The fastest troubleshooting path is to reproduce the issue in **Test Agent** and inspect **Response Details.** Response Details shows which skills were evaluated, which skill matched, and which skills were skipped.

Below, we will cover:

* A quick troubleshooting checklist
* Why a skill did not fire
* Why the wrong skill fired
* Why the agent did not take the expected action
* How to troubleshoot inbound and outbound conversations
* When to escalate to your Element451 team

---

# Quick troubleshooting checklist

Use this checklist before editing the skill:

* Confirm the skill is saved
* Confirm the skill is enabled on the correct agent
* Open Conditions and confirm the correct channel is selected under Availability
* Confirm the schedule allows the skill to run at the test time
* Confirm the trigger clearly matches the user's message
* Confirm the skill is high enough in priority order
* Test in **Test Agent** using the same channel
* Open **Response Details** and review why the skill matched or was skipped

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423561309/2b75f348fcf9d4341ad04f5351bf/CleanShot+2026-05-25+at+15_54_24%402x.png?expires=1784333700&signature=84c3bdf499973f0fc8d78bab54c5f5c5be905c6df78208f5442922c55d8f0827&req=diQlFcx4nIJfUPMW1HO4zUqJGQO%2FwGGCz58IIqpM9uDKSISmgdBAICR9kH9f%0AMSjvQyKcQqBb86mfziI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423561309/2b75f348fcf9d4341ad04f5351bf/CleanShot+2026-05-25+at+15_54_24%402x.png?expires=1784333700&signature=84c3bdf499973f0fc8d78bab54c5f5c5be905c6df78208f5442922c55d8f0827&req=diQlFcx4nIJfUPMW1HO4zUqJGQO%2FwGGCz58IIqpM9uDKSISmgdBAICR9kH9f%0AMSjvQyKcQqBb86mfziI%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2469197077/ed39d33560448ec415eeb7485ee2/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=846a7424181eb6e2811e346ff4dbef265b956e029548790c12d6e8ada30e7d9c&req=diQhH8h3moFYXvMW1HO4zVfoLBlYeAmkz2njCS9c9tqrkBBu58cVb0V332bU%0ASElIH6XrbOXJc%2Fqpgl0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2469197077/ed39d33560448ec415eeb7485ee2/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=846a7424181eb6e2811e346ff4dbef265b956e029548790c12d6e8ada30e7d9c&req=diQhH8h3moFYXvMW1HO4zVfoLBlYeAmkz2njCS9c9tqrkBBu58cVb0V332bU%0ASElIH6XrbOXJc%2Fqpgl0%3D%0A)

---

# The skill did not fire

If a Custom Skill did not fire, check whether the skill was available and enabled before changing the trigger.

Common causes include:

|  |  |
| --- | --- |
| **Cause** | **What to check** |
| **Skill not enabled on the agent** | Open the agent's Skills page and confirm the Custom Skill toggle is on |
| **Channel not selected** | Open Conditions > Channels and confirm the conversation's channel is selected |
| **Schedule restricted** | Check Restrict by schedule and confirm the test time falls inside the window |
| **Trigger too narrow** | Compare the student's exact message to the trigger wording |
| **Higher-priority skill matched first** | Review Response Details and the active skill order on the agent |
| **Skill not saved** | Return to the skill editor and confirm changes were saved |

---

# The wrong skill fired

If the wrong skill fired, the issue is usually priority or overlapping triggers.

To fix it:

1. Open the agent's **Settings > Skills** page
2. Review the active Custom Skills
3. Identify which skills could match the same message
4. Move the more specific skill higher in the priority order
5. Narrow broad triggers so they do not capture unrelated messages
6. Retest in **Test Agent**

✨ **Pro Tip:** Write broad skills last. Start with the specific, high-value scenarios first, then add broader routing skills once the specific skills are working.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423572948/d2fd504b82bab0493437da05ccde/CleanShot-2B2026-05-13-2Bat-2B11_45_07-402x.png?expires=1784333700&signature=d7fe03b6053381e5412de37c4cf1afda7ef46327b1ef0fb5cdcb1e64f7fe573c&req=diQlFcx5n4hbUfMW1HO4zbR%2F8kyCeGJtfFZqpfkOvu31geuP6Pkyj6qT01qy%0Aipnicm9B4UrZBQHpSvQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423572948/d2fd504b82bab0493437da05ccde/CleanShot-2B2026-05-13-2Bat-2B11_45_07-402x.png?expires=1784333700&signature=d7fe03b6053381e5412de37c4cf1afda7ef46327b1ef0fb5cdcb1e64f7fe573c&req=diQlFcx5n4hbUfMW1HO4zbR%2F8kyCeGJtfFZqpfkOvu31geuP6Pkyj6qT01qy%0Aipnicm9B4UrZBQHpSvQ%3D%0A)

---

# The agent response was too generic

If the skill fired but the response was too generic, the action instructions may not be specific enough.

Improve the **Action** by adding:

* A clear goal
* Required qualifying questions
* Decision logic for common paths
* Tool chips for specific system actions
* Rules that tell the agent what not to do
* Escalation or task creation instructions when the agent cannot complete the request

For example, instead of writing "Help the student schedule a visit," tell the agent exactly how to identify the visit type, when to use Register for Event to send a registration link, when to use Schedule Appointment, and when to use Create Task.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423574123/2ec995ea52558fa6cd0cca8ec95e/CleanShot-2B2026-05-25-2Bat-2B15_27_15-402x.png?expires=1784333700&signature=1b032a571b294654f9290550a5ad4a0ab52d553731c45b58d74b986375dfbcd3&req=diQlFcx5mYBdWvMW1HO4zQY407deSgTk9k2HEyKSNORQ7UInOHVY0VjxwO4s%0ALYExcOWfGKOXQ70tADg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423574123/2ec995ea52558fa6cd0cca8ec95e/CleanShot-2B2026-05-25-2Bat-2B15_27_15-402x.png?expires=1784333700&signature=1b032a571b294654f9290550a5ad4a0ab52d553731c45b58d74b986375dfbcd3&req=diQlFcx5mYBdWvMW1HO4zQY407deSgTk9k2HEyKSNORQ7UInOHVY0VjxwO4s%0ALYExcOWfGKOXQ70tADg%3D%0A)

---

# The agent used the wrong tool or did not use a tool

If the agent did not take the expected action, check whether the tool is included in the Action instructions and configured correctly.

Review these areas:

* The tool chip appears in the **Action Description** or **Rules**
* The selected event, appointment type, label, task, or transfer destination is correct
* The action tells the agent when to use the tool
* The action tells the agent when not to use the tool
* The student clearly confirmed the required choice before the tool action

Important: Do not rely on vague wording when a specific system action is required. Use a configured tool chip whenever the agent should send an event registration link, schedule an appointment, create a task, add a label, or transfer a call.  
​

**Tool is not available for your institution:** Confirm the underlying Element451 product or capability is enabled. For example, `@Register for Event` requires Events, `@Schedule Appointment` requires Appointments, and `@Start Application` requires Applications. If a tool appears disabled or unavailable in the Action editor, hover over it or review the helper text to see which product capability is required.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423575320/e9da8a7ff34ce2eec6fc3f842731/CleanShot-2B2026-05-13-2Bat-2B11_58_00-402x.png?expires=1784333700&signature=38cd69b1b82114ff394750bc7fc8fec58a04044d3a213d40602838d038da099d&req=diQlFcx5mIJdWfMW1HO4zbvUj6LzQLnEYGwf0321VPqUyk9Ggra8qKFVUsnc%0AjS30UHl1ipNgCGfmjSs%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423575320/e9da8a7ff34ce2eec6fc3f842731/CleanShot-2B2026-05-13-2Bat-2B11_58_00-402x.png?expires=1784333700&signature=38cd69b1b82114ff394750bc7fc8fec58a04044d3a213d40602838d038da099d&req=diQlFcx5mIJdWfMW1HO4zbvUj6LzQLnEYGwf0321VPqUyk9Ggra8qKFVUsnc%0AjS30UHl1ipNgCGfmjSs%3D%0A)

---

# The skill works in one channel but not another

Custom Skills can behave differently across channels because each channel has different conversation patterns and response expectations.

If the skill works in one channel but not another:

1. Confirm the channel is selected in **Conditions > Channels**
2. Test the same intent in each enabled channel
3. Review Response Details for each channel
4. Update the trigger if students phrase the same intent differently on that channel
5. Add channel-specific rules if needed

For example, a voice caller may say "Can I talk to someone?" while a Messenger visitor may type "Can someone help me with financial aid?" Both may need the same routing outcome, but the trigger should account for the intent across channels.

---

# The skill behaves unexpectedly in an outbound Job conversation

For outbound [Jobs](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job), confirm that the Custom Skill is enabled on the same agent running the Job and that the skill is designed to match the recipient's reply.

Troubleshoot the path this way:

1. Identify the agent used by the Job
2. Open that agent's **Settings > Skills** page
3. Confirm the Custom Skill is active
4. Under Conditions > Availability, confirm the skill's Channels restriction matches the Job channel
5. Reproduce the student reply in **Test Agent**
6. Open **Response Details** to confirm whether the skill matched
7. If the skill does not match, revise the trigger around the reply intent

📌 **Note:** A Job starts the outreach. A Custom Skill handles the conversation when the recipient's reply matches the skill's trigger and the skill is available for that channel.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423577658/7bce2c3d3c3c093eb92f6fa19452/CleanShot-2B2026-05-25-2Bat-2B15_54_24-402x.png?expires=1784333700&signature=cb2d2899f0e2f184a8c508a5569ae2fb52b7c86c700d81bdb0fe03f634ac3a36&req=diQlFcx5modaUfMW1HO4zd4VRPYLoyHcn6a73CLsE1eGLzOGgd%2BBi8ZjSYoW%0APbr8btdDJrIFyFDR1p8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423577658/7bce2c3d3c3c093eb92f6fa19452/CleanShot-2B2026-05-25-2Bat-2B15_54_24-402x.png?expires=1784333700&signature=cb2d2899f0e2f184a8c508a5569ae2fb52b7c86c700d81bdb0fe03f634ac3a36&req=diQlFcx5modaUfMW1HO4zd4VRPYLoyHcn6a73CLsE1eGLzOGgd%2BBi8ZjSYoW%0APbr8btdDJrIFyFDR1p8%3D%0A)

---

# The skill should not have fired

If a Custom Skill fired when it should not have, the trigger is probably too broad or the skill priority is too high.

To fix it:

1. Read the exact student message
2. Compare it to the trigger
3. Add exclusions or more specific intent language
4. Move broader skills lower in priority
5. Add a rule telling the agent when not to proceed
6. Retest with both matching and non-matching examples

Bad trigger:

"Student asks about campus."

Better trigger:

"Prospective student or family member asks about visiting campus, taking a tour, attending an open house, joining an information session, or seeing campus before applying or enrolling."

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423578490/434e5b69f8a4cdaa87b72613fd64/image.png?expires=1784333700&signature=4cd3163c9e6987ad680dd9c1007c5d76c6aa6d7a03ff601bb15a7b5127300cdb&req=diQlFcx5lYVWWfMW1HO4zZgBQmhdAAFKwj3G8odV46tMQblBk9sVBLEjn1Hx%0AKpKtMtzvhsMFUXFjoIU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423578490/434e5b69f8a4cdaa87b72613fd64/image.png?expires=1784333700&signature=4cd3163c9e6987ad680dd9c1007c5d76c6aa6d7a03ff601bb15a7b5127300cdb&req=diQlFcx5lYVWWfMW1HO4zZgBQmhdAAFKwj3G8odV46tMQblBk9sVBLEjn1Hx%0AKpKtMtzvhsMFUXFjoIU%3D%0A)

---

# Escalate when the issue looks like a product bug

Escalate the issue to your Element451 team when configuration appears correct but the skill still does not behave as expected.

Include this information when escalating:

* Agent name
* Custom Skill name
* Channel
* Approximate date and time of the conversation
* Student message that should have triggered the skill
* Expected behavior
* Actual behavior
* Screenshot of Response Details
* Whether the issue occurred in live conversation, Test Agent, or a Job conversation

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468721596/f26b51cb8259677bf231e69eecbb/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=ca9b089c1ab18a439cff0ebb07f2dbab539bb7de7f14fc0aa868108aa2e3c260&req=diQhHs58nIRWX%2FMW1HO4zQB1aCFHE%2FZX0PCWI6K1AkcLZ%2FMLsn7TctdEQzvv%0AhG3gwb9h22XRvorsaTg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468721596/f26b51cb8259677bf231e69eecbb/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=ca9b089c1ab18a439cff0ebb07f2dbab539bb7de7f14fc0aa868108aa2e3c260&req=diQhHs58nIRWX%2FMW1HO4zQB1aCFHE%2FZX0PCWI6K1AkcLZ%2FMLsn7TctdEQzvv%0AhG3gwb9h22XRvorsaTg%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468721748/fce3fceadaa2742d44060d1aa019/CleanShot%2B2026-06-10%2Bat%2B14_44_30-402x.png?expires=1784333700&signature=37a1e4c388f7f5990d28798fed280f739e18d9dbe1c776ac4a6afa3e34a31b9d&req=diQhHs58nIZbUfMW1HO4zS6iAU9U0%2Bu0nbM1tnGudgTGVQ1%2FNThS3ouP42GQ%0Amw5iVwcK7OeLcOUqz%2BY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468721748/fce3fceadaa2742d44060d1aa019/CleanShot%2B2026-06-10%2Bat%2B14_44_30-402x.png?expires=1784333700&signature=37a1e4c388f7f5990d28798fed280f739e18d9dbe1c776ac4a6afa3e34a31b9d&req=diQhHs58nIZbUfMW1HO4zS6iAU9U0%2Bu0nbM1tnGudgTGVQ1%2FNThS3ouP42GQ%0Amw5iVwcK7OeLcOUqz%2BY%3D%0A)

---

# Troubleshooting examples

## Example 1: Skill skipped because of channel

A campus visit skill is configured for Messenger and Email, but the student replies by SMS. The skill is skipped because SMS is not selected in **Channels**.

Fix: Add SMS to the skill's channel availability, then test again.

## Example 2: General skill matched before specific skill

A general admissions support skill appears above Financial Aid Inquiry Handler. A student asks about FAFSA, but the general skill matches first.

Fix: Move Financial Aid Inquiry Handler above the general skill.

## Example 3: Agent invented availability

A student asks for a campus tour on a date that is not configured. The agent gives a date instead of creating a task.

Fix: Add a rule that says the agent must never invent availability and must use **Create Task** for unavailable dates or special requests.

---