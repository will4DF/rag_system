---
title: Importing School History
url: https://help.element451.com/en/articles/10830714-importing-school-history
collection: Data Management
---

Learn how to import high school and college data onto a contact.

This article will provide you a starting guide on how to import high school and college information onto a contact record.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486343687/ada00f69917ae73e328bb761a602/Screenshot+2025-04-21+at+10_47_02%E2%80%AFAM.png?expires=1784333700&signature=e102e86db8f208060f11993756b3b7a8f9877e042dfd293b5a2c33432a359937&req=dSQvEMp6nodXXvMW1HO4zW3FWUjCwnjE5RHDppFqK2ORBTtV%2Bn9T65%2Bw6D66%0AzF3XmyHAwdcEHAPxCJ0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486343687/ada00f69917ae73e328bb761a602/Screenshot+2025-04-21+at+10_47_02%E2%80%AFAM.png?expires=1784333700&signature=e102e86db8f208060f11993756b3b7a8f9877e042dfd293b5a2c33432a359937&req=dSQvEMp6nodXXvMW1HO4zW3FWUjCwnjE5RHDppFqK2ORBTtV%2Bn9T65%2Bw6D66%0AzF3XmyHAwdcEHAPxCJ0%3D%0A)

Creating School Files As a reminder, the files need to be either .csv or .txt, contain a unique identifier (or a few!). There are a few ways we recommend making files of source data.

1. **Generate separate files per school.** Each file would represent the position of the school on the record. For example, a file would be records' first school, another file would records' second school, etc.. Additionally, High Schools and Colleges would be different files.
2. **Format school data into column sets.** In this scenario, columns 4-7 would belong to the record's first high school, then columns 8-11 would belong to the record's second high school, etc.. Further into the columns, there would be chunks of columns for the record's first college, second college, etc..
3. **Repeat file on schools.** In this scenario, a record may be present several times in the file. For this method, you must have a column for row number over student ID and school type that represents if the school is the record's first high school, second high school, third high school, first college, second college, etc.. Fields to Include in the Files Listed are fields you can include on your school files. The bolded fields are strongly recommended.

* **Contact Identifiers (Student ID, Historic ID, and/or Email)**
* **School Type**
* This is to clarify if the school is a High School or College
* **School CEEB**

  + Note: In some cases, such as with the ApplyTexas CSV template, the CEEB code may need to be derived from the last six characters of the high school code (HS\_code) column.
* School Name
* School Address Information
* School Cumulative GPA
* Is GPA Official?
* Start Date
* Graduation or Transfer Date
* Do you or will you graduate? Y/N
* Degree Earned
* Counselor Information

## Importing Schools using Method 1

With separate files for each school, you will be creating import tasks for each file that are identical in column layout, but different scoping set up inside the source fields. There is a Historic School Import template in your instance, but you are not required to follow that exact layout if you need additional unique identifiers or need to put the fields in a different order, the template is a starting point if you need direction.

## Mapping

The following fields should be mapped when importing school history:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **School Fields:** Try to map as many of the school fields listed below as possible.

  + user-education-schools-ceeb-\*
  + user-education-schools-name-\*
  + user-education-schools-street1-\*
  + user-education-schools-street2-\*
  + user-education-schools-city-\*
  + user-education-schools-state-\*
  + user-education-schools-zip-\*
  + user-education-schools-county-\*
  + user-education-schools-country-\*
  + user-education-schools-cumulative-gpa-\*
  + user-education-schools-gpa\_official-\*
  + user-education-schools-start-\*
  + user-education-schools-end-\*
  + user-education-schools-graduate-\*

    - This is the "Did you or will you graduate? Y/N" field
  + user-education-schools-degree-earned-\*
  + user-education-schools-counselor-email-new-\*
  + user-education-schools-counselor-first-name-\*
  + user-education-schools-counselor-last-name-\*

## Scoping

Notice that the source fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. For schools, the scoping settings are school type, position, and zip code.

When selecting the settings, you are telling the system that you are importing a school with these qualities, if a school does not exist with those qualities, create a new one, if one does exist, update it. Without the star mappings, the system updates whatever school is on the record's profile, potentially wiping a historic school.

