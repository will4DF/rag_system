---
title: Field Management
url: https://help.element451.com/en/articles/9118615-field-management
collection: Data Management
---

Learn about field types and how to use and create them.

# Overview

This article assumes you have an understanding of [Data Sources](https://help.element451.com/en/articles/2066888-data-sources).

Data fields are the foundation of data collection in Element451. Applications, Event registrations, Appointments, Forms, and more use data fields to allow students to submit information about themselves, which updates their records.

[![](https://downloads.intercomcdn.com/i/o/1003343524/65bdfa6836d2efe7613861b9/Important+-+Orng.png?expires=1784333700&signature=cd71b56e65c57c71cd98b9623c71ca9eccc83958fb19817472b588c9a0f33637&req=dSAnFcp6noRdXfMW1HO4zUmWip1or%2BMSWnPH9LCq14yExK2eJyin7Q%2ByBczq%0AGlTAU4tytCKdKKq8mDs%3D%0A)](https://downloads.intercomcdn.com/i/o/1003343524/65bdfa6836d2efe7613861b9/Important+-+Orng.png?expires=1784333700&signature=cd71b56e65c57c71cd98b9623c71ca9eccc83958fb19817472b588c9a0f33637&req=dSAnFcp6noRdXfMW1HO4zUmWip1or%2BMSWnPH9LCq14yExK2eJyin7Q%2ByBczq%0AGlTAU4tytCKdKKq8mDs%3D%0A)

Some fields, such as a drop-down menu, only have specific options that can be selected. A Data Source manages those options. In some cases, we may want to switch the Data Source that powers the Field or create a new Field altogether. This will be accomplished in the Field Management Module.

---

# Field Management

Navigate to **Data + Automation** > **Field** **Management** to see and manage your fields**.** Fields are managed across three different tabs:

## Fields Tab

The **Fields** tab lists the pre-defined fields in Element451 **that can be edited**. It's important to note this is a partial list; numerous other fields exist beyond what's displayed here. Explore all fields while editing an Application or other form in Element451 for a full scope. This tab also serves as your interface for modifying the Data Source for these system Fields.

### How To: Editing a Field

Important: Before editing a Field, be sure the system data source is not suitable to your needs.   
​

[![](https://downloads.intercomcdn.com/i/o/680726935/f485dd019b9a1c5d029de272/Screenshot+2023-02-27+at+4.08.21+PM.png?expires=1784333700&signature=1e7d4142e73abec7612fe36715fb1fd5901b00f95156f1af3f6f170fa401d67c&req=cignEct4lIJaFb4f3HP0gJa0hr2GK1gCDiKUJsd1v4ifW8sPapn22jiMSMHV%0AF4Bc3vd3nK1G0QlxZQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/680726935/f485dd019b9a1c5d029de272/Screenshot+2023-02-27+at+4.08.21+PM.png?expires=1784333700&signature=1e7d4142e73abec7612fe36715fb1fd5901b00f95156f1af3f6f170fa401d67c&req=cignEct4lIJaFb4f3HP0gJa0hr2GK1gCDiKUJsd1v4ifW8sPapn22jiMSMHV%0AF4Bc3vd3nK1G0QlxZQ%3D%3D%0A)

1. Navigate to **Data + Automation** > **Field Management.**
2. Click the **Fields** tab from the left-hand menu.
3. Click the **three** **dots** at the end of the row of the field you wish to edit.
4. Click **Edit**.
5. The ***Use Default Data Source*** toggle will be on by default. Set the toggle to ***No*** to change the Data Source.
6. Select a data source. The ***Select Data Source*** field will populate a list of all System Data Sources, Regular Data Sources, and Reference Data Sources in your Element451 instance. Explore more about [Data Source types](https://help.element451.com/en/articles/2066888-data-sources#h_1b2553a10d).
7. Select the columns of that data source that should be the **name** and **value** of the Data Source.

   * Name: What is displayed to users when they interact with the field.
   * Value: What is stored in the database.
8. Click **Save**.

📌 **Note**: When you set a specific Data Source on a field (including a Reference Data Source), the limited options apply when students complete the field on forms and application sites. When an internal user edits that field from the Application card on a contact's profile, the full list of data source options remains available by design, so staff can set values that may not be shown to students.

[![](https://downloads.intercomcdn.com/i/o/1085040348/a6d1227ec79b42f945fd9aea/Orange+Divider.png?expires=1784333700&signature=d0c78a443231ad5bb78d959d871aff15010efdfa0fab60b70f661e20ccadcfdc&req=dSAvE8l6nYJbUfMW1HO4zdbmwOFcDUhXb9ip9hW3oN4oHMeavujYKshm6%2BW7%0A27wWULX7pyPjURVlR6Y%3D%0A)](https://downloads.intercomcdn.com/i/o/1085040348/a6d1227ec79b42f945fd9aea/Orange+Divider.png?expires=1784333700&signature=d0c78a443231ad5bb78d959d871aff15010efdfa0fab60b70f661e20ccadcfdc&req=dSAvE8l6nYJbUfMW1HO4zdbmwOFcDUhXb9ip9hW3oN4oHMeavujYKshm6%2BW7%0A27wWULX7pyPjURVlR6Y%3D%0A)

## Groupings Tab

Field **Groupings** function similarly to the Fields described earlier, coming pre-defined within Element451. Each grouping contains several fields you can show or hide while designing an Application or form in another module.  
​  
Take **Home Address** as an example; this Field Grouping encapsulates multiple fields, including Address Lines 1 & 2, City, State, and Country, offering a comprehensive way to collect detailed information. Dive deeper into how [Field Groupings](https://help.element451.com/en/articles/2582910-field-groupings) enhance your forms and applications.

### How To: Editing a Grouping

Important: Before editing a Grouping, be sure the system data sources are not suitable to your needs.   
​

[![](https://downloads.intercomcdn.com/i/o/680733765/dd9fec08df1fe8cb255e532c/Screenshot+2023-02-27+at+4.50.38+PM.png?expires=1784333700&signature=6df2254e98f537c74301b4928fb4a497adc58e16d3a9e2b045c357534a285aa7&req=cignEcp9modaFb4f3HP0gJLrUOuDkv7lV4GtGH1sLqTdxdy6c%2FoueQWoTj0S%0Ax3naKkkrORbSFyVgCA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/680733765/dd9fec08df1fe8cb255e532c/Screenshot+2023-02-27+at+4.50.38+PM.png?expires=1784333700&signature=6df2254e98f537c74301b4928fb4a497adc58e16d3a9e2b045c357534a285aa7&req=cignEcp9modaFb4f3HP0gJLrUOuDkv7lV4GtGH1sLqTdxdy6c%2FoueQWoTj0S%0Ax3naKkkrORbSFyVgCA%3D%3D%0A)

1. Navigate to **Data + Automation** > **Field Management.**
2. Click the **Groupings** tab from the left-hand menu.
3. Click the **three** **dots** at the end of the row of the grouping you wish to edit.
4. Click **Edit**.
5. The ***Use Default Data Source*** toggle will be on by default. Set the toggle to ***No*** to change the Data Source.
6. When editing a Field in the Grouping, the "Select data source" field will populate a list of all System Data Sources, Regular Data Sources, and Reference Data Sources in your Element451 instance. Learn about [Data Source types](https://help.element451.com/en/articles/2066888-data-sources#h_1b2553a10d).
7. Select a data source. The ***Select Data Source*** field will populate a list of all System Data Sources, Regular Data Sources, and Reference Data Sources in your Element451 instance. Explore more about [Data Source types](https://help.element451.com/en/articles/2066888-data-sources#h_1b2553a10d).
8. Select the columns of that data source that should be the **name** and **value** of the Data Source.

   * Name: What is displayed to users when they interact with the field.
   * Value: What is stored in the database.
9. Click **Save**.

[![](https://downloads.intercomcdn.com/i/o/1085040425/e0eb13aa3ffc360ed75c3a3b/Orange+Divider.png?expires=1784333700&signature=1292cc92d11e19274b35065e1f53d2595aa32e7236e29bd051672babff2d08b4&req=dSAvE8l6nYVdXPMW1HO4zQt3sIEM4JI0zZWj7h9izQaQSVEAmcCUZx4BrcVS%0Aacd%2FNJuNa1qLm5qb4hU%3D%0A)](https://downloads.intercomcdn.com/i/o/1085040425/e0eb13aa3ffc360ed75c3a3b/Orange+Divider.png?expires=1784333700&signature=1292cc92d11e19274b35065e1f53d2595aa32e7236e29bd051672babff2d08b4&req=dSAvE8l6nYVdXPMW1HO4zQt3sIEM4JI0zZWj7h9izQaQSVEAmcCUZx4BrcVS%0Aacd%2FNJuNa1qLm5qb4hU%3D%0A)

## Custom Fields Tab

Custom Fields empower you to craft unique fields for data not automatically available in Element451. For instance, Custom Fields can range from "Favorite Pizza Topping" and "Tee Shirt Size" to any other information you wish to gather, offering unparalleled flexibility in data collection.

### How To: Creating a Custom Field

Important: Before creating a Custom Field, check to be sure that the information you want does not already exist in **Fields** or **Field Groupings**. Still not seeing the Field you need? Check all available Fields and Grouping by editing an Application or other form.

1. Navigate to **Data + Automation** > **Field Management.**
2. Click the **Custom Fields** tab from the left-hand menu.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/273951097/ca27c35e1f11d67f298799f7/Screen+Shot+2020-12-04+at+4.39.50+PM.png?expires=1784333700&signature=f8cd1010a6bc39c8499181b13da6d1e2dca165f312df8aa6c13b312b836e02b7&req=dickH8x%2FnYhYFb4f3HP0gPp45H41VLXG%2FOZFteFOe4cjahycPY8x%2BWy289GW%0AiPo%3D%0A)](https://downloads.intercomcdn.com/i/o/273951097/ca27c35e1f11d67f298799f7/Screen+Shot+2020-12-04+at+4.39.50+PM.png?expires=1784333700&signature=f8cd1010a6bc39c8499181b13da6d1e2dca165f312df8aa6c13b312b836e02b7&req=dickH8x%2FnYhYFb4f3HP0gPp45H41VLXG%2FOZFteFOe4cjahycPY8x%2BWy289GW%0AiPo%3D%0A)
3. Click on the **plus sign** icon in the top right corner to add a **Custom Field**.
4. Select a **Field** **Type** from the list. [Field Types are described below](#h_d722d3a236) in the next section.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/681300614/db57f29a128e6dc33fc54afb/Screenshot+2023-02-28+at+10.01.18+AM.png?expires=1784333700&signature=1178866967eaa926865d2ebc052a9798468e0c95cb5aa1beb3078902b45e968e&req=cigmFcl%2Bm4BbFb4f3HP0gPnkVLvqJYjw0JbZy2PxEApEVA0rLsP7hwRUTR0G%0A6GA%3D%0A)](https://downloads.intercomcdn.com/i/o/681300614/db57f29a128e6dc33fc54afb/Screenshot+2023-02-28+at+10.01.18+AM.png?expires=1784333700&signature=1178866967eaa926865d2ebc052a9798468e0c95cb5aa1beb3078902b45e968e&req=cigmFcl%2Bm4BbFb4f3HP0gPnkVLvqJYjw0JbZy2PxEApEVA0rLsP7hwRUTR0G%0A6GA%3D%0A)
5. Click **Next**. You will be taken to a window where you can configure the field.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/482805499/bf52700147804e1b47993432/Screen+Shot+2022-03-18+at+4.56.19+PM.png?expires=1784333700&signature=160e0215a48fb66116632015dbda339dd0866957d56f42fb1b816af3900b62d2&req=cCglHsl7mYhWFb4f3HP0gEbt%2Fop38LfgEOnJrDvKWM6dGxigXp5737fyNM1n%0AMm8%3D%0A)](https://downloads.intercomcdn.com/i/o/482805499/bf52700147804e1b47993432/Screen+Shot+2022-03-18+at+4.56.19+PM.png?expires=1784333700&signature=160e0215a48fb66116632015dbda339dd0866957d56f42fb1b816af3900b62d2&req=cCglHsl7mYhWFb4f3HP0gEbt%2Fop38LfgEOnJrDvKWM6dGxigXp5737fyNM1n%0AMm8%3D%0A)
6. Configure the field:

   * **General** **Tab**:

     + Create a "Slug" that is unique to your school. Slugs are unique identifiers for Fields throughout Element451. Describe what data the Custom Field will capture.
     + Create a Label for your field. This is the header that will appear when selecting this Field in other modules. The label should be descriptive for other Element451 users on your staff. You can update the label to be more student-friendly and include help text when you add the Field to Forms and Applications.
     + Add an internal description for the custom field. This is an internal description, not visible to students.

       - 📌 **Note**: Custom field descriptions are available to Bolt Agents in Bolt Agent Jobs, giving them added context so it’s easier to interpret the fields. Ensure your field descriptions are accurate for optimal results.
   * **Validation** **Tab**:

     + Set global rules for how the data should be input. Validation rules can also be set when the Field is added to a Form or Application.
   * **Field** **Options** **Tab**:

     + The Field Options tab will only appear if you've created a Field that requires a Data Source. A drop-down menu or checkbox will require a Data Source.

       - The Data Source selection screen will look identical to the Fields and Groupings screen. Select a **Data** **Source** and set a **Name** and **Value**.

---

# Field Types

These are the types of fields you can choose from when creating a new field. They're also the type of pre-made and grouped fields that consist of.

[![](https://downloads.intercomcdn.com/i/o/681300474/83f71de9ef7370a36a64ad02/Screenshot+2023-02-28+at+10.01.18+AM.png?expires=1784333700&signature=44dbff773269264a843ac50749f3a27b13d6c92ec8fdfae22ea22d26c46e028b&req=cigmFcl%2BmYZbFb4f3HP0gCS%2BAAhRlHFUpmnB7wKKTfO%2BoCidqXpQnPzTmNR1%0Aj%2Fn3dx9In8uhLamrHw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/681300474/83f71de9ef7370a36a64ad02/Screenshot+2023-02-28+at+10.01.18+AM.png?expires=1784333700&signature=44dbff773269264a843ac50749f3a27b13d6c92ec8fdfae22ea22d26c46e028b&req=cigmFcl%2BmYZbFb4f3HP0gCS%2BAAhRlHFUpmnB7wKKTfO%2BoCidqXpQnPzTmNR1%0Aj%2Fn3dx9In8uhLamrHw%3D%3D%0A)

|  |  |  |
| --- | --- | --- |
| **Field** **Type** | **Description** | **Special** **Note(s)** |
| **Audio/Video** | Allows users to upload an audio or video file. | Supported file types are .mp4, .mov, .wmv, .avi, .mp3, .aac, .ogg, .ogm, .wav, .wma, .webm. |
| **Boolean** | This is a Yes/No, True/False Field. It is displayed as a single box that can be checked. |  |
| **Checkbox** | A list of items is displayed all at once. Multiple items can be selected.    Don’t use the checkbox field type when only one option should be selected (for example, yes/no). | ¹See display option note below under this table |
| **Date** | A date widget that allows users to select a date from a calendar. |  |
| **DateTime** | A date and time widget that allows users to select a date and time from a calendar. |  |
| **Dropdown** | A list of items that appears when the field is clicked. Only one item can be selected. | ¹See display option note below under this table |
| **Radio Button** | A list of items is displayed all at once. Only one item can be selected. | You should use a yes/no data source when using radio buttons, and it must be linked to a regular data source, not a system data source.    If you want to use a true/false data source, use a Boolean field type instead.    ¹See display option note below under this table |
| **Text** | Users can enter a single line of text. |  |
| **Text Area** | Users can enter multiple lines of text, which is useful when you expect the information to span more than a sentence.    Note: Custom `text area` fields are not supported in filters and segments. |  |
| **Upload** | Allows users to upload a file. | Supported file types are .pdf, .doc, .docx, .txt, .odt, .jpg, .jpeg, .png, .gif, .csv, .ppt, .pptx, .svg, .xls, .xlsx, .html, .bmp, and .htm. |
| **Multiple Upload** | Allows students to upload multiple files at once. Supported file types are the same as Upload. |  |

¹**About the 'Display Option' for Multi-Value Fields**

For field types that allow multiple options, such as Radio Button, Dropdown, and Checkbox, you can adjust the **Display Option** setting when adding the field to a form. If you choose to switch the display option to **Toggle**, use it **only** when the field has two or three short, simple options (for example, Yes/No or Male/Female). Toggle is not designed for long lists or labels. On mobile devices, long or multiple toggle options do not wrap neatly and can cause layout issues.

---