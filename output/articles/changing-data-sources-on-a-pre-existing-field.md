---
title: Changing Data Sources on a Pre-Existing Field
url: https://help.element451.com/en/articles/7321708-changing-data-sources-on-a-pre-existing-field
collection: Data Management
---

Use this guide to properly swap out a data source on a field that has been used across your instance.

# Overview

When you first implemented Element451, you learned all about creating and editing data sources and using them in either the system fields or custom fields you built. As time goes by, some changes may occur where the original data source used on the field is no longer applicable, and a new data source needs to be used.

This article will walk you through the steps to update the field for future use and clean up the old values on student profiles to align with your new data source.

![](https://downloads.intercomcdn.com/i/o/1084913910/b205c08945b6e6c6cbc8ca30/Important+-+Orng.png?expires=1784430000&signature=bf6c2a749ade4f8648ccb846249174c5aa8858ab18808f1810375be1e70de3a1&req=dSAvEsB%2FnoheWfMW3Hu4gaICBQVZUqlMEDazqGB3YpKJ54510u2I5y3BCMW2%0A8A%3D%3D%0A)This article assumes you are familiar with editing [data sources](https://help.element451.com/en/articles/2066888-data-sources) and [fields](https://help.element451.com/en/articles/9118615-field-management), and the [Import + Export](https://help.element451.com/en/collections/8561605-import-export) module. If you are not familiar, please visit those respective help articles before attempting to change data sources.

---

# Updating the Field to Use the New Data Source

## Field Management Level

At this point, you have your new data source built and you are ready to change the field to use the new data source.

1. Navigate to Field Management and find the field you are updating. The first two tabs are **system-delivered fields**, and the last tab is the **custom fields** your institution has created.
2. Click the **pencil** **icon** next to your field.
3. Either navigate to the field options sections or toggle the "Use Default Data Source" to off to select the new data source.

[![](https://downloads.intercomcdn.com/i/o/737206339/f76a817228da80399aa05d8b/edit_field_management.gif?expires=1784333700&signature=c9cd90931360edd12d33bbce2b00d27355a014c248986d90c0333891d0ab77c1&req=cyMgFMl4noJWFb4f3HP0gHvaCorunlQ6RaB6z5Z8%2BMOxo0UGszkebprZYpR7%0Adi1pc6CMO1G%2BaqppOQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/737206339/f76a817228da80399aa05d8b/edit_field_management.gif?expires=1784333700&signature=c9cd90931360edd12d33bbce2b00d27355a014c248986d90c0333891d0ab77c1&req=cyMgFMl4noJWFb4f3HP0gHvaCorunlQ6RaB6z5Z8%2BMOxo0UGszkebprZYpR7%0Adi1pc6CMO1G%2BaqppOQ%3D%3D%0A)

## Form, Application, and Event Level

Changing the data source at the Field Management level will impact any future forms, applications, and events built that use that field, but any current forms, applications, and events need to be updated as well.

Each form, application, and event that uses the field needs to be updated to the new data source by clicking the pencil icon on the field and selecting the new data source.

[![](https://downloads.intercomcdn.com/i/o/737254470/7d3f89495a924c66b19340b2/edit_form.gif?expires=1784333700&signature=1e8464968c241852fce21b3acd8aeff456af189f3d65ae290af1a4cedba682b0&req=cyMgFMx6mYZfFb4f3HP0gH%2FpBQdO5zjbl%2BhdpGCbae70H52Ot34ydir%2FlYgu%0AG3mIonrEDQahly5dlA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/737254470/7d3f89495a924c66b19340b2/edit_form.gif?expires=1784333700&signature=1e8464968c241852fce21b3acd8aeff456af189f3d65ae290af1a4cedba682b0&req=cyMgFMx6mYZfFb4f3HP0gH%2FpBQdO5zjbl%2BhdpGCbae70H52Ot34ydir%2FlYgu%0AG3mIonrEDQahly5dlA%3D%3D%0A)

#

---

# Updating from Old Data Source to New Data Source

Now it is time to clean up all the records that already have data (using the old data source) in that field. This step will involve the Import + Export modules.

1. Create and save a segment for profiles that have data in the field you updated by using the "exists" operator.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/737335413/74d991c5a009c36acbfaf377/Screenshot+2023-05-08+at+2.22.51+PM.png?expires=1784333700&signature=1d871790fb6e6c2e755637ff54632938f2744e7bec9cc430228bb511e39f293a&req=cyMgFcp7mYBcFb4f3HP0gC99LOwrwXunaNxTTniUpojyZjpdc76cb3Koith5%0A9aE%3D%0A)](https://downloads.intercomcdn.com/i/o/737335413/74d991c5a009c36acbfaf377/Screenshot+2023-05-08+at+2.22.51+PM.png?expires=1784333700&signature=1d871790fb6e6c2e755637ff54632938f2744e7bec9cc430228bb511e39f293a&req=cyMgFcp7mYBcFb4f3HP0gC99LOwrwXunaNxTTniUpojyZjpdc76cb3Koith5%0A9aE%3D%0A)
2. Create an export task using that segment, and on the mapping tab, at minimum, add the "Element ID" and the field that needs to be cleaned up.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/737340636/de060c9be866bd0a2aaeb8bf/Screenshot+2023-05-08+at+2.30.34+PM.png?expires=1784333700&signature=73b8ab79f1f2eae15ddf7fccbfe36e7ecbae86cd2e86ae50ec6e82efcfa05763&req=cyMgFc1%2Bm4JZFb4f3HP0gAaBJ0egDDDXXsn9AyuPlmIEo%2FmvO8yReUtvjBQe%0Ao94%3D%0A)](https://downloads.intercomcdn.com/i/o/737340636/de060c9be866bd0a2aaeb8bf/Screenshot+2023-05-08+at+2.30.34+PM.png?expires=1784333700&signature=73b8ab79f1f2eae15ddf7fccbfe36e7ecbae86cd2e86ae50ec6e82efcfa05763&req=cyMgFc1%2Bm4JZFb4f3HP0gAaBJ0egDDDXXsn9AyuPlmIEo%2FmvO8yReUtvjBQe%0Ao94%3D%0A)
3. Once the export task has run, you can open the file in your preferred spreadsheet tool and swap out the old values from the old data source to the new values from your new data source.

   * 📌 **Note:** It does not matter if you insert the names or codes of the new data source as long as they are consistent throughout your spreadsheet.
4. Save your file and head back to your Element451 instance to create an import task.
5. For your import task, after dropping in your cleaned-up file:

   * We recommend setting the import to "Update Existing" profiles on the mapping tab to prevent records from getting created in the event they were deleted/merged during the time you were cleaning the file.
   * Map the Element ID and the field you are updating. For the field you are updating, click on the blue gear. Then, identify if you are bringing in the names or the codes and check the "Enabled" box.
   * On the matching tab, select to match on Element ID. From there, your import task is ready to be run!  
     ​

   [![](https://downloads.intercomcdn.com/i/o/737373035/a85d17f3cb45e113c9538f8f/import.gif?expires=1784333700&signature=be27ad8bea0f7b667d542fede5b90eb966dc02c98f2df118b5ffeca0981f59e5&req=cyMgFc59nYJaFb4f3HP0gCXmiy32sktPRSvcRruHBXL6mdl4yA34S1I%2Fake%2F%0ASBY%3D%0A)](https://downloads.intercomcdn.com/i/o/737373035/a85d17f3cb45e113c9538f8f/import.gif?expires=1784333700&signature=be27ad8bea0f7b667d542fede5b90eb966dc02c98f2df118b5ffeca0981f59e5&req=cyMgFc59nYJaFb4f3HP0gCXmiy32sktPRSvcRruHBXL6mdl4yA34S1I%2Fake%2F%0ASBY%3D%0A)

---

# Confirm the Updates Using Segments

To confirm that all possible records have been updated, create a segment that looks for data in that field that "exists" and is "not in" all the new values. The first part of [this article](https://help.element451.com/en/articles/4404458-a-guide-for-data-clean-up) can guide you in building it.

---