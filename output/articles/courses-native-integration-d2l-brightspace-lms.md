---
title: Courses Native Integration: D2L Brightspace LMS
url: https://help.element451.com/en/articles/11116105-courses-native-integration-d2l-brightspace-lms
collection: Integrations
---

# Overview

The Brightspace LMS integration seamlessly syncs real-time academic and enrollment data from Brightspace into Element451. This guide will walk you through the setup process, from configuring Brightspace settings to completing the integration within Element451.

📌 **Note:** This is a one-way integration. Element451 reads data from Brightspace but **does not** write back any data.

## Overview of the Setup Process

To get started, there are two main steps outlined in detail below.

1. [Set Up Authentication in Brightspace (Register an App)](#h_f50e8009bd)
2. [Provide Brightspace Credentials to Element451](#h_01c166ba50)

---

# Step 1: Set Up Authentication in Brightspace

To allow Element451 to securely connect to your Brightspace environment, you’ll need to register a new OAuth 2.0 application.

🚨 **Important:** You must be a Brightspace admin with access to manage the extensibility tool in order to complete this step.

How to register an Application on Brightspace:

1. Log in to your Brightspace admin account.
2. Navigate to **Manage Extensibility** > **OAuth 2.0** tab.
3. Click **Register an app**.
4. Enter a *name*, the *redirect* *URI*, and the *scope* for the application. You can find these details in the table below.
5. After saving, Brightspace will generate your **Client ID** and **Client Secret**. Copy them and keep them somewhere safe—you’ll need to share them with your Element451 team in the next step.

Application Settings:

|  |  |  |
| --- | --- | --- |
| **Detail** | **What to Enter** | **Purpose** |
| Name | Element451 Integration (or your preferred label) | Identifier |
| Redirect URL | [`https://api.451.io/clients/integrations/brightspace/oauth2`](https://api.451.io/clients/integrations/brightspace/oauth2) | Allows secure communication between Brightspace and Element451 |
| Scope | `'organizations:organization:read'`  `'users:userdata:read'`  `'users:own_profile:read'`  `'role:detail:read'`  `'enrollment:orgunit:read'`  `'orgunits:course:read'`  `'sections:section:read'` ​`'grades:gradevalues:read'`    Note: Element451 only needs **read** permissions. No data will be written back to Brightspace. | Determines the actions that Element451 can perform |

For detailed instructions on registering an OAuth2 Application, refer to the official Brightspace guide: [Registering an Application](https://community.d2l.com/brightspace/kb/articles/21863-how-to-get-started-with-oauth-2-0#registering-an-application).

---

# Step 2: Create (or assign) a Service User Account

When setting up the Element451 integration, the service account (the user you use to authenticate your integration) in Brightspace must have a role with specific permissions. Without these permissions, the integration will not be able to read courses, roles, or enrollment information.  
​

## 1. Create or Select the Service User

* Log in to Brightspace as an administrator.
* Navigate to **Admin Tools → Users**.
* Either create a new dedicated account (recommended) or choose an existing account you want to use for the integration.
* Assign the account a role you will configure for Element451 (for example, “Element451 Service”).

## 2. Assign Permissions to the Role

1. Go to **Admin Tools → Roles and Permissions**.
2. Select the role assigned to your service user.
3. At the **Organization level**, enable the following permissions:

   * Org Units and Semesters

     + **Org Unit Editor → View Org Unit Editor**
   * Roles

     + **Roles and Permissions → See Roles and Permissions**
   * Courses

     + **Course Management Console → See Course Info**
   * Users and Enrollments

     + **Users → See the User Management tool**
     + **Users → View User Enrollments**
     + **Users → Search for <RoleName>** (enable for each role you want Element451 to import, such as Student, Instructor, Advisor)
   * **Grades**

     + Grades → See the Grades tool
     + Grades → See user grade values (API Only)
     + Grades → Retrieve Grade Values for Course Offering Descendants (API Only)
   * **Groups & Sections**

     + Groups & Sections Management → See Sections

## 3. Verify the Role

* Log in as the service user.
* Confirm you can open the **Org Unit Editor**.
* Confirm you can search for users and view their enrollments.

⚠️ **Tip:** Use the minimum permissions above. Additional edit permissions (e.g., “Can Create and Edit Org Units”) are not required and should remain disabled to maintain least-privilege access.

---

# Step 3: Authenticate the Integration in Element451

Once you have registered your application in Brightspace, you'll need to authorize Element451 to access your Brightspace data using OAuth.

1. Click on your avatar/profile picture in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Integrations**.
3. From the left-hand menu, select **Brightspace LMS.**

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1577321213/898efcf728c97a73f7f71327faca/CleanShot+2025-06-18+at+13_22_38.png?expires=1784333700&signature=1b5122ac5dc3db4336bd10ddfed6b7d67333ddd8ba4628e1aac136832c567b40&req=dSUgEcp8nINeWvMW1HO4zcknX%2FXtTuF2OQ4HCDcTvH7hFBNxzchUTGY16VwI%0AgOHN%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1577321213/898efcf728c97a73f7f71327faca/CleanShot+2025-06-18+at+13_22_38.png?expires=1784333700&signature=1b5122ac5dc3db4336bd10ddfed6b7d67333ddd8ba4628e1aac136832c567b40&req=dSUgEcp8nINeWvMW1HO4zcknX%2FXtTuF2OQ4HCDcTvH7hFBNxzchUTGY16VwI%0AgOHN%0A)
4. Click the **Authenticate** button and follow the prompts.

You'll need your `Client ID` and `Client Secret`.

---

# Step 4: Configure Preferences

Once you've authenticated your integration, you can access the LMS integration settings.

To review and adjust your preferences, **click the pencil icon** in the top right corner of your LMS integration card.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613847288/52f8219f94f286b5da31bae59427/CleanShot+2025-07-10+at+15_18_28%402x.png?expires=1784333700&signature=1a3e512051bf22475dae7645b411740421613bf14e409da0831ed3c2398d22cc&req=dSYmFcF6moNXUfMW1HO4zZnC2XBE9lQqI%2BUV0go0RygDxkUSx49L%2FMO1m5tm%0AXbt2lisz%2BY4xd7hUYIc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613847288/52f8219f94f286b5da31bae59427/CleanShot+2025-07-10+at+15_18_28%402x.png?expires=1784333700&signature=1a3e512051bf22475dae7645b411740421613bf14e409da0831ed3c2398d22cc&req=dSYmFcF6moNXUfMW1HO4zZnC2XBE9lQqI%2BUV0go0RygDxkUSx49L%2FMO1m5tm%0AXbt2lisz%2BY4xd7hUYIc%3D%0A)

## Data Sync Preferences

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613876121/3c15c60d90d44c33389172e98bd3/CleanShot+2025-07-10+at+15_33_54%402x.png?expires=1784333700&signature=023c39eea6ecd8c221dc84bdb898a81427b14bb7bf7d0034f51558aa7bb0666f&req=dSYmFcF5m4BdWPMW1HO4zRnMbUI98eySvE7yLavBkT8seRzjqdyGeeNEe1cD%0AeZnTW1H%2Fc87I%2B%2BXYlIc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613876121/3c15c60d90d44c33389172e98bd3/CleanShot+2025-07-10+at+15_33_54%402x.png?expires=1784333700&signature=023c39eea6ecd8c221dc84bdb898a81427b14bb7bf7d0034f51558aa7bb0666f&req=dSYmFcF5m4BdWPMW1HO4zRnMbUI98eySvE7yLavBkT8seRzjqdyGeeNEe1cD%0AeZnTW1H%2Fc87I%2B%2BXYlIc%3D%0A)

* **Courses**¹: Import course information from Brightspace, including course name, code, department, and other relevant details.
* **Sections**¹: Import individual course section information from Brightspace, including dates, instructor names, etc.
* **Enrollments**: Import student enrollment records from Brightspace, including student grades

  + **Match Student Contacts**²: Add enrollments for students already in the Element451 database
  + **Insert Student Contacts**: Create new contacts for students previously not found in Element451, and add their enrollments
  + **Update Student Contacts**: Overwrite existing contact data with data found in Brightspace, such as name and email

¹*Setting is required and cannot be disabled.*

²*Setting is required when Enrollments is enabled.*

## Settings

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613877082/05e3e74ee696da335cf82d4b06fb/CleanShot+2025-07-10+at+15_34_27%402x.png?expires=1784333700&signature=3d72c63629118ec17e5548acf4668d6845b8bc1a5c7a4340b13084cfe94a1f55&req=dSYmFcF5moFXW%2FMW1HO4zQPQcXa4%2FbMEnB9vOARbInVOcrQSxmxnlTHI3zCL%0A%2Faa1dmcXiGskONCoL4k%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613877082/05e3e74ee696da335cf82d4b06fb/CleanShot+2025-07-10+at+15_34_27%402x.png?expires=1784333700&signature=3d72c63629118ec17e5548acf4668d6845b8bc1a5c7a4340b13084cfe94a1f55&req=dSYmFcF5moFXW%2FMW1HO4zQPQcXa4%2FbMEnB9vOARbInVOcrQSxmxnlTHI3zCL%0A%2Faa1dmcXiGskONCoL4k%3D%0A)

