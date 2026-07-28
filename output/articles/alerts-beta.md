---
title: Alerts [Beta]
url: https://help.element451.com/en/articles/13771971-alerts-beta
collection: Case Management (Beta)
---

Learn how to create, triage, and resolve Alerts to flag student risk signals and decide what action to take.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

Alerts in Case Management capture one-time signals that something happened and may require attention. Whether it's a missed class, a grade drop, or a wellbeing concern, Alerts give your team a structured way to triage these signals and decide what action to take.

This article covers everything you need to know about working with Alerts — from creating them to triaging and resolving them.

---

# Alert List Views

When you navigate to Case Management, the Alerts section in the left sidebar provides several pre-filtered views. Each view shows a count badge so you can see at a glance how many items are in that view.

## Triage View (Default)

The Triage view is your default landing page when entering Case Management. **It shows only Alerts in the Triage resolution status** — these are the Alerts that need your attention.

The Triage view displays a stats bar with four key metrics:

* **Need Triage** — the count of Alerts currently in Triage status
* **Overdue** — Alerts past their due date (shown in red)
* **Unassigned** — Alerts with no Reviewer
* **Due Today** — Alerts due today (shown in red if non-zero)

The list table shows columns for:

* Alert Type — name of the alert and link to open the details
* Resolution — the current status of the alert (always triage in this view)
* Reviewer — the assignee responsible to triaging the alert
* Due Date — the assigned date the alert needs to be triaged by

💡 **Note:** The Triage view does not include an Open/Closed toggle like the other views, since it only shows Alerts that still need triage.

## All Alerts and Filtered Views

The remaining Alert views (All Alerts, Unassigned Alerts, Your Alerts, Created by You, and Your Team Alerts) share a similar layout with a few differences from the Triage view:

* **Total Alerts** replaces "Need Triage" in the stats bar
* **Open / Closed toggle** — allows you to switch between open and closed Alerts

## Open vs. Closed Alerts

This toggle allows you filter your view by open or closed Alerts. Below, we list the Alert statuses we use to filter each:

|  |  |
| --- | --- |
| **Open Alerts** | Triage, In Progress, or Escalate to Case |
| **Closed Alerts** | Dismissed, Resolved, or Cancelled |

## Alerts Table

The alerts table (or index) shows you the following columns:

* Alert Name
* Contact (Student)
* Alert Type
* Priority
* Resolution
* Reviewer
* Due Date

