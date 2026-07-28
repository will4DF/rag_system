---
title: Custom Skills Best Practices | Beta
url: https://help.element451.com/en/articles/15232436-custom-skills-best-practices-beta
collection: Bolt AI
---

Learn how to write, organize, test, and maintain Custom Skills so Bolt Agents respond predictably across channels.

# Overview

Custom Skills let you teach [Bolt Agents](https://help.element451.com/en/articles/14846841-custom-skills-for-bolt-agents-beta) how to handle institution-specific scenarios that do not fit neatly into a built-in system skill. A well-written Custom Skill gives the agent a clear trigger, a focused goal, and specific instructions for what to do next.

The best Custom Skills are narrow, testable, and easy to troubleshoot. Instead of trying to solve many scenarios in one large skill, build smaller skills that each handle one job and use priority ordering to control which skill runs first.

Below, we will cover:

* How to structure a strong Custom Skill
* How to write clear triggers and actions
* How to use availability and priority controls
* How to test and improve skills before publishing
* Common patterns to follow when building your first skills

---

# Start with one clear job per skill

Each Custom Skill should handle one specific student intent or operational scenario. If a skill tries to do too many things, it becomes harder to test, harder to prioritize, and harder to understand when something does not work as expected.

Good Custom Skill examples include:

* Campus Visit Scheduler
* Financial Aid Inquiry Handler
* After-Hours Voice Routing
* Mental Health Support Routing

Avoid using one broad skill for many unrelated scenarios, such as admissions questions, campus visits, scholarships, and counselor routing all in the same action.

✨ **Pro Tip:** If the skill name needs the word "and" to explain what it does, consider splitting it into two skills.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423470133/64f41eac68200a3bd9261aea3510/image.png?expires=1784333700&signature=7d7584d9f3f44f73babdeac4b740a0469d49732f93a318102f76c5edbe9b3d1f&req=diQlFc15nYBcWvMW1HO4zbll6AzBpQ%2FaRaNEqlbPIUYKc4X4C%2B88hPCD%2FREV%0Aygn9uhKzuGr7HsABqFM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423470133/64f41eac68200a3bd9261aea3510/image.png?expires=1784333700&signature=7d7584d9f3f44f73babdeac4b740a0469d49732f93a318102f76c5edbe9b3d1f&req=diQlFc15nYBcWvMW1HO4zbll6AzBpQ%2FaRaNEqlbPIUYKc4X4C%2B88hPCD%2FREV%0Aygn9uhKzuGr7HsABqFM%3D%0A)

---

# Write the trigger around student intent

The **Trigger** tells the agent when the skill should activate. Write the trigger in plain language based on what the student or family member is asking for, not based on internal team terminology.

Strong triggers describe the user's intent clearly:

* "Prospective student or family member asks about visiting campus, taking a tour, attending an open house, joining an information session, or seeing the campus before applying or enrolling"
* "Student asks about scholarships, FAFSA, tuition, financial aid, or how to pay for school"
* "Caller asks to speak with a person, admissions counselor, financial aid counselor, or live team member"

Weak triggers are vague or too broad:

* "Student has a question"
* "Admissions help"
* "Campus information"

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423471410/e03af7e56a6922d5339d765926ba/image.png?expires=1784333700&signature=d0d130345ee044073dd9e8a97b5e495834b12c0b6ed7f9354cbfed9c92140a71&req=diQlFc15nIVeWfMW1HO4zTbCZkrmpPFcxeT%2F7rpDfRSLDY9yhbV98t9JV%2F%2Fc%0ABEv0fln9v7DsSSx%2FG5o%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423471410/e03af7e56a6922d5339d765926ba/image.png?expires=1784333700&signature=d0d130345ee044073dd9e8a97b5e495834b12c0b6ed7f9354cbfed9c92140a71&req=diQlFc15nIVeWfMW1HO4zTbCZkrmpPFcxeT%2F7rpDfRSLDY9yhbV98t9JV%2F%2Fc%0ABEv0fln9v7DsSSx%2FG5o%3D%0A)

