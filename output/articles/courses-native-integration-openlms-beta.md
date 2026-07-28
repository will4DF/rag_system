---
title: Courses Native Integration: OpenLMS [Beta]
url: https://help.element451.com/en/articles/13195039-courses-native-integration-openlms-beta
collection: Integrations
---

📌 **Note:** This feature is currently in Beta. For access, reach out to your account manager or live support.

# Overview

The OpenLMS integration seamlessly syncs real-time academic and enrollment data from OpenLMS into Element451. This guide will walk you through the setup process, from configuring OpenLMS settings to completing the integration within Element451.

📌 **Note:** This is a one-way integration. Element451 reads data from OpenLMS but **does not** write back any data.

---

# Step 1: Add Element451 as External Service in OpenLMS

To allow secure communication between OpenLMS and Element451, you’ll need to add Element451 as an External Service in OpenLMS. This will allow you to generate a token that you'll use later in the setup.

🚨 **Important:** The instructions below are ***illustrative*** ***and may not reflect the latest OpenLMS interface or workflow***. We recommend referring to the OpenLMS documentation for authoritative steps on setting up external services and generating access tokens.

## 1) Enabling Web Services

1. Access **Administration** > **Site** **Administration** > **Advanced** **Features**
2. Check **Enable Web Services**
3. Click "**Save** **Changes**"

## 2) Enabling REST Protocol

1. Access **Administration** > **Site** **Administration** > **Server** > **Web** **Services** > **Manage** **Protocols**
2. Enable the "**REST Protocol"**

## 3) Creating a Custom External Service

1. Access **Administration** > **Site** **Administration** > **Server** > **Web** **Services** > **External Services**
2. Click "**Add New Custom Service**"

   * "***Authorized Users Only***" - If enabled, you will need to select the authorized users manually. Otherwise all users with appropriate permissions are allowed
   * "***Required*** ***Capability***" - If enabled, any user accessing the web service will be checked against this selected capability. (This is just an additional optional security layer.)
3. Enter a name (“Element451 Integration”) and check "**Enabled**"
4. Click '**Add** **Service**'

## 4) Adding Functions to the Service

Once the external service as been created, you will need to add web service functions. Your choice will be dictated by what you allow the external application to do.

1. Select **Add Functions** (or **Create Group**, depending on your OpenLMS version)

The following are required functions for the integration to function properly:

* `core_course_get_categories`
* `core_course_get_courses_by_field`
* `core_enrol_get_enrolled_users`
* `gradereport_user_get_grade_items`

## 5) Enabling Required Capabilities

The final step on the OpenLMS side is to grant the appropriate permissions to the **role and user** that Element451 will authenticate as. There are **two layers** of permissions, and both are required.

#### **A. Web Service Access: Allows the Service User to Connect.**

Ensure the token user's role has these capabilities **allowed**:

* `moodle/webservice:createtoken`  
  ​*Allows the user to generate a web service token*
* `webservice/rest:use`   
  ​*Allows use of the REST protocol*

#### **B. Data-Access Capabilities: Allows the Service User Actually Read Your Data**

Registering the four functions on the service is **not** enough — the token user must also hold the capability each function checks at runtime, **in the context of the courses being synced**. Grant the following to the token user's role:

|  |  |  |
| --- | --- | --- |
| **Function** | **Required capability** | **What it reads** |
| `core_course_get_categories` | `moodle/category:viewcourselist` | Course categories (semesters) |
| `core_course_get_courses_by_field` | `moodle/course:view` | Courses |
| `core_enrol_get_enrolled_users` | `moodle/course:viewparticipants` (+ `moodle/user:viewdetails`) | Enrolled students/teachers |
| `gradereport_user_get_grade_items` | `gradereport/user:view` **and** `moodle/grade:viewall` | Student grades |

🚨 **Important — the token service user must be a real, non-guest user with a role in the synced courses.** The grade and participant endpoints run through OpenLMS's standard course-access check. If the token user has no role in a course, OpenLMS treats it as a *guest* and rejects the call (`guestsarenotallowed`), even when the capabilities above are granted globally. Assign the token user's role at the **system level** (so it applies to all courses) or ensure the user is enrolled in / has a role in every course you intend to sync. Grades are read per-user, so `moodle/grade:viewall` is required to read grades for students other than the token user itself.

## 6) Generate a Web Service Token

After the external service and required permissions are configured, you’ll need to generate a web service token for the user that Element451 will authenticate as.