Statuses and priorities are customizable in [Alert Settings](https://help.element451.com/en/articles/13772418-alert-settings-closed-beta).

## Row Actions

Click the ⋮ **(more menu)** at the end of any row to access:

* **Edit** — opens the Alert detail slide-over panel
* **Delete** — deletes the Alert

✨ **Pro** **Tip:** Clicking a contact's name in the list opens the Alert details.

---

# Creating a New Alert

## How Alerts Can Be Created

Alerts can enter the system in the following ways:

* **Manually** — using the **+ New Alert** button in Case Management. See **Manual Alert Creation** below.
* **In bulk from the Portal** — Portal users (such as instructors) can select multiple students from their **My Students** list and submit one Alert per selected student in a single action, making it easy to flag the same concern across a roster. See [Portal for Case Management](https://help.element451.com/en/articles/13772401-portal-for-case-management-beta) for the full workflow.
* **Automatically** — using the **Create Alert** action in Workflows and Automation Rules, so Alerts are generated when platform signals or conditions indicate a student may need attention. See [Automating Case Management](https://help.element451.com/en/articles/14712713-automating-case-management-closed-beta).

## Manual Alert Creation

To create a new Alert, click the **+ New Alert** button at the top right of the Case Management page.

This opens a slide-over panel with the following fields:

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Required** |
| **Contact** | Searchable select | No |
| **Alert Type** | Dropdown | Yes |
| **Priority** | Dropdown | Yes |
| **Reviewer** | Searchable select | No |
| **Description** | Text area | No |
| **Due Date** | Date picker | No |

After filling in the required fields, click **Submit** to create the Alert. The Alert will appear in the Triage view by default until it is reviewed and it's resolution status is updated.

---

# The Alert Detail Panel

To view or edit an Alert's details, click the ⋮ **(more menu)** on the Alert's row and select **Edit**. This opens the Alert detail slide-over panel.

The panel header shows the Alert name, the associated contact's avatar and name, and a Submit button to save any changes.

## Resolution Section

The Resolution section contains the fields used for triage and ownership:

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Reviewer** | The staff member responsible for triaging this Alert. Searchable select field. |
| **Due** | The date by which the Alert should be resolved. |
| **Resolution** | The current resolution status (see Triaging Alerts below). |
| **Match to Case** | If the Alert has been escalated, shows the linked Case along with the Case's **current status** (read-only). The Case chip is clickable and opens the Case detail side-sheet, so you can review the linked Case without leaving the Alert. The linked Case's current status is also surfaced on the alerts index for escalated Alerts. |

## Information Section

The Information section contains the core details of the Alert:

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Alert Type** | The category of the Alert (based on your configured Alert Types). |
| **Priority** | The urgency level — Critical, High, Medium, Low, or a custom priority. |
| **Related Course** | If the Alert Type has Course Related enabled, shows the associated course. |
| **Description** | Free-text notes providing context about the Alert. |

## Internal Notes Section

The Discussion section allows you and your team to collaborate on the Alert through comments. Type a note in the text area and click Add Comment to post it. Comments are visible to anyone who has access to the Alert.

---

# Triaging Alerts

Triaging is the core workflow for Alerts. When an Alert comes in, a Reviewer evaluates it and decides on the appropriate action. Alerts do not expire.

## Resolution Options

When triaging an Alert, you can set the Resolution to one of the following:

|  |  |
| --- | --- |
| **Resolution** | **Description** |
| **Triage** | The default status assigned to all new alerts when they enter the system.    *Note: Triage is a system-applied status and cannot be manually selected. Once an alert's status has been updated to any other resolution, it cannot be reverted back to Triage.* |
| **In Progress** | The Alert is being actively reviewed or worked on, but not yet resolved. |
| **Resolved** | The concern has been addressed and no further action is needed. |
| **Dismissed** | The Alert was reviewed and determined not to require action (e.g., false positive, duplicate). |
| **Escalated to Case** | The Alert requires deeper, ongoing follow-up. This creates or links the Alert to a Case. |

## Escalating to a Case

When you update an alert's status to **Escalated to Case**, a case association is not required at the time of the status change. To fully connect the alert to a case, you'll need to manually select an existing case or create a new one in the **Match to Case** field. Until a case is linked, the alert will remain in **Escalated to Case** status without a related case.

### Important Notes

* If a related alert is removed from within a case, the alert's status will remain **Escalated to Case**. You'll need to manually update the alert's status.
* Similarly, when a case is marked as **Resolved**, the statuses of any related alerts are not automatically updated. If an alert is in **Escalated to Case** status and its linked case is resolved, the alert will remain in **Escalated to Case** until it is manually updated to reflect the resolution. The linked Case's current status is now displayed on the Alert (in the **Match to Case** field and on the alerts index), so you can see at a glance when the Case has moved to Resolved or Cancelled even though the Alert's own status hasn't changed.

---

# Alerts Profile Card

You can add an Alerts card to your contact profile templates so that when viewing a student’s profile, you have quick access to all of their Alerts without needing to navigate to the Case Management module. This is a great way to get a snapshot of a student’s alert history during advising sessions or check-ins.

For guidance on adding profile cards to templates, check out the [Configuring Profile Templates help article](https://help.element451.com/en/articles/10471008-configuring-profile-templates).

⚠️ **Important:** The Alerts profile card must be placed in a two-column or three-column width layout. One-column is not supported.

---