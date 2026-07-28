---
title: Triggers
url: https://help.element451.com/en/articles/1500290-triggers
collection: Workflows + Rules
---

Learn about the types of Triggers and how to use them to enroll Contacts in your Workflows and Rules.

# Overview

## Workflows

Triggers are used to determine who should be enrolled in a workflow. When a contact meets the criteria for the trigger you set, they are automatically enrolled in the workflow. The system then checks each workflow step against the person to determine what should happen to them based on the step's conditions.   
​  
Workflows also allow you to search by name or load a segment. This option is ideal when your focus is on a **specific** group of contacts, where automatic enrollment in the workflow is not required. When loading a segment, it's important to note that this captures a **snapshot** of the segment **at that specific time**. All contacts in the segment at the moment of enrollment will be added to the workflow and remain there, regardless of any subsequent changes to their profiles or segment filters. Adding your audience in this way acts as your trigger for the workflow.

## Rules

When creating a rule with the type **triggered**, you have the same trigger options as when creating a Workflow. **Triggers are not available for Scheduled rules**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1212797732/8428a0ce9a1fe37f44cabf010ed1/Note.png?expires=1784333700&signature=b8b71f06f14d6ccf0559a832ff88da6d3957e4de89ef0301dd09860f415ea51c&req=dSImFM53moZcW%2FMW1HO4zVh4TAQfVrE4iQPIyx%2FIqxR2NPH6cLT981DKZdmm%0Aj4DgEUbUOgwHP8ouKNo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1212797732/8428a0ce9a1fe37f44cabf010ed1/Note.png?expires=1784333700&signature=b8b71f06f14d6ccf0559a832ff88da6d3957e4de89ef0301dd09860f415ea51c&req=dSImFM53moZcW%2FMW1HO4zVh4TAQfVrE4iQPIyx%2FIqxR2NPH6cLT981DKZdmm%0Aj4DgEUbUOgwHP8ouKNo%3D%0A)

You can have multiple triggers, and they operate **independently**. This means that a person only needs to meet the criteria of **one** trigger to be enrolled in the workflow.

---

# How to Add a Trigger

Triggers should be added as the **last** **step** in creating a Workflow or Rule. To learn how to add a trigger, use these resources:

