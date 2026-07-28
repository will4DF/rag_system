---
title: Getting Started with Journeys
url: https://help.element451.com/en/articles/6825003-getting-started-with-journeys
collection: Journeys
---

Learn the fundamentals of Journeys, a way to track and visualize students completing sequential interactions.

# Overview

Our students interact with us in countless ways, and our business processes often span multiple modules within Element451. Journeys are designed to track and visualize people completing sequential interactions, allowing you to monitor and manage custom enrollment funnels, track inquiries, follow admitted students as they progress toward enrollment, and much more. The possibilities with Journeys are endless.

## Benefits of Using a Journey

* Track more than just funnel stages
* Visibility of what processes are working and where students are getting stuck
* Quick insight on conversion rates

## Example Use Cases

* Honors college invite
* Financial aid and scholarships
* Enrollment tracker
* Program completion tracker
* Matriculation requirements
* Student search

## Accessing Journeys

Navigate to **Data + Automations** > **Journeys** > **All Journeys**.

[![](https://downloads.intercomcdn.com/i/o/645442756/dff3d10d85bace11971461ad/J+Menu.gif?expires=1784333700&signature=687b5e8ced18ca92f7609e00658b4e53527cdb2a2526a87902c0f3c7f577ba6c&req=ciQiEs18moRZFb4f3HP0gOLrKZ64dczZT9ALRKviqQEU9WPxASTg%2BWQZNSY4%0AmX%2BC6%2F7UVPSduYJOKA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/645442756/dff3d10d85bace11971461ad/J+Menu.gif?expires=1784333700&signature=687b5e8ced18ca92f7609e00658b4e53527cdb2a2526a87902c0f3c7f577ba6c&req=ciQiEs18moRZFb4f3HP0gOLrKZ64dczZT9ALRKviqQEU9WPxASTg%2BWQZNSY4%0AmX%2BC6%2F7UVPSduYJOKA%3D%3D%0A)

## Components of a Journey

The three components of a Journey are Initial **Journey** **Triggers**, **Steps**, and **Exit** **Triggers**. We'll explain each below.

---

# Journey Triggers

Journey Trigger(s) are activities that automatically **enroll** a person in a Journey.

* You can configure one or multiple triggers.
* If multiple triggers, the Journey will begin if any one of the conditions is met.
* Triggers are configured using various activities that happen in Element451. Click below to view a complete list of trigger options.

## List of Journey Triggers

* Applications

  + Application Completed
  + Application Paid
  + Application Started
  + Application Submitted
* Appointments

  + Appointment Attended
  + Appointment Canceled
  + Appointment No Show
  + Appointment Scheduled
  + Appointment Updated
* Conversations

  + Conversation Started
* Decisions

  + Decision Checklist Completed
  + Decision Checklist Item Updated
  + Decision Released
  + Decision Stage Changed
  + Decision Status Changed
* Documents

  + Document Uploaded
* Event

  + Event Signup
* Forms

  + Form Submitted
* Labels

  + User Label Added
  + User Label Removed
* Users

  + Joined Segment
  + Left Segment
  + User Territory Changed

[![](https://downloads.intercomcdn.com/i/o/1086040451/e67e45f30bdb11db2a447ac6/Pro+Tip+-+Orng.png?expires=1784333700&signature=e7383222f9add750b63c7da04c9db7dfceae62f9974d953d0f30f7ca8f36bbbf&req=dSAvEMl6nYVaWPMW1HO4zTExpE6g%2BMe5IagHD1X4vnLDBj6nrkmMzOZqa4hG%0AxCMLIFDjFaXywT%2FOSKQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1086040451/e67e45f30bdb11db2a447ac6/Pro+Tip+-+Orng.png?expires=1784333700&signature=e7383222f9add750b63c7da04c9db7dfceae62f9974d953d0f30f7ca8f36bbbf&req=dSAvEMl6nYVaWPMW1HO4zTExpE6g%2BMe5IagHD1X4vnLDBj6nrkmMzOZqa4hG%0AxCMLIFDjFaXywT%2FOSKQ%3D%0A)

You can also **manually** enroll contacts individually or via a segment. [Click here to learn more about this process](https://help.element451.com/en/articles/9493679-journeys-managing-enrollees).

---

# Steps

Once a contact is enrolled in a Journey, the steps are the individual activities that must be completed for that contact to progress through the Journey.

Each step can have optional conditions and actions, both of which are **optional**.

## Conditions

Steps can use three different types of conditions to determine step completion:

* **Step Conditions** - These define specific activities that must be completed to mark the step as complete. For example, "submitted this form" or "completed this task." Use step conditions when you want to track a specific action happening.
* **User Segment Conditions** - These define characteristics the user must have to complete the step. Be cautious when using these alone! A step with only user segment conditions will be marked complete when any tracked activity occurs while the user matches these characteristics. This may lead to premature step completion, especially for users going through a Journey multiple times.
* **Segment Reference** - This allows you to reference an existing segment. The same considerations for User Segment Conditions apply here.

## Actions

Step actions can be configured to execute at the completion of a step, such as sending an email or adding a task. While this functionality exists, it was designed as an ancillary feature for the primary purpose of tracking Journeys.

**Important Note:** If your primary goal is to perform a series of automated actions rather than track user progression, consider using Workflows instead, as they were specifically designed for action automation. Journeys excel at visualizing user progress through a specific pathway but have limited action capabilities compared to Workflows.

## Step Progression

Generally, Journey steps must be completed in order (for an exception, see [Step Groups](#h_4a4ede859b) below). A Journey only monitors the **next step** for each user.

For example, consider a Journey that includes the following steps: `Received Open House Email > Clicked on the Link in Email > Registered for Open House`. If the user receives the email and registers for the event directly on the website without clicking the link in the email, the Journey will not move forward because the middle step was not completed.

Therefore, it’s important to identify the most critical metrics for your tracking and consider using Step Groups to ensure flexibility in the process.

## List of Steps

* Account

  + Created Account
  + Logged In
  + Has Been Merged
* Application

  + Completed Application
  + Paid Application
  + Paid Deposit
  + Started Application
  + Submitted Application
  + Supplemental Form Submitted
* Appointment

  + Scheduled Appointment
  + Canceled Appointment
  + Attended Appointment
  + Did Not Attend Appointment
  + Updated Appointment
* Course

  + Completed Course
  + Dropped Course
  + Enrolled Course
  + Updated Course
* Custom

  + Custom Activity
* Decision

  + Decision Checklist Completed
  + Updated Decision Assignment
  + Updated Decision Checklist Item
  + Updated Decision Criteria
  + Updated Decision Stage
  + Updated Decision Status
  + Released Decision
* Email

  + Bounced Email
  + Clicked Link in Email
  + Opened Email
  + Received Email
  + Unsubscribed From Email
* Event

  + Canceled Event Registration
  + Event Marked Attended
  + Registered For Event
* Form

  + Paid Form
  + Submitted Form
* Info Request

  + Received Recommendation
  + Requested Recommendation
* Journey

  + Completed Journey
  + Enrolled In Journey
* Page

  + Clicked Link on Page
  + Viewed Page
* Phone Call

  + Completed Phone Call
  + Did Not Answer Phone Call
  + Failed Phone Call
  + Busy Phone Call
  + Canceled Phone Call
* SMS

  + Clicked Link in SMS
  + Failed SMS
  + Received SMS
  + Undelivered SMS
* Survey

  + Completed Survey
* Task

  + Task Completed
* Whatsapp

  + Failed Whatsapp
  + Received Whatsapp
  + Undelivered Whatsapp

---

# Step Groups

Step Groups allow you to bundle multiple [steps](#h_d366fc9511) to be evaluated together. A Step Group can be configured in two ways:

* **All (Any Order)***:* All activities in this group must be completed, but they can be done in any order. Once all activities are completed, the group will be considered complete, and the Journey will look toward the next step.
* **Any***:* If any single step in this group is completed, the group will be considered complete, and the Journey will move on to the next step.

## Creating a Step Group

To create a group, select two or more steps and click **Create New Group*.***  
​

[![](https://downloads.intercomcdn.com/i/o/645591029/9c29c64b2038d5ecbcb7cf31/Screen+Shot+2023-01-03+at+7.04.39+PM.png?expires=1784333700&signature=e4d587c9066017ebe50eb153bd3d09624b1e2a0aa56e709a43e9f011fa23170a&req=ciQiE8B%2FnYNWFb4f3HP0gCETJvVRoVAN%2B98A08fayC51Kiv8CpGgxSdzKCDK%0AKM5Syt1h94dVJoN4lA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/645591029/9c29c64b2038d5ecbcb7cf31/Screen+Shot+2023-01-03+at+7.04.39+PM.png?expires=1784333700&signature=e4d587c9066017ebe50eb153bd3d09624b1e2a0aa56e709a43e9f011fa23170a&req=ciQiE8B%2FnYNWFb4f3HP0gCETJvVRoVAN%2B98A08fayC51Kiv8CpGgxSdzKCDK%0AKM5Syt1h94dVJoN4lA%3D%3D%0A)

---

# Exit Triggers

Exit Triggers are activity conditions that, when met, update a contact's status to "exited" within a Journey, preventing them from continuing further. Their primary purpose is to maintain accurate analytics by ensuring your Journey data reflects only those contacts who are still eligible to complete the Journey.

## When to Use Exit Triggers

Exit Triggers are most valuable when:

* You need to identify users who have taken actions that make them ineligible to complete the remaining Journey steps
* You want to maintain clean analytics that show true conversion rates among eligible users
* You're tracking a process where people might drop out for legitimate reasons

## How Exit Triggers Work

Exit Triggers are only evaluated against Journeys with "active" or "expired" status. They don't affect Journeys that are already "completed," "inactive," or previously "exited."

## Example Use Case

In a Journey that tracks an admitted student's progress from decision release → deposit → attendance at orientation:

If you set an exit trigger such as `updated decision status = withdrawn`, and a student withdraws their application after being admitted, their Journey status will update to "exited." This ensures your Journey metrics only include students who are still eligible to progress through the full path.

Without this exit trigger, withdrawn students would remain in your "active" count, artificially inflating your denominator and making your conversion rates appear lower than they actually are. Exit Triggers help you maintain accurate, actionable analytics that truly reflect the effectiveness of your student engagement strategy.

## List of Exit Triggers

* Account

  + Created Account
  + Logged In
  + Has Been Merged
* Application

  + Completed Application
  + Paid Application
  + Paid Deposit
  + Started Application
  + Submitted Application
  + Supplemental Form Submitted
* Appointment

  + Scheduled Appointment
  + Canceled Appointment
  + Attended Appointment
  + Did Not Attend Appointment
  + Updated Appointment
* Course

  + Completed Course
  + Dropped Course
  + Enrolled Course
  + Updated Course
* Custom

  + Custom Activity
* Decision

  + Decision Checklist Completed
  + Updated Decision Assignment
  + Updated Decision Checklist Item
  + Updated Decision Criteria
  + Updated Decision Stage
  + Updated Decision Status
  + Released Decision
* Email

  + Bounced Email
  + Clicked Link in Email
  + Opened Email
  + Received Email
  + Unsubscribed From Email
* Event

  + Canceled Event Registration
  + Event Marked Attended
  + Registered For Event
* Form

  + Paid Form
  + Submitted Form
* Info Request

  + Received Recommendation
  + Requested Recommendation
* Journey

  + Completed Journey
  + Enrolled In Journey
* Page

  + Clicked Link on Page
  + Viewed Page
* Phone Call

  + Completed Phone Call
  + Did Not Answer Phone Call
  + Failed Phone Call
  + Busy Phone Call
  + Canceled Phone Call
* SMS

  + Clicked Link in SMS
  + Failed SMS
  + Received SMS
  + Undelivered SMS
* Survey

  + Completed Survey
* Task

  + Task Completed
* Whatsapp

  + Failed Whatsapp
  + Received Whatsapp
  + Undelivered Whatsapp

---

# Creating or Editing a Journey

Now that you've reviewed the basics of a Journey, you can create or edit one. Click below to explore our article on creating and managing Journeys.

[Creating + Managing Journeys →](https://help.element451.com/en/articles/9492988-creating-managing-journeys)

---

# Managing Journey Enrollees

On a Journey’s page, you can review which contacts have been enrolled in the Journey via the established triggers and view details about their progress. Additionally, you can manually add individual contacts or segments of contacts to the Journey.

[Managing Journey Enrollees →](https://help.element451.com/en/articles/9493679-journeys-managing-enrollees)

---

# Journey Analytics

Utilize Journey Analytics to gain valuable insights into the performance and progress of your Journeys.

[Journey Analytics →](https://help.element451.com/en/articles/9493632-journeys-analytics)

---

# Frequently Asked Questions

Find quick answers to common questions about Journeys in our dedicated [FAQ article](https://help.element451.com/en/articles/10606462-journeys-frequently-asked-questions).

​

---