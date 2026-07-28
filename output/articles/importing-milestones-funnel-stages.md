---
title: Importing Milestones/Funnel Stages
url: https://help.element451.com/en/articles/11048532-importing-milestones-funnel-stages
collection: Data Management
---

Tracking a student's progression through the funnel stages is found on Element451's Milestones. For more information on comparing Milestones to Funnel Stages, check out our Funnel Stages article.

Milestones get automatically generated as records complete applications, fill out forms, and sign up for events, but you can also import in milestones. While there are a lot of milestone types that you can import into, this article will focus on importing milestones as it related to funnel stages:

* Inquiry
* Application Start
* Application Submit
* Admit
* Deposit
* Enroll

Milestones are more than just dates, records may go through the funnel multiple times, so to capture the full picture of their funnel stage, milestones associate a term, major, and student type with the date the event happened. This is something to keep in mind as you create your files and import milestone data.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1465115571/b8f22409fe7f13f51e14cb87ed24/Screenshot+2025-04-08+at+9_50_05%E2%80%AFAM.png?expires=1784333700&signature=4fd44aae3aff9e69173619b06b9f7c346ecc47e3b1b256117da81c6855f9f04e&req=dSQhE8h%2FmIRYWPMW1HO4zalRCzQaGYU%2F110B1tKay9pUed14IsrHIAdbFHFD%0A9NOfk55j9txEyE4oGtM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1465115571/b8f22409fe7f13f51e14cb87ed24/Screenshot+2025-04-08+at+9_50_05%E2%80%AFAM.png?expires=1784333700&signature=4fd44aae3aff9e69173619b06b9f7c346ecc47e3b1b256117da81c6855f9f04e&req=dSQhE8h%2FmIRYWPMW1HO4zalRCzQaGYU%2F110B1tKay9pUed14IsrHIAdbFHFD%0A9NOfk55j9txEyE4oGtM%3D%0A)

## Creating Milestone Files

As a reminder, the files need to be either .csv or .txt, contain a unique identifier (or a few!), and only have one row per contact. There are a few methods we recommend making files of milestone data.

1. **Generate Separate Files for Each Term + Milestone Type.** Depending on how much historic data you bring into Element451, your files would look something like: a file for Spring 2025 Inquiry Dates, a file for Spring 2025 Application Start Dates, a file for Spring 2025 Application Submit Dates, a file for Spring 2025..., a file for Fall 2025 Inquiry Dates, a file for Fall 2025 Application Start Dates, a file for Fall 2025 Application Submit Dates, a file for Fall 2025..., etc.
2. **Generate Separate Files for Each Term.** In this method, you would have a Spring 2025 file that contains Inquiry Dates, Application Start Dates, Application Submit Dates, Admit Dates, Deposit Dates, Enroll Dates. Then you would have a Fall 2025 file with their respective dates, and so forth.
3. **Generate File where Milestones Types are in Column Sets.**

   1. If going with this option, it would be preferable for the column sets be associated with specific terms. For example, columns 4-8 are for Fall 2025 Inquiry Dates. If a student has an inquiry date for Fall 2025 they have data in these columns, if not, the cells are blank. Next, columns 9-13 are for Fall 2025 Application Start Dates and so on.
   2. The last option, which will require the most work to prevent milestone overwriting, is the column sets not being associated to specific terms. For example, columns 4-8 are Inquiry Dates for various terms, columns 9-13 are Application Start Dates for various terms and so on

## Fields to Include in the File

Listed are fields you can include on your milestone files. The bolded fields are strongly recommended.

* **Contact Identifiers (Student ID, Historic ID, and/or Email)**
* **Date of Milestone**
* **Term associated to Milestone**
* Major associated to Milestone
* Student Type associated to Milestone
* Degree associated to Milestone

## Importing Milestones using Method 1

With separate files for each milestone type + term combination, you will be creating import tasks for each file that are identical in column layout, but different scoping set up inside the milestone fields. There is a Historic Milestone Import template in your instance, but you are not required to follow that exact layout if you need additional unique identifiers or need to put the fields in a different order, the template is a starting point if you need direction.

## Mapping

