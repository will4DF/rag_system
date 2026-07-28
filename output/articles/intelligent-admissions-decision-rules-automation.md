---
title: Intelligent Admissions: Decision Rules + Automation
url: https://help.element451.com/en/articles/9241624-intelligent-admissions-decision-rules-automation
collection: Decisions
---

Streamline your application process with Intelligent Admissions, automating tasks and enhancing decision-making efficiency.

# Overview

**Intelligent Admissions (IA)** is a powerful automation tool designed to enhance the efficiency of the application evaluation process in various ways. Beyond simply advancing applications through different stages, IA can execute various actions based on customized conditions, streamlining routine tasks and complex workflows. This lets your admissions team focus on strategic decision-making and personal interactions with applicants.

📌 **Note:** IA rules are triggered to run whenever decisions are **created** or **updated**. As a result, rules do not apply to decisions that already exist.

## Accessing IA

To access IA settings where you add new and manage existing rules:

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Intelligent Admissions** tab.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1032248039/8ea02bf6aaf4d61e0517d49c/Decisions+-+IA.png?expires=1784333700&signature=2d67a4b9683f52a665fa2af9f86e83a4b2ad11902905c09337cb2ab762edc51a&req=dSAkFMt6lYFcUPMW1HO4zfLrMmDic9TGL%2B%2FP23l3sVj6JLDp8Obzp4aVP1ur%0AjHtZ%0A)](https://downloads.intercomcdn.com/i/o/1032248039/8ea02bf6aaf4d61e0517d49c/Decisions+-+IA.png?expires=1784333700&signature=2d67a4b9683f52a665fa2af9f86e83a4b2ad11902905c09337cb2ab762edc51a&req=dSAkFMt6lYFcUPMW1HO4zfLrMmDic9TGL%2B%2FP23l3sVj6JLDp8Obzp4aVP1ur%0AjHtZ%0A)

---

# How IA Rules Work

IA utilizes a combination of **Conditions** and **Actions** to automate processes and ensure that each application is handled precisely according to your institutional policies:

## Conditions

Conditions act as the criteria that trigger IA to perform specific actions. These are set based on a variety of application details and evaluation requirements:

* Evaluations such as tests and scores
* Decision-making criteria like stages, statuses, tags, cohorts
* Specifics of the application, such as type, term, major, or checklist items
* User segments or references

🚨 **Important:** Avoid using Application filters (e.g., Application (All Properties) when building Intelligent Admissions rules. We recommend using **Decision** conditionsor Decision segment filters instead whenever possible. This is because Application-based filters are evaluated before all application data has fully synced, which may cause race conditions or inaccurate results.

## Actions

Actions are performed once an application meets the specified conditions. These can vary widely to cover all aspects of application processing:

* Changing the status of an application
* Moving applications to a different stage
* Assigning applications to a team member
* Adding or removing tags and watchers
* Enabling or disabling packages
* Setting specific criteria for further processing

## Example

For instance, if an application is flagged as 'ready for review' and it indicates the applicant's citizenship status as non-US, IA can be set to automatically route the application to the International Review stage and update its status to "in review," thereby ensuring the appropriate team handles the application.

---

# Key Considerations for IA Rules

Before creating an IA rule, there are a few important things you should keep in mind:

## Rule Evaluation Order

When a decision is created or updated, IA evaluates your rules **one at a time, in the order the rules were originally created**—not the order they appear in the UI. The list on the Intelligent Admissions settings page is sorted alphabetically by name, which does not reflect execution order.

This matters because each rule can change the decision it acts on (status, stage, assignment, tags, etc.). If an earlier rule modifies a field that a later rule's condition depends on, the later rule will not trigger—even if the decision originally met those conditions when it entered the system.

**Example:** You have two rules:

* **International Student** (created first)—moves the decision to **Waiting on Citizenship Documentation**.
* **International Apps Assigned to Jennifer** (created second)—assigns the decision to Jennifer when status is **Ready for Review**.

An international application enters the system in **Ready for Review** and matches both rules. Because **International Student** was created first, it runs first and changes the status. When **International Apps Assigned to Jennifer** is evaluated next, the status no longer matches **Ready for Review**, so the rule is skipped.

**Best practice:** When two or more rules could match the same decision, make each rule's conditions specific enough that only the intended rule fires at each step. In the example above, scope the second rule to **status is In Review** or **stage is Waiting on Citizenship Documentation** so it only runs after the first rule has done its work.

## Mutually Exclusive Rules (Loop Prevention)

Ensure that your rules do not overlap to prevent the system from becoming stuck in a loop between conflicting actions. We recommend regularly reviewing your IA configurations to keep them current and prevent overlapping with other rules. If the system detects a loop between two rules, the affected rule is automatically deactivated. See **Rule Loop Alerts** below for details.

## Detailed Conditions

The more detailed your conditions, the more predictable and secure the outcomes will be, reducing the chance of errors.  
​

## When Rules Won't Trigger

* **Released Decisions**: By default, IA rules cannot move a decision to a different stage or change its status once the decision has been released to the student. Other actions—adding tags, updating assignees, toggling packages, and updating watchers—continue to work on released decisions. To allow a specific rule to also update stage or status after release, enable the **Allow Changes to Released Decisions** toggle when creating or editing the rule (see **Allowing Rules to Affect Released Decisions** below).

* **Existing Decisions**: IA rules are triggered to run whenever decisions are **created** or **updated**. As a result, rules do not apply to decisions that already exist.

* **An Earlier Rule Already Modified the Decision**: Rules run in creation order. If an earlier rule changed a field that a later rule's condition checks (for example, status or stage), the later rule will not trigger. See **Rule Evaluation Order** above for details.

## Allowing Rules to Affect Released Decisions

By default, IA rules cannot move a released decision to a different stage or change its status — those actions are blocked once a decision has been released to the student. Other actions (tags, assignees, packages, watchers) are not affected by this guard.

For workflows that need to keep released decisions in sync — for example, tracking deposit or withdrawal status across multiple applications a student has submitted for the same term — enable the **Allow Changes to Released Decisions** toggle on the rule. Once enabled, the rule's **Move to** and **Change Status** actions will run on released decisions in addition to in-progress ones.

🚨 **Important:** Released decisions are visible to applicants in their portal. Changing the stage or status of a released decision may change what the student sees. Use this option carefully, scope your conditions tightly, and confirm the change is intended before activating the rule.

Standard safeguards still apply. If a rule with this toggle enabled produces a loop with another rule, the system will auto-deactivate it the same way it would for any other rule. See **Rule Loop Alerts** below.

---

# IA Rule Loop Alerts

If two IA rules conflict in a way that creates a loop—for example, one rule moves a decision to a stage while another moves it back—the system automatically deactivates the rule that triggered the loop to prevent repeated, unintended changes.

## Identifying a Deactivated Rule

When a rule is deactivated due to a loop, a red warning icon (⚠️) appears next to the rule's toggle on the Intelligent Admissions settings page. Hovering over the icon displays a tooltip with a summary of the issue, including the reason for deactivation, the affected decision, and the other rule suspected of causing the loop.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2197488169/3d7c4c6a46304df7482efc17afee/CleanShot+2026-03-24+at+16_52_48.png?expires=1784333700&signature=8a7a829502c5a794dd1e094965ef965fb543a4b73f5cbc66e5e35e288c86bb52&req=diEuEc12lYBZUPMW1HO4zbdJNurzNpSybXu5U56DPRGlcMkFR8tP9lqbtVQi%0AZlCTgunKdWrIuVo5hPQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2197488169/3d7c4c6a46304df7482efc17afee/CleanShot+2026-03-24+at+16_52_48.png?expires=1784333700&signature=8a7a829502c5a794dd1e094965ef965fb543a4b73f5cbc66e5e35e288c86bb52&req=diEuEc12lYBZUPMW1HO4zbdJNurzNpSybXu5U56DPRGlcMkFR8tP9lqbtVQi%0AZlCTgunKdWrIuVo5hPQ%3D%0A)

## Viewing Error Details

Clicking the warning icon opens a dialog with the full details of the deactivation, including:

* The reason the rule was deactivated
* The affected decision (with a link to view it)
* The other rule suspected of causing the loop
* The date and time the rule was deactivated

From this dialog, you can click **View Decision** to go directly to the affected decision, or click **Restore Rule** to restore the original rule content. Restoring a rule brings back its original conditions and actions but keeps the rule inactive—review and modify the rule's conditions before reactivating it.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2197507813/dca7dd8cd92ae211944cc8031c76/IA-Loop-Error-Details.png?expires=1784333700&signature=eb6153f0a2e37126ad6159316603d292f5672e5c18cc3b00b7768a2b8b53c578&req=diEuEcx%2BmoleWvMW1HO4zeZ3ccuHxgOKJvtZB70lv5zuBBOoEhe0XBqbzC34%0ACs2spSDQO4KQAaxVyLI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2197507813/dca7dd8cd92ae211944cc8031c76/IA-Loop-Error-Details.png?expires=1784333700&signature=eb6153f0a2e37126ad6159316603d292f5672e5c18cc3b00b7768a2b8b53c578&req=diEuEcx%2BmoleWvMW1HO4zeZ3ccuHxgOKJvtZB70lv5zuBBOoEhe0XBqbzC34%0ACs2spSDQO4KQAaxVyLI%3D%0A)

## Email Notifications

Admins with permissions to manage IA rules receive an email notification when a rule is deactivated due to a loop. The email includes a detailed error message describing the issue so you can take action promptly.

---

# List of IA Rules

On the Intelligent Admissions Settings page, you'll see a table listing all the rules you've created. This table is designed to give you a quick overview of key details for each rule, helping you manage and review them efficiently. Within this table, you will find the rule name, description, action, active status, the date the rule was last modified, and the creator of the rule.   
​

[![](https://downloads.intercomcdn.com/i/o/1039533100/4cb18c05027e8a9bc0291831/Decisions+-+IA+Listing.png?expires=1784333700&signature=aa103b7430b07c056600fb220da27f1804b640777544d51e7ed5adaaca81af0a&req=dSAkH8x9noBfWfMW1HO4zRaBXRpF08YL%2BMx%2B0n7Xe4uPN8s7u%2Fh634DVNf3U%0AJzVRLxC8cEEFdQ0L6fo%3D%0A)](https://downloads.intercomcdn.com/i/o/1039533100/4cb18c05027e8a9bc0291831/Decisions+-+IA+Listing.png?expires=1784333700&signature=aa103b7430b07c056600fb220da27f1804b640777544d51e7ed5adaaca81af0a&req=dSAkH8x9noBfWfMW1HO4zRaBXRpF08YL%2BMx%2B0n7Xe4uPN8s7u%2Fh634DVNf3U%0AJzVRLxC8cEEFdQ0L6fo%3D%0A)

---

# Creating + Managing IA Rules

## Creating a New Rule

When creating a rule, it's important to remember that they are triggered to run whenever decisions are **created** or **updated**. As a result, rules do not apply to decisions that already exist.

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Intelligent Admissions** tab.
3. Click on the circle plus sign button in the bottom right corner of the screen.
4. Give your Cohort a **Name** and **Description**.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1039534394/f68459853762557f046c5cd7/Decisions+-+IA+-+New+Rule.png?expires=1784333700&signature=61e2d30d1363081f8096e77a8b989df05679fcc4d0fb9be9adfbfc2b46fd5f86&req=dSAkH8x9mYJWXfMW1HO4zTlunsTjOcc758PbGfTtB2gqHNXV%2Biqg2xwQNdvt%0AbhAo%0A)](https://downloads.intercomcdn.com/i/o/1039534394/f68459853762557f046c5cd7/Decisions+-+IA+-+New+Rule.png?expires=1784333700&signature=61e2d30d1363081f8096e77a8b989df05679fcc4d0fb9be9adfbfc2b46fd5f86&req=dSAkH8x9mYJWXfMW1HO4zTlunsTjOcc758PbGfTtB2gqHNXV%2Biqg2xwQNdvt%0AbhAo%0A)
5. Click **Create**.
6. Set [Conditions](https://help.element451.com/en/articles/9241624-intelligent-admissions-decision-rules-automation#h_9c85de4b10):

   * **Choose Condition Type**: Select a condition from the dropdown menu. Available options encompass standard choices such as **User Segment** and **User Segment Reference**. Additionally, you can access Decision-specific options tailored to your needs, including **stages**, **statuses**, **tests**, and **cohorts**. This variety allows you to create targeted rules based on diverse criteria.
   * Click **Add** **Condition**' to add any additional filters.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/1039535292/0ccc5277fceb2ca8796a2847/Decisions+-+IA+-+New+Rule+Conditions.png?expires=1784333700&signature=52a7a61ddbe996d93985e68dcd0f51f1ba045465aa9cb09668e14ad8b09a886f&req=dSAkH8x9mINWW%2FMW1HO4zVEFqX1XjJ2z1Y%2BnbTrwIEdFLARDBT3%2FIGKTIFGT%0Ab08N%0A)](https://downloads.intercomcdn.com/i/o/1039535292/0ccc5277fceb2ca8796a2847/Decisions+-+IA+-+New+Rule+Conditions.png?expires=1784333700&signature=52a7a61ddbe996d93985e68dcd0f51f1ba045465aa9cb09668e14ad8b09a886f&req=dSAkH8x9mINWW%2FMW1HO4zVEFqX1XjJ2z1Y%2BnbTrwIEdFLARDBT3%2FIGKTIFGT%0Ab08N%0A)
7. Set [Action](https://help.element451.com/en/articles/9241624-intelligent-admissions-decision-rules-automation#h_5e570f7e99):

   * Select an action from the dropdown menu. Depending on your choice, you will be prompted to provide further details. For example, if you select 'Move to' as your action, you must specify both the stage and the status to which the decision should be updated.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/1039537411/5099f41a8b30c6d283206ec7/Decisions+-+IA+-+New+Rule+Actions.png?expires=1784333700&signature=7e23bdc8f115d1b6df1fdd8a65e0eaf103e06420c65fdddef8f9db83c25742fc&req=dSAkH8x9moVeWPMW1HO4zXMJtiz1Of5vVlXeimPuKGBanbxWwXwWiqEBhWzQ%0AAr5d%0A)](https://downloads.intercomcdn.com/i/o/1039537411/5099f41a8b30c6d283206ec7/Decisions+-+IA+-+New+Rule+Actions.png?expires=1784333700&signature=7e23bdc8f115d1b6df1fdd8a65e0eaf103e06420c65fdddef8f9db83c25742fc&req=dSAkH8x9moVeWPMW1HO4zXMJtiz1Of5vVlXeimPuKGBanbxWwXwWiqEBhWzQ%0AAr5d%0A)
8. (Optional) If this rule should be able to update the stage or status of decisions that have already been released, enable **Allow Changes to Released Decisions**. Review the warning carefully — released decisions are visible to applicants. See [Allowing Rules to Affect Released Decisions](https://help.element451.com/en/articles/9241624-intelligent-admissions-decision-rules-automation#h_4d98f9692a) for details.
9. Click **Done**. Your rule will be added to the list.
10. Toggle **Active** to **Yes**: By default, your new rule is inactive. You must make it active for it to run.

## Editing + Deleting Rules

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Intelligent Admissions** tab.
3. Locate the rule you wish to edit/delete:  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1032291671/88babf6a8ebfc78bd4a41839/Decisions+-+IA+Edit+and+Delete.png?expires=1784333700&signature=78a0f46f2000ea081b6f0d3a6100e2c8017f152e7ee2857975c9105c879bc8d1&req=dSAkFMt3nIdYWPMW1HO4zYT6Sy31eOxyUnlKn%2Fzj4dk7477ii%2FRCH6P3%2F%2F3A%0AkyXA%0A)](https://downloads.intercomcdn.com/i/o/1032291671/88babf6a8ebfc78bd4a41839/Decisions+-+IA+Edit+and+Delete.png?expires=1784333700&signature=78a0f46f2000ea081b6f0d3a6100e2c8017f152e7ee2857975c9105c879bc8d1&req=dSAkFMt3nIdYWPMW1HO4zYT6Sy31eOxyUnlKn%2Fzj4dk7477ii%2FRCH6P3%2F%2F3A%0AkyXA%0A)

   * To edit the rule **name** or **description**, click the pencil icon.
   * To edit the **condition(s)** or **action**, click on the **filter** icon.
   * To **activate**/**deactivate** a rule, use the **Active** **toggle**.
   * To **delete** a rule, click the **three vertical dots** and select **Delete**. You will be asked to confirm your action.

## Organizing Rules in Folders

Consider organizing your IA rules into folders to enhance navigation and quickly access them.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1387933064/eae0ff2784c425eacbfd037ce079/Decisions%2B-%2BIA%2B-%2BFolders.png?expires=1784333700&signature=ea3ca1b44690f20d87b1efbcb3923daa3dc5a9b68f0878b74dd219d602fe97f6&req=dSMvEcB9noFZXfMW1HO4zVvvZ3dkbIomjR%2Bvyv79UsHfQxABcTHGr9gW7XKT%0AQ09xpvXIwszZN3TC57o%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1387933064/eae0ff2784c425eacbfd037ce079/Decisions%2B-%2BIA%2B-%2BFolders.png?expires=1784333700&signature=ea3ca1b44690f20d87b1efbcb3923daa3dc5a9b68f0878b74dd219d602fe97f6&req=dSMvEcB9noFZXfMW1HO4zVvvZ3dkbIomjR%2Bvyv79UsHfQxABcTHGr9gW7XKT%0AQ09xpvXIwszZN3TC57o%3D%0A)

## Creating Folders

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Intelligent Admissions** tab.
3. In the lefthand panel, click **+ Add Folder**.
4. Give your folder a **Name**.
5. Click **Create**.

## Editing + Deleting Folders

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Intelligent Admissions** tab.
3. In the lefthand panel, locate the folder you wish to edit/delete.
4. Click the **three vertical dots next to the folder name.**

   * To edit the folder name, click **Edit**.
   * To delete a folder, click **Delete**.

## Moving Rules to Folders

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Intelligent Admissions** tab.
3. Locate the rule you wish to add to a folder.
4. Click the **three vertical dots** at the end of the row.
5. Click **Move to Folder** and select the folder of your choosing.

---

# Tracking IA Rule Activity

When an IA rule triggers a change on a decision, you can now see exactly which rule was responsible and what happened. Each action is recorded in the decision's **Timeline** tab with the rule name — making it easy to audit automated decisions and identify unexpected behavior.

To view rule attribution details, click on the activity entry in the Timeline. A detail panel opens showing the timestamp, the name of the IA rule that triggered the action, and the specifics of what changed (for example, who was assigned or what stage was updated).

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2197495164/d30e1a9841fc9d3f21944abdf1f4/CleanShot%2B2026-03-24%2Bat%2B17_05_02.png?expires=1784333700&signature=e297a87b752f9d76857284c8cfe1acde963a40a987df059c5a1ee546e65fde67&req=diEuEc13mIBZXfMW1HO4zQatLC6rzTEyqibMkUcQBUuqfe4YH2tObZPrWZM8%0At4HtBGYsSzQY3plISLU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2197495164/d30e1a9841fc9d3f21944abdf1f4/CleanShot%2B2026-03-24%2Bat%2B17_05_02.png?expires=1784333700&signature=e297a87b752f9d76857284c8cfe1acde963a40a987df059c5a1ee546e65fde67&req=diEuEc13mIBZXfMW1HO4zQatLC6rzTEyqibMkUcQBUuqfe4YH2tObZPrWZM8%0At4HtBGYsSzQY3plISLU%3D%0A)

---