* **Target Semesters**: Only data from courses with a section within the selected semesters will be imported.
* **Auto Import Semesters**: When enabled, Element451 will automatically sync the selected resources (courses, sections, or enrollments) for new semesters that are added to the LMS.
* **Target Teacher Roles**: Brightspace supports multiple roles for teachers. Select the roles you use for teachers in your Brightspace instance.
* **Target Student Roles**: Brightspace supports multiple roles for students. Select the roles you use for students in your Brightspace instance.

## Matching Student Contact Criteria

The Brightspace LMS integration reads student data from Brightspace and matches to Element records using the following fields:

* user-identities-brightspaceid
* user-identities-school-email
* user-identities-email

If a match can not be determined, the integration will either insert a new student record in Element451 or not depending on the data sync preferences.

## Inserting or Updating Student contacts

The following fields will be populated by the integration when inserting or updating contacts based on Brightspace student data:

* user-first-name
* user-last-name
* user-email-address
* user-preferred-name
* user-sources-source-type = "LMS"
* user-sources-source-name = "Brightspace"
* user-sources-source-date

---

# Step 5: Configure Course Data Source Mappings

After authenticating your Brightspace integration, you must configure value mappings for course dropdown fields before they'll appear in Element451.

1. Navigate to **Data + Automation → Data Sources → Regular Data Sources** and search for **[COURSES]**.
2. For each of the following, add at least one value–label mapping pair:

   * [COURSES] Course Subjects
   * [COURSES] Course Categories
   * [COURSES] Course Statuses
   * [COURSES] Course Grading
   * [COURSES] Course Departments

