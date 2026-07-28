---
title: Managing Internal User Profiles
url: https://help.element451.com/en/articles/14727910-managing-internal-user-profiles
collection: Settings + Permissions
---

Learn how to view and manage an internal user's profile, activity, visibility groups, and restrictions from the user profile page in Element451.

# Overview

When you click into an internal user from **Settings > Manage Users**, you land on their profile page. This is your central hub for reviewing and managing everything about that user—their personal information, group memberships, activity history, contact visibility, and any restrictions applied to their account.

This article covers each tab on the user profile and what you can do from each one. For instructions on adding new users or deactivating existing ones, see [Adding + Managing Internal Users](https://help.element451.com/en/articles/2735199-adding-managing-internal-users).

Below, we will cover:

* Profile header
* Profile tab—basic information and milestones
* Assignments tab
* Groups & Permissions tab
* Activity tab
* Visibility Groups tab
* Restrictions tab—how to scope a user's access by type
* Admin actions

---

# Navigating the User Profile

To open a user's profile, go to **Settings > Manage Users** and click on any internal user's name. The profile opens with six tabs across the top: **Profile**, **Assignments**, **Groups & Permissions**, **Activity**, **Visibility Groups**, and **Restrictions**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308192656/42a9796a0037bacd19109a7a0c51/Internal+User+Profile%402x.png?expires=1784333700&signature=11488ad3123482815fa2f30604fc44ee9fbbff651abb860d0173db39ca8b5fad&req=diMnHsh3n4daX%2FMW1HO4zacWgZg4J5%2FezEholHFJzawWle%2FYAkBj49ckMlMg%0AQOWt%2Bj%2F9NzgIyfjmKDI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308192656/42a9796a0037bacd19109a7a0c51/Internal+User+Profile%402x.png?expires=1784333700&signature=11488ad3123482815fa2f30604fc44ee9fbbff651abb860d0173db39ca8b5fad&req=diMnHsh3n4daX%2FMW1HO4zacWgZg4J5%2FezEholHFJzawWle%2FYAkBj49ckMlMg%0AQOWt%2Bj%2F9NzgIyfjmKDI%3D%0A)

## Profile Header

At the top of every user profile, you'll see key information at a glance:

* **User name** with an **Internal User** chip.

  + The chip outline is **gray** when the user is active.
  + The chip outline is **red** when they have been deactivated.
* **Title** and **Primary Team** displayed below the name.
* **Permission group chips** showing every group the user currently belongs to.

  + Click the **Add Group** button to quickly access the Groups & Permissions tab.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308277578/0db6930a60e927fd4c681d3b0188/CleanShot+2026-04-22+at+16_19_57%402x.png?expires=1784333700&signature=d48fd1ebb396d7cb58ae2f1e08cf845fb363172398ebf0f0a49bc9d1c8ecc20f&req=diMnHst5moRYUfMW1HO4zXbv2zOQGBQ0g92jfXM2C0RMw9J8e7%2B7%2Fpip3Y2u%0ABkR2L1qSHYXv51JNfzY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308277578/0db6930a60e927fd4c681d3b0188/CleanShot+2026-04-22+at+16_19_57%402x.png?expires=1784333700&signature=d48fd1ebb396d7cb58ae2f1e08cf845fb363172398ebf0f0a49bc9d1c8ecc20f&req=diMnHst5moRYUfMW1HO4zXbv2zOQGBQ0g92jfXM2C0RMw9J8e7%2B7%2Fpip3Y2u%0ABkR2L1qSHYXv51JNfzY%3D%0A)

---

# Profile

The **Profile** tab displays the user's personal and account information. Use the left nav to switch between two sub-sections: **Basic Information** and **Milestones**.

## Basic Information

Click **Edit** to update any of the following fields:

