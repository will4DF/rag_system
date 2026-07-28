---
title: Importing Historic Application Data
url: https://help.element451.com/en/articles/10776247-importing-historic-application-data
collection: Data Management
---

Use this guide for getting historic applications into your instance to make your reports come to life.

This article will follow very closely to our [Importing Application Data article](https://help.element451.com/en/articles/9007767-importing-application-data). The main article, has further explanations on how to import applications on a regular basis, and even explains how to make imported applications look like live Element451 applications. For this article, we are keeping it simple and focussing only on importing historic applications.

## Creating Application Files

As a reminder, the files need to be either .csv or .txt, contain a unique identifier (or a few!), and only have one row per contact. There are two ways we recommend making files of application data.

1. **Our preferred method: Generate separate files per application.** This is usually done by term. For example, one import file with Fall 2024 applications, another with Spring 2025 applications and so on. Each file will require it's own Import Task.
2. **Format application data into column sets.** In this scenario, column 4-11, for example, would belong to one application, then columns 12-18 is another application and so on. This "flattens" the file to repeat on one row per contact.

   1. If going with this option, it would be preferable for the column sets be associated with specific terms. For example, columns 4-11 are for Fall 2025 applications. If a student has an application for Fall 2025 they have data in these columns, if not, the cells are blank. Next, columns 12-18 are for Spring 2026 and so on.
   2. The last option, which will require the most work to prevent application overwriting, is the column sets not being associated to specific terms. This means columns 4-11 represents the students first application, could be for any term, and columns 12-18 would be their second application for a different term and so on.

## Fields to Include in the File

Listed are fields you can include on your application file. The bolded fields are strongly recommended.

* **Contact Identifiers (Student ID, Historic ID, and/or Email)**
* **Application Term**
* **Application Major**
* **Application Student Type**
* Application Degree
* Application Campus
* Application Concentration
* Application School
* Application Housing Type
* **Application Start Date**
* Application Completed Date

  + This is the date they completed all the required fields in the application, prior to hitting the submit button.
* **Application Submit Date**
* Application Status

  + This can be "started", "completed", or "submitted" and is not related to the decision.
* Convicted?
* Convicted Explanation
* School Problems?
* School Problems Explanation

## Importing Applications using Method 1

With separate files for each application term, you will be creating import tasks for each file that are identical in column layout, but different scoping set up inside the application fields. There is a Historic Application Import template in your instance, but you are not required to follow that exact layout if you need additional unique identifiers or need to put the fields in a different order, the template is a starting point if you need direction.

## Mapping

The following fields should be mapped when importing historic applications:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Application Fields:** Try to map as many of the application fields listed below as possible, with emphasis on term, major, student type. Think about how you will segment these records, for example, if you are going to want to search for submitted applications from Fall 2024, know that you will want to populate data in the submitted time and status fields.

  + user-applications-term-\*
  + user-applications-major-\*
  + user-applications-student-type-\*
  + user-applications-degree-\*
  + user-applications-campus-\*
  + user-applications-concentration-\*
  + user-applications-school-\*
  + user-applications-housing-\*
  + user-applications-registered-at-\*

    - This is equivalent to application start date
  + user-applications-completed-at-\*
  + user-applications-submitted-time-\*
  + user-applications-status-\*

    - Data in this field can be "started", "completed", or "submitted" and is NOT related to the decision.
  + user-applications-submission-convicted-\*
  + user-applications-submission-convicted-explanation-\*
  + user-applications-submission-school-problems-\*
  + user-applications-submission-school-problems-explanation-\*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427013424/95c65b609c83908bdf9ebd9cfcb9/Screenshot%2B2025-03-17%2Bat%2B10_17_43-E2-80-AFAM.png?expires=1784333700&signature=25394cce894c92930396bedf2f4db8d66396fed6bd824852d9e795133ec19d7e&req=dSQlEcl%2FnoVdXfMW1HO4zbuaXZyTn1V802JqhHy12WxLd2bPUpNbW84QsRh3%0AeqdmH%2BL1pNIioQPbg8s%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427013424/95c65b609c83908bdf9ebd9cfcb9/Screenshot%2B2025-03-17%2Bat%2B10_17_43-E2-80-AFAM.png?expires=1784333700&signature=25394cce894c92930396bedf2f4db8d66396fed6bd824852d9e795133ec19d7e&req=dSQlEcl%2FnoVdXfMW1HO4zbuaXZyTn1V802JqhHy12WxLd2bPUpNbW84QsRh3%0AeqdmH%2BL1pNIioQPbg8s%3D%0A)

