---
title: Configuring Profile Templates
url: https://help.element451.com/en/articles/10471008-configuring-profile-templates
collection: Settings + Permissions
---

# Overview

This article walks you through the settings and configurations for adding or editing a new profile template. If you haven’t already, we recommend starting with the [Getting Started with Profile Templates](https://intercom.help/element451/en/articles/6449965-getting-started-with-profile-templates) article.

When creating or editing a Custom Profile Template (navigate to **Settings > Profile Templates**), the side sheet includes four tabs at the top: **Settings**, **Header**, **Sidebar**, and **Main**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353743365/b675d78b5d4a63505a9aff6737df/Custom%2Bprofile%2Btemplate%2Bsheet.png?expires=1784333700&signature=d0b17b70d55883de9653cf4d951e5a0b668ca997ac2b3d5fdd0e89eeb5c3fecb&req=dSMiFc56noJZXPMW1HO4zXP7GfBLFQMB5zxBmQRTU%2Fijxa64t29ohEJkbSde%0A3mXLg9CJF4Dhwx4yio4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353743365/b675d78b5d4a63505a9aff6737df/Custom%2Bprofile%2Btemplate%2Bsheet.png?expires=1784333700&signature=d0b17b70d55883de9653cf4d951e5a0b668ca997ac2b3d5fdd0e89eeb5c3fecb&req=dSMiFc56noJZXPMW1HO4zXP7GfBLFQMB5zxBmQRTU%2Fijxa64t29ohEJkbSde%0A3mXLg9CJF4Dhwx4yio4%3D%0A)

These tabs correspond to different parts of the [Person Profile](https://intercom.help/element451/en/articles/1475735-the-person-profile) and allow you to customize the layout, display, and functionality to meet your team’s unique needs. This guide provides a detailed breakdown of each tab’s purpose and available settings.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353743146/ad4f0528355d62aaf1be9c569a37/Person+Profile+Diagram.png?expires=1784333700&signature=13162b0731b3802bcc325a6bd2678901e395b912d5d2524cb3e43009ab14392a&req=dSMiFc56noBbX%2FMW1HO4zUXQK9aYiGVcqbQgzAT3e80%2BoEghBwgjkL%2BErYjA%0AuL3WkuPIVIOD11DddCU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353743146/ad4f0528355d62aaf1be9c569a37/Person+Profile+Diagram.png?expires=1784333700&signature=13162b0731b3802bcc325a6bd2678901e395b912d5d2524cb3e43009ab14392a&req=dSMiFc56noBbX%2FMW1HO4zUXQK9aYiGVcqbQgzAT3e80%2BoEghBwgjkL%2BErYjA%0AuL3WkuPIVIOD11DddCU%3D%0A)

---

# Settings

The **Settings** tab lets you configure the core details of a Profile Template, including its name, status, description, and conditions that control its visibility to internal users.

## Configurations

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353799659/50a5c818cf9df8aa762f2f45bf3f/Templates%2B-%2BSettings.png?expires=1784333700&signature=5217465e6c0be270dbf719876cc0712351cb0e10d4e2d94c137b020b908f7f3e&req=dSMiFc53lIdaUPMW1HO4zQiaEWibQatzT7sFgeZHXXv0pcjcmU%2B73oMES5GA%0Ay2LzZevvtWabbnaqoR4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353799659/50a5c818cf9df8aa762f2f45bf3f/Templates%2B-%2BSettings.png?expires=1784333700&signature=5217465e6c0be270dbf719876cc0712351cb0e10d4e2d94c137b020b908f7f3e&req=dSMiFc53lIdaUPMW1HO4zQiaEWibQatzT7sFgeZHXXv0pcjcmU%2B73oMES5GA%0Ay2LzZevvtWabbnaqoR4%3D%0A)

**Name**

The template name is located at the top of the side sheet, and while it is accessible from any tab, it’s a good idea to name your template right away as the first step to avoid forgetting it later.

