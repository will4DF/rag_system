---
title: Import Mapping Examples
url: https://help.element451.com/en/articles/9620676-import-mapping-examples
collection: Data Management
---

Sharing inspiration on what to map with common import examples.

# Overview

You understand the Import feature, but now you have a file you need to import and don't know if you have mapped all the necessary fields. In this article we will share some common examples of imports and fields we recommend mapping to help you feel confident in your import abilities.

---

# Helpful Articles

[Explore More: Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports)

[Explore More: Column Setting Options](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports)

[Explore More: Data Quality Guide](https://help.element451.com/en/articles/9006443-data-quality-guide)

---

## Example 1: Purchased Name List

**Scenario:** You have just received a list of names of students. These students have not directly expressed interest in your institution, but you want to import their contact information and send a generic email to them to potentially spark interest.

**At Minimum, Map:**

* First Name (user-first-name)
* Last Name (user-last-name)
* Personal Email (user-email-address)

**Optional, but Recommended:**

* Address Information (user-addresses-...)
* Date of Birth (user-dob)
* School Information (user-education-...)
* Guardian Information (user-family-...)
* Source Code (user-sources-source-code)
* Source Date (user-sources-source-date)
* Intended Term (user-education-term)
* Intended Major (user-education-prefered-major)

## Example 2: Inquiry Form from 3rd Party

**Scenario:** Along with using the Element451 forms, you have an additional platform that collects student data from Request For Information forms. You receive these files on a daily basis and need to import the students as inquiries into Element451 so they can be entered into your inquiry workflow.

**At Minimum, Map:**

* First Name (user-first-name)
* Last Name (user-last-name)
* Personal Email (user-email-address)
* Intended Term (user-education-term)
* Intended Major (user-education-prefered-major)
* Date of Inquiry Date (user-milestones-prospect-date)
* Date of Inquiry Term (user-milestones-prospect-term)
* Date of Inquiry Major (user-milestones-prospect-major)

**Optional, but Recommended:**

* Address Information (user-addresses-...)
* Date of Birth (user-dob)
* School Information (user-education-...)
* Guardian Information (user-family-...)
* Source Code (user-sources-source-code)
* Source Date (user-sources-source-date)

## Example 3: Applications from 3rd Party

**Scenario:** In addition to using the Element451 Application feature, you are also received applications from other vendors. You want these students to be imported into Element451 where it looks like they practically applied using the Element451 Application feature. These students need to be moved to decisions so staff can start making admission decisions on them. For detailed instructions, check out [Importing Application Data](https://help.element451.com/en/articles/9007767-importing-application-data).

**At Minimum, Map:**

* First Name (user-first-name)
* Last Name (user-last-name)
* Personal Email (user-email-address)
* Address Information (user-addresses-...)
* Date of Birth (user-dob)
* Demographic Information
* School Information (user-education-...)
* Application Term (user-applications-term)
* Application Major (user-applications-major)
* Application Status (user-applications-status)
* Application Registered/Started Date (user-applications-registered-at)
* Application Submitted Date (user-applications-submitted-time)
* Milestone Application Start Date (user-milestones-application-start-date)
* Milestone Application Start Date Term (user-milestones-application-start-term)
* Milestone Application Start Date Major (user-milestones-application-start-major)
* Milestone Application Submit Date (user-milestones-application-submit-date)
* Milestone Application Submit Date Term (user-milestones-application-submit-term)
* Milestone Application Submit Date Major (user-milestones-application-submit-major)
* Label, used to trigger the [decisions rule](https://help.element451.com/en/articles/9007767-importing-application-data#h_41e578a199) (user-labels)

**Optional, but Recommended:**

* Guardian Information (user-family-...)
* Source Code (user-sources-source-code)
* Source Date (user-sources-source-date)
* Application Student Type (user-applications-student-type)
* Application Campus (user-applications-campus)
* Application Degree (user-applications-degree)
* Milestone Application Start Date Student Type (user-milestones-application-start-student-type)
* Milestone Application Start Date - Application GUID (user-milestones-application-start-guid)
* Milestone Application Submit Date Student Type (user-milestones-application-submit-student-type)
* Milestone Application Submit Date - Application GUID (user-milestones-application-submit-guid)

## Example 4: Enrolled Students

**Scenario:** Your admitted students have been sent to your student information system to receive ID numbers, school emails, and registration instructions. You now have a list of students that have registered for courses for their application term and you want to mark them as enrolled in Element451.

**At Minimum, Map:**

* Personal Email (user-email-address)
* Element ID or Spark ID, whatever identifier was sent over to the student information system (user-elementid or user-identities-sparkid)
* School ID (user-identities-schoolid)
* School Email (user-identities-school-email)
* Enrolled Date (user-milestones-enroll-date)
* Enrolled Term (user-milestones-enroll-term)

**Optional, but Recommended:**

* First Name (user-first-name)
* Last Name (user-last-name)
* Enrolled Major (user-milestones-enroll-major)
* Enrolled Student Type (user-milestones-enroll-student-type)

---