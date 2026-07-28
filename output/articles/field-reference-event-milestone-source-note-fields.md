---
title: Field Reference: Event, Milestone, Source + Note Fields
url: https://help.element451.com/en/articles/15902096-field-reference-event-milestone-source-note-fields
collection: Data Management
---

Every standard event, milestone, source, and user note field with its slug, type, purpose, and an example value.

# Events (21 fields)

Note: Does not require a root item when using an inline template.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **What It Does** | **Example** |
| Date of Last Event Attended - Calculated | `user-calculated-date_of_last_event_attended-new` | date | Date of Last Event Attended. Calculated automatically by Element451 and read only. | 2026-08-15 |
| Date of Last Event Registration - Calculated | `user-calculated-date_of_last_event_registration-new` | date | Date of Last Event Registration. Calculated automatically by Element451 and read only. | 2026-08-15 |
| Event 1 Source Date | `user-sources-event_1_date` | date | Event 1 Source Date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Event 1 source name | `user-sources-event-1-name` | string | Event 1 source name. Related to event registration and attendance for the contact. | Text value |
| Event 2 Source Date | `user-sources-event_2_date` | date | Event 2 Source Date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Event 2 source name | `user-sources-event-2-name` | string | Event 2 source name. Related to event registration and attendance for the contact. | Text value |
| Event 3 Source Date | `user-sources-event_3_date` | date | Event 3 Source Date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Event 3 source name | `user-sources-event-3-name` | string | Event 3 source name. Related to event registration and attendance for the contact. | Text value |
| Event 4 Source Date | `user-sources-event_4_date` | date | Event 4 Source Date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Event 4 source name | `user-sources-event-4-name` | string | Event 4 source name. Related to event registration and attendance for the contact. | Text value |
| Event 5 Source Date | `user-sources-event_5_date` | date | Event 5 Source Date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Event 5 source name | `user-sources-event-5-name` | string | Event 5 source name. Related to event registration and attendance for the contact. | Text value |
| Event Source Date | `user-sources-event_date` | date | Event Source Date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Event source name | `user-sources-event-name` | string | Event source name. Related to event registration and attendance for the contact. | Text value |
| Event Type | `user-sources-event-type` | string | Event Type. Related to event registration and attendance for the contact. | Text value |
| Events 1 date | `user-events-1-event-date` | date | Events 1 date. Related to event registration and attendance for the contact. | 2026-08-15 |
| Events guests number | `user-events-guests-number` | integer | Events guests number. Related to event registration and attendance for the contact. | 2 |
| Events status: registration no show | `user-events-status-noshow` | boolean | Events status: registration no show. Related to event registration and attendance for the contact. | true / false |
| Last Event Attended - Calculated | `user-calculated-last_event_attended` | date | Last Event Attended. Calculated automatically by Element451 and read only. | 2026-08-15 |
| Last Event Registration - Calculated | `user-calculated-last_event_registration` | date | Last Event Registration. Calculated automatically by Element451 and read only. | 2026-08-15 |
| Total Events Attended - Calculated | `user-calculated-total_events_attended` | integer | Total Events Attended. Calculated automatically by Element451 and read only. | 2 |

# Milestones (79 fields)

