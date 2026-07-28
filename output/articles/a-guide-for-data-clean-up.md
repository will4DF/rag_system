---
title: A Guide for Data Clean-Up
url: https://help.element451.com/en/articles/4404458-a-guide-for-data-clean-up
collection: Data Management
---

Step-by-step guide on how to conduct clean-up data in Element451

# Overview

This guide provides a step-by-step process to identify and clean up messy data.

---

## Step 1 - Create a Segment

* **Create a Segment**

  + We recommend starting with the following fields:

    - Campus
    - Gender
    - Term
    - Major
  + Choose a dropdown or radio-type field to investigate.
  + Use the following filters: [data] ***exists*** AND [data] ***is not in*** [any of your values] (see screenshot below)  
    ​

    [![](https://downloads.intercomcdn.com/i/o/482759134/fce9d2e2b6a52350c12f0f56/Screen+Shot+2022-03-18+at+3.51.24+PM.png?expires=1784333700&signature=4a4d6822578634be1557f5d1066edff4b82a09bf96efb3b766aaa3fdd877930c&req=cCglEcx3nIJbFb4f3HP0gFjI%2Fvh0jNyehlch2pFtcjv5QlzICdeRqdJf5o8X%0AIBg%3D%0A)](https://downloads.intercomcdn.com/i/o/482759134/fce9d2e2b6a52350c12f0f56/Screen+Shot+2022-03-18+at+3.51.24+PM.png?expires=1784333700&signature=4a4d6822578634be1557f5d1066edff4b82a09bf96efb3b766aaa3fdd877930c&req=cCglEcx3nIJbFb4f3HP0gFjI%2Fvh0jNyehlch2pFtcjv5QlzICdeRqdJf5o8X%0AIBg%3D%0A)

  The segment result should present data that is problematic.

---

# **STEP 2 - Export Segment**

* **Export the Segment**

  + Be sure to the ElementID **and** the field of interest

---

# STEP 3 - Clean Data in Spreadsheet

* **Clean the Data**

  + Use Excel or any other data manipulation tool of your choice to clean up the data. Tip: Look for "Find and Replace" options in your data manipulation tool.

---

# STEP 4: **Re-Import Carefully**

* **Re-import Carefully**

  + When setting up your import task, be sure to pay attention to mappings and transformations.
  + You should review the **preview** **before** running the task.

    - Majors, Terms, Campuses, Sources, and Labels should appear as the *GUID*. Gender should appear as a name, and degrees should appear as codes.
    - Import as null when necessary (to remove data from a field)

---