For importing schools using Method 1, for each field on your import, you will set the scoping settings to whatever school type and position you want them to feed into. Since Method 1 instructs you to have separate files for each school listed, each import will have the same column headers but the scoping settings will reflect the position you are importing. You would have a file for the record's first high school, another file for the record's second high school, and so forth, then one for the first college, another for the second college, and so forth.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486354436/75a2ee12167d9b913da87bbbc791/Screenshot+2025-04-21+at+10_53_39%E2%80%AFAM.png?expires=1784333700&signature=e24b7fe0cc766869c76ff9e1e9c257c1f31fa76e1ca937e71db7f9256cfdacc8&req=dSQvEMp7mYVcX%2FMW1HO4zZbV7bnYKU3ap3dOSXaWW39iK77HTd%2Bsea1XJqrQ%0AapXZPiiOeOoD4jGEwDQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486354436/75a2ee12167d9b913da87bbbc791/Screenshot+2025-04-21+at+10_53_39%E2%80%AFAM.png?expires=1784333700&signature=e24b7fe0cc766869c76ff9e1e9c257c1f31fa76e1ca937e71db7f9256cfdacc8&req=dSQvEMp7mYVcX%2FMW1HO4zZbV7bnYKU3ap3dOSXaWW39iK77HTd%2Bsea1XJqrQ%0AapXZPiiOeOoD4jGEwDQ%3D%0A)

Importing Schools using Method 2 If your file follows Method 2, where you have one file with column sets that are associated with schools type and positions, follow the instructions for mapping below. Mapping

# Column Order Integrity

When using structured templates like ApplyTexas, maintaining the exact column order is critical for calculated fields to function correctly. Avoid moving, removing, or renaming columns unless you update the formulas accordingly. The following fields should be mapped when importing school history:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!
* user-identities-historicid
* user-identities-schoolid
* user-email-address
* **School Fields:** Try to map as many of the source fields listed below as possible, with emphasis on name and date. For each column set, you will want to map the same user-education-...-\* fields, so you may end up with several columns mapped to user-education-schools-ceeb-*, user-education-schools-name-*, etc..
* user-education-schools-ceeb-\*
* user-education-schools-name-\*
* user-education-schools-street1-\*
* user-education-schools-street2-\*
* user-education-schools-city-\*
* user-education-schools-state-\*
* user-education-schools-zip-\*
* user-education-schools-county-\*
* user-education-schools-country-\*
* user-education-schools-cumulative-gpa-\*
* user-education-schools-gpa\_official-\*
* user-education-schools-start-\*
* user-education-schools-end-\*
* user-education-schools-graduate-\*
* This is the "Did you or will you graduate? Y/N" field
* user-education-schools-degree-earned-\*
* user-education-schools-counselor-email-new-\*
* user-education-schools-counselor-first-name-\*
* user-education-schools-counselor-last-name-\*

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486354947/3ff64e7cb74edd0df34d476890c7/Pro+Tip+-+Orng.png?expires=1784333700&signature=828c7c455cd51e5747e2b957bc2ee68e25e0daa308b69a8c0f07016d391fa2a9&req=dSQvEMp7mYhbXvMW1HO4zQvsE0PLir7OEudSIdug%2BONUWjD%2FwNYJoXF%2B1GP%2F%0ASC0G%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486354947/3ff64e7cb74edd0df34d476890c7/Pro+Tip+-+Orng.png?expires=1784333700&signature=828c7c455cd51e5747e2b957bc2ee68e25e0daa308b69a8c0f07016d391fa2a9&req=dSQvEMp7mYhbXvMW1HO4zQvsE0PLir7OEudSIdug%2BONUWjD%2FwNYJoXF%2B1GP%2F%0ASC0G%0A)

  We suggest renaming the headers in the file to include the position that the schools refer to. In our continues example for Method 2, columns 4-7 may be named High School 1 CEEB, High School 1 Name, Source 1 Segment, Source 1 Date. Columns 11-18 may be named Source 2 Type, Source 2 Alias, Source 2 Segment, Source 2 Date. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right term for the chunk of columns.

Scoping Notice that the source fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. For schools, the scoping settings are school type, position, and zip code. When selecting the settings, you are telling the system that you are importing a school with these qualities, if a school does not exist with those qualities, create a new one, if one does exist, update it. Without the star mappings, the system updates whatever school is on the record's profile, potentially wiping a historic school. For importing source using Method 2, for each field on your import, you will set the scoping settings to whatever school type and position you want them to feed into. Since Method 2 will have a chunk of columns dedicated to one school in one position, another chunk dedicated to the another school in the second position and so forth, for scoping, you will select the position that the chunk of columns represent. For example, columns 4-15 would be High School 1, 16-27 would be High School 2, 28-39 would be College 1, and so forth.

