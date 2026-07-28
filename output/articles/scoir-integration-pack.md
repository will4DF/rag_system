---
title: SCOIR Integration Pack
url: https://help.element451.com/en/articles/6821033-scoir-integration-pack
collection: Packs
---

Follow these steps to setup and configure the SCOIR Pack.

# Overview

[![](https://downloads.intercomcdn.com/i/o/647636235/27f52685638b98254dba570b/scoir_header.png?expires=1784333700&signature=f95af5f7a32bc067f8d6713a076b4660a8a67953b3a748f7e21aed0beca25477&req=ciQgEMp4n4JaFb4f3HP0gCcrEBSDWjbVGQjBqIr%2BpW1o75lfjIyGeG9WV1E1%0ADV4Vipm2ZvASWfPDvA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/647636235/27f52685638b98254dba570b/scoir_header.png?expires=1784333700&signature=f95af5f7a32bc067f8d6713a076b4660a8a67953b3a748f7e21aed0beca25477&req=ciQgEMp4n4JaFb4f3HP0gCcrEBSDWjbVGQjBqIr%2BpW1o75lfjIyGeG9WV1E1%0ADV4Vipm2ZvASWfPDvA%3D%3D%0A)

The SCOIR Integration Pack can connect your Element451 instance to SCOIR for automatic document management and import.

This Pack is for any institution that uses [SCOIR](https://www.scoir.com/) to manage documents submitted by applicants (such as transcripts and other application materials.)

![](https://downloads.intercomcdn.com/i/o/1084665151/90fde236980ddf3ff0a72764/Note-Orng.png?expires=1784430000&signature=87bdba54ec93b1f1012cb8ed4e2f1b1920227696f45c7c29cd33c55246877bee&req=dSAvEs94mIBaWPMW3Hu4gZ%2BpQinkGeJx16rDGyigg4WyguqSb4nAd7xFAN7f%0ALQ%3D%3D%0A) Some institutions may want to share these instructions with their IT or networking teams for assistance, as this will connect Element451 to cloud storage for data sharing.

Included Components:

* SCOIR Index Template

  + Data-import-template
* SCOIR Documents Import Task

  + Document-import-task

Setting up and configuring the SCOIR Pack requires the following steps outlined below.   
​

### Video Guide

---

## Step 1 - Install the Pack and Map Document Types

1. Install the Pack.
2. Select the appropriate document type to map to each SCOIR file type in the Pack install options.

   * You may need to configure or add document types to your instance before installing the pack, as it uses a drop-down list to select from *existing document types*. [Learn more about managing document types](https://help.element451.com/en/articles/2433933-managing-document-types).
   * A full list of SCOIR document types can be found [here](https://scoir.helpdocs.io/article/8x9vnwjdrb-for-colleges-supported-document-types).

[![](https://downloads.intercomcdn.com/i/o/647638893/11594a2ca6a9f800d068d433/pack_install_options.gif?expires=1784333700&signature=e5238806f4324697a3cba2e996f752d0e68188adcb82b3d3ad72b95b254fa712&req=ciQgEMp2lYhcFb4f3HP0gLvDYcHXXE59t%2BdT%2FvpYhsajREGs93e5e%2FHKZSXN%0Apm5oxNzqrypaVNsNsQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/647638893/11594a2ca6a9f800d068d433/pack_install_options.gif?expires=1784333700&signature=e5238806f4324697a3cba2e996f752d0e68188adcb82b3d3ad72b95b254fa712&req=ciQgEMp2lYhcFb4f3HP0gLvDYcHXXE59t%2BdT%2FvpYhsajREGs93e5e%2FHKZSXN%0Apm5oxNzqrypaVNsNsQ%3D%3D%0A)

---

## Step 2: Configure Your Source Folder in Element451

1. Locate your import template at **Data + Automations > Import > SCOIR Documents Import > Edit Task*.***
2. Configure your source folder under the "Source" tab on the SCOIR import document task.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/647641803/188b85692ec8890329c2efb7/source_options.gif?expires=1784333700&signature=548eb963929065f198ab3689e33f0e98fd0dcc2942185ec56da73bc7a3d5c5bb&req=ciQgEM1%2FlYFcFb4f3HP0gAA%2F%2F3Az4sHqxDrBIiWU6K6nLLEANf93Hr4QgU7x%0AwYM%3D%0A)](https://downloads.intercomcdn.com/i/o/647641803/188b85692ec8890329c2efb7/source_options.gif?expires=1784333700&signature=548eb963929065f198ab3689e33f0e98fd0dcc2942185ec56da73bc7a3d5c5bb&req=ciQgEM1%2FlYFcFb4f3HP0gAA%2F%2F3Az4sHqxDrBIiWU6K6nLLEANf93Hr4QgU7x%0AwYM%3D%0A)

   * Most likely this will be SFTP, as this is what SCOIR supports for dropping files off. The best practice is to set up a folder specifically for SCOIR exports.   
     ​  
     If you need your Element451 SFTP credentials, please contact Customer Success. *[Learn more about connecting Element451 to SFTP sources.](https://help.element451.com/en/articles/9146573-securely-transferring-files-sftp)*  
     ​

     [![](https://downloads.intercomcdn.com/i/o/647632094/ff56fd122484c865f1954584/Screen_Recording_2023-01-06_at_2_26_01_PM_AdobeExpress.gif?expires=1784333700&signature=8a870409b85c6c5cc1d5c559802dea6b9f9ccf39d0dc9d13d23ab90be875f1ce&req=ciQgEMp8nYhbFb4f3HP0gKyrt%2BW3XbSfQpoM9LgkzqkLoPbUmjXJKSAAlhZ2%0AN5o%3D%0A)](https://downloads.intercomcdn.com/i/o/647632094/ff56fd122484c865f1954584/Screen_Recording_2023-01-06_at_2_26_01_PM_AdobeExpress.gif?expires=1784333700&signature=8a870409b85c6c5cc1d5c559802dea6b9f9ccf39d0dc9d13d23ab90be875f1ce&req=ciQgEMp8nYhbFb4f3HP0gKyrt%2BW3XbSfQpoM9LgkzqkLoPbUmjXJKSAAlhZ2%0AN5o%3D%0A)

   ​

---

## Step 3: Configure your Index File and Delivery Preferences in your SCOIR Account

When installing the SCOIR Pack, a template for the robust version of the SCOIR Index file is created. Some of the basic fields that would be used for matching are pre-mapped. In other fields, you will be able to configure yourself. The index file is important as it allows for the SCOIR Student ID to be imported, which is used in the file name of SCOIR documents and used for matching during the import process. If you are already exporting a previous version of the index file from SCOIR, you may need to adjust your import template mappings.   
​  
​*When configuring your SCOIR settings, it is critical to select export individual PDFs for each document.*

[Explore Additional Documentation via SCOIR](https://scoir.helpdocs.io/article/4fbbxi0lu3-configuring-document-delivery-via-sftp)

1. **Connect your SCOIR export to your source folder in your SCOIR account.** ​Once completed, you can run a test batch, which should show up in your selected SFTP folder.
2. **Once the above steps are completed, create and activate the import tasks.**

   * First, create a data import using the SCOIR index template and select the appropriate source folder. The filename should be "index.csv". If you run a test batch (or have a previous export in the folder), you should see the file in the source folder. Matching can be configured based on the available fields and the processes of the institution. Finally, you'll need to schedule and run the data import for early morning on a daily recurring basis on Element451. SCOIR exports the documents overnight, and the import timing can be fine-tuned as needed.
   * Next, you will need to schedule the SCOIR Document import that the Pack created. When configuring the document import, you may see files under the preview tab if previously exported a test batch or a previous export is in the folder. Continue to the "Run Task" tab and schedule the import. The document import task should be scheduled 30 minutes or more after the time for the data import so that the SCOIR ID can be in the system.   
     ​  
     ​**You can access these settings on the SCOIR Import Document Task > Run Task.**  
     ​

     [![](https://downloads.intercomcdn.com/i/o/647645215/84ccf54f6c8425f46797930a/run_task.png?expires=1784333700&signature=b1107a115e27dc63033ac83eaedfb4326866d06032cdc6e14c0adbdbd444f82e&req=ciQgEM17n4BaFb4f3HP0gAu37tX9q8lBQz79PnThhDMPU4BX4kdX9Jexlzih%0AqmA%3D%0A)](https://downloads.intercomcdn.com/i/o/647645215/84ccf54f6c8425f46797930a/run_task.png?expires=1784333700&signature=b1107a115e27dc63033ac83eaedfb4326866d06032cdc6e14c0adbdbd444f82e&req=ciQgEM17n4BaFb4f3HP0gAu37tX9q8lBQz79PnThhDMPU4BX4kdX9Jexlzih%0AqmA%3D%0A)

### ​

---