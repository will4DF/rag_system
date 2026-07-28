---
title: Cases [Beta]
url: https://help.element451.com/en/articles/13772190-cases-beta
collection: Case Management (Beta)
---

Learn how to create, manage, and resolve Cases that track ongoing student work across Tasks, Conversations, Appointments, and Documents.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

Cases in Case Management represent the ongoing work your staff do to help a student resolve an issue. While Alerts capture a moment-in-time signal, Cases are the system of record for everything that happens next — from assigning ownership to tracking progress across Tasks, Conversations, Appointments, and Documents.

This article covers everything you need to know about working with Cases — from creating them to managing their lifecycle through resolution.

---

# Case List Views

The Cases section in the left sidebar provides pre-filtered views to help you manage your workload. Each view shows a count badge.

|  |  |
| --- | --- |
| **View** | **What It Shows** |
| **All Cases** | All cases across the organization, with no filters applied |
| **Your Cases** | Cases where you are the assigned owner |
| **Created by You** | Cases you created |
| **Your Team Cases** | Cases assigned to any member of your team |
| **Subscribed Cases** | Cases you are subscribed to |

## Stats Bar

Each Case view displays a stats bar with four key metrics:

* **Total Cases** — the total count of cases in the current view
* **Critical** — count of cases with Critical priority (shown in red)
* **Overdue** — cases past their due date (shown in red)
* **Due Today** — cases due today (shown in red if non-zero)

## Cases Table

The cases table (or index) shows you the following columns:

* Case Name
* Contact (Student)
* Case Type
* Priority
* Status
* Assignee
* Due Date

Statuses and priorities are customizable in [Case Settings](https://help.element451.com/en/articles/13775536-case-settings-closed-beta).

## Row Actions

Click the ⋮ **(more menu)** at the end of any row to access:

* **Edit** — opens the Case detail slide-over panel
* **Delete** — deletes the Case

✨ **Pro** **Tip:** Clicking a Case type (name) in the list navigates you to the Case Details.

---

# Creating a New Case

Cases can enter the system in the following ways:

* **Manually by staff** — using the + New Case button in Case Management
* **From an Alert** — when an Alert status is changed to "Escalated to Case," you can create a new case to be linked

🚧 **Coming Soon:** Additional methods for creating alerts, including automated creation via Workflows are currently in development. Stay tuned!

📌 **Note:** Cases can be created with or without an originating Alert. Not every Case needs to come from an Alert.

## Manual Case Creation

To create a new Case, click the **+ New Case** button at the top right of the Case Management page.

This opens a slide-over panel with the following fields:

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Required** |
| **Contact** | Searchable select (individual or team) | Yes |
| **Case Type** | Dropdown | Yes |
| **Priority** | Dropdown | Yes |
| **Assignee** | Searchable select | Yes |
| **Due Date** | Date picker | No |
| **Subscribers** | Searchable select (individual or team) | No |
| **Private** | Toggle (default: No) | No |

After filling in the required fields, click **Create** to create the Case.

## From an Alert

When an Alert status is changed to "Escalated to Case," you can link an existing case or create a new case to be linked.

---

# The Case Detail Panel

To view or edit a Case's details, click the ⋮ **(more menu)** on the Case's row and select **Edit**. This opens the Case detail slide-over panel — the richest view in the module.

## Header Fields

The panel header always displays key information about the Case. These fields are visible at all times, regardless of which tab you're on:

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Contact** | The student associated with this Case. Displayed with avatar and name; links to the contact's profile. |
| **Type** | The Case Type (based on your configured Case Types). |
| **Priority** | The urgency level, displayed as a colored badge. |
| **Status** | The current status, selected from a grouped dropdown (see Case Statuses below). |
| **Assignee** | The staff member or team assigned to own this Case. |
| **Due Date** | Optional due date for the Case. |
| **Private** | Toggle to mark this Case as private (see Case Privacy below). |

## Mark as Complete

At the top right of the Case detail panel, you'll find the **Mark as complete** dropdown button. Clicking it reveals all statuses that belong to the **Resolved** system status group (e.g., "Resolved"). Selecting one moves the Case to a resolved state.

## Case Statuses

Cases use a two-tier status system: fixed Status Groups with custom statuses layered on top.

### Status Groups

Every Case status maps to one of four system-level Status Groups:

|  |  |
| --- | --- |
| **Status Group** | **Meaning** |
| **To Do** | The Case is pending and has not been started yet. |
| **In Progress** | The Case is actively being worked on. |
| **Resolved** | The Case has been completed. Statuses in this group appear in the Mark as complete dropdown. |
| **Cancelled** | The Case was closed without resolution. |

Your administrator can create custom statuses within each group (e.g., "Waiting on Student" under In Progress, or "Referred to External" under Resolved). At least one custom status must exist in each group. [Learn more in Case Settings](https://help.element451.com/en/articles/13775536-case-settings-closed-beta).

When changing a Case's status, the dropdown groups custom statuses under their parent Status Group for easy navigation.

## Case Detail Tabs

The Case detail panel is organized into tabs, each focused on a different aspect of the Case.

### Information Tab

The Information tab contains:

* **Description** — a text area for free-form notes about the Case
* **Subscribers** — add or remove Subscribers who follow the Case for awareness (see below)
* **Alerts** — a list of linked Alerts showing Name, Type, Due Date, and actions
* **Notes** — a text area with an Add button for posting internal case notes

### Tasks Tab

* Displays a table of related Tasks with columns for Task, Reviewer, Due Date, and Status.
* If none exist, you'll see an empty state with options to: Relate existing or Create new.

### Conversations Tab

* Shows Conversations linked to this Case.
* If none exist, you'll see an empty state with options to: Relate existing or Create new.

### Appointments Tab

* Displays a table of related Appointments with columns for Starts at, Duration, Reviewer, Location, and Status.
* If none exist, you'll see an empty state with options to: Relate existing or Create new.

## Documents Tab

* Shows Documents linked to this Case.
* If none exist, you'll see an empty state with options to: Relate existing or Create new.

💡 **Learn More:** For a detailed walkthrough on linking objects to Cases, see Relating Objects to Cases.

---

# Assignees and Subscribers

## Assignee

Every Case has an Assignee — the individual internal user or team primarily responsible for resolving the Case. The Assignee is set when the Case is created and can be changed at any time.

## Subscribers

Subscribers are internal users who follow a Case for awareness. They want updates but are not responsible for resolution. Subscribers can be added or removed from the Information tab of the Case detail panel.

This is useful when multiple departments need visibility into a Case without sharing direct ownership — for example, a student success advisor may subscribe to a Case owned by the financial aid team.

---

# Case Privacy

Cases can be marked as Private using the toggle in the Case detail panel header (or at the time of creation). Use Case privacy for sensitive situations that require limited visibility.

When a Case is private:

* It is completely invisible to users who are not:

  + the Case creator
  + the Case Assignee
  + a user with the View All Cases permission
* Even administrators cannot see private Cases without the View All Cases permission.
* Once a Case has been created, only the Assignee or creator can toggle privacy (unless a user has View All Cases).

---

# Cases Profile Card

You can add a Cases card to your contact profile templates so that when viewing a student’s profile, you have quick access to all of their Cases without needing to navigate to the Case Management module. This gives your team immediate visibility into any open or past case work during advising sessions, check-ins, or when reviewing a student’s history.

For guidance on adding profile cards to templates, check out the [Configuring Profile Templates help article](https://help.element451.com/en/articles/10471008-configuring-profile-templates).

⚠️ **Important:** The Cases profile card must be placed in a two-column or three-column width layout. One-column is not supported.

---