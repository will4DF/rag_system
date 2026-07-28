---
title: Automating Case Management [Closed Beta]
url: https://help.element451.com/en/articles/14712713-automating-case-management-closed-beta
collection: Case Management (Beta)
---

An overview of the two automation engines for Alerts and Cases — the Workflows + Rules module and dedicated Automation Rules — and when to use each.

## 🚀 Case Management is Coming Soon!

This feature is currently in Closed Beta and limited to select partners. We'll keep you in the loop as we work toward a wider release.

# Overview

Case Management supports two complementary automation systems:

1. The first connects Case Management to Element451's **Workflows and Rules** module, enabling communications, cross-module actions, and engagement journeys triggered by Alert and Case activity.
2. The second is a dedicated **Automation Rules** engine built specifically for Alert and Case handling—routing records, assigning staff, escalating signals, and creating follow-up work automatically at the moment of creation.

Together, they cover both the operational and the relational sides of automation. They are not mutually exclusive—Automation Rules can enroll a contact in a Workflow as one of their actions, so you can use Rules for routing and Workflows for the resulting student communication.

This article walks through both engines and then compares them side-by-side so you know when to use each.

---

# Workflows Module

Case Management is integrated into Element451's Workflows and Rules module—meaning alert and case activity can both **trigger** automated workflows and be **created by** them. This allows your team to build fully automated intervention pipelines around student risk signals.

## Triggers

Triggers enroll contacts into a Workflow when a specific event occurs. The following triggers are available for Case Management:

### Alert Created

Enrolls a contact into a Workflow when a new alert is created for them. You can configure which alert types or priorities should trigger enrollment, allowing you to route different alerts to different workflows.

### Case Created

Enrolls a contact into a Workflow when a new case is created for them. Use this to kick off onboarding workflows for the case — such as sending a welcome communication to the student, notifying subscribers, or creating initial tasks for the assigned staff member.

### Alert Status Updated

Enrolls a contact into a Workflow when the status of one of their alerts changes. This trigger fires only on a status change, not on other edits to the alert, and supports scoping conditions such as alert priority and status, so you can target specific transitions (for example, an alert moving into In Progress or Escalated to Case).

### Case Status Updated

Enrolls a contact into a Workflow when the status of one of their cases changes. Like the alert version, it fires only on a status change, not on broad case updates, and supports scoping conditions such as case type, priority, and status.

### Joined Segment

Enrolls a contact into a Workflow the moment they enter a segment. When combined with a segment built from alert or case filter properties, this trigger enables population-based automation that responds to changes in a student's alert or case status over time.

## Actions

Actions are steps within a Workflow or Rule that create or modify records. The following actions are available for Case Management, and can be used with *any* trigger—not just alert and case triggers.

### Create Alert

Creates a new alert for the enrolled contact as a step in a Workflow or Rule. Use this to automatically generate alerts when other platform signals indicate a student may need attention — even if no one manually flagged them.

### Create Case

Creates a new case for the enrolled contact as a step in a Workflow or Rule. Use this to automatically open accountable work records when a trigger condition is met, ensuring no at-risk student falls through the cracks because a case was never opened.