The following fields should be mapped when importing milestones:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Milestone Fields:** Try to map as many of the milestone fields listed below as possible, with emphasis on date and term. Think about how you will segment these records, for example, if you are going to want to search for freshman inquiries from Fall 2024, know that you will want to populate data in the in student type and term fields.

  + user-milestones-date-\*
  + user-milestones-term-\*
  + user-milestones-major-\*
  + user-milestones-student-type-\*
  + user-milestones-degree-\*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1465231977/4729d102e29830613c56bae93872/Screenshot+2025-04-08+at+10_49_35%E2%80%AFAM.png?expires=1784333700&signature=5923edac0e5ec7271ccea2f78c9ef86d699296cf2a10f01979534587b5167c9e&req=dSQhE8t9nIhYXvMW1HO4zcNn%2BOI45SDjgnZyUsX%2BWJlefhRK%2BAt32T%2BQxrBQ%0AEogf9tDxqZRB5OzoQZ4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1465231977/4729d102e29830613c56bae93872/Screenshot+2025-04-08+at+10_49_35%E2%80%AFAM.png?expires=1784333700&signature=5923edac0e5ec7271ccea2f78c9ef86d699296cf2a10f01979534587b5167c9e&req=dSQhE8t9nIhYXvMW1HO4zcNn%2BOI45SDjgnZyUsX%2BWJlefhRK%2BAt32T%2BQxrBQ%0AEogf9tDxqZRB5OzoQZ4%3D%0A)

## Scoping

Notice that the milestone fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. The settings vary but can be position, term, application type, milestone type, and a few more.

When selecting the settings, you are telling the system that you are importing a milestone with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it. Without the star mappings, the system updates whatever milestone is on the record's profile, potentially wiping a historic application.

For importing milestones using Method 1, for each field on your import, you will set the scoping settings to whatever milestone type you want them to feed into and you will select a term. Since Method 1 instructs you to have separate files for each milestone type + term combination, each import will have the same column headers but the scoping settings will reflect the file you are importing. For your Fall 2025 Inquiry file, all the scoping settings should be "Fall 2025" and milestone type "Date of Inquiry" on each milestone field, as an example.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1465261901/be2bcc2325504b0ba1aa722d6949/Screenshot+2025-04-08+at+11_02_56%E2%80%AFAM.png?expires=1784333700&signature=5c087ccfa75a2aed7a026146e06a90a3dfead26742515a0febbf888fc291a979&req=dSQhE8t4nIhfWPMW1HO4zRl7m9ESpX8CWBhf%2BhLbl0j7r8%2FD00nYXCiuoTpX%0AbRJjG1ZkH86DVa3F1%2B4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1465261901/be2bcc2325504b0ba1aa722d6949/Screenshot+2025-04-08+at+11_02_56%E2%80%AFAM.png?expires=1784333700&signature=5c087ccfa75a2aed7a026146e06a90a3dfead26742515a0febbf888fc291a979&req=dSQhE8t4nIhfWPMW1HO4zRl7m9ESpX8CWBhf%2BhLbl0j7r8%2FD00nYXCiuoTpX%0AbRJjG1ZkH86DVa3F1%2B4%3D%0A)

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486313225/a30dba50a4597f3ae9686f490e36/Important+-+Orng.png?expires=1784430000&signature=c31b2f276453b8d3767b5ff11d490b9af98aa7de1257a367efa70da1e681be2c&req=dSQvEMp%2FnoNdXPMW3Hu4gcNqm0OtBbV%2FLQ%2BjX60XFetc2r1GPjOsvQbtLPGt%0A9Q%3D%3D%0A) Position is NOT required, and that is what makes star fields so flexible! We don't know if a record has an milestone, and if we did, we don't know how many they have and what position the Fall 2025 Date of Inquiry is in. The scoping set up in the screenshot is the search criteria for determining if the milestone gets created or updated on the record's milestone card.

## Importing Milestones using Method 2

With separate files for terms, you will be creating import tasks for each file that are identical in column layout, but different scoping set up inside the all of the milestone fields.

## Mapping

