---
title: 📌 Appointments: Frequently Asked Questions
url: https://help.element451.com/en/articles/8834280-appointments-frequently-asked-questions
collection: Appointments
---

This article answers commonly asked questions about Appointments, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389384164/2e982a74a8cfc0685cf7539cd656/Pardon+our+Progress.png?expires=1784333700&signature=6624c34a93a47df0320673f0e101047a4d6fef90ca550848af7bcad61b97f239&req=dSMvH8p2mYBZXfMW1HO4zWxDevotN4monpV3SmQXdboS5%2FraC2MAP2SItHXV%0AyWNwvoCTMKLJ3Ne%2FPGM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389384164/2e982a74a8cfc0685cf7539cd656/Pardon+our+Progress.png?expires=1784333700&signature=6624c34a93a47df0320673f0e101047a4d6fef90ca550848af7bcad61b97f239&req=dSMvH8p2mYBZXfMW1HO4zWxDevotN4monpV3SmQXdboS5%2FraC2MAP2SItHXV%0AyWNwvoCTMKLJ3Ne%2FPGM%3D%0A)

# General

## Why should I use Appointments vs another tool?

By utilizing the Appointments module, you can capture even more important student data. This means that when students schedule appointments, it becomes part of their record in Element451. By leveraging data from appointment scheduling and other student interactions, you can gain insights and engagement scores to track their progress. This holistic view of the student's activities helps you understand their overall experience and provide better support.

## Can you provide proof that Element451 is an approved Microsoft app?

**Yes.** The Element451 Appointments application is published by ELEMENT451 INC., a **Microsoft Verified Publisher**. Microsoft’s Verified Publisher program validates the publisher’s identity and ownership before the application can display the verified publisher designation within Microsoft Entra ID consent and authentication workflows.

Element451’s Outlook Calendar integration is a **private, tenant-level Microsoft Entra ID application** and does not require Microsoft AppSource marketplace listing or public application approval to operate.

Instead, it follows Microsoft’s recommended security model for private Microsoft Entra ID applications and requires a **one-time administrator consent** from your organization’s Microsoft 365 or Entra ID administrator before the application can access Microsoft Graph resources.

Element451 requests a minimal set of Microsoft Graph permissions required to support calendar synchronization and appointment scheduling:

`Calendars.ReadWrite`: Used to check calendar availability and create or update appointments.

`offline_access:` Maintains a secure connection without requiring users to repeatedly authenticate.

`User.Read`: Used to verify identity and retrieve basic profile information.

⚠️ Administrator consent only authorizes the application within your tenant. Individual users must still authenticate and explicitly connect their Outlook calendar within Element451 before any calendar data can be accessed. Element451 only has access to calendars belonging to users who have completed this authorization process.

Element451 does not access email, files, contacts, or other Microsoft 365 data beyond the permissions explicitly granted and required for appointment scheduling functionality.

## Why don’t I see form submission fields for a scheduled appointment?

If the appointment used only the default fields (name, email, and cell), the system doesn’t display a separate form submission. That’s because this basic information is already stored and visible on the contact’s profile.

We only show a form submission card when the scheduling form includes **additional fields** and the complete submission will then appear with the appointment details.

---

# Appointment Settings

## As an admin, can I configure Appointment settings for everyone on my team?

Admins can configure categories, types, and team settings. Admins can also add, edit, and delete availabilities for any user or team from the **Availability** section.

