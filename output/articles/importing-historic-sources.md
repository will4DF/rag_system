---
title: Importing Historic Sources
url: https://help.element451.com/en/articles/11048688-importing-historic-sources
collection: Data Management
---

Learn how to import sources in bulk from another system as part of your historic imports.

This article will walk you through how to import multiple CUSTOM or SEARCH sources at once onto a record's profile, when the records do not have any previous sources listed on their Element451 profile. Be sure you are familiar with sources and source segments by reviewing our help article on [Sources](https://help.element451.com/en/articles/2066892-sources), which also explains how to import sources if you are importing a source and records may have information already on the source section.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486373383/4700d00f511cb108869492ee3512/Note.png?expires=1784430000&signature=18a84eedf009d05d7d9d5ec471e5369be1a57cb646da64c8a7f61f0c5b40d78b&req=dSQvEMp5noJXWvMW3Hu4gap3mrRUHdqa7taRjEm3bd4%2ByyBQ%2FNfmvbNgdXH2%0A0g%3D%3D%0A) CUSTOM, and SEARCH sources are the only source types you can import into. All other source types are system automatically created as records interact with other parts of your Element451 instance. WEB can be imported and automatically generated. Refer to the [Sources](https://help.element451.com/en/articles/2066892-sources) article for more information.

## Creating Source Files

As a reminder, the files need to be either .csv or .txt, contain a unique identifier (or a few!). There are a few ways we recommend making files of source data.

1. **Generate separate files per source.** Each file would represent the position of the source on the record. For example, a file would be records' first source, another file would records' second source, etc..
2. **Format source data into column sets.** In this scenario, columns 4-7 would belong to the record's first source, then columns 8-11 would belong to the record's second source, etc..
3. **Repeat file on sources.** In this scenario, a record may be present several times in the file. For this method, you must have a column for row number over student ID that represents if the source is the record's first, second, third, etc. source.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486374215/972d31ba9027a76bfff417081638/Pro+Tip+-+Orng.png?expires=1784430000&signature=0b9045f52345216a9f4c574c1db4022dda5aac5a330d68c6ff92cdf1c1116233&req=dSQvEMp5mYNeXPMW3Hu4gTGF71ZJrRzoFakANZPNev%2BWLoozZSqzXOZqZMj0%0AEg%3D%3D%0A) If you need to create a row number on an ID using a spreadsheet tool, you can use a formula similar to =COUNTIF($B$2:B3,B3) where B, in this example, is a unique identifier.

## Fields to Include in the Files

Listed are fields you can include on your source files. The bolded fields are strongly recommended.

* **Contact Identifiers (Student ID, Historic ID, and/or Email)**
* **Source Type**

  + This can be CUSTOM or SEARCH
* **Source Name**

  + We use source name, code, and alias interchangeably
