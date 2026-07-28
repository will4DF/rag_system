---
title: How Appointments Are Booked
url: https://help.element451.com/en/articles/14658760-how-appointments-are-booked
collection: Appointments
---

Learn how appointments are created in Element451—either by students through the self-service Appointment Site, or by staff manually from within the Appointments module.

# Overview

Appointments in Element451 can be created in three ways. Students and prospective visitors can self-schedule through the public-facing **Appointment Site**, browsing availability and completing a registration form on their own. Staff members can schedule appointments manually on a student's behalf directly from the **Appointments module**. And **Bolt Agents** can guide students through booking as part of an AI-powered conversation.

All three methods result in a scheduled appointment visible in the Appointments module and tied to the student's record. The right method depends on your workflow—self-service booking reduces staff effort and empowers students, manual scheduling gives staff full control, and Bolt Agents enable proactive, automated outreach that drives students to book.

Below, we will cover:

* How students book through the Appointment Site
* How staff manually schedule appointments from within the platform
* How Bolt Agents guide students through booking

---

# Booking via the Appointment Site (Student-Facing)

The Appointment Site is a branded, public-facing scheduling page where students, prospective students, and other visitors can discover and book appointments with staff.

📌 **Note**: The Appointment Site is set up and configured by an admin. If your institution's site isn't live yet, refer to [Appointments Site + Settings](https://help.element451.com/en/articles/11157302-appointments-site-settings) and [Initial Setup for Appointments (Admins)](https://help.element451.com/en/articles/8141376-initial-setup-for-appointments-admins).

## How Students Access the Site

Students can reach the Appointment Site in two ways:

* **Direct URL** — either a default domain (e.g., `yourschool.appointment451.sites.451.io`) or a custom institutional domain (e.g., `appointments.yourschool.edu`)
* **StudentHub Mobile App** — students can browse and book appointments directly within the app

## The Student Booking Flow

Once on the site, students can:

1. Browse available staff (**People**) or departments (**Teams**)
2. Filter by **Category**, **Appointment Type**, location, or duration
3. Select a staff member or team and view real-time availability
4. Choose an available time slot
5. Complete the **registration form** for the selected appointment type
6. Submit to confirm—they'll receive a confirmation message and an email notification (you can also enable an SMS notification)

🧠 **Good to Know**: For team appointments, students select a time slot and the system automatically assigns an available team member based on the team's assignment settings. The student doesn't need to choose an individual.

## The Registration Form

The registration form students see when booking is configured at the **Appointment Type** level by an admin. It uses standard Element451 data fields and collects the information your team needs to prepare for the meeting.

A few things to know about form submissions:

* Information students enter **overwrites** the data on their existing contact record
* The optional **Additional Information** field (which prompts: *"Please share anything that will help us prepare for our appointment"*) is appointment-specific and **does not** update the contact record
* Submitted form responses are visible when a staff member opens the appointment in the module

📙 [Initial Setup for Appointments (Admins)](https://help.element451.com/en/articles/8141376-initial-setup-for-appointments-admins) — learn how to configure the registration form for each appointment type.

---

# Manually Scheduling an Appointment (Staff)

Staff members can schedule an appointment on behalf of a student directly from the Appointments module—no need for the student to use the Appointment Site.

💡 **Use Case**: A student calls your office to schedule a meeting. Rather than directing them to the Appointment Site, a staff member can book the appointment on the spot while on the phone.

## Steps to Manually Schedule

1. Navigate to **Engagement > Appointments**
2. Click **Schedule an Appointment** in the top-right corner of the header
3. The **Appointment Details** form opens. Fill out the fields.
4. Click **Save**. The appointment is now scheduled and visible in the Appointments module.

|  |  |  |
| --- | --- | --- |
| **Field** | **Required** | **Notes** |
| **Person** | Yes | Search and select a student. |
| **Case** | No | Link the appointment to an open [case](https://help.element451.com/en/articles/13764725-getting-started-with-case-management-closed-beta). Note: Case Management is in closed beta and not yet available to all users. |
| **Team** | No | Select a team. Only teams configured in team settings are available. |
| **Assignee** | No | Defaults to the logged-in user. Can be changed if you have the **Administer Appointments** permission. |
| **Availability** | Yes | Select an availability window to populate the Date & Time options. |
| **Status** | Yes | Defaults to **Scheduled.** However, you can change it to another status: Canceled, Not Attended, Attended. This is helpful for adding previous appointments that may not have been in the system. |
| **Date & Time** | Yes | Available slots appear after selecting an availability window. |

---

# Booking via a Bolt Agent

Bolt Agents can guide students through scheduling an appointment as part of an AI-powered conversation. When the **[Schedule Appointments](https://help.element451.com/en/articles/8993380-bolt-agent-skills)** [skill](https://help.element451.com/en/articles/8993380-bolt-agent-skills) is enabled on a Bolt Agent, the agent handles the entire booking flow—presenting available times, applying advisor assignment preferences, and balancing workload across staff—without the student ever needing to visit the Appointment Site.

This is especially effective for proactive outreach: a student receives a message from a Bolt Agent, expresses interest in meeting, and the agent books the appointment on the spot.

## How the Agent Books

When a student agrees to schedule, the agent:

1. Presents available appointment types and times
2. Checks whether the student has an assigned advisor in the available pool
3. If the assigned advisor is available, books with them directly
4. If not, assigns the staff member with the fewest appointments in the next 30 days
5. Confirms the booking—the appointment appears in the Appointments module automatically

📌 **Note**: The **Schedule Appointments** skill must be enabled on the Bolt Agent, and your institution must have Appointments configured with availability set up. Access depends on your Element451 package.

📙 [Bolt Agent Skills](https://help.element451.com/en/articles/8993380-bolt-agent-skills) — learn how to enable and configure skills on a Bolt Agent.

## Using a Bolt Agent Job to Drive Appointment Bookings

Bolt Agent Jobs let you run a Bolt Agent against a list of students at scale. You can use one to proactively reach out to a segment of students and get them to book an appointment—without any manual staff effort.

When creating a Bolt Agent Job to drive appointment bookings, set the **Goal** to **Schedule Appointment** ("Get the contact to book an appointment") and add a **Schedule Appointment** action linked to the appropriate availability. The agent will handle the conversation and book on the student's behalf. You can launch a job directly from **Engagement > Appointments** using the **Create Bolt Agent Job** button.

📙 [Creating a Bolt Agent Job](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job) — step-by-step guide to configuring goals, actions, and enrollment.

---