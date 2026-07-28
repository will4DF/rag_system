---
title: 📌 Decisions: Frequently Asked Questions
url: https://help.element451.com/en/articles/9251710-decisions-frequently-asked-questions
collection: Decisions
---

This article answers commonly asked questions about Decisions, providing quick solutions and key insights.

[![Pardon our progress as we actively develop this article.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389331925/66376893b62dc47661bfdaecebc5/Pardon%2Bour%2BProgress.png?expires=1784333700&signature=4b0775d977d2f493544eaf45c7b206817da0fa5f9f24b8e186b98eb2622fe3d4&req=dSMvH8p9nIhdXPMW1HO4zQqi3UwaNygofsdkrU85zWGDSlhxXqWst962x3o%2B%0A9Aq7nyCT5zxI%2Fnj9XEg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389331925/66376893b62dc47661bfdaecebc5/Pardon%2Bour%2BProgress.png?expires=1784333700&signature=4b0775d977d2f493544eaf45c7b206817da0fa5f9f24b8e186b98eb2622fe3d4&req=dSMvH8p9nIhdXPMW1HO4zQqi3UwaNygofsdkrU85zWGDSlhxXqWst962x3o%2B%0A9Aq7nyCT5zxI%2Fnj9XEg%3D%0A)

# General

### Why are some decisions missing from All Decisions? I submitted a test application, but it's not visible in Decisions.

This is likely a **permissions issue**. To check:

1. Navigate to **Applications > Decisions > Decision Settings**.
2. Open the **Groups + Permissions** tab.
3. Locate the permission group for yourself or the affected user.
4. Ensure the group has access to **all relevant** permissions.

Updating permissions should allow the missing decisions to appear.

### Is it possible to export notes from the Decision module?

Decision notes cannot be exported from the Decision module. As a workaround, you can add the decision notes to the contact record notes, which are exportable. For added organization, consider creating a custom note type (e.g., "Application" or "Decision") so you can easily categorize these notes when adding them to the contact record.

### How can I grant view-only access to documents?

To grant view-only access to documents, include permissions like **View Profiles** and **Access Decisions**. Avoid adding **Administer Documents**, as that permission provides full control rather than just view-only access.

---

# Cohorts, Stages, and Statuses

### I updated the conditions for my cohort, but it is not updating.

[Cohorts](https://help.element451.com/en/articles/9235440-decisions-cohorts) are recalculated only when the **conditions** **defining** **them** **are** **changed**. Changing the segment that a cohort references does not automatically trigger a re-evaluation of the cohort. This can lead to inconsistencies if updates to segments are expected to influence existing cohorts. To manually trigger a cohort re-evaluation, toggle the cohort's active state to inactive and then back to active.

### I added a new cohort, stage, or status, but I can't see it.

It is likely that you are missing permission to see it. By default, when you add new cohorts, stages, and statuses, they are **not** automatically assigned to any permission groups. This means they are not visible to you or other internal users. You need to **adjust your permissions**. [Click here for a step-by-step guide to adjusting permission groups](https://help.element451.com/en/articles/9235440-decisions-cohorts).

---

# Checklists

### How can I customize checklist requests for different applicant types?

You can customize checklist visibility in **Decision Settings > Checklist** by adjusting the **'Visible To'** setting. This allows you to restrict checklist items based on **user segment or segment reference**, ensuring only relevant applicants see specific requests.

Additionally, checklist items can have **conditions** to further refine visibility. For example, you can hide the transcript request for international applicants while keeping it visible for domestic students.

For step-by-step guidance, visit our help article: [Decisions Checklists](https://help.element451.com/en/articles/9210688-decisions-checklists).

---

# Intelligent Admissions

### My IA rule isn't executing as expected, and I'm using the Application (All Properties) filter.

Rules that rely on **Application (All Properties)** filters can sometimes misfire because those filters are evaluated *before* the full application data finishes syncing. This timing mismatch can cause your rule to skip or trigger incorrectly.

To avoid this, use **Decision conditions** or **Decision segment filters** instead. These re-evaluate *after* the application sync completes, ensuring your logic runs on the most accurate and complete data—like updated GPA, transcript details, or evaluation results.

---

# Packages

### Can I use the same custom field tokens in a Package letter that I use in Campaigns?

The [Tokens](https://help.element451.com/en/articles/9236362-decisions-packages#h_1ce924fabe) feature within Decisions operates differently than tokens in other platform modules. If you wish to insert custom data, you first must create **token placeholders** and then **assign those** **tokens a value at the application decision level**.

---

# Reviewing + Scoring

### Why Didn't the Last Reviewer Field Update?

The Last Reviewer field updates only in specific scenarios, such as when the application's status or stage is changed. However, actions like updating a checklist item do not trigger changes to the Last Reviewer field. For more details, check out the Anatomy of the Application Overview section within [this help article](https://help.element451.com/en/articles/9241630-reviewing-processing-application-decisions#h_8053cb3325).

---