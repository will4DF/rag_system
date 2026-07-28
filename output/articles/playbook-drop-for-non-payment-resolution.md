---
title: Playbook: Drop for Non-Payment Resolution
url: https://help.element451.com/en/articles/12482903-playbook-drop-for-non-payment-resolution
collection: Workflows + Rules
---

Retain students facing financial challenges by proactively resolving outstanding balances before enrollment drops take effect.

# Overview

Drop for non-payment is one of the most critical—and preventable—points of student attrition. When students carry outstanding account balances due to unpaid tuition, fees, or housing charges, institutions typically drop them from courses after the payment deadlines have passed. This automated process protects institutional revenue but can derail student persistence, especially for those experiencing temporary financial hardship.

Students facing financial challenges often experience significant stress that impacts their well-being and academic performance, yet many are unaware of available resources or payment options until it's too late. Financial aid staff who increase communication with students around important deadlines and create more opportunities for students to access help can significantly improve retention outcomes.

Element451's AI-powered Bolt Agents transform this reactive, policy-driven process into a proactive, student-centered intervention that prioritizes solutions over punishment.

---

# 🏛 Your Current Process

Most institutions handle outstanding student balances through a combination of automated billing notifications and manual follow-up from the business office or financial aid staff—but this approach often catches problems too late.

## Automated Billing Notifications

The student accounts system generates generic payment reminder emails at set intervals (e.g., 30 days before, 2 weeks before, payment deadline).

*Challenge: Generic reminders fail to acknowledge individual circumstances, offer actionable solutions, or create a sense of urgency. Many students ignore them or don't understand the consequences of non-payment.*

## Payment Deadline Passes

Students who haven't paid by the deadline have holds placed on their accounts, preventing registration and access to transcripts.

*Challenge: Unpaid tuition and fees threaten not just cash flow but also student retention, as students may disenroll rather than resolve balances. At this point, the damage to student persistence is already happening.*

## Manual Outreach by Business Office

Business office staff manually email or call students with outstanding balances, typically using a shared inbox or individual follow-up.

*Challenge: Staff capacity limits the number of students who can be contacted personally. Many schools lack the necessary tools or resources to effectively manage past-due receivables. Outreach is inconsistent and often impersonal.*

## Enrollment Drop Occurs

After a grace period (typically 1-2 weeks), students who haven't resolved balances or enrolled in payment plans are automatically dropped from courses.

*Challenge: Once dropped, it's likely that students won't re-enroll.*

## Collections Process Begins

Outstanding balances are sent to collections, transcript holds are placed, and the student's path forward becomes increasingly difficult.

*Challenge: Many colleges reserve the right to withhold transcripts as a debt collection practice, which can prevent students from transferring or continuing their education elsewhere.*

---

# The Element451 Process

Bolt Agent Jobs automate proactive, empathetic outreach to students with outstanding balances—at scale.

Rather than relying on generic billing reminders and staff capacity for manual follow-up, Bolt Agents can reach out to at-risk students early and engage them through personalized, multi-channel conversations that connect them to payment solutions before enrollment drops occur.

Your staff focuses on the students who need staff intervention, while the agent handles routine communication, appointment scheduling, and resource sharing.

## Prerequisites

Before setting up this Bolt Agent Job, ensure you have the following in place:

* **Account hold data synced to Element451:** You must send hold information (hold type, hold reason, balance amount, etc.) to Element451 (via SIS or other method) so you can segment students with outstanding balances.
* **Appointment types configured:** If using the Schedule Appointment action, ensure your financial aid advising appointment type is set up in Element451
* **Staff capacity to monitor:** Designate staff (business office, financial aid, or advising) who will monitor agent conversations and respond to complex cases
* **Clear payment plan policies:** Ensure your payment plan options, emergency aid programs, and financial aid policies are documented and accessible to agents in your Knowledge Hub.
* **Approval workflow established:** Determine who will review and approve agent messages (if Self-Approval is disabled).

## Configure Your Target Segment

Create a calculated segment of students with active account holds due to outstanding balances.

**✨ Pro Tip:** Set up a trigger to automatically enroll students into the job when they develop an outstanding balance after the job starts.

## Create Your Bolt Agent Job (Job Template)

Navigate to **Engagement > Bolt Agents > Jobs** and create a new job. Here are some standard configurations that we recommend; however, you can adjust them to suit your specific needs.

* **Job Name:** Account Balance Resolution – [Term/Year]  
  ​
* **Assigned Agent:** Financial Aid Advisor  
  ​
* **Goal:** Choose the outcome that best fits your process:

  + **Leave Segment** – Student resolves their balance, and the hold is removed
  + **Submit Form** – Student completes payment plan agreement or emergency aid application  
    ​
* **Deadline:** Set to 1-2 weeks before your institution's drop-for-non-payment date  
  ​
* **Action** **Options**: Add the actions your agent will take to help students resolve balances:

  + **Provide Information:** Notify students of their balance and share payment options and resources.
  + **Schedule Appointment:** Connect students with financial aid advisors for individualized support

    - *Scoped to [your appointment type]*​
  + **Promote Form:** Direct to payment plan agreements, financial aid applications, or emergency aid forms

    - *Scoped to [your form]*  
      ​
* **General Instructions**: Copy and customize these instructions for your agent:

  + You are a supportive agent helping students resolve outstanding account balances to maintain enrollment. Use an empathetic, non-judgmental tone.   
    ​  
    Acknowledge that financial challenges are common and focus on solutions. If a student expresses hardship, prioritize connecting them with financial aid resources or payment plan options rather than pushing immediate payment.   
    ​  
    Send two messages per week unless the student replies. Use email and SMS. Call students who reply but have not yet taken action.
