---
title: Case Settings [Beta]
url: https://help.element451.com/en/articles/13775536-case-settings-beta
collection: Case Management (Beta)
---

Configure the Case types, statuses, priorities, and templates that shape how Cases work in your institution's Case Management module.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

Case Settings allow administrators to configure the types, statuses, priorities, and templates that define how Cases work in your institution's Case Management module. These settings control the options available when creating and managing Cases.

This article walks through each Case settings page and explains how to configure them.

---

# Accessing Case Settings

To access settings, click the ⋮ **(more menu)** at the top right of the Case Management page and select a settings option. Selecting any option will open Case Management Settings.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131514011/c1ac064e6225e1f3d90bc15f07f2/CleanShot+2026-03-05+at+13_28_11%402x.png?expires=1784333700&signature=5cd2c73795b86a885086d7a85d22e22f5fcd561834b2e01ebee4d9fb98fa9435&req=diEkF8x%2FmYFeWPMW1HO4zbI5UGcXAqYovuJS2kFQDabgBAz93SWqNzqi2UXz%0Aq2P3p71FSzg15p9qMr8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131514011/c1ac064e6225e1f3d90bc15f07f2/CleanShot+2026-03-05+at+13_28_11%402x.png?expires=1784333700&signature=5cd2c73795b86a885086d7a85d22e22f5fcd561834b2e01ebee4d9fb98fa9435&req=diEkF8x%2FmYFeWPMW1HO4zbI5UGcXAqYovuJS2kFQDabgBAz93SWqNzqi2UXz%0Aq2P3p71FSzg15p9qMr8%3D%0A)

In the Settings left sidebar, expand the Cases section to find:

* **Types**
* **Statuses**
* **Priorities**
* **Templates**

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131519472/aee74c2d021feada25b8e58332f7/Case+Mgmt+Settings%402x.png?expires=1784333700&signature=14484e6005e770399252c31d11b28c39bd10720a924258457a495eadaa30c189&req=diEkF8x%2FlIVYW%2FMW1HO4zYmLHY3qU4v4V3eQe4YqTxk9OFSSY8mBYMhUfFmq%0A5EEfXqn56vBLJ3%2BYTh4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131519472/aee74c2d021feada25b8e58332f7/Case+Mgmt+Settings%402x.png?expires=1784333700&signature=14484e6005e770399252c31d11b28c39bd10720a924258457a495eadaa30c189&req=diEkF8x%2FlIVYW%2FMW1HO4zYmLHY3qU4v4V3eQe4YqTxk9OFSSY8mBYMhUfFmq%0A5EEfXqn56vBLJ3%2BYTh4%3D%0A)

---

# Case Types

Case Types categorize the kind of work a Case represents. You can customize your Case Types to match your needs.

Element451 provides the following default Case Types to get you started. However, you can edit, rename, or delete them if you wish.

* Academic
* Advising
* Conduct
* Engagement
* Financial
* Retention
* Wellbeing

## Managing Case Types

The Case Types settings page displays a table with the following columns:

|  |  |
| --- | --- |
| **Column** | **Description** |
| **Type** | The **name** of the Case Type |
| **Description** | A brief description of when this type should be used |
| **Enabled** | Toggle — controls whether this type is available for use |
| **≡ (Drag handle)** | Drag to reorder how the types appear in drop down menus |
| ⋮ **(Actions)** | Edit or Delete the type |

## Adding a New Case Type

Click **+ Add Type** at the bottom of the table to create a new Case Type.

## Editing a Case Type

Click the ⋮ **(more menu)** and select **Edit** to update:

* **Name** — custom name
* **Description** — text area for the type's description
* **Enabled** — toggle to enable or disable the type

---

# Case Statuses

Case Statuses define the stages a Case moves through during its lifecycle.

This is the most detailed settings page in Case Management, because statuses use a two-tier system: fixed **system status** with **custom statuses** layered on top.

Element451 provides the following default Case Statuses to get you started. However, you can edit, rename, or delete them if you wish. (*Note: You can only delete a status if another one exists in that system status group. Continue reading to learn more.*)

