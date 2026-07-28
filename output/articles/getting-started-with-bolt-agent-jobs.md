---
title: Getting Started with Bolt Agent Jobs
url: https://help.element451.com/en/articles/11131186-getting-started-with-bolt-agent-jobs
collection: Bolt AI
---

Introduces the concept of Bolt Agent Jobs, why they exist, and what problems they solve.

# Overview

Most AI tools wait for input. **Bolt Agent Jobs** flip that script—giving your **Bolt Agents** the ability to take initiative, plan their next move, and work toward real goals with minimal human direction.

This article introduces what Jobs are, why they matter, and how they’re different from other automation tools in Element451. If you’re ready to start creating Jobs, check out [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job).

---

# What is a Job?

Bolt Agent Jobs allow you to assign a specific task to a Bolt Agent, such as getting students to register for an event or complete their application, and then empower it to complete the work autonomously.

Instead of sitting in the inbox and waiting to be asked a question, your Bolt Agent proactively:

* Reaches out to the right students
* Uses a mix of approved action skills (e.g., scheduling an appointment)
* Tracks progress toward the goal
* Asks for human approval when needed

## Key Behaviors + Context for Bolt Agent Jobs

* **Context Available to the Agent:**

  + **Enrollment Context**: Agents are aware if a contact is enrolled in other jobs.
  + **Activity/Convo Context**:

    - **Conversations**: Agents can access summaries of a contact's past one-on-one conversations (with staff and other agents).
    - **Campaigns**: Agents have visibility into how users engage with your campaigns, enabling more informed conversations. For example, the agent can reference "I see you received the scholarship email we sent yesterday" or adjust communication strategy based on engagement patterns.

      * Campaign title (internal name)
      * Communication channel (emails, SMS, push)
      * User actions (clicked, delivered, opened, read, sent)
      * Email subject line
      * Message content (SMS and push only)
      * Relative timestamp (e.g. 2 hours ago)

  This supported activity context helps reduce duplicate outreach and supports more relevant, timely messaging.
* **Follow-Up Scheduling:** Agents can automatically recognize and schedule follow-up requests made by students (e.g., “Email me at 3 PM” or “Call me next Tuesday”) across email, SMS, and phone channels.
* **TCPA-Compliant Communications:** All agent-initiated SMS and phone communications are automatically scheduled within federally permitted time windows, based on the recipient’s local time zone.

---

# When (and Why) to Use a Job

**Use a Bolt Agent Job when you want to:**

* Scale outreach without creating a rigid workflow
* Assign a goal to your Bolt Agent (like “Submit Application” or “Schedule Appointment”)
* Let the agent choose the best course of action using its available skills
* Collaborate with staff using approval requests and guidelines

**Jobs are especially useful when:**

* You want to **engage a segment** of students proactively
* The task has a **clear success outcome**
* There are **multiple possible paths** to reach that outcome
* You need to **offload repetitive outreach**, but still want control when it matters

**Some common use cases include:**

* Nudging prospective students to complete their application
* Re-engaging prospective students who haven’t responded
* Promoting an upcoming event to a segment of interested students
* Guiding admitted students to schedule appointments or submit forms
* Introducing your institution to new leads by sharing institutional information

💡 **Bolt Agent Jobs in Case Management:** Jobs act as the proactive-outreach engine for the **Case Management** module—a Job can be triggered when an alert or case is created, handling routine outreach while staff focus on the judgment calls that need a person. The enrollment is automatically related to the case so it stays visible on the case's **Jobs** tab. See [Bolt AI in Case Management](https://help.element451.com/en/articles/15465010-bolt-ai-in-case-management-closed-beta).

For a more in-depth look at use-case examples, be sure to check out our [Advanced Strategies and Best Practices for Bolt Agent Jobs](https://help.element451.com/en/articles/11128047-advanced-strategies-and-best-practices-for-bolt-agent-jobs) article.

---

# Anatomy of a Job

Every Bolt Agent Job includes four essential parts:

|  |  |
| --- | --- |
| **Goal** | This is the outcome you’re asking the Bolt Agent to accomplish (like “Submit Application” or “Sign Up for Event”). The agent uses this to determine when it has finished with each person. |
| **People** | The specific group of contacts the Bolt Agent will act on. You can enroll people manually, through a segment, or automatically via a trigger, such as a form submission. |
| **Actions** | These are the tools your Bolt Agent is allowed to use, such as sending emails, promoting forms, scheduling appointments, or providing information. You decide what’s available and customize how each one should behave. |
| **Approval** | You’re always in control. You can require human approval for every action, or allow the Bolt Agent to act independently with optional self-approval and custom guidelines. |

---

# Accessing Jobs

Jobs are managed in the **Bolt Agents** section under the **Engagement** menu item. When you open the Jobs tab, you’ll see all **current** and **past** jobs, plus high-level metrics like:

* Goals completed
* Estimated hours saved
* Actions needing approval

[![important](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1498371257/2831287b8aed1c396ff668edd20e/Important.png?expires=1784333700&signature=c5b9e05bb21932fee705d1db55cfe8f420ca654d3b3ee574620322c7a12d25a0&req=dSQuHsp5nINaXvMW1HO4zdzybK7JpfOS56pw4gX4ThYEklR6V74wzJJ%2B5mZ%2F%0AE%2FM99Xe4lfI5B9ohYgQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1498371257/2831287b8aed1c396ff668edd20e/Important.png?expires=1784333700&signature=c5b9e05bb21932fee705d1db55cfe8f420ca654d3b3ee574620322c7a12d25a0&req=dSQuHsp5nINaXvMW1HO4zdzybK7JpfOS56pw4gX4ThYEklR6V74wzJJ%2B5mZ%2F%0AE%2FM99Xe4lfI5B9ohYgQ%3D%0A)

If you’re used to step-by-step automation, Jobs will feel different. They adapt based on what works for each contact using the Actions, knowledge, and context available to them.

---

# What’s Next?

Now that you know what Bolt Agent Jobs are and when to use them, you’re ready to build one. Head to [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job) for a step-by-step guide.

---