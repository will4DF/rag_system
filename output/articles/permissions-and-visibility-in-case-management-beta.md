---
title: Permissions and Visibility in Case Management [Beta]
url: https://help.element451.com/en/articles/15465236-permissions-and-visibility-in-case-management-beta
collection: Case Management (Beta)
---

How Element451 controls who can see and act on Alerts and Cases—permission levels, type visibility, contact visibility groups, case privacy, and related-object permissions.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

Who can see and act on an Alert or Case is determined by several layers working together. A user must pass **every applicable check** to see a given Alert or Case—if any single layer excludes it, they won't see it, even if they have general access to the module.

This article walks through each layer and how to configure it.

---

# The Visibility Layers

A user can see an Alert or Case only when all of the following allow it:

* **Individual Permissions**: The user has the relevant Alert and/or Case permissions.
* **Alert & Case Type Visibility**: The Alert or Case type is permitted for the user's permission group.
* **Contact Visibility Groups**: The student is within the user's visibility scope.
* **Case Privacy**: The case is not marked private to others.
* **Related Object Permissions**: For objects inside a case, the user has the relevant object permission.

🧠 **Good to Know:** These checks stack. Failing any one of them hides the record, regardless of the others. Think of them as filters narrowing from broad to specific: permissions decide *what kinds of work* a person can touch, visibility groups decide *which students*, and case privacy protects *individual sensitive cases*.

---

# Permission Levels

Alert and Case permissions are assigned through [permission groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups), and they are separate—a user can have one level for Alerts and a different level for Cases. To configure them, go to **Settings > Manage Users > Permission Groups**, open a group's **Permissions** tab, and find **Alerts** and/or **Cases** under the **Element Core** heading. **Alerts** have four permission levels, and **Cases** share those four plus one additional override:

|  |  |
| --- | --- |
| **Level** | **What it grants** |
| **Access** | View only. |
| **Manage My** | Create and edit records you created. |
| **Manage My Team** | Create and edit records created by your team. |
| **Administer** | Full control over all records of that type, plus the related settings. |
| **View All Cases** *(Cases only)* | A visibility override that lets a user see all Cases, including Private ones. |

💡 **How teams use this:** Match the level to the role.

* **Access** for staff who need to see activity but not change it, such as a department lead keeping an eye on their area.
* **Manage My** for frontline advisors and counselors working their own caseload.
* **Manage My Team** for team leads who coordinate and reassign work across their group.
* **Administer** for the program owner who also configures types, statuses, and templates.
* **View All Cases** sparingly—usually directors or compliance staff who must be able to see private cases.

For details on every individual permission, see [List + Details of Individual Permissions](https://help.element451.com/en/articles/6590379-list-details-of-individual-permissions).

---

# Alert and Case Type Visibility

Beyond the permission level, you can control **which Alert Types and Case Types** a group of users can see. This is configured on the permission group, and it takes two steps—**both are required** for the restriction to take effect:

1. **At the permission group level:** With the group open, select the **Case Management** tab and check the **Alert Types** and/or **Case Types** that should be viewable. Restricted users will only see Alerts and Cases that match the selected types.
2. **At the individual user level:** Go to **Settings > Manage Users**, select the user, open the **Restrictions** tab, and toggle on **Case Management**. This applies the type restriction to that specific user.

💡 **How teams use this:** Give each care unit its own focused queue. Scope the financial aid group to **Financial** types, counseling staff to **Wellbeing**, and conduct officers to **Conduct**—so every office sees only the work that's theirs, and sensitive case types stay with the team that handles them.

⚠️ **Important:** Selecting types on the permission group has no effect until the Case Management restriction is toggled on for the user. See [Creating + Managing Custom Permission Groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups) and [Managing Internal User Profiles](https://help.element451.com/en/articles/14727910-managing-internal-user-profiles).

---

# Contact Visibility Groups

Visibility groups limit which **students** a staff member can see across Element451. If a user is limited by a visibility group, they will only see Alerts and Cases for students within their scope—even if they otherwise have access to the Case Management module. Visibility Groups are managed in **Settings > Manage Users > Visibility Groups**; see [Visibility Groups](https://help.element451.com/en/articles/5214533-visibility-groups) to learn more.

💡 **How teams use this:** Use visibility groups when staff should only work their own population—regional advisors seeing only their territory, or college-specific success coaches seeing only their college's students. Where type visibility limits work by *category*, visibility groups limit it by *student*, and the two combine: a financial aid advisor for the College of Nursing can be scoped to Financial cases *and* only nursing students.

---

# Case Privacy

An individual Case can be marked **private**. A private Case is invisible to everyone except its **creator**, its **assignee**, and users with the **View All Cases** permission. Even administrators cannot see a private Case without that permission.

Privacy can be enabled when a case is created, or later from the header of an existing case. For an existing case, only the case's creator, assignee, or an admin can turn privacy on or off. Privacy can also be applied automatically through the **Mark as Private** action in an Automation Rule. Use it for sensitive work such as conduct or wellbeing cases.

💡 **How teams use this:** For sensitive workflows, pair privacy with automation. Build an Automation Rule that creates a **Conduct** or **Wellbeing** case and applies **Mark as Private** in the same rule—so those cases are protected the moment they're opened, without relying on staff to remember to flag them.

---

# Related Object Permissions

Objects linked to a Case—Conversations, Tasks, Appointments, Jobs, and Documents—each keep their own native permissions. Having access to a Case does **not** automatically grant access to everything inside it. A user needs the appropriate permission for each object type to see it within the Case detail panel. For example, a user without Conversations permissions will not see conversations related to a Case, even if they can open the Case itself.

📙 **Note:** Documents also have a **Document Type visibility** setting, configured at the permission group level. Cases inherit those document restrictions, so a user will only see related documents of the types they're permitted to view.

---