---

# Use availability for hard rules

In the Conditions tab, use the Availability section when a channel or schedule restriction must be enforced before the agent evaluates the trigger. The skill is skipped when the conversation does not match those restrictions.

Use **Channels** when the skill should only run on specific communication channels, such as Messenger, SMS, Email, Voice, or WhatsApp.

Use **Restrict by schedule** when the behavior should change by time of day, such as routing calls to a live team during business hours and creating a callback task after hours.

🚨 **Important:** Do not rely on the trigger text to enforce strict channel or schedule rules. If a skill should only run on Voice, select Voice in **Channels** and deselect the other channels.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423492724/72a144db9d531c6934d08d6843ff/CleanShot+2026-05-25+at+15_23_22%402x.png?expires=1784333700&signature=7269ae42563f851d556eb1d56ede7f4bca224ca4e6731f47b664b89a640534cc&req=diQlFc13n4ZdXfMW1HO4zTERo0tc3EAhZXTdjwsD62fkYgemNS%2BGgBAyWRZa%0AKC7bGgTMu5YDTfVPhxQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423492724/72a144db9d531c6934d08d6843ff/CleanShot+2026-05-25+at+15_23_22%402x.png?expires=1784333700&signature=7269ae42563f851d556eb1d56ede7f4bca224ca4e6731f47b664b89a640534cc&req=diQlFc13n4ZdXfMW1HO4zTERo0tc3EAhZXTdjwsD62fkYgemNS%2BGgBAyWRZa%0AKC7bGgTMu5YDTfVPhxQ%3D%0A)

---

# Write actions as step-by-step instructions

The **Action** tells the agent what to do after the skill fires. Use clear instructions that describe the goal, the decision path, and the exact action the agent should take.

A strong action includes:

* A clear goal
* A short sequence of steps
* Rules for deciding which path to take
* Instructions for what not to do
* Deterministic tools where needed

For example, a campus visit skill can tell the agent to:

* Ask whether the student wants a campus tour, open house, virtual information session, or another visit option
* Use Register for Event to send the registration link for a configured visit event
* Use **Schedule Appointment** when the student wants a one-on-one visit or counselor meeting
* Use **Create Task** when the student asks for a special request, accessibility accommodation, group visit, or unavailable date
* Use **Add Label** after the student shows clear visit interest or completes a registration

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423497015/98a0a3237a7c473e367a363b3db9/CleanShot+2026-05-25+at+15_27_15%402x.png?expires=1784333700&signature=b8c426abb66f3d99780662c493d900bddea4fb03d81a01917d93aa282a6fc2e3&req=diQlFc13moFeXPMW1HO4zfdJQSgSvononbFghxzS%2BhWp2Kt6gucmkgp0iJMA%0AXZ30l7M1mmQfxHz5%2BDM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423497015/98a0a3237a7c473e367a363b3db9/CleanShot+2026-05-25+at+15_27_15%402x.png?expires=1784333700&signature=b8c426abb66f3d99780662c493d900bddea4fb03d81a01917d93aa282a6fc2e3&req=diQlFc13moFeXPMW1HO4zfdJQSgSvononbFghxzS%2BhWp2Kt6gucmkgp0iJMA%0AXZ30l7M1mmQfxHz5%2BDM%3D%0A)

---

# Use tools for deterministic actions

When the agent needs to take a specific action, use the tool chips available in the Action editor. Tool chips give the agent an exact configured action instead of leaving it to infer what should happen.

Common tool patterns:

|  |  |
| --- | --- |
| **Tool Chip** | **Use When** |
| **Register for Event** | The student wants the registration link for a configured event such as an open house, info session, or webinar |
| **Schedule Appointment** | The student wants a one-on-one meeting with a counselor, advisor, or staff member |
| **Create Task** | The request requires staff review, a special accommodation, or an unavailable option |
| **Add Label** | The conversation should trigger downstream segmentation, reporting, or workflow automation |
| **Transfer Call** | A Voice caller needs to reach a specific team or live person |

