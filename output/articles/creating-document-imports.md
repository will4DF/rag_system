---
title: Creating Document Imports
url: https://help.element451.com/en/articles/9011140-creating-document-imports
collection: Data Management
---

How to create a document import.

# Overview

This article walks you through creating an Document Import Task from scratch. This article will focus on importing documents. To import data, visit [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_39374e9e73).

**Things to know before importing documents:**

* We support a variety of document types: .pdf, .doc, .docx, .txt, .odt, .jpg, .jpeg, .png, .gif, .csv .ppt, .pptx, .svg, .txt,.xls, .xlsx, .html, .bmp, .htm
* Document names should contain a unique identifier so documents can be matched to students upon import
* Any documents that go unmatched will end up in the Documents Bin unassigned.
* It is important to have your document types, source folders, and file names set up correctly. To learn more about managing document types, see [here](https://help.element451.com/en/articles/2433933-managing-document-types).

📦 **File size limit:** Each .zip you import should be **300 MB or smaller**. If your document set exceeds 300 MB, split it into multiple smaller .zip files and run them as separate import tasks.

---

# Creating a New Document Import

To create a new document import:

1. Navigate to **Data + Automations > Import + Export.**
2. Click on the **+** button along the right-hand side.
3. Select **Document**, and click **Confirm.**

## Selecting an Import Source

After creating the new document import task, a sidesheet will appear for your new import. The first tab to display will be the **Source** tab. You can import documents from a Dropbox, SFTP, or Google Drive. In this example, we'll use **SFTP** to upload a file from your device. After selecting **SFTP**, click the relevant folder.

[![](https://downloads.intercomcdn.com/i/o/977033224/20bcd7aebef60b72ba4d130a/Screenshot+2024-02-28+at+2_30_01%E2%80%AFPM.png?expires=1784333700&signature=b665e6c691150988e1b515f6d3c475ac0f1d26901b1042aaedfa6198180b4c3f&req=fScgFsp9n4NbFb4f3HP0gII%2B8F2U1RBfTEnrTz9vv8%2Bwuwx7BjH87veicxxe%0An%2Fo5vjY5fE23K%2BjF0Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977033224/20bcd7aebef60b72ba4d130a/Screenshot+2024-02-28+at+2_30_01%E2%80%AFPM.png?expires=1784333700&signature=b665e6c691150988e1b515f6d3c475ac0f1d26901b1042aaedfa6198180b4c3f&req=fScgFsp9n4NbFb4f3HP0gII%2B8F2U1RBfTEnrTz9vv8%2Bwuwx7BjH87veicxxe%0An%2Fo5vjY5fE23K%2BjF0Q%3D%3D%0A)

## Matching

After selecting your folder, you can move to the **Matching** tab and click to add a rule. Toggle the option "Apply this filter to the main folder and the folder in it" if applicable (i.e. if you have the "Resume" folder within your "Documents" folder in the SFTP).

### Select Files

This field is where you define the filename pattern. When you have a identifier in the filename, start typing **[** to see the full list of identifiers you can match on.

🚀 **Pro tip:** If there are other characters in the file name that do not help with matching, you can use **\*** within the file name matching rules. The **\*** means that that part of the file name could contain any alphanumeric characters. Note that the email address, highlighted in orange, is a token and is what connects the file name to the particular student profile. You could also add **\*** after the "." in the file name, meaning that the file format could be .pdf, .docx, or something else and Element451 would still find it by this rule and import it.

### Document Type

Incoming documents that meet the filename pattern will be brought with the document type defined on the matching rule.

## Tags and Folders

Upon import, add tags to documents or assign them in folders to easily filter for them in the Documents Bin

## Filters

By adding filters on the matching rule, you can specify which documents you would like to import based on the size of the file, the date on which the file was created, a token within the file name, or some combination of the three. For example, you might want to set a token filter that only imports files with names such that [user:email\_address] contains the value ".edu," or a date filter that only imports documents uploaded since the import was last run.

[![](https://downloads.intercomcdn.com/i/o/977041627/5398da9ee89e8a3169d3f4fe/Screenshot+2024-02-28+at+2_38_51%E2%80%AFPM.png?expires=1784333700&signature=2e90f95ca465f2aea4f17a54e5c085ad0fa1671c74016101a009e1b1206ce325&req=fScgFs1%2Fm4NYFb4f3HP0gOZx4jcNREzz5RYQN%2BjxTAcHlaDzlA%2FocXwYA7Nr%0AgygxLeAJ0FsaDGLTHQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977041627/5398da9ee89e8a3169d3f4fe/Screenshot+2024-02-28+at+2_38_51%E2%80%AFPM.png?expires=1784333700&signature=2e90f95ca465f2aea4f17a54e5c085ad0fa1671c74016101a009e1b1206ce325&req=fScgFs1%2Fm4NYFb4f3HP0gOZx4jcNREzz5RYQN%2BjxTAcHlaDzlA%2FocXwYA7Nr%0AgygxLeAJ0FsaDGLTHQ%3D%3D%0A)

## Preview

The **Preview** tab will allow you to preview documents that would come in to confirm that everything looks good. The preview will let you know how many documents matched the rules and how many did not.

[![](https://downloads.intercomcdn.com/i/o/977051424/6304c6639227af2e5bc093d8/Screenshot+2024-02-28+at+2_52_07%E2%80%AFPM.png?expires=1784333700&signature=20a0d389c1a01475e5cc8ebefef1149117a6680ab3a2dd86d2d2bfd3b49b46e0&req=fScgFsx%2FmYNbFb4f3HP0gKqNcRS%2FfgKBWu%2B%2Bk4tktWcRJWFx4lmqQcWfsLmN%0AQSWCLFDiqC4K%2FfmRGQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977051424/6304c6639227af2e5bc093d8/Screenshot+2024-02-28+at+2_52_07%E2%80%AFPM.png?expires=1784333700&signature=20a0d389c1a01475e5cc8ebefef1149117a6680ab3a2dd86d2d2bfd3b49b46e0&req=fScgFsx%2FmYNbFb4f3HP0gKqNcRS%2FfgKBWu%2B%2Bk4tktWcRJWFx4lmqQcWfsLmN%0AQSWCLFDiqC4K%2FfmRGQ%3D%3D%0A)

## Run Import

After creating matching rules and previewing the incoming documents, you are ready to move on to running the import task.

Click **Run Import** (if running immediately) or **Schedule** (if running on schedule). Schedules can mean a one-time run in the future or a repeated run. Learn more about [Scheduling Import + Export](https://help.element451.com/en/articles/9007716-scheduling-import-export).

## Run History

The **Run History** tab shows the results of all runs executed by the import. Each run result will show the number of documents added by the run and the number of skipped documents in the folder.

---