## Scoping

Notice that the application fields we recommend you use have asterisks. We call these Star Mappings and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. The settings can be position, term, application type, milestone type, and a few more.

When selecting the settings, you are telling the system that you are importing an application with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it. Without the star mappings, the system updates whatever application is on the record's profile, potentially wiping a historic application.

For importing applications using Method 1, for each field on your import, you will set the scoping settings to whatever application type you want them to feed into, this is typically an inactive Historic Application type, and you will select a term. Since Method 1 instructs you to have separate files for each application term, each import will have the same column headers but the scoping settings will reflect the file you are importing. For your Fall 2025 file, all the scoping settings should be "Fall 2025" and application type "Historic Application" on each application field, as an example.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427013421/fa68ffd5ce86f4771dba23b61ab7/Screenshot%2B2025-03-17%2Bat%2B10_18_23-E2-80-AFAM.png?expires=1784333700&signature=d94578e607a152bf7185dd8e07415df056d6c06b976f560c8433d88eeb7854b4&req=dSQlEcl%2FnoVdWPMW1HO4zYWX6fJabQ3YUxg8TpM5Zy%2F6TRP0MgeNAi3huXu4%0A2JJPMCNK%2BPFWZ7Ly2sg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427013421/fa68ffd5ce86f4771dba23b61ab7/Screenshot%2B2025-03-17%2Bat%2B10_18_23-E2-80-AFAM.png?expires=1784333700&signature=d94578e607a152bf7185dd8e07415df056d6c06b976f560c8433d88eeb7854b4&req=dSQlEcl%2FnoVdWPMW1HO4zYWX6fJabQ3YUxg8TpM5Zy%2F6TRP0MgeNAi3huXu4%0A2JJPMCNK%2BPFWZ7Ly2sg%3D%0A)

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486297458/50576435419cbe4dee0528add29d/Important+-+Orng.png?expires=1784430000&signature=b2719a4543c101bfffea9254733c1816d382b1c9045c5de792f46e3535234d84&req=dSQvEMt3moVaUfMW3Hu4gWUgOTDU9%2FLBDk8gq7z7tHKPE05NN7wyz6bfT94Z%0AKA%3D%3D%0A) Position is NOT required, and that is what makes star fields so flexible! We don't know if a record has an application, and if we did, we don't know how many they have and what position the Fall 2025 application is in. The scoping set up in the screenshot is the search criteria for determining if the application get's created or updated on the record's application card.

## Importing Applications using Method 2a

If your file follows Method 2a, where you have one file with column sets that are associated with specific terms, follow the instructions for mapping below.

## Mapping