🧠 **Good to Know:** Natural-language instructions tell the agent how to reason through the scenario. Tool chips tell the agent exactly what system action to take.  
​

The tools you see in the Action editor depend on the Element451 products and capabilities enabled for your institution. If a tool is not available, use an available tool, adjust the skill instructions, or contact your Element451 team to discuss access.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423498851/d1f6727309f53becbfa18dec638e/CleanShot%2B2026-05-13%2Bat%2B11_58_00-402x.png?expires=1784333700&signature=63fe02ab072365d571a31bc5268b4861b2f5c6da488e0f87cd7f5b4c60cfc6c3&req=diQlFc13lYlaWPMW1HO4zZk4%2F%2FEH1Y9xJ%2FxJv73qxvgZ1bIcXK6DXoEtFGr2%0A4vttxsDuWDGnhwIbQRI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423498851/d1f6727309f53becbfa18dec638e/CleanShot%2B2026-05-13%2Bat%2B11_58_00-402x.png?expires=1784333700&signature=63fe02ab072365d571a31bc5268b4861b2f5c6da488e0f87cd7f5b4c60cfc6c3&req=diQlFc13lYlaWPMW1HO4zZk4%2F%2FEH1Y9xJ%2FxJv73qxvgZ1bIcXK6DXoEtFGr2%0A4vttxsDuWDGnhwIbQRI%3D%0A)

---

# Put specific skills above general skills

When multiple skills could match a conversation, priority determines which active skill should run first. On the agent's **Skills** page, active Custom Skills can be reordered by dragging them into priority order.

A good priority strategy is:

* Place high-risk or highly specific skills first
* Place common intent-specific skills next
* Place broad routing or general support skills lower

For example, place Financial Aid Inquiry Handler above a generic admissions support skill so financial aid questions are handled by the more specific instructions.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423501410/0d2a3574b3f4c675f51aaa9deea4/CleanShot%2B2026-05-13%2Bat%2B11_45_07-402x.png?expires=1784333700&signature=7a3d4fd1341e854a39023fb377c3a4f51a9fd4de5434a581d945a71bae8372e8&req=diQlFcx%2BnIVeWfMW1HO4zQsfnNyeXnAX3YTd2MweUqcNKj5P3NxIZa6I8iFB%0ANXwPbRbGvZL33g3eIRk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423501410/0d2a3574b3f4c675f51aaa9deea4/CleanShot%2B2026-05-13%2Bat%2B11_45_07-402x.png?expires=1784333700&signature=7a3d4fd1341e854a39023fb377c3a4f51a9fd4de5434a581d945a71bae8372e8&req=diQlFcx%2BnIVeWfMW1HO4zQsfnNyeXnAX3YTd2MweUqcNKj5P3NxIZa6I8iFB%0ANXwPbRbGvZL33g3eIRk%3D%0A)

---

# Test every skill before publishing changes

Use **Test Agent** before publishing changes to a live agent. The test console lets you simulate different channels and inspect the **Response Details** without creating real contact records or executing real actions.

A basic testing workflow is:

1. Save the Custom Skill
2. Enable the Custom Skill on the agent
3. Click **Test Agent**
4. Select a simulated channel, such as Messenger, SMS, Email, or Voice. For Voice, choose the appropriate voice test path. Use inbound testing to simulate a caller reaching the agent, or outbound testing to simulate an agent-initiated phone conversation with a defined call goal
5. Send a message that should trigger the skill
6. Open **Response Details** and confirm the correct skill matched
7. Send a message that should not trigger the skill
8. Confirm the skill is skipped for the right reason
9. Repeat on each enabled channel

