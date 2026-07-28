---
title: Managing Enrollments (Contacts) + Approvals in Bolt Agent Jobs
url: https://help.element451.com/en/articles/12037492-managing-enrollments-contacts-approvals-in-bolt-agent-jobs
collection: Bolt AI
---

Learn how to review enrollment history, action details, and agent reasoning, manage approvals, and add or remove people from jobs.

# Overview

Every contact’s participation in a Bolt Agent Job is called an **enrollment**. Reviewing enrollments gives you full transparency into how your agent is working with each contact, the actions being taken, and the reasoning behind those actions. From here, you can also manage approvals, add or remove people from a job, and focus on conversations tied to a specific job.

In this article, you’ll learn how to:

* Review the People tab and enrollment details
* Explore enrollment history and action reasoning
* Manage approvals for agent actions
* Add or remove people from a job

---

# Understanding Contact/Enrollment Statuses

As your agent works toward the job’s goal, each enrollment moves through different **statuses** that reflect what’s happening in the process. These statuses provide visibility into whether the agent is actively planning an action, waiting, requires your approval, or has completed the goal.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676353355/0dd4ab491d2df1f54e9aac79f2d2/Agents+-+Status+-+Gif+%28500+x+200+px%29+%283%29.gif?expires=1784333700&signature=f259549f5538bb7aedc6e1161300a39274fd6a4f1a0eeb1e9ccd6db310ee1cd4&req=dSYgEMp7noJaXPMW1HO4zUVq1tXLVpQAYpegyrmaVF%2B9riaaqqIXq8rISQBZ%0ATUE%2BLBo8yhcDESCQdKk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676353355/0dd4ab491d2df1f54e9aac79f2d2/Agents+-+Status+-+Gif+%28500+x+200+px%29+%283%29.gif?expires=1784333700&signature=f259549f5538bb7aedc6e1161300a39274fd6a4f1a0eeb1e9ccd6db310ee1cd4&req=dSYgEMp7noJaXPMW1HO4zUVq1tXLVpQAYpegyrmaVF%2B9riaaqqIXq8rISQBZ%0ATUE%2BLBo8yhcDESCQdKk%3D%0A)

|  |  |
| --- | --- |
| **Thinking** | The agent is evaluating what to do next. It may be determining the best action, the right time to act, or checking for recent activity from other agents or staff. |
| **Monitoring** | The agent is idle for this contact and waiting until it’s time to “think” again. You can think of this as "sleeping." |
| **Approval Needed** | The agent has executed an action that requires human review before it can proceed. |
| **Goal Completed** | The agent successfully helped the contact achieve the job’s goal. |
| **No Action Needed** | The agent found that the contact had already completed the job’s goal before enrollment (due to the **Consider Past Activity** setting). The agent immediately disenrolled the contact and will take no further action. |
| **Cancelled** | A staff member manually removed this contact from the job. The agent will take no further action. |
| **Abandoned** | The agent stopped working toward the goal for this contact.    This can happen when:  * The job’s deadline passes, and the agent abandons all remaining enrollments that aren’t already final (completed, cancelled, or abandoned). * The agent determines, based on context, that continuing would not help achieve the goal. |
| **Failed** | There was an issue with the enrollment, and the agent cannot proceed.  * An error explanation will appear explaining why the enrollment failed. * You have the option to retry the enrollment. |

## Inactive Enrollment Status

