---
title: Column Setting Options for Imports
url: https://help.element451.com/en/articles/9006325-column-setting-options-for-imports
collection: Data Management
---

Explore setting options for the columns in your imports.

# Overview

While building an import, you will have simple mappings where you are mapping free text to a text field, First Name is a great example, but you will also have advanced mappings where you are trying to bring data into a dropdown field. When mapping to dropdown, checkbox, radio, and date field types, there are extra steps to ensure Element451 interprets the incoming data correctly. Also, some fields may need to be scoped to certain objects like applications and milestones since records can have multiple applications and milestones.

## Accessing Column Setting Options for Imports

Within the import task you are working on, once you have mapped the incoming data to a field in Element451, the column’s settings will show up under the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button.

[![](https://downloads.intercomcdn.com/i/o/977866553/291f0978593f0ab683bfc0a7/Screenshot+2024-02-29+at+9_19_56%E2%80%AFAM.png?expires=1784333700&signature=8cd40b98a605c216c6719c828dde2117bc6e9e315ad04f91ca90a23f6dfd7218&req=fScgHs94mIRcFb4f3HP0gMxl0Yt0sJnmBOAvWp2gmqQYfjDg6fq%2BN%2Bph5qSH%0A2d%2Fd8J8RUy3ndbDoxw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977866553/291f0978593f0ab683bfc0a7/Screenshot+2024-02-29+at+9_19_56%E2%80%AFAM.png?expires=1784333700&signature=8cd40b98a605c216c6719c828dde2117bc6e9e315ad04f91ca90a23f6dfd7218&req=fScgHs94mIRcFb4f3HP0gMxl0Yt0sJnmBOAvWp2gmqQYfjDg6fq%2BN%2Bph5qSH%0A2d%2Fd8J8RUy3ndbDoxw%3D%3D%0A)

## Column Setting Options for Imports

* **Transformations**: Telling imports how to understand the data and transforming the data as needed.
* **Validations**: Ensuring data meets certain criteria before being imported.
* **Empty Values**: Telling the import what to do with the blank cells.
* **Scope**: Defining what the column is related to, such as an application or milestone.

---

# Transformations

Transformations allow you to perform basic changes to the data in your file and tell the import how to read the incoming data for dropdown, checkbox, radio, and date field types. Basic transformations include the following:

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

1. Click on the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button and click **Settings**.
2. Navigate to the **Transformation** tab and **+ Add transformation type**
3. Select the **Transformation** and click **Done**

## System Mapping

System Mapping will show as an option on the **Transformation** tab when you are mapping to dropdown, checkbox, and radio field types. The System Mapping transformation is vital to getting Element451 to interpret the incoming data. Each dropdown, checkbox, and radio fields are associated with data sources, so indicating what values from the data source are coming in from the file helps Element451 match the values to one another. To set up the System Mapping:

1. Click on the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button and click **Settings**.
2. Click the pencil icon on the **Transformation** tab.
3. Set the **Interpret As** field to whatever format is coming into Element451. Not sure what option to pick? Refer to your [Field Management](https://help.element451.com/en/articles/9118615-field-management) setup to see what data source is being used in that field.
4. Check the **Enabled** box to make the transformation active.

[![](https://downloads.intercomcdn.com/i/o/975826456/d9c26bc579f85f6c232cd602/Screenshot+2024-02-27+at+12_57_35%E2%80%AFPM.png?expires=1784333700&signature=d5d0e69733363ad92458f5f99e1ec60fc523fbd38b2457d72ee006915b2bb012&req=fSciHst4mYRZFb4f3HP0gOoCBimrPNwyrIRaKb0pHNqshvdG5my2OxduwtUe%0AOySqw74jMRyv7tl9fQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/975826456/d9c26bc579f85f6c232cd602/Screenshot+2024-02-27+at+12_57_35%E2%80%AFPM.png?expires=1784333700&signature=d5d0e69733363ad92458f5f99e1ec60fc523fbd38b2457d72ee006915b2bb012&req=fSciHst4mYRZFb4f3HP0gOoCBimrPNwyrIRaKb0pHNqshvdG5my2OxduwtUe%0AOySqw74jMRyv7tl9fQ%3D%3D%0A)

## Format Date

Format Date will show as an option on the Transformation tab when you are mapping to a date field type. Date fields coming from different data sources like the Common App, CollegeBoard, or even your own Student Information System have their own date formats. The default date/time format accepted is *2018-10-09 19:37:58* or *2018-10-09*, however, changing this format is relatively straightforward. To set up the Format Date Settings:

1. Click on the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button and click **Settings**.
2. Navigate to the **Transformations** tab.
3. Select the **Date Format** that matches with what is on the data file you are importing. The date formats are associated with PHP date formats.
4. For datetime fields (fields that include both a date and time), the "Use configured client timezone" option is enabled by default, reading incoming dates and times in your instance's configured timezone rather than UTC. For date-only fields (such as Date of Birth, Test/Evaluation Dates, and Custom Date Fields), this option is not available, as timezone conversion on date-only values can shift the date by a day.

![](https://downloads.intercomcdn.com/i/o/978059500/b8662fcd2cc27527daab7b68/Pro+Tip+-+Orange.png?expires=1784430000&signature=0f5d0782a6db6c6d57580ccbaaae08c8f9366c433470c737079f7c3847f92d52&req=fScvFsx3mIFfFb4X1HO4gT8tbN803ZVYeo0DjSHwyo6yKnJ4um99duWklo1m%0A) To ensure your Format Date is set up correctly, head to the Preview tab of your import. On the left-hand side, you should see the format found within your data file. On the right-hand side, that same date should appear but in a different format, Y-m-d\TH:i:sP.

---

# Validations

Validations are a way to ensure that the data you're entering into a field is in the correct format. Here are the validations available to you within Element451:

* **Required**: Make this field required on an import
* **Letter Only**: Ensure this field contains only alpha values
* **Email**: Ensure the field is in a recognizable email format (@element451.com)
* **Maximum Length**: Sets the maximum number of characters that can be entered into this field
* **Minimum Length**: Sets the minimum number of characters that can be entered into this field
* **Between Lengths**: Sets a minimum and maximum number of characters that can be entered into this field
* **After Date**: Ensure this field is after a certain date
* **Before Date**: Ensure this field is before a certain date

To set up the Validation Settings:

1. Click on the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button and click **Settings**.
2. Navigate to the **Validations** tab.

---

# Empty Values

Empty Values are a way to tell the system to do something when it comes across an empty cell. Here are the empty value actions you may see within Element451:

* **Import It**: Imports as empty.
* **Don’t Import It**: Does not put anything in the field.
* **Fill with null**: Inserts null in the field.
* **Fill with empty string**: Inserts an empty string.
* **Fill with current date and time**: Inserts the current date and time into the date field.

To set up the Empty Value Settings:

1. Click on the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button and click **Settings**.
2. Navigate to the **Empty values** tab.

---

# Scoping

When importing data into objects that students can have multiples of, applications, milestones, schools, and test scores, it may be necessary to clarify what application type to put the application data on, what test score type to associate the math score to, and so forth. To set up the Scope Settings:

1. Click on the ![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784430000&signature=fae0d35be743ffb2db1e1927092d0210e046c3ee74b4399385f406418e799f2b&req=fSEmE8t5m4lZFb4X1HO4gWopCNyJgLEc0F4H3Wcd4JRM%2F8gGu%2FintzmP8LPH%0A) more button and click **Settings**.
2. All fields that need to be set up will show on the **Scope** tab.

---