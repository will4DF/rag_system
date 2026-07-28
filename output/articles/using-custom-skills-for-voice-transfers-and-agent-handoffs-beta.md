---
title: Using Custom Skills for Voice Transfers and Agent Handoffs | Beta
url: https://help.element451.com/en/articles/15935383-using-custom-skills-for-voice-transfers-and-agent-handoffs-beta
collection: Bolt AI
---

Learn how to transfer phone callers to specific numbers, route conversations to specialized Bolt Agents, and configure reliable handoff paths.

# Overview

Custom Skills let you control when a handoff should happen and which configured action the Bolt Agent should take. You can transfer an active phone call to a live number, send a conversation to another specialized Bolt Agent, or use the standard human handoff workflow for staff follow-up.

The correct setup depends on the destination. A **Transfer Call** action connects a phone caller to a number. A **Hand Off to Agent** action moves the conversation to another AI agent and preserves its context. For an introduction to Custom Skill conditions, actions, and tool chips, review [Custom Skills for Bolt Agents | Beta](https://help.element451.com/en/articles/14846841-custom-skills-for-bolt-agents-beta).

Below, we will cover:

* How to choose the correct handoff option
* How to configure a Voice transfer
* How to route callers to multiple departments or named people
* How to configure a handoff to another Bolt Agent
* How to test live routing safely
* How to troubleshoot common handoff problems

---

# Choose the right handoff option

Start with the destination that should take over. The three options below solve different problems.

|  |  |  |  |
| --- | --- | --- | --- |
| **Option** | **Destination** | **Best use** | **What happens** |
| **@Transfer Call** | Human phone number or staff queue | A phone caller needs Admissions, Financial Aid, an operator, or a staff direct line | The active phone call transfers to the configured number |
| **@Hand Off to Agent** | Another Bolt Agent | A specialized AI agent has the right knowledge or actions | The target Bolt Agent continues the conversation with its context |
| ***Human Team Member Handoff***  *(**Native skill, not a custom skill)*** | Human inbox user or team through Conversation Rules | A staff member should take over a digital conversation or receive a general fallback | The Bolt Agent disconnects and the matching handoff rule assigns the conversation |

🚨 **Important:** In **@Hand Off to Agent**, “Agent” means another Bolt Agent, not an employee, counselor, or other human team member.

📌 **Note:** Adding a configured **@Transfer Call** chip to a Custom Skill provides the explicit transfer action. You do not need to enable the native phone-transfer or Human Team Member Handoff skill solely for that Custom Skill.

## When to use @Transfer Call

Use **@Transfer Call** when the destination will answer a telephone number.

Common use cases include:

* Transfer a caller to Admissions
* Transfer a caller to Financial Aid
* Transfer a caller to a named employee's approved direct number
* Transfer a caller to an operator or reception line
* Send calls to a staffed hunt group during business hours

Each Transfer Call chip has one configured phone number. While a skill can contain multiple chips, separate focused custom skills are easier to trigger, prioritize, test, and maintain. We recommend you create one custom skill per call that needs to be transferred and do not put multiple call transfer options in one custom skill.

On non-phone channels, Transfer Call uses the standard staff handoff behavior instead of dialing the number. Configure a Conversation Rule with an assignment action so the handed-off conversation reaches the intended staff user or team.

## When to use @Hand Off to Agent

Use **@Hand Off to Agent** when another Bolt Agent should continue helping the student.

Common use cases include:

* A general service agent sends financial aid questions to a Financial Aid Agent
* An admissions agent sends international student questions to an International Admissions Agent
* An intake agent sends application troubleshooting to an Application Support Agent

The target remains an AI agent. Use this option when specialized knowledge or tools are needed, not when the student asks to speak with a person.

A configured @Hand Off to Agent action can target a Bolt Agent outside the source agent's team, and it can be used by the default agent. The same-team and default-agent restrictions described for automatic team handoffs do not apply to this explicit Custom Skill action.

## When to use the standard human handoff

Use the native **Human Team Member Handoff** skill and Conversation Rules when a staff member should take over a digital conversation or when you need a broad human fallback.

Conversation Rules can assign a handed-off conversation to a specific internal user, a staff team, or another operational process based on the handoff intent.

**Explore More >** [Bolt Agent Handoffs](https://help.element451.com/en/articles/8993398-bolt-agent-handoffs)

---

# Configure a Voice transfer

Create a focused Voice Custom Skill for each destination you want callers to reach.

1. Navigate to **Engagement > Bolt Agents > Custom Skills**.
2. Click **Add Custom Skill**.
3. Enter a specific **Skill Name**, such as *Transfer to Admissions*.
4. Open **Conditions**. Under **Channels**, select **Voice**. Add a schedule when the number should only receive calls during certain hours.
5. Write a narrow **Trigger** describing when the caller wants that destination.
6. Open **Actions**. Add a clear **Goal** and explain what the agent should confirm before transferring.
7. In **Action Description**, type **@** and select **Transfer Call**.
8. Configure the destination **Phone number**, an optional **Transition phrase**, and **Pacing**:

   * **Natural:** Wait for the transition phrase to finish before transferring.
   * **Immediate:** Start the transfer as soon as the action runs.
9. Add any required **Rules**, save the skill, and enable it on the correct agent.
10. Place the skill in the correct priority order on the agent's **Skills** page.

[![Custom Skill Action editor showing available tool chips](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2542539914/a022d830b5a2135250419b40adc3/image.png?expires=1784333700&signature=6222203f06ff6cb2ae6cac68e4fb351f8de95100420e88d03de2096aa03a5024&req=diUjFMx9lIheXfMW1HO4ze6L7ozrpEvVJw4hS8ax3mDR0KuYAR7it76nYJWY%0AN9272mezeHTGnyJsc%2BU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2542539914/a022d830b5a2135250419b40adc3/image.png?expires=1784333700&signature=6222203f06ff6cb2ae6cac68e4fb351f8de95100420e88d03de2096aa03a5024&req=diUjFMx9lIheXfMW1HO4ze6L7ozrpEvVJw4hS8ax3mDR0KuYAR7it76nYJWY%0AN9272mezeHTGnyJsc%2BU%3D%0A)

🚨 **Important:** Enter the transfer number in the **@Transfer Call** chip. Writing a phone number only in the Action text does not configure the transfer destination.

📌 **Note:** Use a complete number with country code, such as `+12025550101`. If the chip's number is blank, the call uses that phone line's default handoff number.

✨ **Pro Tip:** Prefer a direct department number over a general switchboard. Confirm that its forwarding, no-answer, and after-hours routes never return to the Bolt Agent's inbound number.

## Inbound calls versus outbound Bolt Agent Jobs

The number in a Custom Skill's Transfer Call chip controls the destination for matching inbound conversations.

For an outbound Bolt Agent Job, configure the Job's **Phone Number for Call Transfer**. Do not rely on an inbound Custom Skill destination to configure an outbound Job.

---

# Route callers to multiple destinations

For several departments or people, create a separate Voice custom skill for each destination. Give every skill its own trigger, Transfer Call number, channel and schedule, and priority.

Prioritize the custom skills from most specific to most general:

1. **Named person or narrowly defined route**
2. **Department route**
3. **Operator or reception fallback**

For example:

1. *Transfer to Jane Smith — Admissions Director*
2. *Transfer to Financial Aid*
3. *Transfer to Admissions*
4. *Transfer to Operator*

[![Bolt Agent Skills page showing Custom Skill priority order](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2542539915/1f458ad4ecb1bdfe45de0007a933/CleanShot%2B2026-05-13%2Bat%2B11_45_07-402x.png?expires=1784333700&signature=c14aadc0719a0100f8b2190e07057d69fc51e37266da195e6bb0166abff2eba9&req=diUjFMx9lIheXPMW1HO4zYfYll1VkvpDZgksKIs5dPjIAe59BT9hA9s7AGMh%0AYJgTB62SOGRu6tY%2BokQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2542539915/1f458ad4ecb1bdfe45de0007a933/CleanShot%2B2026-05-13%2Bat%2B11_45_07-402x.png?expires=1784333700&signature=c14aadc0719a0100f8b2190e07057d69fc51e37266da195e6bb0166abff2eba9&req=diUjFMx9lIheXPMW1HO4zYfYll1VkvpDZgksKIs5dPjIAe59BT9hA9s7AGMh%0AYJgTB62SOGRu6tY%2BokQ%3D%0A)

💡 **Use Case:** A caller who says “I need Jane Smith in Admissions” may match both a named-person route and a general Admissions route. Put Jane's specific skill above Admissions so the intended destination wins.

🧠 **Good to Know:** Transfer Call uses the phone number configured in the chip. It does not dynamically look up a Contact Assignee, My Network relationship, department record, or arbitrary staff member.

## Example — Transfer to Admissions

**Name**

*Transfer to Admissions*

**Availability**

* **Channel:** Voice
* **Schedule:** Business hours

**Trigger**

Caller explicitly asks to speak with Admissions, an admissions counselor, or a person about applying, admission requirements, or application status. Do not activate when the caller asks for a named employee covered by a more specific skill.

**Action**

Confirm that the caller wants Admissions. Tell the caller you will connect them, then use **@Transfer Call** configured with the Admissions direct line. If the caller only wants the agent to answer a general question, continue helping them.

**Example destination**

`+12025550101`

## Example — Transfer to Financial Aid

**Name**

*Transfer to Financial Aid*

**Availability**

* **Channel:** Voice
* **Schedule:** Business hours

**Trigger**

Caller explicitly asks to speak with Financial Aid, a financial aid counselor, or a person about FAFSA, aid eligibility, an award, scholarships, tuition assistance, or payment options.

**Action**

Confirm that the caller wants Financial Aid. Tell the caller you will connect them, then use **@Transfer Call** configured with the Financial Aid direct line. Do not transfer when the caller wants the agent to answer a general question and has not requested a person.

**Example destination**

`+12025550102`

## Example — Transfer to a named person

**Name**

*Transfer to Jane Smith — Admissions Director*

**Availability**

* **Channel:** Voice
* **Schedule:** The employee's receiving hours

**Trigger**

Caller explicitly asks for Jane Smith or asks to speak with the Admissions Director by name or title. Do not activate for a general request for Admissions or any available admissions counselor.

**Action**

Confirm that the caller wants Jane Smith. Tell the caller you will connect them, then use **@Transfer Call** configured with Jane Smith's approved direct number.

**Example destination**

`+12025550103`

Update the skill if the employee or destination number changes.

## Example — Transfer to an operator

**Name**

*Transfer to Operator*

**Availability**

* **Channel:** Voice
* **Schedule:** Hours when the operator line is staffed

**Trigger**

Caller explicitly asks for the operator, reception, or switchboard, or cannot identify the correct office after one clarifying question. Do not activate when a named-person or department-specific transfer skill applies.

**Action**

Ask one clarifying question to determine whether Admissions, Financial Aid, or another configured destination applies. If the caller still wants the operator, confirm the transfer and use **@Transfer Call** configured with the operator's direct receiving number.

**Example destination**

`+12025550100`

🚨 **Important:** Keep an operator route last. A broad fallback placed above specific skills can capture calls intended for a department or named person.

## Example — Business-hours transfer and after-hours follow-up

Create two skills with the same topic but non-overlapping schedules.

**Skill A: Admissions Transfer — Business Hours**

* **Channel:** Voice
* **Schedule:** Business hours
* **Action:** Confirm the request, then use **@Transfer Call** for the Admissions line

**Skill B: Admissions Follow-Up — After Hours**

* **Channel:** Voice
* **Schedule:** After hours
* **Action:** Explain that Admissions is closed and create a staff follow-up task when that action is available and the caller can be identified

Because the schedules do not overlap, only the appropriate skill is available at the time of the call.

💡 **Use Case:** Transfer Admissions calls to a staffed hunt group from 8:00 a.m. to 5:00 p.m. After 5:00 p.m., explain the office hours and create a callback task instead of sending the caller to an unattended line.

---

# Configure a handoff to another Bolt Agent

Use **@Hand Off to Agent** when the target is a specialized Bolt Agent rather than a person answering a telephone.

1. Navigate to **Engagement > Bolt Agents > Custom Skills** and create a new skill.
2. Enter a specific **Skill Name**, such as *Hand Off to Financial Aid Agent*.
3. Under **Conditions**, select the channels and schedule where the handoff should apply.
4. Write a narrow **Trigger** describing when the specialized agent is needed.
5. Under **Actions**, explain how the current agent should introduce the handoff.
6. Type **@**, select **Hand Off to Agent**, and choose the required **Target Agent**.
7. Configure an optional **Transition phrase** and **Pacing**.
8. Save the skill, enable it on the originating agent, and set its priority.

Important for Voice: The source and target agents must use the same speech provider. They may use different voices, but cross-provider Voice handoffs are not supported. Text channels are unaffected.

🧠 **Good to Know:** Conversation context moves with the handoff, the target Bolt Agent becomes active, and its enabled skills become available.

✨ **Pro Tip:** Keep a Voice agent handoff path clear and one-way. Avoid skills that immediately send the conversation back to the source agent or create repeated back-and-forth routing.

## Example — Hand off to a Financial Aid Bolt Agent

**Name**

*Hand Off to Financial Aid Agent*

**Trigger**

Student asks a detailed financial aid question about FAFSA, aid eligibility, scholarships, an award notice, or a financial aid process that belongs with the Financial Aid Bolt Agent.

**Action**

Tell the student you are connecting them with the Financial Aid Agent, then use **@Hand Off to Agent** configured for the Financial Aid Agent. Do not ask the student to repeat information already provided.

**Target Agent**

*Financial Aid Agent*

Configure the target with the appropriate Knowledge, enabled skills, and an internal description that clearly explains what it owns.

Review [Bolt Agent Teams](https://help.element451.com/en/articles/12068259-bolt-agent-teams) when agents are organized by area of expertise.

---

# Test before enabling live routing

Use **Test Agent** to validate skill matching and priority before placing a live call.

1. Save and enable each Custom Skill on the agent.
2. Click **Test Agent**.
3. Select **Voice** for phone-transfer skills.
4. Test a phrase that should match each skill.
5. Test a similar phrase that should not match.
6. Open **Response Details** and confirm that the correct skill matched, broader skills were skipped or ranked lower, and the expected tool would run.

[![Custom Skills Test Agent console showing Response Details](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2542539913/e0fbd0c480a77daf2b0c4a1572c8/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=d432d45ec55f367b3b0c80e49ed7634daca36b09412b9b8c5d11bfb21b64e8cd&req=diUjFMx9lIheWvMW1HO4zcgkSpbePGr57BkHsWyQN8RaVoMstOeUHj9WIP8G%0AMoUahZH%2BSKSV2U%2F0U%2FM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2542539913/e0fbd0c480a77daf2b0c4a1572c8/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=d432d45ec55f367b3b0c80e49ed7634daca36b09412b9b8c5d11bfb21b64e8cd&req=diUjFMx9lIheWvMW1HO4zcgkSpbePGr57BkHsWyQN8RaVoMstOeUHj9WIP8G%0AMoUahZH%2BSKSV2U%2F0U%2FM%3D%0A)

📌 **Note:** Test Agent simulates tool execution and does not place a real transfer. Complete at least one live inbound call test for every phone number before launch.

For a live Voice transfer, verify:

* The intended phone or queue rings
* The caller hears the expected transition
* No-answer and after-hours routing behave correctly
* The destination does not return the call to the Bolt Agent
* The correct destination wins when similar skills exist

For an agent-to-agent handoff, verify:

* The correct Bolt Agent takes over
* The target agent receives the conversation context
* The student is not asked to repeat information
* The original agent does not continue responding after the handoff
* For Voice, both agents use the same speech provider

---

# Troubleshoot handoffs

## The wrong Voice transfer skill matched

1. Compare the caller's exact wording with each skill's **Trigger**.
2. Add exclusions to broad triggers.
3. Move named-person and specialized routes above department and operator routes.
4. Test the overlapping phrase again in **Test Agent**.
5. Review **Response Details** to confirm why each skill matched or was skipped.

## The transfer skill did not run

Confirm that:

* The skill is saved and enabled on the correct Bolt Agent
* **Voice** is selected under **Conditions**
* The current time falls within the skill's schedule
* The trigger describes the caller's actual intent
* The **@Transfer Call** chip is present and configured
* A higher-priority skill is not winning first

Use the checklist in [Troubleshooting Custom Skills | Beta](https://help.element451.com/en/articles/15232472-troubleshooting-custom-skills-beta) before changing several settings at once.

## The call went to the default number or switchboard

Open the **@Transfer Call** chip and confirm that the intended destination number is explicitly configured.

If the number is blank, the transfer uses the Element451 line's default handoff number. This can send several skills to the same switchboard instead of their department-specific destinations.

1. Enter the correct direct number in the chip.
2. Save the skill.
3. Retest the skill match in **Test Agent**.
4. Place a real inbound call and confirm the direct destination rings.

## The call is stuck in a transfer loop

A loop usually means the destination, switchboard, hunt group, or no-answer route forwards the call back to the Bolt Agent's inbound number.

Ask your phone administrator to check:

* Call forwarding on the destination
* Hunt-group overflow routes
* No-answer and after-hours routes
* IVR options that return to the original line
* A switchboard route that points back to the Bolt Agent

Use a direct department number or dedicated receiving queue that does not return to the source line.

🚨 **Important:** Editing the Custom Skill trigger will not correct a loop created by an external phone system.

## The conversation went to the wrong Bolt Agent

Confirm that:

* The correct target is selected in **@Hand Off to Agent**
* The target Bolt Agent is enabled and has the right Knowledge and skills
* The target agent's internal description clearly explains its responsibility
* The originating trigger is narrower than general routing skills
* The handoff does not immediately route back to the source agent

## A Voice agent handoff is unavailable

Confirm that the source and target agents use the same speech provider. Supported pairings are OpenAI to OpenAI and Deepgram to Deepgram. The exact voices may differ.

If the speech providers differ, align them or use a different handoff path. This compatibility requirement does not affect Messenger, SMS, Email, or other text channels.

For additional Voice configuration guidance, review [Playbook: Handle Inbound Phone Calls](https://help.element451.com/en/articles/12053969-playbook-handle-inbound-phone-calls).

---