When an active enrollment becomes **inactive**, its status label displays at 50% opacity, creating a clear visual distinction from active states (to illustrate that it is "paused" and won't continue until the job becomes active). The enrollment’s final status prior to becoming inactive remains visible for historical reference.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1709279080/4e7ba3ccbc12dc95d90e79108007/Enrollment+-+Inactive+State.png?expires=1784333700&signature=a7fff3bb2661813f0fcde6e15a87424465dabca86cbfaabf59fd939facfca839&req=dScnH8t5lIFXWfMW1HO4zTrtNm40DXoEuB%2FY8zOnznJHUpOvA%2FAzFHBRwX8F%0A5YNGtw2Aqrh8l8AiAZk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1709279080/4e7ba3ccbc12dc95d90e79108007/Enrollment+-+Inactive+State.png?expires=1784333700&signature=a7fff3bb2661813f0fcde6e15a87424465dabca86cbfaabf59fd939facfca839&req=dScnH8t5lIFXWfMW1HO4zTrtNm40DXoEuB%2FY8zOnznJHUpOvA%2FAzFHBRwX8F%0A5YNGtw2Aqrh8l8AiAZk%3D%0A)

---

# People (Enrollments)

When you open a job, go to the **People** section in the left-hand menu to see everyone enrolled in that job. We refer to each contact’s participation in a job as an **enrollment**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676292135/e3261b3dfa785d3efc51a654cad3/Jobs-2B--2BPeople-2BTab.png?expires=1784333700&signature=5283ce1d056880f0b5923aae8d222bfc232e716efee6164b8ab30c80a8d824aa&req=dSYgEMt3n4BcXPMW1HO4zaq7CWq0VWQGnr4JQPMG72OFeWn4zA96RA%2FirJqh%0AVAGN8t%2FuSoxV1g62%2BFU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676292135/e3261b3dfa785d3efc51a654cad3/Jobs-2B--2BPeople-2BTab.png?expires=1784333700&signature=5283ce1d056880f0b5923aae8d222bfc232e716efee6164b8ab30c80a8d824aa&req=dSYgEMt3n4BcXPMW1HO4zaq7CWq0VWQGnr4JQPMG72OFeWn4zA96RA%2FirJqh%0AVAGN8t%2FuSoxV1g62%2BFU%3D%0A)

## Summary Bar

At the top of the page, you’ll see a **summary bar** showing how the job is performing overall.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676369704/0117cf9e9c430f956d76a5c738c2/Jobs+-+People+Summary%402x.png?expires=1784333700&signature=ae610a4bd550e7b4bcace870a738f1dae873c17e70f8032fa9af5cd459288451&req=dSYgEMp4lIZfXfMW1HO4zQ4mpynCTc9m75H5CQtAHebI4002dfRHNuISQ9ep%0AmUHbb328QlospXAZIIo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676369704/0117cf9e9c430f956d76a5c738c2/Jobs+-+People+Summary%402x.png?expires=1784333700&signature=ae610a4bd550e7b4bcace870a738f1dae873c17e70f8032fa9af5cd459288451&req=dSYgEMp4lIZfXfMW1HO4zQ4mpynCTc9m75H5CQtAHebI4002dfRHNuISQ9ep%0AmUHbb328QlospXAZIIo%3D%0A)

It includes real-time counts for each enrollment status:

* Total
* Monitoring
* Approval Needed
* Goal Completed
* No Action Needed
* Abandoned/Canceled

⚠️ *Note: The Abandoned/Canceled count is hidden when the number = 0.*

For a definition of each status, refer to the [Understanding Contact Statuses](#h_ddeb49646c)section above.

## People Table

Under the summary bar is the **People table**, which gives you a quick snapshot of the status of each enrollment.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676379404/a78b57fb87a4c7e191a2b7d71e6b/jobs+-+people+table%402x.png?expires=1784333700&signature=9d03a7eb3400e70cfa90d7a555c723c2c90e7cc0fb8c5cdd19b98f845b1f34f7&req=dSYgEMp5lIVfXfMW1HO4zd%2FqrlIuNDk0I%2Buk8D3R%2F1tZQJk53Ie%2FCbXq1KNp%0ApExakeoHzv829ozm01A%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676379404/a78b57fb87a4c7e191a2b7d71e6b/jobs+-+people+table%402x.png?expires=1784333700&signature=9d03a7eb3400e70cfa90d7a555c723c2c90e7cc0fb8c5cdd19b98f845b1f34f7&req=dSYgEMp5lIVfXfMW1HO4zd%2FqrlIuNDk0I%2Buk8D3R%2F1tZQJk53Ie%2FCbXq1KNp%0ApExakeoHzv829ozm01A%3D%0A)

For every contact, you’ll see:

* **Person:** The enrolled contact

  + ✨ **Pro Tip:** Clicking their name opens the **Enrollment Details sidesheet**, where you’ll find their full enrollment history for that job.
