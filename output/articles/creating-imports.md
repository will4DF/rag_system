---
title: Creating Imports
url: https://help.element451.com/en/articles/9001231-creating-imports
collection: Data Management
---

How to create a import task.

# Overview

This article walks you through creating an Import Task from scratch. This article will focus on importing a data file. To import documents, visit [Creating Document Imports](https://help.element451.com/en/articles/9011140-creating-document-imports).

**Things to know before importing:**

* Make sure that you have either a .csv or a .txt file.
* Excel files can't be imported and must be saved as .csv or .txt first.
* Data files should always have an identifier, like email or an ID, to prevent duplicate accounts.

---

## Video Guide

---

# Creating a New Import

To create a new import:

1. Navigate to **Data + Automations > Import + Export > Imports.**
2. Click on the **+** button along the right-hand side.
3. Select **Data**, and click **Confirm.**

## Selecting an Import Source

After creating the new import task, a sidesheet will appear for your new import. The first tab to display will be the **Source** tab. You can import files from a variety of sources.

In this example, we'll use the **Computer** source to upload a file from your device. Again, make sure you have either a .csv or a .txt file. Excel files can't be imported and must be saved as .csv or .txt first. Data files should at least have an email address, first name, and last name for each contact.

After selecting **Computer**, click the **Upload File** to select the .csv or .txt file from your desktop.

[![](https://downloads.intercomcdn.com/i/o/977851766/90c91ce3c97e9ae19bc099e6/Screenshot+2024-02-29+at+9_10_04%E2%80%AFAM.png?expires=1784333700&signature=8f786015c770382be144c08d794d507f5944ebfef1940922e752bccb638022dc&req=fScgHsx%2FmodZFb4f3HP0gA70mWvNDKVDWCesdy3mEu6tLHztN6pCTD7oV%2FWO%0Ath8mirDiGbfZnUJh9w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977851766/90c91ce3c97e9ae19bc099e6/Screenshot+2024-02-29+at+9_10_04%E2%80%AFAM.png?expires=1784333700&signature=8f786015c770382be144c08d794d507f5944ebfef1940922e752bccb638022dc&req=fScgHsx%2FmodZFb4f3HP0gA70mWvNDKVDWCesdy3mEu6tLHztN6pCTD7oV%2FWO%0Ath8mirDiGbfZnUJh9w%3D%3D%0A)

✨ **Pro Tip:** When using SFTP, Dropbox, and Google Drive to import from a folder, you can use **\*** as a wildcard for multiple characters, or you can use **[date:now,format=m-d-Y,timezone=local]** to pick up only a file for the current day. For example, if you have a filename "nursing\_data\_5-18-23.csv", you could use the pattern "\*\_data\_[date:now,format=m-d-Y,timezone=local].csv" to import all data files from the current date.

## Mapping

After selecting your file, you can move to the **Mapping** tab. This is where the bulk of your import work will take place. You'll see each of your file columns displayed vertically on the left. The right will be blank, but that is where you will select the Element451 field to which each file column corresponds.

### Templates

Rather than manually mapping the incoming data by hand, you can apply a pre-built template that automatically maps the incoming data to the Element451 fields. A list of system templates is available by default, or you can build your own. The template must match the incoming data file precisely to prevent errors in the import.

In this article, we'll assume you are not using a template.

### Simple Mapping

For some fields, the mapping will be simple. For example, when importing the first name, you can click **Map to Field**, search "First name," and select the first name field.

### Advanced Mapping

Text fields, like First Name, require no additional setup. When you come across fields with dates, dropdown fields, and application fields, there will be additional setup in the field's column settings—open column settings by clicking the

[![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idMgS3J5rIHC%2FLfJEvjZEmpaDii%0A9S16xZX3L16YdS6Q%2Bg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idMgS3J5rIHC%2FLfJEvjZEmpaDii%0A9S16xZX3L16YdS6Q%2Bg%3D%3D%0A)

at the right of each row. Read our [Column Setting Options on Imports](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports) article for more information on the column settings.

Column Setting tabs include:

* **Scope**: Defining what the column is related to, such as an application or milestone. Read more about Scopes.
* **Transformations**: Telling Imports how to understand and transform the data as needed. This is a crucial setup component to ensure that data comes in clean.
* **Validations**: Ensuring data meets specific criteria before being imported.
* **Empty Values**: Telling the system what to do with blank cells.

## Configuration

Once you have completed the mapping, you will set up additional settings for your import.

### Matching Settings

Matching will prevent duplicate records from being created and assist with the settings selected for Importing Only New People and Updating Existing People. It's common to match on email address, but all imported identity fields can be matched.

Note: The same email address can appear multiple times in an import file. However, to prevent duplicates, be sure to set your **matching criteria** to both **Email AND Student ID**. This ensures each record is properly identified and prevents unintended duplicates.

[![](https://downloads.intercomcdn.com/i/o/977861947/cb35a3cf7ea947b8da3cb341/Screenshot+2024-02-29+at+9_17_45%E2%80%AFAM.png?expires=1784333700&signature=ca04733311d5260e673b5d86666914b5a9dab288615aab427cfb6046b3d28bae&req=fScgHs9%2FlIVYFb4f3HP0gI4Jv9E5eyHsvISKnAu3CgGtCfDsctrN13uqSSrV%0ALmW4AHdZ5kQzx%2BzcSQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977861947/cb35a3cf7ea947b8da3cb341/Screenshot+2024-02-29+at+9_17_45%E2%80%AFAM.png?expires=1784333700&signature=ca04733311d5260e673b5d86666914b5a9dab288615aab427cfb6046b3d28bae&req=fScgHs9%2FlIVYFb4f3HP0gI4Jv9E5eyHsvISKnAu3CgGtCfDsctrN13uqSSrV%0ALmW4AHdZ5kQzx%2BzcSQ%3D%3D%0A)

When multiple matching fields are selected, all of them are used together to decide whether a record should be updated, created, or skipped. This applies for any unique ID combination.  
​  
For example, assume your file includes both SSN and email for everyone:

* If the incoming record only has an email, and that email matches an existing profile, Element will match on email and add the SSN to the existing account.
* If the incoming record only has an SSN, and that SSN matches an existing profile, Element will match on SSN and add the email to the existing account.
* If the SSN matches one existing profile and the email matches a different profile, Element will skip the record, since it cannot determine which profile should be updated. Neither field is prioritized; they are treated equally.
* If the existing profile already has both SSN and email, Element will match successfully and update the record.
* If no matches are found, Element will create a new record.

🔎 Hint: Not seeing fields in the **Matching Settings**? Make sure you have an identity field mapped in your import.

### Destination and Source Settings

Here, you can decide what to do with the records coming in from the import and define the type of file that is coming in.

* **Import Only New People**: Using a unique identifier, like email address, as Element451 imports the data, if it finds a pre-existing record in the system, the record will get skipped. Only new records will be imported and created**.**
* **Update Existing People**: Using a unique identifier, like email address, as Element451 imports the data, if it finds a pre-existing record in the system, it will update it with the new information coming in from the file. No new records will be created.
* **Update Existing and Import Only New People**: Using a unique identifier, like email address, as Element451 imports the data, it will try to find a pre-existing record to update. It will create a brand-new record if it cannot find a pre-existing one.
* **Delimiter Character**: Clarify how the data is separated in the file. The default is Comma.
* **Skip Rows**: Specify a number of rows to skip at the top of the file before headers and data are parsed. Use this when your file includes metadata rows above the header — for example, an export with several rows of report information before the column headers begin. Leave at 0 if your file starts with the header row or with data. The **Skip First Row** toggle is then evaluated against the first remaining row after these are skipped.
* **Skip First Row**: Clarify if the first row in your file should be imported, meaning it contains column header names and not actual record data.

[![](https://downloads.intercomcdn.com/i/o/977862523/afab708740838412e45f4ec5/Screenshot+2024-02-29+at+9_18_03%E2%80%AFAM.png?expires=1784333700&signature=33993b1d968df1b540771bc5760fc2ce620330251136b468aa720abfb98a817c&req=fScgHs98mINcFb4f3HP0gB8NJ0QZXrgmu5JrGyFBaNPL3NMp4urygEYNPqt9%0AyH6Cq9vR3ozsueMNpw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977862523/afab708740838412e45f4ec5/Screenshot+2024-02-29+at+9_18_03%E2%80%AFAM.png?expires=1784333700&signature=33993b1d968df1b540771bc5760fc2ce620330251136b468aa720abfb98a817c&req=fScgHs98mINcFb4f3HP0gB8NJ0QZXrgmu5JrGyFBaNPL3NMp4urygEYNPqt9%0AyH6Cq9vR3ozsueMNpw%3D%3D%0A)

## Groups and User Type

This set of settings will allow you to do the following:

* **Create New Segment**: Create a segment for records affected by your import (This can be helpful when debugging imports).

  + 📌 **Note:**

    - Segments created by an import will **not** have a value for "created by."
    - Each segment created is tied to that specific import when running an import. Changing the ‘New Segment Name’ field will not create a new segment or rename the existing one. To create a new segment, you must duplicate the import template and run a new import, as only one segment can be created per import.
* **Default User Type**: By default, all imported records are assumed to be students. This can be changed to Family or Influencer.

[![](https://downloads.intercomcdn.com/i/o/977863659/ded160be29e45e31a26f256c/Screenshot+2024-02-29+at+9_18_34%E2%80%AFAM.png?expires=1784333700&signature=af9c178ccbec51d2c8579ed60f0597e69bc1a20297c7b8ffe82c1b8b8d8a3697&req=fScgHs99m4RWFb4f3HP0gFDLnrVGkSHmN3NHQVe%2FUHNKGcfG7dNPbqH6OFnx%0A11IAnff6j8iCkoIdKg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977863659/ded160be29e45e31a26f256c/Screenshot+2024-02-29+at+9_18_34%E2%80%AFAM.png?expires=1784333700&signature=af9c178ccbec51d2c8579ed60f0597e69bc1a20297c7b8ffe82c1b8b8d8a3697&req=fScgHs99m4RWFb4f3HP0gFDLnrVGkSHmN3NHQVe%2FUHNKGcfG7dNPbqH6OFnx%0A11IAnff6j8iCkoIdKg%3D%3D%0A)

## Preview

The **Preview** tab will allow you to preview records in your import to confirm that everything looks good. If there are any errors in the formatting of those records, you'll see a yellow yield sign on the right side of the screen. Read our article on [Data Quality](https://help.element451.com/en/articles/9006443-data-quality-guide) for a guide and reference on how the preview screen should look.

[![](https://downloads.intercomcdn.com/i/o/977864413/a7c230c319ae02e8b78d599e/Screenshot+2024-02-29+at+9_19_02%E2%80%AFAM.png?expires=1784333700&signature=6ace626632605602a60ff1ecb48a3da5bad1c7029dc1918c92659cef45396ef3&req=fScgHs96mYBcFb4f3HP0gDXC0hx4cKrJREZv2XLXakBfywm5xPJP0pQgOMv%2B%0AGH6Q2hl0SZYp0Pee7w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977864413/a7c230c319ae02e8b78d599e/Screenshot+2024-02-29+at+9_19_02%E2%80%AFAM.png?expires=1784333700&signature=6ace626632605602a60ff1ecb48a3da5bad1c7029dc1918c92659cef45396ef3&req=fScgHs96mYBcFb4f3HP0gDXC0hx4cKrJREZv2XLXakBfywm5xPJP0pQgOMv%2B%0AGH6Q2hl0SZYp0Pee7w%3D%3D%0A)

## Run Import

After mapping and previewing the incoming data, you are ready to move on to running the import task.

### Test Import

📌 **Note:** At this time, you cannot use the test import function if you are importing relationships, such as parent information.

Before you run, test your import with the **Test Import** button at the top of the import task. This will simulate how many records will be created or updated and how many rows will be skipped without affecting the records. The database will not get updated when testing tasks. To view the results from the **Test Import**, click the **Run History** tab.

### Run Import

Once you've tested and are ready to execute your task, click **Run Import** (if running immediately) or **Schedule** (if running on schedule). Schedules can mean a one-time run in the future or a repeated run. Read more about [Scheduling Imports](https://help.element451.com/en/articles/9007716-scheduling-import-export).

## Run History

The **Run History** tab shows the results of all runs and tests executed by the import. Each run result will show the number of records added or updated by the run and the number of skipped rows in the data file. If a row is skipped, the results will show a warning. Read these warnings to understand why rows were skipped.

---