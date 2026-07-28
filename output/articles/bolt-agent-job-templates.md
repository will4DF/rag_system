---
title: Bolt Agent Job Templates
url: https://help.element451.com/en/articles/12270426-bolt-agent-job-templates
collection: Bolt AI
---

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1723486932/d8ca0814bfd4d0e28ced5c0468c0/Pardon+our+Progress.png?expires=1784333700&signature=e29542e0ba4e75ec38ff497b1f79283f3e7d748ccf8736732b4c206367a70201&req=dSclFc12m4hcW%2FMW1HO4zUerAnhJoIKhJHKUSZP135elWBguZXwIixpSo1Kd%0ALGTAhK4wSTVzOBKBo5E%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1723486932/d8ca0814bfd4d0e28ced5c0468c0/Pardon+our+Progress.png?expires=1784333700&signature=e29542e0ba4e75ec38ff497b1f79283f3e7d748ccf8736732b4c206367a70201&req=dSclFc12m4hcW%2FMW1HO4zUerAnhJoIKhJHKUSZP135elWBguZXwIixpSo1Kd%0ALGTAhK4wSTVzOBKBo5E%3D%0A)

# Overview

This article provides ready-made templates—like recipes—for creating Bolt Agent Jobs that align with specific seasons/terms.

The templates below are organized by fall, spring, summer, winter, and year-round tasks. Each template includes the essential components for building the Bolt Agent Job, along with a prewritten prompt that you can personalize and provide to your Bolt Jobs Creator Agent to generate it.