* Source Segment (optional)

  + Refer to the [sources article](https://help.element451.com/en/articles/2066892-sources#h_225768856a) for more information on Source Segments
* **Source Date**

## Importing Sources using Method 1

With separate files for each source, you will be creating import tasks for each file that are identical in column layout, but different scoping set up inside the source fields. There is a Historic Source Import template in your instance, but you are not required to follow that exact layout if you need additional unique identifiers or need to put the fields in a different order, the template is a starting point if you need direction.

## Mapping

The following fields should be mapped when importing sources:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Source Fields:** Try to map as many of the source fields listed below as possible, with emphasis on name and date.

  + user-sources-type-\*

    - This is to define if it is CUSTOM or SEARCH
  + user-sources-alias-\*

    - We use source name, alias, and code interchangeably
    - The incoming data needs to line up with the [sources in your Element451 instance.](https://help.element451.com/en/articles/2066892-sources#h_2888a7ba32)
  + user-sources-segment-\*
  + user-sources-timestamp-\*

## Scoping

Notice that the source fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. For sources, the scoping setting is position.

When selecting the settings, you are telling the system that you are importing a source into a specific order on the profile, if a source does not exist in the position, create a new one, if one does exist, update it. Without the star mappings, the system updates whatever source is on the record's profile, potentially wiping a historic source.

For importing source using Method 1, for each field on your import, you will set the scoping settings to whatever position you want them to feed into. Since Method 1 instructs you to have separate files for each position, each import will have the same column headers but the scoping settings will reflect the position you are importing. For your first position file, the scoping settings will be "1" for all star mappings. For your second position file, the scoping settings will be "2" for all star mappings.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486377936/98111bad4f4a74d8eefa06329bae/Screenshot+2025-04-21+at+11_09_04%E2%80%AFAM.png?expires=1784333700&signature=7831028233f292b6acf0882c5df687c2cec2278653cf5bb4fa4e9244ae9c61a0&req=dSQvEMp5mohcX%2FMW1HO4zaFwfOjAhUFYfJDv6cZymleyDIkJG5I%2B8JvvkjnU%0AzoAMcF2dqPJOyrtJfek%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486377936/98111bad4f4a74d8eefa06329bae/Screenshot+2025-04-21+at+11_09_04%E2%80%AFAM.png?expires=1784333700&signature=7831028233f292b6acf0882c5df687c2cec2278653cf5bb4fa4e9244ae9c61a0&req=dSQvEMp5mohcX%2FMW1HO4zaFwfOjAhUFYfJDv6cZymleyDIkJG5I%2B8JvvkjnU%0AzoAMcF2dqPJOyrtJfek%3D%0A)

## Importing Sources using Method 2

If your file follows Method 2, where you have one file with column sets that are associated with source positions, follow the instructions for mapping below.

## Mapping

The following fields should be mapped when importing historic applications:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Source Fields:** Try to map as many of the source fields listed below as possible, with emphasis on name and date. For each column set, you will want to map the same user-sources-...-\* fields, so you may end up with several columns mapped to user-sources-type-\*, user-sources-alias-\*, etc..

  + user-sources-type-\*

    - This is to define if it is CUSTOM or SEARCH
  + user-sources-alias-\*

    - We use source name, alias, and code interchangeably
  + user-sources-segment-\*
  + user-sources-timestamp-\*

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486378274/dcb4268f7f6e229aa9b71d990640/Pro+Tip+-+Orng.png?expires=1784430000&signature=ff483e328b8e75664daf117609e06fa60adb10a73ca6f1a3ab7b846b14444d8e&req=dSQvEMp5lYNYXfMW3Hu4gdNzYrp%2BdeOTLvoeFhOi7V76cAnqqWzgPHoyCjkn%0AKg%3D%3D%0A) We suggest renaming the headers in the file to include the position that the sources refer to. In our continues example for Method 2, columns 4-7 may be named Source 1 Type, Source 1 Alias, Source 1 Segment, Source 1 Date. Columns 11-18 may be named Source 2 Type, Source 2 Alias, Source 2 Segment, Source 2 Date. This step is mainly to keep your head straight when setting up the scoping settings and ensuring you are selecting the right term for the chunk of columns.

## Scoping

Notice that the source fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten and also target data that may need to be cleaned up. Any field that is a star mapping, will require scoping settings. For sources, the scoping setting is position.

When selecting the settings, you are telling the system that you are importing a source into a specific order on the profile, if a source does not exist in the position, create a new one, if one does exist, update it. Without the star mappings, the system updates whatever source is on the record's profile, potentially wiping a historic source.

For importing source using Method 2, for each field on your import, you will set the scoping settings to whatever position you want them to feed into. Since Method 2 will have a chunk of columns dedicated to one position, another chunk dedicated to the second position and so forth, for scoping, you will select the position that the chunk of columns represent. For columns 4-7, the scoping settings will be "1" for all star mappings. For columns 8-11, the scoping settings will be "2" for all star mappings.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486378915/c79b2cf4f7d6c850c0462962df99/Screenshot+2025-04-21+at+11_09_04%E2%80%AFAM.png?expires=1784333700&signature=eaf61ea8d382821784a03810cc3a67905431a065cf0ce68e1e4764476b56f26e&req=dSQvEMp5lYheXPMW1HO4zfQMc7NNVTWLzCtWovgKpXHVNINYMqJMsyP6wTbK%0AWFfZAOuEaIu%2FUl%2FncpQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486378915/c79b2cf4f7d6c850c0462962df99/Screenshot+2025-04-21+at+11_09_04%E2%80%AFAM.png?expires=1784333700&signature=eaf61ea8d382821784a03810cc3a67905431a065cf0ce68e1e4764476b56f26e&req=dSQvEMp5lYheXPMW1HO4zfQMc7NNVTWLzCtWovgKpXHVNINYMqJMsyP6wTbK%0AWFfZAOuEaIu%2FUl%2FncpQ%3D%0A)

## Importing Sources using Method 3