* **Status:** Current stage in the job for this enrollment. For a definition of each status, refer to the [Understanding Contact Statuses](#h_ddeb49646c)section above.
* **Last Action:** The most recent step the agent took.
* **Last Agent Action:** A timestamp for the last action taken by the agent.
* **Last Contact Engagement:** The last time the contact engaged. Clicking the contact's name or the "view" option from the more menu will open the enrollment history, and you can click a specific action to open the action details. Here, you'll find a link to the conversation.

---

# Enrollment Details

When you click a person’s name, the **Enrollment Details** sidesheet opens. This view is designed to give you full transparency into how the agent has worked with that contact to achieve the job’s goal.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676292563/6872469aff40076934655a40db1e/Bolt-2BAgent-2BJobs-2B--2BEnrollment-2BDetails.png?expires=1784333700&signature=95913b043e04022a5b7f0a87baba93d590cda568cad759331791584b236c8bc8&req=dSYgEMt3n4RZWvMW1HO4zRSB4N2s35jE6U90fFMZXAR63MGX1Cy6jOjRmFih%0A7GQ3I8N7VRE8hPcEuEA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676292563/6872469aff40076934655a40db1e/Bolt-2BAgent-2BJobs-2B--2BEnrollment-2BDetails.png?expires=1784333700&signature=95913b043e04022a5b7f0a87baba93d590cda568cad759331791584b236c8bc8&req=dSYgEMt3n4RZWvMW1HO4zRSB4N2s35jE6U90fFMZXAR63MGX1Cy6jOjRmFih%0A7GQ3I8N7VRE8hPcEuEA%3D%0A)

Here’s what you’ll see:

* **Overview**: Quick reference info such as status, date enrolled, and last contact engagement.
* **Enrollment History**: A timeline of every action the agent has taken for that enrollment. This is where you get powerful insights into both the **what** and the **why** behind the agent’s decisions.

  + Each action (e.g., *Provide Information*) can be expanded to see its details (explained below in the next section).
  + Each item/action in the Enrollment History has a status.

    - **Pending:** The agent is awaiting the designated staff member too approve its proposed action.
    - **Approved**: The agent has received the necessary approval to proceed with executing the action.
    - **Skipped**: The agent determined no action was needed at that step and moved on without executing anything.

---

# Action Details

When you click on a specific action in the enrollment history, the **Action Details side sheet** opens with two tabs:

## Review Tab

The content displayed on the Review tab depends on whether the action has been executed. Here's what you can find in each state:

* **For Action Pending Approval:**

  + Action Overview
  + Action Settings (draft message being proposed)

    - ✨ **Pro Tip: You can manually edit this the proposed message by clicking into the text box.**
  + Approval/Reject buttons in the header

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1759397011/e08d3ed9fb99af0f78d59113e966/CleanShot%2B2025-10-03%2Bat%2B15_29_14.png?expires=1784333700&signature=ba219392bac0e378e9e21478383a95e89c0ea0231fb28a7d13479d6c3c6bd16d&req=dSciH8p3moFeWPMW1HO4zRYe2UGJXsgWDRRWMdroKvsF%2Bl1Rs5zmA39c5gel%0AC%2B5k%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1759397011/e08d3ed9fb99af0f78d59113e966/CleanShot%2B2025-10-03%2Bat%2B15_29_14.png?expires=1784333700&signature=ba219392bac0e378e9e21478383a95e89c0ea0231fb28a7d13479d6c3c6bd16d&req=dSciH8p3moFeWPMW1HO4zRYe2UGJXsgWDRRWMdroKvsF%2Bl1Rs5zmA39c5gel%0AC%2B5k%0A)

* **For Actions Already Executed:**

  + Action Overview
  + Action Settings (what was sent)
  + Execution date of when the action took place
  + "View Conversation" button linked to the conversation thread  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676457883/958ff523a973caf28025b4f9f1a7/Bolt-2BAgent-2BJobs-2B--2BEnrollment-2BReview.png?expires=1784333700&signature=39991bd19ac6ae4202f2d9bdb036bd0b906261fc789bdb4bf32fb091d22e4dfa&req=dSYgEM17molXWvMW1HO4zVQ0%2BS2IyBrGtzKHCOAxO2yZIZvvu5VObcyZqFAg%0AtqlF%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676457883/958ff523a973caf28025b4f9f1a7/Bolt-2BAgent-2BJobs-2B--2BEnrollment-2BReview.png?expires=1784333700&signature=39991bd19ac6ae4202f2d9bdb036bd0b906261fc789bdb4bf32fb091d22e4dfa&req=dSYgEM17molXWvMW1HO4zVQ0%2BS2IyBrGtzKHCOAxO2yZIZvvu5VObcyZqFAg%0AtqlF%0A)

## Reasoning & Feedback Tab

The content displayed on the Reasoning & Feedback tab depends on whether the action has been executed. Here's what you can find in each state:

