---
title: Creating Import Mapping Templates
url: https://help.element451.com/en/articles/9002061-creating-import-mapping-templates
collection: Data Management
---

Learn about creating, managing, and applying Import Mapping Templates

# Overview

Import Mapping Templates simplify your Import Task workflow by allowing you to quickly apply predefined mapping and transformations to new import tasks. These templates come in handy when you find yourself creating import tasks for identical file layouts time and time again.

In this article, we’ll walk through creating, managing, and applying your Mapping Templates to Imports.

## Important Notes About Import Mapping Templates

* You must have the *Administer Data Templates* permission to create and manage Mapping Templates.
* Mapping Templates will map the columns of your data for you, but you can still modify any field after applying a template.
* Updating templates on the Mapping Templates screen will not affect any previous Import Tasks that used that Template.

---

# Accessing Import Mapping Templates

Mapping Templates for Imports can be found under **Data + Automations** > **Import + Export** > **Mapping Templates** > **Import Mapping Templates**.

[![](https://downloads.intercomcdn.com/i/o/974861963/05dd7cf652d57996a1cdeef6/Screenshot+2024-02-26+at+3_29_30%E2%80%AFPM.png?expires=1784333700&signature=1a95a4233aeff4975bb114453c3f077eb5e2db135e774fc6e9f4eb7eaa9f9e0e&req=fScjHs9%2FlIdcFb4f3HP0gF49myvjK1DxXL4gijUKyRq4bGXYVuFP7MtHYDa0%0AD7MA9vyUQjXgxP%2BnpQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/974861963/05dd7cf652d57996a1cdeef6/Screenshot+2024-02-26+at+3_29_30%E2%80%AFPM.png?expires=1784333700&signature=1a95a4233aeff4975bb114453c3f077eb5e2db135e774fc6e9f4eb7eaa9f9e0e&req=fScjHs9%2FlIdcFb4f3HP0gF49myvjK1DxXL4gijUKyRq4bGXYVuFP7MtHYDa0%0AD7MA9vyUQjXgxP%2BnpQ%3D%3D%0A)

---

# Creating a New Template

## Option 1: Create a New Template on the Template Screen

1. Navigate to **Data + Automations** > **Import + Export** > **Mapping** **Templates** > **Import** **Mapping** **Templates.**
2. Click the **+** button.
3. Enter a name for your Template and click **Confirm.**
4. Click the **+ Add a Mapping** to start adding fields to your Template.

## Option 2: Create a New Template on the Import Task Mapping Tab

1. Navigate to **Data + Automations** > **Import + Export** > **Imports.**
2. Create an Import.
3. After mapping all the fields, click the **Save as Template** button.
4. Enter a name for your Template and click **Confirm.**

[![](https://downloads.intercomcdn.com/i/o/974862973/cbd9998783e8d021d67aad4b/Screenshot+2024-02-26+at+3_42_07%E2%80%AFPM.png?expires=1784333700&signature=57f0ea07bcf87d837573b316be699edfc9d7a53d077f12c13f67eb5394b40b57&req=fScjHs98lIZcFb4f3HP0gL6lkivpN6RNZ7CGHe5gA4LQNKhO%2Flis2iLBRGY%2B%0ARMV524y286xnJNbKAg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/974862973/cbd9998783e8d021d67aad4b/Screenshot+2024-02-26+at+3_42_07%E2%80%AFPM.png?expires=1784333700&signature=57f0ea07bcf87d837573b316be699edfc9d7a53d077f12c13f67eb5394b40b57&req=fScjHs98lIZcFb4f3HP0gL6lkivpN6RNZ7CGHe5gA4LQNKhO%2Flis2iLBRGY%2B%0ARMV524y286xnJNbKAg%3D%3D%0A)

---

# Types of Columns

While creating templates from scratch, when you click the **+ Add a Mapping** button, a sidesheet will come up where you can select the type of column to add to your Template.

* **Standard:** Select a field in the database to map to.
* **Calculated:** Create a formula that performs actions or manipulates the incoming data before inserting it into a field in the database.
* **Relation:** Create a relationship between another contact or organization.

  + ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1212719272/3dd2132cf28d6c42956ce0b8a0b1/Note.png?expires=1784430000&signature=643121b8316b253a3f9e2a0a92ec20141926167bb42f0bfbf8fd0bae65f6a01e&req=dSImFM5%2FlINYW%2FMW3Hu4gXMrgWSs2VFA4VH%2FBJ1p3YwEciPk4SEU9e0ihnT6%0A1g%3D%3D%0A) At this time, you cannot use the test import function if you are importing relationships.
* **Unmapped:** Creates an empty column unless later mapped.

[![](https://downloads.intercomcdn.com/i/o/974863224/a1bcfc5d96e074312566c85e/Screenshot+2024-02-26+at+3_39_40%E2%80%AFPM.png?expires=1784333700&signature=6cf4e9f22d2ee9146e07eaf05ea481b12f8b67c66610f6de2c9a37a838162818&req=fScjHs99n4NbFb4f3HP0gEc87uOvM6sGYj3m0Sg9XmibhItfiWZmbESRfaNZ%0ArcK3mXfM3w9xHdyJsA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/974863224/a1bcfc5d96e074312566c85e/Screenshot+2024-02-26+at+3_39_40%E2%80%AFPM.png?expires=1784333700&signature=6cf4e9f22d2ee9146e07eaf05ea481b12f8b67c66610f6de2c9a37a838162818&req=fScjHs99n4NbFb4f3HP0gEc87uOvM6sGYj3m0Sg9XmibhItfiWZmbESRfaNZ%0ArcK3mXfM3w9xHdyJsA%3D%3D%0A)

---

# Editing and Duplicating Templates

To edit import templates, head to **Data + Automations** > **Import + Export** > **Mapping Templates** > **Import Mapping Templates**.

1. Click the Template you want to edit and start making your changes.
2. The changes will save automatically.

Duplicating imported templates is similar to duplicating Word documents.

1. Click on the Template you want to duplicate.
2. Click the **Save as Template** button in the corner.
3. Name the Template and click **Confirm.**

---

# Applying a Template

1. Navigate to **Data + Automations** > **Import + Export** > **Imports.**
2. Start a new Import and select **Data.**
3. Select a **Source** and **Upload the File.**
4. On the Mapping tab, click the **Load template** button. If it is a template you created, you will find it under Custom Templates.

---