---
title: Creating Document Imports with Index Files
url: https://help.element451.com/en/articles/9585086-creating-document-imports-with-index-files
collection: Data Management
---

Learn how to import your documents utilizing the index files vendors provide.

# Overview

This article walks you through creating a document import where the folder containing the documents has an associated index file. This is a common format seen by our partners using vendors that collect and share student credentials such as transcripts, test scores, diplomas, and more.

📦 **File size limit:** Each .zip you import should be **300 MB or smaller**. If your document set exceeds 300 MB, split it into multiple smaller .zip files and run them as separate import tasks.

---

# Initial Set Up

## Check Data Connectors

Before building any import task, you will want to make sure that the proper data connectors are set up and that the incoming folders of documents are received. Depending on the vendor, you will either provide them with the Element451-hosted SFTP or add the vendor-hosted SFTP to the list of Data Connectors.

[Explore More: Data Connectors](https://help.element451.com/en/articles/9007788-data-connectors)

## Create Document Types and Folders

Make sure all the documents you are importing from your vendor have a Document Type in Element451. Document Types can be general, like Transcripts, or specific, like Official Final Transcripts, depending on your institution's processes.

[Explore More: Managing Document Types](https://help.element451.com/en/articles/2433933-managing-document-types)

During the document import build, you will have the option to import documents into a Document Folder to add a level of organization to your Documents Bin. Creating new folders can be done on the Documents Bin screen.

---

# Creating the Import Tasks

## Create a Data Import for the Index File

Before building a document import, it is critical to start with data import for the index file first. This step will ensure that the students coming from these vendors have a profile in Element451, which will reduce the number of documents going into the General Bin unassigned. Refer to [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports) for a refresher on importing a data file. At a minimum, you will want to map any identifier fields, like email and IDs, but if this is the student's first interaction with your institution, you will probably want more information, like names and addresses, if those fields are available on the index file.

### For Scheduled Imports

If this is going to be a scheduled task that runs every day, utilize dynamic path names to pick up the index file from the current date's folder. When selecting the SFTP as your data connector and navigating through the folders in the SFTP, you can edit the path field toward the top of the screen. For example, if you were working on an SCOIR import, you can edit your path name to end in scoir-documents-[date:now,format=Y-m-d]-\*.zip; once the folder for the current date loads up, select the index.csv file in there and click save. Now, every time the import is scheduled to run, it will look for the current date folder and pull the index.csv in that folder.

[![](https://downloads.intercomcdn.com/i/o/1111894392/e419b585e1d4563c8a937df4/Screenshot+2024-07-12+at+11_06_20%E2%80%AFAM.png?expires=1784333700&signature=2e81cfc87d4b66e58c099b66039289d0808bdc9ec9be756a663733caba46dcf3&req=dSEmF8F3mYJWW%2FMW1HO4zf%2BF%2BBurN9TofZgB1ZTrM7apEEJdiGhtjsZepiwi%0AczuZnSnfIIrKTYUd330%3D%0A)](https://downloads.intercomcdn.com/i/o/1111894392/e419b585e1d4563c8a937df4/Screenshot+2024-07-12+at+11_06_20%E2%80%AFAM.png?expires=1784333700&signature=2e81cfc87d4b66e58c099b66039289d0808bdc9ec9be756a663733caba46dcf3&req=dSEmF8F3mYJWW%2FMW1HO4zf%2BF%2BBurN9TofZgB1ZTrM7apEEJdiGhtjsZepiwi%0AczuZnSnfIIrKTYUd330%3D%0A)

## Create a Document Import

Create another import task, this time a document import. As you are selecting the correct folder in the SFTP, once inside the desired folder, toggle the **Use Index File** to **On**, select the index file in the folder, select **Import from Selected Index File**, and **Save**.

[![](https://downloads.intercomcdn.com/i/o/1111898056/a6b796c149c02479b54ab93b/Screenshot+2024-07-12+at+11_22_49%E2%80%AFAM.png?expires=1784333700&signature=bc826064ea318df0baa502d415dfe4e1fd92accddbe2c886fd0bfa2c07e4f8db&req=dSEmF8F3lYFaX%2FMW1HO4zTXpBCcI5sQyM%2FvQg7gAPzD%2BZjfgCEQ2ITmGZZBO%0AsDUeTkQU1QpSkd%2BSh7M%3D%0A)](https://downloads.intercomcdn.com/i/o/1111898056/a6b796c149c02479b54ab93b/Screenshot+2024-07-12+at+11_22_49%E2%80%AFAM.png?expires=1784333700&signature=bc826064ea318df0baa502d415dfe4e1fd92accddbe2c886fd0bfa2c07e4f8db&req=dSEmF8F3lYFaX%2FMW1HO4zTXpBCcI5sQyM%2FvQg7gAPzD%2BZjfgCEQ2ITmGZZBO%0AsDUeTkQU1QpSkd%2BSh7M%3D%0A)

## For Scheduled Imports

In a similar fashion to the Index File import, you will want to utilize the dynamic path names feature to pick up the current date's folder. When selecting the SFTP as your data connector and navigating through the folders in the SFTP, you can edit the path field toward the top of the screen. For example, if you were working on an SCOIR import, you can edit your path name to end in scoir-documents-[date:now,format=Y-m-d]-\*.zip; once the folder for the current date loads up, toggle the **Use Index File** to **On**, select the index file in the folder, select **Import from Selected Index File**, and **Save**. Now, every time the import is scheduled to run, it will look for the current date folder and pull the index.csv in that folder.

## Index File Settings

After saving your SFTP folder path settings, the tabs of your import will update to the Index File set-up tabs. Under **Index File Settings**, you will instruct Element451 how to use the contents of the index file to match up documents in the folder to the students listed in the index file. The columns in the index file will be displayed on this screen.

[![](https://downloads.intercomcdn.com/i/o/1111898334/4c32258b1a2e6ebf7597b2bd/Screenshot+2024-07-12+at+11_35_42%E2%80%AFAM.png?expires=1784333700&signature=82e6c8adffa610d5a5db3d958b801ead0ec817add3b4d8e150d5b47053079383&req=dSEmF8F3lYJcXfMW1HO4zaecTBDtYdKGv6r2Y9qr2vTOTmV1AptTDQ9dGM53%0AiDuYazkTHt%2FyiuFU3Os%3D%0A)](https://downloads.intercomcdn.com/i/o/1111898334/4c32258b1a2e6ebf7597b2bd/Screenshot+2024-07-12+at+11_35_42%E2%80%AFAM.png?expires=1784333700&signature=82e6c8adffa610d5a5db3d958b801ead0ec817add3b4d8e150d5b47053079383&req=dSEmF8F3lYJcXfMW1HO4zaecTBDtYdKGv6r2Y9qr2vTOTmV1AptTDQ9dGM53%0AiDuYazkTHt%2FyiuFU3Os%3D%0A)

### Person Matching

Identify what columns can be used from the index file to use as matching when trying to find the record in Element451. Common ones are the vendor ID, Common App ID, and email. On the person matching columns, change the Mode dropdown from **Skip** to **Person Matching**. A warning icon will pop up to notify you that there is an additional setup step. Click that icon and select the Element451 field to match on.

[![](https://downloads.intercomcdn.com/i/o/1112021721/52a35560a83bced6e01a4d5e/Note.png?expires=1784333700&signature=c91da94fa9d827c54689dfaf4f0235156e4c4e08d230a9d9b38b40c6c05b1fca&req=dSEmFMl8nIZdWPMW1HO4zaLJhXtwJwv6WVqRqECz%2B7LnctKsg5URF55uVqT3%0ABU%2Fuyt%2BTHnhOpESXzaQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1112021721/52a35560a83bced6e01a4d5e/Note.png?expires=1784333700&signature=c91da94fa9d827c54689dfaf4f0235156e4c4e08d230a9d9b38b40c6c05b1fca&req=dSEmFMl8nIZdWPMW1HO4zaLJhXtwJwv6WVqRqECz%2B7LnctKsg5URF55uVqT3%0ABU%2Fuyt%2BTHnhOpESXzaQ%3D%0A)

Keep in mind what fields you mapped on the initial index file import; if the vendor ID isn't mapped in the initial index file import, it is useless to use as a matching field for the document import.

[![](https://downloads.intercomcdn.com/i/o/1111898619/b43b00ffd8a8f8cd83ee3d6c/Screenshot+2024-07-12+at+11_36_24%E2%80%AFAM.png?expires=1784333700&signature=b871b23a178369923afda65a4e89f161b750545b8c4c1961fc4e3e8c006876db&req=dSEmF8F3lYdeUPMW1HO4zeYEDNVVEnlt%2BTrqfkEPLI2DpF8nUNi6P7J30Xr%2B%0AANAsBAhCntTs983jMPo%3D%0A)](https://downloads.intercomcdn.com/i/o/1111898619/b43b00ffd8a8f8cd83ee3d6c/Screenshot+2024-07-12+at+11_36_24%E2%80%AFAM.png?expires=1784333700&signature=b871b23a178369923afda65a4e89f161b750545b8c4c1961fc4e3e8c006876db&req=dSEmF8F3lYdeUPMW1HO4zeYEDNVVEnlt%2BTrqfkEPLI2DpF8nUNi6P7J30Xr%2B%0AANAsBAhCntTs983jMPo%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1111898799/538c49b8884ac555f21df8e9/Screenshot+2024-07-12+at+11_36_41%E2%80%AFAM.png?expires=1784333700&signature=bccb9768b5c32969dc7e65b38a79b6b5dc8a7e51d8218b25418428e2f4e27599&req=dSEmF8F3lYZWUPMW1HO4zQHmV3Uf9zvzxkJB8oaCNVONpBSkmcy2OG%2FxVUJl%0AKw4aqfDiu1NUAWWQpKs%3D%0A)](https://downloads.intercomcdn.com/i/o/1111898799/538c49b8884ac555f21df8e9/Screenshot+2024-07-12+at+11_36_41%E2%80%AFAM.png?expires=1784333700&signature=bccb9768b5c32969dc7e65b38a79b6b5dc8a7e51d8218b25418428e2f4e27599&req=dSEmF8F3lYZWUPMW1HO4zQHmV3Uf9zvzxkJB8oaCNVONpBSkmcy2OG%2FxVUJl%0AKw4aqfDiu1NUAWWQpKs%3D%0A)

While running, the Task will attempt to match to an existing Person. If no match is found, the document will still import to the designated location.

🚀 **Pro tip:** Create a Data Import Task and import the index file. This will ensure each document matches to an existing Person.

### Document Type

Identify the column in the index file that provides the document type coming in. These document types may not be the exact naming convention you use in Element451, but that will be addressed in the next tab. On the document type column, change the **Mode** dropdown from **Skip** to **Document Type**.

[![](https://downloads.intercomcdn.com/i/o/1111915654/5dd465328f94f5cdc33d0c40/Screenshot+2024-07-12+at+2_06_13%E2%80%AFPM.png?expires=1784333700&signature=59f78ec73ed92f4f53ce0f669ed84fb5c37cc57fe0e2c03f451bf296cd31c44d&req=dSEmF8B%2FmIdaXfMW1HO4zbH8R6nolEGxn1HgMvivF%2Fsjk99R06j153gEzWER%0ANX9eV34mHMJ46IT3UIQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1111915654/5dd465328f94f5cdc33d0c40/Screenshot+2024-07-12+at+2_06_13%E2%80%AFPM.png?expires=1784333700&signature=59f78ec73ed92f4f53ce0f669ed84fb5c37cc57fe0e2c03f451bf296cd31c44d&req=dSEmF8B%2FmIdaXfMW1HO4zbH8R6nolEGxn1HgMvivF%2Fsjk99R06j153gEzWER%0ANX9eV34mHMJ46IT3UIQ%3D%0A)

### Filename

Identify the column in the index file that provides the filename. On the filename column, change the **Mode** dropdown from **Skip** to **Filename**.

[![](https://downloads.intercomcdn.com/i/o/1111916018/2d1c64b7eeffd52f0510f7d6/Screenshot+2024-07-12+at+2_07_30%E2%80%AFPM.png?expires=1784333700&signature=07f8bbd766f70e095e31f40ff3f60d63f4b6754982d1be37fbf514812a2eecb8&req=dSEmF8B%2Fm4FeUfMW1HO4zVWUbJstTNX96ShLuFYwBqX9JzBdy3l%2FyGUKs8ur%0Af7eAhdcPebJf1NI3jMo%3D%0A)](https://downloads.intercomcdn.com/i/o/1111916018/2d1c64b7eeffd52f0510f7d6/Screenshot+2024-07-12+at+2_07_30%E2%80%AFPM.png?expires=1784333700&signature=07f8bbd766f70e095e31f40ff3f60d63f4b6754982d1be37fbf514812a2eecb8&req=dSEmF8B%2Fm4FeUfMW1HO4zVWUbJstTNX96ShLuFYwBqX9JzBdy3l%2FyGUKs8ur%0Af7eAhdcPebJf1NI3jMo%3D%0A)

## Document Types

On the **Document Types** tab, you will create a list of rules that maps the incoming files to their correct Element451 document type.

[![](https://downloads.intercomcdn.com/i/o/1111927965/dcb7c852480ef8be4bec8aaa/Screenshot+2024-07-12+at+2_19_52%E2%80%AFPM.png?expires=1784333700&signature=9584933a2d27fb63710749ec73da2d497c2095aa7d0c24ff398b27f339e90de8&req=dSEmF8B8mohZXPMW1HO4zb4lek8P32pe7OEVOi9LQtGj%2BfYCLnHhI86puzhp%0ABB2F%2FJOQLUjHTKVOGUw%3D%0A)](https://downloads.intercomcdn.com/i/o/1111927965/dcb7c852480ef8be4bec8aaa/Screenshot+2024-07-12+at+2_19_52%E2%80%AFPM.png?expires=1784333700&signature=9584933a2d27fb63710749ec73da2d497c2095aa7d0c24ff398b27f339e90de8&req=dSEmF8B8mohZXPMW1HO4zb4lek8P32pe7OEVOi9LQtGj%2BfYCLnHhI86puzhp%0ABB2F%2FJOQLUjHTKVOGUw%3D%0A)

Start by clicking **Add Matching Rule to Import**. On the **Index File Document Type\*** field, this is where you will insert the document type found in the index file from your vendor. Select the Element451 document type you want to map it to using the **Element451 Document Type\*** dropdown.

[![](https://downloads.intercomcdn.com/i/o/1112023785/78e172afb958d4f7f8de8111/Pro+Tip.png?expires=1784333700&signature=f298a48b5dc69dfcd49a8b0cb0aef5d19d1292e7aee7d9c597f41bf0bab50d78&req=dSEmFMl8noZXXPMW1HO4zSbE%2FHsrdtw0fKPRS4ltrXBDfnRwRcf%2FWz5jlQT6%0AE%2BylY7e6uSIvOllYzkA%3D%0A)](https://downloads.intercomcdn.com/i/o/1112023785/78e172afb958d4f7f8de8111/Pro+Tip.png?expires=1784333700&signature=f298a48b5dc69dfcd49a8b0cb0aef5d19d1292e7aee7d9c597f41bf0bab50d78&req=dSEmFMl8noZXXPMW1HO4zSbE%2FHsrdtw0fKPRS4ltrXBDfnRwRcf%2FWz5jlQT6%0AE%2BylY7e6uSIvOllYzkA%3D%0A)

If you do not want a vendor document type imported into Element451, do not create a matching rule for that document on this tab.

## Additional Set-Up Options

* **Convert to PDF**: Force conversion of the document to PDF.
* **Tags**: Add tags you want to be added to the imported document. This can be helpful to indicate it was not uploaded by the student.
* **Folder**: Select the folder where you want the document to be placed. This can be helpful to store all documents from a vendor in a specified folder.
* **Filters**:

  + Date Filter (Before date, After date, Date is equal to, Since last run, or Relative)
  + Size Filter (Equal, Greater than, Less than / B, KB, MB, GB)
  + Token Filter: Based on the person matching token (Equal, Greater than, Less than)

[![](https://downloads.intercomcdn.com/i/o/1111929615/d8d75e28268d0ac01fc79d77/Screenshot+2024-07-12+at+2_21_33%E2%80%AFPM.png?expires=1784333700&signature=9c21e25d977ef0956782a186fb39498740598d7b002dfb44e1057c6721b44bd8&req=dSEmF8B8lIdeXPMW1HO4zXPJsuCbFqJIpyYOJmcisCNr4jsYS1WhXmhjnHPB%0A%2B0hCxWAk2Xnuwwl0o0E%3D%0A)](https://downloads.intercomcdn.com/i/o/1111929615/d8d75e28268d0ac01fc79d77/Screenshot+2024-07-12+at+2_21_33%E2%80%AFPM.png?expires=1784333700&signature=9c21e25d977ef0956782a186fb39498740598d7b002dfb44e1057c6721b44bd8&req=dSEmF8B8lIdeXPMW1HO4zXPJsuCbFqJIpyYOJmcisCNr4jsYS1WhXmhjnHPB%0A%2B0hCxWAk2Xnuwwl0o0E%3D%0A)

## Notifications

Like other import and export tasks, the **Notifications** tab will let you add emails to receive notifications of the task status.

## Preview

The **Preview** tab will give you an idea of how many documents in the current folder would come into Element451 and how many didn't match the Document Type matching rules.

[![](https://downloads.intercomcdn.com/i/o/1115358666/af8c1594d9824ffbcbc0728c/Screenshot+2024-07-16+at+10_17_12%E2%80%AFAM.png?expires=1784333700&signature=053a79c28b8470d52a6b22e73fba4aa61640062607b1235ce946b04b4e28d996&req=dSEmE8p7lYdZX%2FMW1HO4zU3FM76d37ekJ%2Fz%2FHxPLaiWDanti2D4kiQjt%2FC%2FN%0ADZWCWj9m3%2F9iqIC7V3k%3D%0A)](https://downloads.intercomcdn.com/i/o/1115358666/af8c1594d9824ffbcbc0728c/Screenshot+2024-07-16+at+10_17_12%E2%80%AFAM.png?expires=1784333700&signature=053a79c28b8470d52a6b22e73fba4aa61640062607b1235ce946b04b4e28d996&req=dSEmE8p7lYdZX%2FMW1HO4zU3FM76d37ekJ%2Fz%2FHxPLaiWDanti2D4kiQjt%2FC%2FN%0ADZWCWj9m3%2F9iqIC7V3k%3D%0A)

## Run Import

Once you are ready to execute your task, click **Run Import** (if running immediately) or **Schedule** (if running on schedule). Schedules can mean a one-time run in the future or a repeated run. Read more about [Scheduling Imports](https://help.element451.com/en/articles/9007716-scheduling-import-export).

---