1. Navigate to **Administration > Site Administration > Server > Web Services > Manage Tokens**
2. Click **Add**
3. Select the authorized user
4. Select the **Element451 Integration** service
5. Ensure the **REST protocol** is selected
6. Click **Save**

Copy the generated token and store it securely. You’ll use this token when completing the Element451 setup (explained in the next section).

---

# Step 2: Authenticate the Integration in Element451

Once you have registered Element451 in OpenLMS, you'll need to authorize Element451 to access your OpenLMS data using OAuth.

🚨 **Important:** The user performing the authentication must be an OpenLMS Administrator and have the necessary permissions/access.

1. Click on your avatar/profile picture in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Integrations**.
3. From the left-hand menu, select **Open LMS.**
4. Fill in the required details:

   * Token

     + *The Token is an access token for your OpenLMS LMS account.*
   * Instance URL

     + *The Instance URL is the URL of your OpenLMS LMS account.*
5. Click **Connect.**

---

# Step 4: Configure Preferences

Once you've authenticated your integration, you can access the LMS integration settings.

To review and adjust your preferences:

1. Click on your avatar/profile picture in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Integrations**.
3. From the left-hand menu, select **Open LMS.**
4. Click **Settings** to the right of your Instance URL.

## Details Tab

The details tab shows you:

**General Details**

* Active status
* Instance URL
* Created date
* Updated date
* Created by user

**Permissions**

* Instance URL
* Overall status
* Last status check timestamp
* Endpoints checked and their status
* Option to run a "check" by clicking the "Check" button in the top right corner

## Sync Preferences Tab

### Sync Settings

📌 **Note:** *OpenLMS does not support realtime syncs. Instead, Element451 will sync with your OpenLMS data approximately every 12 hours.*

These settings determine how data in OpenLMS maps into Element451. Read more in our help center.

* **Import Engagement**

  + *Import engagement data from OpenLMS for the student enrollments imported by your integration.*
* **Import Grades**

  + *Import grades from OpenLMS for the student enrollments imported by your integration.*
* **Import Attendance**

  + *Import attendance data from OpenLMS for the student enrollments imported by your integration.*

### Student Roles

OpenLMS does not allow us to get a list of roles using their API, so they need to be inputted manually. Click the "**+ Add Student Role**" and add the relevant student role ID(s).

### Teacher Roles

OpenLMS does not allow us to get a list of roles using their API, so they need to be inputted manually. Click the "**+ Add Teacher Role**" and add the relevant teacher role ID(s).

### Imported Semesters

Click the "+" button to import a semester of data from OpenLMS.

### Auto Import Semesters?

When enabled, Element451 will automatically sync the selected resources (courses, sections, or enrollments) for new semesters that are added to the LMS.

---

# Next Steps

