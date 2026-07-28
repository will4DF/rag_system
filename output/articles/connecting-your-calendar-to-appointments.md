---
title: Connecting Your Calendar to Appointments
url: https://help.element451.com/en/articles/8144429-connecting-your-calendar-to-appointments
collection: Appointments
---

Learn how to connect your calendar to Element451 for availability checks and learn how to add appointments to your external calendar.

# Overview

Element451’s Appointments module helps streamline scheduling one-on-one meetings with students and guests by checking your availability and optionally adding appointments to your external calendar.

This article covers:

* How Element451 checks your availability
* How to connect your calendar
* Ways to add appointments to your calendar

---

# How Element451 Checks Your Availability

To prevent double-bookings, Element451 checks your availability before allowing students to book appointments. It does this using one or both of the following:

* **Connected Calendar:** If your calendar is connected (either directly via integration or via an iCal link), Element451 reads your free/busy times to determine when you’re available.

  + **Direct Google or Outlook integration:** Provides real-time free/busy data and allows appointments to be written directly to your calendar. This option creates a bi-directional sync between Element451 and either your Outlook or Google calendar.
  + **Shared calendar URL (iCal):** Allows Element451 to read availability but does **not** write appointments to your calendar.

* **Existing Appointments in Element451:** Even without a calendar connection, Element451 will use already booked appointments in the system to prevent overlapping bookings.

* **Your Availability Settings:** Regardless of whether or not your calendar is connected, Element451 applies the settings defined for each availability you create, such as:

  + Buffer time between appointments
  + Advance notice required for booking
  + Minimum and maximum appointment windows

🚨 **Important:** Without a connected calendar, Element451 cannot see other external events—only appointments and settings configured within the platform.

---

# Connecting Your Calendar

To ensure accurate availability checks and sync appointments, connect your calendar using one of the following methods:

## Option #1: Direct Google or Outlook Integration (Recommended)

This option offers the best experience. Appointments are automatically added to your calendar, and changes are bi-directionally synced in real time. 📌 **Note:** You can only connect one calendar per user.

Expand the collapsable sections below to get started:

## Instructions for Connecting Your Calendar

1. Navigate to **Engagement > Appointments.**
2. Click the **More (⋮)** icon in the top right.
3. Select **My Settings.**
4. Under **Connect to Provider**, choose your email provider: **Gmail** or **Outlook.**

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1570084212/9ccdeff1c8af95dd9dc91df009c3/Appts-ConnectToProvider.png?expires=1784333700&signature=3515e0d23bde66ae7de653f9b2703ef0d397571fa569b30109387db47c363507&req=dSUgFsl2mYNeW%2FMW1HO4zXHFs7JyMYDtF4tbWuYvJYhQLmvN9yIm7Jv3feOk%0AXr6M%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1570084212/9ccdeff1c8af95dd9dc91df009c3/Appts-ConnectToProvider.png?expires=1784333700&signature=3515e0d23bde66ae7de653f9b2703ef0d397571fa569b30109387db47c363507&req=dSUgFsl2mYNeW%2FMW1HO4zXHFs7JyMYDtF4tbWuYvJYhQLmvN9yIm7Jv3feOk%0AXr6M%0A)
5. Follow the on-screen authentication process to grant the necessary permissions in order for Element451 to connect with your calendar.
6. Once completed, you will be redirected to the All Appointments page, and your calendar will be successfully connected.

## Video Guide: Google Calendar

## Video Guide: Outlook Calendar

📌 **Note:** Before connecting Element451 to an Outlook Calendar at your school, your Microsoft/Outlook Admin may need to authorize Element451's calendar app. To do so, they can follow this link:

```
https://login.microsoftonline.com/{tenant_id}/v2.0/adminconsent?client_id=01f1a5b4-34ce-42e2-acbc-d1dfe46dba94&redirect_uri=https%3A%2F%2Fapi.451.io%2Fusers%2Fintegrations%2Fappointments%2Foutlook%2Fcallback&scope=https%3A%2F%2Fgraph.microsoft.com%2FCalendars.ReadWrite%20offline_access%20openid%20profile
```

Be sure to replace **{tenant-id}** in the above URL with your school's **Microsoft tenant ID.** This is sometimes also called your Azure AD or Office 365 tenant ID

The Element451 Appointments application is published by Element451, a Microsoft Verified Publisher. The application’s publisher identity has been verified through Microsoft’s publisher verification program and displays the verified publisher designation during Microsoft Entra ID consent and authentication flows.

## Disconnecting Connected Calendar

To disconnect your calendar, return to **My Settings** > **Connect to Provider** and click **Disconnect.**

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1570095337/b5016cf0ad27d9f08bd7ffaa53d7/Appointments-DisconnectCalendar.png?expires=1784333700&signature=e93dc8dbdb03a4f7740bbca76b4f75f602ca0f573d146b5ef007626759715f98&req=dSUgFsl3mIJcXvMW1HO4zTBr55OSovhwrJM59I47yNFSNjGbtYWIglYNJ6jP%0Aj%2FREvx34HOr8F61iTKw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1570095337/b5016cf0ad27d9f08bd7ffaa53d7/Appointments-DisconnectCalendar.png?expires=1784333700&signature=e93dc8dbdb03a4f7740bbca76b4f75f602ca0f573d146b5ef007626759715f98&req=dSUgFsl3mIJcXvMW1HO4zTBr55OSovhwrJM59I47yNFSNjGbtYWIglYNJ6jP%0Aj%2FREvx34HOr8F61iTKw%3D%0A)

