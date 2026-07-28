---
title: Creating + Managing Journeys
url: https://help.element451.com/en/articles/9492988-creating-managing-journeys
collection: Journeys
---

Learn how to create and manage Journeys to track and manage students' progression through various stages.

# Overview

Journeys in Element451 help you track and manage students' progression through various stages, from initial contact to enrollment, event participation, or program completion. Using pre-configured templates or creating custom journeys, you can tailor the tracking process to fit your specific needs, ensuring streamlined and effective student data and activities management.

---

# Before Creating a New Journey

Before building out a Journey, it’s essential to brainstorm and organize all the steps, triggers, conditions, and actions. This preparation will ensure a smooth and efficient setup process.

**Example: Tracking a Student’s Progress for a Presidential Scholarship**

Consider the following example, where we track a student’s journey through applying for a presidential scholarship. Each step represents what we would consider a custom milestone, while triggers indicate what should happen for the step to be marked complete. Conditions specify any additional criteria that must be evaluated before completion, and actions define what occurs once the step is completed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Step Name** | **Trigger** | **Condition** | **Actions** |
| Pre-Qualification | Decision-Admitted | ACT >27 GPA >3.75 | * Assign Task to Personally Invite to Scholars Day * Add Label for President Pre-Qualified * Run Workflow with previous President Scholars' testimonies |
| Full-Qualification | Attended Scholars Day |  | * Assign Task to Personally Invite to Submit President Application * Remove President Pre-qualified Label * Add Label for President Full Qualification * Run Workflow with Start President Application Reminders |
| Started President Application | Start President Application |  | * Run Workflow to Submit President Application |
| Submitted President Application | Submit President Application |  | * Remove President Full Qualification Label * Add Label for President Applicant |
| Interview | Updated Decision Status | Status = Interview for President Application |  |
| Final Review | Updated Decision Status | Status = Finalist for President Application |  |
| President Scholarship Awarded | Updated Decision Status | Status = Awarded for President Application | * Assign Task to Personally Congratulate * Assign Task to Mail Packet * Remove President Applicant Label * Add President Winner Label |

---

# Creating a New Journey

When creating a new Journey, you have the option to use a template with preconfigured settings and components or to start from scratch. Both processes are outlined below:

## Using a Template (Application, Event, or Student Search)