Note: Requires the root slug "user-milestones-root" if you want more than the first matching milestone when using an inline template. Titles ending in \* are repeater (per-milestone) variants.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **Data Source** | **What It Does** | **Example** |
| Admitted Date | `user-milestones-admit-date` | date |  | Admitted Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Admitted Date - Major | `user-milestones-admit-major` | string | Transformations for Majors | Admitted Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Admitted Date - Term | `user-milestones-admit-term` | string | Transformations for Term | Admitted Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Application Complete Date | `user-milestones-application-complete-date` | date |  | Application Complete Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Application Complete Date - Major | `user-milestones-application-complete-major` | string | Transformations for Majors | Application Complete Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Application Complete Date - Term | `user-milestones-application-complete-term` | string | Transformations for Term | Application Complete Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Application Decision Date | `user-milestones-application-decision-date` | date |  | Application Decision Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Application Decision Major | `user-milestones-application-decision-major` | string | Transformations for Majors | Application Decision Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Application Decision Term | `user-milestones-application-decision-term` | string | Transformations for Term | Application Decision Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Application Start Date | `user-milestones-application-start-date` | date |  | Application Start Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Application Start Date - Major | `user-milestones-application-start-major` | string | Transformations for Majors | Application Start Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Application Start Date - Term | `user-milestones-application-start-term` | string | Transformations for Term | Application Start Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Application Submit Date | `user-milestones-application-submit-date` | date |  | Application Submit Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Application Submit Date - Application GUID | `user-milestones-application-submit-guid` | string |  | Application Submit Date - Application GUID. A funnel milestone recorded on the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Application Submit Date - Major | `user-milestones-application-submit-major` | string | Transformations for Majors | Application Submit Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Application Submit Date - Student Type | `user-milestones-application-submit-student-type` | string | Values for [SYS] Student Types | Application Submit Date - Student Type. A funnel milestone recorded on the contact. Options come from: Values for [SYS] Student Types. | Text value |
| Application Submit Date - Term | `user-milestones-application-submit-term` | string | Transformations for Term | Application Submit Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Checklist Complete Date | `user-milestones-checklist-complete-date` | date |  | Checklist Complete Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Checklist Complete Major | `user-milestones-checklist-complete-major` | string | Transformations for Majors | Checklist Complete Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Checklist Complete Term | `user-milestones-checklist-complete-term` | string | Transformations for Term | Checklist Complete Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Conditional Admit Date | `user-milestones-conditional-admit-date` | date |  | Conditional Admit Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Conditional Admit Major | `user-milestones-conditional-admit-major` | string | Transformations for Majors | Conditional Admit Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Conditional Admit Term | `user-milestones-conditional-admit-term` | string | Transformations for Term | Conditional Admit Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Date of Inquiry | `user-milestones-prospect-date` | date |  | Date of Inquiry. A funnel milestone recorded on the contact. | 2026-08-15 |
| Date of Inquiry Major | `user-milestones-prospect-major` | string | Transformations for Majors | Date of Inquiry Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Date of Inquiry Term | `user-milestones-prospect-term` | string | Transformations for Term | Date of Inquiry Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Deferred Date | `user-milestones-deferred-date` | date |  | Deferred Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Deferred Major | `user-milestones-deferred-major` | string | Transformations for Majors | Deferred Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Deferred Term | `user-milestones-deferred-term` | string | Transformations for Term | Deferred Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Denied Date | `user-milestones-denied-date` | date |  | Denied Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Denied Major | `user-milestones-denied-major` | string | Transformations for Majors | Denied Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Denied Term | `user-milestones-denied-term` | string | Transformations for Term | Denied Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Deposited Date | `user-milestones-deposit-date` | date |  | Deposited Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Deposited Date - Major | `user-milestones-deposit-major` | string | Transformations for Majors | Deposited Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Deposited Date - Term | `user-milestones-deposit-term` | string | Transformations for Term | Deposited Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Email Hard Bounce Date - Email | `user-milestones-hardbounce-email-email` | string |  | Email Hard Bounce Date - Email. A funnel milestone recorded on the contact. | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Email Hardbounce Date | `user-milestones-email-hardbounce-date` | date |  | Email Hardbounce Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Email Unsubscribe Date | `user-milestones-unsubscribe-email-date` | date |  | Email Unsubscribe Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Email Unsubscribe Date - Email | `user-milestones-unsubscribe-email-email` | string |  | Email Unsubscribe Date - Email. A funnel milestone recorded on the contact. | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Enrolled Date | `user-milestones-enroll-date` | date |  | Enrolled Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Enrolled Major | `user-milestones-enroll-major` | string | Transformations for Majors | Enrolled Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Enrolled Term | `user-milestones-enroll-term` | string | Transformations for Term | Enrolled Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Hold Date | `user-milestones-hold-date` | date |  | Hold Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Hold Major | `user-milestones-hold-major` | string | Transformations for Majors | Hold Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Hold Term | `user-milestones-hold-term` | string | Transformations for Term | Hold Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Interview Date | `user-milestones-interview-date` | date |  | Interview Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Interview Date - Interviewer | `user-milestones-interview-interviewer` | string |  | Interview Date - Interviewer. A funnel milestone recorded on the contact. | Text value |
| Interview Date - Major | `user-milestones-interview-major` | string | Transformations for Majors | Interview Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Interview Date - Term | `user-milestones-interview-term` | string | Transformations for Term | Interview Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Milestones App Type (Internal/External) \* | `user-milestones-application-type-*` | string |  | Milestones App Type (Internal/External). A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Milestones Application \* | `user-milestones-application-guid-*` | string |  | Milestones Application. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Milestones Date \* | `user-milestones-date-*` | date |  | Milestones Date. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Milestones Degree | `user-milestones-degree` | string | Transformations for degrees | Milestones Degree. A funnel milestone recorded on the contact. Options come from: Transformations for degrees. | Bachelor of Science |
| Milestones Degree \* | `user-milestones-degree-*` | string | Transformations for degrees | Milestones Degree. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Transformations for degrees. | Bachelor of Science |
| Milestones Interviewer \* | `user-milestones-interviewer-*` | string |  | Milestones Interviewer. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Milestones Major \* | `user-milestones-major-*` | string | Transformations for Majors | Milestones Major. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Transformations for Majors. | Biology |
| Milestones Name \* | `user-milestones-name-*` | string |  | Milestones Name. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Milestones Student Type \* | `user-milestones-student_type-*` | string | Values for [SYS] Student Types | Milestones Student Type. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Values for [SYS] Student Types. | Text value |
| Milestones Term \* | `user-milestones-term-*` | string | Transformations for Term | Milestones Term. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Transformations for Term. | Fall 2026 |
| Milestones Type \* | `user-milestones-type-*` | string |  | Milestones Type. A funnel milestone recorded on the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Record Created Date | `user-milestones-created-date` | date |  | Record Created Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| SMS Hard Bounce Date - Description | `user-milestones-hardbounce-sms-description` | string |  | SMS Hard Bounce Date - Description. A funnel milestone recorded on the contact. | Text value |
| SMS Hard Bounce Date - Error Code | `user-milestones-hardbounce-sms-error-code` | string |  | SMS Hard Bounce Date - Error Code. A funnel milestone recorded on the contact. | Text value |
| SMS Hard Bounce Date - Number | `user-milestones-hardbounce-sms-number` | string |  | SMS Hard Bounce Date - Number. A funnel milestone recorded on the contact. | Text value |
| SMS Hardbounce Date | `user-milestones-sms-hardbounce-date` | date |  | SMS Hardbounce Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| SMS Unsubscribe Date | `user-milestones-unsubscribe-sms-date` | date |  | SMS Unsubscribe Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| SMS Unsubscribe Date - Number | `user-milestones-unsubscribe-sms-number` | string |  | SMS Unsubscribe Date - Number. A funnel milestone recorded on the contact. | Text value |
| Visit Date (any) | `user-milestones-visit-date` | date |  | Visit Date (any). A funnel milestone recorded on the contact. | 2026-08-15 |
| Waitlist Date | `user-milestones-waitlist-date` | date |  | Waitlist Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Waitlist Date - App Type GUID | `user-milestones-waitlist-application-guid` | string |  | Waitlist Date - App Type GUID. A funnel milestone recorded on the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Waitlist Date - Student Type | `user-milestones-waitlist-student-type` | string | Values for [SYS] Student Types | Waitlist Date - Student Type. A funnel milestone recorded on the contact. Options come from: Values for [SYS] Student Types. | Text value |
| Waitlist Major | `user-milestones-waitlist-major` | string | Transformations for Majors | Waitlist Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Waitlist Term | `user-milestones-waitlist-term` | string | Transformations for Term | Waitlist Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |
| Withdrawn Date | `user-milestones-withdraw-date` | date |  | Withdrawn Date. A funnel milestone recorded on the contact. | 2026-08-15 |
| Withdrawn Date - App GUID | `user-milestones-withdraw-application-guid` | string |  | Withdrawn Date - App GUID. A funnel milestone recorded on the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Withdrawn Date - Major | `user-milestones-withdraw-major` | string | Transformations for Majors | Withdrawn Date - Major. A funnel milestone recorded on the contact. Options come from: Transformations for Majors. | Biology |
| Withdrawn Date - Reason | `user-milestones-withdraw-reason` | string |  | Withdrawn Date - Reason. A funnel milestone recorded on the contact. | Text value |
| Withdrawn Date - Student Type | `user-milestones-withdraw-student-type` | string | Values for [SYS] Student Types | Withdrawn Date - Student Type. A funnel milestone recorded on the contact. Options come from: Values for [SYS] Student Types. | Text value |
| Withdrawn Date - Term | `user-milestones-withdraw-term` | string | Transformations for Term | Withdrawn Date - Term. A funnel milestone recorded on the contact. Options come from: Transformations for Term. | Fall 2026 |