The following fields should be mapped when importing historic applications:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Application Fields:** Try to map as many of the application fields listed below as possible, with emphasis on term, major, student type. Think about how you will segment these records, for example, if you are going to want to search for submitted applications from Fall 2024, know that you will want to populate data in the submitted time and status fields. For each column set, you will want to map the same user-applications-...-\* fields, so you may end up with several columns mapped to user-applications-term-\*, user-applications-major-\*, etc..

  + user-applications-term-\*
  + user-applications-major-\*
  + user-applications-student-type-\*
  + user-applications-degree-\*
  + user-applications-campus-\*
  + user-applications-concentration-\*
  + user-applications-school-\*
  + user-applications-housing-\*
  + user-applications-registered-at-\*

    - This is equivalent to application start date
  + user-applications-completed-at-\*
  + user-applications-submitted-time-\*
  + user-applications-status-\*

    - Data in this field can be "started", "completed", or "submitted" and is NOT related to the decision.
  + user-applications-submission-convicted-\*
  + user-applications-submission-convicted-explanation-\*
  + user-applications-submission-school-problems-\*
  + user-applications-submission-school-problems-explanation-\*

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486298153/85c39f35834ba0923dc8bcf8b0d9/Pro+Tip+-+Orng.png?expires=1784430000&signature=11528051e31e96f3d4f50df78f3b30c5c400dd65b536f5d460fe84ccf3b11d61&req=dSQvEMt3lYBaWvMW3Hu4gTu86I5qYX3R%2B%2BzmHt0PVIn4gU%2FW8QQQsNVC%2B5a7%0A4w%3D%3D%0A) We suggest renaming the headers in the file to include the term that the applications refer to. In our continues example for Method 2a, columns 4-11 may be named FA25 App Term, FA25 App Major, FA25 App Student Type. Columns 11-18 may be named SP26 App Term, SP26 App Major, SP26 App Student Type. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right term for the chunk of columns.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427015635/febb78e14e8f5c5e7e7f738e2a4d/Screenshot+2025-03-17+at+1_36_23%E2%80%AFPM.png?expires=1784333700&signature=4bfe67e888ea36f819505afd8ba54ea9342169c3de3c00180f5d56c8fec7655b&req=dSQlEcl%2FmIdcXPMW1HO4zd6pyba1lGdNPKiJyfy54F1%2BBtD6s%2FWYXgkF%2BPT%2F%0AWvEFDtBlDHHsRfIqgMU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427015635/febb78e14e8f5c5e7e7f738e2a4d/Screenshot+2025-03-17+at+1_36_23%E2%80%AFPM.png?expires=1784333700&signature=4bfe67e888ea36f819505afd8ba54ea9342169c3de3c00180f5d56c8fec7655b&req=dSQlEcl%2FmIdcXPMW1HO4zd6pyba1lGdNPKiJyfy54F1%2BBtD6s%2FWYXgkF%2BPT%2F%0AWvEFDtBlDHHsRfIqgMU%3D%0A)

##

## Scoping

Notice that the application fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten. Any field that is a star mapping, will require scoping settings. The settings can be position, term, application type, milestone type, and a few more.

When selecting the settings, you are telling the system that you are importing an application with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it. Without the star mappings, the system updates whatever application is on the records profile, potentially wiping a historic application.

For importing applications using Method 2a, for each field on your import, you will set the scoping settings to whatever application type you want them to feed into, this is typically an inactive Historic Application type, and you will select a term. Since Method 2a will have a chunk of columns dedicated to one term, another chunk dedicated to a different term, and so forth, for scoping, you will select the term that the chunk of columns represent. In our previous example, columns 4-11 will be scoped to the Historic Application, Fall 2025 and columns 12-18 will be scoped to the Historic Application, Spring 2026.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427021551/d16942a3738a0dde0326c136d16e/Screenshot+2025-03-17+at+1_44_54%E2%80%AFPM.png?expires=1784333700&signature=3f536fad0a12ae97a3ddc0962379101dcdac3583a74510cde07315da77385c82&req=dSQlEcl8nIRaWPMW1HO4zWu9A6CSWYqPKgN6WgBbrll2j9n%2FxkZMA4HGnG3r%0ATzgCDSpf9BFZPd7glM8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427021551/d16942a3738a0dde0326c136d16e/Screenshot+2025-03-17+at+1_44_54%E2%80%AFPM.png?expires=1784333700&signature=3f536fad0a12ae97a3ddc0962379101dcdac3583a74510cde07315da77385c82&req=dSQlEcl8nIRaWPMW1HO4zWu9A6CSWYqPKgN6WgBbrll2j9n%2FxkZMA4HGnG3r%0ATzgCDSpf9BFZPd7glM8%3D%0A)

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486299251/bd84263967601785cc2525608eb9/Important+-+Orng.png?expires=1784430000&signature=2583a1029c1af1b92d7bb18c8cf680756c7cf5616add401bb20ec24b5d7a94f7&req=dSQvEMt3lINaWPMW3Hu4gZaU%2F8JK0ZWXZB6jYonLQQ844KBWN%2F133GAYNZ9j%0AMg%3D%3D%0A) Position is NOT required, and that is what makes star fields so flexible! We don't know if a record has an application, and if we did, we don't know how many they have and what position the Fall 2025 application is in. The scoping set up in the screenshot is the search criteria for determining if the application get's created or updated on the record's application card.

## Importing Applications using Method 2b