* Keep in mind that the name is visible on the profile, helping users identify which template they’re actively viewing. For this reason, choose a name that is **short yet descriptive**, clearly reflecting the template’s purpose or audience.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353559106/7c3b96b9a369208eb2e2baf69bc2/Template+-+Template+View.png?expires=1784333700&signature=455c4c5af318a6e83036da1404569992c22766b0a6aa06083d0c55e6e637fbee&req=dSMiFcx7lIBfX%2FMW1HO4zf0nI%2FCLOr7MbD2dNLm8sJysFiqIgT1O0h1ygoop%0Atcen%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353559106/7c3b96b9a369208eb2e2baf69bc2/Template+-+Template+View.png?expires=1784333700&signature=455c4c5af318a6e83036da1404569992c22766b0a6aa06083d0c55e6e637fbee&req=dSMiFcx7lIBfX%2FMW1HO4zf0nI%2FCLOr7MbD2dNLm8sJysFiqIgT1O0h1ygoop%0Atcen%0A)

**Template Active**

Toggle this option to activate or deactivate the template. An inactive template won’t be evaluated in the [order of precedence](https://help.element451.com/en/articles/6449965-getting-started-with-profile-templates#h_7d0cc67a32) or appear for any users.

**Description**

Add or update a description to clarify the purpose of this template. This is especially useful when managing multiple templates.

**Show When (Conditions)**

Define conditions that determine which internal users will see the profile template based on.

* **How it Works**: When an internal user views a contact's profile, Element451 checks these conditions to determine which profile template to display. If multiple templates are eligible, the **first** matching template in your template list will display. We refer to this as the order of precedence, and it's explained in our [Getting Started with Profile Templates](https://help.element451.com/en/articles/6449965-getting-started-with-profile-templates#h_7d0cc67a32) article.

* **Condition Types: Person vs. User**

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353672010/a73509085264b15e3dcbd2a641e5/Templates+-+Settings+-+Condition+Types.png?expires=1784333700&signature=9010262a412de06bca89bfd6a30f8e4ede861141322dc76a28bb9e6344bf04b5&req=dSMiFc95n4FeWfMW1HO4zVGm81jb2PrisqotEmwE55cBVuvPO89u2RDw1Guk%0AoDwL%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353672010/a73509085264b15e3dcbd2a641e5/Templates+-+Settings+-+Condition+Types.png?expires=1784333700&signature=9010262a412de06bca89bfd6a30f8e4ede861141322dc76a28bb9e6344bf04b5&req=dSMiFc95n4FeWfMW1HO4zVGm81jb2PrisqotEmwE55cBVuvPO89u2RDw1Guk%0AoDwL%0A)

  + **Person Conditions (pertains to the contact of the profile being viewed):**

    - [Labels](https://intercom.help/element451/en/articles/6953481-labels-overview)
    - [Territory](https://intercom.help/element451/en/articles/3990795-territory-management)
    - Profile Type

      * As a rule of thumb, all templates should include a profile type filter.
    - [Visibility Groups](https://intercom.help/element451/en/articles/5214533-visibility-groups)

      * Use a visibility group filter to leverage the full suite of segment filters.
  + **Admin Conditions (pertains to the user accessing the profile):**

    - Admins (specific internal users)
    - [Groups](https://intercom.help/element451/en/articles/2735389-permission-groups-overview) (specific permission groups)
    - [Primary Team](https://intercom.help/element451/en/articles/8346250-teams)
    - [Team](https://intercom.help/element451/en/articles/8346250-teams)

  + To prevent users from seeing the system-delivered templates provided by Element451, create a default profile template without condition filters and place it at the bottom of your Custom Profile list.

## Video Guide

---

# Header

The **Header** section is the top portion of a contact’s profile. Use it to display at-a-glance details and shortcuts, ensuring that important information is easily accessible.

## Configurations

**Show Labels**

Show or hide [labels](https://intercom.help/element451/en/articles/6953481-labels-overview) to indicate key identifiers or statuses for the contact.

**Show Profile Types**

Show or hide the contact’s profile type (e.g., student, family, influencer). You can enable an editable dropdown to allow updates directly from the profile.

**Show Settings**

Show or hide shortcuts to essential actions such as Password Reset, Deactivate User, or Delete User.

**Show Possible Duplicates**

Enable this option to allow users to check for and resolve potential duplicate profiles.

**Background Image**

Choose four geometric background image options.

**Metadata**

Display specific fields as metadata, accompanied by designated icons. This is a great way to highlight concise yet important data (e.g., intended campus, degree, term, major).

**Call-to-Action Buttons**

Add or remove action buttons for quick user interactions. Available options include:

* **Phone Call to Displayed Person (Cell)\***

  + Place an outbound call to the person’s listed *cell* phone number.
* **Phone Call to Displayed Person (Home)\***

  + Place an outbound call to the person’s listed *home* phone number.
* **Email to Displayed Person**

  + Send an email to the person.
* **Open Conversations with Displayed Person**

  + Open conversations associated with the person.
* **Add Task**

  + Create an internal task related to the person.
* **Add Note**

  + Create a new note related to the person.
* **Unsubscribe**

  + Unsubscribe the person from communications (email, SMS, or both).
* **Phone Call\***

  + Place an outbound call to the person and select which number to use.
* **Run Workflow Rule**

  + Trigger a predetermined rule to run for that person.
* **Send Communication**

  + Send a predetermined campaign email to that person.

**\*Important Notes Regarding Phone Call CTAs**

* “Phone Call” action buttons on a contact profile are a powerful way to streamline communication. It allows users to initiate a call directly from the platform, whether using our [in-app calling](https://intercom.help/element451/en/articles/8400679-in-app-calling) feature or the device/browser’s native functionality. When you add the **Phone Call** action to a contact profile template:

  + **In-App Calling Enabled:** If your school uses our in-app calling feature, selecting this action will launch the call directly in the platform.
  + **In-App Calling Not Enabled:** If in-app calling isn’t enabled, the call will be routed through your browser or device’s default phone call handler (e.g., Google Voice, Microsoft Teams, or your device’s dial pad). If your school doesn’t use in-app calling, you must configure your device or browser to ensure phone calls are routed correctly. Here’s how:

    - **Browsers (e.g., Google Chrome)**

      * If you’re using a browser to initiate calls, ensure the browser is set up to handle `tel: links` correctly.
      * For example, Google Chrome can route these links to apps like Google Voice if configured. Refer to [this Google Voice support guide](https://support.google.com/voice/answer/11397414?hl=en#:~:text=Google%20Chrome,left%2C%20click%20Privacy%20and%20security) for steps.
    - **Microsoft Teams or Other Apps**

      * If your school uses Microsoft Teams or a similar app, you may be able to configure it to handle calls initiated from `tel: links`. Check your app’s settings or contact your IT team for guidance.

## Video Guide

---

# Sidebar

The **Sidebar** is an optional area of the profile that can be displayed on the left or right of the main display area. Use it to group important, frequently accessed information for quick reference.

**Note**: *Repeater* fields aren’t supported in the sidebar. The sidebar can only display individual profile fields. To surface data from a repeater, use a card in the main layout.

## Configurations

* **Sidebar Style:** Choose whether the sidebar appears on the **left**, **right**, or is hidden entirely.

* **Show Assignee: S**how or hide the record assignee (e.g., the staff member responsible for managing the contact).

* **Show Territory:** Display the assigned territory, if applicable.

* **Show 'More Data' Button:** Include a button that links users to additional data or extended profile details.

* **Configure Personal Info:** Create and customize sections to group related fields, making it easy for users to locate critical information. For example, a 'contact info' section could include fields like the person's email, phone number, address, and last touch point.

## Video Guide

---

# Main Tab

The **Main** tab is the central display area of the profile. It is a flexible canvas where you can organize information using customizable **Profile Cards.**

## Configurations

**Enable Search**

Enable or disable the search bar for users to quickly find specific profile cards.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353729241/5719f087a79b48ddd944a1e12274/Templates+-+Searh.png?expires=1784333700&signature=deb4c8f62a60a3060cff4259be61fe51c201cf6634707fe070386a7735fc1476&req=dSMiFc58lINbWPMW1HO4zR2v4TPmlO8TQYcAlqo4pvfzh7tAfe%2BUW027HsMw%0AW9tPa4urDWx95Hqqopw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353729241/5719f087a79b48ddd944a1e12274/Templates+-+Searh.png?expires=1784333700&signature=deb4c8f62a60a3060cff4259be61fe51c201cf6634707fe070386a7735fc1476&req=dSMiFc58lINbWPMW1HO4zR2v4TPmlO8TQYcAlqo4pvfzh7tAfe%2BUW027HsMw%0AW9tPa4urDWx95Hqqopw%3D%0A)

**Enable Groups**

Enable groups to organize profile cards into bundles. When this option is enabled, a dropdown field will appear, allowing you to filter and display profile cards by group name.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353729538/1f39c79b5ffbfdaaf465f536bb15/Templates+-+Groups+Dropdown.png?expires=1784333700&signature=0b07bf257c247bc92e4ede7c854d44cd7167b3fa37e7d4312c43516a91c49e14&req=dSMiFc58lIRcUfMW1HO4zaYrpyQgWbqHbJiVbik88c2Gi3dHlTv5FTy1UaGf%0APSBvPC5RHc8fXgZ5bsM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353729538/1f39c79b5ffbfdaaf465f536bb15/Templates+-+Groups+Dropdown.png?expires=1784333700&signature=0b07bf257c247bc92e4ede7c854d44cd7167b3fa37e7d4312c43516a91c49e14&req=dSMiFc58lIRcUfMW1HO4zaYrpyQgWbqHbJiVbik88c2Gi3dHlTv5FTy1UaGf%0APSBvPC5RHc8fXgZ5bsM%3D%0A)

* Each group has an independent layout, making it especially helpful for managing and displaying a large number of cards.
* A card can appear in multiple groups but will display only once in the **All Cards** view.

**Cards**

Choose from 40+ available cards to display key data in **single**, **double**, or **triple**-column widths.

* Wider cards may show additional details or provide extra functionality, depending on the card type.
* Layouts adjust automatically for smaller screen sizes.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353802950/0e661e300ac0916d2c86f25e1a07/Pro+Tip.png?expires=1784333700&signature=3135d83b40304828f38e018b21fc2108e974568626744c8851a1a7113172ab99&req=dSMiFcF%2Bn4haWfMW1HO4zTZK0lLAHhkMXeBCXdox7VNZYnJxeH9%2BUuq%2BlLwM%0ASkaqP%2FnTvjfa0GnezgU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353802950/0e661e300ac0916d2c86f25e1a07/Pro+Tip.png?expires=1784333700&signature=3135d83b40304828f38e018b21fc2108e974568626744c8851a1a7113172ab99&req=dSMiFcF%2Bn4haWfMW1HO4zTZK0lLAHhkMXeBCXdox7VNZYnJxeH9%2BUuq%2BlLwM%0ASkaqP%2FnTvjfa0GnezgU%3D%0A)

Use larger cards for complex data and smaller cards for simpler details.

## Video Guide

---

# Profile Cards

Profile cards provide at-a-glance information about a person or student directly from their profile. These cards make it easy to access and manage key data without navigating away from the profile. Most cards can be expanded to a side sheet, offering even more details while keeping you in context.

Element451 provides **system cards**, preconfigured and ready for use, and the ability to create **custom cards**, allowing you to tailor data displays to meet your institution’s specific needs.

* **System Cards:** Prebuilt, ready-to-use cards that cover common data points like applications, conversations, and activities.
* **Custom Cards:** Admin-defined cards that allow you to organize person-scoped custom and system fields to suit your workflow.

## System Cards

Element451 delivers 40+ system cards that are grouped and organized for quick configuration. These cards can display data in single, double, or triple-column widths, with wider cards often offering additional details or functionality. Cards can also be collapsed into a title row to access the related sheet quickly.

### List and Description of System Cards

|  |  |
| --- | --- |
| **Card Type** | **Description** |
| Academic | Displays academic preferences, including intended major, degree, term, school, campus, student type, academic load, housing preference, veteran funding, and prior application status. |
| Activity | Outlines the documented interactions the student has had with your institution, including opened and clicked emails, SMS, application account interactions, event registrations/attendance, form submissions, etc. |
| Alerts  [Closed Beta] | *Closed Beta: Not yet available for all users.*    The Alerts card displays all [Alerts](https://help.element451.com/en/articles/13771971-working-with-alerts-closed-beta) associated with the student, organized into Open and Closedtabs. Each Alert shows the alert type, due date, reviewer, and status. You can edit or delete an Alert directly from the card without navigating to the Case Management module.    *Note:* *One-column* *width is not supported for Alerts.* |
| Applications | Shows the [applications](https://help.element451.com/en/articles/1963691-getting-started-with-applications) a person has started and their statuses. Includes access to general application information, completed application documents, or logging in as the user for more details. |
| Appointments | Shows the [appointments](https://help.element451.com/en/articles/10458679-getting-started-with-appointments) related to the person, including details like assignee, type, status, and location. You can also create or manage appointments for this person. |
| Athletics | Contains information related to [athletics](https://help.element451.com/en/articles/3229317-athletics) interests and recruitment status. |
| Bolt Agent Jobs | Displays the contact's enrollment history in [Bolt Agent Jobs](https://help.element451.com/en/articles/11131186-getting-started-with-bolt-agent-jobs) (provides the job name, status, last action, and last action date). You can also manually enroll the contact into an existing job from the card. |
| Calculated Segments | Displays all [calculated segments](https://help.element451.com/en/articles/1474191-segments-overview) this record is currently part of. |
| Campaigns | Lists [campaign](https://help.element451.com/en/articles/1513671-getting-started-with-campaigns) messages delivered to this person. |
| Cases  [Closed Beta] | *Closed Beta: Not yet available for all users.* ​ The Cases card displays all [Cases](https://help.element451.com/en/articles/13772190-working-with-cases-closed-beta) associated with the student, organized into Active and Closed tabs. Each Case shows the case name, due date, assignee, priority, and status. You can edit or delete a Case directly from the card without navigating to the Case Management module. ​  *Note:* *One-column* *width is not supported for Cases.* |
| Contact Tasks | Shows incomplete and complete [tasks](https://help.element451.com/en/articles/3065709-getting-started-with-tasks) assigned to the contact. Tasks can also be edited directly from the card. |
| Conversations | Displays the contact's sent/received messages through the [Conversations](https://help.element451.com/en/articles/1894279-getting-started-with-conversations) module. |
| Courses | Displays [course-related data](https://help.element451.com/en/articles/10420398-getting-started-with-courses), such as enrolled classes, sections, and meeting times. |
| Custom Card | Allows Element451 admins to build custom profile cards containing person-scoped custom or system fields. Explore more on creating custom cards in the next section. |
| Custom Fields | Acts as a shortcut to the Custom Fields sheet, available only as a collapsed view card. |
| Discovery | Displays [Bolt Discovery](https://help.element451.com/en/articles/9331910-bolt-discovery-overview) threads started by the contact. |
| Documents | Lists the most recent documents uploaded to the person record, including those via applications, forms, Microsites, or manual uploads. |
| Emergency Contacts | View, add, and manage emergency contact information for the person. |
| Employments | Lists prior or current jobs held by the applicant. |
| Evaluations | Contains information related to official and unofficial [test scores](https://help.element451.com/en/articles/10966006-evaluations-tests-superscores) (e.g., SAT, ACT, GRE). |
| Events | Shows upcoming or past [events](https://help.element451.com/en/articles/1520520-getting-started-with-events) related to this person. |
| Extracurricular Activity | Displays career-related activities of the applicant. |
| Family Members | Shows data and contact information for parents, guardians, spouses, siblings, children, or other [family members](https://help.element451.com/en/articles/8903525-family-members-relationships). |
| Form Submissions | Displays information on all RFI or other [form](https://help.element451.com/en/articles/2582904-getting-started-with-forms) submissions. |
| GPAs | Displays GPAs of the applicant’s prior high schools or colleges. |
| Holds | Displays [hold-related data](https://help.element451.com/en/articles/8704178-administrative-holds-data-object) such as status, type, and amount. |
| Identities | Lists various IDs associated with this record (e.g., Common App ID, Student ID). |
| Imports | Lists data [imports](https://help.element451.com/en/articles/9000459-getting-started-with-imports) that have included this contact, with timestamps and links to each import task. Useful for troubleshooting where a value on the record came from, especially when scheduled imports run frequently. |
| Insights | Provides actionable insights and a heat map of activity over time. |
| Journeys | Displays the [Journeys](https://help.element451.com/en/articles/6825003-getting-started-with-journeys) the user is enrolled in or has completed. |
| Magic Links | Contains [direct access keys](https://help.element451.com/en/articles/8106669-magic-links) for various Element451 portals (e.g., events, applications, Microsites). |
| Milestones | Lists various funnel [milestones](https://help.element451.com/en/articles/3419189-milestones) such as inquiry date and application dates. |
| Network | Links students to internal users representing their support team. |
| Notes | Shows recent notes and allows quick addition of new notes to record one-on-one interactions. |
| Organizations | Lists any organizations related to this person. |
| Payments | Details application, event, deposit, or other fee payments made via Element451 payment integrations. |
| Person Data | Acts as a shortcut to the Person Data sheet. |
| Relationships | Lists connections to other profiles (e.g., parents, coaches, counselors, influencers). |
| Schools | Provides details on prior high schools, colleges, or universities attended. |
| Sources | Lists any sources related to the record. |
| Superscores | Displays calculated superscores for SAT and ACT standardized tests. |
| Surveys | Links to survey responses. |
| Tasks | Allows you to view and update tasks related to this person. |
| Traits | Displays traits calculated by Element451 (e.g., first/last email open, total email interactions). |
| Visibility Groups | Lists visibility groups with access to view the record. |
| Workflows | Displays workflows the student is enrolled in, including finished and aborted workflows, with options to manage them. |

## Custom Cards

Admins can create custom profile cards to organize relevant information in a way that best fits their workflows. Custom cards allow you to combine **person-scoped system fields** and **custom fields**, giving you maximum flexibility.

### Adding + Editing Custom Cards

1. Add a custom card to your profile template.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353772056/ebf07ae08c58c715fb7cf1b29944/Templates+-+Add+Custom+Card.png?expires=1784333700&signature=c4de4a5622f51dce16f4193ea373984221adfb99abb10de78a7d7c4f7634d0f6&req=dSMiFc55n4FaX%2FMW1HO4zU0FXKx34S13LqJsXHU2OYQeSpOG106fKIuVwvDV%0AvLwp%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353772056/ebf07ae08c58c715fb7cf1b29944/Templates+-+Add+Custom+Card.png?expires=1784333700&signature=c4de4a5622f51dce16f4193ea373984221adfb99abb10de78a7d7c4f7634d0f6&req=dSMiFc55n4FaX%2FMW1HO4zU0FXKx34S13LqJsXHU2OYQeSpOG106fKIuVwvDV%0AvLwp%0A)
2. Edit the card to customize the data displayed.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353763217/00f3fc188255473d221676c5327f/Templates+-+Edit+Custom+Card.png?expires=1784333700&signature=acb87d4c5f41c12037ed9745c7ffa3b3ba123cb2e710aadb6e75b3e34d9f7843&req=dSMiFc54noNeXvMW1HO4zQW64nKWkR31kssKm8Hpd3KJWntlSQoPp%2BZ5WZZM%0AO9pr%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353763217/00f3fc188255473d221676c5327f/Templates+-+Edit+Custom+Card.png?expires=1784333700&signature=acb87d4c5f41c12037ed9745c7ffa3b3ba123cb2e710aadb6e75b3e34d9f7843&req=dSMiFc54noNeXvMW1HO4zQW64nKWkR31kssKm8Hpd3KJWntlSQoPp%2BZ5WZZM%0AO9pr%0A)
3. Name the custom card by replacing 'untitled' at the top of the sidesheet.
4. Select an icon for the custom card.
5. If you wish to limit the number of fields that you want to show on the card, input a numerical limit.
6. Add the data fields of your choice using the Add Field button.
7. When done, click **Save** in the top right corner.

### Video Guide

## Editing Card Layout

The layout and configuration options let you tailor how cards appear in the profile.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353798405/75219db36ecc923d6dc677a0c576/Templates-Reorder%2BCards.png?expires=1784333700&signature=377ac73689822e823da840f627d8d758d5f2d8cd7a4b3bbbe1dccafdf9c33d72&req=dSMiFc53lYVfXPMW1HO4zYzYV0YJ5XsBR9FwZ5TNn7k9MzfUctU9TyAn1ZqQ%0AaKHKHQXhZISEGK0B6Uo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353798405/75219db36ecc923d6dc677a0c576/Templates-Reorder%2BCards.png?expires=1784333700&signature=377ac73689822e823da840f627d8d758d5f2d8cd7a4b3bbbe1dccafdf9c33d72&req=dSMiFc53lYVfXPMW1HO4zYzYV0YJ5XsBR9FwZ5TNn7k9MzfUctU9TyAn1ZqQ%0AaKHKHQXhZISEGK0B6Uo%3D%0A)

* **Change Width:** Choose between single, double, or triple-column widths. Larger widths often display more information or functionality.
* **Collapse:** Show only the title, acting as a shortcut to the side sheet.
* **Reorder Cards:** Use the **Move to Previous** or **Move to Next** options to rearrange cards in the profile template.
* **Remove Card:** Remove a card from the template if it’s no longer needed.

---