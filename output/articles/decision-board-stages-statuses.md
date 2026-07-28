---
title: Decision Board: Stages + Statuses
url: https://help.element451.com/en/articles/9210610-decision-board-stages-statuses
collection: Decisions
---

Optimize your application evaluation process with the Decision Board, managing stages, statuses, and transitions effectively.

# Overview

The Decision Board encapsulates your entire application review/evaluation process. It is organized into **Stages**, each represented by cards, and includes **Statuses** and **Transitions**.

* **[Stages](#h_2231581106)**: These are potential steps in your evaluation process. Not every application needs to pass through each stage.
* **[Statuses](#h_2c33f237f5)**: Offer deeper insights into the application's current state within a stage.
* **Transitions**: Define potential next stages for an application, allowing you to bypass irrelevant stages for different student or application types. This flexibility is helpful when managing varied application processes.

## Accessing Decision Board, Statuses, + Stages

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Board** or **Statuses** tab, depending on your intent. Stages are accessed from the Board tab.

[![](https://downloads.intercomcdn.com/i/o/1029263914/4ddf2e08a75584b3d7a65d95/Decisions+-+Accessing.png?expires=1784333700&signature=6087406a34d3fac667a9872fea252ff71eedc8c5cbeeb8167aae94f5c7a31e1f&req=dSAlH8t4noheXfMW1HO4zW1UnOZjPuPYSODAbHHoZsZcRWg%2FPoGXPwuVG91v%0ASGqCBOt9EAOT558eLU8%3D%0A)](https://downloads.intercomcdn.com/i/o/1029263914/4ddf2e08a75584b3d7a65d95/Decisions+-+Accessing.png?expires=1784333700&signature=6087406a34d3fac667a9872fea252ff71eedc8c5cbeeb8167aae94f5c7a31e1f&req=dSAlH8t4noheXfMW1HO4zW1UnOZjPuPYSODAbHHoZsZcRWg%2FPoGXPwuVG91v%0ASGqCBOt9EAOT558eLU8%3D%0A)

## View an example

To better understand how these components work together, here is an example of an *International F-1 Review* Stage designed to help process international student applications. Within the Stage, you can see five statuses: *In Review, F-1 Docs Not Verified, F-1 Docs Pending, F-1 Docs - Verified, and Withdrawn.* Then, we allow the application to be moved to all subsequent stages for the transition setting.  
​

[![](https://downloads.intercomcdn.com/i/o/1029242392/b543a463c9290c56c01e2ed9/Decisions+-+Board-Stages-Statuses+Example.png?expires=1784333700&signature=e549f87fd25f68ac75f241873e7ed2b7ef58aec1290892642d15a100fe3074f6&req=dSAlH8t6n4JWW%2FMW1HO4zUoTQFRoRe6VOzaE99tDzTvxcdXAoMKJZBV99KYU%0ATa0mwe1kD8EYg0P1vUA%3D%0A)](https://downloads.intercomcdn.com/i/o/1029242392/b543a463c9290c56c01e2ed9/Decisions+-+Board-Stages-Statuses+Example.png?expires=1784333700&signature=e549f87fd25f68ac75f241873e7ed2b7ef58aec1290892642d15a100fe3074f6&req=dSAlH8t6n4JWW%2FMW1HO4zUoTQFRoRe6VOzaE99tDzTvxcdXAoMKJZBV99KYU%0ATa0mwe1kD8EYg0P1vUA%3D%0A)

Here are a few takeaways from this example:

* We recommend adding an "In Review" and "Withdrawn" or similar statuses at every stage. This is because the "In Review" lets you know that the application needs action, and the Withdrawn status can help you track and monitor at which stage(s) students are withdrawing.
* You'll notice that the custom statuses are quite descriptive. Choosing descriptive statuses helps you and your team members quickly assess the position of an application. It's also important to note that the statuses displayed here are internal; when creating custom statuses, you will select an 'action' which is what is displayed to the student. We cover this in more detail in the [Statuses](https://help.element451.com/en/articles/9210610-decision-board-stages-statuses#h_2c33f237f5) section below.
* The 'transitions to' setting is configured to allow applications to move from this stage to all subsequent stages. However, if there is a stage after this one that does not apply to international students, you would uncheck this box and select the next relevant stage to which the application should move.

## View things you should consider before building your board

* Before setting up your decision board, it's essential to thoroughly map out your entire decision process from start to finish.
* Keep in mind that not every application needs to pass through each stage you create. If your review process varies by student type or another factor, consider designing specific stages tailored to these differences.
* Additionally, you have the option to automate the progression of an application from one stage to another, streamlining your workflow using [Intelligent Admissions](https://help.element451.com/en/articles/9241624-intelligent-admissions-decision-rules-automation).
* New stages, statuses, or transitions are not automatically assigned to permission groups, so they will only be visible to you or other internal users once you adjust permissions. [Click here for a step-by-step guide to adjusting permission groups](https://help.element451.com/en/articles/9235440-decisions-cohorts).

---

# Stages

**Stages** serve as the steps in your application review process.

It's important to note that not all applications must progress through every stage. For example, if your review process differs between undergraduate and graduate applications, you should create distinct stages tailored to each. Ensure that stages are descriptively named to facilitate easy identification and reference.

Applications can be manually moved between stages or automatically transitioned using an Intelligent Admissions rule.

## System Stages

By default, your board includes three immutable stages added by Element451:

* **Ready for Review**: When an application is submitted, it is automatically placed in the “Ready for Review” stage with the status ‘Submitted.’ From there, you can manually review and update the status/stage or use **intelligent admissions** to automatically move the application to where it needs to go based on conditions.
* **Final Decision**: This stage helps you organize and review which applications have completed the evaluation process.
* **Release**: When an application is moved to the Release stage, the student can see the decision in their application portal. The student will see the status as “in review” until the application reaches the “release” stage.

You can introduce custom stages between "Ready for Review" and "Final Decision" based on your process. Instructions on creating new stages will follow.

## Adding Stages

As mentioned in the overview, the cards represent stages on your board.

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on either the **Board** tab.
3. Click the blue button in the bottom right corner.
4. Provide a **name** for your Stage.
5. Using the dropdown menu, select a **status** or **multiple** **statuses** relevant to this stage. If you need to add a new status, review the next section to learn how.

   * ![](https://downloads.intercomcdn.com/i/o/1038713865/ffb8327d1b01b6e272b34839/Important+-+Orng.png?expires=1784430000&signature=205cb4b7d0c23278b3329ae053b5cad6872643abae1d1df7b2d54ead48a5f1f9&req=dSAkHs5%2FnolZXPMW3Hu4gaIaGJTxGMH1Iw08THoDGixcYR4ljRpr1ZOymEUZ%0AyA%3D%3D%0A) You must select **at least one status**, or the stage will not save.
6. Click **Add**.
7. The stage card will be added to your board.
8. **Add** **Transition(s)**: Use the **All** **Stages** checkbox to allow the application to move to all subsequent stages, or use the **Add** **Transition** button to limit specific stage transitions. Current transitions will be shown as a dropdown field that can be changed without adding a new one.
9. To change the stage's position, follow the instructions below for reordering stages.
10. **Adjust your Permission Groups**: New stages are not automatically assigned to permission groups, so they will only be visible to you or other internal users once you adjust permissions. [Click here for a step-by-step guide to adjusting permission groups](https://help.element451.com/en/articles/9235440-decisions-cohorts).

## Editing, Reordering, + Deleting Stages

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on either the **Board** tab.
3. Locate the stage/card you wish to edit, reorder, or delete.
4. Follow the instructions below.

### Editing:

* **Name**: Click anywhere on the name. Changes are saved automatically.
* **Statuses**: Hover over the statuses on the card. A pencil icon will appear; click the icon. The Edit Statuses dialog window will open. Once you've made your updates, click **Update**.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1029288403/fc392c4eec92b816fb73f8ee/Decisions+-+Edit+Statuses.png?expires=1784333700&signature=1711bd0619fdaef74f95e9967321240b3ccdec29e551a4f4347c9f3a0dffa420&req=dSAlH8t2lYVfWvMW1HO4zd0%2BjHvTescIYVOD2c3L5rf%2B%2FBcduMbxeMitLlg5%0A5fFq%0A)](https://downloads.intercomcdn.com/i/o/1029288403/fc392c4eec92b816fb73f8ee/Decisions+-+Edit+Statuses.png?expires=1784333700&signature=1711bd0619fdaef74f95e9967321240b3ccdec29e551a4f4347c9f3a0dffa420&req=dSAlH8t2lYVfWvMW1HO4zd0%2BjHvTescIYVOD2c3L5rf%2B%2FBcduMbxeMitLlg5%0A5fFq%0A)
* **Transitions**: Use the **All** **Stages** checkbox to allow the application to move to all subsequent stages or use the **Add** **Transition** button to limit specific stage transitions. Current transitions will be shown as a dropdown field that can be changed without adding a new one.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1029289395/0b8347341f959903db2046d9/Decisions+-+Edit+Transitions.png?expires=1784333700&signature=f04489a4a8e0bd5d4e43cac404b7e4ebb5113a50e0e36a97dccc65418af10dd1&req=dSAlH8t2lIJWXPMW1HO4zaF1u4smmjM3PEI1VFg37o8DbOQhTEKIkQk6zqci%0AIWVH%0A)](https://downloads.intercomcdn.com/i/o/1029289395/0b8347341f959903db2046d9/Decisions+-+Edit+Transitions.png?expires=1784333700&signature=f04489a4a8e0bd5d4e43cac404b7e4ebb5113a50e0e36a97dccc65418af10dd1&req=dSAlH8t2lIJWXPMW1HO4zaF1u4smmjM3PEI1VFg37o8DbOQhTEKIkQk6zqci%0AIWVH%0A)

### Reordering:

* To reorder stages, drag and drop the card to the desired location using the double-sided arrow in the top left corner of the card.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1029207991/f31cd4ef9452d30f0e3dc7fd/Decisions+-+Reorder+Stages.png?expires=1784333700&signature=9bf0c17150f936b2e46256b820e6b7f329bf455cbeb61ccebd9dae79bd328340&req=dSAlH8t%2BmohWWPMW1HO4zfRyRfb80AbuJ8OingeKzPrgZt86yOpcJ6OCpcjj%0AiTg2%0A)](https://downloads.intercomcdn.com/i/o/1029207991/f31cd4ef9452d30f0e3dc7fd/Decisions+-+Reorder+Stages.png?expires=1784333700&signature=9bf0c17150f936b2e46256b820e6b7f329bf455cbeb61ccebd9dae79bd328340&req=dSAlH8t%2BmohWWPMW1HO4zfRyRfb80AbuJ8OingeKzPrgZt86yOpcJ6OCpcjj%0AiTg2%0A)

### Deleting:

* Click the **three** **vertical** **dots** icon in the top right corner of the card and select **Delete**. You'll be asked to confirm your action.  
  ​

  ![](https://downloads.intercomcdn.com/i/o/1031296279/cbf8f4ac8380362c9adb41a9/Important+-+Orng.png?expires=1784430000&signature=0f8a356d9ccdb0e2274763d95301531b55dcc2f88b2c95780cd179cb6b483a90&req=dSAkF8t3m4NYUPMW3Hu4gak8isZ5%2F4sp%2F3OMU37UE3%2Bm%2FKi3nyv%2B9ECZN1ec%0AFA%3D%3D%0A) When deleting a stage that contains decisions, you will receive a warning. Before permanently deleting a stage, please ensure all decisions are transferred to another stage.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1029208866/3619852950956230a73b6271/Decisions+-+Delete+Stage.png?expires=1784333700&signature=b6368f37a6a5aced9fe966a07eb96bb847499df9a250551497889787cb7cc0fa&req=dSAlH8t%2BlYlZX%2FMW1HO4zcqKGKH4EyKAjj4SdWQuUtYlKQXhta%2BNNx6ym%2Beo%0A%2FClB%0A)](https://downloads.intercomcdn.com/i/o/1029208866/3619852950956230a73b6271/Decisions+-+Delete+Stage.png?expires=1784333700&signature=b6368f37a6a5aced9fe966a07eb96bb847499df9a250551497889787cb7cc0fa&req=dSAlH8t%2BlYlZX%2FMW1HO4zcqKGKH4EyKAjj4SdWQuUtYlKQXhta%2BNNx6ym%2Beo%0A%2FClB%0A)

#

---

# Statuses

**Statuses** serve an internal function, providing specific details about an application's position within a stage. They are designed to be descriptive and are intended for staff use to manage the review process effectively. Each status is linked to an **Action** that the student sees in their application portal, ensuring clarity and consistency in communication. See example below:  
​

[![](https://downloads.intercomcdn.com/i/o/1033592149/05a8c4baa6becea87d3c0ec6/Decisions+-+Action+-+Portal.png?expires=1784333700&signature=c6b2a78ab8c5987139606f0477bd5be11470a4bb667f4ddce2f85a8db3c9c7c5&req=dSAkFcx3n4BbUPMW1HO4zR11AOVFv6t0UugIIO5LFEqQBFH5rf%2B5X6cseFv4%0AcleCMSpGJ1R7fL4hQdo%3D%0A)](https://downloads.intercomcdn.com/i/o/1033592149/05a8c4baa6becea87d3c0ec6/Decisions+-+Action+-+Portal.png?expires=1784333700&signature=c6b2a78ab8c5987139606f0477bd5be11470a4bb667f4ddce2f85a8db3c9c7c5&req=dSAkFcx3n4BbUPMW1HO4zR11AOVFv6t0UugIIO5LFEqQBFH5rf%2B5X6cseFv4%0AcleCMSpGJ1R7fL4hQdo%3D%0A)

For example, an internal status might be "Denied-Low GPA." While informative for the review team, it’s not appropriate for student viewing. Instead, Element451 offers a predefined list of standard actions such as 'in review,' 'admitted,' or 'deferred.' These actions are visible to students and maintain a consistent and professional tone in communications.  
​

## Actions

Each status you create must be paired with a predefined action. These actions are immutable and standardized by Element451 to ensure uniformity across communications:

* **To** **Review**: Indicates that the application review has not yet begun. Note: Students will see "To Be Reviewed."
* **In Review**: Indicates that the application is currently being processed.
* **Admitted**: Confirms that the student has been accepted.
* **Deferred**: Signifies that the decision on the application has been postponed.
* **Denied**: Communicates that admission has been rejected without specifying internal reasoning. ***The Denied status is displayed as "Not Admitted" on the application portal.***
* **Conditional Offer**: Indicates that the student has been given an offer of admission contingent on meeting specific conditions or requirements
* **Waitlisted**: Signifies that the student has not been denied admission but must wait for an available slot to open up before an offer can be extended.
* **Withdrawn**: Indicates that the application has been withdrawn.

This approach helps maintain privacy and professionalism, ensuring that internal assessments do not directly influence student perceptions.

## Recommended Statuses

Element451 suggests incorporating these three statuses into every stage:

* **In** **Review**: Indicates action is required, or that processing hasn't occurred.
* **Pending**: Provides a status for holding applications when an immediate decision isn't possible, serving as a reminder for future review.
* **Withdrawn**: Enables tracking and monitoring of student withdrawals at various stages."

## System Statuses

By default, you'll encounter one status: **Submitted**, an addition by Element451 that cannot be removed.

Upon submission, applications seamlessly transition to the '**Ready for Review**' stage, marked with the status '**Submitted**.'

## Adding Statuses

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on either the **Statuses** tab.
3. Click the blue button in the bottom right corner.
4. Provide a **name** for your Status.
5. The Slug will generate automatically, but you can change it.
6. Select an Action.

   * Remember, each status is associated with an **action**. An action is what the student sees when they log into their application portal to check their status. Action options are: to review, in review, admitted, deferred, denied, conditional offer, waitlisted, and withdrawn. Therefore, your statuses can be more descriptive, such as 'Admitted - Top 10%' or 'Denied - Low GPA,' as the student will only see 'Admitted' or "Denied.'
7. Use the color picker to select the chip color for that status.
8. Click **Create**.
9. **Adjust your Permission Groups**: New statuses are not automatically assigned to permission groups, so they will only be visible to you or other internal users once you adjust permissions. [Click here for a step-by-step guide to adjusting permission groups](https://help.element451.com/en/articles/9235440-decisions-cohorts).

## Editing + Deleting Statuses

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on either the **Statuses** tab.
3. Locate the status you wish to edit or delete.
4. Follow the instructions below.

### Editing:

1. Click the pencil icon at the end of the row.
2. Make your edits using the Edit Status dialog window.
3. Click **Update**.

### Deleting:

1. Click the **trashcan** icon at the end of the row.
2. Confirm your action.

---