If your file follows Method 2b, where you have one file with column sets that are associated with a students first application, second application, third application, etc.., follow the instructions for mapping below. For this method, you must be familiar with our formula builder. Our list of functions can be found [here](https://integrations.element451.com/calculated-fields-37).

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486299606/d8b87b566018a2087366d9f83c4b/Pro+Tip+-+Orng.png?expires=1784430000&signature=c3c5318fa920540488aae523fb8ced7b21487ed80103643f0c91e8c2e42a5cb0&req=dSQvEMt3lIdfX%2FMW3Hu4gZnI%2BlmVK780zWYq7Qr3%2BMAk%2Bufc3%2Brt3%2F7FalBh%0Apw%3D%3D%0A) We suggest renaming the headers in the file to include the application position that the applications refer to. In our continuous example for Method 2b, columns 4-11 may be named App 1 Term, App 1 Major, App 1 Student Type, etc.. Columns 11-18 may be named App 2 Term, App 2 Major, App 2 Student Type, etc.. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right term for the chunk of columns.

## Mapping

The following fields should be mapped when importing historic applications:

## Standard Mapping:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address

## Calculated Field Mapping:

The following application fields will be Calculated Fields. This means you will scroll to the bottom of you import and select "Add a Mapping" > select "Calculated" > then search for the fields below. Depending on how many unique terms are mentioned in your file will determine how many of each calculated field you have to add. Does your field contain applications for Fall 2025, Spring 2026, and Summer 2026? That means you will be creating 3 calculated fields for user-applications-term-\*, 3 calculated fields for user-applications-major-\*, etc..

* **Application Fields:** Try to add as many of the application fields as calculated fields listed below as possible, with emphasis on term, major, student type. Think about how you will segment these records, for example, if you are going to want to search for submitted applications from Fall 2024, know that you will want to populate data in the submitted time and status fields.

  + user-applications-term-\*
  + user-applications-major-\*
  + user-applications-student-type-\*
  + user-applications-degree-\*
  + user-applications-campus-\*
  + user-applications-concentration-\*
  + user-applications-school-\*
  + user-applications-housing-\*
  + user-applications-registered-at-\*

    - This is equivalent to application start date
  + user-applications-completed-at-\*
  + user-applications-submitted-time-\*
  + user-applications-status-\*

    - Data in this field can be "started", "completed", or "submitted" and is NOT related to the decision.
  + user-applications-submission-convicted-\*
  + user-applications-submission-convicted-explanation-\*
  + user-applications-submission-school-problems-\*
  + user-applications-submission-school-problems-explanation-\*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427054018/f5300499e195ad58f9eae3467a77/Screenshot+2025-03-17+at+2_07_58%E2%80%AFPM.png?expires=1784333700&signature=eafff798ace852f0f5a12bf168548a439e8c33077ff23b8807e990e75df7ec69&req=dSQlEcl7mYFeUfMW1HO4zRtTH6axSjzfwaA28MNtunDhj8b3CbyyOCv9Edv7%0A%2F70G396G1cow641a08Q%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1427054018/f5300499e195ad58f9eae3467a77/Screenshot+2025-03-17+at+2_07_58%E2%80%AFPM.png?expires=1784333700&signature=eafff798ace852f0f5a12bf168548a439e8c33077ff23b8807e990e75df7ec69&req=dSQlEcl7mYFeUfMW1HO4zRtTH6axSjzfwaA28MNtunDhj8b3CbyyOCv9Edv7%0A%2F70G396G1cow641a08Q%3D%0A)

## Scoping and Formulas for Calculated Fields

When adding Calculated Fields, you will be prompted to immediately select your scoping settings and add a formula. You will select an application type, typically the Historic Application, and a term. Using our example above, you would select Fall 2025, Spring 2026, or Summer 2026. The order you build these doesn't matter as long as by the end you have three user-applications-term-\* calculated fields that are scoped to one of the three terms in the file, three user-applications-major-\* calculated fields that are scoped to one of the three terms in the file, and so forth.

Now for the formulas! Each formula is going to contain a series of IF statements. With the file having various terms in each column, we'll be using IF statements to determine what columns are associated to what term for any given student. To set the scene of our example, columns 4-11 represents the students first application, could be for any term, columns 12-19 would be their second application for a different term, columns 20-27 would be their third application for a different term.

## Application Term Formulas