* **For Action Pending Approval:**

  + The **agent’s reasoning** behind proposing that action, which could include why it chose the timing, working, strategy, etc.

    - Example: `I created an enthusiastic and friendly email communication for Eric to promote the completion of "Element University RFI." The email encourages him to fill out the form with a direct, clickable link and invites him to reply if he has any questions. The email is ready to be sent immediately upon approval.`
  + **Feedback Text Box**: The feedback text box works the same way as the *Provide* *Feedback* option available from the My Approvals page or the Bolt Staff Agent Side Panel. Instead of immediately approving or rejecting, you can enter guidance here for the agent to adjust its proposed message. Once submitted, the agent will re-enter the **Thinking** state, apply your feedback, and then resubmit the revised action for your approval.

* **For Actions Already Executed:**

  + The **agent’s reasoning** behind that action, which could include why it chose the timing, working, strategy, etc.

    - Example: `The user is in the PROSPECT stage with a STRANGER engagement score, indicating no prior engagement. The goal is to urge the student to schedule an appointment. Since no communication has been sent yet, it is appropriate to send an initial message now. The user’s preferred open time is MORNING, so the message should be scheduled accordingly.`  
      ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676464667/22f70da8de403ae1bea3c5927585/Bolt%2BAgent%2BJobs%2B-%2BReasoning%2Band%2BFeedback.png?expires=1784333700&signature=cd39cfc21435bc5f919247bc021d2a94018cd8d1a39b1f6b2d3890f7490b4811&req=dSYgEM14mYdZXvMW1HO4zfWkduvbmseIRT6fq5f7ONmsQQJz8yt6HkDj%2B9Mu%0Asr9Q%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676464667/22f70da8de403ae1bea3c5927585/Bolt%2BAgent%2BJobs%2B-%2BReasoning%2Band%2BFeedback.png?expires=1784333700&signature=cd39cfc21435bc5f919247bc021d2a94018cd8d1a39b1f6b2d3890f7490b4811&req=dSYgEM14mYdZXvMW1HO4zfWkduvbmseIRT6fq5f7ONmsQQJz8yt6HkDj%2B9Mu%0Asr9Q%0A)

✨ **Pro Tip:** If you’re ever wondering *why the agent made a decision* (e.g., why it sent an email at a certain time, or why it used a particular message), the **Reasoning & Feedback tab** is the best place to check.

---

# Managing Approvals

If you’ve been assigned as an approver on a Bolt Agent Job, you’ll be notified when the agent proposes an action that requires your review.

## Accessing Approvals

You’ll see yellow notification badge indicators in a few different places:

### (1) My Approvals

* Accessible from **Engagement** > **Bolt** **Agents** or from within a specific job. Both routes take you to the same My Approvals page.
* The My Approvals menu item will display a yellow notification badge when there are pending approvals waiting for your review.
* The My Approvals page provides a dedicated list of all pending approvals assigned to you.
* Use the arrow buttons in the top right corner to flip through your approvals.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676384717/4a2dfcc28eea247bb20bd06bc81c/jobs+-+approvals+-+jobs%402x.png?expires=1784333700&signature=f88ff85ac0e2fb9e8ba3d8eca36db0f3cf4593503d509debd0726ed1ca518d91&req=dSYgEMp2mYZeXvMW1HO4zXHmQSEo%2BMoKiD4MSKgEP%2FJul0zFX8nz9WVGHckS%0AjImC%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676384717/4a2dfcc28eea247bb20bd06bc81c/jobs+-+approvals+-+jobs%402x.png?expires=1784333700&signature=f88ff85ac0e2fb9e8ba3d8eca36db0f3cf4593503d509debd0726ed1ca518d91&req=dSYgEMp2mYZeXvMW1HO4zXHmQSEo%2BMoKiD4MSKgEP%2FJul0zFX8nz9WVGHckS%0AjImC%0A)

### (2) Bolt Staff Agent Side Panel

* The Bolt Agent icon in the top right corner of the main orange navigation menu displays a yellow notification badge when approvals are waiting.
* Clicking the icon opens the **Staff** **Agent** **side** **panel**, where you can navigate to the **Approvals** **tab** to view and manage items without leaving the page you’re on.
* This option is great for quickly reviewing or clearing approvals while you continue working elsewhere in the platform.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676391695/43b30f677ec848b83a997a855715/CleanShot+2025-08-18+at+15_46_52%402x.png?expires=1784333700&signature=17632c820df0480d4cbec5d78aa733bf9791b25c0f6bab3ba03545c156e1d789&req=dSYgEMp3nIdWXPMW1HO4zYPEOjihhZUo3QmcOwd3FK9GC8nzYVRsiiTEjti5%0AD3E%2F%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676391695/43b30f677ec848b83a997a855715/CleanShot+2025-08-18+at+15_46_52%402x.png?expires=1784333700&signature=17632c820df0480d4cbec5d78aa733bf9791b25c0f6bab3ba03545c156e1d789&req=dSYgEMp3nIdWXPMW1HO4zYPEOjihhZUo3QmcOwd3FK9GC8nzYVRsiiTEjti5%0AD3E%2F%0A)

