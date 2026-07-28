---
title: Setting up Integration Codes
url: https://help.element451.com/en/articles/5181322-setting-up-integration-codes
collection: Data Management
---

A step-by-step guide on how to setup integration codes

# Overview

Integration codes allow you to create *additional* mappings for your [data sources](https://help.element451.com/en/articles/2066888-data-sources). These integration codes can be used when working with suspect/prospect lead import tasks, applicant import tasks, or when an additional mapping is required for majors, terms, and degrees.

Element451 provides 5 "custom" integration code slots, as well as slots for the following systems: ACT, Blackboard, Brightspace, Canvas, CIP, Coalition Application, College Board, Common Application, Hobsons, LMS, Naviance, NRCCUA, OpenLMS, and SIS.

Let's explore when and how to use them.

---

# When to Use Integration Codes

For practical data management, we recommend importing and exporting data between Element451 and your Student Information System (SIS). Your SIS codes will be stored in the 'Code' *column of each item.* However, you may need to integrate with other systems (such as an ad platform or LMS). If those systems use separate codes for your SIS, you'll save that additional code as an Integration Code.

📌 **LMS term matching:** The native LMS integrations (Canvas, Brightspace, Blackboard, and OpenLMS) rely on integration codes to match course and section data to your terms. For each term you want to sync, add the integration code for that LMS (e.g., **Canvas**) on the **Terms** data source, with a value matching the term identifier sent by the LMS. Element451 does not fall back to the standard term code, so terms without an integration code will sync in as **No Term**. See your [LMS integration article](https://help.element451.com/en/collections/16479097-courses-lms-integrations) for the exact field to use.

---

# Manually Adding Integration Codes

Integration Codes are added from the Data Sources page in Element451.

1. Navigate to **Data + Automations** > **Data Sources**.
2. Click on the category of your choice (Majors, Terms, Degrees, Campuses, Tests, Schools, or Courses).  
   ​

   [![Click on tab](https://element451.intercom-attachments-7.com/i/o/495341643/ba9e7f5639325b164d86620f/screenshot_520a4dbe-e8c7-4cf6-91b8-6fcc6fba61d4?expires=1784333700&signature=b409adf0fc49c82689af2fb448d5373fc2cd12f61cb5ff7bca4659a4e12f7090&req=cCkiFc1%2Fm4VcFb4f3HP0gGNdeqlFApW8XXOlMbhZJMqRNeRrWaLwh6Zlz1m1%0AYF0%3D%0A)](https://element451.intercom-attachments-7.com/i/o/495341643/ba9e7f5639325b164d86620f/screenshot_520a4dbe-e8c7-4cf6-91b8-6fcc6fba61d4?expires=1784333700&signature=b409adf0fc49c82689af2fb448d5373fc2cd12f61cb5ff7bca4659a4e12f7090&req=cCkiFc1%2Fm4VcFb4f3HP0gGNdeqlFApW8XXOlMbhZJMqRNeRrWaLwh6Zlz1m1%0AYF0%3D%0A)
3. Next to the major, term, etc., click the **pencil icon** to open the editor.  
   ​

   [![Click on cell](https://element451.intercom-attachments-7.com/i/o/495341658/d39ac829bb051ef8dfcf4903/screenshot_9960d215-311b-44b7-933a-5088dd6b2f25?expires=1784333700&signature=e075bc12851cfa9e37a228045339ec62d6300af0db1de027f5cfbc71622f6a88&req=cCkiFc1%2Fm4RXFb4f3HP0gJNQkI3ElfpD7aGplZ9f4Cvu4Bu8okdpZZgQn3Fh%0AeXo%3D%0A)](https://element451.intercom-attachments-7.com/i/o/495341658/d39ac829bb051ef8dfcf4903/screenshot_9960d215-311b-44b7-933a-5088dd6b2f25?expires=1784333700&signature=e075bc12851cfa9e37a228045339ec62d6300af0db1de027f5cfbc71622f6a88&req=cCkiFc1%2Fm4RXFb4f3HP0gJNQkI3ElfpD7aGplZ9f4Cvu4Bu8okdpZZgQn3Fh%0AeXo%3D%0A)
4. Select the Integration Code tab on the modal.
5. Click **+ Add Code** and select an option from the "With" menu. In the example below, we used the "CIP" code.
6. Lastly, input the code value into the "Code" field. Add additional codes as needed.  
   ​

   [![Click on tab](https://element451.intercom-attachments-7.com/i/o/495341664/26a559392e4bfe3a4cb8bf75/screenshot_02f1cf17-1e44-476b-9697-33b5ec18446d?expires=1784333700&signature=f028ecb64d61908d497ec83011730a0a88aa62092de0d05cc9545e577e39e4a5&req=cCkiFc1%2Fm4dbFb4f3HP0gONXE8bb5V7zgdXso9eT%2FFeVOyasu2d2z49vf7zS%0AobE%3D%0A)](https://element451.intercom-attachments-7.com/i/o/495341664/26a559392e4bfe3a4cb8bf75/screenshot_02f1cf17-1e44-476b-9697-33b5ec18446d?expires=1784333700&signature=f028ecb64d61908d497ec83011730a0a88aa62092de0d05cc9545e577e39e4a5&req=cCkiFc1%2Fm4dbFb4f3HP0gONXE8bb5V7zgdXso9eT%2FFeVOyasu2d2z49vf7zS%0AobE%3D%0A)
7. Click **Done**. This will return you to the category's data source list. At this point, you can add additional codes manually by editing each field or uploading them.

---

# Importing Integration Codes

After manually adding one integration code using the process above, you can use the export feature to upload the rest.

1. Navigate to **Data + Automations** > **Data Sources**.
2. Click on the category of your choice (Majors, Terms, Degrees, Campuses, Tests, Schools, or Courses).
3. In the header, click the **Download** icon. Your data sources will be downloaded to your computer as a .csv file.  
   ​

   [![Click on img](https://element451.intercom-attachments-7.com/i/o/495341672/634b8380c6565ad6bd8e0568/screenshot_f1e88bdd-cc27-44d3-824d-610e7400474e?expires=1784333700&signature=0b809d38436642e7c06df3712f7f69308e807b8af21c2a5bf2d377d96ee68ba3&req=cCkiFc1%2Fm4ZdFb4f3HP0gIUad271YoyNWXhygVw3awlEzZmgunXuLhaSF9yu%0AHnA%3D%0A)](https://element451.intercom-attachments-7.com/i/o/495341672/634b8380c6565ad6bd8e0568/screenshot_f1e88bdd-cc27-44d3-824d-610e7400474e?expires=1784333700&signature=0b809d38436642e7c06df3712f7f69308e807b8af21c2a5bf2d377d96ee68ba3&req=cCkiFc1%2Fm4ZdFb4f3HP0gIUad271YoyNWXhygVw3awlEzZmgunXuLhaSF9yu%0AHnA%3D%0A)
4. **Open the file in Excel** (or a software of your choice). Locate the Integration Code column. In our manual example, we selected a "CIP" code. This will correlate to a "CIP" column in the file. Add the rest of the codes to the column.
5. **Save the file as a .csv.** When all codes are added, ensure the final file is saved as a .csv. Excel files cannot be uploaded to Element451.
6. **Import the .csv file to the Data Source**. Find the Upload icon (next to the download icon). Select the "Upload file" card and select the file from your local computer. Select to either import only new data, update existing data, or update existing and import new data. Click "Upload" to begin the upload.  
   ​

   [![Click on dialog](https://element451.intercom-attachments-7.com/i/o/495341684/9a1d7614ed95b9e5e6c6be39/screenshot_9cfbeb4a-a36f-4846-9eb9-f962e3e52cd9?expires=1784333700&signature=c9a34f434cc2d2ff94a1924f93985b6a1457a7a642711ba5b882b6d8e9bd2aca&req=cCkiFc1%2Fm4lbFb4f3HP0gCOa5Wbv0D5aUf%2B1ccqPvJa7I0nyztG8si5wmMOJ%0A2%2BU%3D%0A)](https://element451.intercom-attachments-7.com/i/o/495341684/9a1d7614ed95b9e5e6c6be39/screenshot_9cfbeb4a-a36f-4846-9eb9-f962e3e52cd9?expires=1784333700&signature=c9a34f434cc2d2ff94a1924f93985b6a1457a7a642711ba5b882b6d8e9bd2aca&req=cCkiFc1%2Fm4lbFb4f3HP0gCOa5Wbv0D5aUf%2B1ccqPvJa7I0nyztG8si5wmMOJ%0A2%2BU%3D%0A)

---

# Referencing Integration Codes in Import + Export

With Integration Codes added to your Data Sources, you can now use them when importing and exporting data from the Import + Export Module. This is how you will interpret or send codes between systems.

Before continuing here, ensure you're familiar with the [Import](https://help.element451.com/en/articles/9000459-getting-started-with-imports) + [Export](https://help.element451.com/en/articles/9006515-getting-started-with-exports) Modules.

## Importing Integration Codes

Importing integration code requires using a Calculated column. Once a calculated column is created, use the `DB_MAP()` formula to target the data source and field you wish to export.

In this example, we'll import the CIP code to the user's Intended Major. Let's assume we're importing a file of 20 columns. The 10th column has the CIP major code for each student.

```
DB_MAP("major" , [C10],  "cip", "guid", "")
```

Each parameter of `DB_MAP()` is separated by a comma. The parameters are:

1. **The Type**. In this case, we're using "Major". "Term" & "Taxonomy" are also available.
2. **The Input**. In this case, we're using the 10th column of the file, which the formula will identify as `[C10]`. To select a column, type "[" into the formula field. This will show all columns that can be selected.
3. **The Match**. This is the type of data that is stored in the column of the import file. In this case, the column at `[C10]` stores the CIP of the major. By inputting "cip" in the match parameter, we're telling the formula to anticipate that type of value.
4. **The Output**. This is the attribute of the major we want to appear in the export. No matter the case, we always want import calculated columns to output the GUID of a data source field. The GUID is the only valid data type that data source fields can store. If the CIP code were to be output, the system would not understand how to display or use the data.
5. **The Default**. This will be inserted into the field by default no value exists in the column, or if the Match fails and produces no Output. In this case, the Default is "", which will input no value into the field.

Once the formula is entered, the Preview tab will show the GUID in the output for the calculated column.

Read more about `DP_MAP()` and see all formulas [here](https://integrations.element451.com/calculated-fields-37).

## Exporting Integration Codes

Exporting an integration code will require you to use a Calculated column. Once a calculated column is created, use the `DB_MAP()` formula to target the data source and field you wish to export.

In this example, we'll export the CIP code of the user's Intended Major.

```
DB_MAP("major" , [user-education-prefered-major],  "guid", "cip", "")
```

Each parameter of `DB_MAP()` is separated by a comma. The parameters are:

1. **The Type**. In this case, we're using "Major". "Term" & "Taxonomy" are also available.
2. **The Input**. In this case, we're using `[user-education-prefered-major]`. To select a Field to input, type "[" into the formula field. This will show all slugs that can be selected.
3. **The Match**. This is the attribute of the major that is stored in the field. In this case, the `[user-education-prefered-major]` field stores the GUID of the major. By inputting "guid" in the Match parameter, we're telling the formula to anticipate that type of value.
4. **The Output**. This is the attribute of the major we want to appear in the export. In this case, we want the CIP code, so we insert "cip" into the parameter.
5. **The Default**. This will be inserted into the column by default no value exists in the Field, or if the Match fails and produces no Output. In this case, the Default is "", which will produce an empty cell.

Once the formula is entered, the Preview tab will show the integration code in the output for the calculated column.

Read more about `DP_MAP()` and see all formulas [here](https://integrations.element451.com/calculated-fields-37).

---