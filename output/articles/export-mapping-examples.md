---
title: Export Mapping Examples
url: https://help.element451.com/en/articles/9621148-export-mapping-examples
collection: Data Management
---

Sharing inspiration on what to map with common export examples.

# Overview

To help you get started on building export tasks, we want to provide you with a good starting point. In this article we provide several scenarios of exports we see our partners building out and what fields to include.

---

# Helpful Articles

[Explore More: Creating Exports](https://help.element451.com/en/articles/9007317-creating-exports)

[Explore More: Column Setting Options for Exports](https://help.element451.com/en/articles/9007047-column-setting-options-for-exports)

---

# Examples

## **Example 1: Event Attendee List**

**Scenario**: An event has just completed and you want to share a list of attended students to another department with basic contact information.

**Repeat fields based on:** Events

**Items To Export:** All

**Order By:** Default

**Order:** Blank

**Conditions:** Events (All Properties) where record marked 'Attended' is true for a specific event name

Example of fields that can be mapped:

* First Name (user-first-name)
* Last Name (user-last-name)
* Email (user-email-address)
* School ID (user-identities-schoolid)
* Events Date (user-events-date)
* Events Registration Date (user-events-signup-status-created-date)
* Events Guest Number (user-events-guests-number)

## **Example 2: Application Status Report**

**Scenario**: You need to send out a weekly report around applications and their current status to track progression for the upcoming term.

**Repeat fields based on:** Applications

**Items To Export:** Last (most recent/latest)

**Order By:** Default

**Order:** Blank

**Conditions:** Application (All Properties) with application term and application type identified.

Example of fields that can be mapped:

* First Name (user-first-name)
* Last Name (user-last-name)
* Email (user-email-address)
* School ID (user-identities-schoolid)
* Application Term (user-applications-term)
* Application Major (user-applications-major)
* Application Degree (user-applications-degree)
* Application Student Type (user-applications-student-type)
* Application Status (user-applications-status)
* Application Board Stage (user-applications-board-stage)
* Application Board Status (user-applications-board-status)
* Application Last Updated Date (user-applications-updated-at)

## **Example 3: Funnel Report**

**Scenario**: You need to send out a weekly report around the funnel stages to track progression for the upcoming term.

**Repeat fields based on:** User Profile

* First Name (user-first-name)
* Last Name (user-last-name)
* Email (user-email-address)
* School ID (user-identities-schoolid)
* Active Term (user-calculated-active\_term-new)
* Active Major (user-calculated-active\_major)
* Active Student Type (user-calculated-active\_student\_type)
* Created Date (user-milestones-created-date)
* Date Of Inquiry (user-milestones-prospect-date)
* Application Registered At (user-applications-registered-at-\*)
* Application Completed At (user-applications-completed-at-\*)
* Application Submitted At (user-applications-submitted-time-\*)
* Application Board Status (user-applications-board-status-\*)
* Application Released At (user-applications-decision-released-at-\*)
* Deposit Date (user-milestones-deposit-date)
* Enroll Date (user-milestones-enroll-date)
* Withdrawn Date (user-milestones-withdraw-date)

## **Example 4: Test Scores**

**Scenario**: For your student information system integration, you need to extract test scores of admitted students. You would like each row to represent a test.

**Repeat fields based on:** Evaluations

**Items To Export:** All

**Order By:** Default

**Order:** Blank

**Conditions:** Evaluations (All Properties) with specific test types selected. For example, ACT and SAT.

* First Name (user-first-name)
* Last Name (user-last-name)
* Email (user-email-address)
* School ID (user-identities-schoolid)
* Test Date (user-evaluations-date)
* Test Composite Score (user-evaluations-composite-score)
* Test Math Score (user-evaluations-math-score)
* Test Science Score (user-evaluations-science-score)
* Test English Score (user-evaluations-english-score)
* Test Evidence RW Score (user-evaluations-evidence\_rw-score)
* Test Reading Score (user-evaluations-reading-score)

## **Example 5: Sources**

**Scenario**: It is the end of a season and you are wanting to see where your enrolled students from the cycle came from using the sources object on their profiles.

**Repeat fields based on:** Sources

**Items To Export:** First

**Order By:** Sources Timestamp

**Order:** Ascending

**Conditions:** None

* First Name (user-first-name)
* Last Name (user-last-name)
* Email (user-email-address)
* School ID (user-identities-schoolid)
* Sources Name (user-sources-name)
* Sources Source Code Segment (user-sources-segment)
* Sources Timestamp (user-sources-timestamp)

---