For detailed strategy, best practices, and advanced tips on these use cases, see our **[Bolt Agent Playbooks](https://help.element451.com/en/collections/14520267-playbooks)**.

---

# Fall (August - December)

## 01 - Senior Search Conversion

Convert purchased high school senior lists into inquiries during their critical final year of college decision-making. Transform generic batch outreach into personalized, one-to-one conversations delivered within minutes of uploading your list.

[Read the Playbook ›](https://help.element451.com/en/articles/12089264-playbook-senior-search)

## 02 - High School Visit Outreach

Maximize attendance and value from high school visits by promoting the recruiter’s presence on campus, encouraging student participation, and providing application support for current applicants..

[Read the Playbook ›](https://help.element451.com/en/articles/12294526-playbook-conduct-a-high-school-visit)

## 03 - Promote Fall Open House/Preview Day Event

Drive maximum attendance and engagement for open house or preview day events by targeting prospects at different stages of the enrollment funnel with personalized invitations and compelling reasons to attend.

[Read the Playbook ›](https://help.element451.com/en/articles/12294387-playbook-promote-open-house-preview-day)

---

# Winter (December - January)

*Coming soon!*

---

# Spring (January - May)

*Coming soon!*

---

# Summer (May - July)

*Coming soon!*

---

# Year-Round

## 01 - Application Start Acknowledgment

Celebrate students who have just started an application and offer support as they continue through the process.

## Goal Options

* **Inform or Notify**

## Action Options

We recommend starting with 1–3 actions. You may add more if your use case requires it:

* **Provide Information**  
  Acknowledge the milestone, share encouragement, and point to resources.
* **Schedule Appointment**  
  Optionally allow students to connect with an admissions counselor *(scoped to [your appointment type]).*

## Assigned Agent

* **Recommended:** Admission Advisor

## Target Segment

Students who have started an Application.

## Triggers

* **Application Started:** Enroll students immediately after they begin an application.

## General Instructions

You are a supportive admissions assistant acknowledging that the student has started their application. Use a positive, celebratory tone that acknowledges this as a significant milestone. Emphasize that you’re available to help at any point in the process.

* Send an **immediate acknowledgment message** via Email + SMS.

## Action-Specific Instructions

* **Provide Information**  
  Congratulate the student on starting their application. Encourage them to keep going and share resources like FAQs, timelines, or application guides. Example: *“Congratulations—you’ve started your application! That’s a huge step. If you need help at any point, I’m here.”*
* **Schedule Appointment**  
  Offer a chance to meet with an admissions counselor *(scoped to [your appointment type])*. Position is an optional extra support, not required.

##

## Bolt Jobs Agent Prompt

```
Create a job to acknowledge when a student starts an application.   
  
Job Name: Application Start Acknowledgment – [Insert Term/Year]   
  
Assigned Agent: Admission Advisor Goal: Inform or Notify Target   
  
Deadline: [Insert deadline if applicable]   
  
Enrollment Limit: [Insert enrollment limit if applicable]   
  
Actions: Provide Information, Schedule Appointment   
(Note: Keep only the actions you plan to use for this job. Remove any that don’t apply.)   
  
General Instructions: You are a supportive admissions assistant acknowledging that the student has started their application. Use a positive, celebratory tone. Send an immediate acknowledgment via Email and SMS.  
  
Action Instructions:   
- Provide Information: Congratulate the student and encourage them to continue. Share resources like FAQs, deadlines, or application guides.   
  
- Schedule Appointment: Offer an optional meeting with an admissions counselor [Insert Appointment Type] for additional support.
```

##

## 02 - Application Abandonment Follow-Up

Encourage students who started an application but haven’t submitted it to complete and move forward.

## Goal Options

* **Submit Application**

## Action Options

We recommend starting with 1–3 actions. You may add more if your use case requires it:

* **Promote Application**  
  Provide a direct link to pick up where they left off *(scoped to [your application site]).*  
  ​
* **Provide Information**  
  Offer tips, FAQs, and reminders to overcome barriers.  
  ​
* **Schedule Appointment**  
  Allow students to connect with an admissions counselor if stuck.

  + *Scoped to [your appointment type])*

## Assigned Agent

* **Recommended:** Admission Advisor

## Target Segment

Students who started an application at least 24–48 hours ago and have not submitted it.

## Triggers

* Use a calculated segment for applications started at least 24–48 hours ago with no submission, then enroll that segment or use a Joined Segment trigger. Do not use Application Started by itself for this template; that trigger enrolls the contact immediately.

## General Instructions

You are a supportive admissions assistant, encouraging students to complete their applications. Use a barrier-removing, encouraging tone that acknowledges the progress they’ve made and offers to help if they’re stuck.

## Action-Specific Instructions

* **Promote Application**  
  You are communicating with students who have already started the application process. Provide a direct link back to their application *(scoped to [your application site]).* Example: *“We noticed you started your application—great work! You can pick up where you left off anytime.”*

* **Provide Information**  
  Share resources to overcome common barriers (deadline reminders, how to upload documents, technical FAQs). Keep tone supportive, not pushy.

* **Schedule Appointment**  
  Offer a meeting with an admissions counselor *(scoped to [your appointment type])*. Position as optional help if they’re stuck or unsure how to continue.

## Bolt Jobs Agent Prompt

```
Create a job to help students complete applications they’ve started but not submitted.   
  
Job Name: Application Abandonment Follow-Up – [Insert Term/Year]  
Assigned Agent: Admission Advisor Goal: Submit Application Target  
Enrollment Limit: [Insert enrollment limit if applicable]   
  
Actions: Promote Application, Provide Information, Schedule Appointment   
(Note: Keep only the actions you plan to use for this job. Remove any that don’t apply.)   
  
General Instructions: You are a supportive admissions assistant encouraging students to complete their application. Use an encouraging, barrier-removing tone.  
  
Action Instructions:   
- You are communicating with students who have already started the application process. Provide a direct link back to their application. [Insert Application Site].   
  
- Provide Information: Share resources like deadlines, tips, or FAQs to help them finish.   
  
- Schedule Appointment: Offer a meeting with an admissions counselor [Insert Appointment Type] if they need help.
```

##

## 03 - RFI Form Follow-Up

Acknowledge and nurture prospective students immediately after they submit an RFI or inquiry form, providing timely, personalized value to keep their interest high.

### Goal Options

* Inform or Notify

### Action Options

We recommend starting with 1–3 actions. You may add more if your use case requires it:

* **Make Introduction**  
  Acknowledge their interest and welcome them warmly.  
  ​
* **Provide Information**  
  Share institutional/program details tailored to their form submission.  
  ​
* **Promote Event**

  Suggest campus tours, virtual sessions, or open houses *(scoped to [your event]).*  
  ​
* **Schedule Appointment**

  Offer a 1:1 with admissions *(scoped to [your appointment type]).*

### Assigned Agent

* Recommended: Admission Advisor

### Target Segment

* This job is designed to be trigger-based (see the next setting), engaging students immediately upon submission of a form. However, you can upload a segment of students if you choose.

### Trigger

* Form Submitted (RFI): Enroll any new prospects completing the inquiry form.

### General Instructions

You are a friendly admissions representative reaching out the moment a student submits an RFI form. Use a supportive, encouraging tone that reinforces their decision to inquire and provides immediate value. Reference their intended program or interest, if available from the form submission.

* Send an instant acknowledgment via email + SMS at the moment of enrollment.
* Follow up with up to 2–3 proactive touches over 7–10 days if no reply.
* Reference the intended program they selected (alumni stories, outcomes, highlights).
* Tailor messaging by student type (first-year, transfer, adult learner, international).
* Adjust based on geography (local = convenience; regional/national = destination).

### Action-Specific Instructions

* **Make Introduction**

  Thank them for submitting the form and welcome them. Reference their selected program if available. Example: *“Thanks for letting us know you’re interested in [Insert Program] — we’re excited to help you explore what makes [Institution] unique.”*  
  ​
* **Provide Information**

  Share relevant knowledge-base content about their program, outcomes, and campus life. Include differentiators that set your institution apart.  
  ​
* **Promote Event**

  Invite them to an upcoming tour, info session, or open house *(scoped to [your event]).* Frame as a natural next step to learn more.  
  ​
* **Schedule Appointment**

  Offer a 1:1 admissions appointment *(scoped to [your appointment type]).* Position as optional extra support if they want a deeper conversation.

### Approval Guidance

* **Recommendation:** Keep Self-Approval **ON**, as this job is intended to have the Agent immediately reach out to the student upon form submission.

### Bolt Jobs Agent Prompt

```
Create a job to engage students immediately after they complete an RFI form on our website.  
  
Job Name: RFI Form Follow-Up – [Insert Campaign / Term / Year]    
Assigned Agent: Admission Advisor    
Goal: Inform or Notify    
Enrollment Limit: [Insert enrollment limit if applicable]    
  
Actions: Make Introduction, Provide Information, Promote Event, Schedule Appointment    
(Note: Keep only the actions you plan to use for this job. Remove any that don’t apply.)    
  
General Instructions: You are a friendly admissions representative reaching out the moment a student submits an RFI form. Use an encouraging tone, acknowledge their interest, and personalize based on their form responses (program of interest, student type, geography). Send an immediate acknowledgment via email and SMS. Limit to 2–3 proactive touches over 7–10 days if no reply.    
  
Action Instructions:    
- Make Introduction: Thank them for submitting the form and reference their program of interest if available.    
- Provide Information: Share details about their program, alumni outcomes, and support resources.    
- Promote Event: Invite them to an upcoming open house, tour, or info session [Insert Event].    
- Schedule Appointment: Offer a meeting with an admissions counselor [Insert Appointment Type] for personalized support.
```

##

##

##

---