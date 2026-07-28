---
title: Creating a Bolt Agent Job
url: https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job
collection: Bolt AI
---

Learn how to create a Bolt Agent Job—choose goals, assign agents, set actions, manage approvals, and configure triggers.

# Overview

Once you understand what Bolt Agent Jobs are and when to use them, the next step is creating one. This article walks you through how to set up a job in Element451—from choosing a goal to configuring actions and assigning your Bolt Agent.

If you're looking for an overview first, check out [Getting Started with Bolt Agent Jobs](https://help.element451.com/en/articles/11131186-getting-started-with-bolt-agent-jobs).

---

# Creating a Bolt Job

To get started creating a new Bolt Agent Job, head over to the Bolt Agents section of Element451:

1. Navigate to **Engagement > Bolt Agents.**
2. Click the **Jobs** tab in the left-hand menu. You'll see a table of all existing jobs, along with key stats such as the total number of people, approvals needed, and the last action date.
3. Select **+ New Job** in the top-right corner.

You're now in the job builder! Let's walk through each section below.

## Using Bolt Jobs Agent

Need help creating a Job? The Bolt Jobs Agent is a [staff agent](https://help.element451.com/en/articles/7173423-getting-started-with-bolt-agents-for-staff) that guides you through the setup using conversational AI. It's a quick, easy way to get started.

You can launch the Bolt Jobs Agent from the sidebar, no matter where you are in Element451. Just start a chat and let the agent walk you through the process of building and configuring a Job that fits your goals.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1586078946/7e23ad29b5a26f00403a20727802/Create+Bolt+Job+Card%402x.png?expires=1784333700&signature=0c1a5ff5b03252d7e67d7f6c92198e5e61d7e3504c762ca995919707a0d878d9&req=dSUvEMl5lYhbX%2FMW1HO4zSDNy3Dpf1ul%2BjfqO3OsLEWAnvhgsTyLw2%2B7V5ZR%0AY2%2Fr3LtRWsLFToYAjT0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1586078946/7e23ad29b5a26f00403a20727802/Create+Bolt+Job+Card%402x.png?expires=1784333700&signature=0c1a5ff5b03252d7e67d7f6c92198e5e61d7e3504c762ca995919707a0d878d9&req=dSUvEMl5lYhbX%2FMW1HO4zSDNy3Dpf1ul%2BjfqO3OsLEWAnvhgsTyLw2%2B7V5ZR%0AY2%2Fr3LtRWsLFToYAjT0%3D%0A)

---

# Settings

* **Name**

  + Replace the default "Untitled Job" with a descriptive name that clearly indicates the purpose of the job.
* **Active**

  + Toggle the job on when you're ready to launch it. It's best to complete your configuration before activating.
* **Bolt Agent**

  + Select the Bolt Agent that should own the job. Choose an agent based on its configured expertise. You can manage your Bolt Agents in the **All Agents** section.

    - Note: When an agent is assigned to a Bolt Agent Job, they're automatically enabled to handle inbound SMS and email responses. This cannot be disabled. If you want a different set of agents to appear in Live Chat or StudentHub, create a Team with a rule that defines your preferred configuration.
* **Channels**

  + Select the channels the agent is allowed to use (Email, SMS, and/or Phone)

    - Note: To protect your institution, ensure that phone calls and recordings are used in compliance with any applicable regulations.
* **Email Address**

  + If the email channel is enabled, you can select an email address that the agent will use to send emails from.
  + If not specified, the agent's configured email will be used. If the agent has no configured email address, the default system email address will be used.
* **User Email Preference**

  + Choose which emails the agent can send to. If both are selected, the available one will be used. If only school is selected, it will fall back to primary if school is missing or unsubscribed.
* **Phone Number**

  + If the SMS and/or Phone Call channels are enabled, you can select the phone number that the agent will use to contact the user. If not specified, the agent's configured phone number will be used. If the agent has no configured phone number, the default system phone number will be used.
* **Phone Number for Call Transfer**

  + Enter the phone number where calls should be transferred when a user requests to speak to a human.
