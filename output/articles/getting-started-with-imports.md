---
title: Getting Started with Imports
url: https://help.element451.com/en/articles/9000459-getting-started-with-imports
collection: Data Management
---

Introduction to the Imports Feature.

# Overview

Importing People records is key to using Element451. This feature allows you to bring in important data points to use in all other features in Element451, like segment building, workflow conditions, and email personalization.

## Import Permissions

* **Access Import/Export**: The user has basic access to the import, export, and templates sections.
* **Administer Data Templates**: The user has access to create, edit, and delete import/export templates.
* **Administer Import/Export**: The user has access to create, edit, and delete import/export tasks.

[Read more on permissions →](https://help.element451.com/en/collections/3963257-permission-permission-groups)

## What Can Imports Do?

The Import feature is your tool to easily bring in large amounts of data on records without having to create each record manually.

* Create Parent, Student, and Influencer Records
* Bring in Test Scores
* Create Applications
* Update Records with Student IDs, Student Emails, Deposit and Enrollment information
* Upload Hold Information

## Features

* **Sources**: Identify and select the data file you want to import.
* **Update Preference**: Decide whether to create only new records, update existing ones, or both.
* **Matching**: Check incoming records against already existing records on a chosen identifier to prevent duplicate records in your instance.
* **Segments**: Import records directly into a segment.
* **Preview**: View the input/outputs of the first few records to ensure data quality.
* **Test Import**: Run the import without creating any records to review how many records would be updated, created, and skipped.

## Accessing Imports

To access **Import + Export**, navigate to **Data + Automations > Import + Export > Import + Export.**

---

# Import Management

The Import + Export screen is the main area for navigating between the import and export features and where you can see the comprehensive import + export tasks you and your team have created and run. On the import screen specifically, you can:

* View all imports you and your team create
* Manage your import tasks (edit, delete, duplicate)
* Apply quick filters to your import tasks
* Search for import tasks
* Assign import tasks to folders

[Import Management →](https://help.element451.com/en/articles/9000606-import-management)

---

# Creating Imports

Imports can be spun up quickly using pre-existing templates or can manually be set up.

[Creating Imports →](https://help.element451.com/en/articles/9001231-creating-imports)

---

# Column Setting Options

When creating imports and mapping the incoming data to fields in Element451, additional cleaning or transformations need to occur. Don’t worry about making names titlecase in your spreadsheet tool, Element451 can get it done.

[Column Setting Options →](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports)

---

# Data Quality Guide

Use this reference guide as you are building your imports to double-check that your data comes in clean the first time.

[Data Quality Guide →](https://help.element451.com/en/articles/9006443-data-quality-guide)

---

# Per-Contact Import History

The **Imports** card on a contact's profile shows every import that has included that contact, with timestamps and links to each import task. This is useful when investigating where a specific value on a record came from.

📙 *Note: If you don't see an Imports card on a contact's profile, an administrator will need to add it to the active [profile template](https://help.element451.com/en/articles/10471008-configuring-profile-templates).*

[Learn More: The Person Profile →](https://help.element451.com/en/articles/1475735-the-person-profile)

---

# Creating Document Imports

Along with data, you can also bring in documents and relate them to records.

[Creating Document Imports →](https://help.element451.com/en/articles/9011140-creating-document-imports)

---

# Decision Tree: Regular or System Data Source?

Below is a decision tree graphic designed to guide you on how to bring data into Element451. While it focuses on import tasks, the same steps can be applied to API use. This resource will help clarify the best practices for setting up custom fields and integrating your data sources efficiently.

*Click the image to enlarge:*

[![](https://downloads.intercomcdn.com/i/o/1191167433/90982defd2440b227d4c95d3/Data+Item+Import+Decision+Tree.png?expires=1784333700&signature=edd8673d25ffe479289520bc09970aa9be24071b916adae6d40aabfd882323b3&req=dSEuF8h4moVcWvMW1HO4zTOcXm6bXetp4V4nWz6jH57g8KRSHT2Fs%2F8j5Xmx%0AOWc14wGwy1B41tv5ADU%3D%0A)](https://downloads.intercomcdn.com/i/o/1191167433/90982defd2440b227d4c95d3/Data+Item+Import+Decision+Tree.png?expires=1784333700&signature=edd8673d25ffe479289520bc09970aa9be24071b916adae6d40aabfd882323b3&req=dSEuF8h4moVcWvMW1HO4zTOcXm6bXetp4V4nWz6jH57g8KRSHT2Fs%2F8j5Xmx%0AOWc14wGwy1B41tv5ADU%3D%0A)

---

# FAQ + Troubleshooting

### Can I import a student's secondary email address?

Secondary email is not an available field for imports. Instead, the secondary email is added to a profile during the merge process if the emails are different. To import a secondary email, we recommend creating a custom field. You can then use an email token to send it to that email address. Ensure that the field has email validation enabled.

---