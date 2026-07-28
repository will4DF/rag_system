---
title: Importing Historic Test Scores
url: https://help.element451.com/en/articles/11088661-importing-historic-test-scores
collection: Data Management
---

Learn how to import test scores onto a contact record in bulk.

This article will provide you a starting guide on how to import historic test scores onto a contact record. If you are building imports for test scores that come straight from the test provider, please refer to our [Integrations Guide](https://integrations.element451.com/flat-file-integrations-12) where we have links to guide you through importing SAT and ACT scores that come directly from the provider.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486360397/36434451ce835d38ed74b64b320a/Screenshot+2025-04-21+at+10_58_13%E2%80%AFAM.png?expires=1784333700&signature=0bcae3c2c4557373fc031cae8ed5256e95500375c9f2f9f5606a4057321deca2&req=dSQvEMp4nYJWXvMW1HO4zbBCE7AyaECneOrV978WslZOW1vGrNWlpDZTXhVy%0AgJHd7chz%2FeKcOjRAWbM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486360397/36434451ce835d38ed74b64b320a/Screenshot+2025-04-21+at+10_58_13%E2%80%AFAM.png?expires=1784333700&signature=0bcae3c2c4557373fc031cae8ed5256e95500375c9f2f9f5606a4057321deca2&req=dSQvEMp4nYJWXvMW1HO4zbBCE7AyaECneOrV978WslZOW1vGrNWlpDZTXhVy%0AgJHd7chz%2FeKcOjRAWbM%3D%0A)

## Creating Test Score Files

As a reminder, the files need to be either .csv or .txt, contain a unique identifier (or a few!). There are a few ways we recommend making files of test score data.

1. **Generate separate files per test.** Each file would represent the position of the school on the record. For example, a file would be records' first SAT test, another file would records' second SAT test, then first ACT test, second ACT test, etc..
2. **Format test data into column sets.** In this scenario, columns 4-7 would belong to the record's first SAT test, then columns 8-11 would belong to the record's second SAT test, etc.. Further into the columns, there would be chunks of columns for the record's first ACT test, second ACT test, etc..
3. **Repeat file on tests.** In this scenario, a record may be present several times in the file. For this method, you must have a column for row number over student ID and test type that represents if the test is the record's first SAT, second SAT, third SAT, first ACT, second ACT, etc..

## Fields to Include on the Files

Listed are fields you can include on your school files. The bolded fields are strongly recommended.

* **Contact Identifiers (Student ID, Historic ID, and/or Email)**
* **Test Type**
* **Test Date**
* **Test Composite/Overall Score**
* Test Sub-scores
* **Is the Test Official?**

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486360834/141fb63c11dda13963bdc209b8ab/Note.png?expires=1784430000&signature=a91ecacbea48cc125db8c02bfa9bafefbb2fbbc3d76a88a1b356f0576e773d51&req=dSQvEMp4nYlcXfMW3Hu4gUDleKBfxo1CudiLW5KDWE%2FFoWj8tUPdzQ7HQIj9%0A1Q%3D%3D%0A) Test scores have different sub-scores, so you may have empty columns on some rows if tests don't have a subtest, or may have to make separate file layouts for each test type.

## Importing Tests using Method 1

With separate files for each test, you will be creating import tasks for each file that are similar in column layout, but different scoping set up inside the source fields.

## Mapping