* **Goal**

  + Choose the outcome you're asking your Bolt Agent to achieve. The **job's goal cannot be changed once created**, so choose carefully.
  + Depending on your selected goal, you may be prompted to provide additional context, like choosing which application, form, or event applies.
  + [We explain goals more in the next section](#h_d60858b69a).
* **Close Conversation on Send**

  + When enabled, the agent will close the conversation after sending a message.
* **Consider Past Activity**

  + When enabled, the agent will check each contact's record at enrollment to see if they have already completed the job's goal. If they have, the agent will mark them as **No Action Needed** and take no further steps.
  + Turn this off if you want the job to run for all enrolled contacts, regardless of whether they've completed the goal in the past.
* **General Instructions**

  + Provide high-level guidance on how the Bolt Agent should approach the job.

    - Instructions are optional, but **HIGHLY** recommended.
    - Instructions can include guidance for things like:

      * Preferred order or use of channels already enabled in the Channels setting (e.g., "start with Email")
      * Cadence of outreach (e.g., "no more than twice per week")
      * Content focus based on audience (e.g., nursing students → promote clinical sites and exam pass rate)
      * Tone (casual vs. formal), urgency, or strategic focus areas
    - For guidance and best practices for writing strong instructions, [click here](https://help.element451.com/en/articles/11128047-advanced-strategies-and-best-practices-for-bolt-agent-jobs#h_5a76b36f42).
* **Segment**

  + Choose the segment of contacts who will be enrolled in this job. This is your target audience. This works similarly to Workflows, where your audience is loaded once during job creation. If you want to add contacts to the job dynamically, you can use the **trigger** option. We discuss triggers later in this article.
* **Approvers**

  + Select the users who should be notified when the agent needs approval for actions.
* **Assign Conversation To**

  + Select one or more users who will be assigned to the conversations created by the agent.
* **Make Conversations Private**

  + When enabled, all conversations created by this agent will be marked as private. Requires at least one conversation assignee.
  + 🚨Warning: Enabling this option can also make existing open conversations private.
* **Enrollment Limit**

  + This is the maximum number of contacts who can be active in this Job at once. Contacts added beyond the limit show a Pending status until space becomes available. A Job’s limit cannot exceed the instance-level Jobs Enrollment Limit shown in Engagement > Bolt Agents > Settings.
* **Deadline**

  + Set a date by which the job should end. After midnight on this date, the agent will stop taking action for this job.

---

# Goals

The goal is the core outcome you want your Bolt Agent to achieve. Everything in the job revolves around it. It sets the purpose and defines what success looks like. The goal you select will determine what context the agent needs (such as a specific form, application, or event), and it helps shape the agent's strategy.

Once a goal is selected and the job is created, it cannot be changed, so choose thoughtfully.

Need help choosing the right goal or designing a smart job strategy? Check out our guide on [Advanced Strategies and Best Practices for Bolt Agent Jobs](https://help.element451.com/en/articles/11128047-advanced-strategies-and-best-practices-for-bolt-agent-jobs), which includes recommendations, use cases, and tips to align jobs with your institution's goals.

## Goal Types

Below are the goal types available when creating a Bolt Job, along with their intended outcomes:

|  |  |
| --- | --- |
| **Goal** | **Description** |
| **Inform or Notify** | Deliver a message or piece of information to the contact; no action required |
| **Capture Leads** | Collect initial interest or contact details from a new prospect |
| **Submit Application** | Get the contact to complete and submit an application they've started |
| **Submit Form** | Get the contact to complete and submit a specified form |
| **Start Application** | Get the contact to begin filling out an application |
| **Pay Form** | Get the contact to make a form payment. |
| **Pay Application Fee** | Get the contact to pay an application fee. |
| **Pay Deposit Fee** | Get the contact to pay a deposit fee. |
| **Sign Up for Event** | Get the contact to register for a specific event  *Jobs with "Sign Up For Event" goals validate event availability upfront, abandoning enrollments when events are closed or signups are disabled.* |
| **Schedule Appointment** | Get the contact to book an appointment |
| **Submit Survey** | Get the contact to submit a survey. |
| **Join Segment** | Get the contact to meet the conditions to join a specific segment |
| **Leave Segment** | Get the contact to meet the conditions to leave a specific segment |

---

# Actions

Once your job's structure is in place—goal, audience, assigned agent—it's time to define what your Bolt Agent is allowed to do to achieve the goal. These are called **Actions**.

An Action is a permission your Bolt Agent uses to engage with a contact, whether that's sending a message, promoting a form, or scheduling a meeting. You can add multiple actions per job, and order matters: the agent will prioritize actions in the order they are listed.

**Important**: If an action uses a feature that consumes [usage credits](https://help.element451.com/en/articles/10421758-usage-based-billing-credits) (such as sending an SMS), the same charges apply when the agent performs it. In general, anything that costs credits when done manually will also consume credits when done by a Bolt Agent.

## Action Types

Below are the action types available when creating a Bolt Job, along with the context needed:

|  |  |  |
| --- | --- | --- |
| **Action** | **Context Needed** | **Additional Info** |
| Make Introduction | None |  |
| Promote Application | Select the application |  |
| Promote Survey | Select the survey |  |
| Provide Information | None |  |
| Promote Event | Select the event  (and occurrence if applicable) | *The agent validates event availability upfront, abandoning enrollments when events are closed or signups are disabled.*  *When events reach capacity, the agent continues monitoring for capacity changes (the following day at 9 AM), allowing for potential reopening if spots become available.* |
| Promote Form | Select the form |  |
| Schedule Appointment | Select the availability |  |
| Enroll in Workflow | Select the workflow |  |

## Adding an Action

1. Click **+ Add Action** button from the job configuration screen.
2. Replace **"Untitled Action"** with a clear, descriptive name to help you identify what the agent is trying to do.
3. Configure the settings in both the **General** and **Self-Approval** tabs, as explained below.
4. Click Save in the top right corner.
5. Repeat steps 1-4 to add more actions.

### General Tab

* **Name**: In the header, replace the generic action type text, with a descriptive name that reflects its purpose.
* **Action Type**

  + Choose the type of action the agent should take. Action types are explained in the section above titled "Action Types."
* **Context Settings**

  + Some skill types require you to select additional context. For example, if you're promoting an event, you'll need to select which event. This field will dynamically appear if the type requires it.
* **Settings**

  + **Enabled?**: Toggle on or off to determine whether the agent can use this action.
  + **Instructions**: Provide specific guidance for how the agent should carry out this action. This can include tone, messaging points, or behavior rules.

    - For guidance and best practices for writing strong instructions, [click here](https://help.element451.com/en/articles/11128047-advanced-strategies-and-best-practices-for-bolt-agent-jobs#h_5a76b36f42).

### Self-Approval Tab

Use these settings to control when your Bolt Agent can act independently versus when it should request human approval.

* **Allow Self-Approval:** Enable this toggle if the agent should be allowed to complete this action without human review and approval.

* **Self-Approval Guidelines:** Add free-text guidance to help the agent decide when to act independently and when to ask for approval. You can add multiple guidelines and reorder them. The agent will follow them in order.

**Important**: Enabling self-approval means you're allowing the agent to take action on its own, without human input. This effectively removes the "human in the loop" for this particular action. You should only enable self-approval when you're confident the action is low-risk or you've provided detailed, clear **approval guidelines**. Proceed with caution and test thoroughly before scaling.

To learn more about managing your approvals, [click here](https://help.element451.com/en/articles/12037492-managing-enrollments-contacts-approvals-in-bolt-agent-jobs#h_cabd86f210).

## Action Settings

Under your list of actions, you'll see one additional setting to configure:

* Urgent Mode: Prompts faster eligible action by reducing scheduling and monitoring delays. SMS and Phone actions still follow permitted local-time windows and all safety and compliance safeguards.

---

# Triggers

In addition to enrolling people through a segment, you can also use **triggers** to automatically add individuals to the job based on specific actions they take.

**This can be used in conjunction with your segment.** For example, you might start with a segment of inquiry-stage students and also set up a trigger to enroll anyone who submits a Request for Information (RFI).

💡 **Case Management:** The **Alert Created** and **Case Created** triggers connect Bolt Agent Jobs to the **Case Management** module—a Job can enroll any contact who gets a qualifying alert or case, and the enrollment is automatically related to the case so it appears on its **Jobs** tab. For how this fits into Case Management automation, see [Automating Case Management](https://help.element451.com/en/articles/14712713-automating-case-management-closed-beta) and [Bolt AI in Case Management](https://help.element451.com/en/articles/15465010-bolt-ai-in-case-management-closed-beta).

## Adding a Trigger

1. Click **+ Add Trigger**
2. Choose a **trigger** (see the list of options below)
3. Enter a name and description
4. Set the trigger to Active or Inactive

### List of Trigger Options

* **Alerts**

  + **Alert Created** — Enrolls the contact when an alert is created for them
* **Applications**

  + **Application Completed** — Enroll people who complete an application
  + **Application Started** — Enroll people who start an application
  + **Application Submitted** — Enroll people who submit an application
  + **Recommendation Submitted** — Enroll people when a recommendation is submitted
* **Appointments**

  + **Appointment Attended** — Enroll people who have attended an appointment
  + **Appointment Canceled** — Enroll people who have canceled an appointment
  + **Appointment No Show** — Enroll people who have been marked as No Show to an appointment
  + **Appointment Scheduled** — Enroll people who scheduled an appointment
  + **Appointment Updated** — Enroll people who updated an appointment
* **Cases**

  + **Case Created** — Enrolls the contact when a case is created for them
* **Decisions**

  + **Decision Checklist Items** — Enroll people when their checklist item status (completed, waived, incomplete) is changed
  + **Decision Released** — Enroll people when their application decision is released
  + **Decision Stage Changed** — Enroll people when their application decision stage changes
  + **Decision Status Changed** — Enroll people when their application decision status changes
* **Documents**

  + **Document Uploaded** — Enroll people when a related document is uploaded or imported
* **Events**

  + **Event Signup** — Enroll people who sign up for an event
* **Forms**

  + **Form Submitted** — Enroll people who submit a form (e.g. information request on a landing page)
  + **Paid Form** — Enroll people who submit a paid form
* **Grades**

  + **Grade Risk Changed** — Enroll people when their grade risk changes
* **Labels**

  + **User Label Added** — Enroll people when they are given the selected label
  + **User Label Removed** — Enroll people when the selected label is removed from them
* **Surveys**

  + **Survey Response - Positive Sentiment** — Enroll people who submit a survey response with positive sentiment
  + **Survey Response - Negative Sentiment** — Enroll people who submit a survey response with negative sentiment
* **Users**

  + **Joined Segment** — Enroll people when they join a calculated segment
  + **Joined or Left Segment** — Enroll people when they join or exit a calculated segment
  + **Left Segment** — Enroll people when they exit a calculated segment
  + **User Birthday** — Enroll people at 5:01 UTC on their birthday
  + **User Territory Changed** — Enroll people when their territory changes

---

# What's Next?

Once your job is created and active, your agent gets to work. To help you stay on top of what's happening, here are two articles to guide your next steps:

* **[Monitoring + Managing Bolt Agent Jobs](https://help.element451.com/en/articles/11128001-monitoring-managing-bolt-agent-jobs)**

  Learn how to track job-level performance on the All Jobs page. This article covers how to monitor overall impact, edit job settings, duplicate or delete jobs, and access approvals.

* **[Reviewing & Managing Enrollments (Contacts) in Bolt Agent Jobs](https://help.element451.com/en/articles/12037492-managing-enrollments-contacts-approvals-in-bolt-agent-jobs)**  
  Take a closer look at individual enrollments inside your job. You'll learn how to review enrollment details and action history, understand the agent's reasoning, manage approvals, and add or remove people.

You can also check out **[Advanced Strategies and Best Practices for Bolt Agent Jobs](https://help.element451.com/en/articles/11128047-advanced-strategies-and-best-practices-for-bolt-agent-jobs)** for guidance on designing jobs, layering actions, and fine-tuning your approach to support every stage of the student journey.

---

# Create Bolt Agent Jobs from Modules

You can launch a Bolt Agent Job directly from the header of several key modules in Element451. Just click the "**Create Bolt Agent Job"** button at the top of the page while working in **Applications**, **Appointments**, **Events**, **Forms**, or **Surveys**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1922506889/37a7f4d8789e13f91a97be5cc8ff/CleanShot+2026-01-08+at+18_23_06%402x.png?expires=1784333700&signature=5c938851c6a13ff4f92728e81c63b7999582c04e5d98f6b9f737e46cccbf11ac&req=dSklFMx%2Bm4lXUPMW1HO4zbJqUPqmd81bm4PrZfUhqYXj%2F%2B%2FJ1ApqiO8xm7lJ%0A54NxJa0e2CqJzYLrW3c%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1922506889/37a7f4d8789e13f91a97be5cc8ff/CleanShot+2026-01-08+at+18_23_06%402x.png?expires=1784333700&signature=5c938851c6a13ff4f92728e81c63b7999582c04e5d98f6b9f737e46cccbf11ac&req=dSklFMx%2Bm4lXUPMW1HO4zbJqUPqmd81bm4PrZfUhqYXj%2F%2B%2FJ1ApqiO8xm7lJ%0A54NxJa0e2CqJzYLrW3c%3D%0A)

Each job is powered by a best-practice template designed to support common recruitment and follow-up actions. You can review and personalize the job before launching.

Here's what's available in each module:

* **Applications**

  • Promote Application

  • Finish Your Application

  • Collect Deposit
* **Appointments**

  • Promote Appointment

  • Follow-Up On Appointment
* **Events**

  • Promote Event

  • Follow-Up On Event
* **Forms**

  • Promote Form

  • Follow-Up From Form Submission
* **Surveys**

  • Promote Survey

  • Follow-Up On Survey

---