* **Action-Specific Instructions:** Tailor how your agent executes each action:

  + **Provide Information:**

    - Lead with empathy: "I'm here to help you explore solutions for your account balance." Establish trust and position the institution as a partner in resolving challenges. Reference the specific amount owed when known. Clearly state that the student has an outstanding balance and specify the payment deadline. Provide direct links to the student portal or billing system. Include specific options for payment plans, emergency aid, or financial aid support. Limit proactive information messages to one per week unless the student responds.
  + **Schedule Appointment:**

    - Direct students to meet with a financial aid advisor (scoped to [your appointment type]). Emphasize that appointments are meant to find solutions, not to demand immediate payment. Highlight confidentiality and support.
  + **Promote Form:**

    - Direct students to the appropriate form (scoped to [your form]), such as payment plan agreements, financial aid applications, or emergency aid requests. Provide a brief explanation of why completing the form is important.  
      ​
* **Self-Approval Settings**: Keep Self-Approval **OFF** for initial outreach.

  + You may also consider keeping it enabled beyond initial outreach for additional review (until you're comfortable enabling it), as it is a sensitive topic.

## Launch the Bolt Agent Job + Monitor

* Start the job and monitor the Summary Bar for real-time performance
* Review messages needing approval
* Track goal completion rates and adjust instructions or actions as needed

## Bolt Jobs Creator Agent Prompt

Below is an example of a prompt you could give your Bolt Jobs Creator Agent (Staff Agent) to create this job for you. Be sure to read through and update/personalize the information before submitting the prompt.

```
Create a job to help students resolve outstanding account balances before enrollment drops.  
  
Job Name: Account Balance Resolution – [Insert Term/Year]    
Assigned Agent: Financial Aid Advisor    
Goal: [Choose: Leave Segment "Outstanding Balance" OR Join Segment "Account Current" OR Submit Form (for payment plans/aid applications)]      
Deadline: [Insert deadline if applicable]    
Enrollment Limit: [Insert enrollment limit if applicable]    
  
Actions: Make Introduction, Provide Information, Schedule Appointment, Promote Form    
(Note: Keep only the actions you plan to use for this job. Remove any that don’t apply.)    
  
General Instructions: You are a supportive agent helping students resolve outstanding account balances to maintain enrollment. Use an empathetic, non-judgmental tone. Limit proactive outreach to one message per week unless the student replies. Use email and SMS for details, reminders, and phone calling for when student replies but has not yet completed the goal.    
  
Action Instructions:    
- Make Introduction: Lead with empathy and position yourself as a resource.    
- Provide Information: Inform students of their outstanding balance. Share direct links to their student portal and highlight payment plan and financial aid resources.    
- Schedule Appointment: Direct students to book a financial aid advising appointment [Insert Appointment Type]. Emphasize the goal is finding solutions.    
- Promote Form: Direct students to [Insert Payment Plan/Financial Aid Form]. Explain why completing it is critical to maintaining enrollment.
```

---

# Best Practices + E451 Recommendations

## Communication Strategy

### Early + Empathetic Outreach

Institutions should identify students with outstanding balances early and take steps to intervene before financial challenges force them to drop out. Begin outreach 3-4 weeks before the drop deadline, not just days before.

A simple, timely, empathetic message can make the difference between a student feeling supported or alienated. Instruct the agent to lead with understanding, not blame:

* "I'm reaching out because I want to help you stay enrolled..."
* "I know financial challenges can happen to anyone..."
* "Let's work together to find a solution that works for you..."

### Multi-Channel, Multi-Touch Approach

* The agent should use a variety of channels:

  + **Email:** Best for detailed information (balance breakdown, payment options, links to forms)
  + **SMS:** Best for urgent reminders, quick links to scheduling, and brief check-ins
  + **Phone:** Best for students who have engaged but not completed the goal, or students expressing confusion/distress
* The agent should also increase communication with students regarding important deadlines. Example cadence:

  + Week 1: Email initial outreach + balance notification
  + Week 2: SMS reminder with payment plan option
  + Week 3: Email with appointment scheduling link
  + Week 4: Phone call for students who have engaged but not resolved

### Transparent Information Sharing

Information about balances, fees, terms, processes, payment plans, and other relevant details is often scattered across multiple systems and communications, making it difficult for students to understand their financial situation. Ensure your agent has access to these details on the student's record or within your Knowledge Hub:

* Clear payment deadline with consequences explicitly stated
* Direct links to the student portal/billing system
* All available options (payment plans, emergency aid, financial aid adjustments)
* Account hold details (balance, etc.) or where to find them

### Adapt Tone Based on Engagement

* **No response:** Maintain encouraging, resource-focused tone
* **Engaged but struggling:** Shift to problem-solving mode, offer an appointment
* **Expressed hardship:** Immediately connect to emergency aid and financial aid counseling

## Audience Segmentation

### Prioritize High-Risk Students

Students with the highest unmet need are less likely to persist than those with lower balances. Segment your population to prioritize:

* Students with balances > $1,000
* First-generation students
* Pell Grant recipients
* Students who have used payment plans previously
* Students with multiple holds on their account

### Tailor Messaging by Student Profile

* **First-generation students:** Use encouraging, supportive language that acknowledges their pioneering role. Emphasize support services and family-friendly messaging.
* **Pell Grant recipients:** Reference emergency aid programs and flexible payment options explicitly.
* **International students:** Provide additional context about U.S. billing practices and emphasize confidential support.
* **Students with prior payment plan use:** Acknowledge previous successful resolution and offer streamlined re-enrollment.

##

---