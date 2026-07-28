---
title: Integrate Your Tools with Zapier
url: https://help.element451.com/en/articles/6350700-integrate-your-tools-with-zapier
collection: Integrations
---

Learn how to connect web applications to Element451 using Zapier

# Overview

Zapier is a no-code automation tool that lets you streamline workflows between different web applications. By integrating Zapier with Element451, you can easily send student data to and from Element451, eliminating the need for manual import or export tasks. Check out the full list of apps compatible with Zapier [here](https://zapier.com/explore).

Before creating Zaps, you should be comfortable with:

* [Importing into Element451](https://help.element451.com/en/collections/8566724-imports-fundamentals)
* [Exporting from Element451](https://help.element451.com/en/collections/8566725-exports-fundamentals)
* [Calculated Fields](https://help.element451.com/en/articles/9007704-calculated-fields)
* [Creating an Import/Export Template](https://help.element451.com/en/collections/8566729-mapping-templates)
* [Date Fields and Formatting](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports)

For a walkthrough guide on how to connect Element451 to Zapier, view our [video guide](#h_227dc0e4ae) at the end of this article.

---

# Triggers + Actions

**Triggers:** Think of a trigger as the starting point for your automation. It’s like a cue that tells Zapier, “Hey, something just happened!” For example, if you want Zapier to do something every time a new contact is added in Element451, the new contact being added is the trigger.

## List of Trigger Options

* **Application Completed**

  + Trigger when user completes an application.
* **Application Payment Submitted**

  + Trigger when user submits payment an application.
* **Application Recommendation Letter Received**

  + Trigger when user submits an application.
* **Application Submitted**

  + Trigger when user submits an application.
* **Appointment Attended**

  + Trigger when appointment is attended
* **Appointment Canceled**

  + Trigger when appointment is canceled.
* **Appointment No Show**

  + Trigger when appointment is marked as no show.
* **Appointment Scheduled**

  + Trigger when appointment is scheduled.
* **Appointment Updated**

  + Trigger when appointment is updated.
* **Bulk User Entered Segment**

  + Trigger when Bulk Users Entered Segment.
* **Bulk User Exited Segment**

  + Trigger when Bulk Users Exited Segment.
* **Decision Check List Item Changed**

  + Trigger when decision Check List Item was changed.
* **Decision Released**

  + Trigger when decision is released.
* **Decision Stage Changed**

  + Trigger when decision stage was changed.
* **Decision Status Changed**

  + Trigger when decision status was changed.
* **Document Uploaded**

  + Trigger when document is uploaded.
* **User Birthday**

  + Trigger when it's users's birthday.
* **User Entered or Exited Segment**

  + Trigger when User Entered or Exited Segment.
* **User Entered Segment**

  + Trigger when User Entered Segment.
* **User Event Registration Successful**

  + Trigger when User Event Registration Succe
* **User Exited Segment**

  + Trigger when User Exited Segment.
* **User Label Added**

  + Trigger when user label is added.
* **User Label Removed**

  + Trigger when user label was changed.
* **User Territory Changed**

  + Trigger when User Territory Changed.

**Actions:** Actions are what Zapier does in response to the trigger. It’s the task Zapier performs automatically after the trigger. Continuing the example, if your trigger is a new contact in Element451, the action could be to add that contact to a Google Sheet. The action is what makes the automation useful.

## List of Action Options

* **Add Activity to User**

  + Add a new activity to an existing user.
* **Add Label to User**

  + Add a label to a user.
* **Add Note to User**

  + Add a new note to an existing user.
* **Add Task to User**

  + Add a new task and associate with an existing external user.
* **Change User Owner**

  + Change user admin owner
* **Create Conversation**

  + Send a message from a user into the Conversations inbox. A new conversation will be created. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Create Form Submission**

  + Create a new submission for a selected form. A new user is created or an existing user is updated based on their email address.
* **Create Webhook Execution**

  + Create Webhook Execution. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Create/Register Attendee to Event**

  + Create a new Event Attendee for a selected event.
* **Create/Update User**

  + Create or update an Element451 user based on an import template.
* **Enroll User to Workflow**

  + Enroll a user to a workflow.
* **Remove Label From User**

  + Remove a label from a user.
* **Send Communication to User**

  + Send a communication to a user.
* **Set Milestone Application Deposit**

  + Set Milestone Application Deposit. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Application Start**

  + Set Milestone Application Start. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Application Submit**

  + Set Milestone Application Submit. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Checklist Complete**

  + Set Milestone Checklist Complete. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Date of Inquiry**

  + Set Milestone Date Of Inquiry. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Defer**

  + Set Milestone Defer. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Enrolled**

  + Set Milestone Enrolled. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Interview**

  + Set Milestone Interview. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone on Hold**

  + Set Milestone On Hold. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Unsubscribe Email**

  + Set Milestone Unsubscribe Email. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Unsubscribe SMS**

  + Set Milestone Unsubscribe SMS. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Visit**

  + Set Milestone Visit. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Waitlist**

  + Set Milestone Waitlist. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set Milestone Withdrawn**

  + Set Milestone Withdrawn. Note the user must exist in Element451 and have a profile email address that matches the incoming email address.
* **Set User Territory**

  + Set a user's territory.

---

# Accessing your API URL + Feature Token

When setting up a Zap with Element451, you’ll need to connect your account. Zapier will prompt you for an ***API URL*** and ***Feature Token***.

You can find these details in your Element451 instance by clicking on your profile picture in the top right corner of the orange navigation menu and then going to **Settings** > **Integrations** > **Zapier**.

![](https://downloads.intercomcdn.com/i/o/1194875093/a2f37f39ba57036a8f8b597f/Note.png?expires=1784430000&signature=2f8a34044c5b99f4d4f8c6d2d1bfb85b20dd2c9ea77e84ec0f46dfff9825e736&req=dSEuEsF5mIFWWvMW3Hu4gZHVW3kwtriBV2OtFDPajliSkH3JjvR1vTwOY%2FB7%0AIA%3D%3D%0A)If you find that your Feature Token field is blank, please reach out to your Implementation Strategist or contact Live Support. We’ll assist in generating it for you.

[![](https://downloads.intercomcdn.com/i/o/1147207536/56edc2ca564d54907265261b/Zapier.png?expires=1784333700&signature=52aa85277bd1ab5949431021cdaf8f40d5ab4df5d5767d10df0f6af64165a00f&req=dSEjEct%2BmoRcX%2FMW1HO4zf8lvmnuDqPcxNBMj1ZRDgNg%2Fj1HblHuL3RV4fG6%0A8ZoVwSWECpVlnKG6Amg%3D%0A)](https://downloads.intercomcdn.com/i/o/1147207536/56edc2ca564d54907265261b/Zapier.png?expires=1784333700&signature=52aa85277bd1ab5949431021cdaf8f40d5ab4df5d5767d10df0f6af64165a00f&req=dSEjEct%2BmoRcX%2FMW1HO4zf8lvmnuDqPcxNBMj1ZRDgNg%2Fj1HblHuL3RV4fG6%0A8ZoVwSWECpVlnKG6Amg%3D%0A)

![](https://downloads.intercomcdn.com/i/o/1147213237/99654be60e39998f65348ae1/Pro+Tip.png?expires=1784430000&signature=f37fdb4858ea3482aab7138670f2c36734192a704b677a6ae6e2f227a1480220&req=dSEjEct%2FnoNcXvMW3Hu4gVeqmS0asRMVujzD3mQRCsUjAWy%2FOZbjHpdgzK%2Ba%0AeQ%3D%3D%0A) Once you create Zaps that are connected to Element451, they will be listed on the same page under the ***Your Workflows*** heading.

---

# Example: Connecting Calendly to Element451

Integrating Calendly with Element451 is a popular workflow among our partners. Follow these steps to set up a simple “Zap” that sends student data to Element451 when a student signs up for an event in Calendly.

## Step One: Create a Template in Element451

1. Navigate to **Data + Automations** > **Import/Export** > **Templates** in your Element451 instance.
2. Create a [new import template](https://help.element451.com/en/articles/9002061-creating-import-mapping-templates) to prepare for the data coming from Calendly.

## Step Two: Create Your Zap in Zapier

1. **Log In to Zapier**:

   * Sign in to your [Zapier](https://zapier.com/developer/public-invite/1614/a425da4484fe5a6c2b59477ded05450c/) account and click on “Create Zap.”
2. **Set Up the Trigger**:

   * Search for “Calendly” and select it as your trigger app.
   * Choose the trigger event, such as “Invitee Created.”
   * Connect your Calendly account to Zapier by logging in and authorizing access.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/539144820/9778076f6d59bfe3f489e184/Screen+Shot+2022-06-30+at+6.10.04+PM.png?expires=1784333700&signature=26a4aa9228e258d806060b4edfa419e5176c2dc5443d9140fe232f41ecb2780e&req=cSMuF816lYNfFb4f3HP0gAsOJhbmGS64VA867EJc%2BZuTpJD9SSSaHFhiyBxT%0AKFc%3D%0A)](https://downloads.intercomcdn.com/i/o/539144820/9778076f6d59bfe3f489e184/Screen+Shot+2022-06-30+at+6.10.04+PM.png?expires=1784333700&signature=26a4aa9228e258d806060b4edfa419e5176c2dc5443d9140fe232f41ecb2780e&req=cSMuF816lYNfFb4f3HP0gAsOJhbmGS64VA867EJc%2BZuTpJD9SSSaHFhiyBxT%0AKFc%3D%0A)
3. **Test the Trigger** (optional):

   * Test the trigger to ensure Zapier can retrieve data from Calendly.
4. **Set Up the Action**:

   * Search for “Element451” and select it as your action app.
   * Choose an action event, such as “Create/Update User.”
   * Connect your Element451 account to Zapier. If this is your first time, you may need an API key from Element451. You can access this information in your Element451 instance by clicking on your profile picture/avatar in the top right corner of the navigation bar and then navigating to **Settings** > **Integrations** > **Zapier**.
5. **Map the Data Fields**:

   * Select the import template you created in Element451.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/539151103/b3fb187784666953649731ac/Screen+Shot+2022-06-30+at+6.35.45+PM.png?expires=1784333700&signature=86c44aef1da4918ebd717971ac3972eac9f487683897c2ae6459eeaa57d8d1ef&req=cSMuF8x%2FnIFcFb4f3HP0gENp5zDcNJVw%2B3y95PeQR4%2FhfJmFDPMMMEKNeSWd%0A4J4%3D%0A)](https://downloads.intercomcdn.com/i/o/539151103/b3fb187784666953649731ac/Screen+Shot+2022-06-30+at+6.35.45+PM.png?expires=1784333700&signature=86c44aef1da4918ebd717971ac3972eac9f487683897c2ae6459eeaa57d8d1ef&req=cSMuF8x%2FnIFcFb4f3HP0gENp5zDcNJVw%2B3y95PeQR4%2FhfJmFDPMMMEKNeSWd%0A4J4%3D%0A)
   * Map the fields from Calendly to the corresponding fields in Element451. This might include the student's name, email, and event details.
   * If you have calculated fields in your Element451 template, insert an empty string (””) in those fields to prevent errors.
6. **Test the Action**:

   * Test the action step to ensure data is correctly sent to Element451.
   * Check your Element451 instance to verify that the data has been imported correctly.

## Step Three: Make your Zap Live!

**Review and Activate**:

1. If everything looks good, turn on your Zap.
2. Monitor the initial data flow to ensure everything works as expected.

---

# Video Guide

---

# Important: Zapier Triggers and Deleted Items in Element451

When you create a Zap in Zapier using an Element451 trigger, Zapier stores the unique ID (identifier) of the item you selected, such as a label, segment, taxonomy, or template.

If you **delete** that item in Element451 (even if you recreate it with the same name), the new item will have a **different identifier**. Zapier won’t know about the deletion, so your Zap will no longer work as expected.

* Zapier does **not** automatically update when you delete or rename an item in Element451.
* If you delete an item that’s used in a Zap trigger, you must **edit your Zap** in Zapier and select the new item.
* This applies to all entities used in Zapier triggers: events, labels, segments, taxonomies, templates, etc.

✨ **Pro Tip:** Before deleting something in Element451, check whether it’s used in any Zaps. You can do this by reviewing your Zaps in Zapier and noting which Element451 items they reference.

---

# Additional Resources

For a full list of Element451 actions in Zapier and additional help videos, check out our [Integration Documentation](https://integrations.element451.com/zapier-121).

---