Let's start with formula for the user-applications-term-\* fields. In this example, we assume the terms in the file are Fall 2025, Spring 2026, and Summer 2026 and that the term columns in the file are columns 4, 12, and 20. There will be three term calculations. For user-applications-term-\* that is scoped to Fall 2025, the formula would look like:

```
IF([C4]="Fall 2025",DB_MAP("term",[C4],"name","guid",""),  
IF([C12]="Fall 2025",DB_MAP("term",[C4],"name","guid",""),  
IF([C20]="Fall 2025",DB_MAP("term",[C4],"name","guid",""),"")))
```

The formula first tries column 4 and looks to see if the term is Fall 2025, if so, we populate the term into the user-applications-term-\* field that is scoped to a Fall 2025 application, if column 4 is not Fall 2025, it then will try column 12 and then column 20. If none of the columns have Fall 2025, indicating a student doesn't have a Fall 2025 application, one will not get created.

Repeating these steps, the next formula for user-applications-term-\* that is scoped to Spring 2026 would look like:

```
IF([C4]="Spring 2026",DB_MAP("term",[C4],"name","guid",""),  
IF([C12]="Spring 2026",DB_MAP("term",[C12],"name","guid",""),  
IF([C20]="Spring 2026",DB_MAP("term",[C20],"name","guid",""),"")))
```

And you would repeat these steps for the last user-applications-term-\* scopes to Summer 2026. In the end, you will have three user-applications-term-\* calculated fields.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1463172942/8537f06e57c70d0c873c929eb713/Screenshot+2025-04-07+at+10_45_19%E2%80%AFAM.png?expires=1784333700&signature=3ee5191830923a354a210ba2952b10b4d81ef19d94c5d84d6c6f3563500e3fac&req=dSQhFch5n4hbW%2FMW1HO4zRp9GwA%2B0RYAWWPb5zaZoQRARUwY3a4M%2B1vQXDcH%0Anlt3K956H6gTLFSV9jI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1463172942/8537f06e57c70d0c873c929eb713/Screenshot+2025-04-07+at+10_45_19%E2%80%AFAM.png?expires=1784333700&signature=3ee5191830923a354a210ba2952b10b4d81ef19d94c5d84d6c6f3563500e3fac&req=dSQhFch5n4hbW%2FMW1HO4zRp9GwA%2B0RYAWWPb5zaZoQRARUwY3a4M%2B1vQXDcH%0Anlt3K956H6gTLFSV9jI%3D%0A)

## Application Major Formulas

Next are the formulas for the user-applications-major-\* fields. Using the same example from the term section, we assume the terms in the file are Fall 2025, Spring 2026, and Summer 2026 and that the term columns in the file are columns 4, 12, and 20 and the major columns are columns 5, 13, and 21. There will be three major calculations. For user-applications-major-\* that is scoped to Fall 2025, the formula would look like:

```
IF([C4]="Fall 2025",DB_MAP("major",[C5],"name","guid",""),  
IF([C12]="Fall 2025",DB_MAP("major",[C13],"name","guid",""),  
IF([C20]="Fall 2025",DB_MAP("term",[C21],"name","guid",""),"")))
```

The formula first tries column 4 and looks to see if the term is Fall 2025, if so, we populate the major column into the user-applications-major-\* field that is scoped to a Fall 2025 application, if column 4 is not Fall 2025, it then will try column 12 and then column 20. If none of the columns have Fall 2025, indicating a student doesn't have a Fall 2025 application, one will not get created.

Repeating these steps, the next formula for user-applications-major-\* that is scoped to Spring 2026 would look like:

```
IF([C4]="Spring 2026",DB_MAP("major",[C5],"name","guid",""),  
IF([C12]="Spring 2026",DB_MAP("major",[C13],"name","guid",""),  
IF([C20]="Spring 2026",DB_MAP("major",[C21],"name","guid",""),"")))
```

