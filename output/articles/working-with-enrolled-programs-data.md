---
title: Working with Enrolled Programs Data
url: https://help.element451.com/en/articles/15032196-working-with-enrolled-programs-data
collection: People
---

How to use Enrolled Programs data across Element451: imports and exports, segments, workflows, campaign merge tags, and the API.

# Overview

Enrolled Programs data can be used throughout Element451 in imports/exports, segments, workflows, campaigns, and the API. This article covers the available tools and patterns.

---

# Importing and Exporting Enrolled Programs Data

Enrolled Programs data can be imported and exported using the standard Import/Export tool. Fields marked with an asterisk (`*`) are the **identifier** versions used to match and update existing records.

|  |  |
| --- | --- |
| **Program Major** | `user-programs-major` |
| **Program Major \*** | `user-programs-major-*` |
| **Program Status** | `user-programs-status` |
| **Program Status \*** | `user-programs-status-*` |
| **Program Degree** | `user-programs-degree_code` |
| **Program Degree \*** | `user-programs-degree_code-*` |
| **Program Term** | `user-programs-term` |
| **Program Term \*** | `user-programs-term-*` |
| **Program Campus** | `user-programs-campus` |
| **Program Campus \*** | `user-programs-campus-*` |
| **Program Cumulative GPA** | `user-programs-cumulative_gpa` |
| **Program Cumulative GPA \*** | `user-programs-cumulative_gpa-*` |
| **Program Major GPA** | `user-programs-major_gpa` |
| **Program Major GPA \*** | `user-programs-major_gpa-*` |
| **Program Earned Credits** | `user-programs-earned_credits` |
| **Program Earned Credits \*** | `user-programs-earned_credits-*` |
| **Program Attempted Credits** | `user-programs-attempted_credits` |
| **Program Attempted Credits \*** | `user-programs-attempted_credits-*` |
| **Program Required Credits** | `user-programs-required_credits` |
| **Program Required Credits \*** | `user-programs-required_credits-*` |
| **Program Start Date** | `user-programs-start_date` |
| **Program Start Date \*** | `user-programs-start_date-*` |
| **Program End Date** | `user-programs-end_date` |
| **Program End Date \*** | `user-programs-end_date-*` |
| **Program External ID** | `user-programs-external_id` |
| **Program External ID \*** | `user-programs-external_id-*` |
| **Program Item ID** | `user-programs-item_id` |
| **Program Item ID \*** | `user-programs-item_id-*` |

---

# Building Segments with Enrolled Programs

You can target contacts based on their Enrolled Programs data using the **Program (All Properties)** filter when building a segment.

Available properties:

* Major
* Status
* Degree
* Term
* Campus
* Cumulative GPA
* Major GPA
* Earned Credits
* Attempted Credits
* Item ID

**Example segments:**

* Students enrolled in Nursing with a Cumulative GPA below 2.0
* Students with an active program at a specific campus
* Students whose attempted credits exceed earned credits by a defined margin

**Note:** Users without the **View Enrolled Program GPA** permission cannot use GPA-based filters in segments.

---

# Triggering Workflows

There is no dedicated "Program Added" or "Program Updated" trigger. To run a workflow based on Enrolled Programs data, use the **Join Segment** trigger:

1. Build a segment using the Program (All Properties) filter.
2. Create a workflow with the **Join Segment** trigger pointed at that segment.
3. When a contact's Enrolled Programs data changes such that they newly match the segment, the workflow fires.

This pattern enables use cases like:

* Sending a retention email when a student's GPA drops below a threshold
* Notifying an advisor when a student declares a new major
* Triggering an outreach sequence for students approaching credit completion

---

# Using Tags in Campaigns

Three Enrolled Programs merge tags are available in email and SMS campaigns:

|  |  |
| --- | --- |
| **Tag** | **Output** |
| `[program:program_major_name]` | The student's program major name |
| `[program:program_campus_name]` | The student's program campus name |
| `[program:program_term_name]` | The student's program term name |

These tags resolve to the human-readable referenced values from the linked data sources, not internal IDs.

---

# API Access

For programmatic access, the Enrolled Programs API endpoint is:

`/v2/users/:userId/profile/programs`

Supported operations:

* `GET`: List a contact's program records
* `POST`: Create a new program record
* `PUT`: Update an existing program record (by Item ID)
* `DELETE`: Remove a program record (by Item ID)

Refer to the Element451 API documentation for full request and response schemas.

---