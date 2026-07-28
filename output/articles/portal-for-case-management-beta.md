---
title: Portal for Case Management [Beta]
url: https://help.element451.com/en/articles/13772401-portal-for-case-management-beta
collection: Case Management (Beta)
---

A streamlined Element451 experience for internal users who submit and track student Alerts without needing access to the full platform.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

The Portal for Case Management provides a streamlined experience for internal users who don't need access to the full Element451 platform. Portal users can view a list of students, submit Alerts, and track the status of Alerts they have created.

When an admin adds a new internal user to Element451, they choose whether the user is a **Platform** user (full Element451 access) or a **Portal** user (lightweight Portal UI only). Portal users log in at the same Element451 URL as Platform users and are automatically routed to the Portal interface. [To learn more about adding and managing internal users, click here](https://help.element451.com/en/articles/2735199-adding-managing-internal-users).

## Accessing the Portal

Portal users log in through your institution's Element451 URL (for example, *yourinstitution.element451.io*) using their standard credentials. Element451 detects the user's type and routes Portal users to the Portal UI on login.

## Managing Your Account

Portal users can manage their own account details directly from the Portal. Click your avatar in the top right and select **Manage Account** to update your personal information and upload a profile picture.

---

# My Students Tab

⚠️ **Note:** Student visibility restrictions (limiting Portal users to only the students they have a relationship to) are planned for a future release. At this time, visibility is not restricted and **all students** will be visible in this list.

The **My Students** tab is the default view and displays a paginated list of students.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2413659803/c290b217bdefaee0503563381bc4/Faculty%2BPorta-402x.png?expires=1784333700&signature=73f20c571af7d40002ff56fd899971b8183fc329237c6d09622b5fc7a3c5f516&req=diQmFc97lIlfWvMW1HO4zRYsafvZg4oCp3Cde8bxbmUT%2Fz3wf9WutMPLbi0C%0AnLFs0DzrqFGWvVPxHcs%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2413659803/c290b217bdefaee0503563381bc4/Faculty%2BPorta-402x.png?expires=1784333700&signature=73f20c571af7d40002ff56fd899971b8183fc329237c6d09622b5fc7a3c5f516&req=diQmFc97lIlfWvMW1HO4zRYsafvZg4oCp3Cde8bxbmUT%2Fz3wf9WutMPLbi0C%0AnLFs0DzrqFGWvVPxHcs%3D%0A)

The table includes the following columns:

* **Name**
* **Email**
* **Course/Section**
* **Location**
* **Alerts** (a count of Alerts on the student)

Above the table, use the toolbar to:

* Toggle between **All Students** and **With Alerts** to filter the list.
* Search by name or email using the magnifying glass icon.
* Page through results with the pagination controls.

## Viewing a Student

Click a student's name to open the Student Details side sheet with two cards:

* **Information**: Name, Email, Phone, and Location
* **Alerts**: A list of Alerts associated with the student, with controls to search, filter (see Advanced Filter below), or add a new Alert

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2413655393/cc53a6a1edd51f9af15a1b7d49ca/portal-student%402x.png?expires=1784333700&signature=dd1f011f0161695efbccf1808adea7bcfff2a28b1e1004a06f100a6866c20396&req=diQmFc97mIJWWvMW1HO4zRjxAULwSa%2FdIVIkT7Zak3YSnwlfpiGwSfZkgQCw%0ArlVcTE%2B3mUm8T%2BFAb0c%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2413655393/cc53a6a1edd51f9af15a1b7d49ca/portal-student%402x.png?expires=1784333700&signature=dd1f011f0161695efbccf1808adea7bcfff2a28b1e1004a06f100a6866c20396&req=diQmFc97mIJWWvMW1HO4zRjxAULwSa%2FdIVIkT7Zak3YSnwlfpiGwSfZkgQCw%0ArlVcTE%2B3mUm8T%2BFAb0c%3D%0A)

---

# Submitting an Alert

There are two ways to submit Alerts from the Portal: one Alert for a single student, or a bulk submission that creates one Alert per selected student.

When filling out the New Alert form, Portal users select an **Alert Template** set up by your Platform users. The template applies its preset values (such as Priority, Assignee, and Due Date) automatically, so Portal submissions stay consistent without exposing those fields.