# Sources (26 fields)

Note: May require the root slug "user-sources-root" if you want more than the first matching source when using an inline template. Titles ending in \* are repeater (per-source) variants.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **Data Source** | **What It Does** | **Example** |
| Event 1 Source Date | `user-sources-event_1_date` | date |  | Event 1 Source Date. Describes where the contact or engagement originated. | 2026-08-15 |
| Event 1 source name | `user-sources-event-1-name` | string |  | Event 1 source name. Describes where the contact or engagement originated. | Text value |
| Event 2 Source Date | `user-sources-event_2_date` | date |  | Event 2 Source Date. Describes where the contact or engagement originated. | 2026-08-15 |
| Event 2 source name | `user-sources-event-2-name` | string |  | Event 2 source name. Describes where the contact or engagement originated. | Text value |
| Event 3 Source Date | `user-sources-event_3_date` | date |  | Event 3 Source Date. Describes where the contact or engagement originated. | 2026-08-15 |
| Event 3 source name | `user-sources-event-3-name` | string |  | Event 3 source name. Describes where the contact or engagement originated. | Text value |
| Event 4 Source Date | `user-sources-event_4_date` | date |  | Event 4 Source Date. Describes where the contact or engagement originated. | 2026-08-15 |
| Event 4 source name | `user-sources-event-4-name` | string |  | Event 4 source name. Describes where the contact or engagement originated. | Text value |
| Event 5 Source Date | `user-sources-event_5_date` | date |  | Event 5 Source Date. Describes where the contact or engagement originated. | 2026-08-15 |
| Event 5 source name | `user-sources-event-5-name` | string |  | Event 5 source name. Describes where the contact or engagement originated. | Text value |
| Event Source Date | `user-sources-event_date` | date |  | Event Source Date. Describes where the contact or engagement originated. | 2026-08-15 |
| Event source name | `user-sources-event-name` | string |  | Event source name. Describes where the contact or engagement originated. | Text value |
| Event Type | `user-sources-event-type` | string |  | Event Type. Describes where the contact or engagement originated. | Text value |
| Sources - Source Code (Alias) - Custom | `user-sources-source-code` | string | Transformation for Source Code (Alias) | Sources - Source Code (Alias) - Custom. Describes where the contact or engagement originated. Options come from: Transformation for Source Code (Alias). | Text value |
| Sources - Source Code (Alias) \* | `user-sources-alias-*` | string |  | Sources - Source Code (Alias). Describes where the contact or engagement originated. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Sources - Source Code Date - Custom | `user-sources-source-code-date` | date |  | Sources - Source Code Date - Custom. Describes where the contact or engagement originated. | 2026-08-15 |
| Sources - Source Code Segment - Custom | `user-sources-source-code-segment` | string |  | Sources - Source Code Segment - Custom. Describes where the contact or engagement originated. | Text value |
| Sources - Source Code Segment \* | `user-sources-segment-*` | string |  | Sources - Source Code Segment. Describes where the contact or engagement originated. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Sources index\_weight \* | `user-sources-index_weight-*` | integer |  | Sources index\_weight. Describes where the contact or engagement originated. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2 |
| Sources name \* | `user-sources-name-*` | string |  | Sources name. Describes where the contact or engagement originated. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Sources Timestamp \* | `user-sources-timestamp-*` | date |  | Sources Timestamp. Describes where the contact or engagement originated. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Sources type \* | `user-sources-type-*` | string |  | Sources type. Describes where the contact or engagement originated. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Web Source - UTM Campaign | `user-sources-web-properties-utm-campaign` | string |  | Web Source - UTM Campaign. Describes where the contact or engagement originated. | Text value |
| Web Source - UTM Content | `user-sources-web-properties-utm-content` | string |  | Web Source - UTM Content. Describes where the contact or engagement originated. | Text value |
| Web Source - UTM Medium | `user-sources-web-properties-utm-medium` | string |  | Web Source - UTM Medium. Describes where the contact or engagement originated. | Text value |
| Web Source - UTM Source | `user-sources-web-properties-utm-source` | string |  | Web Source - UTM Source. Describes where the contact or engagement originated. | Text value |

# User Notes (5 fields)

Note: Requires "user-notes-root" when using an inline template.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **What It Does** | **Example** |
| Note Author | `user-notes-admin-id` | string | Note Author. Part of a note on the contact record. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Note body (html) | `user-notes-note-body` | string | Note body (html). Part of a note on the contact record. | Text value |
| Note creation date | `user-notes-note-created` | date | Note creation date. Part of a note on the contact record. | 2026-08-15 |
| Note type | `user-notes-note-type` | string | Note type. Part of a note on the contact record. | Text value |
| Note update date | `user-notes-note-updated` | date | Note update date. Part of a note on the contact record. | 2026-08-15 |

---