---
title: Creating Exports
url: https://help.element451.com/en/articles/9007317-creating-exports
collection: Data Management
---

# Overview

This article walks you through creating an Export Task from scratch. This article will focus on exporting a data file. To export documents, visit [Creating Document Exports](https://help.element451.com/en/articles/9011277-creating-document-exports).

---

# Creating a New Export

To create a new export:

1. Navigate to **Data + Automations > Import + Export > Exports.**
2. Click on the **+** button along the right-hand side.
3. Select **Data**, and click **Confirm.**

## Selecting a Segment to Export

After creating the new export task, a sidesheet will appear for your new export. The first tab to display will be the **Segment** tab. On this tab, you will identify a pre-built segment of records you want to export.

[![](https://downloads.intercomcdn.com/i/o/977873392/bab8ee9a3dbe72a8589af746/Screenshot+2024-02-29+at+9_25_27%E2%80%AFAM.png?expires=1784333700&signature=973136ab6cdd9c4a120c07ee7dc5814a9085c3787188587a765682b46c2cf9bd&req=fScgHs59nohdFb4f3HP0gOrsGh92cy2xpyjPaiuu8A7tccDPUgRDyEmHi416%0Ao%2BoWWtIXQKheZ78f%2BA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977873392/bab8ee9a3dbe72a8589af746/Screenshot+2024-02-29+at+9_25_27%E2%80%AFAM.png?expires=1784333700&signature=973136ab6cdd9c4a120c07ee7dc5814a9085c3787188587a765682b46c2cf9bd&req=fScgHs59nohdFb4f3HP0gOrsGh92cy2xpyjPaiuu8A7tccDPUgRDyEmHi416%0Ao%2BoWWtIXQKheZ78f%2BA%3D%3D%0A)

## Repeat Fields Based On

Select what each row represents to add a layer of customization to your reports. The default is the person record, but you can select from a list of objects. Other commonly chosen objects are applications, where each row represents an application, and test scores, where each row represents a test.

If your export only includes one task per student, even when set to "Repeat Fields Based On: Task" and "Item to Export: ALL," the issue may lie in the segment filter. Ensure the segment driving the export does not filter tasks, as filters applied to tasks will limit the export to only those matching the filter criteria. Additionally, verify that the segment includes users based on non-task criteria (e.g., submitted forms) to ensure all tasks for those users are exported.

[![](https://downloads.intercomcdn.com/i/o/976085556/5d9a478ccd9f4c073cb09764/Screenshot+2024-02-27+at+7_55_05%E2%80%AFPM.png?expires=1784333700&signature=b866a4a4fa35d914c1693df1de23a8fed2b8f2343f0ea2c3af65b949d125feab&req=fSchFsF7mIRZFb4f3HP0gGHy07xnCvcI1n2AePYJtrKGR3Oj5cJEKS5InIzu%0AccbBcjpQUsEWMpevkQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976085556/5d9a478ccd9f4c073cb09764/Screenshot+2024-02-27+at+7_55_05%E2%80%AFPM.png?expires=1784333700&signature=b866a4a4fa35d914c1693df1de23a8fed2b8f2343f0ea2c3af65b949d125feab&req=fSchFsF7mIRZFb4f3HP0gGHy07xnCvcI1n2AePYJtrKGR3Oj5cJEKS5InIzu%0AccbBcjpQUsEWMpevkQ%3D%3D%0A)

![](https://downloads.intercomcdn.com/i/o/978047656/dcebd51193311da31bb46dc5/Pro+Tip+%281%29.png?expires=1784430000&signature=b02c620a5550f053edcb3da43a1bb15880afb95a4524aa39cf98a1980dbb1e65&req=fScvFs15m4RZFb4X1HO4gT1xjE4rXPSQIb3dSRi1suSzCinEUzJD5mg4GRhG%0A) In addition to changing the Repeat Fields setting, you can add additional export filtering. For example, when repeating rows on applications, you can create a filter only to export applications with specific statuses for a particular term. You can also pull the latest application on their record or their first. These settings are found below the Repeat Fields settings.

For example, if exporting tasks, ensure that the segment does not apply task-specific filters that could limit the data. Instead, base the segment on broader criteria to include all relevant tasks.

---

# Mapping

You can move to the Mapping tab after setting up the audience you want to export. This is where the bulk of your export work will take place.

## Templates

Rather than manually adding columns to your export by hand, you can apply a pre-built template that automatically maps the Element451 fields. A list of system templates is available by default, or you can build your own.

In this article, we'll assume you are not using a template.

## Simple Mapping

For some fields, the mapping will be simple. For example, when exporting the first name, you can click "Map to Field," search "First name," and select the first name field.

## Advanced Mapping

Text fields, like First Name, require no additional setup. Fields with dates, dropdown fields, and application fields will need additional setup in the field's column settings—open column settings by clicking the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) at the right of each row. For more information on the column settings, check out our article on [Column Setting Options for Exports](https://help.element451.com/en/articles/9007047-column-setting-options-for-exports).

Column Setting tabs include:

* **Scope**: Defining what the column is related to, such as an application or milestone. Read more about Scopes.
* **Transformations**: Transform the data as it leaves the system.
* **Validations**: Ensuring data meets specific criteria before being exported.
* **Empty Values**: Telling the system what to do with blank cells.

To avoid duplicate rows when exporting data, you can use the Scope setting to map multiple application-specific columns. For instance, set "Repeat Fields Based On" to Person and add fields for each application instance (e.g., scope 1–N for multiple applications). This consolidates data into a single row with multiple application columns.

---

# Configuration

The **Configuration** tab is where you decide where the export will be delivered and what the file will be named.

### Source Settings

* **Filename**: Determine how the file should be named. To add a timestamp within the file name, you can utilize date tokens, **[date:now,format=m-d-Y,timezone=local]**. For example, app\_submits\_[date:now,format=mdy,timezone=local].csv would export as app\_submits\_02272024.csv
* **Delimiter Character**: Clarify how the data should be separated in the file. The default is Comma.
* **Extension**: Clarify the file extension. The default is Comma Separated Values (.csv).
* **Export first row as a header**: Decide if you want the first row of your export to be column headers. The default is toggled on.

### Destination Settings

* **Email**: A data export task will be delivered to the email address provided. The email will prompt you to **Click to Download**.
* **SFTP**
* **Dropbox**
* **Google Drive**

### Notification

The **Notification** tab allows you to receive an email notification regarding the export status. This is an excellent feature if a daily report gets dropped into the SFTP and you want to know if it delivered without logging into the SFTP.

[![](https://downloads.intercomcdn.com/i/o/977876417/4e1db4cf4d4f1b7c8319e326/Screenshot+2024-02-29+at+9_27_37%E2%80%AFAM.png?expires=1784333700&signature=67f0b948408fca6dbb03fa4d55775fab0e58c46cbb7323b186ffd5d74d16f70b&req=fScgHs54mYBYFb4f3HP0gFIXNDtQc31KaCQkGZvCbHbCXnP7IC355h9R9sxz%0AwgjH3ThEk8Vr%2B1G%2Buw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977876417/4e1db4cf4d4f1b7c8319e326/Screenshot+2024-02-29+at+9_27_37%E2%80%AFAM.png?expires=1784333700&signature=67f0b948408fca6dbb03fa4d55775fab0e58c46cbb7323b186ffd5d74d16f70b&req=fScgHs54mYBYFb4f3HP0gFIXNDtQc31KaCQkGZvCbHbCXnP7IC355h9R9sxz%0AwgjH3ThEk8Vr%2B1G%2Buw%3D%3D%0A)

---

# Preview

The **Preview** tab will allow you to preview records in your export to confirm that everything looks good.

[![](https://downloads.intercomcdn.com/i/o/976096791/5b367af38398a2c89263fd09/Screenshot+2024-02-27+at+8_26_46%E2%80%AFPM.png?expires=1784333700&signature=9b3160c8468ce7d86291fd565b4a15611bc78e998dbf9279088177af66c0e0d2&req=fSchFsB4moheFb4f3HP0gBRiSIycmLRUZXFdXxt9Cn1GCAGUN%2FI66if0DDPu%0ABDUC766McW%2FpsbFxAg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976096791/5b367af38398a2c89263fd09/Screenshot+2024-02-27+at+8_26_46%E2%80%AFPM.png?expires=1784333700&signature=9b3160c8468ce7d86291fd565b4a15611bc78e998dbf9279088177af66c0e0d2&req=fSchFsB4moheFb4f3HP0gBRiSIycmLRUZXFdXxt9Cn1GCAGUN%2FI66if0DDPu%0ABDUC766McW%2FpsbFxAg%3D%3D%0A)

# Run Export

After mapping and previewing the outgoing data, you are ready to move on to running the export task.

Click **Run Export** (if running immediately) or **Schedule** (if running on schedule). Schedules can mean a one-time run in the future or a repeated run.

[Read more about Scheduling Exports →](https://help.element451.com/en/articles/9007716-scheduling-import-export)

## Run History

The **Run History** tab shows the results of all runs executed by the export. Each run result will show the number of records exported by the run and the number of skipped rows in the data file. If a row is skipped, the results will show a warning. Read these warnings to understand why rows were skipped.

# Best Practices for Data Management

* **Plan Your Export Criteria**: Clearly define the data you need before configuring the export.
* **Test Export Settings**: Run test exports to verify the output meets your requirements.
* **Use Filters Wisely**: Avoid overly restrictive filters that may exclude necessary data.

By following these best practices, you can optimize your data exports in Element451, ensuring they are accurate and comprehensive.

---