For more information on getting started with appointments for admins, [click here](https://help.element451.com/en/articles/8141376-getting-started-with-appointments-for-admins#h_e6eed0e885). If you are a non-admin user, [click here](https://help.element451.com/en/articles/8148396-start-accepting-appointments) to get started.

## Can I set up a round-robin or group meeting type?

You can create **team availabilities** that distribute appointments across team members using one of two assignment methods:

* **Round-Robin**: Rotates assignments evenly across eligible team members
* **Balanced**: Assigns to the member with the fewest appointments within 7 days **before** and **after** the selected time slot

Admins configure teams in **Appointment** **Settings** > **Team** **Settings**, then create

availabilities with the **Assignee** **Type** set to "Team." For a complete setup guide,

see [Team Appointments](https://help.element451.com/en/articles/8346250-teams).

## Can you collect fees/payments via Appointments?

Not at this time. Payment integration is not available for appointments.

## Can we hide specific appointment types from the Appointment site?

Yes, you can configure appointment types to be private. To do so, create a new appointment type specifically for faculty interviews and mark it as private. After creating the appointment type, add your availability for these interviews. Finally, share your availability link with the individuals who need to schedule appointments. This ensures that the faculty interview appointments remain hidden from the public appointment site.

## Can I restrict appointments to specific days and times?

Yes, for each of your availabilities, you can configure the *[weekly hours settings](https://help.element451.com/en/articles/8148396-start-accepting-appointments#h_aaf807f66c)* to determine your specific availability for each day and time.

## Can I embed the appointment booking form on our website?

No, at this time, the Appointments Site acts as its own entity. To ensure branding, we recommend setting up your [external domain](https://help.element451.com/en/articles/9358702-configuring-external-domains) so that your appointments site URL will read something like `appointments.element451.edu.`

## Can I set overlapping availability for different appointment types?

For example, can I be available for Advising Meetings M-F from 9-5 and also for Career Counseling M-F from 9-5?  
​  
Yes, you can have different availabilities with overlapping times. This allows you to be available for different types of appointments during the same time slots. However, keep in mind that once an appointment is booked for one availability, that time slot will no longer be available for any other availabilities at that same time. Using your example above, if a student books a 9:00 advising appointment, you will no longer be available at 9:00 for career counseling.

## Can Zoom links be generated for Appointments?

Currently, there is no integration between Zoom and our Appointments module. We recommend creating a standard Zoom meeting link, such as your personal meeting link, and placing that URL in either the availability **location** or **description** fields.

## What’s the difference between Appointment Categories and Types?

Both help organize and filter appointments, but they serve different purposes:

* **Types** are the foundation for scheduling by configuring key appointment details, including **privacy settings, location, milestone creation, and the registration form** students complete when booking. Each Type is assigned a **Category** and is used as the base when individuals add their own availability.

* **Categories** act as top-level labels, often aligning with departments or broad use cases. They help students quickly filter and find relevant appointments.

## I'm trying to disconnect my Google Calendar from Appointments, but the button is unresponsive.

If you are unable to remove your Google Calendar via Element451, you can remove it by visiting <https://myaccount.google.com/connections> and removing the authorization on your Google Account. We only recommend doing this if you are unable to remove it via the Element451 interface.

---

# Appointment Booking Process + Availability

## Does an Appointment booking create a prospect milestone?

By default, scheduling an appointment will generate a prospect milestone if the person doesn’t already have a record in Element451. However, you can control this behavior with the “Create Date of Inquiry Milestone” setting in Appointment Types, allowing flexibility based on your needs.

## Can a non-student or community member book an appointment?

Anyone can schedule an appointment. However, for this use case, we recommend disabling the “Create Date of Inquiry Milestone” setting in the relevant Appointment Type. This will prevent new records from being created for anyone who does not have an existing contact record (and you don't wish for them to have one).   
​

## Can I share a URL that takes the invitee to schedule a specific meeting?

Yes, you can. Your custom URL includes a unique slug for each appointment type. When viewing the appointment type, copy the URL from your browser.

## Can the invitee cancel or reschedule their appointment?

Using the links in their [confirmation email/SMS](https://help.element451.com/en/articles/9362119-appointment-notifications-messages), they can update their information (name, email, phone) or cancel. To reschedule, they will need to cancel and book another appointment. When canceling, they will be prompted with the option to "book again."

## Are appointments automatically added to my calendar?

It depends on how your calendar is connected. If you use the **direct Google or Outlook integration**, appointments are automatically added to your calendar and kept up to date when they are changed or canceled. If you connect using a **read-only iCal URL** (or have no connected calendar), Element451 can only check when you're free or busy. In that case, your notification email will contain a [.ics attachment](https://help.element451.com/en/articles/9362119-appointment-notifications-messages#h_2cf5503e9c) you can open to add the meeting to your calendar. Learn more in [Connecting Your Calendar to Appointments](https://help.element451.com/en/articles/8144429-connecting-your-calendar-to-appointments).

## What happens if my availability changes before someone submits their form?

The system performs a final check on your calendar availability when the “Schedule Appointment” button is clicked to prevent any unexpected double bookings.

## Why does a time slot show as available in Element451 when it’s already booked?

If a time slot appears open in Element451 but is actually booked, check the following:

* **Confirm your calendar connection:** Element451 syncs with your linked calendar (Google or Outlook) to display available times. Ensure your calendar is properly connected.

  + **Google Calendar:** Set it to public with “See only free/busy (hide details)” selected. Copy the “Public Address in iCal Format” URL and paste it into **Appointment Settings > My Settings > Import Calendar**.
  + **Outlook Calendar:** Set permissions to “Can view when I’m busy,” copy the ICS URL, and paste it into **Appointment Settings > My Settings > Import Calendar**.

## How does Element451 Appointments determine my availability?

When displaying available time slots, Element451 Appointments checks three key factors:

1. **Configured Availability in Element451**  
   Verifies whether the time slot matches your configured availability, accounting for buffer times.  
   ​
2. **Existing Element451 Appointments**  
   Booked appointments won't show as available.  
   ​
3. **Linked Calendar Status (if applicable)**  
   Checks if you're marked "busy" due to meetings, out-of-office blocks, or other event based on your connected calendar.

For team appointments, these same checks are performed for each team member to determine who is eligible for assignment.

A final availability check occurs when "Schedule Appointment" is clicked to prevent double bookings between search and completion.

---

# Appointment Notifications

## Will I receive a notification notifying me of scheduled appointments?

Yes, you and the invitee will receive an email when an appointment is scheduled, updated, or canceled. For team appointments, the assigned team member receives the notification. You can explore more on appointment notifications [here](https://help.element451.com/en/articles/9362119-appointment-notifications-messages).

## What automatic notifications and reminders are sent to the invitee?

The invitee is sent a confirmation email immediately after scheduling, updating, or canceling (and you will receive a similar email). The invitee is also sent a reminder email 1 hour before the appointment is scheduled to begin. You can explore more on appointment notifications [here](https://help.element451.com/en/articles/9362119-appointment-notifications-messages).

## Why doesn't an appointment confirmation email appear in the contact's Activity Feed?

If the appointment host has a connected Outlook calendar, confirmation emails for scheduled and rescheduled appointments are sent by Outlook as calendar meeting invitations, not by Element451. Since Element451 does not send these messages, they are not logged in the contact's Activity Feed and cannot be tracked. The appointment activity itself is still recorded on the contact's profile, and reminder emails are always sent (and logged) by Element451. Learn more in [Connecting Your Calendar to Appointments](https://help.element451.com/en/articles/8144429-connecting-your-calendar-to-appointments).

## If an invitee declines the Outlook meeting invitation, is their appointment canceled?

No. RSVP responses in Outlook (accept or decline) do not sync to Element451, so the appointment remains scheduled. To cancel or change an appointment, the invitee must use the links included in their confirmation email or SMS.

## Can I customize the automatic notifications?

At this time, you are unable to customize notifications. However, you can use tokens to reference upcoming appointments in Campaign communications. [You can explore more about this here](https://help.element451.com/en/articles/9362119-appointment-notifications-messages#h_55d438bcde).

## Why is the Element451 logo being used on confirmation and reminder emails?

To send these automated messages, a full-color logo is required. If you see the Element451 logo, it means a full-color logo hasn’t been set. We’ve used our system fallback to ensure your message(s) were delivered. To fix this, go to [General Settings > Branding](https://intercom.help/element451/en/articles/8471334-general-settings) and upload your full-color logo.

## Can I add additional notifications, like a 24-hour text reminder?

Yes! You can use an ongoing Campaign and Workflow to send additional reminders or notifications based on your institution's needs. [Click here for more information.](https://help.element451.com/en/articles/9362119-appointment-notifications-messages#h_55d438bcde)

---

# Appointment Analytics

## How are multiple appointments for the same person counted in Insights? If an appointment is canceled and rescheduled, how will that be counted?

In Insights, each appointment is represented by one row. For instance, if one appointment is scheduled and canceled and then a new appointment is scheduled and attended, you will have two total appointments recorded—one canceled and one attended. This distinction is crucial for users analyzing appointment data.

---

# Team Appointments

## How does team appointment assignment work?

When a student books a team availability, Element451 evaluates eligibility in order: team membership, personal booking link, and calendar/scheduling availability. If multiple members are eligible, the system uses the assignment method configured on the availability (Round-Robin or Balanced) to select one team member. The student receives a confirmation with the assigned staff member's name.

## What makes a team member eligible for assignment?

A team member is eligible if they:

* Are a member of the team associated with the availability
* Have a personal booking link configured in **Appointment** **Settings** > **My** **Settings**
* Are not already booked in Element451 or marked as busy on a connected calendar during the selected time slot

  + *Members without a connected calendar are assumed to be available unless they have an existing Element451 appointment at that time*

## Can I share a direct link to a team's booking page?

Yes. Each team with a configured slug has a dedicated booking URL following the format appointments.yourdomain.edu/teams/[team-slug].

## Where do I manage team membership vs. team appointment settings?

Team membership (who belongs to a team) is managed under **Settings** > **Manage** **Users** > **Teams**. Appointment-specific settings for a team — such as display name and slug — are configured in **Appointment** **Settings** > **Team** **Settings**.

## Can a Bolt Agent book a team appointment on behalf of a student?

Yes. Bolt Agents can book team appointments using the same assignment logic if the agent has the Schedule Appointments skill enabled.

## Can multiple appointments be booked at the same time slot for a team?

Yes. As long as more than one team member is eligible at a given time, multiple appointments can be booked for that same slot. Each booking assigns the next available member based on the configured assignment method. The time slot remains available until all eligible members are booked. This applies to both the booking site and when scheduling from the admin side.

## Will duplicate time slots appear if multiple team members are available at the same time?

No. Time slots are shown once per availability, not per available member. If three members of the Admissions team are all free at 2:00 PM, the student sees one 2:00 PM slot — not three. The system handles who gets assigned behind the scenes. More available team members means broader time coverage (slots stay open even if some members are busy), not duplicate slots.

## How do team appointments work with multiple campuses?

Each team is a separate entity on the booking site. For example, you could configure an "Admissions - Main Campus" team and an "Admissions - West Campus" team — each appears as its own team card with its own availabilities. Students select a team first, then see that team's available time slots.

---