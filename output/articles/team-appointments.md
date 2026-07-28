---
title: Team Appointments
url: https://help.element451.com/en/articles/13921320-team-appointments
collection: Appointments
---

Learn how to set up team-based scheduling so students can book with a department or group and let Element451 automatically assign the right team member.

# Overview

Team Appointments let you offer availability on behalf of a **group** of internal users rather than a single individual. When a student books a team appointment, Element451 automatically assigns one eligible team member based on the assignment method you choose. From that point forward, the appointment behaves like a standard one-on-one booking—the student receives a confirmation with the assigned staff member's name, and the appointment appears on that member's schedule.

## Common Use Cases:

* Admissions offers interviews that any available counselor can fill
* Advising offers drop-in hours staffed by whichever advisor is free
* Financial Aid offers loan counseling availability across multiple specialists

## How it Works at a Glance:

1. Configure a team in **Appointment Settings** > **Team Settings**
2. Create an availability and assign it to that team
3. Students browse the booking site, select a team, and choose a time
4. Element451 assigns the appointment to an eligible team member automatically

---

# Prerequisites

Before setting up team appointments, make sure the following are in place:

1. **Make sure you've configured teams in Element451 that align with how you want to structure your appointment bookings.**

   * Teams are managed under *[Settings](https://help.element451.com/en/articles/8346250-teams)* [> *Manage Users* > *Teams*](https://help.element451.com/en/articles/8346250-teams). You'll select from these existing teams when configuring Appointment Settings, but you can't create new teams from within Appointment Settings itself.
   * Users can belong to multiple teams, so feel free to create new teams specifically for appointments without affecting your existing setup.
   * Like individuals, Teams have a dedicated booking page.   
     ​
2. **Team members have personal booking links.**

   * Each team member must have a custom slug configured in [Appointment Settings > My Settings](https://help.element451.com/en/articles/8148396-configuring-your-appointment-availability).
   * Members without a personal booking link are not eligible to receive team appointment assignments.
3. **Calendar connections are recommended.**

   * Team members who [connect their Google or Outlook calendars](https://help.element451.com/en/articles/8144429-connecting-your-calendar-to-appointments) allow Element451 to check busy/free status when assigning appointments.

---

# Step 1: Configure Team Settings

Team Settings is where you configure which of your organization's teams are available for appointment scheduling.

## Accessing Team Settings

1. Navigate to **Engagement** > **Appointments.**
2. Click the **⋮** (more) icon in the upper-right corner of the page.
3. Select **Team Settings** from the menu.

You'll see a list of all teams configured for appointments, with columns for **Team**, **Display Name**, and **Slug**.

## Adding a Team to Leverage Appointments

1. Click **+ Add Team** at the bottom of the list
2. In the **Team** field, search for and select an existing team from the dropdown.

   * This list is populated from your organization's teams managed under **Settings** > **Manage Users** > **Teams**.
3. Enter a **Display Name**. This is the name students see on the booking site.
4. Enter a **Slug**. This creates the team's dedicated booking page URL (e.g., `appointments.yourdomain.edu/teams/admissions-team`).

   * **Important**: Only teams with a defined slug appear on the booking site.
5. Click **Save**

## Editing + Deleting a Team

1. Click the **⋮** (more) icon at the end of any team row
2. Select **Edit** to modify the display name or slug, or **Delete** to remove the team from appointment scheduling

📌 **Note:** Deleting a team from Appointment Team Settings removes it from the booking site and prevents future bookings. It does not delete the team itself. Team management and membership is managed under **Manage Users** > **Teams**.

---

# Step 2: Create a Team Availability

Once your teams are configured in Team Appointment Settings, you can create availabilities assigned to a team rather than an individual.

## Creating Team Availability

1. Navigate to **Engagement** > **Appointments**
2. Click the **⋮** (more) icon and select **Availability**
3. Click **+ Add Availability**
4. Fill in the appointment details:

   * **Name:** A descriptive name for this availability (e.g., *Admissions Interview* or *Academic Advising Drop-In*)
   * **Appointment Type:** Select the appropriate type
   * **Slug:** A URL-friendly identifier for this specific availability
   * **Active:** Toggle on to make this availability bookable
   * **Description:** Optional details shown to students on the booking page
5. Under **Assignee Type**, select **Team**

   * Selecting **Admin** assigns the availability to an individual internal user
   * Selecting **Team** assigns the availability to a team
6. In the **Assign to a Team** dropdown, select your team.

   * Only teams configured in **Team Settings** appear here.
7. Choose an **Assignment Method:**

   * **Round-Robin** — Rotates assignments evenly across eligible team members in sequence, ensuring even distribution over time.
   * **Balanced** — Assigns the appointment to the available team member with the fewest appointments within 7 days before and 7 days after the selected time slot. If there is a tie, the system falls back to Round-Robin.
8. Configure the remaining fields — **Location Type**, **Location**, **Scheduling Window**, **Buffer Time**, **Scheduling Conditions**, **Weekly Hours**, and **Notifications** — the same way you would for any individual availability.
9. Click **Save**

🧠 **Good to Know:** For details on scheduling windows, buffer time, weekly hours, date overrides, and notification settings, see [Configuring Your Appointment Availability](https://help.element451.com/en/articles/8148396-configuring-your-appointment-availability).

---

# How Team Member Assignment Works

When a student selects a time slot on a team availability, Element451 determines which team member to assign by evaluating eligibility in the following order:

1. **Team** **Membership**  
   The system checks the team associated with the availability and identifies all members of that team.  
   ​
2. **Personal** **Booking** **Link**  
   Of those team members, the system narrows the list to members who have a custom slug configured in **Appointment** **Settings** > **My** **Settings**. Members without a personal booking link are not eligible for assignment.  
   ​
3. **Calendar** **Availability**  
   Of the remaining eligible members, Element451 checks for scheduling conflicts. This includes existing appointment bookings within Element451 as well as busy status on any connected Google or Outlook calendar. Members who are already booked or marked as busy during the selected time slot are excluded. Members without a connected calendar are assumed to be available unless they have an existing Element451 appointment at that time.  
   ​
4. **Assignment** **Method**

   * If only **one** eligible member remains, they receive the appointment.
   * If **multiple** members are still eligible, the system uses the assignment method configured on the availability (described below).

## Assignment Methods

|  |  |
| --- | --- |
| **Method** | **How it works** |
| **Round-Robin** | Maintains an ordered list of eligible members and assigns the next available person in sequence. Ensures even rotation over time. |
| **Balanced** | Counts each eligible member's appointments in the 7 days before and after the selected time slot. Assigns to the member with the fewest total appointments. Ties are broken by Round-Robin. |

🧠 **Good to Know***:* A single time slot can support multiple bookings as long as eligible team members remain available. For example, if three team members are free at 10:00 AM, three separate 10:00 AM appointments can be booked — each assigned to a different member. The time slot remains available on the booking site until all eligible members are booked at that time.

🚨 **Important:** Once assigned, the appointment is treated as a standard one-on-one booking. **There is no automatic reassignment if the assigned staff member becomes unavailable after booking.**

---

# The Booking Site Experience

Your [appointments booking site](https://help.element451.com/en/articles/11157302-appointments-site-settings) organizes availabilities into two sections:

## People

* Individual staff members with active availabilities appear here, sorted alphabetically by last name.
* Visitors can select a person to view their available time slots and book directly.
* On an individual booking page, only one-on-one availabilities are displayed. Team availabilities that the individual may participate in are not shown.

## Teams

* Teams with active availabilities and configured slugs appear here sorted alphabetically by team name.
* Each team displays with a team icon and its display name.
* Visitors select a team to view its available time slots. They do not choose a specific staff member. Element451 handles the assignment automatically.
* The **Teams** section only appears on the booking site when at least one team has an active availability and a configured slug. If no teams meet these criteria, the section is hidden.

---

# Team Booking Pages

Each team has a dedicated booking page based on its slug. When a visitor selects a team from the booking site, they are taken to that team's booking page, which displays all of the team's active availabilities with details including duration, location, and availability name.

## Sharing Team Booking URLs

You can share a team's booking page URL directly. The URL follows the format:

`appointments.yourdomain.edu/teams/[team-slug]`. For example, a team with the slug `admissions-team` would have the booking page:

`appointments.yourdomain.edu/teams/admissions-team`

These links can be:

* Shared via email, chat, or social media
* Used in **Bolt Jobs** to send scheduling links to students at scale
* Embedded in campaign communications using scheduling link tokens

---

# Bolt Agent Support

Bolt Agents can book team appointments on behalf of students when the [Schedule Appointments skill](https://help.element451.com/en/articles/8993380-bolt-agent-skills) is enabled. When a Bolt Agent schedules a team appointment, the same assignment logic applies — Element451 selects an eligible team member using the configured assignment method.

✨ **Pro Tip:** You can also use [Bolt Agent Jobs](https://help.element451.com/en/articles/11131186-getting-started-with-bolt-agent-jobs) to send team appointment scheduling links to groups of students, making it easy to promote department-level booking pages at scale.

---