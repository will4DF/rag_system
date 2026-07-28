---
title: Playbook: Priority Registration Push
url: https://help.element451.com/en/articles/12500696-playbook-priority-registration-push
collection: Workflows + Rules
---

Maximize registration rates and ensure students secure their course schedules before seats fill up.

# Overview

Course registration is a critical milestone in the student lifecycle, yet many students miss their registration windows, delay scheduling advising appointments, or fail to complete pre-registration requirements. This leads to closed courses, scheduling conflicts, extended time-to-degree, and—in the worst cases—stopouts.

Traditional registration communication relies on mass emails sent to all eligible students, regardless of their individual readiness or barriers. These generic reminders often fail to account for students who require advising appointments, have unresolved holds, or simply don't understand the registration process. By the time staff identify students who haven't registered, priority time slots have passed, and course options have dwindled.

Bolt Agent Jobs automates personalized, proactive outreach that meets students where they are—guiding them through pre-registration requirements, connecting them to advising support, and creating urgency around registration deadlines based on their individual priority window.

---

# 🏛 Your Current Process

Most institutions handle course registration through a combination of mass email campaigns and reactive advising support—but this approach leaves too many students behind.

## Mass Email Announcements

The Registrar's Office or Advising sends campus-wide emails announcing registration dates, typically two to four weeks prior to registration opening.

*Challenge: Mass emails often fail to account for individual registration windows, advising holds, or prerequisite requirements. Students ignore generic announcements or assume the information doesn't apply to them yet.*

## Registration Portal Opens

Students with the earliest registration windows (typically seniors, honors students, athletes) register first, followed by subsequent priority groups on staggered dates.

*Challenge: Many students are unaware of their specific registration date and time. Those who miss their window face limited course availability and scheduling conflicts.*

## Reactive Advising Support

Students who need advising appointments must proactively reach out to schedule. Advisors respond to inquiries as they come in, often getting overwhelmed as registration deadlines approach.

*Challenge: Advising bottlenecks occur right before registration. Students who need guidance the most—those who are first-generation, exploratory majors, or on academic probation—are least likely to proactively seek it.*

## Registration Holds + Barriers

Students discover registration holds (advising, financial, academic) only when they attempt to register. They must then resolve holds before proceeding, often missing their priority window.

*Challenge: Students don't learn about holds until it's too late. Resolving holds takes time, pushing registration into less favorable windows when courses are full.*

## Late Registrants + Non-Registrants

Weeks after registration opens, a significant portion of students still haven't registered. Staff manually pull lists and send follow-up emails or make phone calls.

*Challenge: Scaling manual outreach is impossible. Staff can only reach a fraction of non-registrants, and by this point, course options are severely limited.*

## Closed Courses + Schedule Conflicts

Students who register late often face closed courses, unfavorable time slots, and scheduling conflicts that can delay their degree progress.

*Challenge: Poor registration outcomes compound over time, extending the time-to-degree and increasing the risk of dropout.*

---

# The Element451 Process

Bolt Agent Jobs automate personalized registration outreach, reaching every student at the right time with the right information—whether that's their specific registration date, a reminder to schedule advising, or a nudge to resolve a hold. Rather than relying on mass emails and reactive support, your advising team can focus on complex cases while the agent handles routine communication, appointment scheduling, and registration reminders at scale.

## Pre-Requisites

Before setting up this Bolt Agent Job, ensure you have the following in place:

* **Registration status synced to Element451:** Send the registration status (registered/not registered) for the target term to Element451, allowing you to segment students accordingly.
* **Registration windows and process:** Registration windows, priority groups, and registration processes should be accessible to your agent.
* **Target segment configured:** Create a segment for eligible students who haven't yet registered for the target term.
* **Appointment types configured:** Ensure your academic advising appointment types are set up in Element451.
* **Advising capacity:** Ensure your advising team has the capacity to handle increased appointment requests.
* **Clear registration policies:** Document registration dates, priority windows, holds policies, and course selection guidelines.
* **Registration resources available:** Course catalogs, degree audits, and schedule planning tools should be accessible to students.

## Configure Your Target Segment

Create a segment of students who are eligible to register but haven't yet done so.

Your segment criteria might include:

