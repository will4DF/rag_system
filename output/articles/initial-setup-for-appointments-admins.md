---
title: Initial Setup for Appointments (Admins)
url: https://help.element451.com/en/articles/8141376-initial-setup-for-appointments-admins
collection: Appointments
---

Initial setup of Appointments for users with admin access.

# Overview

This guide is for those with administrator access who are responsible for configuring the Appointments module for their institution.

Before your team can begin offering and accepting appointments, you’ll need to complete a few setup steps:

* Configure your Booking Page
* Create at least one Category and Appointment Type
* Configure teams for team-based scheduling (optional)
* Set availability for yourself and others (or train others on setting their own)

🚨 **Important:** Admins must configure at least one **Category** and one **Appointment Type** before users can begin setting their availability.

---

# Appointments Booking Site

Each institution is provided with a dedicated Appointments Site where students, guests, or colleagues can browse and book one-on-one meetings with staff or faculty.

The booking site organizes availabilities into two sections: **People**, where visitors select a specific staff member to meet with, and **Teams**, where visitors select a department or group and the system automatically assigns an available team member. If no teams are configured, only the People section appears.

Administrators are responsible for configuring the Appointments Site settings, including:

* Choosing the primary or custom domain
* Uploading the institution’s logo
* Setting a thank you message for completed bookings
* Managing the site footer and additional branding elements

