---
title: Traits
url: https://help.element451.com/en/articles/6960851-traits
collection: People
---

Learn what Person Traits are, how they are calculated and how you can use them.

# Overview

## What are Traits?

Traits are dynamic attributes **calculated from the data within a Person record**, designed to facilitate student segmentation and progress tracking. These attributes are essential for creating targeted Campaigns, Workflows, and internal Tasks.

## How do Traits work?

Traits are calculated and updated when data is added to the Person record reflecting the most current or relevant attribute values.

For example, the "Active Term" trait is calculated from a student's most recent milestone, application, or form submission. The [complete listing of Trait calculations](#h_b6be742207) can be found in the following section.

![](https://downloads.intercomcdn.com/i/o/978289139/3da2030b704386fda0d5138b/Important+Button.png?expires=1784430000&signature=20aa9e6bd716a452436492148ad75835c8c351b54b763b70e7779ae1bf552ed9&req=fScvFMF3nIJWFb4X1HO4gd5oEtyDWPBnb4gvAdZlXQvAEMI0%2FT%2BAIvG5lsIA%0A) Traits are recalculated when new data is added to the Person record. The Person is queued for recalculation instantly, but it can take several hours to complete and be updated on the student record.

## How can I leverage Traits?

Traits can significantly enhance student engagement strategies by allowing for precise tracking and segmentation.

For instance, you could send a targeted email Campaign highlighting the Nursing program's achievements to students who have an *Active Major* in Nursing and have opened and clicked on at least one email in the past. This ensures your message is relevant and reaches those most likely to be interested.

---

# List of Traits

## Active Campus

**Description**

The Campus that the person is currently associated with based on their Milestones and Applications.

**Calculation**

```
first_not_null(first_not_null(applications_campus), intended_campus)
```

## Active Degree

**Description**

The Degree that the person is currently associated with based on their Milestones and Applications.

**Calculation**

```
first_not_null(first_not_null(applications_degree), intended_degree)
```

## Active Funnel Stage

**Description**

The funnel stage that the person currently in based on their Milestones.

**Calculation**

```
first_not_null(milestones_type)
```

## Active Major

**Description**

The Major that the person is currently associated with based on their Milestones and Applications.

**Calculations**

```
first_not_null(first_not_null(milestones_major), first_not_null(applications_major), intended_major)
```

## Active Student Type

**Description**

The Student Type that the person is currently associated with based on their Milestones and Applications.

**Calculations**

```
first_not_null(first_not_null(milestones_student_type), first_not_null(applications_student_type), intended_student_type)
```

## Active Term

**Description**

The Term that the person is currently associated with based on their Milestones and Applications.

* The "active term" helps you keep track of which term a student is currently engaged with, even if they have interacted with your institution in the past. This ensures that students receive the right communications at the right time, regardless of their application history. Here are some examples of why it's important:

  + **Multiple Applications:** Students may apply to your institution multiple times for different terms. The "active term" field identifies the term associated with their most recent interaction.
  + **Application Status:** Even if a student withdraws an application or is denied, they may still submit an RFI form for a future term. The "active term" field ensures they are included in segments and communications for that new term.

**Calculations**

```
first_not_null(first_not_null(milestones_term), first_not_null(applications_term), intended_term)
```

## Date of Last Decision Released

**Description**

The date of the most recent decision released activity.

**Calculation**

```
last(decision_release_date)
```

## Date of Last Email Clicked

**Description**

The date of the most recent decision released activity.

**Calculation**

```
last(email_click_date)
```

## Date of Last Email Delivered

**Description**

The date of the most recent email delivered activity.

**Calculation**

```
last(email_delivered_date)
```

## Date of Last Email Opened

**Description**

The date of the most recent email open activity.

**Calculation**

```
last(email_opened_date)
```

## Date of Last Event Attended

**Description**

The date of the most recent event attended activity.

**Calculation**

```
last(event_attended_date)
```

## Date of Last Event Registration

**Description**

The date of the most recent event registration activity.

**Calculation**

```
last(event_registration_date)
```

## Date of Last External Activity

**Description**

The date of the most recent external or custom activity.

**Calculation**

```
last(activity_date)
```

## Date of Last Form Submitted

**Description**

The date of the most recent form submission activity.

**Calculation**

```
last(form_submitted_date)
```

## Date of Last Pageview

**Description**

The date of the most recent pageview activity.

**Calculation**

```
last(pageview_date)
```

## Date of Last Profile Address Updated

**Description**

The date of the most recent profile address update activity.

**Calculation**

```
last(profile_address_update_date)
```

## Date of Last Profile Email

**Description**

The date of the most recent profile email update activity.

**Calculation**

```
last(profile_email_update_date)
```

## Date of Last Profile Name Updated

**Description**

The date of the most recent profile name update activity.

**Calculation**

```
last(profile_address_update_date)
```

## Date of Last Profile Updated

**Description**

The date of the most recent profile update activity.

**Calculation**

```
last(profile_update_date)
```

## Date of Last SMS Clicked

**Description**

The date of the most recent SMS clicked activity.

**Calculation**

```
last(sms_click_date)
```

## Date of Last SMS Delivered

**Description**

The date of the most recent SMS delivered activity.

**Calculation**

```
last(sms_delivered_date)
```

## Date of Last Task Deleted

**Description**

The date of the most recent task deleted activity.

**Calculation**

```
last(task_deleted_date)
```

## Date of Last User Merged

**Description**

The date of the most recent user merged activity.

**Calculation**

```
last(user_merge_date)
```

## Email Suppression

**Description**

Boolean indicating if emails to the record are being suppressed. Email Suppression is used to prevent excessive spam errors and ensures a high "trust score" with email platforms.

**Calculation**

```
if(  
  total_pageviews = 0   
  AND total_logins = 0  
  AND total_email_clicked = 0  
  AND total_email_delivered > 10,  
    
  TRUE,  
  
  FALSE  
)
```

## Engagement Score

**Description**

Categorical representation of a students engagement with the institution.

Options are "Stranger", "Unengaged", "Dormant", "Lurker", "Follower", and "Fan".

**Calculation**

Engagement Score uses custom calculations not applicable to other traits.

The Engagement Score considers the students behavior across several traits:

```
date_of_last_email_click  
date_of_last_sms_clicked  
date_of_last_form_submitted  
date_of_last_pageview  
date_of_last_event_attended  
date_of_last_login  
date_of_last_conversation_message
```

First, a difference calculation finds the days between the date of a given trait and the current date.

```
days_since_last_login = date_diff('day', date_of_last_login, now())
```

Then, each trait is scored based on days since the last activity. Scoring can be represented by a JavaScript if() statement for example purposes.

```
if (days_since_last_pageview <= 7):  
  pageview_score = 1  
elif (days_since_last_pageview <= 14):  
  pageview_score = 0.75  
elif (days_since_last_pageview <= 30):  
  pageview_score = 0.5  
elif (days_since_last_pageview <= 60):  
  pageview_score = 0.25  
elif (days_since_last_pageview > 60):  
  pageview_score = 0.1
```

Each trait score is then added and divided by the total number of trait scores. The result is a numeric engagement score.

```
engagement_score = float(email_score + sms_score + form_score + login_score + pageview_score + event_score + conversation_score)/7
```

A "no engagement" score is also calculated and will later be used to determine if any engagement has happened at all.

```
no_engagement = total_email_delivered_events + total_sms_delivered_events
```

Finally, scores are categorized based on the engagement score and "no engagement" score. This can be represented by a JavaScript if() statement for example purposes.

```
if (engagement_score >= 0.33):  
  return 'FAN'  
elif (.33 > engagement_score >= 0.2):  
  return 'FOLLOWER'  
elif (0.2 >  engagement_score >= 0.05):  
  return 'LURKER'  
elif (0.05 >  engagement_score > 0):  
  return 'DORMANT'  
elif (engagement_score = 0 OR user-milestones-unsubscribe-date exists):  
  return 'UNENGAGED'  
elif (engagement_score = 0 OR no_engagement = 0):  
  return 'STRANGER'
```

## First Application

**Description**

The first application that the person started.

**Calculation**

```
first(application_name)
```

## First Pageview URL

**Description**

The URL of the first website page the person viewed.

**Calculation**

```
first(pageview_url)
```

## First Source

**Description**

The name of the person's first Source by date.

**Calculation**

```
first(source_name)
```

## First Source Description

**Description**

The description of the person's first Source by date.

**Calculation**

```
first(source_description)
```

## First Source Type

**Description**

The description of the person's first Source by date.

**Calculation**

```
first(source_type)
```

## Furthest Funnel Stage

**Description**

The most advanced Milestone that person has achieved.

**Calculation**

```
last(milestone)
```

## Last Form Submitted

**Description**

The name of the most recent form the person submitted.

**Calculation**

```
last(form_submitted_name)
```

## Last Pageview URL

### Description

The **Last Pageview URL** trait shows the most recent page a known user visited—*but only if we can identify them at the time of their visit.*

Here’s what you need to know to ensure this trait populates as expected:

#### When Pageviews Become Identified

We can match pageview activity to a user if they:

* Visit a tracked page **using a URL that includes** `_eid={element_id}`
* Click a tracked link **from an Element-powered communication** (like an email or SMS)
* Visit a tracked page **while logged into an Element-powered site** (like a portal or microsite)

In these cases, the user’s browser is tagged, and future pageviews (and sometimes past ones) can be stitched to their record.

#### Why You Might See “N/A” for Last Pageview URL

If a student visits a page using a **direct link** (like from your website or a third-party site), and they’re **not logged in** or using a link from an Element campaign, their activity is tracked—but remains **anonymous**.

That’s why the *Last Pageview URL* trait may not show a value yet. Even though the pixel is working, we don’t know who the visitor is—**yet**.

#### How Identity Stitching Helps

When a student eventually **clicks a tracked link with \_eid**, their browser is matched to their record. At that point, our system runs an identity stitching process to associate any **past anonymous pageviews** from the same browser with their contact record. When this happens, the *Last Pageview URL* trait updates automatically.

This process can take time and is only triggered by **identifiable** web activity.

#### **What You Can Do**

* **Send links using Element451 campaigns.** Links shared through email or SMS will include the \_eid and help identify the user.
* **Use Element-powered landing pages or microsites.** When users are logged in, tracking is automatic.
* **Check the form submission source.** Even if the Last Pageview URL trait is empty, you can still see the source URL of a submitted form under that activity’s details in the contact record.

**Pro Tip**: If you want to confirm your pixel is working, visit the tracked page using a URL that includes your contact’s \_eid. You’ll see a new, identified pageview appear in their activity timeline—and the *Last Pageview URL* trait should update shortly after.

### Calculation

```
last(pageview_url)
```

## Last Seen City

**Description**

The city of the most recent activity with geographic information.

Note: Geographic information about activities is derived from the person's device.

**Calculation**

```
last(activity_city)
```

## Last Seen Country

**Description**

The country of the most recent activity with geographic information.

**Calculation**

```
last(activity_country)
```

## Last Seen Region

**Description**

The state or region of the most recent activity with geographic information.

**Calculation**

```
last(activity_region)
```

## Last Seen Timezone

**Description**

The timezone of the most recent activity with geographic information.

**Calculation**

```
last(activity_timezone)
```

## Last Submitted App

**Description**

The name of the most recent application the person has submitted.

**Calculation**

```
last(application_submitted)
```

## Last Touchpoint

**Description**

The name of the most recent touchpoint activity for the person.

Note: "Touchpoints" are a subset of all activities. See more.

**Calculation**

```
last(touchpoint)
```

## Last User Activity

**Description**

The name of the most recent user-initiated activity for the person.

Note: "User" activities are a subset of all activities. See more.

**Calculation**

```
last(user_activity)
```

## Preferred Open Time

**Description**

Categorical representation of the most common time a student opens Email and SMS messages.

Options are "Morning", "Day", "Afternoon", "Evening", "Night", and "Late-Night".

**Calculation**

Preferred Open Time uses custom calculations not applicable to other traits.

First, the local hour of the activity is categorized. This can be represented as a SQL case statement for example purposes.

```
case  
  when activity_local_hour > 4AM and < 9AM then "Morning"    
  when activity_local_hour > 9AM and < 1PM then "Day"  
  when activity_local_hour > 1PM and < 5PM then "Afternoon"  
  when activity_local_hour > 5PM and < 9PM then "Evening"  
  when activity_local_hour > 9PM and < 12AM then "Night"  
  when activity_local_hour > 12AM and < 4AM then "Late-Night"  
end
```

Activities are then counted by category. The category with the most activities is considered the preferred open time.

## Total Applications

**Description**

Total number of application started activities for the person.

**Calculation**

```
total(application_started)
```

## Total Completed Tasks

**Description**

Total number of tasks completed for the person.

**Calculation**

```
total(task_completed)
```

## Total Email Opens

**Description**

Total number of email open activities for the person.

**Calculation**

```
total(email_opened)
```

## Total Events Attended

**Description**

Total number of event attended activities for the person.

**Calculation**

```
total(event_attended)
```

## Total Forms Submitted

**Description**

Total number of form submission activities for the person.

**Calculation**

```
total(form_submitted)
```

## Total Open Tasks

**Description**

Total number of tasks opened or in progress for the person.

Calculation

```
total(task_created) - total(task_completed)
```

## Total SMS Delivered

**Description**

Total number of SMS delivered activities for the person.

**Calculation**

```
total(sms_delivered)
```

## Total Sources

**Description**

Total number of sources for the person.

**Calculation**

```
total(sources)
```

## Total Tasks

**Description**

Total number of tasks for the person.

**Calculation**

```
total(tasks_created)
```

## Total Unique Emails Clicked

**Description**

Total number of email click activities per campaign.

**Calculation**

```
total( unique(email_clicked_campaign) )
```

## Total Unique Emails Opened

**Description**

Total number of email open activities per campaign.

**Calculation**

```
total( unique(email_opened_campaign) )
```

## Total Unique SMS Clicks

**Description**

Total number of SMS click activities per campaign.

**Calculation**

```
total( unique(sms_clicked_campaign) )
```

## Total User Login Events

**Description**

Total number of login activities for the person.

**Calculation**

```
total(user_login)
```

## Type of Last Custom Activity

**Description**

The type of the most recent custom activity for the person.

**Calculation**

```
last(custom_activity_type)
```

## Unique Email Open Rate

**Description**

The rate of unique open for unique emails delivered.

**Calculation**

```
rate( unique(email_open_campaign), unique(email_delivered_campaign) )
```

---

# Calculation Descriptions

Traits use one or more calculations to derive a value, which are reused across multiple traits. For example, *Total Events Attended* and *Total Tasks* both use the 'total' calculation.

Note: These are not the exact formulas used in calculating traits, but are representative for the purpose of documentation.

## Exists

Given a data object or array, returns TRUE if the object exists or the array is not empty.

## First

Given a set of timestamped data objects, returns an attribute of the object with the oldest date.

## First Not Null

Given a set of data objects, returns an attribute of the first object where the attribute appears.

## Last

Given a set of timestamped data objects, returns an attribute of the object with the most recent date.

## Rate

Given two sets of activities, find the count of each and return the division of the larger from the smaller

## Total

Counts all items of a specific data type and returns a number.

## Unique

Given a set of data objects, returns a set of unique items, ensuring each item is listed only once.

---

# Understanding Milestones, Touchpoints, and User Activities

## Milestones

Milestones in Element451 are organized based on their expected sequence in the admission process, as opposed to an arbitrary ordering. Here's how they work:

* **Automatically Generated Milestones**: As students move through Forms, Applications, and Decisions, most Milestones (except for "Enroll") are automatically created by Element451. This includes "Created" and "Application Completed."  
  ​
* **Manually Generated Milestones**: The Milestones "Checklist Complete," "Application Decision," "Graduate," and "Enroll" must be manually generated or imported.

**View a complete ordered list of Milestones**

1. Enroll
2. Deposit
3. Withdraw
4. Deferred
5. Admit
6. Conditional Admit
7. Waitlist
8. Denied
9. Hold
10. Application Submit
11. Application Start
12. Prospect
13. (Created, Application Completed, Checklist Complete, Application Decision, Graduate)

## Touchpoints

Touchpoints refer to activities connected to a person, initiated either by staff (Element451 internal users) or automation within Element451.  
​

**View a complete list of Touchpoints**

* Decision Assignment Updated
* Decision Checklist Item Added
* Decision Checklist Item Removed
* Decision Checklist Item Updated
* Decision Criteria Deleted
* Decision Criteria Updated
* Decision Note Added
* Decision Note Deleted
* Decision Note Updated
* Decision Stage Updated
* Decision Status Updated
* Decision Released
* Email Delivered
* External Activity Completed
* SMS Delivered
* Survey Key Created
* Survey Response Completed
* Task Created
* Task Assigned
* User Created
* User Profile Address Updated
* User Profile Email Updated
* User Profile Milestones Updated
* User Profile Name Updated
* User Profile Updated

## User Activities

**User** **Activities** detail actions initiated by the person, distinguishing them from Touchpoints. These include any interaction or step taken by the person, like engaging with applications or communications.

**View a complete list of User Activities**

* Application Completed
* Application Paid
* Application Registration Successful
* Application Submitted
* Appointment Attended
* Appointment Canceled
* Appointment Scheduled
* Appointment Updated
* Email Clicked
* Email Complaint
* Email Delivered
* Email Inbound Received
* Email Opened
* Email Unsubscribed
* Event Marked Attended
* Event Registration Canceled
* Event Registration Successful
* Form Submitted
* Pageview
* Recommendation Requested
* SMS Clicked
* SMS Delivered
* SMS Inbound Received
* Supplemental Form Submitted
* Survey Answered
* Survey Key Created
* Survey Key Opened
* Survey Response Completed
* Survey Response Saved
* User Created
* User Forgot Password
* User Login

---

# Choosing Between “Active Term” and “Application Term” in Segments

When building segments for communications, deciding between **Active Term** and **Application Term** can be tricky. Here’s a breakdown to help you choose the right option for your needs.

## Active Term

* **Focus:** The student’s current engagement with your institution.
* **Best for:** Communications based on a student’s most recent interactions, regardless of their application history.
* **Examples:**

  + Sending a welcome email to students who recently submitted an RFI form.
  + Inviting students to an event related to their intended major.
  + Reminding students to complete outstanding tasks for their active term.

## Application Term

* **Focus:** The specific term associated with a student’s application.
* **Best for:** Communications related to the application process or the term for which the student applied.
* **Examples:**

  + Sending updates about application deadlines or requirements.
  + Informing students about their admission status for a specific term.
  + Requesting final transcripts or enrollment deposits for the application term.

## How to Decide

Consider these factors when selecting the appropriate term field:

* **Communication Content:** Is the message about the student’s current engagement or their original application?
* **Tokens Used:** Are you using tokens related to the application term (e.g., application term start date) or the active term?
* **Post-Application Activities:** If students engage with your institution after applying (e.g., submitting RFI forms, updating contact info), their active term may differ from their application term.

## Example Scenarios

You want to send an orientation event invite to admitted students.

* If you use **Active Term**, students engaged for other reasons—such as a summer program—could receive the message, even if they’re admitted for a future term.
* If you use **Application Term**, only students admitted for the specific term of the orientation event will receive the invite.

---