---
title: Field Reference: Application, Decision + Checklist Fields
url: https://help.element451.com/en/articles/15901975-field-reference-application-decision-checklist-fields
collection: Data Management
---

Every standard application, decision, and decision checklist field with its slug, type, purpose, and an example value.

# Applications (94 fields)

Note: Must use unwinding or root slug "user-applications-root" when using an inline template. Titles ending in \* are repeater (per-application) variants.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **Data Source** | **What It Does** | **Example** |
| Application - Activities | `user-applications-activities` | array |  | Application - Activities. Stored on the application record attached to the contact. | 28 |
| Application - Associate Degree? | `user-applications-associated-degree` | boolean |  | Application - Associate Degree?. Stored on the application record attached to the contact. | true / false |
| Application - Associate Degree? \* | `user-applications-associated-degree-*` | boolean |  | Application - Associate Degree?. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application - Auto Submit? | `user-applications-submission-auto` | boolean |  | Application - Auto Submit?. Stored on the application record attached to the contact. | true / false |
| Application - Auto Submit? \* | `user-applications-submission-auto-*` | boolean |  | Application - Auto Submit?. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application - Decision Type | `user-applications-plan-type` | string |  | Application - Decision Type. Stored on the application record attached to the contact. | Text value |
| Application - Decision Type \* | `user-applications-plan-type-*` | string |  | Application - Decision Type. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application - Degree | `user-applications-degree` | string | Transformations for degrees | Application - Degree. Stored on the application record attached to the contact. Options come from: Transformations for degrees. | Bachelor of Science |
| Application - Degree \* | `user-applications-degree-*` | string |  | Application - Degree. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Bachelor of Science |
| Application - Department | `user-applications-department` | string |  | Application - Department. Stored on the application record attached to the contact. | Text value |
| Application - Department \* | `user-applications-department-*` | string |  | Application - Department. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application - FAFSA? | `user-applications-fafsa` | boolean |  | Application - FAFSA?. Stored on the application record attached to the contact. | true / false |
| Application - FAFSA? \* | `user-applications-fafsa-*` | boolean |  | Application - FAFSA?. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application - Financial Aid? | `user-applications-financial-aid` | boolean |  | Application - Financial Aid?. Stored on the application record attached to the contact. | true / false |
| Application - Financial Aid? \* | `user-applications-financial-aid-*` | boolean |  | Application - Financial Aid?. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application - Has Associates Degree? | `user-applications-associates` | boolean |  | Application - Has Associates Degree?. Stored on the application record attached to the contact. | true / false |
| Application - Honor Society? | `user-applications-honor-society` | boolean |  | Application - Honor Society?. Stored on the application record attached to the contact. | true / false |
| Application - Housing Interest | `user-applications-housing` | string | Values for Housing List | Application - Housing Interest. Stored on the application record attached to the contact. Options come from: Values for Housing List. | Text value |
| Application - Housing Interest \* | `user-applications-housing-*` | string | Values for Housing List | Application - Housing Interest. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Values for Housing List. | Text value |
| Application - Opt in for SMS \* | `user-application-sms-updates-*` | boolean |  | Application - Opt in for SMS. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application - Payment Waiver Code | `user-applications-payment-waiver-code` | string |  | Application - Payment Waiver Code. Stored on the application record attached to the contact. | Text value |
| Application - Pre Professional Programs | `user-applications-preprofessional-programs` | string |  | Application - Pre Professional Programs. Stored on the application record attached to the contact. | Biology |
| Application - Previously Applied Semester | `user-applications-previous-semester` | string |  | Application - Previously Applied Semester. Stored on the application record attached to the contact. | Text value |
| Application - Previously Applied? | `user-applications-previously-applied` | boolean | Values for [SYS] Yes/No | Application - Previously Applied?. Stored on the application record attached to the contact. Options come from: Values for [SYS] Yes/No. | Yes / No |
| Application - School | `user-applications-school` | string | Transformations for schools | Application - School. Stored on the application record attached to the contact. Options come from: Transformations for schools. | Text value |
| Application - School \* | `user-applications-school-*` | string |  | Application - School. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application - Special Programs | `user-applications-special-programs` | array |  | Application - Special Programs. Stored on the application record attached to the contact. | Biology |
| Application - Student Type | `user-applications-student-type` | string | Values for [SYS] Student Types | Application - Student Type. Stored on the application record attached to the contact. Options come from: Values for [SYS] Student Types. | Text value |
| Application - Student Type \* | `user-applications-student-type-*` | string |  | Application - Student Type. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Campus | `user-applications-campus` | string | Transformations for campuses | Application Campus. Stored on the application record attached to the contact. Options come from: Transformations for campuses. | Main Campus |
| Application Campus \* | `user-applications-campus-*` | string |  | Application Campus. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Main Campus |
| Application Completed Date | `user-applications-completed-at` | date |  | Application Completed Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Completed Date \* | `user-applications-completed-at-*` | date |  | Application Completed Date. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Concentration | `user-applications-concentration` | string |  | Application Concentration. Stored on the application record attached to the contact. | Text value |
| Application Concentration \* | `user-applications-concentration-*` | string |  | Application Concentration. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Creation Date | `user-applications-registered-at` | date |  | Application Creation Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Creation Date \* | `user-applications-registered-at-*` | date |  | Application Creation Date. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Decision - Assigned to User \* | `user-applications-assigned-to-user-id-*` | mongoid |  | Application Decision - Assigned to User. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Application Decision - Board Stage \* | `user-applications-board-stage-*` | string |  | Application Decision - Board Stage. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Decision - Board Status | `user-applications-board-status` | string |  | Application Decision - Board Status. Stored on the application record attached to the contact. | Text value |
| Application Decision - Board Status \* | `user-applications-board-status-*` | string |  | Application Decision - Board Status. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Decision - Cohorts \* | `user-applications-cohorts-*` | array |  | Application Decision - Cohorts. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | multiple values (list) |
| Application Decision - Tags \* | `user-applications-tags-items-*` | array |  | Application Decision - Tags. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | multiple values (list) |
| Application Decision Release Date | `user-applications-decision-released-at` | date |  | Application Decision Release Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Decision Release Date \* | `user-applications-decision-released-at-*` | date |  | Application Decision Release Date. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Guid | `user-applications-guid` | string |  | Application Guid. Stored on the application record attached to the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Application Guid \* | `user-applications-guid-*` | string |  | Application Guid. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Application Last Login Date | `user-applications-last-login` | date |  | Application Last Login Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Last Login Date \* | `user-applications-last-login-*` | date |  | Application Last Login Date. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Last Updated Date | `user-applications-updated-at` | date |  | Application Last Updated Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Last Updated Date \* | `user-applications-updated-at-*` | date |  | Application Last Updated Date. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Major | `user-applications-major` | string | Transformations for Majors | Application Major. Stored on the application record attached to the contact. Options come from: Transformations for Majors. | Biology |
| Application Major - Second | `user-applications-major-second` | string | Transformations for Majors | Application Major - Second. Stored on the application record attached to the contact. Options come from: Transformations for Majors. | Biology |
| Application Major - Second \* | `user-applications-major-second-*` | string |  | Application Major - Second. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Biology |
| Application Major - Third | `user-applications-major-third` | string | Transformations for Majors | Application Major - Third. Stored on the application record attached to the contact. Options come from: Transformations for Majors. | Biology |
| Application Major - Third \* | `user-applications-major-third-*` | string |  | Application Major - Third. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Biology |
| Application Major \* | `user-applications-major-*` | string |  | Application Major. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Biology |
| Application Minor | `user-applications-minor` | string |  | Application Minor. Stored on the application record attached to the contact. | Text value |
| Application Minor \* | `user-applications-minor-*` | string |  | Application Minor. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Payment - Successful | `user-applications-payment-successful` | boolean |  | Application Payment - Successful. Stored on the application record attached to the contact. | true / false |
| Application Payment - Time | `user-applications-payment-time` | date |  | Application Payment - Time. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Payment - Time \* | `user-applications-payment-time-*` | date |  | Application Payment - Time. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Payment Amount | `user-applications-payment-amount` | float |  | Application Payment Amount. Stored on the application record attached to the contact. | 50.00 |
| Application Progress | `user-applications-numeric-progress` | integer |  | Application Progress. Stored on the application record attached to the contact. | 160 |
| Application Progress \* | `user-applications-numeric-progress-*` | integer |  | Application Progress. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 160 |
| Application Registration Id | `user-applications-registration-id` | string |  | Application Registration Id. Stored on the application record attached to the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Application Registration Id \* | `user-applications-registration-id-*` | string |  | Application Registration Id. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Application Status | `user-applications-status` | string |  | Application Status. Stored on the application record attached to the contact. | Text value |
| Application Status \* | `user-applications-status-*` | string |  | Application Status. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Submission - Convicted Explanation | `user-applications-submission-convicted-explanation` | string |  | Application Submission - Convicted Explanation. Stored on the application record attached to the contact. | Text value |
| Application Submission - Convicted Explanation \* | `user-applications-submission-convicted-explanation-*` | string |  | Application Submission - Convicted Explanation. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Submission - Convicted? | `user-applications-submission-convicted` | boolean |  | Application Submission - Convicted?. Stored on the application record attached to the contact. | true / false |
| Application Submission - Convicted? \* | `user-applications-submission-convicted-*` | boolean |  | Application Submission - Convicted?. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application Submission - Electronic Sign | `user-applications-submission-electronic-sign` | string |  | Application Submission - Electronic Sign. Stored on the application record attached to the contact. | Text value |
| Application Submission - Electronic Sign \* | `user-applications-submission-electronic-sign-*` | string |  | Application Submission - Electronic Sign. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Submission - Legal Note Confirm \* | `user-applications-submission-legal-note-confirm-*` | boolean |  | Application Submission - Legal Note Confirm. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application Submission - School Problems | `user-applications-submission-school-problems` | boolean |  | Application Submission - School Problems. Stored on the application record attached to the contact. | true / false |
| Application Submission - School Problems \* | `user-applications-submission-school-problems-*` | boolean |  | Application Submission - School Problems. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Application Submission - School Problems Explanation | `user-applications-submission-school-problems-explanation` | string |  | Application Submission - School Problems Explanation. Stored on the application record attached to the contact. | Text value |
| Application Submission - School Problems Explanation \* | `user-applications-submission-school-problems-explanation-*` | string |  | Application Submission - School Problems Explanation. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Application Submitted Date | `user-applications-submitted-time` | date |  | Application Submitted Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Submitted Date | `user-applications-term-submitted-time` | date |  | Application Submitted Date. Stored on the application record attached to the contact. | 2026-08-15 |
| Application Submitted Date \* | `user-applications-submitted-time-*` | date |  | Application Submitted Date. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2026-08-15 |
| Application Term | `user-applications-term` | string | Transformations for Term | Application Term. Stored on the application record attached to the contact. Options come from: Transformations for Term. | Fall 2026 |
| Application Term \* | `user-applications-term-*` | string |  | Application Term. Stored on the application record attached to the contact. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Fall 2026 |
| Decision assigned to user | `decisions-assigned-to-user` | mongoid |  | Decision assigned to user. Stored on the application record attached to the contact. | Text value |
| Decision created | `decisions-created_at` | date |  | Decision created. Stored on the application record attached to the contact. | 2026-08-15 |
| Decision evaulation score | `decisions-score` | float |  | Decision evaulation score. Stored on the application record attached to the contact. | 28 |
| Decision last review date | `decisions-last-reviewer-date` | date |  | Decision last review date. Stored on the application record attached to the contact. | 2026-08-15 |
| Decision Last reviewer user | `decisions-last-reviewer-user` | mongoid |  | Decision Last reviewer user. Stored on the application record attached to the contact. | Text value |
| Decision stage id | `decisions-stage_id` | string |  | Decision stage id. Stored on the application record attached to the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision status guid | `decisions-status_guid` | string |  | Decision status guid. Stored on the application record attached to the contact. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision updated | `decisions-updated_at` | date |  | Decision updated. Stored on the application record attached to the contact. | 2026-08-15 |
| Have you ever been placed on probation, suspended, expelled, or refused readmission to any other college/university or school? | `user-applications-submission-school-probation-suspended-expelled` | boolean |  | Have you ever been placed on probation, suspended, expelled, or refused readmission to any other college/university or school?. Stored on the application record attached to the contact. | true / false |