The following fields should be mapped when importing milestones:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Milestone Fields:** Try to map as many of the milestone fields listed below as possible. Think about how you will segment these records, for example, if you are going to want to search for freshman inquiries from Fall 2024, know that you will want to populate data in the in student type and term fields. For each column set, you will want to map the same user-milestone-...-\* fields, so you may end up with several columns mapped to user-milestones-date-\*, user-milestones-major-\*, etc..

  + user-milestones-date-\*
  + user-milestones-term-\*
  + user-milestones-major-\*
  + user-milestones-student-type-\*
  + user-milestones-degree-\*

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486314483/95d0c7739a3dda869f10080c3b79/Pro+Tip+-+Orng.png?expires=1784430000&signature=11313c1f8325ba7902c320cd49615dbf6ae5b96413ad649e14c126ca51bd6133&req=dSQvEMp%2FmYVXWvMW3Hu4gdNYRoyh3IFACHGbxiYxH8o%2BNIHx94z6brhHAdOG%0AgA%3D%3D%0A) We suggest renaming the headers in the file to include the milestone type that the column refers to. For example, columns 4-8 are for Date of Inquiry, columns 9-13 are for Application Start Date, and so on. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right milestone type for the chunk of columns.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467568865/095ea5025a03cb672c6a4dc963fc/Screenshot%2B2025-04-09%2Bat%2B2_02_17-E2-80-AFPM.png?expires=1784333700&signature=4fe28ae6b0e351e08dfab34e4de63fd0d8eeef4f3351b72571977ec73fa97bb2&req=dSQhEcx4lYlZXPMW1HO4zWDEwawwV%2BkK0zm26vktEcTkRlWpPbOFuWNNqleT%0AWm0CTxp1vPfPaeuHmeE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467568865/095ea5025a03cb672c6a4dc963fc/Screenshot%2B2025-04-09%2Bat%2B2_02_17-E2-80-AFPM.png?expires=1784333700&signature=4fe28ae6b0e351e08dfab34e4de63fd0d8eeef4f3351b72571977ec73fa97bb2&req=dSQhEcx4lYlZXPMW1HO4zWDEwawwV%2BkK0zm26vktEcTkRlWpPbOFuWNNqleT%0AWm0CTxp1vPfPaeuHmeE%3D%0A)

## Scoping

Notice that the milestone fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. The settings vary but can be position, term, application type, milestone type, and a few more.

When selecting the settings, you are telling the system that you are importing a milestone with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it. Without the star mappings, the system updates whatever milestone is on the record's profile, potentially wiping a historic application.

For importing milestones using Method 2, for each field on your import, you will set the scoping settings to whatever milestone type you want them to feed into and you will select the term. Since Method 2 instructs you to have separate files for each term, each import will have the same column headers but the scoping settings will reflect the file you are importing. For your Fall 2025 file, all the scoping settings should be "Fall 2025" and depending on the column set, you would select the milestone type. In the example for Method 2, columns 4-8 would be "Date of Inquiry" type, columns 9-13 would be "Application Start Date" type, etc..

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467583324/5c168326e3bf2d3bf50df67efb92/Screenshot+2025-04-09+at+2_12_53%E2%80%AFPM.png?expires=1784333700&signature=9f0d2e8180ea0b25817f8d5df0bf33ca010ab8390224608bd2d03f46e626d70a&req=dSQhEcx2noJdXfMW1HO4zX8GLsp%2F49tji5HPMMnUdEdmw%2BaKsz5I8sNJ3Mmo%0AGeVAuz5m6pt79He0Ock%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467583324/5c168326e3bf2d3bf50df67efb92/Screenshot+2025-04-09+at+2_12_53%E2%80%AFPM.png?expires=1784333700&signature=9f0d2e8180ea0b25817f8d5df0bf33ca010ab8390224608bd2d03f46e626d70a&req=dSQhEcx2noJdXfMW1HO4zX8GLsp%2F49tji5HPMMnUdEdmw%2BaKsz5I8sNJ3Mmo%0AGeVAuz5m6pt79He0Ock%3D%0A)

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486315733/33c5ce6699f217e6b99747d0cf58/Important+-+Orng.png?expires=1784430000&signature=b037bef773cb9f5052d6c5d260282a894d1d479b26c65707ef7ec14bea4ef78a&req=dSQvEMp%2FmIZcWvMW3Hu4gXjBqkwYjKe7uwSet5I7W2w%2F9jhBsiTtwsve2F6x%0AMA%3D%3D%0A) Position is NOT required, and that is what makes star fields so flexible! We don't know if a record has an milestone, and if we did, we don't know how many they have and what position the Fall 2025 Application Start is in. The scoping set up in the screenshot is the search criteria for determining if the milestone gets created or updated on the record's milestone card.

