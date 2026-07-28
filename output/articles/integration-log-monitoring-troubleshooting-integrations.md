---
title: Integration Log: Monitoring + Troubleshooting Integrations
url: https://help.element451.com/en/articles/9455171-integration-log-monitoring-troubleshooting-integrations
collection: Data Management
---

![](https://downloads.intercomcdn.com/i/o/1080860149/4ec8c14ef8d4aa80e7db7b28/Note-Orng.png?expires=1784430000&signature=f016305d3ab0cb961c82dcecc9de0896be35ba90af1f406b18d63187556df7a2&req=dSAvFsF4nYBbUPMW3Hu4gdPccz4a661FlskzxCtyN792MhjkdjwdnMxX6ZVB%0AKA%3D%3D%0A) The Integration Log feature is only available to partners that have **managed integrations** with Element451.

# Overview

The Integration Log is a powerful tool to enhance transparency and efficiency for partners with managed data integrations. The Integration Log allows you to monitor and identify successful data syncs and errors, streamlining the troubleshooting process and maintaining your integrations by providing detailed information on every synced record.

[![](https://downloads.intercomcdn.com/i/o/1078439972/4fe961c0afbcf01ead4e9301/Integration+Logs+%281%29.png?expires=1784333700&signature=a4e273db74eabb851f2225df97b2ccdc50b5946428401572173040bbd97f1de2&req=dSAgHs19lIhYW%2FMW1HO4zSstyngszVhGUTKPkWKkvtp%2Banxz06bny0VCsBWO%0A3FqlJY38tQHtDev3xdc%3D%0A)](https://downloads.intercomcdn.com/i/o/1078439972/4fe961c0afbcf01ead4e9301/Integration+Logs+%281%29.png?expires=1784333700&signature=a4e273db74eabb851f2225df97b2ccdc50b5946428401572173040bbd97f1de2&req=dSAgHs19lIhYW%2FMW1HO4zSstyngszVhGUTKPkWKkvtp%2Banxz06bny0VCsBWO%0A3FqlJY38tQHtDev3xdc%3D%0A)

## Key Features

* **Comprehensive Listing:**The Integration Log lists every synced record for managed integrations to or from Element451, offering a complete overview of all integration activities.
* **Status Indication:** Easily see whether each sync was successful or if an error occurred. This feature allows for a quick assessment of the overall health of your integrations.
* **Error Summaries:** When an error occurs, the Integration Log often provides a summary, such as “More than one possible match,” offering quick insights into what went wrong.
* **Detailed Error Information:** For more in-depth troubleshooting, you can view full error details, including the error code and the content of the error. This detailed information helps you understand and resolve issues more effectively.
* **Search and Filter:** The Integration Log includes robust search and filter capabilities, allowing you to quickly find specific logs by name, ID, status (Success or Error), and date. This makes it easier to locate and address particular issues.

---

# Accessing the Integration Log

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1348974867/58ccdc776d4ff3dcb1cc413c0973/Note.png?expires=1784430000&signature=f6d162073f2cadb1f84774d9aeea49740e5e50ee700003e023f94003a2d162c7&req=dSMjHsB5mYlZXvMW3Hu4gdHmmI5v8RDZaDCk2Ay4OlZ2QgWanqHwmxt9wgXx%0A9g%3D%3D%0A) You must have the ***Administer Settings*** permission to access the logs.

Click on your avatar/profile picture and navigate to **Settings** > **Integrations** > **Integration** **Logs**.  
​

[![](https://downloads.intercomcdn.com/i/o/1078439737/b8ea4e43499dc6722c898986/Screenshot+2024-06-11+at+9_38_35%E2%80%AFAM.png?expires=1784333700&signature=e35f1259a44661a2ad989b34b5994311272091ea3251274f1dad49bd7c1299c1&req=dSAgHs19lIZcXvMW1HO4zeud3i2mBJI3ceRZ%2BS5hEX0Dbx29KZX3i8YY7zoJ%0AzTON%2Bkyeela6l2objLo%3D%0A)](https://downloads.intercomcdn.com/i/o/1078439737/b8ea4e43499dc6722c898986/Screenshot+2024-06-11+at+9_38_35%E2%80%AFAM.png?expires=1784333700&signature=e35f1259a44661a2ad989b34b5994311272091ea3251274f1dad49bd7c1299c1&req=dSAgHs19lIZcXvMW1HO4zeud3i2mBJI3ceRZ%2BS5hEX0Dbx29KZX3i8YY7zoJ%0AzTON%2Bkyeela6l2objLo%3D%0A)

---

# How to Use the Integration Log

## Review Synced Records

The Integration Log shows a comprehensive listing of all synced records. Each call has a dedicated row that displays:

[![](https://downloads.intercomcdn.com/i/o/1078465572/dcbc159d80f7c3a444a3cc91/Integration+Log+-+Details+%283%29.png?expires=1784333700&signature=16cd9ea68fae927e5fcacb82b341980745b84daf3ba2262e50c7f98e2b5bcea5&req=dSAgHs14mIRYW%2FMW1HO4zfqnoFMcoqs1yR7B%2FWcoDfL8xdnAQOOMq0xljVsc%0AA53A4I3kUZXRMA8OfIo%3D%0A)](https://downloads.intercomcdn.com/i/o/1078465572/dcbc159d80f7c3a444a3cc91/Integration+Log+-+Details+%283%29.png?expires=1784333700&signature=16cd9ea68fae927e5fcacb82b341980745b84daf3ba2262e50c7f98e2b5bcea5&req=dSAgHs14mIRYW%2FMW1HO4zfqnoFMcoqs1yR7B%2FWcoDfL8xdnAQOOMq0xljVsc%0AA53A4I3kUZXRMA8OfIo%3D%0A)

* **Name**: Contact Name (if available).
* **Type**: Integration (e.g., Ethos to E451)
* **Status**: Success or Error
* **Processed** **At**: Date when the sync was processed
* **Error** **Summary**: If the status is Error, a summary is provided (e.g., no matching user found to update)

## Detailed Error Information

* On a row with an Error status, you can click on the three vertical dots ![](https://downloads.intercomcdn.com/i/o/1078449654/113edc75c239ae0ac6044f88/More+Icon2.png?expires=1784430000&signature=749a970523173dcee560d4fb2b7fbdd7b2783e7c45035eccaa4a4e5f703b267f&req=dSAgHs16lIdaXfMW3Hu4gWtojWmejSHwT7k0%2B2d8JhusYUFjikaK44iG%2Bd1O%0AJQ%3D%3D%0A) and click view to open the error log for more details on the error to assist in troubleshooting and resolving issues.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1078458354/4c87ad2b2d542652ae94c802/Integration+Log+-+Details.png?expires=1784333700&signature=6b3283bc1719e942bbece2b3bcd956415b53bf99386b3ba1d841a84d93b3355c&req=dSAgHs17lYJaXfMW1HO4zWwpea8o4oMyl0N%2BDw43M5vPbB%2FEFnDTddRWhds%2B%0A%2FEMY%0A)](https://downloads.intercomcdn.com/i/o/1078458354/4c87ad2b2d542652ae94c802/Integration+Log+-+Details.png?expires=1784333700&signature=6b3283bc1719e942bbece2b3bcd956415b53bf99386b3ba1d841a84d93b3355c&req=dSAgHs17lYJaXfMW1HO4zWwpea8o4oMyl0N%2BDw43M5vPbB%2FEFnDTddRWhds%2B%0A%2FEMY%0A)

![](https://downloads.intercomcdn.com/i/o/1078451697/17885b27e69f3f09d005ca25/Pro+Tip+-+Orng.png?expires=1784430000&signature=7b920e9e42577fc40d6decde25d5612808d0d26cec0ad6724848a34768bc0faf&req=dSAgHs17nIdWXvMW3Hu4gR8qQht8LY0QjWx6VNymZivFFnOxT5AloCVg3agf%0ArA%3D%3D%0A) Use the search and filter options to narrow the logs by **status** and **date**. For external systems, you can even search by ID. This helps you find specific entries quickly.

---

# Integration Runs Profile Card

You can add the **Integration Runs** card to the [student profile](https://help.element451.com/en/articles/1475735-the-person-profile). This allows you to view a student's integration sync history directly from their record without navigating to the Integration Log.

---