---
title: Courses Integration: Ethos for Banner + Colleague
url: https://help.element451.com/en/articles/11586099-courses-integration-ethos-for-banner-colleague
collection: Integrations
---

# Overview

The Ethos Integration allows you to sync student data from your SIS—Banner or Colleague—directly into Element451. This integration is ideal for institutions that use these systems as their system of record, especially for academic and enrollment-related data.

Ethos can bring in a broad range of student information, depending on what’s stored in your SIS. This might include:

* Student profile data (e.g., type, status, ID)
* Enrollment and registration details (terms, course sections)

💡 **Pro Tip:** If you also use OpenLMS you can integrate both systems. Element451 is designed to sync data from each source appropriately based on where that data lives. If there is overlapping data, the SIS will always be treated as the authoritative source. LMS data supplements where appropriate but will not override SIS values.

🚨 **Important:** At this time, only OpenLMS can be synced along side the Ethos integration. We plan on adding this functionality to bring our other LMS systems to parity with OpenLMS.

---

# Integration Setup

Element451’s Ethos integration supports both **Banner** and **Colleague**. Configuration steps vary slightly depending on which SIS you're using. Select the setup path below based on your institution's system:

## Colleague

### Step 1: Set Up Your Ethos Proxy User

Before connecting to Element451, you’ll need to configure a proxy user in Colleague for Ethos to use.

📌 **Note:** You can use the same user as your baseline Ethos configuration or create a new one, depending on your internal security policies.

1. On **SCD**: Define a **Security Class** for this user.
2. On **SOD**: Create an **Opers Equivalent**, using the Security Class from above.
3. On **NAE**: Create a **PERSON record** and note the Person ID.
4. On **DRUS**: Register the user and note the username.
5. Use **CCDF/CCSU** to set a secure password for this account.

---

### Step 2: Configure Required Permissions in Colleague

Use the **MRPR screen** in Colleague to assign necessary permissions to the proxy user. Attach these permissions to the user via **AROR**, ensuring you set a **start date**.

#### Required Permissions

* VIEW.STUDENT.TRANSCRIPT.GRADES
* VIEW.STUDENT.INFORMATION
* VIEW.STUDENT.ACADEMIC.PROGRAM
* VIEW.STUDENT.ACADEMIC.PERIODS
* VIEW.STUDENT.ACADEMIC.CREDENTIALS
* VIEW.SECTION.ROSTER
* VIEW.SECTION.INSTRUCTORS
* VIEW.SECTION.GRADING
* VIEW.SECTION.ATTENDANCE
* VIEW.REGISTRATIONS
* VIEW.ANY.PERSON

🚨 **Important:** Permissions that are missing or misconfigured may cause the integration to fail or partially sync. You can check the status in Element451 once connected.

---

### Step 3: Create an Application in Ethos

To enable Element451 to communicate with your Colleague instance via Ethos:

1. Log in to **Ethos**.
2. Navigate to the **Applications** tab and click **Create New App: Manually**.
3. **Check** the box for **Configure REST API Proxy** and click **Continue**.
4. Enter the following details:

   * **Application Name:** Element451 Courses
   * **Description:** Element451 Courses integration application
5. Click **Next** and choose **Add Source Application**.
6. Select your **Colleague WebAPI application** (name may vary by school).
7. Provide the **Colleague proxy username/password** from earlier.
8. Click **Add**.

---

### Step 4: Subscribe to Resources

To ensure Element451 can detect and sync updates or changes automatically, you must subscribe to the following resources:

* `courses`
* `instructional-events`
* `persons`
* `sections`
* `section-instructors`
* `section-registrations`
* `student-transcript-grades`
* `student-unverified-grades`

---

### Step 5: Connect and Authenticate in Element451

🚨 **Important**

