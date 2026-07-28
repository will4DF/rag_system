---
title: Creating Export Mapping Templates
url: https://help.element451.com/en/articles/9006851-creating-export-mapping-templates
collection: Data Management
---

Learn how to create templates for your exports.

# Overview

Export Mapping Templates simplify your Export Task workflow by allowing you to quickly apply predefined mapping and transformations to new export tasks. These templates come in handy when you find yourself creating export tasks for identical file layouts time and time again.

In this article, we’ll walk through creating, managing, and applying your Mapping Templates to Exports.

## Important Notes About Export Mapping Templates

* You must have the *Administer Data Templates* permission to create and manage Mapping Templates.
* Mapping Templates will map the columns of your data for you, but you can still modify any field after applying a template.
* Updating templates on the Mapping Templates screen will not affect any previous Export Tasks that used that Template.

---

# Accessing Export Mapping Templates

Mapping Templates for Imports can be found under **Data + Automations** > **Import + Export** > **Mapping Templates** > **Export Mapping Templates**.

[![](https://downloads.intercomcdn.com/i/o/975988661/4366025b098f9723e0fe28d0/Screenshot+2024-02-27+at+4_19_14%E2%80%AFPM.png?expires=1784333700&signature=e8aabaaf7afbfaf4859892eb3b40fdfc84093e884dace413865d7be1722d5e44&req=fSciH8F2m4deFb4f3HP0gG9FOuzjwc3luLW1yEiSSmdIorMxQGRXpAOilP4Q%0Ax4ycqjwYdlqWmzOikw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/975988661/4366025b098f9723e0fe28d0/Screenshot+2024-02-27+at+4_19_14%E2%80%AFPM.png?expires=1784333700&signature=e8aabaaf7afbfaf4859892eb3b40fdfc84093e884dace413865d7be1722d5e44&req=fSciH8F2m4deFb4f3HP0gG9FOuzjwc3luLW1yEiSSmdIorMxQGRXpAOilP4Q%0Ax4ycqjwYdlqWmzOikw%3D%3D%0A)

---

# Creating a New Template

## Option 1: Create a New Template on the Template Screen

1. Navigate to **Data + Automations** > **Import + Export** > **Mapping** **Templates** > **Export** **Mapping** **Templates.**
2. Click the **+** button.
3. Enter a name for your Template and click **Confirm.**
4. Click the **+ Add a Mapping** to start adding fields to your Template.

<insert gif>

## Option 2: Create a New Template on the Export Task Mapping Tab

1. Navigate to **Data + Automations** > **Import + Export** > **Exports.**
2. Create an Export.
3. After mapping all the fields, click the **Save as Template** button.
4. Enter a name for your Template and click **Confirm.**

[![](https://downloads.intercomcdn.com/i/o/975991758/a8476b764c267de2d1a80d02/Screenshot+2024-02-27+at+4_23_42%E2%80%AFPM.png?expires=1784333700&signature=f1dafb61767faedf3968fb8b22b5896685a2f8be2eb11fdf88cf4a32f0b51ac8&req=fSciH8B%2FmoRXFb4f3HP0gN47qtQGssiDTGpqGADFZrzT%2FJg2aZ8g2go9e1IK%0AjfZkS29rgDZkhs4j2w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/975991758/a8476b764c267de2d1a80d02/Screenshot+2024-02-27+at+4_23_42%E2%80%AFPM.png?expires=1784333700&signature=f1dafb61767faedf3968fb8b22b5896685a2f8be2eb11fdf88cf4a32f0b51ac8&req=fSciH8B%2FmoRXFb4f3HP0gN47qtQGssiDTGpqGADFZrzT%2FJg2aZ8g2go9e1IK%0AjfZkS29rgDZkhs4j2w%3D%3D%0A)

---

# Types of Columns

While creating templates from scratch, when you click the **+ Add a Mapping** button, a sidesheet will come up where you can select the type of column to add to your Template.

* **Standard:** Select a field in the database to export.
* **Calculated:** Create a formula that performs actions or manipulates the data on its way out of Element451
* **Unmapped:** Creates an empty column unless later mapped.

[![](https://downloads.intercomcdn.com/i/o/975992955/2ed7f647aa47173a546648f3/Screenshot+2024-02-27+at+4_26_53%E2%80%AFPM.png?expires=1784333700&signature=84ef91c526f8039334aa1afd2225aa823636f3837cd3945f7ce70ad3ac784f85&req=fSciH8B8lIRaFb4f3HP0gBG0LgQwbYCq5L6zHpTN5iQxcyVBexy%2BnM3jay1I%0A%2FkyRYPnL7BEDaT6gng%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/975992955/2ed7f647aa47173a546648f3/Screenshot+2024-02-27+at+4_26_53%E2%80%AFPM.png?expires=1784333700&signature=84ef91c526f8039334aa1afd2225aa823636f3837cd3945f7ce70ad3ac784f85&req=fSciH8B8lIRaFb4f3HP0gBG0LgQwbYCq5L6zHpTN5iQxcyVBexy%2BnM3jay1I%0A%2FkyRYPnL7BEDaT6gng%3D%3D%0A)

---

# Editing and Duplicating Templates

To edit export templates, head to **Data + Automations** > **Import + Export** > **Mapping Templates** > **Export Mapping Templates**.

1. Click the Template you want to edit and start making your changes.
2. The changes will save automatically.

Duplicating export templates is similar to duplicating Word documents.

1. Click on the Template you want to duplicate.
2. Click the **Save as Template** button in the corner.
3. Name the Template and click **Confirm.**

---

# Applying a Template

1. Navigate to **Data + Automations** > **Import + Export** > **Exports.**
2. Start a new Export and select **Data.**
3. Select your **Segment** and **Repeat Rows Setting.**
4. On the **Mapping** tab, click the **Load template** button. If it is a template you created, you will find it under Custom Templates.

---