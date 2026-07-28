---
title: Creating Document Exports
url: https://help.element451.com/en/articles/9011277-creating-document-exports
collection: Data Management
---

How to create document exports.

# Overview

The Document Export feature in Element451 is a great way to process batches of documents. Some potential reasons to use Document Exports are transferring documents to your institution's SIS, archiving application materials for your institution's records, or even to print certain documents that were uploaded to Element451.

📌 **Note:** Document exports perform best on batches of up to **10,000 files**. Larger exports aren't guaranteed to complete reliably and may fail during processing or delivery. For high-volume needs, use the filters under **Files > Advanced Settings** (such as Date, User Segment, or Size) to split the job into smaller batches, or schedule recurring exports.

---

# Creating a New Document Export

To create a new document export:

1. Navigate to **Data + Automations > Import + Export > Exports.**
2. Click on the **+** button along the right-hand side.
3. Select **Document**, and click **Confirm.**

## Files

After creating the new document export task, a sidesheet will appear for your new export. The first tab to display will be the **File** tab. This will be where you decide where are the documents getting pulled from, what documents you want to export, and any additional parameters. Sources for documents include:

* **Application**: application previews and any documents the student is asked to upload on their application before submitting it (such as a personal statement or a resume)
* **Info Request**: any documents that are asked for as part of the "Info Request" section of the application, such as letters of recommendation or church endorsement forms
* **General Bin**: any "studentless" documents (a document that was imported but never matched up with a student in Element451)
* **Microsite Document**: anything an admitted student can upload via the Microsite
* **Users Bin**: any documents on the record profile
* **Webform**: any documents collected on a form response