📌 **Note:** The test console simulates behavior for the selected channel. For Voice, use real-time audio testing to validate how the skill behaves in simulated inbound and outbound phone conversations. Test actions remain safe simulations and do not place real calls.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468717596/7bf9331b698c915b59389e0ff414/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=f772b187db75cd7e416de84f8790141cc9904381c5a93974568dee757df9d01e&req=diQhHs5%2FmoRWX%2FMW1HO4zS16ckgXHtNDr3kPXPexKRFKh%2Bjk0NUt%2BsYG4ydo%0AFuchLjPRkplCu9jcedQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468717596/7bf9331b698c915b59389e0ff414/CleanShot%2B2026-06-10%2Bat%2B14_42_01-402x.png?expires=1784333700&signature=f772b187db75cd7e416de84f8790141cc9904381c5a93974568dee757df9d01e&req=diQhHs5%2FmoRWX%2FMW1HO4zS16ckgXHtNDr3kPXPexKRFKh%2Bjk0NUt%2BsYG4ydo%0AFuchLjPRkplCu9jcedQ%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468717838/677adbabd354c8d16d465e56fd36/CleanShot%2B2026-06-10%2Bat%2B14_44_30-402x.png?expires=1784333700&signature=80ba23c89b78ba5a7737307288e95b680081d9cc86eb33ab9827c446fdf9dbcc&req=diQhHs5%2FmolcUfMW1HO4zXmklRK0TAEC5d9ykbiW83SjuBqYYobiIwHfJWpK%0A8WEjfPga769cLFNi3BQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2468717838/677adbabd354c8d16d465e56fd36/CleanShot%2B2026-06-10%2Bat%2B14_44_30-402x.png?expires=1784333700&signature=80ba23c89b78ba5a7737307288e95b680081d9cc86eb33ab9827c446fdf9dbcc&req=diQhHs5%2FmolcUfMW1HO4zXmklRK0TAEC5d9ykbiW83SjuBqYYobiIwHfJWpK%0A8WEjfPga769cLFNi3BQ%3D%0A)

---

# Keep rules explicit

Rules help keep the agent from taking the wrong action. Add rules when there are known boundaries the agent should follow.

Useful rule patterns include:

* Always identify the student's specific need before taking action
* Always use a configured tool when the student asks for that action
* Never invent dates, times, availability, requirements, deadlines, or staff commitments
* Never send an event registration link or schedule a student until they clearly confirm the option they want
* Create a task when the request requires staff review

💡 **Use Case:** A campus visit skill can tell the agent to never invent event availability. If a student asks for a date that is not available, the agent creates a staff task instead of promising a visit time that has not been configured.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423508347/b1c732ef089888631498685ff52e/CleanShot+2026-05-25+at+15_31_15%402x.png?expires=1784333700&signature=efa66cbaa323e4e79a1210ea40f9b0a731492c01f6b6ad4d36e7a5bca840861b&req=diQlFcx%2BlYJbXvMW1HO4zcKif29R2k%2FipJb4IlnqMAFxn9Kf%2F55X0tAq8qME%0A%2FU3cxQAS2BhhnhzDgK0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423508347/b1c732ef089888631498685ff52e/CleanShot+2026-05-25+at+15_31_15%402x.png?expires=1784333700&signature=efa66cbaa323e4e79a1210ea40f9b0a731492c01f6b6ad4d36e7a5bca840861b&req=diQlFcx%2BlYJbXvMW1HO4zcKif29R2k%2FipJb4IlnqMAFxn9Kf%2F55X0tAq8qME%0A%2FU3cxQAS2BhhnhzDgK0%3D%0A)

---

# Maintain skills as your processes change

Custom Skills should be reviewed whenever your team changes a process, event, phone number, appointment type, routing rule, or campaign strategy.

Review Custom Skills when:

* A new event or appointment type is created
* A phone number or team routing path changes
* Staff notice repeated incorrect responses
* A skill is skipped unexpectedly in **Response Details**
* A workflow changes downstream of an **Add Label** action
* A beta limitation changes or a new tool becomes available

---