If your file follows Method 3, where you have one file that repeats on sources and includes a row number of an identity, follow the instructions for mapping below. For this method, you must be familiar with our formula builder. Our list of functions can be found [here](https://integrations.element451.com/calculated-fields-37).

## Mapping

The following fields should be mapped when importing historic sources:

## Standard Mapping:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address

## Calculated Field Mapping:

The following source fields will be Calculated Fields. This means you will scroll to the bottom of your import and select "Add a Mapping" > select "Calculated" > then search for the fields below. Depending on how many sources one records has, will determine how many of each calculated field you have to add. Is the max row number over identities five, meaning a record has five sources? That means you will be creating five calculated fields for user-sources-type-\*, five calculated fields for user-sources-alias-\*, etc..

* **Source Fields:** Try to map as many of the source fields listed below as possible, with emphasis on name and date.

  + user-sources-type-\*

    - This is to define if it is CUSTOM or SEARCH
  + user-sources-alias-\*

    - We use source name, alias, and code interchangeably
  + user-sources-segment-\*
  + user-sources-timestamp-\*

## Scoping and Formulas for Calculated Fields

When adding Calculated Fields, you will be prompted to immediately select your scoping settings and add a formula. On each field you will select a position. The order you build these doesn't matter as long as by the end you have the max row number of user-sources-type-\* calculated fields that are scoped to one of the positions, the max row number of user-sources-alias-\* calculated fields that are scoped to one of the positions, and so forth. For our example from the Mapping section, that would mean five of each field.

Now for the formulas! Each formula is going to contain an IF statement. With the file having several sources in different rows, we'll be using IF statements to make sure we are putting the first source in the first position, the second source in the second position, and so forth.. To set the scene of our example, column 4 is our source type, column 5 is the source alias, 6 is the segment, 7 is the date, and 8 is the row number over the identities. The max amount of sources a record has is three.

## Source Type Formula

You'll be building three different formulas for three user-sources-type-\* fields. They'll be very similar, just with different conditions for each position. Below is what the user-sources-type-\* field scoped to position "1" would look like:

```
IF([C8]="1",[C4],"")
```

The formula checks to see if the row number is 1, if it is, it grabs the source type column. If it is not, it does nothing.

Below is the formula for user-sources-type-\* field scoped to position "2":

```
IF([C8]="2",[C4],"")
```

Basically, you are swapping out the position on the scope and formula.

## Source Alias and Segment Formula

You'll be building three different formulas for three user-sources-alias-\* fields. They'll be very similar, just with different conditions for each position. Below is what the user-sources-alias-\* field scoped to position "1":

```
IF([C8]="1",TAXONOMY_MAP([C5],"name","guid",""),"")
```

The formula checks to see if the row number is 1, if it is, it grabs the source alias column and uses the sources list in your Element451 instance to find the guid code using name as the mapping. You can swap "name" with "code" if you are sending codes instead. If the row number is not 1, it does nothing.

Below is the formula for user-sources-type-\* field scoped to position "2":

```
IF([C8]="2",TAXONOMY_MAP([C5],"name","guid",""),"")
```

Basically, you are swapping out the position on the scope and formula.

For Source Segments, the formulas will be the exact same format, because we store sources and source segments in the same spot. Rather than pull the source alias column, you would pull your source segment column:

```
IF([C8]="1",TAXONOMY_MAP([C6],"name","guid",""),"")
```

## Source Date Formula

You'll be building three different formulas for three user-sources-timestamp-\* fields. They'll be very similar, just with different conditions for each position. Below is what the user-sources-timestamp-\* field scoped to position "1":

```
IF([C8]="1",DATE_READ([C7],"m/d/Y"),"")
```

The formula checks to see if the row number is 1, if it is, it grabs date column. If the row number isn't 1, it will do nothing.

Below is the formula for user-sources-type-\* field scoped to position "2":

```
IF([C8]="2",DATE_READ([C7],"m/d/Y"),"")
```

Basically, you are swapping out the position on the scope and formula.

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486380149/e2561f3b9483fb1922ab9b618db7/Pro+Tip+-+Orng.png?expires=1784430000&signature=82c0e7c038c6d0740723f5d1f4a37998f8a1b71e5a3d2780cc65f1da0dca9f34&req=dSQvEMp2nYBbUPMW3Hu4gSCsy6O46yJocpscfW6Shsh%2F4g8N5J7qORofeyRf%0AKQ%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

---