Before connecting your integration, **make sure your academic terms are set up in Element451**. Terms are not automatically imported from your SIS. They must be [added manually ahead of time](https://help.element451.com/en/articles/3152502-adding-majors-terms-degrees-campuses-schools).

**Each term needs either an SIS integration code or a unique code value that matches the corresponding term code in your SIS**. This allows Element451 to correctly map enrollment and course data to the right terms during the initial sync.

Now you’re ready to connect Element451 to your Ethos application.

1. In Element451, go to:

   * **Settings > Integrations > Native Course Integrations**
2. Click the **SIS (via Ethos)** button.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811417702/0910bd2340ca3829e1002e442ed0/CleanShot+2025-11-03+at+16_11_06.png?expires=1784333700&signature=edc91cf7d5d27e33e63edaf9490901425ed85b3571ce920e7e8018a297c22e68&req=dSgmF81%2FmoZfW%2FMW1HO4zVsd6RUHxptxHmWw22Xtk5G8aiuRqM5g1gaFFk%2Bv%0Ag5A6%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811417702/0910bd2340ca3829e1002e442ed0/CleanShot+2025-11-03+at+16_11_06.png?expires=1784333700&signature=edc91cf7d5d27e33e63edaf9490901425ed85b3571ce920e7e8018a297c22e68&req=dSgmF81%2FmoZfW%2FMW1HO4zVsd6RUHxptxHmWw22Xtk5G8aiuRqM5g1gaFFk%2Bv%0Ag5A6%0A)
3. Paste your **API Key** from Ethos.
4. Click **Connect**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811421928/639efcc762e81b64f10c093281fa/CleanShot+2025-11-03+at+16_12_57.png?expires=1784333700&signature=80d797dcd41972cdd4e2a3754fd0f9d125f76d7d5382b590b7dba9bc16abfeef&req=dSgmF818nIhdUfMW1HO4zb%2B2nIGExB3HO6%2BRPehS17JxLE9psWYmhF0CLkzt%0A235%2F%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811421928/639efcc762e81b64f10c093281fa/CleanShot+2025-11-03+at+16_12_57.png?expires=1784333700&signature=80d797dcd41972cdd4e2a3754fd0f9d125f76d7d5382b590b7dba9bc16abfeef&req=dSgmF818nIhdUfMW1HO4zb%2B2nIGExB3HO6%2BRPehS17JxLE9psWYmhF0CLkzt%0A235%2F%0A)
5. Run the **permission test** to confirm everything is set up correctly.

If the permissions test fails, revisit MRPR and AROR to ensure the necessary permissions and roles are active for the proxy user.

---

### Step 5: Contact Element451 Support for Activation

Reach out to our support team to activate the integration and start the initial import. Our engineering team handles this step for you.

You can contact Support through **Live Support** in the platform or by emailing **[support@element451.com](mailto:support@element451.com)**.

## Banner

To configure the integration with **Banner**, follow these steps:

### Step 1: Create a Proxy User in Banner

1. **Create a proxy user** for Ethos to use.

   * This can be the same user from your baseline Ethos setup or a new one based on your institution’s security policies.

---

### Step 2: Assign Required Permissions

* Ensure the proxy user has appropriate access to the academic and enrollment data required by Element451.

  + These permissions are configured via Banner’s security and roles systems. (Work with your IT or Banner admin to ensure this user can access all necessary APIs and data endpoints.)

#### Required Permissions

Element451 must have read access to the following resources:

* academic-periods
* buildings
* course-categories
* course-statuses
* courses
* educational-institution-units
* grade-definitions
* grade-schemes
* instructional-delivery-methods
* instructional-events
* instructional-methods
* persons
* rooms
* section-instructors
* section-registrations
* section-statuses
* sections
* sites
* student-transcript-grades
* student-unverified-grades
* subjects

---

### Step 3: Create Application in Ethos

1. Log into **Ethos**.
2. Go to **Applications** > **Create New App: Manually**
3. Check **Configure REST API Proxy** > Click **Continue**
4. Enter:

   * **Application Name**: `Element451 Courses`
   * **Description**: `Element451 Courses integration application`
5. Click **Next** > **Add Source Application**
6. Select your **Banner Web API application**
7. Enter the **username/password** of your Banner proxy user
8. Click **Add**

---

### Step 4: Subscribe to Resources

To ensure Element451 can detect and sync updates or changes automatically, you must subscribe to the following resources:

* `courses`
* `instructional-events`
* `persons`
* `sections`
* `section-instructors`
* `section-registrations`
* `student-transcript-grades`
* `student-unverified-grades`

---

### Step 5: Connect to Element451

🚨 **Important**