📌 **Note Regarding Google:** Disconnecting your Google calendar here is the recommended way to revoke access. If you remove access directly from your Google account, it will cut off ***all*** Element451 integrations, including Drive access used in Import + Export.

## Option #2: Read-Only iCal URL Connection

If you don't wish to connect directly with Google or Outlook, you can share your calendar’s availability using a public iCal (ICS) link.

Expand the collapsable sections below to get started:

## How-To: Google iCal URL

1. Open your Google Calendar in a web browser
2. Click the gear icon (settings) at the top right
3. On the left menu, under Settings for my calendars, select the calendar you want Element451 to check for availability
4. Ensure the settings under **Access Permissions for Events** are as follows:

   * **Make available to public** is enabled
   * **See only free/busy (hide details)** from the dropdown menu is selected
5. Click **Integrate Calendar**
6. Copy the **Public Address in iCal Format** URL
7. Navigate back to Element451
8. Go to **Engagement > Appointments**
9. Click the **More (⋮)** icon in the top right
10. Select **My Settings**
11. Click the **Import** **Calendar** button
12. Paste the copied URL into the Calendar URL box
13. Click **Save**

If you need additional help, check out the [Google Help Center](https://support.google.com/calendar/answer/37083?sjid=12303287338565736424-NA#link&zippy=%2Cshare-a-link).

## How-To: Outlook iCal URL

1. Open your Outlook calendar in a web browser
2. At the top right, click the gear icon (settings)
3. On the left side menu, select **Calendar**
4. From the expanded menu, select **Shared calendars**
5. Under **Publish a calendar**, select the calendar name from the drop-down that you want Element451 to check for availability
6. For the **Select permissions** drop-down, choose **Can view when I'm busy**
7. Click **Publish**
8. Copy the **ICS** URL.
9. Navigate back to Element451
10. Go to **Engagement > Appointments**
11. Click the **More (⋮)** icon in the top right
12. Select **My Settings**
13. Click the **Import** **Calendar** button
14. Paste the **ICS** URL that you copied from your Outlook settings into the Calendar URL box.
15. Click **Save**

If you need additional help, check out the [Microsoft Help Center](https://support.microsoft.com/en-gb/office/share-your-calendar-in-outlook-com-0fc1cb48-569d-4d1e-ac20-5a9b3f5e6ff2).

## What if I don’t connect my calendar?

You can continue to manage appointments in *Engagement > Appointments*, even if you haven't linked your calendar. Element451 will still prevent overlapping appointments within the platform, but it won’t be aware of your other commitments outside the system.

---

# How a Connected Outlook Calendar Affects Notifications

When you connect your Outlook calendar, Element451 creates each appointment as an event on your calendar with the invitee listed as an attendee. Because Outlook automatically emails attendees a meeting invitation, Element451 does not send its own confirmation email for scheduled or rescheduled appointments. This prevents invitees from receiving duplicate notifications.

Keep the following in mind:

* **Confirmation emails come from Outlook.** Invitees receive the Outlook meeting invitation instead of an Element451 confirmation email when an appointment is scheduled or rescheduled.
* **These emails are not logged in Element451.** Because Element451 did not send the message, it will not appear in the contact's **Activity Feed** or email activity, and open/click tracking is not available. The appointment activity (scheduled, updated, or canceled) is still recorded on the contact's profile.
* **Reminder emails are unaffected.** Element451 always sends reminder emails, and they appear in the Activity Feed as expected.
* **Outlook RSVP responses do not sync to Element451.** If an invitee accepts or declines the meeting invitation in Outlook, the appointment status in Element451 does not change. A declined invitation does **not** cancel the appointment. Invitees must use the update or cancel links in their notification to change their appointment.
* **Cancellations sync through the calendar event.** If an invitee cancels through Element451, the event is removed from your Outlook calendar and Outlook sends the cancellation notice. If you delete the event from your Outlook calendar, the appointment is canceled in Element451.

📌 **Note:** This behavior applies only to connected Outlook calendars. With a connected Google calendar, Element451 suppresses Google's automatic invitation and sends its own notification emails, which are logged in the contact's Activity Feed as expected.

---

# Adding Appointments to Your Calendar

Adding appointments to your external calendar ensures you stay organized, receive reminders in your email client, and keep your availability visible to colleagues who may schedule with you outside of Element451.

## Option 1: Direct Calendar Connection (Most Seamless)

When you connect your Google or Outlook calendar using the steps above, Element451 will automatically add appointments to your calendar. It also keeps events up to date if appointments are changed or canceled. No further action is required once connected.

## Option 2: ICS File Attachment in Confirmation Email

**Best for:** Manual control over what’s added to your external calendar.

* Each time an appointment is booked, you’ll receive a confirmation email.
* The email includes an .ics file you can open to add the appointment to your calendar.

You should know:

* Google Calendar may auto-add the event depending on your Gmail settings. However, Outlook users must add it manually by opening the attachment.

---