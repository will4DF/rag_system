---
title: Data Hygiene Dashboard
url: https://help.element451.com/en/articles/8814567-data-hygiene-dashboard
collection: Insights
---

Learn how to use the Data Hygiene dashboard and fix data errors.

# Overview

The Data Hygiene dashboard is designed to surface issues in your data and help you fix them. The dashboard covers three main areas of concern on the Person record, attributes, applications and milestones. Use the downloadable file from the dashboard to fix errors in your preferred spreadsheet app. Finally, Import the corrected data to Element451.

## Accessing the Data Hygiene Dashboard

The Data Hygiene dashboard can be found via the Insights sub-menu. The Insights module can be accessed from the Data + Automations dropdown in the top navigation.

---

# Dashboard Features

Use the Data Hygiene dashboard to find errors in commonly used data and correct them. The dashboard will provide you with a downloadable file that you can then modify and Import back into Element451, correcting the data issues.

## Tabs

### The Overview Tab

The Overview tab provides a quick summation of data quality across three key dimensions of the Person record: their direct attributes, Applications, and Milestones.

[![](https://downloads.intercomcdn.com/i/o/944812710/947d3008daa2acbb362470cc/Screenshot+2024-01-26+at+9.12.15%E2%80%AFAM.png?expires=1784333700&signature=b0db21b0ae38f92d6fe1b9f7e5f0b5c6a4701e6a5679cfb9ae7f0fcad5a70876&req=fSQjHsh8moBfFb4f3HP0gMSNdlkgs5oDag%2F5cMFhenNOC4iIveRkOxazChMD%0AFutoDsHPlnOAYzonYQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/944812710/947d3008daa2acbb362470cc/Screenshot+2024-01-26+at+9.12.15%E2%80%AFAM.png?expires=1784333700&signature=b0db21b0ae38f92d6fe1b9f7e5f0b5c6a4701e6a5679cfb9ae7f0fcad5a70876&req=fSQjHsh8moBfFb4f3HP0gMSNdlkgs5oDag%2F5cMFhenNOC4iIveRkOxazChMD%0AFutoDsHPlnOAYzonYQ%3D%3D%0A)

* **Person Record Errors Summary:** Shows the number of errors across 7 commonly used attributes:  
  ​

  + Intended Term
  + Intended Major
  + Intended Degree
  + Intended Campus
  + Intended Student Type
  + Citizenship Status
  + Citizenship Country

  Each card shows the number of errors. A total card shows the total number of errors, and the percent of Person records with Application errors against all Person records.
* **Application Data Errors Summary:** Shows the number of errors across 7 commonly used attributes:  
  ​

  + Application Term
  + Application Major
  + Application Degree
  + Application Campus
  + Application Student Type
  + Application Status
  + Application Type

  Each card shows the number of errors. A total card shows the total number of errors and the percent of Person records with errors against all Person records.
* **Milestone Data Errors Summary:** Shows the number of errors across 3 commonly used attributes:  
  ​

  + Milestone Term
  + Milestone Major
  + Milestone Student Type

  Each card shows the number of errors. A total card shows the total number of errors, and the percent of Person records with Milestone errors against all Person records.

### The Error Report Tab

The Error Report tab allows you to select a field, observe errors for that field and it's expected values, then download a file of errors. Additionally, lookup up Import tasks that may have created the error.

[![](https://downloads.intercomcdn.com/i/o/1016655988/2afbbec999a78bb719d7240e/Screenshot+2024-04-09+at+2_20_50%E2%80%AFPM.png?expires=1784333700&signature=4657809e41ebe60dd49edb8363a9785c5c9e0dbba701287de208a81d70297f84&req=dSAmEM97mIhXUfMW1HO4zb6Zd2YnqBm2Di5QSTFZXNGCZvcH9LG1WZqN3Ane%0A7U9wDXNPgVURQ6P0zkM%3D%0A)](https://downloads.intercomcdn.com/i/o/1016655988/2afbbec999a78bb719d7240e/Screenshot+2024-04-09+at+2_20_50%E2%80%AFPM.png?expires=1784333700&signature=4657809e41ebe60dd49edb8363a9785c5c9e0dbba701287de208a81d70297f84&req=dSAmEM97mIhXUfMW1HO4zb6Zd2YnqBm2Di5QSTFZXNGCZvcH9LG1WZqN3Ane%0A7U9wDXNPgVURQ6P0zkM%3D%0A)

---

# Fixing Data Errors

The Data Hygiene dashboard is designed to give you a file of Person records with errored data. You can then correct the data in a spreadsheet application of your choice and import the corrected data via the Import module.

The following instructions assume that you are familiar with Importing Data into Element451.

## Field Mappings

Use these mappings when Importing:

### Person Record Attributes

|  |  |
| --- | --- |
| **Field** | **Mapping Slug** |
| Citizenship Country | user-citizenship-country |
| Citizenship Status | user-citizenship-status |
| Intended Campus | user-education-campus |
| Intended Degree | user-education-degree |
| Intended Major | user-education-preferred-major |
| Intended Student Type | user-education-student-type |
| Intended Term | user-education-term |

### Application Attributes

|  |  |
| --- | --- |
| **Field** | **Mapping Slug** |
| Application Campus | user-applications-campus-\* |
| Application Degree | user-applications-degree-\* |
| Application Major | user-applications-major-\* |
| Application Status | user-applications-status-\* |
| Application Student Type | user-applications-student-type-\* |
| Application Term | user-applications-term-\* |

### Milestone Attributes

|  |  |
| --- | --- |
| **Field** | **Mapping Slug** |
| Milestone Major | user-milestones-major-\* |
| Milestone Student Type | user-milestones-student-type-\* |
| Milestone Term | user-milestones-term-\* |

---

# Example 1: Fixing Intended Term

Watch the following video as we walk through an example:

Intended Term is a direct attribute of the Person record. It does not repeat. This makes it straightforward to fix, compared to Application and Milestone attributes.

## Review the Step-by-Step Process

1. **Select Intended Term as the Active Field**: On the "Error Report" tab, find the Person Record Errors section at the top. Set the Active Field control to "Intended Term."  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015455153/97f9131230c0720ee75388c7/Screenshot+2024-04-08+at+1_57_49%E2%80%AFPM.png?expires=1784333700&signature=879872ae0b2d05801bbf85fcd128b4505ed2ad66509d19c7a11c4de50a69a5fe&req=dSAmE817mIBaWvMW1HO4zeJ5uxqbh9AZV5wARPkR1QEeFZRh8%2FhRF%2BXnVadp%0A5%2BHP%0A)](https://downloads.intercomcdn.com/i/o/1015455153/97f9131230c0720ee75388c7/Screenshot+2024-04-08+at+1_57_49%E2%80%AFPM.png?expires=1784333700&signature=879872ae0b2d05801bbf85fcd128b4505ed2ad66509d19c7a11c4de50a69a5fe&req=dSAmE817mIBaWvMW1HO4zeJ5uxqbh9AZV5wARPkR1QEeFZRh8%2FhRF%2BXnVadp%0A5%2BHP%0A)
2. **Observe the Error Values and Expected Values**: With Intended Term selected, observe the "Records with Errors" table, and contrast it to the "Expected Values" table. Notice that the expected values are "GUIDs", the unique identifier for Terms in the Element451 database.
3. **Download the Records with Errors Table**: Download the "Records with Errors" table using the three-dot menu in the top right corner of the table. CSV and Excel options are available, either should work fine.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015455272/b9c5cd6ca4f9ffcd1f5220e8/Screenshot+2024-04-08+at+1_59_13%E2%80%AFPM.png?expires=1784333700&signature=22522e2f6a49d23cb464b41c414c4e3f8281f6d955c7a6328f4af1caaa788238&req=dSAmE817mINYW%2FMW1HO4zVyfwe4Q8hTut67YNXVRHY5%2FzXPehHzHH%2BCdT%2FLu%0A4JU%2F%0A)](https://downloads.intercomcdn.com/i/o/1015455272/b9c5cd6ca4f9ffcd1f5220e8/Screenshot+2024-04-08+at+1_59_13%E2%80%AFPM.png?expires=1784333700&signature=22522e2f6a49d23cb464b41c414c4e3f8281f6d955c7a6328f4af1caaa788238&req=dSAmE817mINYW%2FMW1HO4zVyfwe4Q8hTut67YNXVRHY5%2FzXPehHzHH%2BCdT%2FLu%0A4JU%2F%0A)
4. **Open the Downloaded File in Your Spreadsheet App**: In your spreadsheet app, use find and replace to select error data and replace it with the correct value. Replacing the error with the Term GUID is preferable, but replacing the error with Term code or Term name is also acceptable.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/940829708/3c268861090c7f04663b0fc2/Screenshot+2024-01-22+at+4.47.37%E2%80%AFPM.png?expires=1784333700&signature=fffbd158292183bebd2ce1bed6fc4b98fc1571eef5ba94e791edbe2d5573b3f3&req=fSQnHst3moFXFb4f3HP0gBQWYC2DFGK%2F2yn%2Bmw6flWCMyOpdxuOuyBRbjICz%0A8fQ%3D%0A)](https://downloads.intercomcdn.com/i/o/940829708/3c268861090c7f04663b0fc2/Screenshot+2024-01-22+at+4.47.37%E2%80%AFPM.png?expires=1784333700&signature=fffbd158292183bebd2ce1bed6fc4b98fc1571eef5ba94e791edbe2d5573b3f3&req=fSQnHst3moFXFb4f3HP0gBQWYC2DFGK%2F2yn%2Bmw6flWCMyOpdxuOuyBRbjICz%0A8fQ%3D%0A)
5. **Save the Corrected File as a CSV**: After errored data has been corrected, save the file as a .csv. This will be required when uploading to Element451.
6. **Create an Import Task in Element451 and Upload the Correct File as the Source:** On the Source tab of the Import Task, selected the corrected file from your local computer.
7. **Map the Columns of the Corrected File**: On the Mapping tab, map the Element ID column to `user-elementid`. Map the Intended Term column to `user-education-term`.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015446702/ade34d6db8191c80a45a115c/Screenshot+2024-04-08+at+1_50_23%E2%80%AFPM.png?expires=1784333700&signature=e3b36572370233d8db1530ece2fb47690fc36a459db27cb40fafabcca17373d2&req=dSAmE816m4ZfW%2FMW1HO4zcwqHjBiwa5dZzeNQq6tjV1H66GkzgoSsjeVLq8y%0Au8MC%0A)](https://downloads.intercomcdn.com/i/o/1015446702/ade34d6db8191c80a45a115c/Screenshot+2024-04-08+at+1_50_23%E2%80%AFPM.png?expires=1784333700&signature=e3b36572370233d8db1530ece2fb47690fc36a459db27cb40fafabcca17373d2&req=dSAmE816m4ZfW%2FMW1HO4zcwqHjBiwa5dZzeNQq6tjV1H66GkzgoSsjeVLq8y%0Au8MC%0A)
8. **Set Intended Term Column Settings**: In Intended Term column settings, set "interpret as" to be the value you corrected your error data to. If you found errors and replaced them with the Term GUID, set "interpret as" to "guid". If you replaced with Term code, set "interpret as" to "code."

   IMPORTANT: This step is critical to fixing the data. Data errors will persist if imported data is not correctly transformed.  
   ​  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015447700/d93b60606e4f348da89eb006/Screenshot+2024-04-08+at+1_51_30%E2%80%AFPM.png?expires=1784333700&signature=7388553bbaeff714b5be4bd268f789b2f6a34af659421d0a8cba6ccc6fe11358&req=dSAmE816moZfWfMW1HO4zX2ge7DEt2PNqVexEqleJYqrFHaLMkZpPILWwNrj%0ATkoB%0A)](https://downloads.intercomcdn.com/i/o/1015447700/d93b60606e4f348da89eb006/Screenshot+2024-04-08+at+1_51_30%E2%80%AFPM.png?expires=1784333700&signature=7388553bbaeff714b5be4bd268f789b2f6a34af659421d0a8cba6ccc6fe11358&req=dSAmE816moZfWfMW1HO4zX2ge7DEt2PNqVexEqleJYqrFHaLMkZpPILWwNrj%0ATkoB%0A)

   ​

   [![](https://downloads.intercomcdn.com/i/o/1015447760/389a0e568efca6be4541eee7/Screenshot+2024-04-08+at+1_51_18%E2%80%AFPM.png?expires=1784333700&signature=a874284c5f2cc3808b951f56eb3d5df9799088c8490d1ffac55a7e40b8282d0a&req=dSAmE816moZZWfMW1HO4zT8JTcqvU0QnehfYcQ0hqPRqYEePAApzgYOK8vDp%0ApUmj%0A)](https://downloads.intercomcdn.com/i/o/1015447760/389a0e568efca6be4541eee7/Screenshot+2024-04-08+at+1_51_18%E2%80%AFPM.png?expires=1784333700&signature=a874284c5f2cc3808b951f56eb3d5df9799088c8490d1ffac55a7e40b8282d0a&req=dSAmE816moZZWfMW1HO4zT8JTcqvU0QnehfYcQ0hqPRqYEePAApzgYOK8vDp%0ApUmj%0A)
9. **Match the Element ID Column**: On the Matching tab, match entities by "Element ID". This will match imported data to the existing Person records.
10. **Preview the Mappings**: On the Preview tab, observe the right column, "Database", to verify that incoming data is being transformed properly. For Intended Term, Term GUID should be shown in the right column.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/1015449500/9c7fb1a2e9d728eba53ac656/Screenshot+2024-04-08+at+1_52_48%E2%80%AFPM.png?expires=1784333700&signature=09f0197e3ffaad2a133030f16649f29bdb18b770d867fb0a2fe3f355cae7840f&req=dSAmE816lIRfWfMW1HO4zUL7TuEMoNO%2BMpNzCL%2Fm8bvncVQgy6ElWczQDXSU%0AzzMj%0A)](https://downloads.intercomcdn.com/i/o/1015449500/9c7fb1a2e9d728eba53ac656/Screenshot+2024-04-08+at+1_52_48%E2%80%AFPM.png?expires=1784333700&signature=09f0197e3ffaad2a133030f16649f29bdb18b770d867fb0a2fe3f355cae7840f&req=dSAmE816lIRfWfMW1HO4zUL7TuEMoNO%2BMpNzCL%2Fm8bvncVQgy6ElWczQDXSU%0AzzMj%0A)
11. **Import the Corrected Values and Verify**: Run the Import task, then verify that Intended Term is correct on the Person Profile. The Data Hygiene dashboard will also update, but may take longer than an individual Person Profile. Please allow up to 12 hours for changes to be visible on the dashboard.

---

# Example 2 : Fixing Application Major

Watch the following video as we walk through an example:

Application Major is an attribute of the Person record's Applications. Applications have a many-to-one relationship with the student record, and are stored as an array on the Person Record. To target a specific Application Major, we'll need to know it's "position" in the array. The position is provided in the "Records with Errors" table, and is selected along with Active Field.

## Review the Step-by-Step Process

1. **Select Application Major as the Active Field**: On the "Error Report" tab, find the "Application Errors" section in the middle. Set the Active Field control to "Application Major". Set the Application Position control to "1."  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015445270/7f95e3dd26e482d1ec0eecf8/Screenshot+2024-04-08+at+1_46_54%E2%80%AFPM.png?expires=1784333700&signature=1fe7483c2e53c4c787a197707da98bb0cb9ef2ecaa4e7e3865113209ac4a635e&req=dSAmE816mINYWfMW1HO4zd6ce7rDdunJJz1Phnt%2FWZIh0pasus6QjG61aDkl%0A689K%0A)](https://downloads.intercomcdn.com/i/o/1015445270/7f95e3dd26e482d1ec0eecf8/Screenshot+2024-04-08+at+1_46_54%E2%80%AFPM.png?expires=1784333700&signature=1fe7483c2e53c4c787a197707da98bb0cb9ef2ecaa4e7e3865113209ac4a635e&req=dSAmE816mINYWfMW1HO4zd6ce7rDdunJJz1Phnt%2FWZIh0pasus6QjG61aDkl%0A689K%0A)
2. **Observe the Error Values and Expected Values**: With Application Major selected, observe the "Records with Errors" table, and contrast it to the "Expected Values" table. Notice that the expected values are "GUIDs", the unique identifier for Majors in the Element451 database.
3. **Download the Records with Errors Table**: Download the "Records with Errors" table using the three-dot menu in the top right corner of the table. CSV and Excel options are available, either should work fine.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015445172/7a259ba0b531f1b94c1137f3/Screenshot+2024-04-08+at+1_47_21%E2%80%AFPM.png?expires=1784333700&signature=e57a8937a93bef4473dcab4aae00a6992016d3873717c5ad27ebcea0a69361a7&req=dSAmE816mIBYW%2FMW1HO4zchO2S5xgYpGECbwq3F8lrHiOoE2NjJn453xyIjl%0AfWaI%0A)](https://downloads.intercomcdn.com/i/o/1015445172/7a259ba0b531f1b94c1137f3/Screenshot+2024-04-08+at+1_47_21%E2%80%AFPM.png?expires=1784333700&signature=e57a8937a93bef4473dcab4aae00a6992016d3873717c5ad27ebcea0a69361a7&req=dSAmE816mIBYW%2FMW1HO4zchO2S5xgYpGECbwq3F8lrHiOoE2NjJn453xyIjl%0AfWaI%0A)
4. **Open the Downloaded File in Your Spreadsheet App**: In your spreadsheet app, use find and replace to select error data and replace it with the correct value. Replacing the error with the Major GUID is preferable, but replacing the error with Major code or Major name is also acceptable.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/941869284/c2563ea714713b78232bb82d/Screenshot+2024-01-23+at+2.37.47%E2%80%AFPM.png?expires=1784333700&signature=d891865f9fdc177ebb2f7271609b574831f143a430683e518f9ec639007b2ba7&req=fSQmHs93n4lbFb4f3HP0gI0%2FSOXoIfb6mRzVjMUTnugKJvJgrLUnSu%2F8Bz9w%0AH30%3D%0A)](https://downloads.intercomcdn.com/i/o/941869284/c2563ea714713b78232bb82d/Screenshot+2024-01-23+at+2.37.47%E2%80%AFPM.png?expires=1784333700&signature=d891865f9fdc177ebb2f7271609b574831f143a430683e518f9ec639007b2ba7&req=fSQmHs93n4lbFb4f3HP0gI0%2FSOXoIfb6mRzVjMUTnugKJvJgrLUnSu%2F8Bz9w%0AH30%3D%0A)
5. **Save the Corrected File as a CSV**: After errored data has been corrected, save the file as a .csv. This will be required when uploading to Element451.
6. **Create an Import Task in Element451 and Upload the Correct File as the Source**: On the Source tab of the Import Task, selected the corrected file from your local computer.
7. **Map the Columns of the Corrected File**: On the Mapping tab, map the Element ID column to `user-elementid`. Map the Application Major column to `user-applications-major-*`. Leave the "Position" column unmapped.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015436506/33779f79803e7d8333fc83c3/Screenshot+2024-04-08+at+1_35_51%E2%80%AFPM.png?expires=1784333700&signature=00070ebd0234c04060c4c64e509f9818678e0ba7abe445b69e0a36b2ca0b26b3&req=dSAmE819m4RfX%2FMW1HO4zYy8DTqcwMf%2FuxUNuxWGKfJxKKwc5%2B336CO0CTRl%0AnCS4%0A)](https://downloads.intercomcdn.com/i/o/1015436506/33779f79803e7d8333fc83c3/Screenshot+2024-04-08+at+1_35_51%E2%80%AFPM.png?expires=1784333700&signature=00070ebd0234c04060c4c64e509f9818678e0ba7abe445b69e0a36b2ca0b26b3&req=dSAmE819m4RfX%2FMW1HO4zYy8DTqcwMf%2FuxUNuxWGKfJxKKwc5%2B336CO0CTRl%0AnCS4%0A)
8. **Set Application Term Column Settings**: In Application Major column settings, set "interpret as" to be the value you corrected your error data to. If you found errors and replaced them with the Term GUID, set "interpret as" to "guid". If you replaced with Term code, set "interpret as" to "code."  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015435940/4f0cffa000a7549697768ed4/Screenshot+2024-04-08+at+1_36_10%E2%80%AFPM.png?expires=1784333700&signature=d9b64bfb735f16770cf211791ae4b52c0a78d4036dfbcc7e4f8063054454d830&req=dSAmE819mIhbWfMW1HO4zWdGj%2Fuw2s07pTH3CbjuvTbix19o9OPtMJtmHhMK%0Ay9nF%0A)](https://downloads.intercomcdn.com/i/o/1015435940/4f0cffa000a7549697768ed4/Screenshot+2024-04-08+at+1_36_10%E2%80%AFPM.png?expires=1784333700&signature=d9b64bfb735f16770cf211791ae4b52c0a78d4036dfbcc7e4f8063054454d830&req=dSAmE819mIhbWfMW1HO4zWdGj%2Fuw2s07pTH3CbjuvTbix19o9OPtMJtmHhMK%0Ay9nF%0A)

   ​

   [![](https://downloads.intercomcdn.com/i/o/1015436325/7dee1951e8c8960a68df7345/Screenshot+2024-04-08+at+1_39_13%E2%80%AFPM.png?expires=1784333700&signature=b93893c6bb8927c681240fae9d1240722f11037b8dedabc9d089bf03b04d370d&req=dSAmE819m4JdXPMW1HO4zQWtSOEEnE4boBfU%2Fm9i5oqXUGLFtA0u668bBRmp%0AuTPX%0A)](https://downloads.intercomcdn.com/i/o/1015436325/7dee1951e8c8960a68df7345/Screenshot+2024-04-08+at+1_39_13%E2%80%AFPM.png?expires=1784333700&signature=b93893c6bb8927c681240fae9d1240722f11037b8dedabc9d089bf03b04d370d&req=dSAmE819m4JdXPMW1HO4zQWtSOEEnE4boBfU%2Fm9i5oqXUGLFtA0u668bBRmp%0AuTPX%0A)

   Additionally, set the Position Scope of the column to the Position selected on the dashboard. In this example, we're working with Position 1.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/1015435636/4feef7dd5b554d5519bb2f00/Screenshot+2024-04-08+at+1_36_18%E2%80%AFPM.png?expires=1784333700&signature=b41c4ff923e3956b18c6499b8078142e02ef595e2c0a23c8f147f267103108bf&req=dSAmE819mIdcX%2FMW1HO4zbejiqrXtgK5hhKFRUYX%2FOtmWUKqFJswaLzQzFyc%0A9KIU%0A)](https://downloads.intercomcdn.com/i/o/1015435636/4feef7dd5b554d5519bb2f00/Screenshot+2024-04-08+at+1_36_18%E2%80%AFPM.png?expires=1784333700&signature=b41c4ff923e3956b18c6499b8078142e02ef595e2c0a23c8f147f267103108bf&req=dSAmE819mIdcX%2FMW1HO4zbejiqrXtgK5hhKFRUYX%2FOtmWUKqFJswaLzQzFyc%0A9KIU%0A)

   IMPORTANT: This step is critical to fixing the data. Data errors will persist if imported data is not correctly transformed. New data errors may occur if Position is incorrectly configured.
9. **Match the Element ID Column**: On the Matching tab, match entities by "Element ID." This will match imported data to the existing Person records.
10. **Preview the Mappings**: On the Preview tab, observe the right column, "Database", to verify that incoming data is being transformed properly. For Application Major, Major GUID should be shown in the right column.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/1015435180/78651c14240ff42b6ad7cb7d/Screenshot+2024-04-08+at+1_36_33%E2%80%AFPM.png?expires=1784333700&signature=cd1acc8a1c9cf3b3fa6e4d9c30b31410e4ce2115f8e2d1ff956aae555dcd21a8&req=dSAmE819mIBXWfMW1HO4zSBfOijyKKd4LIuMve%2BDbKy6m4JodR%2BJvoWDNKIO%0A06ya%0A)](https://downloads.intercomcdn.com/i/o/1015435180/78651c14240ff42b6ad7cb7d/Screenshot+2024-04-08+at+1_36_33%E2%80%AFPM.png?expires=1784333700&signature=cd1acc8a1c9cf3b3fa6e4d9c30b31410e4ce2115f8e2d1ff956aae555dcd21a8&req=dSAmE819mIBXWfMW1HO4zSBfOijyKKd4LIuMve%2BDbKy6m4JodR%2BJvoWDNKIO%0A06ya%0A)
11. **Import the Corrected Values and Verify**: Run the Import task, then verify that Application Major is correct on the Person Profile. The Data Hygiene dashboard will also update, but may take longer than an individual Person Profile. Please allow up to 12 hours for changes to be visible on the dashboard.

---

# Additional Considerations

### Transformation Errors

Errors take many forms, but it's common for errors to simply be incorrectly transformed data. For example, when importing Intended Term into Element451, it's common to accidentally import the Term Code, instead of transforming the code to GUID in the column settings. [Learn more about transforming codes to GUIDs during Import.](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports)

In this case, we can modify our steps for fixing the issue. Referring to the "Fixing Intended Term" example, we can skip Step 4. Simply download the file from the dashboard and upload it straight into the Import task. Set the "Interpret as" settings to correctly identify the Term code. Then run the task.

---

# Finding Data Errors in Import Tasks

Import tasks are the most common place where data errors occur. Imports are highly customizable to fit a variety of needs, but if incoming data is not properly interpreted and transformed, data can be incorrectly saved to the database. Learn more about [data errors](#h_dce6e3f8d3).

The Data Hygiene dashboard makes it easy to find imports that could have caused data errors. Use the "Import Tasks Mapping to.." table on the "Error Report" tab to see Import tasks that could have caused data errors for the selected.

---

# Troubleshooting and FAQ

## What constitutes a data "error"?

A data error occurs when an unexpected data value is saved to the database. For each field on the Person record, Element451 anticipates a certain type of data in a certain format. For Data-Source-controlled fields, like Term, Major and Student Type, Element451 also anticipates only specific values as defined by the Data Source.

As shown in the examples above, a data error occurred for the Intended Term field when the value "Fall 2022" was saved to the database. The database anticipated the Term GUID.

## How did my instance get so many data errors?

Data errors for Data-Source-controlled fields usually occur during an Import. It's common to accidentally mis-configure the column settings for these fields, forgetting to set their interpretation to the correct value. Pay special attention to the [transformations when mapping](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports).

## How can I fix Application Type errors?

Application Type cannot be changed via an Import or through the Element451 interface. Please reach out to Element451 support for assistance with these errors.

## How often does the Data Hygiene dashboard update?

The Data Hygiene dashboard currently refreshes twice a day at 6:00 am and 12:00 pm Eastern. Depending on the size of the dataset, the refresh can take up to 30 minutes. You will see changes to the dashboard shortly after the refresh times.

---