## Importing Milestones using Method 3a

If your file follows Method 3a, where you have one file with column sets that are associated with specific terms and milestone types, follow the instructions for mapping below.

## Mapping

The following fields should be mapped when importing milestones:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Milestone Fields:** Try to map as many of the milestone fields listed below as possible. Think about how you will segment these records, for example, if you are going to want to search for freshman inquiries from Fall 2024, know that you will want to populate data in the in student type and term fields. For each column set, you will want to map the same user-milestone-...-\* fields, so you may end up with several columns mapped to user-milestones-date-\*, user-milestones-major-\*, etc..

  + user-milestones-date-\*
  + user-milestones-term-\*
  + user-milestones-major-\*
  + user-milestones-student-type-\*
  + user-milestones-degree-\*

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486316198/8df931aa17594d07453bd20360b6/Pro+Tip+-+Orng.png?expires=1784430000&signature=84577431eb9cb62a80cba0eb8bebc6caa198fc9d88dc1e23d7fa02faaef5a723&req=dSQvEMp%2Fm4BWUfMW3Hu4gSSjoxOJwNRDDMENmQ663PSGIAHEsi6IBzOtK%2BxN%0Aow%3D%3D%0A) We suggest renaming the headers in the file to include the milestone type that the column refers to. For example, columns 4-8 are for Date of Inquiry for Fall 2025, columns 9-13 are for Application Start Date for Spring 2026, and so on. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right milestone type for the chunk of columns.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467707250/6e1c9b65a8063aa0c033f3bbaed9/Screenshot+2025-04-09+at+3_36_01%E2%80%AFPM.png?expires=1784333700&signature=c11dc40a6b4ba044a9e5f09c6453354893288f57891ecf68b026fffdf39bafa5&req=dSQhEc5%2BmoNaWfMW1HO4zQCMV%2Fu23zm62WEh1kYX7RrTKL%2BQ4h8qLqbV%2FNYo%0AUCJZ1X%2BbGADWUk4mR80%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467707250/6e1c9b65a8063aa0c033f3bbaed9/Screenshot+2025-04-09+at+3_36_01%E2%80%AFPM.png?expires=1784333700&signature=c11dc40a6b4ba044a9e5f09c6453354893288f57891ecf68b026fffdf39bafa5&req=dSQhEc5%2BmoNaWfMW1HO4zQCMV%2Fu23zm62WEh1kYX7RrTKL%2BQ4h8qLqbV%2FNYo%0AUCJZ1X%2BbGADWUk4mR80%3D%0A)

## Scoping

Notice that the milestone fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. The settings vary but can be position, term, application type, milestone type, and a few more.

When selecting the settings, you are telling the system that you are importing a milestone with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it. Without the star mappings, the system updates whatever milestone is on the record's profile, potentially wiping a historic application.

