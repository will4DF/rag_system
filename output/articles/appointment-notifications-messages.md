---
title: Appointment Notifications + Messages
url: https://help.element451.com/en/articles/9362119-appointment-notifications-messages
collection: Appointments
---

This article covers automating notifications to boost efficiency and reduce no-shows with email and SMS appointment reminders.

# Overview

Automated appointment notifications save you time by increasing workflow efficiency and reducing the risk of no-shows by reminding your invitees of their upcoming appointments.

## Notification Settings

Notification settings are configured at the availability level, allowing you to control the sender name, sender email, reply email address, and SMS notification enablement. To access and modify these settings, navigate to the **[Appointment](https://help.element451.com/en/articles/8148396-start-accepting-appointments)** [**Settings** > **Availability**](https://help.element451.com/en/articles/8148396-start-accepting-appointments).

## ICS Attachments

An ICS file is attached to all notification emails sent to both hosts and invitees.

ICS files are used to share calendar event details, such as event times, locations, attendees, and other information, across different calendar applications and platforms. When you receive an ICS file attached to an email, you can import or open it in your calendar application (e.g., Google Calendar, Apple Calendar, Microsoft Outlook). This allows the calendar event details to be added automatically to your calendar, saving you from manually entering the information.

---

# Host Notifications

## Confirmation Email

* Hosts automatically receive emails after appointments are **scheduled**, **updated**, or **canceled.**

  + For team appointments, the assigned team member receives the host notification.
  + Emails are sent regardless of who performs the action (the invitee, you, or another internal user).
  + Emails include a link to conveniently manage your appointments.
  + Emails include an ICS file to add the appointment to your calendar.

## Reminder Email

* You are sent a reminder email **one hour before the appointment is scheduled to begin**.

---

# Invitee Notifications

## Confirmation Email + SMS

* The invitee (contact) is **automatically** sent an email after their appointment has been **scheduled**, **updated**, or **canceled**.

  + To send an SMS confirmation in addition to the email, you must enable the SMS notification option in the settings for that specific availability.
  + For team appointments, the confirmation includes the assigned staff member's name.
  + Notifications are sent regardless of who performs the action (the invitee, you, or another internal user).
  + The scheduled and updated notifications both include links to update or cancel the appointment. The canceled notification provides a link to reschedule the appointment.
  + Emails include an ICS file to add the appointment to their calendar.

    - The ICS title is formatted to read: {{Attendee First}} {{Attendee Last}} | {{ClientName:AppointmentTypeName}}.

🚨 **Important:** If the appointment host has a connected **Outlook** calendar, the confirmation email for scheduled and rescheduled appointments is sent by Outlook as a calendar meeting invitation, not by Element451. Because Element451 does not send this email, it will not appear in the contact's **Activity Feed** or email activity, and open/click tracking is not available. This prevents the invitee from receiving duplicate emails (one from Element451 and one from Outlook). The appointment itself (scheduled, updated, or canceled) is still recorded in the contact's Activity Feed, and reminder emails are always sent by Element451. Hosts with a connected **Google** calendar are not affected: Element451 sends and logs all notifications as expected.

[![](https://downloads.intercomcdn.com/i/o/1058751645/b29640dddef65a9c1bb0c7bf/Email+Confirmation.png?expires=1784333700&signature=864c24f8cb1c05a782cf587d25f2573e69d7868d29795eccb72ff428e6ab206f&req=dSAiHs57nIdbXPMW1HO4zXI%2BkQtLiJQLsFvw5pETBwedMKC0%2BslsdKhvNfNl%0AZOaxrNKUaESjvSel1FU%3D%0A)](https://downloads.intercomcdn.com/i/o/1058751645/b29640dddef65a9c1bb0c7bf/Email+Confirmation.png?expires=1784333700&signature=864c24f8cb1c05a782cf587d25f2573e69d7868d29795eccb72ff428e6ab206f&req=dSAiHs57nIdbXPMW1HO4zXI%2BkQtLiJQLsFvw5pETBwedMKC0%2BslsdKhvNfNl%0AZOaxrNKUaESjvSel1FU%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1058751837/fde2452c40fc247406b6db7a/Text+Confirmation.png?expires=1784333700&signature=924837463ea314e2adef7942f19f6fe32a5049c1318ce0fce612ae8bdabc9fae&req=dSAiHs57nIlcXvMW1HO4zQ7rX924bv452WhS8TAIjlt%2B%2FHMB0AGuX7LzlhHY%0AGVFpMhUH%2BZZDxn3UpDA%3D%0A)](https://downloads.intercomcdn.com/i/o/1058751837/fde2452c40fc247406b6db7a/Text+Confirmation.png?expires=1784333700&signature=924837463ea314e2adef7942f19f6fe32a5049c1318ce0fce612ae8bdabc9fae&req=dSAiHs57nIlcXvMW1HO4zQ7rX924bv452WhS8TAIjlt%2B%2FHMB0AGuX7LzlhHY%0AGVFpMhUH%2BZZDxn3UpDA%3D%0A)

## Reminder Email + SMS

* The invitee is sent a reminder email **one hour before the appointment is scheduled to begin**. This ensures that the invitee is prepared and organized for their upcoming appointment.

  + To send an SMS reminder in addition to the email, you must enable the SMS notification option in the settings for that specific availability.
  + The reminder notification includes links to update or cancel the appointment.
  + Emails include an ICS file to add the appointment to your calendar.

[![](https://downloads.intercomcdn.com/i/o/1058749406/6c5f60758d881bcf26b43c15/Email+Reminder.png?expires=1784333700&signature=36ecd4d7b40fb16a8603cb6b53c108cd224e36970691437cbfd0bf111c10a032&req=dSAiHs56lIVfX%2FMW1HO4zW9Jr8jx6SBSNF8BKmllme7lrmLzP6GcC7%2FAVHZB%0AbUvUYh0JmsbBHiUExLY%3D%0A)](https://downloads.intercomcdn.com/i/o/1058749406/6c5f60758d881bcf26b43c15/Email+Reminder.png?expires=1784333700&signature=36ecd4d7b40fb16a8603cb6b53c108cd224e36970691437cbfd0bf111c10a032&req=dSAiHs56lIVfX%2FMW1HO4zW9Jr8jx6SBSNF8BKmllme7lrmLzP6GcC7%2FAVHZB%0AbUvUYh0JmsbBHiUExLY%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1058750110/2b0a1bdc944d1a8c8a6a4778/Text+Reminder.png?expires=1784333700&signature=a0162cc99e0f5f02d142675f195c054134a37571d12feaed445854bd3ebc065a&req=dSAiHs57nYBeWfMW1HO4zebK%2Ft02MFLrzIZFZRLMULdHzeDnJWPtrDnJF%2B6u%0AN%2Bw7w8BGXhC6UUgIVTQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1058750110/2b0a1bdc944d1a8c8a6a4778/Text+Reminder.png?expires=1784333700&signature=a0162cc99e0f5f02d142675f195c054134a37571d12feaed445854bd3ebc065a&req=dSAiHs57nYBeWfMW1HO4zebK%2Ft02MFLrzIZFZRLMULdHzeDnJWPtrDnJF%2B6u%0AN%2Bw7w8BGXhC6UUgIVTQ%3D%0A)

---

# Customizing Appointment Notifications + Messages

Currently, system appointment confirmation and reminder notifications cannot be customized. However, you can use [tokens](https://help.element451.com/en/articles/1524113-tokens) to reference upcoming appointments in [Campaigns](https://help.element451.com/en/collections/124581-campaigns). This lets you send personalized one-time or ongoing communications through a Workflow to your appointment invitees.

|  |  |
| --- | --- |
| **Next Appointment Type** | [appointment:next\_appointment\_type] |
| **Next Appointment Date and Time** | [appointment:next\_appointment\_datetime] |
| **Next Appointment URL** | [appointment:next\_appointment\_url] |
| **Next Appointment Assignee** | [appointment:next\_appointment\_assignee] |

Each token includes additional scopes such as *Appointment Type*, *Appointment* *Status*, and *Appointment* *Assignee*.

[![](https://downloads.intercomcdn.com/i/o/1058676497/401950c3c2a995bc763c022f/Note-Orng.png?expires=1784333700&signature=202865a8adc2a725b0943cc747c73272076436659b318c4057ae15d5c8c49b3d&req=dSAiHs95m4VWXvMW1HO4zc6wbcvs167De%2BTNpOnxoBMXHCTcml7bvNa6Pf5x%0AkHvdxIL33669AgKRuaU%3D%0A)](https://downloads.intercomcdn.com/i/o/1058676497/401950c3c2a995bc763c022f/Note-Orng.png?expires=1784333700&signature=202865a8adc2a725b0943cc747c73272076436659b318c4057ae15d5c8c49b3d&req=dSAiHs95m4VWXvMW1HO4zc6wbcvs167De%2BTNpOnxoBMXHCTcml7bvNa6Pf5x%0AkHvdxIL33669AgKRuaU%3D%0A)

These tokens reference **future** appointments. If the contact has no upcoming appointments, the token value will be blank.

​

---