For full details on configuring your Appointments Site, visit [Appointments Site + Settings](https://help.element451.com/en/articles/11157302-appointments-site-settings).

[Appointments Site + Settings →](https://help.element451.com/en/articles/11157302-appointments-site-settings)

---

# Types

Appointment Types act as templates that define the structure of meetings offered by staff. They allow you to configure shared information when one or more users can host a specific type of appointment.

When adding Types, think about routine appointments offered by your team. For example, you may have four academic advisors available for one-on-one academic advising. In this case, *Individual Academic Advising* could become one of your Appointment Types.

* Each Appointment Type has a **registration form** that the invitee or student completes when booking.
* In addition to Categories, students can also filter appointments by Type.

## Adding + Managing Types

If you're already in Appointment Settings, you can click on **Types** from the left-hand menu. If not, click on the **more (⋮)** iconin the Appointments header and select **Types**.

From here, you can add new or edit existing types. To get you started, Element451 provides three sample types: Admissions Interview, Advising Office Hours, and FAFSA Help. These can be edited or deleted.

## How-To: Add New Type (Including Registration Form)

To add a new type:

1. Click the **+ Add Type** button
2. Configure the type settings:

   * **Name:** Give your appointment type a name. When selecting a name, remember that appointment types are visible to the student for filtering purposes.
   * **Category:** Select the category associated with this type.
   * **Public**

     + Enabled:

       - Accessible from your Appointments Site or via URL.
     + Disabled:

       - Only accessible via URL; hidden from the Appointments Site.
       - The user cannot navigate back to see the public details of that appointment type.
   * **Location** **Type:** Select the appointment's location type - physical or virtual.
   * **Location:** Provide the location of this appointment. If physical, provide details such as the building, room number, etc. If virtual, you can specify how they will access the appointment (e.g., by providing a link to your personal meeting room).
   * **Create Date of Inquiry Milestone:** By default, appointment bookings will generate a Date of Inquiry Milestone using the term and major specified on the registration form. Disabling this setting will prevent the creation of a Date of Inquiry Milestone when someone books this appointment.
   * **Description:** Provide a description of the appointment type.
   * **Additional** **Information**: Allows you to collect appointment-specific details from students. You should enable this field instead of creating a custom field for per-appointment notes. When this is enabled:

     + The 'additional information' field is automatically added to the form.
     + Students will see a prompt: *“Please share anything that will help us prepare for your appointment.”* This cannot be edited.
     + This data is **scoped to the appointment only** and will not overwrite any contact record fields. As a result, it's not visible on the record.
     + To view this information, open the appointment and click **"Edit. "** The response will be visible in the *form submission info* section.
3. Configure the **Registration** **Form.** We go into more detail on this process below.
4. Click **Save**.

## Registration Form

Use the **Registration Form** section to configure the booking form that students complete when scheduling this type of appointment.

Appointment registration forms use the same **[data fields](https://help.element451.com/en/articles/9093505-fields-validation-conditional-logic)** as other forms in Element451, such as application or event forms. If a student enters updated information (e.g., a new phone number), it will overwrite the existing data in their contact record. Be mindful when adding standard fields that may already exist on the student profile.

## How-To: Edit Existing Type

To **edit** or **delete** an existing type:

1. Click the **more (⋮)** icon at the end of that type's row
2. Select the action you wish to perform

---

# Categories

Categories are used to organize appointments by purpose or department, such as Admissions, Financial Aid, or Advising. Students can filter by category on the public Appointments Site.

## Adding + Managing Categories

If you're already in Appointment Settings, you can click on Categories from the left-hand menu. If not, click the **more (⋮)**iconin the Appointments header and select **"Categories"**.

From here, you can add new or edit existing categories. To get you started, Element451 provides three sample categories: Admissions, Financial Assistance, and Advising. These can be edited or deleted.

### How-To: Add + Edit Categories

* To **add** a new category:

  1. Click the **+ Add Category** button
  2. Give your category a name and click **Save**
* To **edit** or **delete** an existing category:

  1. Click the **vertical ellipsis (⋮)** at the end of that category's row
  2. Select the action you wish to perform

---

# Team Settings

Team Settings is where you configure which of your teams are available for appointment scheduling. When a team is configured here, admins can create availabilities assigned to that team rather than an individual staff member.

To access Team Settings, click the **more** **(⋮)** icon in the Appointments header and select **"Team** **Settings"**, or click **Team** **Settings** from the left-hand menu if you're already in Appointment Settings.

Administrators are responsible for configuring teams for appointment scheduling, including:

* Selecting existing teams from your organization's team management (**Settings** > **Manage** **Users** > **Teams**)
* Setting a **Display** **Name** for each team (visible to students on the booking site)
* Defining a **Slug** for each team (creates the team's dedicated booking page URL)
* Adding team availabilities or training other users on creating them

*Note:* *Teams* *are* *created* *and* *managed* *under* *Settings* *>* *Manage* *Users* *>* *Teams.* *If* *you need* *a* *team* *that* *doesn't* *exist* *yet,* *someone with the **Administer Internal Users** permission* *will* *need* *to* *create* *it there* *first.*

For a complete guide to configuring teams, creating team availabilities, and understanding how assignment works, read our [Team Appointments](https://help.element451.com/en/articles/13921320-team-appointments) help article.

[Team Appointments →](https://help.element451.com/en/articles/13921320-team-appointments)

---

# Availability

Once Categories, Types, and Teams have been configured, availability can be set.

* Admins can add, edit, and delete availabilities for any user or team from the **Availability** section.
* Non-admin users can add and manage their own availabilities from **My** **Availability**.

## How-To: Add Your Availability

For a step-by-step guide, check out our [Configuring Your Appointment Availability](https://help.element451.com/en/articles/8148396-configuring-your-appointment-availability) help article.

## How-To: View + Edit User's Availability

1. Navigate to **Engagement** > **Appointments.**
2. Click the **more** **(⋮)** icon in the right corner of the header.
3. Select the **Availability** button ![](https://downloads.intercomcdn.com/i/o/967585578/25e6b49f1779e8cd28583868/Availability+.png?expires=1784430000&signature=d0069c2af9f5877466b3cb4e060042e4cf0a3eaf9a30df563bfba24789874e11&req=fSYgE8F7mIZXFb4X1HO4gXnA1o8xMOlXRKePER%2Ff2qTp6%2F25fCl1xz60wFdu%0A) from the menu.
4. Locate the availability you wish to manage and select the **more** **(⋮)** icon at the end of the row.
5. Select the action you wish to take:

   * **Copy** **Link:** Copy the URL for the booking page for that availability.
   * **Open**: Open the booking page for that availability.
   * **Edit:** For adjustments to existing availability, including changing the settings or modifying when the appointment can be booked, opt for the **Edit** mode. This feature allows you to modify any aspect of an availability, such as appointment type, scheduling conditions, weekly hours, and notifications. The only exception is the assignee, which remains fixed to ensure clarity on who the appointment is with. This approach ensures you can fine-tune the details of your availability without needing to remove the slot entirely.
   * **Delete**: If you find that a certain availability slot is no longer necessary or you wish to completely remove the option, use the **Delete** option. This action permanently removes the availability from the booking page.

   [![](https://downloads.intercomcdn.com/i/o/967603224/3f25ff28b3266dea976f6d4f/Appt+Avail+More+Options.png?expires=1784333700&signature=7364fec6408ef5ef25226d40b6cef574a50a71bf98921ae6304916c0c210734e&req=fSYgEMl9n4NbFb4f3HP0gP2KsAukQ7XOPPahZb30FkN90asWeyeqjavqCznW%0Ak%2Fo%3D%0A)](https://downloads.intercomcdn.com/i/o/967603224/3f25ff28b3266dea976f6d4f/Appt+Avail+More+Options.png?expires=1784333700&signature=7364fec6408ef5ef25226d40b6cef574a50a71bf98921ae6304916c0c210734e&req=fSYgEMl9n4NbFb4f3HP0gP2KsAukQ7XOPPahZb30FkN90asWeyeqjavqCznW%0Ak%2Fo%3D%0A)

#

---

# What Non-Admin Users Need to Do

Before a staff member can be booked for appointments, they must:

* Configure their personal booking link (custom slug)
* Set their availability for each appointment type they offer
* Optionally connect their Google or Outlook calendar

✨ **Pro Tip***:* *Staff* *members* *who* *belong* *to* *a* *team* *configured* *for* *appointments* *should* *ensure their* *personal* *booking* *link (custom slug)* *is* *set* *up*.

For more guidance, see: [Configuring Your Appointment Availability →](https://help.element451.com/en/articles/8148396-configuring-your-appointment-availability)

[Appointment Availability →](https://help.element451.com/en/articles/8148396-configuring-your-appointment-availability)

---

# Additional Resources

## Frequently Asked Questions

For a list of commonly asked questions about the functionality of the Appointments Module, visit our [FAQ help article](https://help.element451.com/en/articles/8834280-appointments-frequently-asked-questions).

## Video Guide

---