# Decisions (12 fields)

Note: Currently cannot be exported through the API. Please use Applications to export this information.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **What It Does** | **Example** |
| Application Registration Id | `user-applications-registration-id` | string | Application Registration Id. Part of the decision record on an application. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision applications.guid | `decisions-application_guid` | string | Decision applications.guid. Part of the decision record on an application. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision assigned to user | `decisions-assigned-to-user` | mongoid | Decision assigned to user. Part of the decision record on an application. | Text value |
| Decision created | `decisions-created_at` | date | Decision created. Part of the decision record on an application. | 2026-08-15 |
| Decision evaulation score | `decisions-score` | float | Decision evaulation score. Part of the decision record on an application. | 28 |
| Decision last review date | `decisions-last-reviewer-date` | date | Decision last review date. Part of the decision record on an application. | 2026-08-15 |
| Decision Last reviewer user | `decisions-last-reviewer-user` | mongoid | Decision Last reviewer user. Part of the decision record on an application. | Text value |
| Decision Registration Id | `decisions-registration-id` | string | Decision Registration Id. Part of the decision record on an application. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision Released date | `decisions-decision-released-at` | date | Decision Released date. Part of the decision record on an application. | 2026-08-15 |
| Decision stage id | `decisions-stage_id` | string | Decision stage id. Part of the decision record on an application. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision status guid | `decisions-status_guid` | string | Decision status guid. Part of the decision record on an application. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision updated | `decisions-updated_at` | date | Decision updated. Part of the decision record on an application. | 2026-08-15 |

