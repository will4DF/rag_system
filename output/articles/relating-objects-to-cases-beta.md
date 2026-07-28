---
title: Relating Objects to Cases [Beta]
url: https://help.element451.com/en/articles/13772358-relating-objects-to-cases-beta
collection: Case Management (Beta)
---

Learn how to link Alerts, Tasks, Conversations, Appointments, Documents, and Bolt Agent Jobs to a Case so all related work lives in one place.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

One of the most powerful aspects of Cases in Case Management is their ability to act as containers for related work. A Case doesn't replace your existing tools for Tasks, Conversations, Appointments, or Documents—instead, it brings them together in a single view so you can track all the work associated with a student's issue in one place.

This article explains how to link (relate) and unlink objects to and from Cases, and what each type of related object looks like within the Case detail panel.

Cases can relate to the following object types:

* Alerts
* Tasks
* Conversations
* Appointments
* Documents
* Bolt Agent Jobs

🔒 **Permissions & Visibility:** Related objects respect the permissions and visibility groups already configured in Element451. Users will only see related objects they have access to. For example, a user without Conversations permissions will not see any conversations related to a case, even if they have access to the case itself.

---

# How Relating Works

When you relate an object to a Case, you're creating a link between them. The related object keeps its native behavior and remains accessible in its original module (e.g., a Task is still visible in the Tasks module). It simply becomes "case-aware" — visible within the Case detail panel for context and coordination.

🧠 **Good to Know:** An Alert can belong to only one Case at a time. Tasks, Conversations, Appointments, and Documents do not have this restriction.

## How to Relate Objects to a Case

1. **From within the Case**: Using the tabs in the Case detail panel to relate existing objects or create new ones.
2. **Directly from the object's module**: For example, associating a Task with a Case from the task creation or edit form.

Each method is explained in the next sections.

---

# 1) Relating Objects from the Case Detail Panel

Each tab in the Case detail panel (Tasks, Conversations, Appointments, Documents) provides two options for adding related objects:

* **Relate existing** — search for and link an object that already exists in Element451
* **Create new** — create a brand new object and automatically link it to the Case

You can also use the **+ button** in the top right corner of each tab to add objects.

## Alerts (via Information Tab)

Linked Alerts appear in the Information tab of the Case detail panel, in the Alerts section. The table shows each Alert's Name, Type, Due Date, and an action menu.

Alerts are typically linked to Cases through the escalation process (setting an Alert's resolution to "Escalate to Case"). However, you can also manually relate an existing Alert to a Case.

⚠️ **Important:** Each Alert can only be related to **one** Case at a time. You can un-relate an Alert from a Case if you need to re-review or relate it to a different Case.

## Tasks

The Tasks tab displays a table of related Tasks with columns for Task, Reviewer, Due Date, and Status.

From this tab, you can:

* **Relate existing** Tasks that have already been created in the Tasks module
* **Create new** Tasks that are automatically linked to this Case

Related Tasks retain their full functionality in the Tasks module. Changes made in either location are reflected in both.

## Conversations

The Conversations tab shows Conversations linked to this Case. You can relate existing Conversations or create new ones.

This is particularly useful for tracking communications related to the Case — for example, outreach emails, follow-up messages, or check-in threads with the student.

## Appointments

The Appointments tab displays a table of related Appointments with columns for Starts at, Duration, Reviewer, Location, and Status.

Relating Appointments to a Case is helpful for tracking advising sessions, counseling meetings, or other scheduled interactions that are part of the Case work.

## Documents

The Documents tab shows Documents linked to this Case. You can relate existing Documents or upload new ones.

Use this tab to centralize supporting documentation — for example, incident reports, accommodation letters, or academic plans.

## Bolt Agent Jobs

The Jobs tab shows the Bolt Agent Jobs a contact is enrolled in that are related to this Case. A Bolt Agent Job puts an AI agent to work on proactive outreach toward a goal, with staff approving any actions that need a human in the loop. From this tab, you can:

* **Enroll** the contact in a Bolt Agent Job directly from the Case
* **Relate existing** — if the contact is already enrolled in a Job, relate that enrollment to the Case

Contacts can also be enrolled automatically through the **Enroll in Bolt Agent Job** action in Automation Rules or Workflows, and Jobs can start on their own using the **Alert Created** and **Case Created** triggers. For all the ways Bolt works across Case Management, see *Bolt AI in Case Management*; for the job builder itself, see [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job).

---

# 2) Relating Objects Directly from Each Module

You can also relate objects to a Case from within the object's own module. When working with a Task, Conversation, Appointment, or Document, a **Case** field is available to associate it with one of the contact's cases.

⚠️ **Important:** The **Case** field dropdown is scoped to the associated contact's cases only, so you'll only see cases relevant to that student.

## Tasks

You can associate both internal and contact tasks with a Case.

* **New Task**: The **Case** field appears on the task creation form. Use it to associate the task with one of the contact's cases.
* **Existing Task**: The Case field also appears when editing an existing task.

Once linked, the task appears in the **Tasks** tab of the Case detail panel and remains fully accessible in the Tasks module. Changes made in either location are reflected in both.

🧠 **Good to Know:** The Tasks index table includes a **Related Case** column, so you can see at a glance which tasks are associated with a case without opening each one.

## Conversations

* **New Conversation**: The **Case** field is available during conversation creation and from the conversation detail view. Use it to associate a conversation with one of the contact's cases — useful when an outreach thread, follow-up, or check-in is directly tied to an ongoing case.
* **Existing Conversation**: if the contact has an active case, there will be a "Cases" section under the Related tab on the Conversation (right-hand side). Click the plus sign to relate the Case to the Conversation.

Once linked, the conversation appears in the **Conversations** tab of the Case detail panel and remains accessible in the Conversations module.

## Appointments

* New Appointment: The **Case** field is available on the appointment scheduling form. Use it to associate an appointment with one of the contact's cases — helpful for tracking advising sessions, counseling meetings, or other scheduled interactions that are part of the case work.
* Existing Appointment: The Case field also appears when editing an appointment.

Once linked, the appointment appears in the **Appointments** tab of the Case detail panel and remains accessible in the Appointments module.

🧠 **Good to Know:** The Appointments index table includes a **Related Case** column, so you can see at a glance which appointments are associated with a case without opening each one.

## Documents

Documents are associated with a Case from the document detail view. To associate a document with a case:

1. Upload the document first (if it doesn't already exist).
2. Locate the document and click the **More (⋮)** icon, then select **View**.
3. In the document detail view, find the **Case** field, then search for and select the case to associate it.

Once linked, the document appears in the **Documents** tab of the Case detail panel and remains accessible in the Documents module.

---

# How to Remove or Unrelate Object/Case Relationship

Unlinking an object does not delete it—it simply removes the connection to the Case. The object continues to exist in its native module. Here are the ways to unrelate:

1. **From the Case:** Use the action menu (⋮) on the related object's row within the Case detail panel.
2. **From the Object's Module**: When viewing or editing a Task, Conversation, Appointment, or Document, clear the Case field to unlink it from the associated case. For help navigating to the Case field, see the above Relating Objects from the Objects

---