Once authentication is complete, Element451 will begin syncing data from OpenLMS based on your configuration. This data lives in [Courses](https://help.element451.com/en/articles/10420398-getting-started-with-courses) (**Data + Automation** > **Courses**), where you can view course records from your LMS.

Now that your course data is flowing into Element, you can begin using it to:

* Build targeted segments
* Trigger workflows + communications
* Assign tasks or academic support resources
* Personalize student experiences in StudentHub

To explore how to make the most of your LMS data, check out our [Getting Started with Courses](https://help.element451.com/en/articles/10420398-beta-getting-started-with-courses) article.

---

# Field Mapping

Once your LMS integration is active, Element451 automatically syncs data from your system into organized, consistent fields. This eliminates manual data entry while ensuring all information flows seamlessly between platforms.

Element451 automatically creates data sources for your course data directly from your LMS. No manual setup required—everything is generated automatically during the integration process.

The tables below show exactly which LMS fields map to which Element451 fields:

## Course

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **OpenLMS Object** | **OpenLMS Field** |
| Institution ID | course | id |
| Name | course | name |
| Description | *Not available* | *Not available* |
| Code | *Not available* | shortname |
| Total Students | *Not available* | *Not available* |
| Departments -Institution ID -Name | *Not available* | *Not available* |
| Status | *Not available* | *Not available* |
| Type | *Not available* | *Not available* |
| Term² | course | From shortname if available courseCode.termCode |
| Timezone | *Not available* | *Not available* |
| Subject | *Not available* | *Not available* |
| Number | *Not available* | *Not available* |
| Credits | *Not available* | *Not available* |
| Version | *Not available* | *Not available* |
| Grading | *Not available* | *Not available* |

## Section

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **OpenLMS Object** | **OpenLMS Field** |
| Institution ID | course | id |
| Code | course | shortname |
| Status | *Not available* | *Not available* |
| Instruction Mode | *Not available* | *Not available* |
| Term² | course | From shortname if available courseCode.termCode |
| School | *Not available* | *Not available* |
| Instructor¹ | user | first\_name + last\_name |
| Instructor Email | user | email |
| Current Enrollments | *Not available* | *Not available* |
| Timezone | *Not available* | *Not available* |
| Start Date | course | startdate |
| End Date | course | enddate |
| Section Type | *Not available* | *Not available* |
| Version | *Not available* | *Not available* |
| Campus | *Not available* | *Not available* |
| Total Meetings | *Not available* | *Not available* |
| Max Enrollment | *Not available* | *Not available* |
| Times | *Not available* | *Not available* |

## Enrollment

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **OpenLMS Object** | **OpenLMS Field** |
| Institution ID | enrollment | id |
| Enrollment Status | *Not available* | *Not available* |
| Current Grade (Text) | *Not available* | *Not available* |
| Current Grade (Number) | *Not available* | *Not available* |
| Final Grade (Text) | *Not available* | *Not available* |
| Final Grade (Number) | *Not available* | *Not available* |
| Last LMS Activity | enrollment | lastaccess |
| Last Attended Date | *Not available* | *Not available* |
| Total Active Time | *Not available* | *Not available* |
| Total Absences | *Not available* | *Not available* |

¹ Automatically creates a data source in Element451  
² Matched against existing terms in Element451 using the term's **OpenLMS integration code** (see [Matching OpenLMS Terms to Element451](#h_olterm) below)

---

# Matching OpenLMS Terms to Element451

When course and section data syncs from OpenLMS, Element451 matches each record to an existing term in your account so it can be used for filtering and segmentation. This match is made using the term's **OpenLMS integration code**—not the term's standard code.

🚨 **Important:** You must add an **OpenLMS integration code** to each term you want to sync. Element451 does not fall back to the standard term code—even when it's identical to the OpenLMS value. If a term has no OpenLMS integration code, its courses and sections will sync in with **No Term**, which prevents you from filtering or segmenting on them.

The OpenLMS integration code must match the term code OpenLMS derives from the course `shortname` (`courseCode.termCode`). To add it:

1. Navigate to **Data + Automations** > **Data Sources** > **Terms**.
2. Click the **pencil icon** next to the term to open the editor.
3. Select the **Integration Code** tab.
4. Click **+ Add Code**, choose **OpenLMS** from the "With" menu, and enter the term code as the value.
5. Click **Done**. Term data will resolve on the next sync.

For more on adding and importing integration codes, see [Setting up Integration Codes](https://help.element451.com/en/articles/5181322-setting-up-integration-codes).

---

# Reviewing Imported Semesters

To review your imported semester data:

1. Navigate to **Settings** > **Integrations**.
2. From the left-hand menu, select **Open LMS.**
3. Click **Settings** to the right of your Instance URL.
4. Click the "**Sync Preferences**" tab.
5. On the **Imported Semesters** card, you'll see:

   * Semester
   * Status
   * Added At
   * Started At
   * Last Sync Completed At

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1894344437/bd3ea13ba5e581379d632d06c388/CleanShot-2B2025-07-10-2Bat-2B15_37_22-402x.png?expires=1784333700&signature=0b7dbb9562f0cb17518da9a6395fdf40db63bcc3d934a15ea5460cc6d5732a4e&req=dSguEsp6mYVcXvMW1HO4zb4vVL%2BeXJO3J%2B1nw0GOUXSo1dlkU1Sh%2B9Z2xJj%2F%0A6%2BIdjLvdxQg6DSQ%2BLcc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1894344437/bd3ea13ba5e581379d632d06c388/CleanShot-2B2025-07-10-2Bat-2B15_37_22-402x.png?expires=1784333700&signature=0b7dbb9562f0cb17518da9a6395fdf40db63bcc3d934a15ea5460cc6d5732a4e&req=dSguEsp6mYVcXvMW1HO4zb4vVL%2BeXJO3J%2B1nw0GOUXSo1dlkU1Sh%2B9Z2xJj%2F%0A6%2BIdjLvdxQg6DSQ%2BLcc%3D%0A)

---