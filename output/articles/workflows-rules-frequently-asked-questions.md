---
title: 📌 Workflows + Rules: Frequently Asked Questions
url: https://help.element451.com/en/articles/10618199-workflows-rules-frequently-asked-questions
collection: Workflows + Rules
---

[![pardon our progress, this article is in development](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390931069/b309b2e3447bf4b191453c636fe5/Pardon+our+Progress.png?expires=1784333700&signature=3425aac5e962d4b8aeabf78e3ece4b0834a35f96ccb174ad1d73835e2a1c5c6c&req=dSMuFsB9nIFZUPMW1HO4zS4o6Onn0cMtGrpIovLd0JJtP9nvDFzQmKRLNcX%2F%0AFn5vjCnDGm8aNR1r3Nk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390931069/b309b2e3447bf4b191453c636fe5/Pardon+our+Progress.png?expires=1784333700&signature=3425aac5e962d4b8aeabf78e3ece4b0834a35f96ccb174ad1d73835e2a1c5c6c&req=dSMuFsB9nIFZUPMW1HO4zS4o6Onn0cMtGrpIovLd0JJtP9nvDFzQmKRLNcX%2F%0AFn5vjCnDGm8aNR1r3Nk%3D%0A)

# General

#### What happens if contacts are enrolled in an inactive workflow?

Inactive workflows **do not run**, but contacts can still be enrolled. If the workflow is later activated, all enrolled contacts will immediately begin moving through the workflow. Be sure to review any pending enrollments before turning it on to prevent unintended actions.

#### What does the Workflows profile card show?

The Workflows card displays all workflows and rules associated with an individual student. It’s divided into three sections:

* **Active Workflows**: Shows workflows the student is currently in. Includes:

  + Workflow title
  + Last completed step
  + Enrollment date
  + Click the title to view details, including:

    - Run reason
    - Trigger name (if applicable)
    - Step-by-step flow with condition results and action status

* **Completed Workflows**: Shows workflows the student has finished. Includes the same data points as Active, plus:

  + Completed date

* **Rule Activity**: Displays past rule executions tied to the student. Includes:

  + Rule name + title
  + Execution timestamp
  + Click to view the condition evaluation and executed action details

---

# Actions

#### Can I deactivate contacts via a workflow or rule?

No, our system does not currently support an action to deactivate contacts in bulk via workflows or rules automatically.

---

# Delays

#### Can I use both a standard and relative delay in the same workflow step?

No, you can only use **one delay type per step**—either standard or relative, not both. ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390940593/f5f66915c168f853f2bfa22bc810/Important.png?expires=1784430000&signature=691d85c00e6e14390c973018777bbb9b11b14e0e4ebd60487700b6df6abe6cd7&req=dSMuFsB6nYRWWvMW3Hu4gZo3EJBEli4j9p%2B04rSjGmx%2FOkEuIYFLhoy1D0hf%0AxQ%3D%3D%0A) When configuring a delay, the **active tab at the time of saving** determines which delay type is used. If both the **Standard** and **Relative** tabs are configured, only the delay type selected on the active tab will apply when you save.

---

# Troubleshooting

#### Why does the “Updated” column on the All Workflows page show today’s date, even if I didn’t make changes?

The **Updated** column reflects **backend updates**, not just manual edits. For active workflows, this timestamp will often show today’s date because workflows are continuously processed and updated in the background. Even if no one on your team made changes, the system activity can still update the timestamp.

We’re exploring ways to improve this in the future for better clarity.

#### How can I remove a delay from a workflow when I get an error stating "the selected `content.segment guid` is invalid"?

This error typically occurs when a condition in the workflow is missing a selected segment. To resolve it:

1. Open the workflow and locate the step where the error appears.
2. Select a **segment** for the condition.
3. Once a segment is chosen, you can delete the delay.

Repeat these steps for each instance where the error occurs.

#### Why isn’t the email sending in my workflow, even though students are progressing through the steps?

If students are successfully moving through the workflow but not receiving the email, check the *Send Communications* action settings:

* First, review the **send time** option. If it’s set to *user’s preferred open time*, the email won’t send immediately—it’ll wait for the student’s optimal engagement time. Learn more about how that works [here](https://help.element451.com/en/articles/8857428-preferred-time-to-send).
* To send the email as soon as the student reaches that step, switch the send option to *immediate*.
* Also, confirm the student hasn’t **unsubscribed** from emails. You can check this on their contact record (milestones), along with their preferred open time.

#### How can I troubleshoot a workflow to understand why a student did—or didn’t—receive an action like an email?

We recommend using the **Workflows** card on the student’s profile to investigate.

When you click into a workflow listed on the card, you’ll see a visual breakdown of the steps. This includes:

* **Timestamps** for when each action occurred
* **Pass/fail indicators** for conditions

This view helps you determine whether the student met the conditions that triggered a specific path in the workflow. In other words, it answers the “why” or “why not” behind the action execution.

#### Why is a Contact not in the Workflow or Rule?

Below is a list of suggested troubleshooting tips to resolve any potential problems that may be causing Contacts to be excluded from your Workflow or Rule:

* **Verify Contact Meets Conditions**

  1. Navigate to the Contact's profile.
  2. Confirm that the Contact meets all the conditions specified.

* **Inspect Step Conditions + Segment Triggers**

  1. Ensure there's congruence between the step conditions and segment triggers. For example, confirm that the segment doesn't exclude Contacts who fail to meet the conditions.
* **Inspect Delays**

  1. Review all delays, especially those relative to the previous step.
  2. Confirm that the delays are correctly configured.

* **Inspect Communication Statistics**

  1. Check for email bounce rates and recipient status.
  2. Investigate if there are issues, such as incorrect email addresses, or if the Contact has opted out of receiving emails from your institution.

* **Inspect Your Segments**

  1. Revisit your segment(s) and ensure they are filtering Contacts as intended.

**Pro Tip:** When configuring your Workflow or Rule, it's imperative to **activate it before adding any Triggers.** Adding triggers before activation can result in students who have joined the segment not progressing as they should.

---