[Getting Started with Workflows + Rules →](https://help.element451.com/en/articles/1500265-getting-started-with-workflows-rules)

---

# Automation Rules

Automation Rules are a dedicated, trigger-based automation engine built specifically for Case Management. They let you handle routine Alert and Case work automatically — instead of manually assigning reviewers, setting priorities, escalating to Cases, or creating follow-up Tasks, you can build rules that fire as soon as an Alert or Case is created and apply the actions you choose.

Every rule follows the same pattern—**Trigger → Conditions → Actions**. The Trigger fires the rule (today, that's "Alert Created" or "Case Created"). Conditions narrow which records the rule applies to. Actions are what the rule does when those conditions are met. You can stack multiple conditions and multiple actions on a single rule.

Alerts and Cases each have their own Automation Rules page, with vocabulary and capabilities scoped to that record type.

## Where to Find Automation Rules

Automation Rules live inside Case Management Settings, with separate pages for Alerts and Cases.

1. Navigate to **Engagement > Case Management**.
2. Click the **⋮ (more menu)** at the top right of the page and select a settings option to open **Case Management Settings**.
3. In the settings sidebar, expand **Alerts** or **Cases**, then click **Automation Rules**.

📌 **Note:** Alert rules and Case rules are configured independently. A rule you build on the Alerts page does not affect Cases, and vice versa. For configuring the underlying Alert and Case fields these rules act on, see [Alert Settings](https://help.element451.com/en/articles/13772418-alert-settings-closed-beta) and [Case Settings](https://help.element451.com/en/articles/13775536-case-settings-closed-beta).

## The Rules List

Both Automation Rules pages share the same layout. The list shows every rule you've created for that record type.

### Columns

|  |  |
| --- | --- |
| **Column** | **Description** |
| **Name** | The rule's name (set in the side sheet Title field). |
| **Description** | Free-text description from the side sheet; shows **—** if empty. |
| **Actions** | Comma-separated summary of every action configured on the rule (e.g., *Update Reviewer, Update Resolution*). |
| **Last Updated** | When the rule was last edited. |
| **Enabled** | Inline toggle to switch the rule on or off without opening it. |

### Creating a new rule

Two entry points open the same rule side sheet:

* The **+** icon button at the top right of the table
* The **+ Add Rule** button at the bottom of the list

### Row actions

Click the **⋮ (more menu)** at the end of any rule's row to:

* **Edit** — open the rule in the side sheet
* **Delete** — remove the rule

## Creating a Rule

Clicking **+**, **+ Add Rule**, or **Edit** opens a side sheet that takes up most of the screen. The side sheet is structured top to bottom around the same pattern: **Title → Settings → Trigger → Conditions → Actions**.

### 1. Title

At the top of the side sheet, the **Title** field defaults to **Alert Rule** on the Alerts page or **Case Rule** on the Cases page. Click into the field and replace the default with a descriptive name (for example, "Auto-assign high-priority attendance alerts"). This is the name shown in the rules list.

### 2. Settings

* **Enabled** — Toggle that controls whether the rule runs. On by default. You can also flip this from the list view without opening the rule.
* **Description** — Optional free-text field for explaining what the rule does. Shows in the **Description** column on the list view (or **—** if empty).

### 3. Trigger

The **Trigger** field is prefilled and read-only:

* On the Alerts page: **Alert Created**
* On the Cases page: **Case Created**

This means each rule evaluates whenever a new Alert or Case is created. No other trigger options are available today.

### 4. Conditions

Conditions are optional filters that narrow which records the rule applies to. If you add no conditions, the rule applies to every Alert or Case that fires the trigger.

To add a condition, click **+ Add Condition** and pick a condition type from the menu (see the **Conditions Reference** below). You can stack multiple conditions on a single rule.

### 5. Actions

Actions are what the rule does when its trigger fires and its conditions are met.

To add one, click **+ Add Action**. Each action renders as its own card with an **Action** dropdown at the top, action-specific fields below, and a trash icon to remove it. You can add multiple actions to a single rule—they appear comma-separated in the **Actions** column on the list view. See the **Actions Reference** below for the full list.

### 6. Save

Click **Save** at the top right of the side sheet to commit the rule. **Save** stays disabled until required fields are filled in (Title, at least one valid Action, plus any required fields on each action—such as a **Due Date** on **Update Due Date**). Click the **X** at the top left to close the side sheet without saving.

## Conditions Reference

The condition types available depend on whether you're on the Alerts or Cases page.

### Alert Conditions

|  |  |
| --- | --- |
| **Condition** | **What it does** |
| **Segment Reference** | Apply the rule only when the Alert's contact matches an existing saved segment. |
| **Segment Builder** | Build an inline segment in place instead of referencing a saved one. |
| **Date Condition** | Filter on a date field or relative date. |
| **Alert Property** | Filter on the Alert's own fields (Type, Priority, Reviewer, etc.). |

### Case Conditions

|  |  |
| --- | --- |
| **Condition** | **What it does** |
| **Segment Reference** | Apply the rule only when the Case's contact matches an existing saved segment. |
| **Segment Builder** | Build an inline segment in place instead of referencing a saved one. |
| **Date Condition** | Filter on a date field or relative date. |
| **Case Property** | Filter on the Case's own fields (Type, Priority, Status, Assignee, etc.). |
| **Related Alert** | Branch the rule on properties of an Alert linked to the Case. |

🧠 **Good to Know:** When you stack multiple conditions on a rule, all of them must be true for the rule to apply.

## Actions Reference

Different actions are available on each page, reflecting the different fields available on Alerts vs. Cases.

### Alert Actions

|  |  |
| --- | --- |
| **Action** | **What it does** |
| **Update Reviewer** | Assign a Reviewer. Supports **Selected**, **Rotational**, or **Balanced** assignment across users, teams, the Contact's Assignee, or a Network Role (see Assignment Behavior below). |
| **Update Priority** | Change the Alert's priority. |
| **Update Resolution** | Update the Alert's resolution status. |
| **Update Due Date** | Set or update the Alert's due date—either an exact date or a number of days from when the rule runs. |
| **Create Case** | Spin up a new Case from the Alert. The action now exposes the full set of Case fields—Case Name, Assignee, Subscribers, Due Date, Privacy, Description, and Case Template—matching what you can set when creating a Case manually. Assignee and Subscribers also accept the Contact Assignee and Network Role tokens. |
| **Enroll in Workflow** | Enroll the Alert's contact in a Workflow. |
| **Enroll in Bolt Agent Job** | Trigger a Bolt Agent Job for the Alert. |

### Case Actions

|  |  |
| --- | --- |
| **Action** | **What it does** |
| **Update Assignee** | Assign an owner. Supports **Selected**, **Rotational**, or **Balanced** assignment across users, teams, the Contact's Assignee, or a Network Role (see Assignment Behavior below). |
| **Update Priority** | Change the Case's priority. |
| **Update Status** | Move the Case to a different status. |
| **Update Type** | Change the Case Type. |
| **Update Due Date** | Set or update the Case's due date—either an exact date or a number of days from when the rule runs. |
| **Add Subscriber** | Add a Subscriber to the Case. |
| **Remove Subscriber** | Remove a Subscriber from the Case. |
| **Mark as Private** | Mark the Case as Private. |
| **Create Task** | Create a Task linked to the Case. The action supports both internal and contact tasks, along with subtasks, subscribers, and Task Templates, mirroring the Create Task action in Workflows. |
| **Enroll in Workflow** | Enroll the Case's contact in a Workflow. |
| **Enroll in Bolt Agent Job** | Trigger a Bolt Agent Job for the Case. |

## Assignment Behavior

When you add an **Update Reviewer** action on the Alerts page or an **Update Assignee** action on the Cases page, you'll see an **Assignment Behavior** dropdown with three options. This controls how the rule chooses among the users or teams you've selected in the **Reviewer** / **Assignee** field.

|  |  |
| --- | --- |
| **Behavior** | **What it does** |
| **Selected** *(default)* | Assigns to the specific user(s), team(s), Contact Assignee, or Network Role chosen. |
| **Rotational** | Rotates assignment across the chosen pool, one record at a time, in order. |
| **Balanced** | Balances load across the chosen pool, sending each new record to whoever currently has the lightest open workload. |

🔁 **Dynamic assignment tokens:** Beyond specific users or teams, the Reviewer/Assignee field supports two tokens that resolve *per record* based on the student:

* **Contact Assignee** — assigns to whoever owns the contact in Element451.
* **Network Role** — assigns to whoever holds a given network role for that student. For example, routing a grade alert to that student's **Academic Advisor**, or a financial case to their **Financial Aid Counselor**.

Because these resolve dynamically, one rule routes every record to the right person without naming individuals. See [Network: Connect Contacts with Internal Users](https://help.element451.com/en/articles/9884014-network-connect-contacts-with-internal-users) to set up roles.

✨ **Pro Tip:** Use **Balanced** when you have a team that should share work evenly. Use **Rotational** when you want round-robin assignment regardless of current load.

## Editing, Enabling, and Deleting Rules

* **Edit** — Click the rule row's **⋮ (more menu)** and choose **Edit** to reopen the side sheet.
* **Enable / Disable** — Flip the **Enabled** toggle in the list view to pause or resume a rule without losing its configuration.
* **Delete** — Click the rule row's **⋮ (more menu)** and choose **Delete**.

🚨 **Important:** Deleting a rule cannot be undone. If you want to pause a rule temporarily, disable it instead.

## Examples

### Auto-assign new high-priority alerts to a specific reviewer

Create an Alert rule with a single **Alert Property** condition (*Priority = High*) and an **Update Reviewer** action set to your advising lead. Every new high-priority Alert will be assigned automatically.

### Route alerts to each student's Academic Advisor

Create an Alert rule with an **Update Reviewer** action and set the Reviewer to the **Network Role** token for *Academic Advisor*. Each new Alert is assigned to whoever holds that role for the student—no need to name individuals or build a rule per advisor.

### Escalate alerts for first-year students to a Case

Create an Alert rule and combine a **Segment Reference** condition (*First-Year Students*) with a **Create Case** action. Alerts for that population will spin up a Case automatically.

### Set a 7-day due date on new advising cases

Create a Case rule, add a **Case Property** condition (*Type = Advising*), and an **Update Due Date** action with **Due Days = 7**.

### Distribute incoming cases evenly across the advising team

Create a Case rule, add an **Update Assignee** action, set **Assignment Behavior = Balanced**, and choose your advising team. Each new Case will go to whichever team member has the lightest workload.

---

# Bolt Agent Job Triggers

Beyond the **Enroll in Bolt Agent Job** action described above, a Bolt Agent Job can also enroll contacts on its own. The job builder includes built-in **Alert Created** and **Case Created** triggers, so a Job pulls in any contact who gets a qualifying alert or case—no Automation Rule or Workflow required.

Use a Job trigger when the enrollment logic belongs to the Job itself. Use the **Enroll in Bolt Agent Job** action in Automation Rules or Workflows when enrollment is one step in a larger routing or communication flow. No matter which path enrolls the contact, the Job enrollment is automatically related to the Case and appears on its **Jobs** tab.

For the full trigger list and setup, see [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job). For all the ways Bolt works across Case Management, see [Bolt AI in Case Management](https://help.element451.com/en/articles/15465010-bolt-ai-in-case-management-closed-beta).

---

# When to Use Each Engine

Both tools can automate actions when an Alert or Case is created, but they serve different purposes.

Automation Rules and Workflows + Rules are not mutually exclusive — Automation Rules can enroll a contact in a Workflow as one of their actions, so you can use Rules for routing and Workflows for the resulting student communication, all triggered by the same event.

## Side-by-Side Comparison

|  |  |  |
| --- | --- | --- |
|  | **Automation Rules** | **Workflows** |
| **Best for** | Routing and handling alerts/cases—assignment, prioritization, escalation, task creation | Cross-platform automation—student communications, creating alerts/cases from external signals |
| **Configured in** | Case Management Settings > Alerts/Cases > Automation Rules | Data + Automations > Automations |
| **Triggers** | Alert Created, Case Created | Alert Created, Case Created, Alert Status Updated, Case Status Updated, Joined Segment, form submissions, and more |
| **Actions** | Update reviewer/assignee (Selected, Rotational, or Balanced; supports Contact Assignee and Network Role tokens), priority, status, type, resolution, due date; add/remove subscribers; mark private; create case or task; enroll in Workflow or Bolt Agent Job | Send communication, create alert or case, update contact properties, enroll in Workflow, execute webhook, and more |

## Choosing Where to Build

|  |  |
| --- | --- |
| **Use Case** | **Recommended Approach** |
| **Auto-assign reviewers based on Alert type or student segment** | Automation Rules |
| **Route alerts or cases to each student's network role (e.g., Academic Advisor)** | Automation Rules |
| **Auto-escalate Alerts to Cases when conditions are met** | Automation Rules |
| **Auto-assign Cases to specific teams based on type** | Automation Rules |
| **Create follow-up Tasks when a new Case is created** | Automation Rules |
| **Trigger a Bolt Agent Job when a Case is created** | Automation Rules |
| **Coordinate Case actions with email campaigns or other platform workflows** | Workflows + Rules module |

---