* First Name, Last Name
* Email
* Title
* Office Phone Number
* Primary Team, Other Teams
* Preferred Start Page
* Office Building, Office Room
* Allow Direct Messages from Network Connections
* **I**dentity Fields (for [SSO](https://help.element451.com/en/articles/10542911-configuring-managing-single-sign-on-sso) Matching):

  + School ID: A stable institutional identifier, such as the value printed on a staff badge or used for HR and business records. Click + Add to set a value, or Edit/Delete to manage an existing one.
  + SSO ID: The identifier your identity provider returns in its SAML response. Click + Add to set a value, or Edit/Delete to manage an existing one.

Two password actions are available at the bottom of this section:

* **Change Password**—Set a new password directly for the user.
* **Send Reset Password Link**—Email the user a link to reset their own password.

## Milestones

The **Milestones** sub-section shows read-only timestamps for the user's account activity:

* **Last Seen** — When the user last logged in.
* **Last Modified** — When the user's record was last updated.
* **Account Created** — When the account was originally created.

---

# Assignments

The **Assignments** tab shows contact records currently assigned to this user and lets you reassign or un-assign records in bulk. These features are particularly useful during employee transitions and assignment shifts. It not only displays the **total** **count** of assigned records to that user, but also gives you the ability to perform two bulk actions pertaining to that user’s assigned records:

* **Reassign** **All**: Reassign all records to a different user or team in a single action. You will be required to type the user’s name or email to confirm the action.
* **Unassign** **All**: Unassign all records. You will be required to type the user’s name or email to confirm the action.

---

# Groups & Permissions

The **Groups & Permissions** tab is where you manage which permission groups this user belongs to. Permission groups control what the user can see and do across Element451. See [Creating + Managing Custom Permission Groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups) for details.

---

# Activity

The **Activity** tab displays a log of everything this user has done in the system. Use the left nav to filter by activity type: All Events, Appointments, Conversation, Task, Account, Session, Decision, Phone, Event, Custom, Payment Gateway, and SFTP.

Click any activity row to open a detail panel with the full event.

---

# Visibility Groups

Visibility groups control which contact records this user can see in Element451. By default, users have full visibility. Assigning a user to a visibility group limits their view to only contacts who match that group's conditions. On this tab, you can enable the setting "**Restrict the people visible to this user?**" by toggling it on and selecting one or more visibility groups from the checklist below the toggle. If no visibility groups are selected, the user retains full contact visibility even if the toggle is on.

[Explore More on Visibility Groups](https://help.element451.com/en/articles/5214533-visibility-groups)

---

# Restrictions

Restrictions let you scope a user's access to specific types of content. The **Restrictions** tab has four toggles—one for each restriction type. When a toggle is on, the user only sees the types their permission group allows for that resource.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308336262/c21d5272004e9a32e15a29f45dc0/CleanShot+2026-04-22+at+16_35_04%402x.png?expires=1784333700&signature=7483e8e7e99f9a06a45da2adaecd36bb47d1a985274361c42229cac7ea0c3399&req=diMnHsp9m4NZW%2FMW1HO4zQR%2FEPR3cTB7ig0atNwypAxcqFCDgzYsWVO8TN2m%0ArD1PCUVsf79b5SLSu5k%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308336262/c21d5272004e9a32e15a29f45dc0/CleanShot+2026-04-22+at+16_35_04%402x.png?expires=1784333700&signature=7483e8e7e99f9a06a45da2adaecd36bb47d1a985274361c42229cac7ea0c3399&req=diMnHsp9m4NZW%2FMW1HO4zQR%2FEPR3cTB7ig0atNwypAxcqFCDgzYsWVO8TN2m%0ArD1PCUVsf79b5SLSu5k%3D%0A)

## Restriction Types

Each toggle corresponds to a specific resource. For each one, the allowed types must first be configured in the user's permission group before the toggle here has any effect.

### Document Types

Limits which document types are visible to this user. When enabled, only the document types selected in the permission group's **Document Types** settings will be accessible. See [Creating + Managing Custom Permission Groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups) for how to configure allowed document types.

### Campaigns

Limits which campaigns are visible to this user, filtered by campaign tag. When enabled, only campaigns tagged with the allowed tags (configured in the permission group's **Campaigns** settings) will be visible. See [Creating + Managing Custom Permission Groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups) for how to configure allowed campaign tags.

### Alert Types

Limits which alert types this user can see and work with in Case Management. When enabled, only the alert types selected in the permission group's **Case Management** settings are accessible—across settings, alert creation, and alert queues.

### Case Types

Limits which case types this user can see and work with in Case Management. When enabled, only the case types selected in the permission group's **Case Management** settings are accessible—across settings, case creation, and case queues.

## How Restrictions Work

Restrictions are a two-step system:

1. **Configure the permission group.** In **Settings > Permission Groups**, open the group and select which types that group is allowed to access for each resource (Document Types, Campaigns, Alert Types, Case Types).
2. **Enable the restriction on the user.** On the user's **Restrictions** tab, turn on the toggle for each restriction type you want to enforce.

🚨 **Important:** Both steps must be completed. Enabling the toggle without configuring the permission group—or configuring the group without enabling the toggle—has no effect. The user will continue to see everything their base permissions allow.

💡 **Use Case:** A school wants advisors in the Financial Aid office to only see and work with Financial Aid alert and case types—not Registrar or Housing types. An admin configures the Financial Aid advisors' permission group to include only Financial Aid types, then enables the Alert Types and Case Types toggles on each advisor's Restrictions tab. Those advisors now only see Financial Aid alerts and cases across settings, creation, and their queues.

## What Changes When a Restriction Is Active

Once enabled, the user's experience is scoped to their allowed types. The specific impact depends on the restriction type:

### Document Types

The user's experience is scoped across three areas:

* **Settings:** Only allowed document types appear in Document Type settings.
* **Uploading documents:** Only allowed document types are selectable when uploading a new document.
* **Documents bin:** Only documents of allowed types are visible in the documents bin.

### Campaigns

Only campaigns matching the allowed tags are visible to the user.

### Alert Types & Case Types

The user's experience is scoped across three areas:

* **Settings:** Only allowed types appear in type dropdowns and template lists. This applies when creating or viewing Alert Type Settings, Case Type Settings, Alert Templates, and Case Templates.
* **Creating alerts/cases:** Only allowed types are selectable. Templates tied to a restricted type are hidden from the template list.
* **Viewing alerts/cases:** Only alerts and cases of allowed types are visible anywhere in the platform.

## Exempting a User from Restrictions

Restrictions apply to all users, regardless of permission level. Even users with **Administer Alerts**, **Administer Cases**, or **Administer Documents** permissions are subject to type restrictions when the toggle is on.

To give a specific user full, unrestricted access—for example, a supervisor who needs to see all types—simply disable the relevant toggle(s) on their **Restrictions** tab. This exempts that user from restriction enforcement regardless of how the permission group is configured.

🧠 **Good to Know:** Restrictions are additive constraints layered on top of base permissions. The permission group defines *which types are allowed*; the user-level toggle controls *whether the restriction is enforced* for that individual.

---

# Admin Actions

In the top-right corner of the user profile, click the person/gear icon to access admin actions:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308344625/f778e823fecd70a325210afaebbc/CleanShot+2026-04-22+at+16_36_53%402x.png?expires=1784333700&signature=d2e4a64db469b15c91b1c629daffb2d84456e04fa86d63ed62e52ebb120b17df&req=diMnHsp6mYddXPMW1HO4zTnndvbwzYBv1tiHMKKUiFw37zy8dbZqKFO9jyUd%0A7ehGyCxGeuejXfCz32o%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308344625/f778e823fecd70a325210afaebbc/CleanShot+2026-04-22+at+16_36_53%402x.png?expires=1784333700&signature=d2e4a64db469b15c91b1c629daffb2d84456e04fa86d63ed62e52ebb120b17df&req=diMnHsp6mYddXPMW1HO4zTnndvbwzYBv1tiHMKKUiFw37zy8dbZqKFO9jyUd%0A7ehGyCxGeuejXfCz32o%3D%0A)

* **Deactivate User**: Disables the user's login without deleting their record or data.

  + If the user is already deactivated, this option will display as **Activate User** instead, allowing you to restore their access.
* **Delete User**: Permanently removes the user from the system.
* **Change User's Password**: Set a new password for the user directly.

🚨 **Important:** Deleting a user is permanent and cannot be undone. Consider deactivating instead if you may need the user's record in the future.

---