For importing milestones using Method 3a, for each field on your import, you will set the scoping settings to the milestone type and term that is intended. Since Method 3a will have a chunk of columns dedicated to one term and milestone type, another chunk dedicated to a different term and milestone type, and so forth, for scoping, you will select the term and milestone type that the chunk of columns represent.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467754025/1e9547ac4025e7c89c4028511d2c/Screenshot%2B2025-04-09%2Bat%2B2_12_53-E2-80-AFPM.png?expires=1784333700&signature=2723cf6600b6f5a0dba342555fa213a47957317dc5bf3ca325d9ff62f49cea18&req=dSQhEc57mYFdXPMW1HO4zfbhsYMLRMNkoDRMMGyikWGJev2u0TY3jhTDJN7a%0Ai1vZctrohJdb%2BYrYl8k%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1467754025/1e9547ac4025e7c89c4028511d2c/Screenshot%2B2025-04-09%2Bat%2B2_12_53-E2-80-AFPM.png?expires=1784333700&signature=2723cf6600b6f5a0dba342555fa213a47957317dc5bf3ca325d9ff62f49cea18&req=dSQhEc57mYFdXPMW1HO4zfbhsYMLRMNkoDRMMGyikWGJev2u0TY3jhTDJN7a%0Ai1vZctrohJdb%2BYrYl8k%3D%0A)

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486316859/bb631d61b5fc75deab742a90bd74/Important+-+Orng.png?expires=1784430000&signature=8d06051af22caf6087b9abc82b1c1fb81a614cf7faed5c03c90864bd35ddbfba&req=dSQvEMp%2Fm4laUPMW3Hu4gZQqLWvDdr%2F84XfhLVIM7GYEkXdWFxx37O4MTfjG%0AZw%3D%3D%0A) Position is NOT required, and that is what makes star fields so flexible! We don't know if a record has an application, and if we did, we don't know how many they have and what position the Fall 2025 application is in. The scoping set up in the screenshot is the search criteria for determining if the application get's created or updated on the record's application card.

## Importing Milestones using Method 3b

If your file follows Method 3b, where you have one file with column sets that are associated with a students Date of Inquiry for any term, Application Start for any term, Application Submit for any term, etc.., follow the instructions for mapping below. For this method, you must be familiar with our formula builder. Our list of functions can be found here.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486318190/8111d193f364029c627e4710070d/Pro+Tip+-+Orng.png?expires=1784430000&signature=fc8b0e177c0a0fc83ee9d8d8ed821879e263f280822ba32ddcd0c54195af9e8d&req=dSQvEMp%2FlYBWWfMW3Hu4gTDWaz4JDZC1zvRxcqgItbgJJXi55MPFYMMyz%2BB2%0AOw%3D%3D%0A) We suggest renaming the headers in the file to include the milestone type and position that the column set refers to. In our continuous example for Method 3b, columns 4-8 may be named Date of Inquiry, Date of Inquiry Term, Date of Inquiry Major, etc.. Columns 9-13 may be named App Start Date, App Start Term, App Start Major, etc.. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right term for the chunk of columns.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486321345/10bebb822949b93453541e1e067b/Screenshot+2025-04-21+at+10_32_51%E2%80%AFAM.png?expires=1784333700&signature=53750ad4dce46a0fa4dcb32258e50c7e931cd9b9f19c87a420da9ce26e40beff&req=dSQvEMp8nIJbXPMW1HO4zb0cslAREnHHo3fMyCYaxEuExY1GXdkhw6umHZtK%0AJLCZXWqnr4tSGGzJyJI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486321345/10bebb822949b93453541e1e067b/Screenshot+2025-04-21+at+10_32_51%E2%80%AFAM.png?expires=1784333700&signature=53750ad4dce46a0fa4dcb32258e50c7e931cd9b9f19c87a420da9ce26e40beff&req=dSQvEMp8nIJbXPMW1HO4zb0cslAREnHHo3fMyCYaxEuExY1GXdkhw6umHZtK%0AJLCZXWqnr4tSGGzJyJI%3D%0A)

## Mapping

The following fields should be mapped when importing milestones:

## **Standard Mapping:**

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address

## **Calculated Field Mapping:**

The following application fields will be Calculated Fields. This means you will scroll to the bottom of you import and select "Add a Mapping" > select "Calculated" > then search for the fields below. Depending on how many unique terms are mentioned in your file will determine how many of each calculated field you have to add. Does your file contain milestones for Fall 2025, Spring 2026, and Summer 2026? That means you will be creating 3\*# of milestone types of calculated fields user-milestones-date-\*, 3\*# of milestone types calculated fields for user-milestones-term-\*, etc.. So if you are bringing in App Start and App Submit milestones for Fall 2025, Spring 2026, and Summer 2026, you would be building six user-milestones-date-\* calculated fields, six user-milestones-term-\* calculated fields, etc.

