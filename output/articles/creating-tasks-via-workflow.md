---
title: Creating Tasks via Workflow
url: https://help.element451.com/en/articles/7960169-creating-tasks-via-workflow
collection: Tasks
---

Use workflows to automate task creation based on user activities

# Overview

Element451's Workflows offer a dynamic way to automate task creation, enhancing efficiency and ensuring timely follow-ups. This article guides you through setting up Workflows with the 'Create Task' action, focusing on aspects specific to workflow-created tasks.

Workflow triggers in Element451 are primarily based on user activities, allowing you to integrate task creation into your daily processes seamlessly. You can automatically generate tasks when specific actions are taken. For instance, you can set up a workflow to create a 'Phone Call Follow-Up' task once a student is admitted or a 'Review Documents' task after a residency form submission.

Unique to workflow-created tasks are "token style" assignees:

|  |  |
| --- | --- |
| **Contact Assignee**  (Internal Tasks) | Assign the task to the assignee of the contact being processed. |
| **Network Role** (Internal Tasks) | Assign the task to the internal user who holds the selected network role (for example, Academic Advisor or Financial Aid Counselor) for the contact being processed. |
| **Workflow Contact** (Contact Tasks) | Assign the task to the contact currently being processed in that workflow step. |

[![](https://downloads.intercomcdn.com/i/o/1195967277/80713367cf760f36afb20ba9/Note.png?expires=1784333700&signature=2eb0b5a97b5162033c24605be5a721f508007e8d884036f1f390cfeac154d725&req=dSEuE8B4moNYXvMW1HO4zRuL9Q%2Fn4DuPCZNvHppYdPyKumcvVMNvPVHyJRJ%2B%0A24%2BkX2w2AZM9kxKcahg%3D%0A)](https://downloads.intercomcdn.com/i/o/1195967277/80713367cf760f36afb20ba9/Note.png?expires=1784333700&signature=2eb0b5a97b5162033c24605be5a721f508007e8d884036f1f390cfeac154d725&req=dSEuE8B4moNYXvMW1HO4zRuL9Q%2Fn4DuPCZNvHppYdPyKumcvVMNvPVHyJRJ%2B%0A24%2BkX2w2AZM9kxKcahg%3D%0A)

This article assumes you have a good understanding of creating Workflows and Rules. You can learn more about these in the [Workflows + Rules Collection](https://help.element451.com/en/collections/124560-workflows-rules).

---

# Step 1: Create the Workflow

1. Navigate to **Data + Automations** > **Workflows** > **All Workflows**.
2. Click the **+ New Workflow** button

   [![](https://downloads.intercomcdn.com/i/o/911542676/b38858b8f3052ba7deb2c782/Screenshot+2023-12-16+at+10.50.09%E2%80%AFPM.png?expires=1784333700&signature=320ae7fef7a34dad4e0ec125d454eb1d9fdee8bab95b5f6fb3ca85a8be91db74&req=fSEmE818m4ZZFb4f3HP0gLUMVvaS%2B1JxQJIBJJKJpw6V8ZSVT%2F3ISrUKCqby%0ATLs%3D%0A)](https://downloads.intercomcdn.com/i/o/911542676/b38858b8f3052ba7deb2c782/Screenshot+2023-12-16+at+10.50.09%E2%80%AFPM.png?expires=1784333700&signature=320ae7fef7a34dad4e0ec125d454eb1d9fdee8bab95b5f6fb3ca85a8be91db74&req=fSEmE818m4ZZFb4f3HP0gLUMVvaS%2B1JxQJIBJJKJpw6V8ZSVT%2F3ISrUKCqby%0ATLs%3D%0A)

   in the top right corner of the header.
3. Provide a **Name** and a short **description** of the workflow.
4. Click **Add** in the top right corner.
5. You will be taken to the edit page for your new workflow, where you can configure your trigger(s) and action(s).

[Explore More: Creating Workflows →](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow)

---

# Step 2: Add Your Action (Task Creation Process)

To begin the task creation process:

1. Click on the **plus sign** in your workflow to add a new action.
2. Select **Create** **Task** from the action type dropdown menu.

---

# Step 3: Configure Task Details

For most fields (Task Template, Task Name, Type, Status, Priority, Description, Subtasks, and Subscribers), refer to the [Creating Tasks Manually](https://help.element451.com/en/articles/8716070-creating-tasks-manually) article.   
​  
✨ **Pro Tip**: Highlight the text in your description to activate the WYSIWYG editor to apply rich formatting (bold, italics, underline, bullet points, numbered lists, hyperlinks, and more).

Below, you will find sections that focus on fields specific to workflow-created tasks.

---

# Assigned To

This field determines whether you're creating an Internal or Contact Task.

* ## Internal Tasks

  Select the individual user(s) or [teams](https://help.element451.com/en/articles/8346250-teams) to whom to assign the task. You also have the option to select **Contact Assignee** (specific to workflows) at the top of the list. It works like a token, assigning the task to the assignee of the contact being processed. You can also select a **Network Role** token, which assigns the task to the internal user who holds that role (for example, Academic Advisor or Financial Aid Counselor) for the contact being processed. Learn more in [Network: Connect Contacts with Internal Users](https://help.element451.com/en/articles/9884014-network-connect-contacts-with-internal-users).

* ## For Contact Tasks:

  Selecting a specific contact task is not an option when assigning contact tasks using a workflow. However, you can select the **Workflow Contact** option at the top of the list. It works like a token, assigning the task to the contact currently processed in that workflow step.

## Assignment Behavior for Internal Task Assignees

This field determines how tasks are distributed among assigned users or teams when more than one is selected.  
​

[![](https://downloads.intercomcdn.com/i/o/1196044905/1a2a4a0af321477fe015b205/Screenshot-2B2023-12-17-2Bat-2B6_24_13-E2-80-AFPM.png?expires=1784333700&signature=2a5ae9b919094132cc1b9d7e0d567b1544d64007fbda1893245af19c6924b989&req=dSEuEMl6mYhfXPMW1HO4zSOtYLzPylNYCtLRr%2FYRSskA3JRB8YL8H5U1Pdw%2F%0A82so0BykZhqKhpwJh6U%3D%0A)](https://downloads.intercomcdn.com/i/o/1196044905/1a2a4a0af321477fe015b205/Screenshot-2B2023-12-17-2Bat-2B6_24_13-E2-80-AFPM.png?expires=1784333700&signature=2a5ae9b919094132cc1b9d7e0d567b1544d64007fbda1893245af19c6924b989&req=dSEuEMl6mYhfXPMW1HO4zSOtYLzPylNYCtLRr%2FYRSskA3JRB8YL8H5U1Pdw%2F%0A82so0BykZhqKhpwJh6U%3D%0A)

* **Selected (Default)**: Assigns tasks to **all** user(s) listed in the *Assigned To* field every time the workflow runs.
* **Rotational**: Assigns the task to a single user from the *Assigned To* field on a rotational basis. The assignment will occur in order each time the workflow runs, and when each person on the list has received an assigned task, the rotation will start back at the beginning.

  + [![](https://downloads.intercomcdn.com/i/o/1196039348/ab862ab86d89ecb6a72626f3/Note.png?expires=1784333700&signature=82d1196361d9cb0c6f0f3a5878ce7bdec7b6a519c624c4dabf672181d5df324b&req=dSEuEMl9lIJbUfMW1HO4zX%2FN7DgdX6tevgsRv1XG3I%2FGCvLm41zxYsCZy1m1%0Ae3m6%0A)](https://downloads.intercomcdn.com/i/o/1196039348/ab862ab86d89ecb6a72626f3/Note.png?expires=1784333700&signature=82d1196361d9cb0c6f0f3a5878ce7bdec7b6a519c624c4dabf672181d5df324b&req=dSEuEMl9lIJbUfMW1HO4zX%2FN7DgdX6tevgsRv1XG3I%2FGCvLm41zxYsCZy1m1%0Ae3m6%0A)

    The rotation history resets **monthly**, starting with the first user, regardless of whether it has reached all users in the cycle. After this reset, the workflow begins anew, starting with the first user in the rotation rather than continuing from the last point. If you often have just a few assignments each month, consider opting for a balanced assignment method instead. This approach considers the total workload for each user on the list, ensuring tasks are distributed more evenly.
* **Balanced Assignment**: Assigns the task to the user with the lowest number of assigned tasks, balancing workload among all individuals in the Assigned To field.

---

# Due Date Type and Due Date

When a workflow creates a task, you can set the due date in two ways:

## Exact

* Sets a specific due date and time for each task created by the workflow no matter when the workflow runs—for example, Sept 1, 2024, at noon.
* Please note that workflows will create overdue tasks if this date is past.

## Relative

* Sets a date in the future *relative* to when the workflow creates the task. For example, you could put a task due five days after an inquiry submits an RFI form.
* Ideal for ongoing activity-based follow-up tasks.

---