And you would repeat these steps for the last user-applications-major-\* scopes to Summer 2026. In the end, you will have three user-applications-major-\*.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1463178035/71fe0b841393e29e3bf7372a1373/Screenshot+2025-04-07+at+10_47_50%E2%80%AFAM.png?expires=1784333700&signature=c71bb191379b21ef029bc6feec6601ff953299c67f480120e938825663179be7&req=dSQhFch5lYFcXPMW1HO4zdUA%2BZ351WsgoGUPLe0Ej0s%2BxVNItl9IPo38RkJx%0A6vA3USo7yFtw%2Bd94Apg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1463178035/71fe0b841393e29e3bf7372a1373/Screenshot+2025-04-07+at+10_47_50%E2%80%AFAM.png?expires=1784333700&signature=c71bb191379b21ef029bc6feec6601ff953299c67f480120e938825663179be7&req=dSQhFch5lYFcXPMW1HO4zdUA%2BZ351WsgoGUPLe0Ej0s%2BxVNItl9IPo38RkJx%0A6vA3USo7yFtw%2Bd94Apg%3D%0A)

## Application Student Type Formulas

Using the same example from the term section, we assume the terms in the file are Fall 2025, Spring 2026, and Summer 2026 and that the term columns in the file are columns 4, 12, and 20 and the student type columns are columns 6, 14, and 22. There will be three student type calculations. For user-applications-student-type-\* that is scoped to Fall 2025, the formula would look like:

```
IF([C4]="Fall 2025",DS_MAP([C6],"example.data_source.1234,"column-1","column_2",""),  
IF([C12]="Fall 2025",DS_MAP([C14],"example.data_source.1234,"column-1","column_2",""),  
IF([C20]="Fall 2025",DS_MAP([C22],"example.data_source.1234,"column-1","column_2",""),"")))
```

The formula first tries column 4 and looks to see if the term is Fall 2025, if so, we populate the major column into the user-applications-major-\* field that is scoped to a Fall 2025 application, if column 4 is not Fall 2025, it then will try column 12 and then column 20. If none of the columns have Fall 2025, indicating a student doesn't have a Fall 2025 application, one will not get created.

Repeating these steps, the next formula for user-applications-student-type-\* that is scoped to Spring 2026 would look like:

```
IF([C4]="Spring 2026",DS_MAP([C6],"example.data_source.1234,"column-1","column_2",""),  
IF([C12]="Spring 2026",DS_MAP([C14],"example.data_source.1234,"column-1","column_2",""),  
IF([C20]="Spring 2026",DS_MAP([C22],"example.data_source.1234,"column-1","column_2",""),"")))
```

And you would repeat these steps for the last user-applications-student-type-\* scopes to Summer 2026. In the end, you will have three user-applications-student-type-\*.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1463189480/f5d3ec20e8febc13977c6d02690c/Screenshot+2025-04-07+at+10_53_09%E2%80%AFAM.png?expires=1784333700&signature=36fe95861394fb971d57acce7ede524470b675086eaa1f11db25f226a51e2928&req=dSQhFch2lIVXWfMW1HO4zVbahfRJKZS%2F8iCfUQbiuwKjwhNsUM1lQ6HVJrpP%0AXjbXyZ23QnNpNuKUf7E%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1463189480/f5d3ec20e8febc13977c6d02690c/Screenshot+2025-04-07+at+10_53_09%E2%80%AFAM.png?expires=1784333700&signature=36fe95861394fb971d57acce7ede524470b675086eaa1f11db25f226a51e2928&req=dSQhFch2lIVXWfMW1HO4zVbahfRJKZS%2F8iCfUQbiuwKjwhNsUM1lQ6HVJrpP%0AXjbXyZ23QnNpNuKUf7E%3D%0A)

##

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486305366/59d71e18be23298ca39aad16ed34/Pro+Tip+-+Orng.png?expires=1784430000&signature=539d1aca7dd294988e07f433faa043c313c8e4fc1162c232abcf42724e2475b6&req=dSQvEMp%2BmIJZX%2FMW3Hu4gePpw8acGwSwVkd8YWbwg6CRW4NXOt7WVndeZDgB%0ANQ%3D%3D%0A)![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481773211/3aac945129121b1dedb050b14dc3/Pro+Tip+-+Orng.png?expires=1784430000&signature=1f5216c7f520ff2b4e0faf96e0bba7fdc76ed98b9458e8209e7da0929ea42eea&req=dSQvF855noNeWPMW3Hu4gQPB%2F7hveCrq0Ap9LUnl468Fqh7GUo37%2FitwjDq5%0AOw%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

---