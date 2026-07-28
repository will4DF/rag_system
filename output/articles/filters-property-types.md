---
title: Filters: Property Types
url: https://help.element451.com/en/articles/8800347-filters-property-types
collection: People
---

# Overview

Element451 offers powerful filters to help you narrow down groups of people based on specific conditions. These filters are categorized by **Property Type**, which organizes the data into meaningful groups for easier selection and segmentation.

When creating a Segment, use the **Filter Type** drop-down menu to limit the list of available filters to those relevant to your needs.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1334431218/4eadbd58e84e484afb4006cd7651/filters.png?expires=1784333700&signature=a7465ffd1d42b8c15d3960277d93d5f7426c87009ce605ecd1e0e82d16456aa6&req=dSMkEs19nINeUfMW1HO4zYDJ9N2dYMu1TwIJKkw3d6tMce9zqmEljga2Fen3%0A5im8H5SQv2FNDM6rVUs%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1334431218/4eadbd58e84e484afb4006cd7651/filters.png?expires=1784333700&signature=a7465ffd1d42b8c15d3960277d93d5f7426c87009ce605ecd1e0e82d16456aa6&req=dSMkEs19nINeUfMW1HO4zYDJ9N2dYMu1TwIJKkw3d6tMce9zqmEljga2Fen3%0A5im8H5SQv2FNDM6rVUs%3D%0A)

## Notes About Property Types

* **Does Not Exist Operator**: This operator cannot be used in *Activity*, *Document*, or *Decision* filters to identify missing data. Instead, [label users](https://intercom.help/element451/en/articles/6953481-labels-overview) with the required data and exclude them from your filter.
* **Color Groupings**: Each Property Type is assigned a color, making it easier to visualize and organize Filters in your Segments. Color groupings make it easier to identify related Filters and ensure your Segments are logically structured.

  + Color Grouping Guide

    - **Blue**: Contacts
    - **Purple**: Decisions
    - **Maroon**: Tasks
    - **Orange**: Activity
    - **Green**: Documents
    - **Red**: Surveys
    - **Light Green**: Relationships
    - **No Color**: Appointments

---

# Property Types + Categories

## Users (People/Contacts)

These Filters relate to external users, such as students or applicants. They include personal information, preferences, and application-related data.

**Example Filters**:

* Name
* Bio/Demo Information
* Preferred Major
* Application Term

**Data Categories**:

* Academic Preferences
* Address
* Application
* Athletics
* Citizenship
* College
* Dates
* Education
* Emergency Contact
* Evaluations
* Events
* Funnel Stage
* High School
* Holds
* Identities
* Milestones
* Notes
* Phone
* Relationship
* School
* Sources
* Traits
* User
* User - Custom

###

## Activity

These Filters track user actions, such as account creation, application submission, or email engagement. These properties help you track how people interact with your communications, applications, and other efforts. For these actions, you can filter based on how often the student did the activity and within what time window.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1364636197/948bcb20db4a100c480e66c29a36/Important.png?expires=1784430000&signature=d78a11f8c99b714ed92a7bc214e25ff5fdff2e34630637720b0c80ed9545e43c&req=dSMhEs99m4BWXvMW3Hu4gbYPIHjULHcLMfLePdGwa6CHkND3GqFdX9aKRebJ%0Apg%3D%3D%0A)The **Activity** filter type does **not** **support** searching for multiple instances of the same activity using an **AND** condition.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1364637917/e9de97ef83c2a29b98cb59fdff0a/Activity+Filter+-+Two+Same.png?expires=1784333700&signature=6948efb2cb208db2702e8d3e220c2f0fda629568bc30b4dadd5d70caa8e83b4d&req=dSMhEs99moheXvMW1HO4zZRJMBpojhUv9E8KFSI%2FhD3Q5xBlHbB8qnqXuzBV%0AKCaNmXpKKKwLEMFUiCQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1364637917/e9de97ef83c2a29b98cb59fdff0a/Activity+Filter+-+Two+Same.png?expires=1784333700&signature=6948efb2cb208db2702e8d3e220c2f0fda629568bc30b4dadd5d70caa8e83b4d&req=dSMhEs99moheXvMW1HO4zZRJMBpojhUv9E8KFSI%2FhD3Q5xBlHbB8qnqXuzBV%0AKCaNmXpKKKwLEMFUiCQ%3D%0A)

**Example Filters**:

* Number of Applications Submitted
* SMS Sent within Last 30 Days

**Data Categories**:

* Account
* Application
* Appointment
* Courses
* Custom
* Decision
* Email
* Events
* Forms
* Info Request
* Journey
* Page
* Phone Call
* SMS
* Survey
* Task

## Relationship