* **Milestone Fields:** Try to map as many of the milestone fields listed below as possible. Think about how you will segment these records, for example, if you are going to want to search for freshman inquiries from Fall 2024, know that you will want to populate data in the in student type and term fields.

  + user-milestones-date-\*
  + user-milestones-term-\*
  + user-milestones-major-\*
  + user-milestones-student-type-\*
  + user-milestones-degree-\*

## Scoping and Formulas for Calculated Fields

When adding Calculated Fields, you will be prompted to immediately select your scoping settings and add a formula. You will select an milestone type and a term. Using our example above, you would select either Application Start or Application Submit for type and Fall 2025, Spring 2026, or Summer 2026 for term. The order you build these doesn't matter as long as by the end you have six user-milestones-date-\* calculated fields that are scoped to one of the three terms in the file, six user-milestones-term-\* calculated fields that are scoped to one of the three terms in the file, and so forth.

Now for the formulas! With the file having various terms in each column, we'll be using IF statements to determine what columns are associated to what term for any given student. To set the scene of our example, columns 4-8 represents the students Application Start milestone, could be for any term, and columns 9-13 would be their Application Submit milestone for any term. Column 4 and 9 are dates, 5 and 10 are terms, 6 and 11 are majors, 7 and 12 are student types, and 8 and 13 are degrees.

## Milestone Date Formulas

Listed below will be examples of the formulas for the user-milestones-date-\* fields. We are using the example from above.

For user-milestones-date-\* scoped to Application Start Date and Fall 2025:

```
IF([C5]="Fall 2025",DATE_READ([C4],"m-d-Y"),"")
```

The formula checks to see if the App Start Term column equals Fall 2025, if so, it pulls the date associated to it. If the term is not Fall 2025, it inserts nothing.

Repeating these steps, the next formula for user-milestones-date-\* that is scoped to Application Start Date and Spring 2026 would look like:

```
IF([C5]="Spring 2026",DATE_READ([C4],"m-d-Y"),"")
```

The formula checks to see if the App Start Term column equals Spring 2026, if so, it pulls the date associated to it. If the term is not Spring 2026, it inserts nothing.

For the Application Submit milestone, the formula for user-milestones-date-\* will be very similar but with a different scope. The scope would be switched to Application Submit Date, and when the term is set to Fall 2025, the formula would look like:

```
IF([C10]="Fall 2025",DATE_READ([C9],"m-d-Y"),"")
```

