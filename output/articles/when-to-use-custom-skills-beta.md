---
title: When to Use Custom Skills | Beta
url: https://help.element451.com/en/articles/15232459-when-to-use-custom-skills-beta
collection: Bolt AI
---

Learn when a Custom Skill is the right tool for Bolt Agent behavior, and when to use another configuration option instead.

# Overview

[Custom Skills](https://help.element451.com/en/articles/14846841-custom-skills-for-bolt-agents-beta) are best for institution-specific scenarios where a Bolt Agent needs to recognize a particular type of conversation and follow a defined response path. They give teams more control than general agent instructions because each skill has its own trigger, availability settings, action instructions, and optional tools.

Use a Custom Skill when the behavior should be repeatable and tied to a specific student intent. Do not use Custom Skills as a catch-all replacement for Knowledge, system skills, agent settings, or workflows.

Below, we will cover:

* When Custom Skills are the right fit
* When to use Knowledge instead
* When to use system skills instead
* When to use Jobs or workflows instead
* Common Custom Skill examples

---

# Use Custom Skills for institution-specific scenarios

Use a Custom Skill when your team has a scenario that is specific to your institution and needs a defined response pattern.

Common examples include:

* Routing students who ask about a specific program
* Handling campus visit questions
* Supporting scholarship or financial aid questions
* Responding to athletic recruiting interest
* Routing callers during business hours or after hours
* Collecting information before creating a staff follow-up task
* Adding a label when a student expresses a specific intent

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423515987/a8b2cdf433bc12d9e8d1385eabf0/CleanShot+2026-05-25+at+15_34_35%402x.png?expires=1784333700&signature=bc869cc19d0f90bfccddca51713befaa8f4a6da47025a42dc540f04649d2abd4&req=diQlFcx%2FmIhXXvMW1HO4zcNyvRO8SIo6OBG56cL3UPqzn4aWKFkpOo1EMoS4%0Ak9FIYelroZasNs%2FT41c%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423515987/a8b2cdf433bc12d9e8d1385eabf0/CleanShot+2026-05-25+at+15_34_35%402x.png?expires=1784333700&signature=bc869cc19d0f90bfccddca51713befaa8f4a6da47025a42dc540f04649d2abd4&req=diQlFcx%2FmIhXXvMW1HO4zcNyvRO8SIo6OBG56cL3UPqzn4aWKFkpOo1EMoS4%0Ak9FIYelroZasNs%2FT41c%3D%0A)

💡 **Use Case:** Your admissions team wants any student who asks about visiting campus to be guided toward the right visit option. A Custom Skill can ask whether they want an open house, personalized tour, virtual session, or appointment, then use the right configured tool.

---

# Use Custom Skills when behavior must be predictable

Use a Custom Skill when the agent should follow a specific sequence every time the same type of conversation occurs.

This is useful when the agent needs to:

* Ask a required qualifying question
* Use a specific tool
* Route to a specific team
* Avoid making promises about dates, availability, eligibility, or pricing
* Add a specific label for reporting or automation
* Create a follow-up task when the request cannot be completed automatically

Custom Skills are especially helpful when a general answer is not enough and the agent needs to move the conversation toward a defined operational outcome.

---

# Use Knowledge when the agent only needs information

Use **Knowledge** when the agent needs to answer questions from approved content, such as policies, program pages, deadlines, or office information.

Use a Custom Skill instead when the agent needs to do more than answer, such as asking follow-up questions, sending a configured event registration link, adding a label, creating a task, routing the conversation, or applying channel-specific behavior.  
​

Custom Skills can only use tools tied to products and capabilities enabled for your institution, so the exact tools available in your Action editor may vary.

|  |  |
| --- | --- |
| **Need** | **Use** |
| Answer a factual question from approved content | Knowledge |
| Confirm a student's intent before taking action | Custom Skill |
| Send a configured event registration link or trigger a tool such as Schedule Appointment | Custom Skill |
| Apply different behavior by channel or schedule | Custom Skill |
| Surface program pages, office hours, or deadlines | Knowledge |

