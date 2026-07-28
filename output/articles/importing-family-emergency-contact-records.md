---
title: Importing Family/Emergency Contact Records
url: https://help.element451.com/en/articles/10826356-importing-family-emergency-contact-records
collection: Data Management
---

Learn how to import family and/or emergency contact data onto a contact.

This article will provide you a template on how to import family and emergency contact information onto a contact record. For more information on family records and creating relationships, please refer to the [Family Members and Relationships](https://You%20can%20learn%20more%20about%20Family%20Members%20and%20Relationships%20in%20our%20general%20article.) article.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486326898/4f2e2e7307798bc5de36f2bccaf5/Note.png?expires=1784430000&signature=72c13f202c886b138f521ca960d46f4824058d5c4ea6b905509a7f2449c2b6c8&req=dSQvEMp8m4lWUfMW3Hu4gWGSTQwV6SQf2XWvk5Hl6ziZVgeyjVrQbdBq0hww%0ApA%3D%3D%0A) Family and Emergency Contacts are different parts of the profile. We address them in this article together because their imports will be very similar. Be sure you understand how your team is going to use the two parts of the profile when importing these files.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1428561925/0ae1798a4b8341411b54c89d0176/Screenshot+2025-03-18+at+10_43_54%E2%80%AFAM.png?expires=1784333700&signature=08f165dd9cd714e4a5a934469df454c0e512179330d538cbae4aa7be7f24d03d&req=dSQlHsx4nIhdXPMW1HO4zcljk2pCed1XYOZ%2FwJCg%2FiWymgg2VCa94CSw%2Bxyw%0AHGU7UG1hYHT72pAB8Zg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1428561925/0ae1798a4b8341411b54c89d0176/Screenshot+2025-03-18+at+10_43_54%E2%80%AFAM.png?expires=1784333700&signature=08f165dd9cd714e4a5a934469df454c0e512179330d538cbae4aa7be7f24d03d&req=dSQlHsx4nIhdXPMW1HO4zcljk2pCed1XYOZ%2FwJCg%2FiWymgg2VCa94CSw%2Bxyw%0AHGU7UG1hYHT72pAB8Zg%3D%0A)

## Creating a Family or Emergency Contact File

As a reminder, the files need to be either .csv or .txt, contain a unique identifier (or a few!), and only have one row per contact. There are two ways we recommend making files of family and/or emergency contact data.

1. One file with each family member or emergency contact as a column set. For example, the record's first family member's data are in columns 4-16, the record's second family member's data are in columns 17-29, and so forth.

   1. Additionally, you could tack on the emergency contacts as column sets in the same file.
2. Several files where each file represents a single family member or emergency contact.

## Fields to Include in the File

Listed are fields you can include on your family file. The bolded fields are strongly recommended.

* **Contact Identifiers (Student ID, Historic ID, and/or Email)**
* **Family Relationship**
* **Family Name**
* **Family Email**
* Family Address
* Family Phone
* Family Occupation
* Family Degree Earned

## Importing Family and Emergency Contacts using Method 1

If your file follows Method 1, where you have one file with column sets that are associated with parents and emergency contacts, follow the instructions for mapping below.

## Mapping

The following fields should be mapped when importing family members or emergency contacts:

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Family Member Fields:** Below is the standard family member fields we see imported, but there are more you could add that aren't listed. Think about how you will segment these records, for example, if you are going to want to search on family education level, know that you will want to populate data in the education level field.. For each column set, you will want to map the same user-family-...-\* fields, so you may end up with several columns mapped to user-family-first-name-\*, user-family-last-name-\*, etc..

  + user-family-relationship-\*

    - These need to be the code/value of the data source used in the family member relationship in your instance.
  + user-family-first-name-\*
  + user-family-last-name-\*
  + user-family-email-\*
  + user-family-phone-country-code-\*
  + user-family-phone-number-\*
  + user-family-address-street-1-\*
  + user-family-address-street-2-\*
  + user-family-address-city-\*
  + user-family-address-state-\*
  + user-family-address-province-\*
  + user-family-address-country-\*
  + user-family-address-zipcode-\*
* Emergency Contact Fields: Similar to the family member fields, below is what we typically see imported, but there are more fields you could map that aren't listed here.

  + user-emergency-contacts-relationship-type-\*

    - These need to be the code/value of the data source used in the emergency contact relationship in your instance.
  + user-emergency-contacts-first-name-\*
  + user-emergency-contacts-last-name-\*
  + user-emergency-contacts-email-\*
  + user-emergency-contacts-cell-phone-country-code-\*
  + user-emergency-contacts-cell-phone-number-\*
  + user-emergency-contacts-address-street-1-\*
  + user-emergency-contacts-address-street-2-\*
  + user-emergency-contacts-address-city-\*
  + user-emergency-contacts-address-state-\*
  + user-emergency-contacts-address-province-\*
  + user-emergency-contacts-address-country-\*
  + user-emergency-contacts-address-zipcode-\*

## Scoping

Notice that the family member and emergency contact fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten. Any field that is a star mapping, will require scoping settings.

When selecting the settings, you are telling the system that you are importing a family member or emergency contact with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it.

For importing family members and emergency contacts using Method 1, for each field on your import, you will set the scoping settings to whatever position the family member belongs to. Since Method 1 will have a chunk of columns dedicated to one family member, another chunk dedicated to a different family member, and so forth, for scoping, you will select the position that the chunk of columns represent. In our previous example, columns 4-16 will be scoped to the position 1 because they are the first parent and columns 17-29 will be scoped to position 2 because they are the second parent.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1428978855/2faf9a7e491dc67df5405ddac392/Screenshot+2025-03-18+at+2_34_35%E2%80%AFPM.png?expires=1784333700&signature=2fad9545da117c45ef733f1ade210bb3214818f22280b99e7933feb13a98ca54&req=dSQlHsB5lYlaXPMW1HO4zbgAqZw72CXxve1dduTD%2BWbxNvd3Fd2OrbOSzWH%2F%0AUI4hCsNBtRLHNiPvtR4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1428978855/2faf9a7e491dc67df5405ddac392/Screenshot+2025-03-18+at+2_34_35%E2%80%AFPM.png?expires=1784333700&signature=2fad9545da117c45ef733f1ade210bb3214818f22280b99e7933feb13a98ca54&req=dSQlHsB5lYlaXPMW1HO4zbgAqZw72CXxve1dduTD%2BWbxNvd3Fd2OrbOSzWH%2F%0AUI4hCsNBtRLHNiPvtR4%3D%0A)

