---
title: Courses Native Integration: Canvas LMS
url: https://help.element451.com/en/articles/11124554-courses-native-integration-canvas-lms
collection: Integrations
---

# Overview

The Canvas LMS integration seamlessly syncs real-time academic and enrollment data from Canvas into Element451. This guide will walk you through the setup process, from configuring Canvas settings to completing the integration within Element451.

📌 **Note:** This is a one-way integration. Element451 reads data from Canvas but **does not** write back any data.

## Overview of the Setup Process

To get started, you’ll work through the following four steps. We outline each in detail in the subsequent sections of this article.

1. [Create a Developer Key in Canvas](#h_b29ec969c2)
2. [Enable Live Events in Canvas](#h_03f2c33253)
3. [Provide Credentials to Element451](#h_b9707c5dc6)
4. [Authenticate the Integration](#h_986285233d)

---

# Step 1: Create a Developer Key in Canvas

To allow secure communication between Canvas and Element451, you’ll first need to create a **Developer Key** in Canvas. This generates a Client ID and Client Secret you'll use later in the setup.

1. Log in to your Canvas account as an **Admin**.
2. Navigate to the **Developer Keys** section in your Canvas admin settings.
3. Click **+ Developer Key** and select **API Key**.
4. Configure the key with the following:

   * **Key Name**: Element451
   * **Redirect URL:**

     [`https://api.451.io/clients/integrations/canvas/oauth2`](https://api.451.io/clients/integrations/canvas/oauth2)
5. Save the key, then toggle it to On to enable it (new developer keys default to off).
6. Copy the **Client ID** and **Client Secret**—you’ll need these in Step 3.

   * 📌Note: Depending on your version of Canvas, you may see a 18-digit code with a "Show Key" button. If you see this, the 18-digit code is your Client ID and the "Show Key" button exposes your Client Secret.

🔗 For more detailed instructions, see [Canvas’s guide on creating developer keys](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-add-a-developer-API-key-for-an-account/ta-p/259).

**The Element451 ⇄ Canvas integration is designed to operate without scopes on the Developer Key.** The Developer Key creates the OAuth client. Subsequent API access is determined by the Canvas user (ideally a dedicated service account) who completes OAuth, with the permissions listed in Step 3.

---

# Step 2: Enable Live Events in Canvas

Element451 uses Canvas Live Events to receive real-time LMS activity from Canvas, including course, section, enrollment, and grade updates.

During this step, Canvas is configured to publish Live Events directly to an Element451-managed SQS queue. Element451 restricts publishing to approved partner Canvas instances and consumes these events to keep Courses data in Element451 up to date.

With this in mind, you:

* Do not need to create or manage a new SQS Queue in AWS
* Do not grant Element451 AWS IAM access to any of your AWS resources
* Do not reuse this setup for any other Canvas integrations

Canvas Data Services is built into your Canvas instance and does not require a separate installation. To configure a new stream, navigate to **Admin → [Your Account Name] → Data Services** in your Canvas account navigation and click **Add Stream**.

Configure the stream with the following settings:

|  |  |
| --- | --- |
| **Name/Title** | Your choice (e.g., "Element451 Live Events") |
| **Delivery Method** | Amazon SQS |
| **URL** | <https://sqs.us-east-1.amazonaws.com/783873245484/canvas-live-events-prod> |
| **AWS Region** | us-east-1 |
| **Authentication** | Select None |
| **AWS Credentials** | Leave blank |

**About the SQS Queue:** The SQS queue used for this integration is hosted & managed by Element451 and is configured to allow **only Canvas instances** from our partners to publish Live Events. Element451 consumes and processes these events to keep Courses data in Element451 up to date.

|  |  |
| --- | --- |
| **Event Category** | **Events** |
| Assignment | While assignment events are not required right now, we recommend enabling them to support future expansion. |
| Course | Created, Updated, Completed, Progress, Deleted |
| Course Section | Created, Updated, Deleted |
| User | Created, Updated, Deleted |
| Enrollment | Created, Updated, Deleted |
| Grade | Course Grade Change |

---

# Step 3: Authenticate the Integration in Element451 via OAuth

Once you have registered your application in Canvas, and setup live events, you'll need to authorize Element451 to access your Canvas data using OAuth via Canvas Account.

🚨 **Important:** The user performing the authentication must be a Canvas Administrator and have read access to: Courses, Course Sections, Users, Enrollments, Assignments, and Grades. You can read more about Canvas permissions [here](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-set-permissions-for-an-account-level-role/ta-p/213).

1. **Create a Canvas service account (recommended). Avoid using an account used for other integration or tied to a named user.**

   1. In Canvas, add a user to act as the integration’s service account. Do **not** use a personal account.
   2. Make the account an *Account Administrator* or assign an account-level role that includes read access to Courses, Course Sections, Users, Grades, Assignments and Enrollments. This account’s permissions will be the permissions Element451 runs with.
2. **Authenticate in Element451**

   1. Click on your avatar/profile picture in the top right corner of the orange navigation menu.
   2. Navigate to **Settings** > **Integrations**
   3. From the left-hand menu, select **Native Course Integrations**
   4. Select Canvas
   5. Enter your Connection Details
   6. Click the **Connect** button; you'll be redirected to Canvas
   7. Authenticate using the service account you created above (or other account you wish to use) and approve the authorization.

You'll need your `Client ID` and `Client Secret` to complete this process.

---

# Step 4: Configure Preferences

Once you've authenticated your integration, you can access the LMS integration settings.

To review and adjust your preferences, **click the pencil icon** in the top right corner of your LMS integration card.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613874515/3bed86cdfb69f7ec5b05ea9bee47/CleanShot+2025-07-10+at+15_32_45%402x.png?expires=1784333700&signature=945cbefbb8db97357797c2ef0d5a0681d821252b5c960631020ae0da2cdb6e7f&req=dSYmFcF5mYReXPMW1HO4zbSQWsd6CjumbgEwzoJcmn0ShDggpenaCkHBiClt%0AaC1obUPt7haCtNmSfPI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613874515/3bed86cdfb69f7ec5b05ea9bee47/CleanShot+2025-07-10+at+15_32_45%402x.png?expires=1784333700&signature=945cbefbb8db97357797c2ef0d5a0681d821252b5c960631020ae0da2cdb6e7f&req=dSYmFcF5mYReXPMW1HO4zbSQWsd6CjumbgEwzoJcmn0ShDggpenaCkHBiClt%0AaC1obUPt7haCtNmSfPI%3D%0A)

## Data Sync Preferences

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613870557/67c3976102281f709a8c649c2f36/CleanShot+2025-07-10+at+15_30_40%402x.png?expires=1784333700&signature=14bb99d7b49bbe3aad7405f8260e09eb840206ae80aa6495e34c4f719cc08384&req=dSYmFcF5nYRaXvMW1HO4zR4xXPQiwABABHFLo8WqEuD3n9B9dM6%2FnwDYHfSm%0A5OJON82cfjkSLBiLxIc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613870557/67c3976102281f709a8c649c2f36/CleanShot+2025-07-10+at+15_30_40%402x.png?expires=1784333700&signature=14bb99d7b49bbe3aad7405f8260e09eb840206ae80aa6495e34c4f719cc08384&req=dSYmFcF5nYRaXvMW1HO4zR4xXPQiwABABHFLo8WqEuD3n9B9dM6%2FnwDYHfSm%0A5OJON82cfjkSLBiLxIc%3D%0A)

* **Courses**¹: Import course information from Canvas, including course name, code, department, and other relevant details.
* **Sections**¹: Import individual course section information from Canvas, including dates, instructor names, etc.
* **Enrollments**: Import student enrollment records from Canvas, including student grades

  + **Match Student Contacts**²: Add enrollments for students already in the Element451 database
  + **Insert Student Contacts**: Create new contacts for students previously not found in Element451, and add their enrollments
  + **Update Student Contacts**: Overwrite existing contact data with data found in Canvas, such as name and email

¹*Setting is required and cannot be disabled.*

²*Setting is required when Enrollments is enabled.*

## Settings

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613872140/a25fb1d93eae6ff4b613bef69420/CleanShot+2025-07-10+at+15_31_33%402x.png?expires=1784333700&signature=ee197231aa61bffe5c82081fa591dfffeb12fd4b7b567779e4ffeca205e1126b&req=dSYmFcF5n4BbWfMW1HO4zcjZQFSCAaSnxZUiLtnR2NsR5pv4qHic9q4JaBCb%0ArB8RpJgpGR%2F46YizbiI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1613872140/a25fb1d93eae6ff4b613bef69420/CleanShot+2025-07-10+at+15_31_33%402x.png?expires=1784333700&signature=ee197231aa61bffe5c82081fa591dfffeb12fd4b7b567779e4ffeca205e1126b&req=dSYmFcF5n4BbWfMW1HO4zcjZQFSCAaSnxZUiLtnR2NsR5pv4qHic9q4JaBCb%0ArB8RpJgpGR%2F46YizbiI%3D%0A)

* **Target Semesters**: Only data from courses with a section within the selected semesters will be imported.
* **Auto Import Semesters**: When enabled, Element451 will automatically sync the selected resources (courses, sections, or enrollments) for new semesters that are added to the LMS.

## Matching Student Contact Criteria

The Canvas LMS integration reads student data from Canvas and matches to Element records using the following fields:

* user-identities-canvasid
* user-identities-school-email
* user-identities-email

If a match can not be determined, the integration will either insert a new student record in Element451 or not depending on the data sync preferences.

### Inserting or Updating Student contacts

The following fields will be populated by the integration when inserting or updating contacts based on Canvas student data:

* user-first-name
* user-last-name
* user-email-address
* user-preferred-name
* user-sources-source-type = "LMS"
* user-sources-source-name = "Canvas"
* user-sources-source-date

---

# Next Steps

Once authentication is complete, Element451 will begin syncing data from Canvas based on the configured Live Events. This data lives in [Courses](https://help.element451.com/en/articles/10420398-getting-started-with-courses) (**Data + Automation** > **Courses**), where you can view course records from your LMS.

Now that your course data is flowing into Element, you can begin using it to:

* Build targeted segments
* Trigger workflows + communications
* Assign tasks or academic support resources
* Personalize student experiences in StudentHub

To explore how to make the most of your LMS data, check out our [Getting Started with Courses](https://help.element451.com/en/articles/10420398-beta-getting-started-with-courses) article.

---

# Matching Canvas Terms to Element451

When course and section data syncs from Canvas, Element451 matches each record to an existing term in your account so it can be used for filtering and segmentation. This match is made using the term's **Canvas integration code**—not the term's standard code.

🚨 **Important:** You must add a **Canvas integration code** to each term you want to sync. Element451 does not fall back to the standard term code—even when it's identical to the Canvas value. If a term has no Canvas integration code, its courses and sections will sync in with **No Term**, which prevents you from filtering or segmenting on them.

The Canvas integration code must match the term's `sis_term_id` in Canvas. To add it:

1. Navigate to **Data + Automations** > **Data Sources** > **Terms**.
2. Click the **pencil icon** next to the term to open the editor.
3. Select the **Integration Code** tab.
4. Click **+ Add Code**, choose **Canvas** from the "With" menu, and enter the term's Canvas `sis_term_id` as the value.
5. Click **Done**.

For more on adding and importing integration codes, see [Setting up Integration Codes](https://help.element451.com/en/articles/5181322-setting-up-integration-codes).

---

# Field Mapping

Once your LMS integration is active, Element451 automatically syncs data from your system into organized, consistent fields. This eliminates manual data entry while ensuring all information flows seamlessly between platforms.

Element451 automatically creates data sources for your course data directly from your LMS. No manual setup required—everything is generated automatically during the integration process.

The tables below show exactly which LMS fields map to which Element451 fields:

## Course

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Canvas Object** | **Canvas Field** |
| Institution ID | course | id |
| Name | course | name |
| Description | course | public\_description |
| Code | course | course\_code |
| Total Students | course | total\_students |
| Departments¹ -Institution ID -Name | course course course | Multiple values supported  -account->id  -account->name |
| Status¹ | course | workflow\_state |
| Type¹ | course | course\_format |
| Term² | course | term->sis\_term\_id |
| Timezone | course | time\_zone |
| Subject | - | *Not available* |
| Number | - | *Not available* |
| Credits | - | *Not available* |
| Version | - | *Not available* |
| Grading | - | *Not available* |

## Section

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Canvas Object** | **Canvas Field** |
| Institution ID | section | id |
| Code | course | course\_code |
| Status¹ | course | workflow\_state |
| Instruction Mode¹ | course | course\_format |
| Term² | course | term->sis\_term\_id |
| School | course | account->name |
| Instructor¹ | user | first\_name + last\_name |
| Instructor Email | user | email |
| Current Enrollments | course | total\_students |
| Timezone | course | time\_zone |
| Start Date | course | start\_at |
| End Date | course | end\_at |
| Section Type | - | *Not available* |
| Version | - | *Not available* |
| Campus | - | *Not available* |
| Total Meetings | - | *Not available* |
| Max Enrollment | - | *Not available* |
| Times | - | *Not available* |

## Enrollment

|  |  |  |
| --- | --- | --- |
| **Element451 Field** | **Canvas Object** | **Canvas Field** |
| Institution ID | enrollment | id |
| Enrollment Status¹ | enrollment | enrollment\_state |
| Current Grade (Text) | enrollment | grades->current\_grade |
| Current Grade (Number) | enrollment | grades->current\_score |
| Final Grade (Text) | enrollment | grades->final\_grade |
| Final Grade (Number) | enrollment | grades->final\_score |
| Last LMS Activity | enrollment | last\_activity\_at |
| Last Attended Date | enrollment | last\_attended\_at |
| Total Active Time | enrollment | total\_activity\_time |
| Total Absences | - | *Not available* |

¹ Automatically creates a data source in Element451  
² Matched against existing terms in Element451 using the term's **Canvas integration code** (see [Matching Canvas Terms to Element451](#h_termmatching) above)

---

# Reviewing Imported Semesters

To review your imported semester data, navigate to **Settings** > **Integrations** and click on your LMS from the left-hand menu.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627131670/e16787902a43a6e423e36cc170f2/CleanShot-2B2025-07-10-2Bat-2B15_37_22-402x.png?expires=1784333700&signature=425a4726a92a93f5ee45414c1033e16be293a33d5f55b11b885752cef2036bdc&req=dSYlEch9nIdYWfMW1HO4zZC6xwKVJsTgvgmPbwg60phQbcHW%2BLonX%2FHdoWP%2B%0AEwCXUNB2zuwkv8S6q7g%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627131670/e16787902a43a6e423e36cc170f2/CleanShot-2B2025-07-10-2Bat-2B15_37_22-402x.png?expires=1784333700&signature=425a4726a92a93f5ee45414c1033e16be293a33d5f55b11b885752cef2036bdc&req=dSYlEch9nIdYWfMW1HO4zZC6xwKVJsTgvgmPbwg60phQbcHW%2BLonX%2FHdoWP%2B%0AEwCXUNB2zuwkv8S6q7g%3D%0A)

On the **Imported Semesters** card, you'll see:

* Semester
* Status
* Added At
* Started At
* Last Sync Completed At

---