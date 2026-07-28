---
title: Star (*) Mappings
url: https://help.element451.com/en/articles/9745028-star-mappings
collection: Data Management
---

[![The Element451 Help Center](https://downloads.intercomcdn.com/i/o/459207/a300afa4340c54d3e6feb919/0773d5d71431701d7fa15561a49c7fdf.png)](/en/)

Search for articles...

# Star (\*) Mappings

Learn how to use Import + Export mappings that end in a asterisk.

# Overview

In the Imports + Exports module, you might notice certain column mapping options ending with an asterisk (\*). We call these ***star mappings***—because, well, they shine a little brighter 🌟.

But what makes them special? The asterisk indicates that these mappings can be *scoped* to a specific object within the repeater targeted by the mapping.

Wait…what’s a scope? And what’s a repeater? Don’t worry—we’ll break it all down for you. Let’s get started!

---

# Understanding the Element451 Data Model

To make the most of star mappings, it’s helpful to understand how Element451 stores and organizes data—and how mappings interact with it.

Before diving in, ensure you’re familiar with [Element451’s Data Model](https://intercom.help/element451/en/articles/9824701-the-element451-data-model), particularly the concepts of ***repeaters*** and Import + Export ***mappings***. These fundamentals will provide the context you need to use star mappings effectively.

---

# What are Scopes?

Scopes tell mappings which specific repeater to target within the data.

Let’s revisit the example `user-applications-major` from the [Element451 Data Model article](https://intercom.help/element451/en/articles/9824701-the-element451-data-model). This mapping requires a single scope: the application’s “type,” corresponding to the `app_type` attribute in the data structure.

[![](https://downloads.intercomcdn.com/i/o/1147259445/d227a7b40ab5323ee659ddc3/Screenshot+2024-08-15+at+3_06_18%E2%80%AFPM.png?expires=1784333700&signature=14992a64870db4a5d66d84260c7fc5d7710ab2a3f3491062bd0743dfa14891b9&req=dSEjEct7lIVbXPMW1HO4zT7hPihU01WiAQxNrdAd1zsM9h6jwRlXZDDJmtM0%0AhBVnbeeDqZwVxJzFsQQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1147259445/d227a7b40ab5323ee659ddc3/Screenshot+2024-08-15+at+3_06_18%E2%80%AFPM.png?expires=1784333700&signature=14992a64870db4a5d66d84260c7fc5d7710ab2a3f3491062bd0743dfa14891b9&req=dSEjEct7lIVbXPMW1HO4zT7hPihU01WiAQxNrdAd1zsM9h6jwRlXZDDJmtM0%0AhBVnbeeDqZwVxJzFsQQ%3D%0A)

For instance, if the Application scope is declared, the `user-applications-major` mapping will match the first application object where the `app_type` attribute matches the scope.

```
{  
  registration_id: "849F3PO",  
  app_type: "Incoming Freshman"  
  major: "Dancing",  
  term: "Fall",  
  student_type: "Freshman",  
  index_weight: 1  
},
```

But what happens if multiple applications share the same `app_type`—for example, two applications both labeled as “Incoming Freshman”?

In cases like this, we need more precision. That’s where star mappings come in.

By using a star mapping field like `user-applications-major-*`, you can match based on **one or more properties** of the application. The system will locate the **first** application object that satisfies ***all*** specified scopes.

[![](https://downloads.intercomcdn.com/i/o/1147259446/0da3a1601b2394d08d4fb872/Screenshot+2024-08-15+at+3_23_33%E2%80%AFPM.png?expires=1784333700&signature=7849d15074271672b0a96fd95443f66bd3cbdb43f2f8e4ec5083d1493252072a&req=dSEjEct7lIVbX%2FMW1HO4zVQtCjqjeFS2xvyFcx6heBJbgWOQ0v19EOlZE5U%2B%0AFHGlrZG6CsOcD6NykDI%3D%0A)](https://downloads.intercomcdn.com/i/o/1147259446/0da3a1601b2394d08d4fb872/Screenshot+2024-08-15+at+3_23_33%E2%80%AFPM.png?expires=1784333700&signature=7849d15074271672b0a96fd95443f66bd3cbdb43f2f8e4ec5083d1493252072a&req=dSEjEct7lIVbX%2FMW1HO4zVQtCjqjeFS2xvyFcx6heBJbgWOQ0v19EOlZE5U%2B%0AFHGlrZG6CsOcD6NykDI%3D%0A)

---

# Using Scopes with Star Mappings

## Scope Options

Star mappings allow you to define one or more scopes to specify the target object. Here are the scoping options:

* **Type:** Defines the type of the target object (e.g., application type, milestone type, or test type).
* **Position:** Refers to the object’s position in its repeater array, identified by the **index\_weight** property.
* **Term:** Specifies the term an application is for (available in `user-applications-*` mappings).
* **Major:** Indicates the major associated with an application (available in `user-applications-*` mappings).
* **ZIP Code:** Available in `user-school-*` and `user-address-*` mappings.
* **Registration ID:** Available in `user-applications-*` mappings.

## Repeaters with Star Mappings

The following repeaters support star mapping options:

* `user-addresses-...`
* `user-applications-...`
* `user-education-...`
* `user-emergency-contacts-...`
* `user-family-...`
* `user-holds-...`
* `user-milestones-...`
* `user-sources-...`

## Pre-scoped Mappings

Unlike star mappings, which are fully customizable, pre-scoped mappings come with a predefined scope.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1345290906/1e5cfceffa0c38b25a178adbfe8f/Note.png?expires=1784430000&signature=7bb404b55371dad2d707dd8ab1ddada43cb60010368ccdb23c649e668a130124&req=dSMjE8t3nYhfX%2FMW3Hu4gUoibcHP%2ByoW5Shx3vbJcGEyr1%2FDc53T3OG9yjWP%0AtA%3D%3D%0A) Pre-scoped mappings are still available in the Import module but are deprecated. It’s recommended to use star mappings wherever possible.

For example:

* `user-addresses-city-*` allows you to specify an address scope, such as “home” or “mailing.”
* `user-adressess-home-city` is a **pre-scoped** version that applies only to the “home” address type.

Similar pre-scoped examples exist for **evaluation types**, **school types** (e.g., `user-education-*`), and **family members**.

---

# Star Mapping Examples

Here are some common examples where star mappings are used.

## Example 1: Importing Historic Applications, One Row per Contact

In this example, we'll see one way star fields can be used to import multiple applications per row of the data file. This example is also discussed in our Importing Application Data article, [here (option 2)](https://help.element451.com/en/articles/9007767-importing-application-data#h_2c5b05db7f).

## Example Data File

Let's imagine a data file where each row represents one contact. In the first column, we might have their ID, in the second their email and so on. In columns 33-38, we'll have data for their first application. In columns 39-44, data for a second application. We want to import the data from both applications.

## Mapping

For columns 33-38, we'll map each column to it corresponding field in Element using the star fields. 33 is term, so it maps to `user-applications-term-*.` 34 is major, so `user-applications-major-*` and so on. This set of columns corresponds to the students first application, so we'll simply scope it to position 1. For columns 39-44, we'll use the same mappings but scope to position 2.

## Expected Results

After running the import task, contacts should be created in Element451. Contacts should have the same number of applications as they had data for. If one contact only had data in columns 33-38, they should have one application listed on their Applications profile card. If another contact had data in columns 33-38 and 39-44, they should have two applications listed on their card.

## Explanation

Importing historic applications usually occurs when first implementing Element451, so we can assume that these data files will create new contacts in Element. Since these contacts are new, we don't need to worry about overwriting existing data. Simply mapping to position will suffice. We can repeat this process for as many sets of columns as needed.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1345293518/5a1bc66dbfd735f505a97e2ed9ef/Pro+Tip.png?expires=1784430000&signature=c19c07f59532bc944bc7c3aae1b0bedd87896d954396e45e47cbb1df0e863158&req=dSMjE8t3noReUfMW3Hu4gXLd2rG5kI5qT37mJ7vIvR1M3Of6bXmrs1LjB%2B0c%0Alg%3D%3D%0A) This same strategy applies to all of the other [repeaters](https://help.element451.com/en/articles/9745028-star-mappings#h_fbdc4267b2) listed. In fact, creating a data file with one row per contact is the preferred format for Imports.

## Example 2: Scoping to an Application by Term and Type

Type and Term are the most common scopes for Application mappings. Using them is the recommended method of matching a single application across multiple import tasks.

## Example Data File(s)

In this example, we have two data files. Both correspond to an undergraduate application type for fall 2024.

In the first, each row represents one contact and contains data about an application they have started. In the first column, we might have their ID, in the second their email and so on. In column 20, we have the term for which they have started an application, and in column 21, we have their major.

The second file also has one contact per row, but it contains additional information about the application that the student provided upon submission. We still have their student ID in column 1 to identify them, but now, in column 35, we have their student type, and in 36, the campus where they want to study.

The goal is to write the data from file 2 to the same application created by file 1.

## Mapping

In file 1, we'll map column 20 to `user-applications-term-*`, and column 21 to `user-applications-major-*`. For both, we'll scope the Application Type to "Undergraduate Application," as it's named in Element451. We'll also scope the Term to "Fall 2024."

In file 2, we'll map column 35 to `user-applications-student-type-*` and column 36 to `user-application-campus-*`. Just like file 1, we'll scope the Type to "Undergraduate Application" and the Term to "Fall 2024."

## Expected Results

After the first import task is run, we would expect contacts from the file to have one application on their Application profile card for Undergraduate Application, with a term of Fall 2024. The Major of that application should also be populated, but other fields should be blank.

After the second import task is run, we would expect contacts from the file to still have one application on their profile card for Undergraduate Application and Fall 2024, but now with more data, such as student type and campus.

## Explanation

This process works because we know the application type and term is consistent for all contacts in both files. We can assume that existing contact's application data won't be overwritten because they have not had an application of this type from this term before. While other applications may exist on their record, none of them match that type and term combination.

In a given data file, if the type and term are varied, you will likely need to split that data file by type and term, creating a unique file for each type and term combination.

## Example 3: Exporting Student's School & Evaluation Data

It is common to export a student's high school, college, and test data when sending data from Element451 to another system. Repeating on Schools and Evaluations is effective, but produce two files. This example assumes a single export file is required.

## Example Data File

In this example, we'll create a single file that repeats on the User (one row per student). We'll assume the contact and demographic data has already been mapped, and we now need to map the student's first and second high school, first and second college, and ACT scores.

## Mapping

Beginning at the next available column of the export task, we'll map the following.

1. `user-education-schools-ceeb-*`
2. `user-education-schools-gpa-*`
3. `user-education-schools-ceeb-*`
4. `user-education-schools-gpa-*`
5. `user-education-schools-ceeb-*`
6. `user-education-schools-gpa-*`
7. `user-education-schools-ceeb-*`
8. `user-education-schools-gpa-*`
9. `user-evaluations-composite-score-*`

Notice that `user-education-schools-ceeb-*` and `user-education-schools-gpa-*` are repeated four times. This corresponds to the four schools we wish to export.

We'll set the scope of the first set of `ceeb-*` and `gpa-*` mappings as:

* School Type = Highschool
* Position = 1

[![](https://downloads.intercomcdn.com/i/o/1185859223/3a355d43c5bef62d036218f0/Screenshot%2B2024-09-16%2Bat%2B11_22_57-E2-80-AFAM.png?expires=1784333700&signature=2560de8b0f29a43d23faa886760cfc1dadfcbd050884db940586bec16552b64b&req=dSEvE8F7lINdWvMW1HO4zRjThdPCsJm1HZEpEXiQfA9l6xsj%2BdkXb2pXqmTV%0AaVhRlYrxeXleKKJPxDI%3D%0A)](https://downloads.intercomcdn.com/i/o/1185859223/3a355d43c5bef62d036218f0/Screenshot%2B2024-09-16%2Bat%2B11_22_57-E2-80-AFAM.png?expires=1784333700&signature=2560de8b0f29a43d23faa886760cfc1dadfcbd050884db940586bec16552b64b&req=dSEvE8F7lINdWvMW1HO4zRjThdPCsJm1HZEpEXiQfA9l6xsj%2BdkXb2pXqmTV%0AaVhRlYrxeXleKKJPxDI%3D%0A)

Then repeat this process for the remaining sets of schools, modifying the School Type and Position scopes as necessary.

The `user-evaluations-composite-score-*` mapping should be scoped to:

* Type = ACT

## Expected Results

After running the Export Task, the resulting file should have one row per student and should output student's schools and ACT score as configured. A student with only one highschool on record should have null values for the high school 2 and college columns.

##

---