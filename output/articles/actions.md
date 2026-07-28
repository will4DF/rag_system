---
title: Actions
url: https://help.element451.com/en/articles/1500292-actions
collection: Workflows + Rules
---

Discover the functionality, types, and implementation of Actions in Workflows + Rules.

# Overview

Actions in Workflows + Rules are what make things happen. They're the steps defining each Contact's outcome. For instance, actions can send a communication like an email or SMS, submit a completed application, or apply a label such as "prospect" to a person's profile.

### Action Types

There is a wide range of [action types](#h_2088cb5333). Each type serves a unique purpose, enabling you to customize your Workflow or Rule precisely.

All action types are available when using Workflows or a **triggered** Rule.

* If you are using a **scheduled** Rule, your action types are limited to `create login token`, `create profile`, `validate phone numbers`, and `run rule`.

### Multiple Actions per Step

You can add more than one action to a single step. This flexibility lets you handle different tasks simultaneously.

### Conditions for Tailored Actions

If you're using [conditions](https://help.element451.com/workflows/conditions) to have more granular control over your actions and steps, you can have an action for each "yes" and "no" branch. You may also add more than one action to a branch.

---

# How to Add an Action

The process of adding Actions is outlined in our help articles on creating Workflows + Rules:

* **Workflows**

  + [Adding an Action a New Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow#h_73b1e4802c)
  + [Adding an Action to an Existing Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow#h_3d3964e6d7)
* **Rules**

  + [Adding an Action to a New Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule#h_d6f11c33df)
  + [Adding an Action to an Existing Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule#h_90d410f7be)

---

# Types of Actions

## Activities

* **Add Custom Activity**

  + Add a custom activity that happened outside of Element451.

## Applications

* **Move to a new campus**

  + Move applications from one campus to another.
* **Move to a new degree**

  + Move applications from one degree to another.
* **Move to a new major**

  + Move applications from one major to another.
* **Move to a new school**

  + Move applications from one school to another.
* **Move to a new student type**

  + Move applications from one student type to another.
* **Move to a new term**

  + Move applications from one term to another.
* **Register Application as Decision**

  + Create a decision for submitted applications.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205728360/0344c0530f1123749d538535ca98/Note.png?expires=1784333700&signature=967a1d3a60af2c2b76ccf39a3f4b7f7a542812e33ed300adbb5774162015d2f6&req=dSInE858lYJZWfMW1HO4zZ9Oo1EmrTics8rEWB1Rt9q%2FEr1KCuLEUczDfgEo%0A0ecg%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205728360/0344c0530f1123749d538535ca98/Note.png?expires=1784333700&signature=967a1d3a60af2c2b76ccf39a3f4b7f7a542812e33ed300adbb5774162015d2f6&req=dSInE858lYJZWfMW1HO4zZ9Oo1EmrTics8rEWB1Rt9q%2FEr1KCuLEUczDfgEo%0A0ecg%0A)

    When using this action, the application must have a **submitted** status for a decision to be created.
* **Submit Application**

  + Automatically submit completed applications.

💡 **Apply to Application Status:** The **Move to…** actions include an **Apply to Application Status** selector that controls which applications the action affects: **Unsubmitted** (the default), **Submitted**, or **All**. This lets a workflow set a value for a specific application field, such as major, student type, or campus, on applications that have already been submitted, not just unsubmitted ones. Existing workflows keep their current behavior because the selector defaults to Unsubmitted.

## Campaigns

* **Send Communication**

  + Send an ongoing communication.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205728834/9eb281e3f71b1cf3796e756b8c38/Did+You+Know.png?expires=1784333700&signature=c46181f6812db8d8ac0bcabc0481cb779a41460b4de0624b9ea0eee8004854ba&req=dSInE858lYlcXfMW1HO4zW%2BGCU7SRaejWQek753l61KVBGY2T927f0iVHXwx%0AAZdn%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205728834/9eb281e3f71b1cf3796e756b8c38/Did+You+Know.png?expires=1784333700&signature=c46181f6812db8d8ac0bcabc0481cb779a41460b4de0624b9ea0eee8004854ba&req=dSInE858lYlcXfMW1HO4zW%2BGCU7SRaejWQek753l61KVBGY2T927f0iVHXwx%0AAZdn%0A)

    The *Send Communication* action allows you to set the Time to Send setting to **User Preferred Open Time** to send the campaign when the contact is most likely to open it based on previous activity.  
    ​

    [Learn More: Preferred Time to Send](https://help.element451.com/en/articles/8857428-preferred-time-to-send)

## Labels

* **Add Label**

  + Add a label if not already present.
* **Remove** **Label**

  + Remove a label from a person.
* **Set** **Territory**

  + Set the person's territory.

## Milestones

* **Set Milestone - Application Deposit**

  + Add a deposited milestone.
* **Set Milestone - Application Start**

  + Add an application start milestone.
* **Set Milestone - Application Submit**

  + Add an application submit milestone.
* **Set Milestone - Checklist Complete**

  + Add a checklist complete milestone.
* **Set Milestone - Date of Inquiry**

  + Add a date of inquiry (prospect) milestone.
* **Set Milestone - Defer**

  + Add a defer milestone.
* **Set Milestone - Enrolled**

  + Add an enrolled milestone.
* **Set Milestone - Interview**

  + Add an interview milestone.
* **Set Milestone - On Hold**

  + Add a hold milestone.
* **Set Milestone - Unsubscribe Email**

  + Add an email unsubscribe milestone.
* **Set Milestone - Unsubscribe SMS**

  + Add an SMS unsubscribe milestone.
* **Set Milestone - Visit**

  + Add a visit milestone.
* **Set Milestone - Waitlist**

  + Add a waitlist milestone.
* **Set Milestone - Withdrawn**

  + Add a withdrawn milestone.

## Tasks

* **Create Task**

  + Create a new related task.

## Users

* **Add network connection:** Add a network connection to another user.
* **Add custom source to user:** Add a custom source.
* **Change assignee:** Set the person's assignee (*an individual or a [Team](https://help.element451.com/en/articles/8346250-teams)).*

  + When using the ***Change Assignee*** action, you can configure the [Assignment Behavior](https://help.element451.com/en/articles/8857504-assignment-behavior) to determine how the internal user is assigned to a contact.
* **Remove assignee:** Clear a person's assignee.
* **Set user's custom date property:** Set a date value for a custom field.
* **Set user's custom property:** Set a value for a custom field (value must be exact).
* **Set user's property:** Set a value for a system field (value must be exact).

### Advanced Features When Using Set User's Actions

* **Formula Fields**

  + Add custom-calculated fields by employing formulas
  + Works with any of the set user's actions (custom date property, custom property, or property)

  [Read more about custom-calculated fields here](https://help.element451.com/en/articles/8857623-formula-field).

* **AI Workflow Evaluations**

  + Dynamically generate values by selecting **AI Prompt** as the property’s value. This allows AI to populate custom fields with relevant, real-time data based on predefined criteria, unlocking powerful data manipulation possibilities.
  + Works with set user's custom property or set user's property actions.

  [Read more about AI Workflow Evaluations at theend of this article](#h_0a26c8013f).

## Webhooks

* **Execute** **Webhook**

  + Execute Webhook for the person

## Workflows

* **Abort Workflow**

  + Finish the current workflow (stops processing but does not remove the record).
* **Enroll to Workflow**

  + Enroll the person in the selected workflow.

    - ***Apply Overlapping Enrollment***: This setting allows you to enroll a user in the same workflow more than once simultaneously for different applications. This option is only available when using `application`, `decision`, and `event signup` triggers.  
      ​

      [![](https://downloads.intercomcdn.com/i/o/1038677470/89aa312a89c09f4fe1a9efe8/Workflows+-+Actions+-+Overlapping+Enrollment.png?expires=1784333700&signature=8b6be42ce3f39e2a80e46ecce763d6504faf91c957e110253114696290656cc6&req=dSAkHs95moVYWfMW1HO4zYFTL0UxPGuFBtf1c%2BtfAN%2BXcQLdwObtk987rG6V%0Arv1p%0A)](https://downloads.intercomcdn.com/i/o/1038677470/89aa312a89c09f4fe1a9efe8/Workflows+-+Actions+-+Overlapping+Enrollment.png?expires=1784333700&signature=8b6be42ce3f39e2a80e46ecce763d6504faf91c957e110253114696290656cc6&req=dSAkHs95moVYWfMW1HO4zYFTL0UxPGuFBtf1c%2BtfAN%2BXcQLdwObtk987rG6V%0Arv1p%0A)

      **How does it work?**

      When enabled, users can be enrolled in the same workflow multiple times simultaneously, provided each enrollment is associated with a unique trigger context, such as an application registration ID or event signup ID. Overlapping enrollment is not available for workflows triggered by joined segments or manual enrollments, as these do not have a specific trigger context.  
      ​
* **Finish Workflow**

  + Finish the current workflow (stops processing but does not remove the record).
* **Remove from Workflow**

  + Remove from the workflow (stops processing and deletes any record of this run).

---

# AI Workflow Evaluations

We e've temporarily removed access to the AI Workflow Evaluation action, while the feature under goes updates and optimization. We hope to restore this feature in the near future.

When using the **Set User’s Property** or **Set User’s Custom Property** workflow actions, you can dynamically generate values **by sele**cting **AI Prompt** as the property’s value. This allows AI to populate custom fields with relevant, real-time data based on predefined criteria.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1400210571/93b48e6cb359ff85a36f379dd2ed/AI+Workflow+Eval.png?expires=1784333700&signature=4dda783deda755893fa637a2a88381d47b1007fc287be8ef4dfc629755205961&req=dSQnFst%2FnYRYWPMW1HO4zThB8dEV%2B71kn9TKNr3a2IxFOz0yzYj1JrNJ9olD%0AYzDAwV7Rnxubmjz1Czw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1400210571/93b48e6cb359ff85a36f379dd2ed/AI+Workflow+Eval.png?expires=1784333700&signature=4dda783deda755893fa637a2a88381d47b1007fc287be8ef4dfc629755205961&req=dSQnFst%2FnYRYWPMW1HO4zThB8dEV%2B71kn9TKNr3a2IxFOz0yzYj1JrNJ9olD%0AYzDAwV7Rnxubmjz1Czw%3D%0A)

## How It Works

1. Ensure '**AI Workflow Evaluations**' is enabled in [Billing Settings](https://help.element451.com/en/articles/8471334-general-settings).
2. **Select an Action** – Choose **Set User’s Property** or **Set User’s Custom Property** within your workflow.
3. **Choose AI Prompt** – In the **Value** field, select **AI Prompt** as the data source.
4. **Enter an AI Prompt** – Provide a structured prompt for AI to generate the value. Example: *“Based on a student’s major, recommend a relevant career path and set their ‘Career Interest’ custom field accordingly.”*
5. **Test the Output** – Select a contact and click **Evaluate** to preview the AI-generated value before finalizing.

---