These Filters are based on [relationships](https://intercom.help/element451/en/articles/8903525-family-members-relationships) between contacts, such as a parent and child.

* The first part of the type refers to the person you are querying for.
* The second part and the filters below refer to the person they must be related to (for example, Parent-Child).

**Example Filters**:

* Relationship Type
* Specific Attributes of the Related Person

## Tasks

These Filters focus on [Task](https://intercom.help/element451/en/articles/3065709-getting-started-with-tasks)-related data, such as status, priority, and type.

**Example Filters**:

* Task Status (e.g., Completed or Overdue)
* Task Type

## Decisions

Filters for [decision](https://intercom.help/element451/en/articles/9200421-getting-started-with-decisions)-related data, such as application checklist items or decision statuses.

**Example Filters**:

* Missing Checklist Items
* Last Reviewer

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1345574500/d1751722b25f295e91ce4695bd1e/Note.png?expires=1784430000&signature=4aebf39933a34be736378bba1fc7ff6e2100a37b339f19567751f0811f9d058b&req=dSMjE8x5mYRfWfMW3Hu4gWQj0yPjrLXyWZadiNj6f6OATZ%2BIJ8vIW%2BpvJMZy%0AqA%3D%3D%0A) The "*Checklist Completed"* filter lets you filter by completed checklists, with the option to narrow it down to a specific property (e.g., term or application). In contrast, the "*Checklist Item"* filter allows you to filter by a specific checklist item (e.g., a transcript document).

## Documents

Filter users based on documents that have been created and mapped to fields and tags such as transcripts.

* One of the most commonly used searches is the [Document Type](https://intercom.help/element451/en/articles/2433933-managing-document-types), which allows you to segment if specific document types have been submitted.

**Example Filters**:

* Document Type
* Submission Date

## Surveys

Filters based on [survey](https://intercom.help/element451/en/articles/5405227-getting-started-with-surveys) responses or completion statuses.

**Example Filters**:

* Survey Completed (count)
* Survey Answered

## Appointments

Filters related to one-on-one [appointments](https://intercom.help/element451/en/articles/8141376-getting-started-with-appointments-for-admins) with users, such as appointment type and status.

**Example Filters**:

* Appointment Type
* Assignee

## Conversations

These Filters focus on [conversation](https://help.element451.com/en/articles/1894279-getting-started-with-conversations) data, such as status, delivery method, and AI-analyzed engagement signals.

* Status
* Created At
* Last Activity At
* Delivery Method
* Assigned To
* Is Anonymous?
* AI Confusion Score
* AI Conversation Type
* AI Customer Experience Score
* AI Engagement Score
* Intent to Stop Communications?
* Needs Follow-Up after AI?
* AI Sentiment Analysis
* AI Tone Analysis

## Courses

These Filters focus on [course and enrollment data](https://help.element451.com/en/articles/10420398-getting-started-with-courses), such as grades, section details, and instructor information.

* Course - Category
* Enrollment - Current Grade (number)
* Enrollment - Current Grade (text)
* Enrollment - Risk Level
* Enrollment - Final Grade (number)
* Enrollment - Final Grade (text)
* Enrollment - Institution ID
* Enrollment - Last Attended Date
* Enrollment - Last LMS Activity
* Enrollment - Last Course Access Date
* Enrollment - LMS URL
* Section
* Section - Campus
* Section - Code
* Section - End Date
* Section - Institution ID
* Section - Instruction Mode
* Section - Instructors
* Section - Instructor
* Section - Instructor Email
* Section - School

## Transcripts

These Filters focus on academic transcript data, such as GPA, credits, courses, and institution details.

* Class Rank Percentile
* Class Rank Decile
* Concentrations
* Converted 4.0 Core GPA
* Converted 4.0 Unweighted GPA
* Converted 4.0 Weighted GPA
* Course (College)
* Course (High School)
* Course Level Totals
* Created At
* Credits Attempted
* Credits Completed
* Credits Earned
* Cumulative Reported GPA
* Cumulative Recalculated GPA
* Degree Level
* Degree Programs
* Degree Type
* Doctoral 700+ Level Courses
* Graduation Date
* Graduate 500-699 Level Courses
* Highest Course per Academic Area
* Highest Course per Subject
* Institution Address
* Institution Code
* Institution Name
* Institution Type
* Institutional Credits
* Institutional Reported GPA
* Institutional Recalculated GPA
* Last 30 Credits GPA
* Majors
* Minors
* Major GPA
* Reported Weighted GPA
* Reported Unweighted GPA
* SAT
* STEM Count
* Student ID
* Subject Area Totals
* Transcript Date
* Transfer Credits
* Upper Division 300-400 Level Courses

## Cases (Closed Beta)

These Filters focus on Case-related data ([Case Management](https://help.element451.com/en/articles/13764725-getting-started-with-case-management-closed-beta)), such as type, priority, status, and associated activity.

* Case Type
* Case Priority
* Case Status
* Case Status Category
* Confidentiality
* Assigned To
* Subscribers
* Created By
* Created At
* Due At
* Updated At
* Resolved At
* Closed At
* Number Of Tasks
* Has Open Tasks
* Has Conversations
* Has Notes
* Has Documents
* Has Alerts Attached
* Number Of Attached Alerts

## Alerts (Closed Beta)

These Filters focus on Alert-related data ([Case Management](https://help.element451.com/en/articles/13764725-getting-started-with-case-management-closed-beta)), such as type, priority, status, and review history.

* Alert Type
* Alert Priority
* Alert Status
* Alert Status Category
* Reviewer
* Created By
* Created At
* Reviewed At
* Escalated At
* Resolved At
* Dismissed At
* Has Associated Case
* Associated Case Type
* Associated Case Status

---

# Combining Filters: All (AND) + Any (OR)

Filters from **different Property Types** (different colors) are always connected using the **All (AND)** operator. Filters with the same color can be grouped using either Any (OR) or All (AND), but the **Any (OR)** operator cannot be used between Filters from different Property Types. For Example:

* A segment looking for students in Missouri **AND** who have uploaded a transcript will connect the Filters automatically with All (AND).
* You cannot create a segment where students are in Missouri **OR** have uploaded a transcript.

For more details about using operators, see our [help article on operators](https://intercom.help/element451/en/articles/3648165-filters-all-any-operators).

#

---