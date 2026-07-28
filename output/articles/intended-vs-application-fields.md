---
title: Intended vs Application Fields
url: https://help.element451.com/en/articles/2582913-intended-vs-application-fields
collection: Data Management
---

What is the difference between Intended and Application Fields

# Overview

In Element451, the **Intended** and **Application** fields help identify a student's status in the enrollment process. These fields distinguish between what students plan to study (Intended) and what they have officially applied for (Application).

---

# Intended Fields

* Designed to be used at the **prospect** stage (e.g., when a student submits a request for information form, registers for an event, etc.).
* Capture what the student *intends* to study and the term they intend to enroll.
* Can be added to **Forms** and **Event registrations**.

## Where to Find Intended Fields

* **Student** **Profile** → **More** **Data** → **Academic**
* **Student** **Profile** → **Header (or Sidebar)**

  + To appear in the header or sidebar, they must be added to your profile template. You can learn how to customize profile templates in [this article](https://help.element451.com/en/articles/10471008-configuring-profile-templates).

## List of Intended Fields

|  |  |
| --- | --- |
| **Label** | **Slug** |
| Intended Campus | user-education-campus |
| Intended Degree | user-education-degree |
| Intended Major | user-education-prefered-major |
| Intended School | user-education-intended-school |
| Intended Student Type | user-education-student-type |
| Intended Term | user-education-term |

---

# Application Fields

* Designed to be used at the **application** stage when a student submits an application.
* These fields are only available for Applications and capture official data related to a student’s application.

For more information on how applications are stored on the student profile, check out our help article, [The Element451 Data Model](https://help.element451.com/en/articles/9824701-the-element451-data-model).

## Where to Find Application Fields

* **Decisions** module
* **Student** **Profile** → **More** **Data** → **Applications**
* **Student** **Profile** → **Application Card**

  + If the application card is not visible, you may need to add it to your profile template. You can learn how to customize profile templates in [this article](https://help.element451.com/en/articles/10471008-configuring-profile-templates).

![Note](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1514969018/d6a8bad98af23c3c20d51b03abbf/Note.png?expires=1784430000&signature=43e46f0abceb5802285954da9c5c318043e41c5ac1072cc462bf5d1be6f52abb&req=dSUmEsB4lIFeUfMW3Hu4gQ8zLpNHKiqArGLiKRrbvz4j4VzeE7oDaf4CBwy4%0AmA%3D%3D%0A) Application Fields cannot be added to the header or sidebar of the student profile because they are scoped to an individual application, and a student may have more than one.

## List of Application Fields

|  |  |
| --- | --- |
| **Label** | **Slug** |
| Application Campus | user-applications-campus |
| Application Concentration | user-applications-concentration |
| Application - Degree | user-applications-degree |
| Application - Housing Interest | user-applications-housing |
| Application Major | user-applications-major |
| Application Minor | user-applications-minor |
| Application Second Major | user-applications-major-second |
| Application Student Type | user-applications-student-type |
| Application Term | user-applications-term |
| Application Third Major | user-applications-major-third |

---

# What About "Active" Fields?

An "active" field, such as `Active Major`, is a Trait. Traits are **calculated** by Element451 and updated when data is added to the Person record, reflecting the most current or relevant attribute values.  
​  
One of the most frequently asked questions is how to choose between “Active Term” and “Application Term” in Segments. [You can read more about that topic here](https://help.element451.com/en/articles/6960851-traits#h_ca0e1ccb76).

---