1. Navigate to **Data + Automations** > **Journeys** > **All Journeys**.
2. Click the **+ New Journey** button in the module header.
3. **Choose Template**: Select a preconfigured template that provides a guide to get started. If you want to start from scratch, select **Custom** and follow the process outlined in the [next section](https://help.element451.com/en/articles/9492988-creating-managing-journeys#h_2b59c265d4).

   * **Application**: A template that tracks the progression of a prospective student from initial contact through enrollment
   * **Event**: A template that tracks the progression of a student from enrollment through completing a degree program
   * **Student** **Search**: A template that tracks the basic progression of a student from enrollment through completing a non-degree program
   * **Custom**: Create your own journey (start from scratch).  
     ​

     [![](https://downloads.intercomcdn.com/i/o/1085917101/e1056ef7b4973adc01d99fd8/Screenshot+2024-06-18+at+1_50_10%E2%80%AFPM.png?expires=1784333700&signature=19f46b30aabb63430f266241473c3a79fbf5bcdb967844eb04a39c0d4b638786&req=dSAvE8B%2FmoBfWPMW1HO4zazITUR60rTyGrxeSE7Ywfjuz7ca6F7%2FOrlhcy%2Fm%0AS2bq%0A)](https://downloads.intercomcdn.com/i/o/1085917101/e1056ef7b4973adc01d99fd8/Screenshot+2024-06-18+at+1_50_10%E2%80%AFPM.png?expires=1784333700&signature=19f46b30aabb63430f266241473c3a79fbf5bcdb967844eb04a39c0d4b638786&req=dSAvE8B%2FmoBfWPMW1HO4zazITUR60rTyGrxeSE7Ywfjuz7ca6F7%2FOrlhcy%2Fm%0AS2bq%0A)
4. **Configure Journey Settings**: Based on the template option selected in the prior step, configure the settings outlined below:

   * **Application Template**

     + Past Activities: Journey evaluation will include activities that happened before the user was enrolled
     + Admitted Decision Status\*
     + Include Deposit Step
     + Application, Major, Term, Campus, Degree, Student Type
   * **Event Template**

     + Past Activities: Journey evaluation will include activities that happened before the user was enrolled
     + Enroll Selected Segment?
     + Trigger Segment\*
     + Event\*
     + Event Invite Communication\*
     + Post Event Communication\*
   * **Student Search Template**

     + Enroll Selected Segment?
     + Trigger Segment\*
     + Received Communication\*
5. Once you've configured the settings for the template-based Journey, click **Save**. The journey will be added to the All Journeys list. By default, the Journey is set to inactive.
6. Click the **three vertical dots** ![](https://downloads.intercomcdn.com/i/o/1085942049/e7139d6ab99043804154b931/More+Icon2.png?expires=1784430000&signature=b879303d619894e82e7fdf7923f472c51a309c2d9b476f4f11467e980dd81a49&req=dSAvE8B6n4FbUPMW3Hu4gZ2yqLXKbO577KL31DagQuVGG%2BQ%2BuOXAa9rJ58rA%0AEg%3D%3D%0A) icon at the end of the row for that new Journey.
7. Select **Edit**. The Journey editor will open.
8. You can now review and edit the pre-configured settings, such as the Journey name, color scale, triggers, steps, etc. These settings are explained below in the Custom Journey details.
9. Once you have reviewed and made edits as needed, you can activate your Journey.

## Custom Journey

1. Navigate to **Data + Automations** > **Journeys** > **All Journeys**.
2. Click the **+ New Journey** button in the module header.
3. **Choose Template**: Select **Custom**-Create Your Own Journey.
4. **Configure Journey Settings**:

   * **Name**: Give your Journey a name by entering text in the header.
   * **Journey** **Active**: This enables or disables this Journey. An inactive journey will not listen for or evaluate any user events.
   * **Color** **Scale**: This color is the basis for the Journey path as it is displayed on the Journeys profile card.   
     ​

     [![](https://downloads.intercomcdn.com/i/o/645484522/91d39ecfa573e3c7705355e3/Screen+Shot+2023-01-03+at+3.00.37+PM.png?expires=1784333700&signature=b0f33352d7e5f505c1025d2656b693d10b3767b5e4657e7fefc6ac107bd724ea&req=ciQiEsF6mINdFb4f3HP0gJiHGfCazvl8ZvxWhbjDQ66a8Ns0Ptu1XzPUVJx9%0Au1A%3D%0A)](https://downloads.intercomcdn.com/i/o/645484522/91d39ecfa573e3c7705355e3/Screen+Shot+2023-01-03+at+3.00.37+PM.png?expires=1784333700&signature=b0f33352d7e5f505c1025d2656b693d10b3767b5e4657e7fefc6ac107bd724ea&req=ciQiEsF6mINdFb4f3HP0gJiHGfCazvl8ZvxWhbjDQ66a8Ns0Ptu1XzPUVJx9%0Au1A%3D%0A)
   * **Conversion** **Window**: This setting establishes the time the Journey will continue to evaluate events after someone has started the Journey. New events will no longer be evaluated when the conversation window is over.
   * **Past** **Activities**: This optional mode allows you to evaluate actions that may have happened before the Journey was activated.

     + It only applies to **Steps** and **Exit Events** for users **already enrolled**—it does **not** apply to **Journey Triggers**.
     + *Toggling on Past Activities will not enroll users who experienced the Trigger before the Journey was activated. It only evaluates past activities for users who are already part of the Journey.*
   * **Description**: Add text to explain to others the Journey.
5. Add **Journey Components**:

   * **Journey Triggers**

     + After you select a trigger, you must configure additional settings for that specific trigger.
   * **Journey Steps**

     + After you select a step, you will be prompted to add conditions and actions. Both of these are **optional**.

       - **Conditions:** Before marking the step complete, are there any additional things to check?
       - **Actions:** Actions execute when the enrolled person completes this step/event.
   * **Add Exit Triggers**

     + After you select an exit trigger, you will be required to configure additional settings for that specific trigger.

     If you need help with Journey Components, our [Getting Started with Journeys](https://help.element451.com/en/articles/6825003-journeys) article comprehensively explains each component.
6. Once your settings are configured and components have been added, click **Save**.

---

# Editing, Duplicating, + Deleting Journeys

To manage your existing Journeys:

1. Navigate to **Data + Automations** > **Journeys** > **All Journeys**.
2. Locate the Journey you wish to manage from the All Journeys list.
3. Click the **three vertical dots** ![](https://downloads.intercomcdn.com/i/o/1085942049/e7139d6ab99043804154b931/More+Icon2.png?expires=1784430000&signature=b879303d619894e82e7fdf7923f472c51a309c2d9b476f4f11467e980dd81a49&req=dSAvE8B6n4FbUPMW3Hu4gZ2yqLXKbO577KL31DagQuVGG%2BQ%2BuOXAa9rJ58rA%0AEg%3D%3D%0A) icon at the end of the row for that Journey.
4. Select the action you wish to take: **Edit**, **Duplicate**, or **Delete**.

[![](https://downloads.intercomcdn.com/i/o/1085933023/ec99e0006182924421afc8e1/Screenshot+2024-06-18+at+2_05_28%E2%80%AFPM.png?expires=1784333700&signature=d39a2e85de602c70db5f432d5deb2b4e89ee11c360f0278c8f4052cda1e92a04&req=dSAvE8B9noFdWvMW1HO4zaLf2fngYAAnYY6%2F%2BrOMQBiYwQGT7g8d%2BT8fWcpY%0AZJyfKt3XyQZPEZLZ7O8%3D%0A)](https://downloads.intercomcdn.com/i/o/1085933023/ec99e0006182924421afc8e1/Screenshot+2024-06-18+at+2_05_28%E2%80%AFPM.png?expires=1784333700&signature=d39a2e85de602c70db5f432d5deb2b4e89ee11c360f0278c8f4052cda1e92a04&req=dSAvE8B9noFdWvMW1HO4zaLf2fngYAAnYY6%2F%2BrOMQBiYwQGT7g8d%2BT8fWcpY%0AZJyfKt3XyQZPEZLZ7O8%3D%0A)

##

---