Before connecting your integration, **make sure your academic terms are set up in Element451**. Terms are not automatically imported from your SIS. They must be [added manually ahead of time](https://help.element451.com/en/articles/3152502-adding-majors-terms-degrees-campuses-schools).

**Each term needs either an SIS integration code or a unique code value that matches the corresponding term code in your SIS**. This allows Element451 to correctly map enrollment and course data to the right terms during the initial sync.

Once your Ethos application is configured, connect it to Element451:

1. In Element451, go to:

   * **Settings > Integrations > Native Course Integrations**
2. Click the **SIS (via Ethos)** button

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811460558/32563fb8897c3b0f441beed1c735/CleanShot%2B2025-11-03%2Bat%2B16_11_06.png?expires=1784333700&signature=d19a0ff2c1315c074a5d0ac5cb3c5f4e2a8cdeeafcc5a3596ad6c48b03d9b424&req=dSgmF814nYRaUfMW1HO4zUCsuEF3nRBD3toPmUK9ul6KvWhnb6WYBsySe7ig%0AqMBp%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811460558/32563fb8897c3b0f441beed1c735/CleanShot%2B2025-11-03%2Bat%2B16_11_06.png?expires=1784333700&signature=d19a0ff2c1315c074a5d0ac5cb3c5f4e2a8cdeeafcc5a3596ad6c48b03d9b424&req=dSgmF814nYRaUfMW1HO4zUCsuEF3nRBD3toPmUK9ul6KvWhnb6WYBsySe7ig%0AqMBp%0A)
3. Enter the **API Key** from your Ethos application
4. Click **Connect**

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811460762/7794ed067bf05134db874e7727db/CleanShot%2B2025-11-03%2Bat%2B16_12_57.png?expires=1784333700&signature=f4a4ae2c451af8b3a53e7c5f8bd85c4f592b312d636be693e1a4ca95dd84fddc&req=dSgmF814nYZZW%2FMW1HO4zQzQi2fzqtP5EGeT9R7ChpGd%2Ba3a16ax0D7dptTc%0AQJwD%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811460762/7794ed067bf05134db874e7727db/CleanShot%2B2025-11-03%2Bat%2B16_12_57.png?expires=1784333700&signature=f4a4ae2c451af8b3a53e7c5f8bd85c4f592b312d636be693e1a4ca95dd84fddc&req=dSgmF814nYZZW%2FMW1HO4zQzQi2fzqtP5EGeT9R7ChpGd%2Ba3a16ax0D7dptTc%0AQJwD%0A)
5. Perform the **permission test** to confirm successful setup

After making changes to permissions in Ethos, you can re-test from this screen using the **Check** button.

---

### Step 6: Contact Element451 Support for Activation

Reach out to our support team to activate the integration and start the initial import. Our engineering team handles this step for you.

You can contact Support through **Live Support** in the platform or by emailing **[support@element451.com](mailto:support@element451.com)**.

---

# Managing the Integration

Once the connection is active, you can access the Settings for your integration.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811447968/3c6a0b3a0e7bb92975eac0260675/CleanShot-2B2025-11-03-2Bat-2B16_15_22.png?expires=1784333700&signature=d1875c347b4ad8691a272f2a5f8c55b80545b05881fc23c98ebf71e22fb0b3a2&req=dSgmF816mohZUfMW1HO4zX4PuTIF268Yst7wHvpwEw6TdOMcCoj4JDMRFjEx%0AHJhd5XJWlEZL4eD7qp0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811447968/3c6a0b3a0e7bb92975eac0260675/CleanShot-2B2025-11-03-2Bat-2B16_15_22.png?expires=1784333700&signature=d1875c347b4ad8691a272f2a5f8c55b80545b05881fc23c98ebf71e22fb0b3a2&req=dSgmF816mohZUfMW1HO4zX4PuTIF268Yst7wHvpwEw6TdOMcCoj4JDMRFjEx%0AHJhd5XJWlEZL4eD7qp0%3D%0A)

Here, you will see two tabs:

## Details Tab

## Integration Status

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811427091/3a0aa74a16588ba434fcc1e437de/CleanShot+2025-11-03+at+16_17_39.png?expires=1784333700&signature=04d0657805d1dc3ffc71bd75220e7775bfc392c2a895ce76863c3629bbca1596&req=dSgmF818moFWWPMW1HO4zRY9U9rU36GQLkjB752wARB55CFaQzQQvhOK7lyz%0AempzEve9FRnkcDQ6wxE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811427091/3a0aa74a16588ba434fcc1e437de/CleanShot+2025-11-03+at+16_17_39.png?expires=1784333700&signature=04d0657805d1dc3ffc71bd75220e7775bfc392c2a895ce76863c3629bbca1596&req=dSgmF818moFWWPMW1HO4zRY9U9rU36GQLkjB752wARB55CFaQzQQvhOK7lyz%0AempzEve9FRnkcDQ6wxE%3D%0A)