* **Enrolled Status:** Active/enrolled students
* **Term:** Target term (e.g., Spring 2026)
* **Registration Status:** NOT registered for the target term
* **Exclusions:** Students with financial holds that prevent registration entirely (focus on those who CAN register but haven't)

**✨ Pro Tip:** Create multiple segments by priority group or registration window to personalize outreach timing. Students with earlier windows should receive earlier communication. Or, instruct the agent to schedule outreach based on this information.

## Create Your Bolt Agent Job

Navigate to **Engagement > Bolt Agents > Jobs** and create a new job.

* **Job Name:** Priority Registration Push – [Term + Year]
* **Assigned Agent:** Academic Advisor
* **Goal:** Join Segment (students who successfully register for the term)
* **Action Options:**

  + **Provide Information**: The agent shares registration dates, priority windows, important deadlines, and links to resources (course catalog, degree audit, registration portal).
  + **Schedule Appointment**: Direct students to schedule advising appointments to discuss course selection, degree planning, or resolve advising holds. Scope to your academic advising appointment type.
* **General Instructions:** Copy and customize these instructions for your agent:

  + You are an enthusiastic academic advisor helping students register for classes on time.
  + Use an encouraging and supportive tone that creates a sense of urgency without feeling pressured.
  + Reference the student's specific registration date/window when known. If they have an advising hold, prioritize directing them to schedule an appointment before their registration window opens.
  + Send two messages per week unless the student replies.
  + Use email for detailed information (registration dates, course planning resources, degree requirements). Use SMS for urgent reminders about approaching registration windows.
  + Call students who engage but haven't registered or scheduled an appointment by one week before their priority window closes.
* **Action-Specific Instructions:**

  + **Provide Information:** Share the student's specific registration date and time if available. If not available, please share their priority group and the date registration opens for that group. Include direct links to the registration portal, course catalog, and degree audit tool. Highlight any pre-registration requirements (advising appointments, hold clearance, etc.). Create urgency around approaching deadlines: "Your registration window opens in 3 days" or "Priority registration ends soon—popular courses are filling up fast." For students with advising holds, clearly explain that they must schedule an advising appointment before they can register.
  + **Schedule Appointment:** Direct students to schedule an advising appointment (scoped to [your appointment type]) if they:

    - Have an advising hold preventing registration
    - Are undecided about course selection
    - Haven't met with an advisor this term
    - Are exploring majors or degree pathways
  + Emphasize that advising appointments help them choose the right courses, stay on track to graduate, and avoid common registration mistakes.
  + For students with approaching registration windows, note appointment availability and encourage booking ASAP.
* **Self-Approval Settings:**

  + **Recommendation:** You can enable Self-Approval **ON** for this job after initial testing, as registration communication is typically less sensitive than financial topics. However, review the first 20-30 messages to ensure tone and accuracy before enabling.

## Launch the Bolt Agent Job + Monitor

* **Start the job** and monitor insights for performance
* **Track appointment scheduling rates** to ensure advising capacity isn't overwhelmed
* **Monitor registration completions** to see which students are registering after agent contact
* **Adjust instructions** based on what's working (e.g., if SMS reminders drive more action, increase SMS frequency)

## Bolt Jobs Creator Agent Prompt

Use this prompt with your Bolt Jobs Creator Agent (Staff Agent) to quickly generate this job.

**Be sure to read through and update/personalize the information before submitting:**

```
Create a job to help students register for classes on time.    
Job Name: Priority Registration Push – [Insert Term + Year]     
Assigned Agent: Academic Advisor     
Goal: Join Segment  
Deadline: [Insert deadline]     
Enrollment Limit: [Insert limit]      
Actions: Provide Information, Schedule Appointment      
General Instructions: You are an enthusiastic academic advisor helping students register for classes on time. Use an encouraging, supportive tone that creates urgency without pressure. Reference the student's specific registration date/window when known. If they have an advising hold, prioritize directing them to schedule an appointment before their registration window opens. Send two messages per week unless the student replies. Use email for detailed information and SMS for urgent reminders.    
Action Instructions:     
- Provide Information: Share the student's specific registration date/time or priority group. Include direct links to registration portal, course catalog, and degree audit. Highlight pre-registration requirements. Create urgency around approaching deadlines.     
- Schedule Appointment: Direct students to schedule an advising appointment [Insert Appointment Type] if they have advising holds, are undecided about courses, or haven't met with an advisor this term. Emphasize that appointments help them choose the right courses and stay on track.
```

---

# Best Practices + E451 Recommendations

## Communication Strategy

### Tiered Timing Based on Priority Windows

Don't send the same message to all students at once. Segment by registration priority group and time outreach accordingly, or add these specifics to your job instructions.

* **3 weeks before their window:** Initial awareness message
* **1 week before their window:** Reminder with specific date/time
* **2 days before their window:** Urgent SMS reminder
* **Day after their window opens:** Follow-up for non-registrants

### Create Urgency Without Pressure

Registration communication should motivate action without creating anxiety. Instruct the agent to:

* Emphasize benefits: "Get the classes you need" and "Create your ideal schedule"
* Highlight scarcity: "Popular courses fill up fast" and "Seats are limited"
* Avoid guilt or blame: Never imply students are "behind" or "late"

### Multi-Channel Approach

The agent should use a variety of channels:

* **Email:** Best for detailed information (registration dates, course planning resources, step-by-step instructions)
* **SMS:** Best for urgent reminders ("Your registration window opens tomorrow at 8 AM!")
* **Phone:** Best for students with advising holds who haven't scheduled appointments, or students who haven't registered one week after their priority window

### **Clear, Actionable Information**

Students need to know exactly what to do next. Ensure your agent provides:

* Specific registration date and time (not just "your priority group")
* Direct link to registration portal (not just "check your student portal")
* Explicit next steps: "Schedule an advising appointment" or "Clear your advising hold before [date]"
* Pre-registration checklist if applicable

### Adapt Tone Based on Engagement

* **No response:** Maintain encouraging, excited tone about registration
* **Engaged but hasn't registered:** Shift to problem-solving—ask if they need help or have questions
* **Has advising hold:** Prioritize appointment scheduling with clear explanation of why it's required
* **Registered successfully:** Celebrate and confirm their schedule (optional follow-up)

## Audience Segmentation

### Prioritize High-Risk Groups

Some students are more likely to miss registration deadlines or need additional support:

* First-year students (unfamiliar with the process)
* Students with less than 30 completed credits
* Students on academic probation (often have advising holds)
* Students who registered late in previous terms
* Exploratory/undecided majors

### Tailor Messaging by Student

* **First-year students:** Provide extra context about how registration works, what priority windows mean, and how to read a course schedule
* **Students with advising holds:** Lead with appointment scheduling, not registration reminders
* **Transfer students:** Acknowledge their prior experience but highlight institution-specific processes
* **Seniors:** Emphasize degree completion and graduation readiness
* **Athletes/honors students:** Recognize their early registration window as a benefit

---