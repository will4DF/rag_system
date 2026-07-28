---
title: Courses Native Integration: Blackboard Learn LMS
url: https://help.element451.com/en/articles/11199263-courses-native-integration-blackboard-learn-lms
collection: Integrations
---

# Overview

The Blackboard LMS integration seamlessly syncs academic and enrollment data from Blackboard Learn into Element451. This guide will walk you through the setup process, from configuring Blackboard Learn settings to completing the integration within Element451.

Element451’s Blackboard integration is built for Blackboard Learn. While much of the underlying architecture is shared with Blackboard Ultra and may work depending on your setup, the integration has not been fully validated for Ultra and may produce unexpected results.

📌 **Note:** This is a one-way integration. Element451 reads data from Blackboard Learn but **does not** write back any data.

## Overview of the Setup Process

To get started, you'll work through three steps outlined below in detail.

1. [Configure Learn User (Service Account) Permissions](#h_0fd9a2281a)
2. [Set Up OAuth Authentication in Blackboard](#h_50934fb208)
3. [Provide Credentials to Element451](#h_3b5972d631)
4. [Authenticate the Integration](#h_4312019199)

---

# Step 1: Configure Learn User (Service Account) Permissions

The **Learn User**, often called a **service account**, is a dedicated Blackboard user account that an integration uses to authenticate against the Learn REST APIs. When you register a REST Application in Blackboard, you must associate it with a specific Learn User. That user’s permissions determine what the Element451 integration can see and do inside Blackboard.  
​  
You can use an existing Learn User, but we recommend having a dedicated service account for your Element451 integration.

## Why set it up?

* **Security & least privilege**: Using a service account allows you to grant only the exact privileges the integration needs (e.g., read access to Courses, Users, Memberships, and Grades) without exposing an administrator’s full rights.
* **Reliability**: The service account is not tied to a real person’s login. This means the integration won’t break if someone leaves the institution, changes roles, or has their personal account disabled.
* **Auditability**: All API activity is clearly logged as coming from the service account, making it easier to track and monitor integration behavior.
* **Maintainability**: Credentials and permissions for integrations can be rotated or adjusted independently of staff accounts, simplifying support.

## Required User Permissions

* **Courses**

  + Course/Organization Control Panel (Users and Groups) → View Enrollments
  + Course/Organization Control Panel (Customization) → View Course Settings
* **Users**

  + System User Management → Users → View
* **Memberships**

  + Course/Organization Control Panel (Users and Groups) → View Enrollments
* **Orgnaizations**

  + Organization Control Panel → View Enrollments
  + Organization Control Panel → View Settings
* **Grades**

  + Course/Organization Control Panel (Grade Center) → View Grades
* **Roles**

  + System Administration → Courses/Organizations → Course/Organization Roles → View

---

# Step 2: Set Up OAuth Authentication in Blackboard

To allow secure communication between Blackboard and Element451, you'll first need to **register a REST API application** in Blackboard. This generates a Client ID and Client Secret you'll use later in the setup.

1. Log in to your Blackboard account as a **System Administrator**.
2. Navigate to **System Admin** > **Integrations** > **REST API Integrations**.
3. Click **Create Integration**.
4. Fill in the required information:

   * **Application ID**: `f7835300-48bb-4051-b8a8-e43af1c7edc0`
   * **Learn User**: Select a user (service) account with sufficient read permissions (usually an admin-level service account)
   * **End User Access**: Set to **No**
   * **Authorized To Act As User?**: Set to **No**
5. Click **Submit to Proceed**

🔗 For more detailed instructions, see Blackboard's guide on [Registering an Application](https://developer.blackboard.com/portal/displayApi/admin#registration).

---

# Step 3: Authenticate the Integration in Element451

Once you have registered your application in Blackboard, you'll need to authorize Element451 to access your Blackboard data using OAuth.

🚨 **Important:** The user performing the authentication must be a Blackboard System Administrator and have read access to: Courses, Users, Memberships, Organizations, and Grades.

1. Click on your avatar/profile picture in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Integrations**.
3. From the left-hand menu, select **Blackboard LMS.**
4. Click the **Authenticate** button and follow the prompts.

You'll need your Blackboard Instance URL (typically something like [`https://youruniversity.blackboard.com`](https://youruniversity.blackboard.com)).

---

# Step 4: Configure Preferences

Once you've authenticated your integration, you can access the LMS integration settings.

To review and adjust your preferences, **click the pencil icon** in the top right corner of your LMS integration card.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613801801/4de1688e77d5994adf26da7f7eba/CleanShot+2025-07-10+at+14_50_48%402x.png?expires=1784333700&signature=19d4fe4da5a6cbeb554fd30ee10b4789c78bfc71bc1f37fb539ee171e11e59e2&req=dSYmFcF%2BnIlfWPMW1HO4zSMkL%2FWgeVreCH8T6xu8HuX4lI439dMGxVHWcMvn%0AOESRSNhJhbPZkz5Y4rw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613801801/4de1688e77d5994adf26da7f7eba/CleanShot+2025-07-10+at+14_50_48%402x.png?expires=1784333700&signature=19d4fe4da5a6cbeb554fd30ee10b4789c78bfc71bc1f37fb539ee171e11e59e2&req=dSYmFcF%2BnIlfWPMW1HO4zSMkL%2FWgeVreCH8T6xu8HuX4lI439dMGxVHWcMvn%0AOESRSNhJhbPZkz5Y4rw%3D%0A)

## Data Sync Preferences

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613821856/19ae3826546c2fbb2db8e35a68d2/CleanShot%2B2025-07-10%2Bat%2B15_03_17-402x.png?expires=1784333700&signature=193e6038842dc0729b350b120e4f16654b0bbbb65f88e0a8f84a597dc08b22fd&req=dSYmFcF8nIlaX%2FMW1HO4zYxjSqprx2XPSJYDhqHhk5cdjP27sqOzI91vhwCp%0ABnzqunhYUlFzeqfIL8Q%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613821856/19ae3826546c2fbb2db8e35a68d2/CleanShot%2B2025-07-10%2Bat%2B15_03_17-402x.png?expires=1784333700&signature=193e6038842dc0729b350b120e4f16654b0bbbb65f88e0a8f84a597dc08b22fd&req=dSYmFcF8nIlaX%2FMW1HO4zYxjSqprx2XPSJYDhqHhk5cdjP27sqOzI91vhwCp%0ABnzqunhYUlFzeqfIL8Q%3D%0A)

* **Courses**¹: Import course information from Blackboard, including course name, code, department, and other relevant details.
* **Sections**¹: Import individual course section information from Blackboard, including dates, instructor names, etc.
* **Enrollments**: Import student enrollment records from Blackboard, including student grades

  + **Match Student Contacts**²: Add enrollments for students already in the Element451 database
  + **Insert Student Contacts**: Create new contacts for students previously not found in Element451, and add their enrollments
  + **Update Student Contacts**: Overwrite existing contact data with data found in Blackboard, such as name and email

¹*Setting is required and cannot be disabled.*

²*Setting is required when Enrollments is enabled.*

## Settings

* **Target Semesters**: Only data from courses with a section within the selected semesters will be imported.
* **Auto Import Semesters**: When enabled, Element451 will automatically sync the selected resources (courses, sections, or enrollments) for new semesters that are added to the LMS.
* **Target Teacher Roles**: Blackboard supports multiple roles for teachers. Select the roles you use for teachers in your Blackboard instance.
* **Target Student Roles**: Blackboard supports multiple roles for students. Select the roles you use for students in your Blackboard instance.

## Matching Student Contact Criteria

The Blackboard Learn LMS integration reads student data from Blackboard and matches to Element records using the following fields:

* user-identities-blackboardid
* user-identities-school-email
* user-identities-email

If a match can not be determined, the integration will either insert a new student record in Element451 or not depending on the data sync preferences.

## Inserting or Updating Student contacts

The following fields will be populated by the integration when inserting or updating contacts based on Blackboard data:

* user-first-name
* user-last-name
* user-email-address
* user-preferred-name
* user-sources-source-type = "LMS"
* user-sources-source-name = "Blackboard"
* user-sources-source-date

---

# Next Steps

Once authentication is complete, Element451 will begin syncing data from Blackboard. This data lives in [Courses](https://help.element451.com/en/articles/10420398-getting-started-with-courses) (**Data + Automation** > **Courses**), where you can view course records from your LMS.

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
| **Element451 Field** | **Blackboard Object** | **Blackboard Field** |
| Institution ID | course | id |
| Name | course | name |
| Description | course | description |
| Code | course | courseId |
| Status¹ | course | availability->available |
| Term² | course | termId |
| Subject | - | *Not available* |
| Number | - | *Not available* |
| Credits | - | *Not available* |
| Version | - | *Not available* |
| Total Students | - | *Not available* |
| Departments | - | *Not available* |
| Grading | - | *Not available* |
| Type | - | *Not available* |
| Timezone | - | *Not available* |

## Section

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Blackboard Object** | **Blackboard Field** |
| Institution ID | course | id |
| Code | course | code |
| Status¹ | course | status |
| Instruction Mode¹ | course | type |
| Term² | course | termId |
| Instructor¹ | user | name->given + name->family |
| Instructor Email | user | contact->email |
| School | - | *Not available* |
| Section Type | - | *Not available* |
| Version | - | *Not available* |
| Campus | - | *Not available* |
| Total Meetings | - | *Not available* |
| Max Enrollment | - | *Not available* |
| Current Enrollments | - | *Not available* |
| Timezone | - | *Not available* |
| Start Date | - | *Not available* |
| End Date | - | *Not available* |
| Times | - | *Not available* |

## Enrollment

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Blackboard Object** | **Blackboard Field** |
| Institution ID | enrollment | id |
| Final Grade (Text) | - | Calculated³ |
| Final Grade (Number) | - | Calculated³ |
| Last LMS Activity | enrollment | lastAccessed |
| Enrollment Status | - | *Not available* |
| Current Grade (Text) | - | *Not available* |
| Current Grade (Number) | - | *Not available* |
| Last Attended Date | - | *Not available* |
| Total Active Time | - | *Not available* |
| Total Absences | - | *Not available* |

¹ Automatically creates a data source in Element451  
² Matched against existing terms in Element451 using the term's **Blackboard integration code** (see [Matching Blackboard Terms to Element451](#h_bbterm) below)

³ Calculated automatically by Element451 (see Calculation Logic below for details)

## Blackboard Grade Calculation Logic

This logic handles how a student’s final grade is saved based on the type of grading scale used in Blackboard. The system supports multiple grading types, including Percent, Score, Letter, Tabular, Text, and Complete/Incomplete. **Note:** This logic applies only to final grades.

### Grade Logic Explained

#### Step 1: Pull grade data

The system attempts to retrieve:

* **Score**: the numeric value the student earned
* **Possible**: the total possible points
* **Text**: a grade label like “A” or “Complete”
* **Scale type**: defines how to interpret the grade

#### Step 2: Process based on the grading scale type

**Percent**:

* If a score exists and the possible points are greater than 0:

  + Calculate a percentage: (score / possible) \* 100
  + Save this to `final_grade_number` (rounded to 2 decimals)
  + Save the formatted version (e.g., “87.50%”) to `final_grade_text`

**Score**:

* If a score exists:

  + Save the numeric score to `final_grade_number` (rounded to 2 decimals)
  + Save the same number (e.g., “87.50”) as text in `final_grade_text`

**Letter**:

* If a text grade exists:

  + Save the text (e.g., “A” or “B+”) to `final_grade_text`

**Tabular**:

* If a score and possible points are available:

  + Calculate and save the percentage to `final_grade_number`
* If a text grade is available:

  + Save the text to `final_grade_text`

**Text** or **Complete**/**Incomplete**:

* If a text grade exists:

  + Save the text to `final_grade_text`

**Doesn’t match any of the above:**

* No action is taken

---

# Matching Blackboard Terms to Element451

When course and section data syncs from Blackboard, Element451 matches each record to an existing term in your account so it can be used for filtering and segmentation. This match is made using the term's **Blackboard integration code**—not the term's standard code.

🚨 **Important:** You must add a **Blackboard integration code** to each term you want to sync. Element451 does not fall back to the standard term code—even when it's identical to the Blackboard value. If a term has no Blackboard integration code, its courses and sections will sync in with **No Term**, which prevents you from filtering or segmenting on them.

The Blackboard integration code must exactly match the term's `termId` in Blackboard. To add it:

1. Navigate to **Data + Automations** > **Data Sources** > **Terms**.
2. Click the **pencil icon** next to the term to open the editor.
3. Select the **Integration Code** tab.
4. Click **+ Add Code**, choose **Blackboard** from the "With" menu, and enter the term's Blackboard `termId` as the value.
5. Click **Done**. Term data will resolve on the next daily sync.

For more on adding and importing integration codes, see [Setting up Integration Codes](https://help.element451.com/en/articles/5181322-setting-up-integration-codes).

---

# Reviewing Imported Semesters

To review your imported semester data, navigate to **Settings** > **Integrations** and click on your LMS from the left-hand menu.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613885831/11b526e37419749f9efe9d3de532/CleanShot%2B2025-07-10%2Bat%2B15_37_22-402x.png?expires=1784333700&signature=f94e231a47b1e2815a0c2f06f64df28294ebf9d32e8141c672a94c0bf9ce9ebf&req=dSYmFcF2mIlcWPMW1HO4zVQAV1n7lOIfPf%2BeSosT7JNl2jGygdOsaWlSA23c%0AuHuyDHFIN3kp0fR%2BQJ8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613885831/11b526e37419749f9efe9d3de532/CleanShot%2B2025-07-10%2Bat%2B15_37_22-402x.png?expires=1784333700&signature=f94e231a47b1e2815a0c2f06f64df28294ebf9d32e8141c672a94c0bf9ce9ebf&req=dSYmFcF2mIlcWPMW1HO4zVQAV1n7lOIfPf%2BeSosT7JNl2jGygdOsaWlSA23c%0AuHuyDHFIN3kp0fR%2BQJ8%3D%0A)

On the **Imported Semesters** card, you'll see:

* Semester
* Status
* Added At
* Started At
* Last Sync Completed At

---