On this tab, you will find:

* When it was created
* Last sync time
* Last updated by (user)

## Permissions

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811428642/6e81222cfe92d719b2ce84847132/CleanShot+2025-11-03+at+16_18_58.png?expires=1784333700&signature=8d86aa6fd9421d7490f31dc7fb9c292c7f5a5918403c00f9552bc19085149726&req=dSgmF818lYdbW%2FMW1HO4zZ4qJsQxVBbtYp4e6JqR%2FOXQ%2FWFXPen9Z1eu%2FLmc%0AMDO1At4Mv0DuSxg5v%2FM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811428642/6e81222cfe92d719b2ce84847132/CleanShot+2025-11-03+at+16_18_58.png?expires=1784333700&signature=8d86aa6fd9421d7490f31dc7fb9c292c7f5a5918403c00f9552bc19085149726&req=dSgmF818lYdbW%2FMW1HO4zZ4qJsQxVBbtYp4e6JqR%2FOXQ%2FWFXPen9Z1eu%2FLmc%0AMDO1At4Mv0DuSxg5v%2FM%3D%0A)

On this tab, you will find:

* A visual checklist of required permissions
* Use the **Check** button to re-test after changes in Ethos

## Sync Preferences Tab

Use these preferences to customize how Element451 maps and syncs your SIS data.

### Settings

The settings listed here determine how data in Ethos maps into Element451.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811429937/e64ed6043e41bb4d1bd839ec3507/CleanShot+2025-11-03+at+16_19_58.png?expires=1784333700&signature=1d33c87ec24b044aadee0076a2a56e9357477f977c3e0350331297a07d395303&req=dSgmF818lIhcXvMW1HO4zQE7YmgWYsLZ%2F20oizObrFnsInFcA7O5tPBz509z%0AwDmN21Vt5QGl6GghhBM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811429937/e64ed6043e41bb4d1bd839ec3507/CleanShot+2025-11-03+at+16_19_58.png?expires=1784333700&signature=1d33c87ec24b044aadee0076a2a56e9357477f977c3e0350331297a07d395303&req=dSgmF818lIhcXvMW1HO4zQE7YmgWYsLZ%2F20oizObrFnsInFcA7O5tPBz509z%0AwDmN21Vt5QGl6GghhBM%3D%0A)

#### Data to Sync

* **Courses**

  + Imports course information from Ethos (such as course name, code, and department).
  + Always imported by default and acts as the foundation for related data—sections cannot exist without courses.
* **Sections**

  + Imports course section information from Ethos (such as start/end dates and assigned instructors).
  + Required for enrollments and students to be imported successfully.
* **Enrollments**

  + Imports student enrollment records from Ethos, including student grades.
  + Represent the connection between students and sections and therefore cannot be imported without them.
* **Students**

  + Must be imported alongside enrollments, since enrollment records require a valid student reference.

#### Student Import Options

* **Match Student Contacts (default)**

  + Matches incoming student records with existing contacts in Element451 using unique identifiers (such as email or student ID).
  + This option is always enabled to ensure enrollments connect to the correct students.
* **Insert Student Contacts**

  + Creates new student contacts for any records not found in Element451.
  + Automatically adds their related enrollments.
  + Enable this option to add new students from your SIS who aren’t already in Element451.
* **Update Student Contacts**

  + Updates existing student contact data in Element451 with information from your SIS (such as name, email, or other synced fields).
  + Enable this option to keep student profiles in Element451 aligned with your SIS.

#### Grades + Attendance Import Settings (When LMS Integration is Active)

These options appear **only if you’ve integrated both your SIS (Banner or Colleague)** and an **LMS** (such as Canvas, D2L Brightspace, or Blackboard). They let you control which system provides grade and attendance data.

* **Import Grades**\*

  + Imports grades from your SIS alongside student enrollments.
  + When both integrations (SIS + LMS) provide grades, the **SIS data takes precedence**.
