---
title: Bolt Analysis for Cases [Beta]
url: https://help.element451.com/en/articles/15265836-bolt-analysis-for-cases-beta
collection: Case Management (Beta)
---

An AI-powered briefing on every case—what's happening, what matters about the student, and what to do next.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

**Bolt Analysis** is a persistent, AI-generated briefing that lives on every **Case**. It reads the case and the student's record, then summarizes what's happening, what matters, and what to do next—so you can walk into any case with context already on the page. And because the recommended next steps are **actionable**, you can act on them right from the panel and move the case forward without ever leaving it.

You don't have to ask for it. Bolt Analysis is generated automatically when the case is created and refreshes as the case evolves.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2451470862/15ddcc2816859170a01b2f6fc708/Bolt+AI+Analysis+for+Cases.png?expires=1784333700&signature=6db231c925781c6b9b4b7b34727204a9894d1bd3b5915c0966f92d3ed055ce77&req=diQiF815nYlZW%2FMW1HO4zUWs%2F0p6xWRS8YEoutfsc4HDO5%2BscTzJCCv0xP2o%0A9W1l2FPjzo5PeoVQHTA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2451470862/15ddcc2816859170a01b2f6fc708/Bolt+AI+Analysis+for+Cases.png?expires=1784333700&signature=6db231c925781c6b9b4b7b34727204a9894d1bd3b5915c0966f92d3ed055ce77&req=diQiF815nYlZW%2FMW1HO4zUWs%2F0p6xWRS8YEoutfsc4HDO5%2BscTzJCCv0xP2o%0A9W1l2FPjzo5PeoVQHTA%3D%0A)

---

# Where You'll See It

Open any Case and go to the **Information** tab. Bolt Analysis appears as its own section near the top of the tab, above the case description and notes.

Each analysis shows a **Last updated** timestamp and a **Re-run** button in the top right corner of the card, so you can see how fresh the briefing is and force a re-evaluation if needed.

---

# What's in the Analysis

Every Bolt Analysis is structured into the same three sections, in the same order, so you always know where to look.

## Case Summary

A short, plain-language read on **what's happening with this case right now**—not a full history. It leads with the most relevant signal: progress made, what's still pending, an overdue task, an upcoming appointment, or the fact that nothing has happened in a while.

Expect one to three sentences. The goal is for you to know the state of the case before you scroll.

Directly below the summary, a **Show reasoning** toggle lets you expand Bolt's underlying reasoning inline. Toggle it on to reveal the reasoning, and off to collapse it again—no separate sidesheet to open.

## Student Context

The signals from the student's record that matter **for this specific case**. Not a profile dump—just the things that change how you should approach the work.

Depending on the case and what data is available, this can include engagement signals, recent platform activity, holds, academic standing, other open alerts or cases on the student, sentiment from recent conversations, or relevant staff notes. Signals are surfaced only if they're meaningfully connected to the case.

## Recommended Next Steps

Between one and four specific, prioritized suggestions for moving the case forward. **Steps are numbered** to communicate the recommended order. Each step states what to do and maps to a specific action type in Element451. Available action types include Change Status, Start Conversation, Create Contact Task, Create Internal User Task, Schedule Appointment, Have Agent Call Student, Relate Existing Item, Add Case Note, Create Alert, and Enroll in Bolt Agent Job.

Recommendations are tailored to the current state of the case—what's been tried, what's worked, and what hasn't.

### See why Bolt suggested a step

Each step is collapsed by default. Click the chevron on the right of a step to expand it and read Bolt's reasoning for that specific recommendation—why it fits the case right now. Click the chevron again to collapse it.

