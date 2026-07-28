---
title: Filters: All Properties | Has + Does Not Have
url: https://help.element451.com/en/articles/7024581-filters-all-properties-has-does-not-have
collection: People
---

Learn how to apply advanced segment filters.

# Overview

Filters are essential for creating segments in Element451. By using different filter combinations, you can include or exclude attributes and behaviors of a person to generate a specific segment of person profiles.

In this article, we will discuss advanced segment filters by combining "All Properties" with HAS and DOES NOT HAVE operators.

---

# All Properties

Within Element, there are several data groups that feature an **All Properties** filter option. These filters enable you to select specific conditions based on multiple properties associated with that data. For instance, if you use the Address (All Properties) filter, you can filter for a particular state and specific county in one filter.

The All Properties filters allow you to **include** or **exclude** multiple properties into one segment filter by using the **HAS** and **DOES** **NOT** **HAVE** operators.

Additionally, you can combine multiple filters using **ANY** and **ALL** operators to create highly targeted and robust segments within Element. [Learn more about Any and All Operators by reading this article](https://help.element451.com/en/articles/3648165-filters-all-any-operators).

Data Groups that contain the **All Properties** filter are:

|  |  |  |
| --- | --- | --- |
| * Address * Application * Athletic * Birthday * College * Document Request * Emergency Contact * Employment | * Evaluation * Event * Extracurricular Activity * GPA * High School * Hold * Identity * Journey | * Milestone * Note * Phone * Program * School * Source |

To find an **All** **Properties** filter, you can use the Find Filter search feature or scroll the list to locate a filter with All Properties in parenthesis.

[![](https://downloads.intercomcdn.com/i/o/907794462/deea6630afdbd288a252fac6/Screenshot+2023-12-12+at+2.33.07%E2%80%AFPM.png?expires=1784333700&signature=5d4672036db6a4584e13ff9c398dc39e8a3d4919d3cf3e7e865cf1f594f2d626&req=fSAgEcB6mYddFb4f3HP0gD1bmgD4CjuQg2X9DYOEl9pCKQSKbwBNeBPgcaVn%0AXe%2FA2V20Piy8zE2nJw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/907794462/deea6630afdbd288a252fac6/Screenshot+2023-12-12+at+2.33.07%E2%80%AFPM.png?expires=1784333700&signature=5d4672036db6a4584e13ff9c398dc39e8a3d4919d3cf3e7e865cf1f594f2d626&req=fSAgEcB6mYddFb4f3HP0gD1bmgD4CjuQg2X9DYOEl9pCKQSKbwBNeBPgcaVn%0AXe%2FA2V20Piy8zE2nJw%3D%3D%0A)

---

# HAS vs. DOES NOT HAVE

Within any **All Properties** filter, you can group filters within a property to generate a segment using the **HAS** or **DOES NOT HAVE** operator.

* **HAS**: Use when you want to include only those users who match specific property attributes in your segment. This operator ensures that your segment consists of users who possess the characteristics or details you've chosen.
* **DOES NOT HAVE**: Use when you aim to exclude users with certain property attributes from your segment. This operator filters out users who have the specific characteristics or details you wish to avoid.

For example, the screenshot below illustrates using the **All Properties** filter and the **HAS** operator. This filter will create a segment that **includes** users with an application that meets all the following criteria:

* The **Term** is **Fall 2022**
* The **Application Status** is **Submitted**
* The **Student Type** is **Freshman**

If we use the **DOES NOT HAVE** operator instead, the filter will return users that have an application but that application fails to meet all three filter criteria.

* The Term **IS NOT** Fall 2022
* The Application Status **IS NOT** Submitted
* The Student Type **IS NO**T Freshman
* Additionally, the list will also include records with no applications at all.

[![](https://downloads.intercomcdn.com/i/o/678385792/eae98b87247e3b9cd7e9e670/status.png?expires=1784333700&signature=489fd2c7668e6444d4fa535b7389fb3779d2480a31751ac3074c97e2f94693e2&req=cicvFcF7mohdFb4f3HP0gJphrbzuBbS7EG35ztt%2FXzp1ZDgnYwih78eI64B6%0AwRECC5GYIsyCdXno2w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/678385792/eae98b87247e3b9cd7e9e670/status.png?expires=1784333700&signature=489fd2c7668e6444d4fa535b7389fb3779d2480a31751ac3074c97e2f94693e2&req=cicvFcF7mohdFb4f3HP0gJphrbzuBbS7EG35ztt%2FXzp1ZDgnYwih78eI64B6%0AwRECC5GYIsyCdXno2w%3D%3D%0A)

***💡 Pro Tip:*** Consider reading the segment conditions as a sentence to understand better how your segment will function. For the examples above:

* <Find people that> **Has** an application <with> this term, status, and student type associated with it.
* <Find people that> **Does Not Have** an application <with> this term, status, and student type associated with it.

---

# Additional Use Case Example

Suppose you would like to send an email campaign to users with **submitted applications *and*** **have not yet registered for a specific visit day event**.

You can combine filters and operators to narrow down your user list accordingly.

1. Use the **Application (All Properties)** filter  
   ​
2. Use the HAS operator to include users who have submitted an application for the current term using these properties:

   * Status = Submitted
   * Term = Fall 2022  
     ​

   [![](https://downloads.intercomcdn.com/i/o/678401422/5e7e9ee0aeda979b97ea02ba/applicaiton_props.png?expires=1784333700&signature=4d360ddd89b2f72a890313dcd1fb6d808eef8d64ec9441c48b1354c2354e253b&req=cicvEsl%2FmYNdFb4f3HP0gK7m8x8yJQc0Z8FpyyyOJcNBe32TAhgKT4Xf%2FS0R%0AvMA%3D%0A)](https://downloads.intercomcdn.com/i/o/678401422/5e7e9ee0aeda979b97ea02ba/applicaiton_props.png?expires=1784333700&signature=4d360ddd89b2f72a890313dcd1fb6d808eef8d64ec9441c48b1354c2354e253b&req=cicvEsl%2FmYNdFb4f3HP0gK7m8x8yJQc0Z8FpyyyOJcNBe32TAhgKT4Xf%2FS0R%0AvMA%3D%0A)
3. Then, add an additional filter, **Event (All Properties)**   
   ​
4. Use the HAS NOT operator to include users who have not registered for Campus Visit Day

   * Event Name = Campus Visit Day

   [![](https://downloads.intercomcdn.com/i/o/678401096/8862dff5a270b452a0a41209/events.png?expires=1784333700&signature=f67b9278d9c39a116f1c177fcb8c4a2a8be518035aea7d9a1758e46ebefa26f1&req=cicvEsl%2FnYhZFb4f3HP0gBrA073fcVct0Ju3dRLO5eDaZJMqvQRfPbCgvYFH%0AaI4%3D%0A)](https://downloads.intercomcdn.com/i/o/678401096/8862dff5a270b452a0a41209/events.png?expires=1784333700&signature=f67b9278d9c39a116f1c177fcb8c4a2a8be518035aea7d9a1758e46ebefa26f1&req=cicvEsl%2FnYhZFb4f3HP0gBrA073fcVct0Ju3dRLO5eDaZJMqvQRfPbCgvYFH%0AaI4%3D%0A)
5. Once you apply the additional filter, you will notice that it groups the two filters together with the ALL operator. This requires the criteria outlined in both filters to be matched in order for a user to be included.

   [![](https://downloads.intercomcdn.com/i/o/678501950/58cdc7c76e2e72ccda549044/submitted_apps.png?expires=1784333700&signature=813a3c1fa4cedca79c38fe63036dfb0452ca70279aafd1af0615ea79101c4f25&req=cicvE8l%2FlIRfFb4f3HP0gINnLz35jDITGlLcWykNX9nhobUMC83ERV4J6Chz%0ALKA%3D%0A)](https://downloads.intercomcdn.com/i/o/678501950/58cdc7c76e2e72ccda549044/submitted_apps.png?expires=1784333700&signature=813a3c1fa4cedca79c38fe63036dfb0452ca70279aafd1af0615ea79101c4f25&req=cicvE8l%2FlIRfFb4f3HP0gINnLz35jDITGlLcWykNX9nhobUMC83ERV4J6Chz%0ALKA%3D%0A)

The resulting segment will be those with submitted applications for the Fall 2022 term who have not registered for the Campus Visit Day event.

---

# Common Mistakes

Users commonly think that using **HAS** combined with **IS NOT** or **NOT IN** is the same as **DOES NOT HAVE** combined with **IS** or **IN**. Let's look at another simple example of this:

Scenario: You want all users who have not registered for an upcoming open house.

Using the **Event (All Properties)** filter**:**  
​  
🟢 CORRECT

**[Event (All Properties] [DOES NOT HAVE] [EVENT NAME] [IS] [OPEN HOUSE]**

Explanation: This will include users with no event registrations AND those with an event registration for an event with a name other than *Open House*.  
​

🔴 INCORRECT

**[Event (All Properties] [HAS] [EVENT NAME] [IS NOT] [OPEN HOUSE]**

Explanation: This will only include users who have registered for an event that is not named *Open House*.

---