⚠️ **Important:** A **Template is required** for Portal users to submit an Alert. If you plan to use the Portal, create at least one Alert Template first in [Alert Settings](https://help.element451.com/en/articles/13772418-alert-settings-beta) (**Case Management** > **Settings** > **Alert Settings** > **Templates**). Without a template, Portal users won't be able to create an Alert.

## Single Alert

1. On the **My Students** tab, click the student's name to open their drawer.
2. In the **Alerts** card, click the **+** icon.
3. Fill in the New Alert form (see fields below).
4. Click **Submit**.

## Bulk Alert

1. On the **My Students** tab, select the checkbox next to each student you want to alert. A "*n* Selected" counter appears in the toolbar.
2. Click the **+ New Alert** button in the page header.
3. The New Alert form opens with each selected student pre-populated as a chip in the **Contacts** field, along with the helper text *"Each contact will receive their own alert."*
4. Fill in the New Alert form.
5. Click **Submit**. Element451 creates one Alert per selected student.

## New Alert Form Fields

Portal users see a streamlined version of the New Alert form with these fields:

* **Template** (required) — Choose from Alert Templates configured by your Platform users. The template sets the alert's **Priority**, **Assignee**, and **Due Date**.
* **Contact(s)**
* **Alert Type** (required)
* **Related Course** — shown only if the selected Alert Type has Course Related enabled
* **Description**

📙 **Note:** To keep the Portal form simple and Alerts consistent, the **Priority**, **Assignee**, and **Due Date** fields are hidden from Portal users. These values are set by the selected Template and can't be edited in the Portal.

---

# My Alerts Tab

The **My Alerts** tab is the Portal user's personal work list. It lists Alerts the user has created.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2413658096/07b6ffd466c491969ae345f5cd35/portal-myalerts%402x.png?expires=1784333700&signature=2d8296de9cd05b577b5056c57343b6c8636353bd4a19a75dd051c147d31aee47&req=diQmFc97lYFWX%2FMW1HO4zYyRVhhjd1a6GnPYzJXbjJsb4Zjjp8IrPepiFv3b%0A3ciwAJtAij5Sqq0EcT0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2413658096/07b6ffd466c491969ae345f5cd35/portal-myalerts%402x.png?expires=1784333700&signature=2d8296de9cd05b577b5056c57343b6c8636353bd4a19a75dd051c147d31aee47&req=diQmFc97lYFWX%2FMW1HO4zYyRVhhjd1a6GnPYzJXbjJsb4Zjjp8IrPepiFv3b%0A3ciwAJtAij5Sqq0EcT0%3D%0A)

The table includes:

* **Name**
* **Contact**
* **Alert Type**
* **Course Sections**
* **Resolution**
* **Reviewer**

Above the table:

* Toggle between **Active** and **Inactive** Alerts.
* Use the search and filter icons to narrow the list.

## Viewing and Editing an Alert

Click an Alert row to open the Alert detail side sheet:

* **Resolution card**: Update the **Reviewer**, **Due** date, and **Resolution** status (Triage, In Progress, Dismissed, Resolved, or Escalated to Case).
* **Information card**: Update the **Alert Type**, **Priority**, **Related Course**, and **Description**.
* **Discussion card**: Add notes to track collaboration on the Alert.

Edits save in place as you make them.

---

# Advanced Filter

The Advanced Filter modal is available using the funnel icon in both the student details side sheet and the **My Alerts** tab. Filter options include:

* **Alert Type**
* **Reviewer**
* **Due Date**
* **Due Date Range**
* **Contact**

Click **Apply Filters** to apply, or **Clear All** to reset.

---

# What Portal Users Can and Cannot Do

**Portal Users Can:**

* View students in the My Students list
* Submit Alerts individually or in bulk
* View and update Alerts they have created
* Add comments/notes to their Alerts
* Filter and search students and Alerts
* Update their personal information and profile picture via Manage Account

**Portal Users Cannot:**

* Access the full Element451 platform
* View or interact with Cases or Case work (Tasks, Conversations, etc.)
* Access Case Management settings or configuration

⚠️ **Note:** Portal users can only view and edit the details of Alerts they have created. Alerts created by other users may contribute to a student's Alert count in the My Students table, but those Alerts are not accessible from the Portal.

---

# For Admins: Setting Up Portal Access

[When adding a new internal user in Element451](https://help.element451.com/en/articles/2735199-adding-managing-internal-users), admins choose between two user types:

* **Platform**: Full Element451 platform access.
* **Portal**: Lightweight Portal UI only.

Once created as a Portal user, the user automatically sees the Portal interface when they log in.

💡 **Tip: Previewing the Portal as an Admin.** Because the experience is determined by user type at login, admins cannot preview the Portal from their own Platform account. To test the Portal UI, create a second internal user with the **Portal** user type using a different email address.

If your email provider supports **plus-addressing**, you can append *+portal* to your existing email to route the invite to your same inbox while creating a distinct Portal user — for example, *[michael.stephenson+portal@element451.com](mailto:michael.stephenson%2Bportal@element451.com)*. Gmail / Google Workspace, Outlook / Microsoft 365, Yahoo Mail, and iCloud Mail all support this.

⚠️ **Note**: At this time, Element451 does not support bulk user management, but it is on the roadmap for a future enhancement.

---