## Importing Family and Emergency Contacts using Method 2

With separate files for each family member or emergency contact, you will be creating import tasks for each file that are identical in column layout, but different scoping set up inside the family member or emergency contact fields.

## Mapping

The following fields should be mapped when importing family members or emergency contacts. If your file is a family member, map the family member fields, if the file is an emergency contact, map the emergency contact fields.

* **Contact Identifiers**: This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address
* **Family Member Fields:** Below is the standard family member fields we see imported, but there are more you could add that aren't listed. Think about how you will segment these records, for example, if you are going to want to search on family education level, know that you will want to populate data in the education level field..

  + user-family-relationship-\*

    - These need to be the code/value of the data source used in the family member relationship in your instance.
  + user-family-first-name-\*
  + user-family-last-name-\*
  + user-family-email-\*
  + user-family-phone-country-code-\*
  + user-family-phone-number-\*
  + user-family-address-street-1-\*
  + user-family-address-street-2-\*
  + user-family-address-city-\*
  + user-family-address-state-\*
  + user-family-address-province-\*
  + user-family-address-country-\*
  + user-family-address-zipcode-\*
* **Emergency Contact Fields:** Similar to the family member fields, below is what we typically see imported, but there are more fields you could map that aren't listed here.

  + user-emergency-contacts-relationship-type-\*

    - These need to be the code/value of the data source used in the emergency contact relationship in your instance.
  + user-emergency-contacts-first-name-\*
  + user-emergency-contacts-last-name-\*
  + user-emergency-contacts-email-\*
  + user-emergency-contacts-cell-phone-country-code-\*
  + user-emergency-contacts-cell-phone-number-\*
  + user-emergency-contacts-address-street-1-\*
  + user-emergency-contacts-address-street-2-\*
  + user-emergency-contacts-address-city-\*
  + user-emergency-contacts-address-state-\*
  + user-emergency-contacts-address-province-\*
  + user-emergency-contacts-address-country-\*

## Scoping

Notice that the family member and emergency contact fields we recommend you use have asterisks. We call these [Star Mappings](https://help.element451.com/en/articles/9745028-star-mappings) and it is a great tool to use to ensure that data does not get overwritten. Any field that is a star mapping, will require scoping settings.

When selecting the settings, you are telling the system that you are importing a family member or emergency contact with these qualities, if one does not exist already on the record, create a new one, if one does exist that meet the qualities, update it.

For importing family members or emergency contacts using Method 2, for each field on your import, you will set the scoping settings to whatever position the family member belongs to. Since Method 1 instructs you to have separate files for each family member or emergency contact, each import will have the same column headers but the scoping settings will reflect the file you are importing. For your first family member, the scoping settings should be position 1. For your second family member, the scoping settings should be position 2. For your first emergency contact, the scoping settings should be position 1, and so forth.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1429052079/e35b594790aa032b62d28e9982d4/Screenshot%2B2025-03-18%2Bat%2B2_34_35-E2-80-AFPM.png?expires=1784333700&signature=53c72d380a55f17e8ef245ce1628d299a5cac6a4b10068c437d27260b7d40317&req=dSQlH8l7n4FYUPMW1HO4zZImfNEKr%2BCYDaZkH0jBoD9%2BoULoenugGdhubqGp%0AG0ArsXS1XtKFzFPAAR0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1429052079/e35b594790aa032b62d28e9982d4/Screenshot%2B2025-03-18%2Bat%2B2_34_35-E2-80-AFPM.png?expires=1784333700&signature=53c72d380a55f17e8ef245ce1628d299a5cac6a4b10068c437d27260b7d40317&req=dSQlH8l7n4FYUPMW1HO4zZImfNEKr%2BCYDaZkH0jBoD9%2BoULoenugGdhubqGp%0AG0ArsXS1XtKFzFPAAR0%3D%0A)

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486337019/34b6b1199032a14e56c3643caaac/Pro+Tip+-+Orng.png?expires=1784430000&signature=e5aab80c1e935aa9834f39b46932953736b5612779fc20daf6134fc09f34aea8&req=dSQvEMp9moFeUPMW3Hu4gf8yf8M8ollWUYKZKm5xWAaz9viMWqXS0n6fmnSp%0AJQ%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

---