---
title: Getting Started with Bolt Student Agent Plugins [Closed Beta]
url: https://help.element451.com/en/articles/11750044-getting-started-with-bolt-student-agent-plugins-closed-beta
collection: Bolt AI
---

Allows Bolt Agents to pull data in real-time from the SIS to answer student questions.

[![Features mentioned in this article are currently in closed beta, not yet available to all users. Stay tuned for a wider release.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613482258/112d79a3166437dcc672ac486511/Closed+Beta.png?expires=1784333700&signature=706997a9dde650472bc4365bfcb44e00bc08e3793f089aa7ecb54664ad0724d3&req=dSYmFc12n4NaUfMW1HO4zcYKuaeQ7N9%2FLVKURMQT4nJQIG4YfJ5eIo%2FivqDh%0AEPLJCKY94LHY6UMvWoY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613482258/112d79a3166437dcc672ac486511/Closed+Beta.png?expires=1784333700&signature=706997a9dde650472bc4365bfcb44e00bc08e3793f089aa7ecb54664ad0724d3&req=dSYmFc12n4NaUfMW1HO4zcYKuaeQ7N9%2FLVKURMQT4nJQIG4YfJ5eIo%2FivqDh%0AEPLJCKY94LHY6UMvWoY%3D%0A)

# Overview

Bolt Plugins extend the capabilities of Bolt Agents by enabling direct, real-time access to your Student Information System (SIS) or Learning Management System (LMS). This means agents can respond to students with live information about their academic records, registration, financial aid, and more, without storing any SIS data inside Element451.

This is especially valuable when information in Element451 hasn’t yet been updated from your SIS. With a plugin, agents fetch data directly from the source during a conversation, ensuring students receive the most current information available.

## Supported Platforms via Ethos

Currently, we support Banner and Colleague through Ethos. This feature is in closed beta and is not yet available to all users. The Plugin framework is designed to grow with more integrations and data points becoming available over time.

---

# How Plugins Work

When a Bolt Plugin is connected, the agent communicates securely with your SIS or LMS to pull data for the **authenticated** student.

## Data Access

* Every data request is scoped to the authenticated student engaged in the conversation.
* Plugins only **retrieve** data in real time.
* No SIS information is stored or written back to Element451.
* This mirrors the process a staff member would follow if they manually checked SIS records and replied to the student.

## Channel Support

* Available for **live chat** and **email** conversations.
* Not currently supported for SMS or WhatsApp conversations.

## Authentication Process

* **Live Chat:** Student authenticates using their school email during the chat.
* **Email:** Automatically authenticated based on the email address of the sender.
* If a matching SIS record is not found, or if multiple matches exist, the agent will not return any data.

---

# Permissions Required

To enable a plugin, your SIS administrator must provide an **API key** with the following permissions.

📌 **Note**: All permissions must be granted for the plugin to work. Partial access will prevent the agent from retrieving student information.

```
/api/student-advisor-relationships    
/api/student-academic-programs    
/api/student-academic-programs/${studentAcademicProgramId}    
/api/student-financial-aid-awards    
/api/student-academic-credentials    
/api/student-unverified-grades    
/api/section-instructors    
/api/section-registrations/${sectionRegistrationId}    
/api/sections/${sectionId}    
/api/sites/${siteId}    
/api/persons    
/api/persons/${personId}    
/api/person-holds    
/api/person-hold-types/${holdTypeId}    
/api/addresses/${addressId}    
/api/academic-programs/${academicProgramId}    
/api/academic-periods/${academicPeriodId}    
/api/academic-credentials/${credentialId}    
/api/academic-levels/${academicLevelId}    
/api/academic-disciplines/${disciplineId}    
/api/admission-applications    
/api/admission-decisions    
/api/admission-decision-types/${admissionDecisionTypeId}    
/api/grade-definitions/${gradeDefinitionId}    
/api/courses/${courseId}
```

---

# Supported Student Questions

With a plugin connected, Bolt Agents can answer a variety of real-time questions. Below are examples grouped by category:

## Academic advisor

* “Who is my advisor?”
* “What academic advisors are assigned to me?”
* “Can you provide details about my advisor?”

## Admissions

* “What’s the status of my admissions application?”
* “What application decisions have been made?”
* “Which programs have I applied to?”

## Financial aid

* “How much financial aid do I have?”
* “What are my financial aid awards?”

## Graduation

* “What is my graduation status?”
* “Is my graduation date set?”

## Holds

* “Do I have any holds on my account?”
* “What’s the status of my account holds?”

## Major/minor programs

* “What’s my declared major or minor?”
* “What program am I enrolled in?”
* “What’s my expected graduation date?”

## Grades

* “What are my grades for this term?”

## Personal information

* “What address, phone number, or email do you have on file for me?”
* “What is my student ID or username?”

## Class schedule

* “What classes am I registered for?”
* “Who are my instructors?”
* “Where are my classes located?”
* “What are the course details for my current term?”
* “How many credits am I registered for?”

## Education history

* “What’s my transcript history or status?”
* “What’s my attendance history from other institutions?”

---

# Accessing Bolt Plugins

1. Navigate to **Engagement** > **Bolt** **Agents**.
2. Select Plugins from the left-hand menu.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649125145/7bd1efb4f12cdb49b27cf01217f5/BoltPlugins+%281%29.png?expires=1784333700&signature=2bd8d4c59a37e9ad857e934e6412db7cdf1f1ece9425fe8d973f9991cbe6e41a&req=dSYjH8h8mIBbXPMW1HO4za5HMyQdgG%2FcxlZ1JxZaRflZGMtnqipvrzzYKESW%0A1%2Bgr%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649125145/7bd1efb4f12cdb49b27cf01217f5/BoltPlugins+%281%29.png?expires=1784333700&signature=2bd8d4c59a37e9ad857e934e6412db7cdf1f1ece9425fe8d973f9991cbe6e41a&req=dSYjH8h8mIBbXPMW1HO4za5HMyQdgG%2FcxlZ1JxZaRflZGMtnqipvrzzYKESW%0A1%2Bgr%0A)