**Important Notes:**

* 📌 To avoid blank fields, add a mapping for every value you expect to appear. Any imported value without a matching mapping will display as empty—adding just one pair will make the dropdown render, but records with unmapped values will still show blank.
* 📌 Departments is the only field where Brightspace provides the values, but you still need to configure the mappings in Data Sources. For Subject, Category, Status, and Grading, Brightspace sends no data; you'll define the value list manually based on your institution's course taxonomy.

---

# Next Steps

Once your Brightspace integration is authenticated, Element451 will automatically start syncing academic data. This data lives in [Courses](https://help.element451.com/en/articles/10420398-getting-started-with-courses) (**Data + Automation** > **Courses**), where you can view course records from your LMS.

Now that your course data is flowing into Element, you can begin using it to:

* Build targeted segments
* Trigger workflows + communications
* Assign tasks or academic support resources
* Personalize student experiences in StudentHub

To explore how to make the most of your LMS data, check out our [Getting Started with Courses](https://help.element451.com/en/articles/10420398-getting-started-with-courses) article.

---

# Field Mapping

Once your LMS integration is active, Element451 automatically syncs data from your system into organized, consistent fields. This eliminates manual data entry while ensuring all information flows seamlessly between platforms.

Element451 automatically creates data sources for your course data directly from your LMS. No manual setup required—everything is generated automatically during the integration process.

The tables below show exactly which LMS fields map to which Element451 fields:

## Course

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Brightspace Object** | **Brightspace Field** |
| Institution ID | template | Identifier |
| Name | template | Name |
| Code | template | Code |
| Departments¹  -Institution ID  -Name | course  course  course | Multiple values supported  -Department->Identifier  -Department->Name |
| Term² | course | Semester->Code |
| Description | - | *Not available* |
| Subject | - | *Must be defined manually via Data Sources* |
| Number | - | *Not available* |
| Credits | - | *Not available* |
| Version | - | *Not available* |
| Total Students | - | *Not available* |
| Grading | - | *Not available* |
| Status | - | *Not available* |
| Type | - | *Not available* |
| Timezone | - | *Not available* |

## Section

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Brightspace Object** | **Brightspace Field** |
| Institution ID | se|co³ | Identifier |
| Code | se|co³ | Code |
| Status¹ | course | IsActive |
| Term² | course | Semester->Code |
| Instructor¹ | user | FirstName + LastName |
| Instructor Email | user | ExternalEmail |
| Start Date | course | StartDate |
| End Date | course | EndDate |
| Instruction Mode | - | *Not available* |
| School | - | *Not available* |
| Section Type | - | *Not available* |
| Version | - | *Not available* |
| Campus | - | *Not available* |
| Total Meetings | - | *Not available* |
| Max Enrollment | - | *Not available* |
| Current Enrollments | - | *Not available* |
| Timezone | - | *Not available* |
| Times | - | *Not available* |

## Enrollment

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Brightspace Object** | **Brightspace Field** |
| Enrollment Status¹ | enrollment | IsActive |
| Current Grade (Text) | - | Calculated⁴ |
| Current Grade (Number) | - | Calculated⁴ |
| Final Grade (Text) | - | Calculated⁴ |
| Final Grade (Number) | - | Calculated⁴ |
| Last LMS Activity | enrollment | LastAccessed |
| Institution ID | - | *Not available* |
| Last Attended Date | - | *Not available* |
| Total Active Time | - | *Not available* |
| Total Absences | - | *Not available* |

¹ Automatically creates a data source in Element451  
² Matched against existing terms in Element451 using term code  
³ Uses section data if available, otherwise falls back to course data  
⁴ Calculated automatically by Element451 (see Calculation Logic below for details)

---

# Brightspace Grade Calculation Logic

Element451 retrieves both *calculated* and *adjusted* grades from Brightspace for each user’s course section. Based on the section’s status and the type of grade available, the system determines where to store the grade values.

### Grade Logic Explained

#### Step 1: Check if the section is open or closed

* A section is considered **open** if:

  + Its **status is active**, **and**
  + Today’s date falls between the section’s **start** and **end** dates.  
    ​

  If either condition is not met, the section is considered **closed.**

#### Step 2: Determine which grade to save and where

* **If the section is open:**

  + If an **adjusted grade** is available → save it to the `current_grade` field.
  + If no adjusted grade but a **calculated grade** is available → save it to the `current_grade` fields.
  + Save to:

    - `current_grade_text` if the grade is text
    - `current_grade_number` if the grade is numeric
* **If the section is closed:**

  + If an **adjusted grade** is available → save it to the `final_grade` fields.
  + If no adjusted grade but a **calculated grade** is available → save it to the `final_grade` fields.
  + Save to:

    - `final_grade_text` if the grade is text
    - `final_grade_number` if the grade is numeric

---

# ⚠️ Important: Term Code Mapping

For term information to display correctly on course and enrollment data, you must map your Brightspace term codes to the corresponding terms in Element451.

The integration imports term codes from Brightspace, but Element451 needs to know which term each code corresponds to. Without this mapping, the term field will be empty and you won't be able to filter or segment by term.

## How to Add Term Codes

* **Via** **Integration** **Codes** **tab:** Navigate to your Terms data source, edit a term, open the "Integration Codes" tab, and add a new code with type brightspace. Enter the exact term code from Brightspace as the value.
* **Via** **CSV** **Import:** Export your Terms, add a column with the header brightspace, populate it with the matching Brightspace term codes, and re-import.

## Finding Your Brightspace Term Codes

Term codes in Brightspace typically follow patterns like `sem_2025FA` or `2025_Fall_Semester`. Check your Brightspace semester settings for the exact codes.

🚨 **Important:** The code must exactly match what's in Brightspace. After adding the codes, term data will resolve on the next daily sync.

---

# Reviewing Imported Semesters

To review your imported semester data, navigate to **Settings** > **Integrations** and click on your LMS from the left-hand menu.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613884406/28ce8774883ee1fad578f207c465/CleanShot+2025-07-10+at+15_37_22%402x.png?expires=1784333700&signature=d63ba0286a6affcb3eb8a5220a3389513660da1215427536946e6fc4d09be808&req=dSYmFcF2mYVfX%2FMW1HO4zWc5xCFZ49O1fIxR5qVb6YGVi2O%2FSN0DQGznhEJR%0Ah7MM6k2OVFloeMW90hI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613884406/28ce8774883ee1fad578f207c465/CleanShot+2025-07-10+at+15_37_22%402x.png?expires=1784333700&signature=d63ba0286a6affcb3eb8a5220a3389513660da1215427536946e6fc4d09be808&req=dSYmFcF2mYVfX%2FMW1HO4zWc5xCFZ49O1fIxR5qVb6YGVi2O%2FSN0DQGznhEJR%0Ah7MM6k2OVFloeMW90hI%3D%0A)

On the **Imported Semesters** card, you'll see:

* Semester
* Status
* Added At
* Started At
* Last Sync Completed At

---

🚨 **Important:** Brightspace does not support real-time syncing. Data will update once daily during an overnight sync.

---