* Workflows: [How to Create a Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow#h_a17eac09da)
* Rules: [How to Create a Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule#h_7c278297f4)

---

# Types of Triggers

## Applications

* **Application Completed**: Enroll people when they complete a selected application.
* **Application Started:** Enrolls people when they begin a selected application.
* **Application Submitted:** Enroll people when they submit a selected application.
* **Payment** **Submitted**: Enroll people when they pay the fee for a selected application.
* **Recommendation** **Submitted**: Enroll people when a recommendation is submitted for a selected application.

Once selected, application triggers have the following options:

* **Application:** Choose which application the trigger relates to.
* **Term (optional):** Choose the term applicants have chosen that should enroll them.
* **Major (optional):** Choose the major applicants have chosen that should enroll them.

## Appointments

* **Appointment Attended**- Enroll people who have attended an appointment
* **Appointment Canceled**- Enroll people who have canceled an appointment
* **Appointment No-Show**- Enroll people who have been marked as no-show to an appointment
* **Appointment Scheduled**- Enroll people who scheduled an appointment
* **Appointment Updated**- Enroll people who updated an appointment

## Case Management

These triggers are available when the Case Management module is enabled. They let you enroll contacts into a Workflow based on Alert and Case activity.

* **Alert Created**: Enroll people when a new alert is created for them. You can scope enrollment by alert type or priority.
* **Case Created**: Enroll people when a new case is created for them.
* **Alert Status Updated**: Enroll people when the status of one of their alerts changes. This trigger fires only on a status change, not on other edits to the alert, and can be scoped by alert priority and status.
* **Case Status Updated**: Enroll people when the status of one of their cases changes. This trigger fires only on a status change, not on broad case edits, and can be scoped by case type, priority, and status.

## Conversations

* **Conversation Started**- Enroll people who start a conversation

  + If selected, you can then select the channel:

    - Any
    - Email
    - Messenger
    - SMS
    - Phone

## Decisions

* **Decision Checklist Items**: Enroll people when their checklist item status (completed, waived, incomplete) is changed
* **Decision Released**: Enroll people when their application decision is released
* **Decision Stage Changed**: Enroll people when their application decision stage changes.
* **Decision Status Changed:** Enroll people when their application decision status changes.

## Documents

* **Document Uploaded**: Enroll people when a related document is uploaded or imported (contact must be associated with the document upload)

## Events

* **Event Signup**: Enroll the user when they sign up for a specified event.

[![](https://downloads.intercomcdn.com/i/o/1018522227/2f90215adefda54967adced7/Note-Orng.png?expires=1784333700&signature=d526c6e887f3357dc59186a44d907d42fbf3229685b72fa8c6d254eb136fa827&req=dSAmHsx8n4NdXvMW1HO4zV%2FkLJvlG06HHGggsqARj6cDQyFAlMvrkMxGZhm8%0Adh3pZmdYnG1OJHDTN9M%3D%0A)](https://downloads.intercomcdn.com/i/o/1018522227/2f90215adefda54967adced7/Note-Orng.png?expires=1784333700&signature=d526c6e887f3357dc59186a44d907d42fbf3229685b72fa8c6d254eb136fa827&req=dSAmHsx8n4NdXvMW1HO4zV%2FkLJvlG06HHGggsqARj6cDQyFAlMvrkMxGZhm8%0Adh3pZmdYnG1OJHDTN9M%3D%0A)

Each event you create in Events has automated messaging built-in. So, you don't need to create workflows to send messages to attendees. For more information on event messaging, [click here.](https://help.element451.com/en/articles/1524108-message-attendees)

## Forms

* **Form Submitted**: Enroll a person when they submit a form. For example, a request for information form.

## Labels

* **User Label Added**: Enroll people when they are tagged with a chosen label.
* **User Label Removed**: Enroll the user when a label is removed.

[![](https://downloads.intercomcdn.com/i/o/1018522614/03b40d9c81161acb283658cb/Pro+Tip+-+Orng.png?expires=1784333700&signature=31fcb6376c48c64dc5e7f451c8f3997304598994759aebf96f722b8847854c2f&req=dSAmHsx8n4deXfMW1HO4zVGLLLEOM3l30fV3PzS%2FcjO3G3XPMInRAbF%2FGX8b%0ATS3WYsujfPqUxDGLkE0%3D%0A)](https://downloads.intercomcdn.com/i/o/1018522614/03b40d9c81161acb283658cb/Pro+Tip+-+Orng.png?expires=1784333700&signature=31fcb6376c48c64dc5e7f451c8f3997304598994759aebf96f722b8847854c2f&req=dSAmHsx8n4deXfMW1HO4zVGLLLEOM3l30fV3PzS%2FcjO3G3XPMInRAbF%2FGX8b%0ATS3WYsujfPqUxDGLkE0%3D%0A)

You can use workflows to automate applying labels to people, which would, in turn, trigger this trigger. For example, you can create a workflow that tags people with "prospect" when they click a link in a student search email.

## Users

* **Record Created**: Enroll people when a new contact record is created, regardless of how it was created — form submission, import, API call, or manual entry. Useful for automations that should apply universally to every new contact entering the system without setting up separate triggers per entry point.
* **Joined Segment**: Enroll people when they join a calculated segment.
* **Joined or Left Segment**: Enroll people when they join or exit a calculated segment.
* **Left Segment**: Enroll people when they exit a calculated segment.
* **User Birthday**: Enroll people at 5:01 UTC (12:01 AM) on their birthday
* **User** **Territory** **Change**: Enroll people when their territory changes

---

# Re-Enrollment and the Repeatable Toggle

By default, a person can only be enrolled in a workflow once. Each trigger has a **Repeatable** toggle that controls whether that trigger can enroll the same person more than once.

* **Non-repeating triggers** never create a second enrollment for the same person, even when the person's earlier enrollment came from a different, repeatable trigger.
* **Repeatable triggers** can enroll the same person again, as long as no earlier enrollment came from the **same** trigger with the same **context**. For application and decision triggers, the context is the specific application (registration); for other triggers, it is the source entity, such as an event registration, form, alert, or case.

Because triggers are evaluated independently, the order of events matters when a workflow uses both repeating and non-repeating triggers:

* If a person is enrolled by a **non-repeating** trigger first and later meets a **repeatable** trigger, they are enrolled again.
* If a person is enrolled by a **repeatable** trigger first and later meets a **non-repeating** trigger, they are **not** enrolled again, because the non-repeating trigger cannot create a duplicate enrollment.

For example, in a workflow with a non-repeating *Joined Segment* trigger and a repeatable *Application Submitted* trigger, submitting two different applications creates two enrollments (one per application), while entering the segment after the person is already enrolled does not add another.

---

# Considerations When Using "Joined" or "Left" Triggers

* "Joined” triggers activate when a user’s profile is updated, but they won’t activate based on the passage of time or changes to someone else’s profile. Here are two cases where joined triggers won’t work:

  + If the segment includes a relative date filter.
  + If the segment includes a relationship filter (e.g., the family profile is not evaluated when there is a change to the related student’s profile).
* Calculated segments are not designed to update instantly. If you’re looking for an immediate response based on user actions, consider using workflow triggers like “Application Start” or “Form Submitted.” These instant triggers are helpful when a user takes an action that requires a prompt response. However, immediate responses may not be necessary for activities like labeling users based on their behavior for reporting purposes.
* If you change the filters on a **Calculated Segment** that’s being used as a workflow trigger, keep in mind:

  + **The segment will be re-evaluated.** Anyone who now meets the updated conditions will be added to the segment and enrolled into the workflow.
  + **Contacts already in the workflow will not be removed.** Even if they no longer meet the updated conditions, they will continue moving through the workflow.

---