Importing Schools using Method 3 If your file follows Method 3, where you have one file that repeats on schools and includes a row number of an identity, follow the instructions for mapping below. For this method, you must be familiar with our formula builder. Our list of functions can be found [here](https://integrations.element451.com/calculated-fields-37). Mapping The following fields should be mapped when importing school history: Standard Mapping

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!
* user-identities-historicid
* user-identities-schoolid
* user-email-address

Calculated Field Mapping The following source fields will be Calculated Fields. This means you will scroll to the bottom of your import and select "Add a Mapping" > select "Calculated" > then search for the fields below. Depending on how many schools one record has, will determine how many of each calculated field you have to add multiplied by two, to factor in the school being either a high school or college. Is the max row number over identities three, meaning a record has three schools? That means you will be creating six calculated fields for user-sources-type-*, six calculated fields for user-sources-alias-*, etc..

* **School Fields:** Try to map as many of the school fields listed below as possible.
* user-education-schools-ceeb-\*
* user-education-schools-name-\*
* user-education-schools-street1-\*
* user-education-schools-street2-\*
* user-education-schools-city-\*
* user-education-schools-state-\*
* user-education-schools-zip-\*
* user-education-schools-county-\*
* user-education-schools-country-\*
* user-education-schools-cumulative-gpa-\*
* user-education-schools-gpa\_official-\*
* user-education-schools-start-\*
* user-education-schools-end-\*
* user-education-schools-graduate-\*
* This is the "Did you or will you graduate? Y/N" field
* user-education-schools-degree-earned-\*
* user-education-schools-counselor-email-new-\*
* user-education-schools-counselor-first-name-\*
* user-education-schools-counselor-last-name-\*

Scoping and Formulas for Calculated Fields When adding Calculated Fields, you will be prompted to immediately select your scoping settings and add a formula. On each field you will select a position. The order you build these doesn't matter as long as by the end you have enough of each field that cover the max number of schools a record has multiplied by two to consider if the school is either a high school or college. Now for the formulas! Each formula is going to contain an IF statement. With the file having several sources in different rows, we'll be using IF statements to make sure we are putting the correct school type and position into the system. To set the scene of our example, column 4 is our school type, column 5 is the school ceeb, 6 is the graduate date, and 7 is the row number over the identities. The max amount of schools a record has is three. Note: For our examples, we won't be mapping column 4, school type, but we will use it in each formula to make sure we create the correct high school or college item. School CEEB Formulas For example, if using the ApplyTexas CSV template, the CEEB code can be derived by extracting the last six characters from the HS\_code column. A formula for this might look like: IF([C4]="High School" & [C7]="1",SUBSTRING([C5],LEN([C5])-5,6),"") You'll be building six different formulas for user-education-schools-ceeb-\* fields. They'll be very similar, just different conditions to determine if it is a high school or college and position. Below is what the user-education-schools-ceeb-\* scoped to High School and position 1 would look like: IF([C4]&#x3D;"High School" & [C7]&#x3D;"1",[C5],"") The formula checks if the school type is High School and the row number is 1, if it is, it pulls the CEEB in to the field that is scoped the High School and Position 1, if not, it doesn't import anything. Below is the formula for user-education-schools-ceeb-\* scoped to High School and position 2: IF([C4]&#x3D;"High School" & [C7]&#x3D;"2",[C5],"") You would continue this pattern, switching out the positions. For user-education-schools-ceeb-\* scoped to College and position 1, that would look the following: IF([C4]&#x3D;"College" & [C7]&#x3D;"1",[C5],"") Then you would continue with similar pattern of switching out the positions. School Graduation Date Formula You'll be building six different formulas for user-education-schools-end-\* fields. They'll be very similar, just different conditions to determine if it is a high school or college and position. Below is what the user-education-schools-end-\* scoped to High School and position 1 would look like: IF([C4]&#x3D;"High School" & [C7]&#x3D;"1",DATE\_READ([C6],"m/d/Y"),"") The formula checks if the school type is High School and the row number is 1, if it is, it pulls the graduation date into the field that is scoped the High School and Position 1, if not, it doesn't import anything. Below is the formula for user-education-schools-end-\* scoped to High School and position 2: IF([C4]&#x3D;"High School" & [C7]&#x3D;"2",DATE\_READ([C6],"m/d/Y"),"") You would continue this pattern, switching out the positions. For user-education-schools-end-\* scoped to College and position 1, that would look the following: IF([C4]&#x3D;"College" & [C7]&#x3D;"1",DATE\_READ([C6],"m/d/Y"),"") Then you would continue with similar pattern of switching out the positions.

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486357371/1515edece0235694fde9aa7aa714/Pro+Tip+-+Orng.png?expires=1784430000&signature=fbf3e3c16deb6ad637292df3496338d11780eff331264ea6147f45dc4cf5f50b&req=dSQvEMp7moJYWPMW3Hu4gRyOPVrEVgJLUfBtoJebHlLpy6jkhhBD5CzlsbzG%0AGA%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

---