[![](https://downloads.intercomcdn.com/i/o/977083423/426e76dfa8dbb8a56f38f2fb/Screenshot+2024-02-28+at+3_33_29%E2%80%AFPM.png?expires=1784333700&signature=c72efa1a2c20c052488062088c6cfbf902f2268d8ce4d4d2219efa248061557b&req=fScgFsF9mYNcFb4f3HP0gHPzj6FnFNsVFJbKc0CZ20vT6OeyE5fZeYYJSmrM%0ApBBpXTFRSrIVvR27Tg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977083423/426e76dfa8dbb8a56f38f2fb/Screenshot+2024-02-28+at+3_33_29%E2%80%AFPM.png?expires=1784333700&signature=c72efa1a2c20c052488062088c6cfbf902f2268d8ce4d4d2219efa248061557b&req=fScgFsF9mYNcFb4f3HP0gHPzj6FnFNsVFJbKc0CZ20vT6OeyE5fZeYYJSmrM%0ApBBpXTFRSrIVvR27Tg%3D%3D%0A)

📌 Note: When using the "*Tag Exported Documents*" option, only documents in the Documents card on a profile are tagged. Element451-created documents are not tagged.

After selecting a **Source** for the documents to get pulled from, you will then decide what document types to pull. From this page, you could choose **Select All** and export all documents collected on an application. You could also select documents from many different sources, such as pulling a few documents from Applications and a few from Microsites.

[![](https://downloads.intercomcdn.com/i/o/977085398/e34c4217788d08392bbdef79/Screenshot+2024-02-28+at+3_36_26%E2%80%AFPM.png?expires=1784333700&signature=dc85f4cd6cfa4cf1108201b2ba2a653c531405623bf77989799c9fea00669f30&req=fScgFsF7nohXFb4f3HP0gO5tnGZcaUhC8zlHI2tCcid8r4FIqM3zVzdnLAjj%0Ao9ggHLWYlDNS2DgbCA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977085398/e34c4217788d08392bbdef79/Screenshot+2024-02-28+at+3_36_26%E2%80%AFPM.png?expires=1784333700&signature=dc85f4cd6cfa4cf1108201b2ba2a653c531405623bf77989799c9fea00669f30&req=fScgFsF7nohXFb4f3HP0gO5tnGZcaUhC8zlHI2tCcid8r4FIqM3zVzdnLAjj%0Ao9ggHLWYlDNS2DgbCA%3D%3D%0A)

## Files Advanced Settings

Once documents have been added to the document export, you can click the

[![](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idMgS3J5rIHC%2FLfJEvjZEmpaDii%0A9S16xZX3L16YdS6Q%2Bg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/911527686/a564a35d2a992e31b2f11dd7/Screenshot+2023-12-16+at+9.30.16%E2%80%AFPM.png?expires=1784333700&signature=b4c3f7c7e3827b0866564a5b046e29f00c28359cff589dd10904b3cc1b01165f&req=fSEmE8t5m4lZFb4f3HP0gJbD9r63glNm3idMgS3J5rIHC%2FLfJEvjZEmpaDii%0A9S16xZX3L16YdS6Q%2Bg%3D%3D%0A)

more button and add setup additional **Settings**. Under the **Settings** side sheet you can decide how the files should be named and add filters. The filter options you can choose from will depend on the source of the document. If you chose files from the General Bin, for example, which is comprised of documents not matched to a student, you will not be able to filter based on student information. Here are some of the filter options:

* **User Segment or User Segment Reference**: These two function similarly to segments in other modules, including People, Workflows, and Data Exports. You can either build one within the export or reference an existing segment that you have already created.
* **Name**: The Name condition allows you to filter the exports based on file names (only file names that contain "official," for example).
* **Date** - The Date condition lets you select only the files that were uploaded to Element451 either before, on, or after a particular date
* **Size** - The Size condition lets you select only the files that are less than, equal to, or greater than a particular file size.
* **Extension** - The Extension condition lets you choose if you only want files with extension .CSV, .PDF, or .DOC to be exported.

[![](https://downloads.intercomcdn.com/i/o/977092866/8c0593bedb88eab99d8f83ef/Screenshot+2024-02-28+at+3_46_44%E2%80%AFPM.png?expires=1784333700&signature=523fe1358c3005346cb6feb78f7dcbbf643f83418ada8270dd9b7ab5108f581e&req=fScgFsB8lYdZFb4f3HP0gOaOEgBM67r18T%2B5MrBSfWupSRNzcHKnFV48jG72%0AMyuXhS6FXVbeTMBDNA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977092866/8c0593bedb88eab99d8f83ef/Screenshot+2024-02-28+at+3_46_44%E2%80%AFPM.png?expires=1784333700&signature=523fe1358c3005346cb6feb78f7dcbbf643f83418ada8270dd9b7ab5108f581e&req=fScgFsB8lYdZFb4f3HP0gOaOEgBM67r18T%2B5MrBSfWupSRNzcHKnFV48jG72%0AMyuXhS6FXVbeTMBDNA%3D%3D%0A)

## Destination

Under the Destination tab, you will decide where the document export will be placing the documents.

## Packaging

After you have chosen the destination for your document export, navigate to the Packaging tab. Here you can specify the index file name pattern and select whether you want to Combine PDFs, create one folder per person, and/or zip everything.

* **One folder per person**: Groups files by student and uses ElementID as the folder name.
* **Zip everything**: Zips exported materials before storing them in the destination.

[![](https://downloads.intercomcdn.com/i/o/977102232/2e3d44e62cec63814fda7ada/Screenshot+2024-02-28+at+3_58_09%E2%80%AFPM.png?expires=1784333700&signature=8f4f24e6d80175f6af3a33f3efb0ff4b53ccb6ad8200e6a13bc2eb9f092bfcad&req=fScgF8l8n4JdFb4f3HP0gPtQ50UvHHV%2BN5aLKTKjT7yS17RyEaT6KqdtxptG%0AUw%2Fm8V7gkt14jo58vw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977102232/2e3d44e62cec63814fda7ada/Screenshot+2024-02-28+at+3_58_09%E2%80%AFPM.png?expires=1784333700&signature=8f4f24e6d80175f6af3a33f3efb0ff4b53ccb6ad8200e6a13bc2eb9f092bfcad&req=fScgF8l8n4JdFb4f3HP0gPtQ50UvHHV%2BN5aLKTKjT7yS17RyEaT6KqdtxptG%0AUw%2Fm8V7gkt14jo58vw%3D%3D%0A)

## Run Document Export

After creating matching rules and previewing the incoming documents, you are ready to move on to running the export task.

## Run Export

Click **Run Export** (if running immediately) or **Schedule** (if running on schedule). Schedules can mean a one-time run in the future or a repeated run. Learn more about [Schedule Exports](https://help.element451.com/en/articles/9007716-scheduling-import-export).

## Run History

The **Run History** tab shows the results of all runs executed by the import. Each run result will show the number of documents added by the run and the number of skipped documents in the folder.

---