|  |  |
| --- | --- |
| **Custom Status Name** | **System Status** |
| To Do | To Do |
| In Progress | In Progress |
| Resolved | Resolved |
| Cancelled | Cancelled |

## System Statuses

Every custom status must belong to one of four system status groups. These groups cannot be renamed or removed — they provide the underlying structure for the Case lifecycle:

|  |  |  |
| --- | --- | --- |
| **System Status** | **Meaning** | **Examples** |
| **To Do** | Cases that are pending or not yet started | Not Started, Awaiting Assignment |
| **In Progress** | Cases that are actively being worked on | In Progress, Waiting on Student, Under Review |
| **Resolved** | Cases that have been completed successfully | Resolved, Referred to External, Graduated |
| **Cancelled** | Cases that were closed without resolution | Cancelled, Duplicate, Withdrawn |

🚨 **Important:** At least one custom status must exist in each system status group. Element creates default statuses for you, which you can rename or edit.

## Default Status

At the top of the Case Statuses settings page, a dropdown lets you choose the default status for **newly created Cases**.

For example, "Not Started" means when you click "Create Case," the form will open with the status "Not Started" pre-selected for you.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131546473/5faad4ba4e7faa38378742e0f0fa/CleanShot+2026-03-05+at+13_41_03%402x.png?expires=1784333700&signature=f6344a8379f472baf4a4b15aff978ff1b01263cd0a72f7a7174e718f2713d183&req=diEkF8x6m4VYWvMW1HO4zaagK5WhBqVDZboG0gQ9NDFUxXUvnqIYl08EqgQg%0AJjwrTArRi0cC4sclEgo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131546473/5faad4ba4e7faa38378742e0f0fa/CleanShot+2026-03-05+at+13_41_03%402x.png?expires=1784333700&signature=f6344a8379f472baf4a4b15aff978ff1b01263cd0a72f7a7174e718f2713d183&req=diEkF8x6m4VYWvMW1HO4zaagK5WhBqVDZboG0gQ9NDFUxXUvnqIYl08EqgQg%0AJjwrTArRi0cC4sclEgo%3D%0A)

## Managing Custom Statuses

Each System Status Group section shows:

* **+ Add** button to create a new custom status within that group
* A list of custom statuses, each with a drag handle (≡) for reordering how they appear in drop down menus and an actions menu (⋮)

### Editing a Status

Click the ⋮ **(more menu)** on a status and select **Edit** to open the edit panel. From there you can edit:

* **Name**
* **Status Group** — a dropdown that lets you move this status to a different group (e.g., moving a status from To Do to In Progress)

🧠 **Good to Know:** Statuses in the **Resolved** group appear in the "Mark as complete" dropdown on the Case detail panel. When a user clicks Mark as complete, they select from the Resolved statuses (if more than one exists).

---

# Case Priorities

Case Priorities define the urgency levels available when creating or managing Cases. Each priority has a custom color and icon for visual distinction in list views.

Element451 provides the following default Case Priorities to get you started. However, you can edit, rename, or delete them if you wish. (*Note: You can not delete the Critical priority because it's used by the system to count the total number of Critical cases to display on the All Cases table.*)

* Critical
* High
* Medium
* Low

## Managing Case Priorities

The Case Priorities settings page works identically to Alert Priorities. The table shows columns for Custom Priority, Icon, Color, Enabled toggle, drag handle, and actions menu.

### Adding a Custom Priority

Click **+ Add Custom Priority** at the bottom of the table.

### Editing a Priority

Click the ⋮ **(more menu)** and select **Edit** to update:

* **Name** — enter a custom name
* **Icon** — select from the icon library
* **Color** — set a hex color code with visual swatch preview
* **Enabled** — toggle to enable or disable the priority

✨ **Pro** **Tip:** You can enable or disable priorities directly in the table without opening the edit panel, making quick configuration changes easy.

---

# Case Templates

Case Templates let you define a standard set of pre-configured field values that can be applied when creating a new case—manually or through a workflow action. Templates save time and keep your team consistent across every case they create.

For a complete guide to creating and using both Alert and Case Templates, see [Alert and Case Templates](https://help.element451.com/en/articles/14659708-alert-and-case-templates-closed-beta).

---