### (3) Review Tab of Enrollment Details

* If an action within an enrollment requires approval, you’ll see it flagged directly in the **Review** **tab** (explained above).
* From here, you can approve, reject, or provide feedback while also seeing the action’s full details and the agent’s reasoning.

## Reviewing, Editing, + Managing Approvals

When viewing an approval request from the **My Approvals page** or the **Bolt Staff Agent** **side panel**, you’ll see a preview of the action the agent wants to take. This includes:

* The contact the message is for
* The channel(s) being used (email, text, etc.)
* The message draft and specific details

### Available Actions

* **Reject**

  + Clicking **Reject** will discard the action. The agent will not proceed and returns to a monitoring state to determine next steps.
* **Provide** **Feedback**

  + Clicking **Feedback** allows you to send conversational feedback to the agent. After submitting feedback, the agent will re-enter the thinking state, apply your input, and submit a revised action for your approval.
  + Alternatively, you can manually edit the message content for SMS and emails. See the "Manually Edit the Message" bullet below.
* **Approve**

  + Clicking **Approve** confirms the action, and your agent will proceed as proposed.
* **View** **Full** **Details**

  + Clicking **View Full Details** opens the **Reasoning & Feedback** tab in the Action Details sidesheet. This is especially helpful when you’re not ready to approve or reject yet and want to investigate how the agent reached its decision. In this view, you’ll see the agent’s **reasoning** behind the proposed action and a **full breakdown** of the action, including timing, channel, and content details.
  + Note: When approving from the Review tab of Enrollment Details, to provide feedback, you must switch to the Reasoning & Feedback tab to enter your comments.
* **Manually** **Edit** **the** **Message**

  + For email and SMS messages, you have the option to manually edit the text content inline. To edit the text, click into the text box of the proposed subject line or message. You can also highlight text to edit or add formatting.  
    ​

## Bulk Approving, Rejecting, + Feedback

Bulk Approvals make it easy to review and take action on multiple approvals at once, rather than handling them individually. This feature is available from both the **My** **Approvals page** and an **individual agent’s page**.

### Where to Access Bulk Approvals

You can switch to **Bulk View** in two places:

1. **My Approvals page** – View all pending approvals across agents.
2. **Agent page** – View approvals scoped to a single agent (via the “My Approvals” tab).

In either location, use the toggle in the top-right corner to switch between **Single View** and **Bulk View**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1759421816/d669c2440eb98d582c248135b86f/CleanShot+2025-10-03+at+15_44_35%402x.png?expires=1784333700&signature=e856858c6b772f99ca745fdaff684933428830f0b9725c15904fe8c7e5fc2742&req=dSciH818nIleX%2FMW1HO4zUMUKwZKsXeC%2Bd8CQ7e%2BASfBGfrszSAARbHEUuK2%0ATdTik%2B%2FFCHCcvEn%2BFSc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1759421816/d669c2440eb98d582c248135b86f/CleanShot+2025-10-03+at+15_44_35%402x.png?expires=1784333700&signature=e856858c6b772f99ca745fdaff684933428830f0b9725c15904fe8c7e5fc2742&req=dSciH818nIleX%2FMW1HO4zUMUKwZKsXeC%2Bd8CQ7e%2BASfBGfrszSAARbHEUuK2%0ATdTik%2B%2FFCHCcvEn%2BFSc%3D%0A)

### How Bulk Approvals Work

In Bulk View, you can:

* **Select multiple approvals** at once using checkboxes.
* **Approve, reject, or provide feedback** in a single action.
* Review and act on approvals more efficiently, without repeating the same steps for each one.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1759424202/8fe7b778175245e544580498b5c9/CleanShot%2B2025-10-03%2Bat%2B11_00_03.png?expires=1784333700&signature=f5b84c877d0a530486c1115745b480d300060d7a4dbfbd2a8c05d87dcd9d2fcc&req=dSciH818mYNfW%2FMW1HO4zWcrTtLC7g1%2BST4%2Bty7Owexwj%2FspS7wZnX4djKeV%0AEDUJPDbOgfOGnbqyqN8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1759424202/8fe7b778175245e544580498b5c9/CleanShot%2B2025-10-03%2Bat%2B11_00_03.png?expires=1784333700&signature=f5b84c877d0a530486c1115745b480d300060d7a4dbfbd2a8c05d87dcd9d2fcc&req=dSciH818mYNfW%2FMW1HO4zWcrTtLC7g1%2BST4%2Bty7Owexwj%2FspS7wZnX4djKeV%0AEDUJPDbOgfOGnbqyqN8%3D%0A)