[![Expanded Next Steps showing Bolt's per-step reasoning](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2451470862/15ddcc2816859170a01b2f6fc708/Bolt+AI+Analysis+for+Cases.png?expires=1784333700&signature=6db231c925781c6b9b4b7b34727204a9894d1bd3b5915c0966f92d3ed055ce77&req=diQiF815nYlZW%2FMW1HO4zUWs%2F0p6xWRS8YEoutfsc4HDO5%2BscTzJCCv0xP2o%0A9W1l2FPjzo5PeoVQHTA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2451470862/15ddcc2816859170a01b2f6fc708/Bolt+AI+Analysis+for+Cases.png?expires=1784333700&signature=6db231c925781c6b9b4b7b34727204a9894d1bd3b5915c0966f92d3ed055ce77&req=diQiF815nYlZW%2FMW1HO4zUWs%2F0p6xWRS8YEoutfsc4HDO5%2BscTzJCCv0xP2o%0A9W1l2FPjzo5PeoVQHTA%3D%0A)

### Take action directly from the panel

Recommended Next Steps are **actionable**, so you can move a case forward without ever leaving it. Every step has its own action button plus a **Dismiss** button, and the action button's label reflects the action type:

* **Change Status** → **Update**
* **Start Conversation** → **Send**
* **Create Contact Task** → **Create**
* **Create Internal User Task** → **Create**
* **Schedule Appointment** → **Schedule**
* **Have Agent Call Student** → **Call**
* **Relate Existing Item** → **Relate**
* **Add Case Note** → **Add**
* **Create Alert** → **Create**
* **Enroll in Bolt Agent Job** → **Enroll**

### How actions execute

How an action runs depends on whether it needs more detail from you. Where possible, Bolt prefills the resulting form with values drawn from the analysis, and anything it can't confidently fill is left empty for you to complete.

* **Actions that need details open a side sheet.** Steps such as Start Conversation, Create Contact Task, and Add Case Note open a side sheet so you can review and complete the details before the action executes. Bolt hands off a **starting draft built from the analysis context**—a suggested message for a conversation, or a description for a task—so you begin with a working draft instead of a blank field. Edit anything you like before you send or save.
* **Create Internal User Task** opens the internal task side sheet to create a task for a staff member (rather than for the contact).
* **Schedule Appointment** opens the appointment scheduling side sheet with the student and case pre-set, so the appointment is automatically related to this case.
* **Have Agent Call Student** starts a one-off Bolt Agent phone call to the student.
* **Relate Existing Item** opens the relate-item side sheet so you can link an existing Task, Conversation, Appointment, Document, or Course to the case.
* **Create Alert** opens the new alert side sheet with a prefilled title and description.
* **Change Status executes immediately.** Clicking **Update** on a Change Status step applies the new status right away, with no additional confirmation.
* **Enroll in Bolt Agent Job opens the job enrollment flow with the case relationship pre-set.** Choose the Bolt Agent Job and confirm to enroll the contact. Because the case relationship is already set, the enrollment is automatically related to this case and appears on the case's **Jobs** tab.

⚠️ **Important:** Because **Change Status** takes effect immediately, be mindful of any automation triggered by a status change. If you have Automation Rules or Workflows that fire when a case enters a status (for example, moving to **In Progress**), updating the status from Bolt Analysis will trigger them just as a manual status change would.

### Completed and dismissed steps

* **Completed:** Once you take an action, the step is marked complete with a green check, so you can see at a glance what has already been handled. After you save, you're always returned to the Information tab where Bolt Analysis lives—you aren't navigated out to Tasks, Conversations, or Appointments.
* **Dismissed:** Click **Dismiss** to clear a recommendation you don't intend to act on. Dismissing only removes the suggestion from the list; it does not change the case.

📙 **Note:** When the analysis regenerates—automatically or from a manual **Re-run**—the Recommended Next Steps are rebuilt for the case's current state. Steps you already **completed or dismissed will no longer appear** in the refreshed list. Anything you created from a step (a task, conversation, or note) still lives on the case in its respective tab as a related object; only the suggestion is cleared from the list.

---

# How the Analysis Adapts to the Case

Bolt Analysis is **phase-aware**. It changes what it emphasizes based on how mature the case is, because a brand-new case and a stalled case need very different briefings.

## Initial (just created)

Applies when a case was created **less than 24 hours ago** and has had **fewer than 2 activity events**.

* **Case Summary** restates what triggered the case and the case type.
* **Student Context** does the heavy lifting—pulling in the student's profile so you understand who you're working with before taking action.
* **Recommended Next Steps** are "get started" oriented: first outreach, an introductory task, a meeting.

## Active (work is in progress)

Applies when the case has activity and the **last activity was less than 7 days ago**.

* **Case Summary** leads with progress: what's been done, what's pending, what's still open.
* **Student Context** shifts toward what's changed *since* the case opened—new alerts, updated engagement, appointment outcomes, recent conversations.
* **Recommended Next Steps** respond to outcomes: what worked, what didn't, what should happen next.

## Stale (no recent activity)

Applies when the **last activity was 7 or more days ago**.

* **Case Summary** leads with the staleness signal—"no activity in X days" is the headline.
* **Student Context** highlights what changed *outside* the case while it sat idle.
* **Recommended Next Steps** focus on re-engagement, escalation, or—if the underlying issue appears to have resolved itself—closing the case.

---

# What Data Bolt Analysis Considers

Bolt Analysis pulls from data that's already in Element451. **What shows up in the briefing depends on what's available for that case and student**—a case with no related conversations won't get a conversation summary, and a student without LMS data won't get grade signals.

## Core data (always considered)

* **The case itself** — type, status, priority, assignee, due date, description, days since last activity
* **Related work** — tasks, conversations, appointments, documents, and alerts linked to the case
* **Active Bolt Agent Job enrollments** — the contact's current job enrollments and their statuses (for example pending, scheduled, thinking, taking action, waiting for approval, or completed)
* **Student profile** — engagement score, last platform activity, preferred contact time, active term, campus, major, student type
* **Holds** — type and subtype
* **Other open alerts and cases** on the same student
* **History** — past alerts and cases for pattern context
* **Email engagement** — opens, clicks, last delivered
* **Conversation history** — sentiment, confusion signals, channels used
* **Appointment history** — outcomes, attendance, no-show patterns
* **Non-private staff notes**
* **Custom field values** — surfaced only when relevant to the case

## Integration-dependent data (when connected)

If your institution has an LMS or SIS integration, Bolt Analysis also considers:

* **Course grade and risk** — current numeric and letter grade, risk level, risk codes
* **Grade trend** — velocity, change from peak, consecutive decline streak, below-passing flag
* **Attendance** — total absences, last attended date
* **LMS activity** — last LMS activity timestamp, per-course engagement
* **Enrollment status** per course

If these data sources aren't connected, the briefing simply omits them—it doesn't guess.

---

# When the Analysis Refreshes

Bolt Analysis isn't real-time. It's evaluated on specific triggers and cached between them, so the briefing stays consistent until something meaningful changes.

📙 **Note**: Load times may vary at the moment and you may need to close out of the side-sheet and reopen it for the refreshed analysis to render.

## Automatic refresh triggers

The analysis re-runs when the **facts of the case change**—not every time someone interacts with it. Triggers include:

* A new alert is related to the case
* A task on the case is completed
* An appointment is completed or marked as a no-show
* The case status moves to **In Progress**
* The case assignee changes
* An inbound conversation arrives from the student

In addition, all active cases re-evaluate **once every 24 hours** so the analysis can catch "nothing has happened" patterns.

📙 **Note:** Some events intentionally do *not* trigger a refresh—priority changes, subscriber updates, internal comments, and outbound messages from staff. These don't change the underlying picture of the case.

## Manual re-run

You can force a re-evaluation at any time by clicking **Re-run** in the top right corner of the Bolt Analysis card. Manual re-runs are rate-limited to **once every 3 hours per case**.

---

# FAQ

#### Does Bolt Analysis run on every case?

Yes. Every case in Case Management has Bolt Analysis on its Information tab. Resolved and cancelled cases don't continue to re-evaluate.

#### Can students see Bolt Analysis?

No. Bolt Analysis is a staff-only briefing. It does not appear on student-facing surfaces and is not used to generate student messages.

#### Can I undo an action I took from a Next Step?

Actions taken from Bolt Analysis behave exactly like the same action taken anywhere else in Element451. A status change applies immediately and can be changed again manually; a conversation, task, or note is created once you complete and submit its side sheet. There is no single "undo" for a completed step, so review the details before you confirm—especially for Change Status, which executes right away.

#### Why don't I see academic data in the briefing?

Academic and course data only appears if your institution has an LMS or SIS integration connected and data is available for the student on the case. If you expect that data to be present but it isn't, check with your administrator about your integration setup.

#### Why does the analysis look the same after I added a comment?

Internal comments don't change the underlying facts of the case, so they don't trigger a re-evaluation. If you want a fresh briefing, click **Re-run** in the top right corner of the Bolt Analysis card.

---