---
title: Column Setting Options for Exports
url: https://help.element451.com/en/articles/9007047-column-setting-options-for-exports
collection: Data Management
---

Explore the setting options for the columns in your export.

# Overview

While building an export, you will have simple mappings where you are exporting a text field, First Name is a great example, but you will also have advanced mappings where you are trying to export a dropdown field with a specific code recognized by your Student Information System. When mapping to dropdown, checkbox, radio, and date field types, there are extra steps you can take to format the data on its way out. Also, some fields may need to be scoped to certain objects like applications and milestones since records can have multiple applications and milestones.

## Accessing Column Setting Options for Exports

Within the export task you are working on, once you have mapped the fields you want to add to your export, the column’s settings will show up under the

[![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idMgS3J5rIHC%2FLfJEvjZEmpaDii%0A9S16xZX3L16YdS6Q%2Bg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idMgS3J5rIHC%2FLfJEvjZEmpaDii%0A9S16xZX3L16YdS6Q%2Bg%3D%3D%0A)

more button.

[![](https://downloads.intercomcdn.com/i/o/976026252/ed8696a58d2bb981e605c86f/Screenshot+2024-02-27+at+5_27_35%E2%80%AFPM.png?expires=1784333700&signature=35edcce07f3ef087dbe8bd63733698bde6e6deb306cac372794e6fafb17d3a70&req=fSchFst4n4RdFb4f3HP0gDpOCIheZuMdWiBL6P9OE57KNh00Zq4nYoJWh4DN%0A94BOABKFm0%2FYvMRaFg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976026252/ed8696a58d2bb981e605c86f/Screenshot+2024-02-27+at+5_27_35%E2%80%AFPM.png?expires=1784333700&signature=35edcce07f3ef087dbe8bd63733698bde6e6deb306cac372794e6fafb17d3a70&req=fSchFst4n4RdFb4f3HP0gDpOCIheZuMdWiBL6P9OE57KNh00Zq4nYoJWh4DN%0A94BOABKFm0%2FYvMRaFg%3D%3D%0A)

## Column Setting Options for Exports

* **Transformations**: Telling exports how to format the data, and transform the data as needed.
* **Validations**: Ensuring data meets certain criteria before being exported.
* **Empty Values**: Telling the export what to do with the blank cells.
* **Scope**: Defining what the column is related to, such as an application or milestone.

---

# Transformations

Transformations allow you to perform basic changes to the data in your file and tell the export what format to send a field over, like whether to send the code or label on a dropdown field. Basic transformations include the following:

* **Uppercase**: All alpha characters will be changed to uppercase
* **Lowercase**: All alpha characters will be changed to lowercase
* **Titlecase**: Capitalize the first letter of each word in a string
* **UCFirst**: Capitalize the first letter of an entire string
* **Trim**: Remove any leading or trailing spaces from a field
* **Append**: Add characters to the beginning of a field
* **Prepend**: Add characters to the end of a field
* **Replace**: Replace a string with another string
* **Substring**: Extract a set of characters from within the middle of a field

To set up basic transformation:

1. Click on the

   [![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)

   more button and click **Settings**.
2. Navigate to the **Transformation** tab and **+ Add transformation type**
3. Select the **Transformation** and click **Done**

## System Mapping

System Mapping will show as an option on the Transformation tab when you are exporting dropdown, checkbox, and radio field types. This transformation will let you export data as different formats like codes, labels, Guids, and more. To set up the System Mapping:

1. Click on the

   [![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)

   more button and click **Settings**.
2. Click the pencil icon on the **Transformation** tab.
3. Set the **Represent As** field to whatever format you want the field to export as. Not sure what option to pick? Refer to your [Field Management](https://help.element451.com/en/articles/9118615-field-management) to see what data source is being used in that field.
4. Check the **Enabled** box to make the transformation active.

[![](https://downloads.intercomcdn.com/i/o/976070139/906c9481a4165def86cd0278/Screenshot+2024-02-27+at+7_12_24%E2%80%AFPM.png?expires=1784333700&signature=97ffd0a1836432831176191ed7c82b513ec02b45c018ee973f7f2a29830af159&req=fSchFs5%2BnIJWFb4f3HP0gJmFQAUxDvzoDsmKI%2FD5I%2FmrphOo1U8hNlYPZcuV%0AFJE%2F4JIbCh7szvMDNg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976070139/906c9481a4165def86cd0278/Screenshot+2024-02-27+at+7_12_24%E2%80%AFPM.png?expires=1784333700&signature=97ffd0a1836432831176191ed7c82b513ec02b45c018ee973f7f2a29830af159&req=fSchFs5%2BnIJWFb4f3HP0gJmFQAUxDvzoDsmKI%2FD5I%2FmrphOo1U8hNlYPZcuV%0AFJE%2F4JIbCh7szvMDNg%3D%3D%0A)

## Format Date

Format Date will show as an option on the Transformation tab when you are exporting a date field. The default date/time format is *2018-10-09 19:37:58,* however, changing this format is relatively straightforward. To set up the Format Date Settings:

1. Click on the

   [![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)

   more button and click **Settings**.
2. Navigate to the **Transformations** tab.
3. Select the **Date Format** that you would like the date exported as. The date formats are associated to PHP date formats.
4. For datetime fields (fields that include both a date and time), the "Use configured client timezone" option is enabled by default, exporting dates and times in your instance's configured timezone rather than UTC. For date-only fields (such as Date of Birth, Test/Evaluation Dates, and Custom Date Fields), this option is not available, as timezone conversion on date-only values can shift the date by a day.

---

# Validations

Validations are a way to set up requirements on your export on specific fields. Here are the validations available to you within Element451:

* **Required**: Make this field required
* **Letter Only**: Ensure this field contains only alpha values
* **Email**: Ensure the field is in a recognizable email format (@element451.com)
* **Maximum Length**: Sets the maximum number of characters that can be entered into this field
* **Minimum Length**: Sets the minimum number of characters that can be entered into this field
* **Between Lengths**: Sets a minimum and maximum number of characters that can be entered into this field
* **After Date**: Ensure this field is after a certain date
* **Before Date**: Ensure this field is before a certain date

To set up the Validation Settings:

1. Click on the

   [![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)

   more button and click **Settings**.
2. Navigate to the **Validations** tab.

---

# Empty Values

Empty Values are a way to tell the system to do something when it comes across an empty cell. Here are the empty value actions you may see within Element451:

* **Export It**: Exports as is
* **Don’t Export It**: Does not put anything in the field
* **Fill with null**: Inserts null in the field
* **Fill with empty string**: Inserts an empty string
* **Fill with current date and time**: Inserts the current date and time into the date field

To set up the Empty Value Settings:

1. Click on the

   [![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)

   more button and click **Settings**.
2. Navigate to the **Empty values** tab.

---

# Scoping

When exporting certain data fields that students can have multiples of, applications, milestones, schools, test scores, it may be necessary to clarify what application type to extract from, what test score type to extract the math score from, and so forth. To set up the Scope Settings:

1. Click on the

   [![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idWhSvA3JhsR7LmnmykzYTLOJy%2B%0Ajqc%3D%0A)

   more button and click **Settings**.
2. All fields that need to be set up will show on the **Scope** tab.

---

# Item to Export + Order By

When you export data that a record can have multiples of, such as event registrations, the Export Settings include an **Item to Export** option (First or Last) and an **Order By** option.

**Order By** controls how each individual record's items are sorted before the export selects the First or Last one. For example, ordering event registrations by date ascending and selecting Last exports each person's most recent registration.

🚨 **Important:** These settings do not sort the rows of the exported file. Sorting the entire CSV is not supported during export; exports are processed in batches, so row order in the final file is not configurable. To sort the full file, open it in a spreadsheet app such as Excel or Google Sheets after downloading.

---