# Decisions Checklist (13 fields)

Note: Currently requires exporting through unwinding when using an inline template. Root mapping for all fields: decisions-checklist-root.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **What It Does** | **Example** |
| Decision checklist \_id | `decisions-checklist-_id` | string | Decision checklist \_id. Part of the decision checklist on an application. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Decision checklist ceeb | `decisions-checklist-ceeb` | string | Decision checklist ceeb. Part of the decision checklist on an application. | 345678 |
| Decision checklist completed\_at | `decisions-checklist-completed_at` | date | Decision checklist completed\_at. Part of the decision checklist on an application. | 2026-08-15 |
| Decision checklist completed\_by | `decisions-checklist-completed_by` | string | Decision checklist completed\_by. Part of the decision checklist on an application. | Text value |
| Decision checklist completed\_by\_user | `decisions-checklist-completed_by_user` | mongoid | Decision checklist completed\_by\_user. Part of the decision checklist on an application. | Text value |
| Decision checklist index\_weight | `decisions-checklist-index_weight` | integer | Decision checklist index\_weight. Part of the decision checklist on an application. | 2 |
| Decision checklist item\_key | `decisions-checklist-item_key` | string | Decision checklist item\_key. Part of the decision checklist on an application. | Text value |
| Decision checklist name | `decisions-checklist-name` | collection-item | Decision checklist name. Part of the decision checklist on an application. | Text value |
| Decision checklist status | `decisions-checklist-status` | string | Decision checklist status. Part of the decision checklist on an application. | Text value |
| Decision checklist status\_changed\_at | `decisions-checklist-status_changed_at` | date | Decision checklist status\_changed\_at. Part of the decision checklist on an application. | 2026-08-15 |
| Decision checklist type | `decisions-checklist-type` | string | Decision checklist type. Part of the decision checklist on an application. | Text value |
| Decision checklist updated\_at | `decisions-checklist-updated_at` | date | Decision checklist updated\_at. Part of the decision checklist on an application. | 2026-08-15 |
| Decision checklist visible | `decisions-checklist-visible` | boolean | Decision checklist visible. Part of the decision checklist on an application. | true / false |

---