---

# Adding a Bolt Plugin

1. Navigate to **Engagement** > **Bolt** **Agents**.
2. Select Plugins from the left-hand menu.
3. Click the "**+ Add Bolt Plugin**" button.
4. Select the system you wish to integrate—either Banner or Colleague.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613500603/8540396f0c50bc5bf7dc7d4e6670/CleanShot+2025-07-10+at+12_06_53%402x.png?expires=1784333700&signature=674dcf9e984ef0f7de26336d143c46c9b01f90db3ca62fe39a783bb45ca75a79&req=dSYmFcx%2BnYdfWvMW1HO4zb404AFOzW5YyYpDradlg%2BWLOwZuZ3yXmm3OTTeq%0AnvCz%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613500603/8540396f0c50bc5bf7dc7d4e6670/CleanShot+2025-07-10+at+12_06_53%402x.png?expires=1784333700&signature=674dcf9e984ef0f7de26336d143c46c9b01f90db3ca62fe39a783bb45ca75a79&req=dSYmFcx%2BnYdfWvMW1HO4zb404AFOzW5YyYpDradlg%2BWLOwZuZ3yXmm3OTTeq%0AnvCz%0A)
5. Enter your **API key** in the "Add Plugin" side sheet.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613503410/5dbd7acc127b7304024215fe18c7/CleanShot+2025-07-10+at+12_08_38%402x.png?expires=1784333700&signature=5304ee6454173630f911c54aed27914e202c6e569dc3119d23744e6b02bcca46&req=dSYmFcx%2BnoVeWfMW1HO4zWeqYvl8aRtu2c47r8BDROqV4uYixDbv6wzNXa7d%0A5wsm%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613503410/5dbd7acc127b7304024215fe18c7/CleanShot+2025-07-10+at+12_08_38%402x.png?expires=1784333700&signature=5304ee6454173630f911c54aed27914e202c6e569dc3119d23744e6b02bcca46&req=dSYmFcx%2BnoVeWfMW1HO4zWeqYvl8aRtu2c47r8BDROqV4uYixDbv6wzNXa7d%0A5wsm%0A)
6. Test your plugin using the "**Test**" button.
7. When finished, click "**Create**."

---