The following fields should be mapped when importing historic applications:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Test Data:** Try to map as many of the test score fields as possible with emphasis on the date, composite score, and if it is official. Listed below are **some** of the common test score fields we see, please note, not all fields are applicable to all test types. (SAT doesn't have a Science test)

  + user-evaluations-date-\*
  + user-evaluations-official-\*
  + user-evaluations-writing-score-\*
  + user-evaluations-science-score-\*
  + user-evaluations-reading-score-\*
  + user-evaluations-math-score-\*
  + user-evaluations-composite-score-\*

There are many more options for test score fields, when adding a mapping, you can search user-evaluations- to see a full list of the fields.

## Scoping

Notice that the test fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. For tests, the scoping settings are test type and position.

When selecting the settings, you are telling the system that you are importing a test with these qualities, if a test does not exist with those qualities, create a new one, if one does exist, update it. Without the star mappings, the system updates whatever test is on the record's profile, potentially wiping a historic test score.

For importing tests using Method 1, for each field on your import, you will set the scoping settings to whatever test type you want them to feed into. Since Method 1 instructs you to have separate files for each school listed, each import will have the same column headers but the scoping settings will reflect the position you are importing. For example, you would have a file for the record's first SAT, another file for the record's second SAT, and so forth, then one for the first ACT, another for the second ACT, and so forth.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486368828/c0908a65bdb6c0ce283c23b3e880/Screenshot+2025-04-21+at+11_03_09%E2%80%AFAM.png?expires=1784333700&signature=4593723d4aad1c5715b54c4f7328f007f09da64cd78f792749b82fcdaf8a64f1&req=dSQvEMp4lYldUfMW1HO4zSd2mvrTYQ0owiNGN5b9KGqy8e2aOMm7NyOTEz9V%0A0dT7gA02qyMV5r2D%2FmA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486368828/c0908a65bdb6c0ce283c23b3e880/Screenshot+2025-04-21+at+11_03_09%E2%80%AFAM.png?expires=1784333700&signature=4593723d4aad1c5715b54c4f7328f007f09da64cd78f792749b82fcdaf8a64f1&req=dSQvEMp4lYldUfMW1HO4zSd2mvrTYQ0owiNGN5b9KGqy8e2aOMm7NyOTEz9V%0A0dT7gA02qyMV5r2D%2FmA%3D%0A)

## Importing Tests using Method 2

If your file follows Method 2, where you have one file with column sets that are associated with test types and positions, follow the instructions for mapping below.

## Mapping

The following fields should be mapped when importing test scores:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Test Data:** Try to map as many of the test score fields as possible with emphasis on the date, composite score, and if it is official. Listed below are **some** of the common test score fields we see, please note, not all fields are applicable to all test types. (For example, SAT doesn't have a Science test). For each column set, you will want to map the same user-evaluations-...-\* fields, so you may end up with several columns mapped to user-evaluations-date-\*, user-evaluations-official-\*, etc..

  + user-evaluations-date-\*
  + user-evaluations-official-\*
  + user-evaluations-writing-score-\*
  + user-evaluations-science-score-\*
  + user-evaluations-reading-score-\*
  + user-evaluations-math-score-\*
  + user-evaluations-composite-score-\*

There are many more options for test score fields, when adding a mapping, you can search user-evaluations- to see a full list of the fields.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486363844/30d76b9d56832f3feb4cc06b31e9/Pro+Tip+-+Orng.png?expires=1784430000&signature=aa3e71bec20b71a4875962030ee75090aef7ef1a4d2ab91ceae2dad7a224d1ba&req=dSQvEMp4nolbXfMW3Hu4gRMIMTOPBCpa3ZocuXw9l%2B51xbU02xko1xxmbHSP%0A6Q%3D%3D%0A) We suggest renaming the headers in the file to include the position that the sources refer to. In our continues example for Method 2, columns 4-7 may be named Source 1 Type, Source 1 Alias, Source 1 Segment, Source 1 Date. Columns 11-18 may be named Source 2 Type, Source 2 Alias, Source 2 Segment, Source 2 Date. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right term for the chunk of columns.

## Scoping

Notice that the test fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. For tests, the scoping settings are test type and position.

When selecting the settings, you are telling the system that you are importing a test with these qualities, if a test does not exist with those qualities, create a new one, if one does exist, update it. Without the star mappings, the system updates whatever test is on the record's profile, potentially wiping a historic test score.

For importing tests using Method 2, for each field on your import, you will set the scoping settings to whatever test type and position you want them to feed into. Since Method 2 instructs you to have a chunk of columns dedicated to one test of a specific type, each import will have the similar column headers but the scoping settings will reflect the type and position you are importing. Columns 4-7 could belong to the record's first SAT test, then columns 8-11 could belong to the record's second SAT test, etc.. Further into the columns, there could be chunks of columns for the record's first ACT test, second ACT test, etc..

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486369624/12d101228d414ff09d0480fa4a0c/Screenshot+2025-04-21+at+11_03_09%E2%80%AFAM.png?expires=1784333700&signature=42c2d3e29631259e0791346d05570d516a3bdbbe645da6de63dfaa8c82b34c1e&req=dSQvEMp4lIddXfMW1HO4zQlc170ETRsqsH5ypmzpDqltD4DaPQudbBhAgL3d%0AcLGQCY2iVGLkVjs%2FFDA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486369624/12d101228d414ff09d0480fa4a0c/Screenshot+2025-04-21+at+11_03_09%E2%80%AFAM.png?expires=1784333700&signature=42c2d3e29631259e0791346d05570d516a3bdbbe645da6de63dfaa8c82b34c1e&req=dSQvEMp4lIddXfMW1HO4zQlc170ETRsqsH5ypmzpDqltD4DaPQudbBhAgL3d%0AcLGQCY2iVGLkVjs%2FFDA%3D%0A)