**Explore More >** [Adding Knowledge Hub Sources](https://help.element451.com/en/articles/12276752-adding-knowledge-hub-sources)

---

# Use system skills for standard agent capabilities

Bolt Agents include native skills for common platform capabilities, such as inquiry flows, application actions, event registration, appointment scheduling, handoffs, and data access. Use native skills when the standard behavior already fits the job.

Use a Custom Skill when you need to control when and how those capabilities are used for a specific scenario.

For example:

* Enable **Register for Event** as a native skill so the agent can use event registration
* Create a Campus Visit Scheduler Custom Skill to decide when the agent should send the registration link for a specific open house or schedule a specific appointment type

**Explore More >** [Bolt Agent Skills](https://help.element451.com/en/articles/8993380-bolt-agent-skills)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423546111/379082ae8ae258db4a44138d7b80/CleanShot+2026-05-25+at+15_48_06%402x.png?expires=1784333700&signature=6c7254d0ba14a1c8e431587beea53c4cd8324f539863bc07f9794d2c6389d187&req=diQlFcx6m4BeWPMW1HO4zSaLavQH7kOLpk8runl2TUj7cqQTOLocPjYs4s7U%0AqrzorcC2eRXOVLC%2FGrM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423546111/379082ae8ae258db4a44138d7b80/CleanShot+2026-05-25+at+15_48_06%402x.png?expires=1784333700&signature=6c7254d0ba14a1c8e431587beea53c4cd8324f539863bc07f9794d2c6389d187&req=diQlFcx6m4BeWPMW1HO4zSaLavQH7kOLpk8runl2TUj7cqQTOLocPjYs4s7U%0AqrzorcC2eRXOVLC%2FGrM%3D%0A)

---

# Use Jobs for proactive outreach

Use **Bolt Agent Jobs** when your team wants the agent to start outreach proactively, such as contacting a segment of students with a campaign-like objective.

Use Custom Skills to control how the agent handles qualifying replies or student intent during the conversation.

For example:

* A Job starts an outbound message about campus visit opportunities
* A student replies that they want to attend an open house
* The agent uses the active Custom Skill to guide the conversation and send the correct registration link or use the correct scheduling action

📌 **Note:** Custom Skills are designed around conversations. If a behavior depends on a student response inside a Job conversation, test that path carefully with the agent and confirm the skill triggers as expected.

**Explore More >** [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job)

---

# Use workflows when the process should continue outside the conversation

Use **workflows** when a downstream process should run after a person is identified or categorized. A Custom Skill can help start that process by applying a label, creating a task, or collecting information during the conversation.

A common pattern is:

1. The student expresses a specific intent
2. The Custom Skill confirms the intent
3. The Custom Skill uses **Add Label**
4. A workflow or segment uses that label for follow-up

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423552928/5bd327bd1b48fd5cf52ebb1d7d61/CleanShot+2026-05-25+at+15_51_05%402x.png?expires=1784333700&signature=d52dafc938b5fd414b41a56379f8feedb4c387496013e86a1e493512f7e1754c&req=diQlFcx7n4hdUfMW1HO4ze%2FwyZIKDuMe0EB%2FX99hEnKLcdcvvRmwhqsR5loq%0AXgXZ1TczYBjgvN6%2By6M%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2423552928/5bd327bd1b48fd5cf52ebb1d7d61/CleanShot+2026-05-25+at+15_51_05%402x.png?expires=1784333700&signature=d52dafc938b5fd414b41a56379f8feedb4c387496013e86a1e493512f7e1754c&req=diQlFcx7n4hdUfMW1HO4ze%2FwyZIKDuMe0EB%2FX99hEnKLcdcvvRmwhqsR5loq%0AXgXZ1TczYBjgvN6%2By6M%3D%0A)

---

# Do not use Custom Skills for everything

Custom Skills are powerful, but they should stay focused. Avoid creating a Custom Skill for every possible question.

Do not use a Custom Skill when:

* The agent only needs to answer from Knowledge
* A native skill already handles the scenario correctly
* The scenario is too broad to test reliably
* The action depends on information that is not configured or approved
* Your team has not decided what the correct process should be

🚨 **Important:** A Custom Skill should reflect a process your team understands. If the process is unclear, define the workflow first, then build the skill.

---