🧠 **Good to Know:** Approvers are only notified and see approvals for the jobs they’ve been assigned to.

---

# Managing Enrollments (Add or Remove People)

## Adding Contacts to a Job

After a job has been created, you can continue to manually enroll new people into the job at any time by clicking the **Add People** button in the job header.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676305607/be8beab134e466e7a748f3981184/CleanShot-2B2025-07-09-2Bat-2B15_24_38-402x.png?expires=1784333700&signature=a7aa42876d189d191b74cf6d91177966373960ac2e906193e0e5ad9ea1753da9&req=dSYgEMp%2BmIdfXvMW1HO4zXi2kInEv17dbBh4RfjpW9Ctt1K98X%2FdixzUBHrg%0Ai18A79S52MaNYW%2Fcpfo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676305607/be8beab134e466e7a748f3981184/CleanShot-2B2025-07-09-2Bat-2B15_24_38-402x.png?expires=1784333700&signature=a7aa42876d189d191b74cf6d91177966373960ac2e906193e0e5ad9ea1753da9&req=dSYgEMp%2BmIdfXvMW1HO4zXi2kInEv17dbBh4RfjpW9Ctt1K98X%2FdixzUBHrg%0Ai18A79S52MaNYW%2Fcpfo%3D%0A)

From here, you have the option to add by "**Manual Selection**" or "**Segment**."

### Manual Selection

The manual selection option allows you to search and add individual contacts.

### Via Segment

The segment option allows you to select an existing segment of contacts to enroll.

🚨 **Important Note**: When adding people to a Job **using** **a segment**, the preview list in the *Add People* sheet might appear shorter than expected. Here’s why that may be the case:

* **Visibility Groups:** Some contacts in the segment may be hidden from view due to your visibility group settings. They won’t appear in the preview, but they *will* be added to the Job since the entire segment is included.
* **Already-Enrolled Contacts:** If someone in the segment is already enrolled in the Job, they’ll be excluded from the preview list to prevent duplication, but they will still be counted in the total.

This behavior only affects the ***"Add People"*** sheet, where a preview is displayed. It doesn’t apply during initial Job creation because:

* No contacts have been added yet
* There’s no segment preview at that stage

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676313763/01325b0c1069fe637b49b0d3f3ce/CleanShot-2B2025-07-09-2Bat-2B15_30_03-402x.png?expires=1784333700&signature=d2039b21689eb59f69da6535f81c2b29fed7e4e8db27725db91a90ac6c59728e&req=dSYgEMp%2FnoZZWvMW1HO4zRDHoZ1LpmUmIsNvCfJLp2B%2F1uQ5SI9HomiDUJvm%0AIEqQTJpDulBdluB6F%2Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1676313763/01325b0c1069fe637b49b0d3f3ce/CleanShot-2B2025-07-09-2Bat-2B15_30_03-402x.png?expires=1784333700&signature=d2039b21689eb59f69da6535f81c2b29fed7e4e8db27725db91a90ac6c59728e&req=dSYgEMp%2FnoZZWvMW1HO4zRDHoZ1LpmUmIsNvCfJLp2B%2F1uQ5SI9HomiDUJvm%0AIEqQTJpDulBdluB6F%2Bg%3D%0A)

Not sure if someone made it in? You can always confirm in the **People** tab of the Job after saving.

🧠 **Good to Know:** You can also use the Bolt Agent Jobs profile card to manually enroll a contact in an existing job. If you don't see the profile card, it may need to be enabled for your [profile template](https://help.element451.com/en/articles/10471008-configuring-profile-templates).

## Removing Contacts from a Job

To manually remove a contact from a job:

1. Click the **vertical** **ellipsis** (**⋮**) next to their row.
2. Select **Cancel Job.**

The contact will be removed from the job immediately. The agent will take no further action for that person.

---

# Looking for Additional Guidance?

Check out our article, [Advanced Strategies and Best Practices for Bolt Agent Jobs](https://help.element451.com/en/articles/11128047-advanced-strategies-and-best-practices-for-bolt-agent-jobs), to learn how to layer actions, fine-tune segments, and design jobs that support every stage of the student journey.

---