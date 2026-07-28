---
title: Administrative Holds - Data Object
url: https://help.element451.com/en/articles/8704178-administrative-holds-data-object
collection: People
---

# Overview

Element451 has a specific data object for administrative holds. This feature helps to improve student engagement, success, and persistence by segmenting users with holds to provide personalized and timely communication.

📙 Note: The Hold data object in Element451 is read-only and intended to help with personalized and targeted engagement. Management of administrative holds will still need to be facilitated in your SIS.

---

# Accessing Hold Data in Element451

Hold data is displayed on the student profile on the Holds card. You must have the Holds card displayed on your profile template in order to view Hold data on the student profile. [Learn more about Profile Templates](https://help.element451.com/en/articles/1475735-the-person-profile).

1. Navigate to **Contacts** > **People** or use the search bar in the top right corner to search the student's name.
2. Locate the student you wish to view hold data for and click on their name to open the profile.
3. Look for the **Holds** card on the user profile. You can also search for it using the search bar.

   [![](https://downloads.intercomcdn.com/i/o/909010777/abfbd0cda523b14a3b9d138f/Screenshot+2023-12-13+at+8.51.39%E2%80%AFPM.png?expires=1784333700&signature=22d2baa5efdc59a1c8da1fb53ec52cfe5bf0990e133a6aa807262465633d99c9&req=fSAuFsh%2BmoZYFb4f3HP0gDpNzQPxXlfpdqS5SjjVSJahFAq0%2FuwflvRIGS20%0AE5s%3D%0A)](https://downloads.intercomcdn.com/i/o/909010777/abfbd0cda523b14a3b9d138f/Screenshot+2023-12-13+at+8.51.39%E2%80%AFPM.png?expires=1784333700&signature=22d2baa5efdc59a1c8da1fb53ec52cfe5bf0990e133a6aa807262465633d99c9&req=fSAuFsh%2BmoZYFb4f3HP0gDpNzQPxXlfpdqS5SjjVSJahFAq0%2FuwflvRIGS20%0AE5s%3D%0A)
4. To view more information about the hold data, expand the card by clicking the arrow.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/909011083/d51a6ad8a6f26f933fe5e089/Screenshot+2023-12-13+at+8.51.52%E2%80%AFPM.png?expires=1784333700&signature=ec4cbb244747f6c5720507f2163281f0eba941f954aff5242474ddf637f2a213&req=fSAuFsh%2FnYlcFb4f3HP0gIVlGTk4Ms7gpS8Ju0FK7sE%2F8X4tyZKEbMYMfcRh%0AHMM%3D%0A)](https://downloads.intercomcdn.com/i/o/909011083/d51a6ad8a6f26f933fe5e089/Screenshot+2023-12-13+at+8.51.52%E2%80%AFPM.png?expires=1784333700&signature=ec4cbb244747f6c5720507f2163281f0eba941f954aff5242474ddf637f2a213&req=fSAuFsh%2FnYlcFb4f3HP0gIVlGTk4Ms7gpS8Ju0FK7sE%2F8X4tyZKEbMYMfcRh%0AHMM%3D%0A)

---

# Importing Hold Data + Data Sources

To begin, make sure that your Hold data is in Element451.

There are three system sources- **Hold** **Status**, **Hold** **Type**, and **Hold** **Subtype**. When importing and mapping your data, you will need to use the corresponding system source fields listed below.

## [SYS] Hold Types

|  |  |  |
| --- | --- | --- |
| **System Data Source** | **Type** | **Code** |
| **Hold Type**  *user-holds-type-\** | Financial  Health  Academic  Conduct | FIN HEA ACD CON |

## [SYS] Hold Statuses

|  |  |  |
| --- | --- | --- |
| **System Data Source** | **Status** | **Code** |
| **Hold Status** ​*user-holds-status-\** | Active  Released | active  released |

## [SYS] Hold Subtypes

|  |  |  |  |
| --- | --- | --- | --- |
| **System Data Source** | **Subtype** | **Code** | **Hold Type** |
| **Hold Subtype** ​*user-holds-subtype-\** | Balance  Missing Payment Information  Documentation  Vaccine  Unsatisfactory Progress  Suspension  Expulsion | BAL INF DOC VAX UAP SUSP EXP | FIN FIN HEA HEA ACD CON CON |

## Other Hold Fields

You can also map data to the following text fields:

* Hold Description (*user-holds-description-\**)
* Hold Amount (*user-holds-amount-\**)
* Hold Start Date (*user-holds-start-date-\**)
* Hold End Date (*user-holds-end-date-\**)
* Hold Placed By (*user-holds-placed-by-\**)
* Hold Updated At (*user-holds-updated-at-\**)
* Hold Term (*user-holds-term-\**)
* Hold Subtype Description (*user-holds-subtype\_description-\**)

[Learn More: Importing](https://help.element451.com/en/articles/9000459-getting-started-with-imports)

---

# Creating a Segment with Hold Data

When adding filters to create a segment, you can use hold data properties.

For instance, if you wish to target students who have active financial-related holds, you can combine the filters as follows:

[![](https://downloads.intercomcdn.com/i/o/909013496/97a48833c65d842daef9e15e/Screenshot+2023-12-13+at+9.00.50%E2%80%AFPM.png?expires=1784333700&signature=a21cb3b8a5f8ba23cd8ffeb8bcd765c77938333d54b606da61c1fa6b3b687cd3&req=fSAuFsh9mYhZFb4f3HP0gLSbMCSJFpJ8FQEmBQYPZNgM0Wxdu4MVZlL3Pfys%0AsnfhUODydUPLbZMiqQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/909013496/97a48833c65d842daef9e15e/Screenshot+2023-12-13+at+9.00.50%E2%80%AFPM.png?expires=1784333700&signature=a21cb3b8a5f8ba23cd8ffeb8bcd765c77938333d54b606da61c1fa6b3b687cd3&req=fSAuFsh9mYhZFb4f3HP0gLSbMCSJFpJ8FQEmBQYPZNgM0Wxdu4MVZlL3Pfys%0AsnfhUODydUPLbZMiqQ%3D%3D%0A)

[Learn More: Filters + Segments](https://help.element451.com/en/collections/124543-filters-segments)

---

# Use Cases

**Personalized Communication**: You can tailor your outreach, providing students with specific, relevant information about their holds. This personalized approach not only fosters better engagement but also makes students feel more supported and understood.

**Proactive Intervention**: Having immediate access to hold data enables you to quickly identify and address issues that could impede a student's progress. This proactive intervention is crucial in preventing minor issues from escalating into major obstacles, thereby enhancing student success and retention.

**Efficient Resolution**: Real-time access to hold data streamlines the process of resolving holds, reducing students' time navigating administrative hurdles. This efficiency not only improves the overall student experience but also keeps students on track for the timely completion of their academic goals.

---