* **Import Attendance**\*

  + Imports attendance data from your SIS alongside student enrollments.
  + When both integrations (SIS + LMS) provide attendance, the **SIS data takes precedence**.

### Ethos Maintenance Window

When Ethos is under scheduled maintenance, Element451 will not attempt to sync data. To set your maintenance window, use the following settings:

* Frequency (daily, weekly, monthly)
* Start and end times
* Time zone

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811436907/c3a23333e40511282462b372fd81/CleanShot+2025-11-03+at+16_24_26.png?expires=1784333700&signature=d3268cddea1cee77761d26a0cca35b43b51d0c6e1a4387686aca8224125ba0ab&req=dSgmF819m4hfXvMW1HO4zSyGxHec%2FlK2YkvRvRN%2BgT7%2BwEDaqx8f6Jdn03qR%0AOLYqFsgVtueg99NPp%2F4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811436907/c3a23333e40511282462b372fd81/CleanShot+2025-11-03+at+16_24_26.png?expires=1784333700&signature=d3268cddea1cee77761d26a0cca35b43b51d0c6e1a4387686aca8224125ba0ab&req=dSgmF819m4hfXvMW1HO4zSyGxHec%2FlK2YkvRvRN%2BgT7%2BwEDaqx8f6Jdn03qR%0AOLYqFsgVtueg99NPp%2F4%3D%0A)

### Sync Dates

* Element451 will sync course sections that started on or after the provided start date, along with their related courses, enrollments, and students.
* Defaults to 5 years in the past, but you can update it to a specific date of your choosing.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811438586/bd0740f45dbb87c30cd59db7c354/CleanShot%2B2025-11-03%2Bat%2B16_25_02.png?expires=1784333700&signature=b6ea78b53654321b0bf06442452fb64386147b93a0efbefea23372e875b9fd0b&req=dSgmF819lYRXX%2FMW1HO4zTx56cIUF4V07VAdSr2Z8%2FlHsVv%2FugIaIn%2B%2B%2FSAS%0Ax5KyvSTl%2BPTkLEFgd9w%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811438586/bd0740f45dbb87c30cd59db7c354/CleanShot%2B2025-11-03%2Bat%2B16_25_02.png?expires=1784333700&signature=b6ea78b53654321b0bf06442452fb64386147b93a0efbefea23372e875b9fd0b&req=dSgmF819lYRXX%2FMW1HO4zTx56cIUF4V07VAdSr2Z8%2FlHsVv%2FugIaIn%2B%2B%2FSAS%0Ax5KyvSTl%2BPTkLEFgd9w%3D%0A)

### ID Translations

To match your Ethos records correctly, enter your institution's key identifiers:

* **School ID**

  + Maps from Ethos "credentials" to Element451 `SCHOOL_ID`
  + Default value is `colleaguePersonId`
* **Username ID**

  + Maps from Ethos "credentials" to Element451 `USERNAME_ID`
  + Default value is `colleagueUserName`
* **School Email (Email Type ID)**

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811440059/d9047e39dd8fe9078d6a493f838c/CleanShot+2025-11-03+at+16_26_46.png?expires=1784333700&signature=542bf9cc9fa6f9a0ac9d64af9f17ae3c00d8a934a7d7360a57bcccb14612b92f&req=dSgmF816nYFaUPMW1HO4ze2CSrSJB9Pd%2BKuGa9rNZoFcl1x%2F0EQv1MptDyGm%0A1poCBSAKjGCEwMJjPjg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1811440059/d9047e39dd8fe9078d6a493f838c/CleanShot+2025-11-03+at+16_26_46.png?expires=1784333700&signature=542bf9cc9fa6f9a0ac9d64af9f17ae3c00d8a934a7d7360a57bcccb14612b92f&req=dSgmF816nYFaUPMW1HO4ze2CSrSJB9Pd%2BKuGa9rNZoFcl1x%2F0EQv1MptDyGm%0A1poCBSAKjGCEwMJjPjg%3D%0A)

---

# Integration Logs

To monitor errors:

1. Go to **Settings > Integrations > Integration Logs**
2. Use the filter to select **EthosCourses to E451**

This will show only the logs relevant to your Ethos integration, helping you quickly identify and troubleshoot issues.

---