Though the formulas are very similar, make sure your scopes align with the milestone and term you are wanting to build. Inside the formula, make sure the [C#] are pulling the correct columns.

## Milestone Term Formulas

Listed below will be examples of the formulas for the user-milestones-term-\* fields. We are using the example from above.

For user-milestones-term-\* scoped to Application Start and Fall 2025:

```
IF([C5]="Fall 2025",DB_MAP("term",[C5],"name","guid",""),"")
```

The formula checks to see if the App Start Term column equals Fall 2025, if so, it pulls the term. If the term is not Fall 2025, it inserts nothing.

Repeating these steps, the next formula for user-milestones-term-\* that is scoped to Application Start and Spring 2026 would look like:

```
IF([C5]="Spring 2026",DB_MAP("term",[C5],"name","guid",""),"")
```

The formula checks to see if the App Start Term column equals Spring 2026, if so, it pulls the term. If the term is not Spring 2026, it inserts nothing.

For the Application Submit milestone, the formula for user-milestones-term-\* will be very similar but with a different scope. The scope would be switched to Application Submit, and when the term is set to Fall 2025, the formula would look like:

```
IF([C10]="Fall 2025",DB_MAP("term",[C10],"name","guid",""),"")
```

Though the formulas are very similar, make sure your scopes align with the milestone and term you are wanting to build. Inside the formula, make sure the [C#] are pulling the correct columns.

## Milestone Major Formulas

Listed below will be examples of the formulas for the user-milestones-major-\* fields. We are using the example from above.

For user-milestones-major-\* scoped to Application Start and Fall 2025:

```
IF([C5]="Fall 2025",DB_MAP("major",[C6],"name","guid",""),"")
```

The formula checks to see if the App Start Term column equals Fall 2025, if so, it pulls the major. If the term is not Fall 2025, it inserts nothing.

Repeating these steps, the next formula for user-milestones-major-\* that is scoped to Application Start and Spring 2026 would look like:

```
IF([C5]="Spring 2026",DB_MAP("major",[C6],"name","guid",""),"")
```

The formula checks to see if the App Start Term column equals Spring 2026, if so, it pulls the major. If the term is not Spring 2026, it inserts nothing.

For the Application Submit milestone, the formula for user-milestones-major-\* will be very similar but with a different scope. The scope would be switched to Application Submit, and when the term is set to Fall 2025, the formula would look like:

```
IF([C10]="Fall 2025",DB_MAP("major",[C11],"name","guid",""),"")
```

Though the formulas are very similar, make sure your scopes align with the milestone and term you are wanting to build. Inside the formula, make sure the [C#] are pulling the correct columns.

## Milestone Student Type Formulas

Listed below will be examples of the formulas for the user-milestones-student-type-\* fields. We are using the example from above.

For user-milestones-student-type-\* scoped to Application Start and Fall 2025:

```
IF([C5]="Fall 2025",  
DS_MAP([C7],"example.data_source.1234","column_1","column_2",""),"")
```

The formula checks to see if the App Start Term column equals Fall 2025, if so, it pulls the student type. If the term is not Fall 2025, it inserts nothing.

Repeating these steps, the next formula for user-milestones-student-type-\* that is scoped to Application Start and Spring 2026 would look like:

```
IF([C5]="Spring 2026",  
DS_MAP([C7],"example.data_source.1234","column_1","column_2",""),"")
```

The formula checks to see if the App Start Term column equals Spring 2026, if so, it pulls the student type. If the term is not Spring 2026, it inserts nothing.

For the Application Submit milestone, the formula for user-milestones-student-type-\* will be very similar but with a different scope. The scope would be switched to Application Submit, and when the term is set to Fall 2025, the formula would look like:

```
IF([C10]="Fall 2025",  
DS_MAP([C12],"example.data_source.1234","column_1","column_2",""),"")
```

Though the formulas are very similar, make sure your scopes align with the milestone and term you are wanting to build. Inside the formula, make sure the [C#] are pulling the correct columns.

## Milestone Degree Formulas

Listed below will be examples of the formulas for the user-milestones-degree-\* fields. We are using the example from above.

For user-milestones-degree-\* scoped to Application Start and Fall 2025:

```
IF([C5]="Fall 2025",  
DS_MAP([C8],"data_source.degrees_ref","name","code",""),"")
```

The formula checks to see if the App Start Term column equals Fall 2025, if so, it pulls the degree. If the term is not Fall 2025, it inserts nothing.

Repeating these steps, the next formula for user-milestones-degree-\* that is scoped to Application Start and Spring 2026 would look like:

```
IF([C5]="Spring 2026",  
DS_MAP([C8],"data_source.degrees_ref","name","code",""),"")
```

The formula checks to see if the App Start Term column equals Spring 2026, if so, it pulls the degree. If the term is not Spring 2026, it inserts nothing.

For the Application Submit milestone, the formula for user-milestones-degree-\* will be very similar but with a different scope. The scope would be switched to Application Submit, and when the term is set to Fall 2025, the formula would look like:

```
IF([C10]="Fall 2025",  
DS_MAP([C13],"data_source.degrees_ref","name","code",""),"")
```

Though the formulas are very similar, make sure your scopes align with the milestone and term you are wanting to build. Inside the formula, make sure the [C#] are pulling the correct columns.

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486324582/55987357e6f09ac7d5f61dfe13fb/Pro+Tip+-+Orng.png?expires=1784430000&signature=36b5adf5ce34e94d675f18744e4cf2fba5a7572699200a6359c62129ab90bf5b&req=dSQvEMp8mYRXW%2FMW3Hu4gRuuchKGKE2CrEF97Hv6K0%2Fz1ptrGGKm2Z9zmSMW%0Aeg%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

---