## Importing Tests using Method 3

If your file follows Method 3, where you have one file that repeats on tests and includes a row number of an identity and test type, follow the instructions for mapping below. For this method, you must be familiar with our formula builder. Our list of functions can be found [here](https://integrations.element451.com/calculated-fields-37).

## Mapping

The following fields should be mapped when importing test scores:

## Standard Mapping

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address

## Calculated Field Mapping

The following source fields will be Calculated Fields. This means you will scroll to the bottom of your import and select "Add a Mapping" > select "Calculated" > then search for the fields below. Depending on how many tests one record has, will determine how many of each calculated field you have to add. Is the max number of SAT tests a student has two and max number of ACT tests three? That means you will be creating five calculated fields for user-evaluations-date-\*, five calculated fields for user-evaluations-date-\*, etc..

* **Test Data:** Try to map as many of the test score fields as possible with emphasis on the date, composite score, and if it is official. Listed below are **some** of the common test score fields we see, please note, not all fields are applicable to all test types. (SAT doesn't have a Science test)

  + user-evaluations-date-\*
  + user-evaluations-official-\*
  + user-evaluations-writing-score-\*
  + user-evaluations-science-score-\*
  + user-evaluations-reading-score-\*
  + user-evaluations-math-score-\*
  + user-evaluations-composite-score-\*

There are many more options for test score fields, when adding a mapping, you can search user-evaluations- to see a full list of the fields.

## Scoping and Formulas for Calculated Fields

When adding Calculated Fields, you will be prompted to immediately select your scoping settings and add a formula. On each field you will select a test type and position. The order you build these doesn't matter as long as by the end you have enough of each field that cover the max number of tests a record has.

Now for the formulas! Each formula is going to contain an IF statement. With the file having several tests in different rows, we'll be using IF statements to make sure we are putting the correct test type and position into the system. To set the scene of our example, column 4 is our test type, column 5 is the test date, 6 is the composite score, and 7 is the row number over the identities. The max amount of tests a record has is one TOEFL test and two SAT tests, so three tests.

Note: For our examples, we won't be mapping column 4, test type, but we will use it in each formula to make sure we create the correct test object.

## Test Date Formulas

For the scenario, you'll be building three formulas for user-evaluations-date-\* fields. They'll be very similar, just different conditions to determine what test and position it is. Below is what the user-evaluations-date-\* scoped to TOEFL and position 1 would look like:

```
IF([C4]="TOEFL" & [C7]="1",DATE_READ([C5],"m/d/Y"),"")
```

The formula checks if the test type is TOEFL and the row number is 1, if it is, it will pull in the test date in, if not, it doesn't import anything.

Below is the formula for user-evaluations-date-\* scoped to SAT and position 1:

```
IF([C4]="SAT" & [C7]="1",DATE_READ([C5],"m/d/Y"),"")
```

Then lastly, the user-evaluations-date-\* scoped to SAT and position 2:

```
IF([C4]="SAT" & [C7]="2",DATE_READ([C5],"m/d/Y"),"")
```

## Composite Formulas

For the scenario, you'll be building three formulas for user-evaluations-composite-\* fields. They'll be very similar, just different conditions to determine what test and position it is. Below is what the user-evaluations-composite-\* scoped to TOEFL and position 1 would look like:

```
IF([C4]="TOEFL" & [C7]="1",[C6],"")
```

The formula checks if the test type is TOEFL and the row number is 1, if it is, it will pull in the composite score in, if not, it doesn't import anything.

Below is the formula for user-evaluations-composite-\* scoped to SAT and position 1:

```
IF([C4]="SAT" & [C7]="1",[C6],"")
```

Then lastly, the user-evaluations-composite-\* scoped to SAT and position 2:

```
IF([C4]="SAT" & [C7]="2",[C6],"")
```

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486365321/7b44e3cee5c51553ba5107054c85/Pro+Tip+-+Orng.png?expires=1784430000&signature=60e507c8ddc815e3f033bcd0e9bb69c843ae30d568db290f8b58b4c262fdd9c0&req=dSQvEMp4mIJdWPMW3Hu4gQ%2FjpUfOFzqnqi8NFpQ5%2FVpTrFi8EL0PL6S%2FNv2D%0Ahw%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

---