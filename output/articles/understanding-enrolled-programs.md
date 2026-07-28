---
title: Understanding Enrolled Programs
url: https://help.element451.com/en/articles/15032187-understanding-enrolled-programs
collection: People
---

What Enrolled Programs are, how they differ from Application Programs and Intended Major, the available fields, and how data is populated.

# Overview

Enrolled Programs is a data structure on the Contact record that stores information about a student's current academic program(s) at your institution. It's distinct from what a student applied to or expressed interest in as a prospect.

## What Are Enrolled Programs?

Enrolled Programs is a repeating data type, meaning a single contact can have multiple program records (for example, a student pursuing a dual major, or a student who has changed majors over time). Each program record stores details like major, degree, term, campus, GPA, and credits.

This data type is intended for **current students**, typically populated from your Student Information System (SIS) such as Banner, Colleague, or Anthology.

---

# Enrolled Programs vs. Other Program Fields

Element451 has several program-related fields. Here's how they differ:

|  |  |  |
| --- | --- | --- |
| Field | Where It Lives | Use Case |
| **Intended Major** | Top-level contact field | Prospect's stated program of interest, captured on RFI forms, events, and appointments. |
| **Application Program** | Application object | The program a student listed on a submitted application. Frozen at submission. |
| **Enrolled Programs** | Repeating data on the contact | The student's current academic program(s), typically synced from the SIS. |
| **Active Major** | Calculated trait | Derived from application milestone data. |

**Note:** Active Major is calculated from application milestones and does not currently read from Enrolled Programs data.

---

# Available Fields

Each Enrolled Program record can include the following fields:

|  |  |
| --- | --- |
| **Program Major** | The student's declared major. References your Majors data source. |
| **Program Status** | Whether the program is `active` or `inactive` for this student. |
| **Program Degree** | The credential being pursued (e.g., AA, BS). References your Degrees data source. |
| **Program Term** | The catalog term associated with the program. References your Terms data source. |
| **Program Campus** | The campus where the program is being studied. References your Campus data source. |
| **Cumulative GPA** | The student's overall GPA at the institution. |
| **Major GPA** | The student's GPA within their major. |
| **Earned Credits** | Credits the student has successfully completed. |
| **Attempted Credits** | Total credits the student has attempted. |
| **Required Credits** | Total credits required to complete the program. |
| **Start Date** | When the student started this program. |
| **End Date** | When the student completed or left this program. |
| **External ID** | Identifier from your SIS for mapping purposes. |
| **Item ID** | Internal Element451 record identifier. |

---

# How Data Is Populated

Enrolled Programs is a **read-only data type** within the contact profile. You cannot manually add, edit, or delete program records from a contact's profile page.

Program data must be populated through one of the following methods:

* **Import/Export**: Bulk upload program data using the [Import + Export module](https://help.element451.com/en/articles/9000459-getting-started-with-imports).
* **API**: Programmatic create, update, and delete via the REST API (`/v2/users/:userId/profile/programs`).
* **SIS Integration**: Managed integrations with systems like Ellucian Ethos (Banner/Colleague) and Anthology populate Enrolled Programs automatically.

---

# Viewing Enrolled Programs on a Contact

Enrolled Programs appear as a card on the contact's profile. If you don't see the card, you may need to add it to your [profile template](https://help.element451.com/en/articles/10471008-configuring-profile-templates).

Each program record displays as its own entry on the card, summarizing the program at a glance. The card title follows the pattern Major – Term – Degree, with the date range, campus, GPA, and credit completion shown below:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2401888714/5005ab76af0cb351d05f34620d97/Enrolled+Programs+Card%402x.png?expires=1784333700&signature=e3b13b993c921fd7953f23034b45e2ff04aa669191677ea9f855d462b29888d9&req=diQnF8F2lYZeXfMW1HO4zWnAbq6B3XVV%2FXhRzW5HW3L8U4whLORgHppXFWG3%0AAIMpR2JQj1SKtM6kK4o%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2401888714/5005ab76af0cb351d05f34620d97/Enrolled+Programs+Card%402x.png?expires=1784333700&signature=e3b13b993c921fd7953f23034b45e2ff04aa669191677ea9f855d462b29888d9&req=diQnF8F2lYZeXfMW1HO4zWnAbq6B3XVV%2FXhRzW5HW3L8U4whLORgHppXFWG3%0AAIMpR2JQj1SKtM6kK4o%3D%0A)

Click any program record to open its full detail view. The detail view shows every field stored on that record—Major, Term, Campus, Degree Code, Start and End Dates, Status, Cumulative GPA, Major GPA, and credit details:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2401892436/8dee5940f8d4c0b33d66c601d7ce/Enrolled+Program+Details%402x.png?expires=1784333700&signature=17463c9ca967f73c264fabc2bc3976090999bf8607a06e6b7dd31011810a5113&req=diQnF8F3n4VcX%2FMW1HO4zYUJWlb8RMenWvN%2FMIdTd0Nc%2FAW3Ud4AZdVLW2pH%0AoNYZ3KerqVoqLY2uB4I%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2401892436/8dee5940f8d4c0b33d66c601d7ce/Enrolled+Program+Details%402x.png?expires=1784333700&signature=17463c9ca967f73c264fabc2bc3976090999bf8607a06e6b7dd31011810a5113&req=diQnF8F3n4VcX%2FMW1HO4zYUJWlb8RMenWvN%2FMIdTd0Nc%2FAW3Ud4AZdVLW2pH%0AoNYZ3KerqVoqLY2uB4I%3D%0A)

---

# Permissions

A dedicated [permission](https://help.element451.com/en/articles/6590379-list-details-of-individual-permissions), **View Enrolled Program GPA**, controls whether a user can see GPA values (Cumulative GPA and Major GPA).

Users without this permission:

* Cannot see GPA values on the contact profile
* Cannot use GPA-based segment filters

Configure this permission per role in your platform settings.

---