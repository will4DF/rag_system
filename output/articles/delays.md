---
title: Delays
url: https://help.element451.com/en/articles/10618338-delays
collection: Workflows + Rules
---

Learn about using delays between Workflow steps.

# Overview

Delays allow you to customize the timing of step actions. They're particularly useful for actions involving sending communications and notifications. An action like auto-submitting a student's application would also benefit from a delay.

Delays can be based on the time since the last step occurred or relative to when a person in the workflow did something, such as starting an application.

---

# How to Add a Delay

The process of adding Actions is outlined in our help articles on creating Workflows + Rules:

* **Workflows**

  + [Adding an Action a New Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow#h_73b1e4802c)
  + [Adding an Action to an Existing Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow#h_3d3964e6d7)
* **Rules**

  + [Adding an Action to a New Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule#h_d6f11c33df)
  + [Adding an Action to an Existing Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule#h_90d410f7be)

When you add a new step to a workflow, the delay defaults to 0, meaning the step will happen immediately unless you specify a delay. To add a delay:

---

# Delay Types

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390958906/257bb9651f29cd703fcc82dff07f/Important.png?expires=1784430000&signature=4ce9bfb040802d6984236645326e0d7b501cedf538c6625f3aa5366b9c44e87f&req=dSMuFsB7lYhfX%2FMW3Hu4gfsV60%2FyofZilVRMda9Q0qIv0JBedOCxAAUiX9re%0Axg%3D%3D%0A) When configuring a delay, the **active tab at the time of saving** determines which delay type is used. If you have configurations on both the Standard and Relative tabs, only the delay type selected on the active tab will apply when you save. You can only use one delay type per step.

When configuring a delay, the **active tab at the time of saving** determines which delay type is used. If you have configurations on both the Standard and Relative tabs, only the delay type selected on the active tab will apply when you save. You can only use one delay type per step.

## Standard Delay

A standard delay is based on when the last step was completed.

* If the delay is on the first step of a workflow, the time is based on when people entered the workflow.
* The delay is simply entering the number of seconds, minutes, hours, and days. The seconds and minutes are for precision. It's OK to indicate only days or hours.  
  ​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390957757/1c14df0a028567c954d9742867ba/Screenshot%2B2024-01-25%2Bat%2B2_35_22-E2-80-AFPM.png?expires=1784333700&signature=0f9ae20a9c741f27ebfaf7bcc7136e86eab277a6e55fc75aa900b1230717d19f&req=dSMuFsB7moZaXvMW1HO4zSrL%2F50TXfOfEbjxA7wUj8Bna1vj%2BTpvKKU7pemQ%0AjvSdZDcN9BGihOBvV%2Fo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390957757/1c14df0a028567c954d9742867ba/Screenshot%2B2024-01-25%2Bat%2B2_35_22-E2-80-AFPM.png?expires=1784333700&signature=0f9ae20a9c741f27ebfaf7bcc7136e86eab277a6e55fc75aa900b1230717d19f&req=dSMuFsB7moZaXvMW1HO4zSrL%2F50TXfOfEbjxA7wUj8Bna1vj%2BTpvKKU7pemQ%0AjvSdZDcN9BGihOBvV%2Fo%3D%0A)

## Relative Delay

Relative delays are based on when a person in the workflow did something or a specific date.

The first fields are the same as in the standard delay, but you now have the option to select:

* **Before** or **After**: Should the step occur before or after the time you enter
* **Parameter**: When a person in the workflow does something or when something happens in relation to their account. For example, when they start an application or last logged into it.

Once you select a parameter, you'll need to configure the constraints. Constraints are the specifics of a parameter. For example, the name of the application a person starts or the calendar date of their birthday.

Click the heading below to view the list of parameters available:

## **Parameters**

* **Application Completed Date**: The date a Contact completed their application by filling in all required fields and submitting necessary documents.
* **Application Registration Date**: The date a Contact started their application.
* **Application Submission Date**: The date a Contact submitted their application.
* **Event Date**: The date tied to the contact’s event registration, not the general event listing.

  + If a contact is not registered for the event, the delay cannot be calculated, and the step will never run for them.
  + If a contact registers **after** the calculated delay date, the step will run immediately.
  + To have all contacts enter the step on the same date regardless of registration, use the specific date delay instead.
* **Last Email Click Date**: The most recent date a Contact clicked on a link in an email.
* **Last Email Delivery Date**: The most recent date an email was successfully delivered to a Contact.
* **Last Email Open Date**: The most recent date a Contact opened an email.
* **Last Event Attendance Date**: The most recent date a Contact attended an event.
* **Last Event Registration Date**: The most recent date a Contact registered for an event.
* **Last Page View Date**: The most recent date a Contact viewed a page.
* **Last SMS Click Date**: The most recent date a Contact clicked on a link in an SMS message.
* **Last SMS Delivery Date**: The most recent date an SMS message was successfully delivered to a Contact.
* **Last User Login Date**: The most recent date a user logged into an application, microsite, etc., on Element451.
* **Specific Delay Date**: A chosen date for delaying a workflow step. This step will be on hold until the specified date and any set delay conditions are met. The step will execute at midnight UTC if only a date is set. Workflow instances reaching this step after meeting the date and delay conditions will execute immediately.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390957758/78f0d61024625a26f674ca635a71/Screenshot%2B2024-01-25%2Bat%2B2_35_31-E2-80-AFPM.png?expires=1784333700&signature=3320b344387ea3095b14e21714d7c6b2e78ccaf2cf88f782ff3c3790e075b60a&req=dSMuFsB7moZaUfMW1HO4zWv%2FQdAUIzs%2BhHO9C9cxGjoalZex7nb3dUuLURkH%0AQbaUZnXurJNV82yPluM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1390957758/78f0d61024625a26f674ca635a71/Screenshot%2B2024-01-25%2Bat%2B2_35_31-E2-80-AFPM.png?expires=1784333700&signature=3320b344387ea3095b14e21714d7c6b2e78ccaf2cf88f782ff3c3790e075b60a&req=dSMuFsB7moZaUfMW1HO4zWv%2FQdAUIzs%2BhHO9C9cxGjoalZex7nb3dUuLURkH%0AQbaUZnXurJNV82yPluM%3D%0A)

---