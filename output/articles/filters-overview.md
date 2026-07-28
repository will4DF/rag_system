---
title: Filters Overview
url: https://help.element451.com/en/articles/1476084-filters-overview
collection: People
---

Introduction to the power of filters for creating segments and searching for people.

*Available in **Element Core**. See [our packages overview](https://help.element451.com/en/articles/11428377-understanding-element451-packages) for details.*

---

# Overview

In Element451, Filters are the core of how Segments are created, as they help narrow down groups of people based on specific conditions that you set up and combine.

Using Filters, Segments can provide valuable information about your prospects, applicants, admits, and enrolled students. Filters also enable you to send personalized communications and content to your target audience.

[![](https://downloads.intercomcdn.com/i/o/900547383/8291868f14c4f8b848716cb8/Filters.gif?expires=1784333700&signature=41fdd6beac9ef8432ebd46c15e9cc1a89a2ad9ac9f2f1d245c1a9861ae69cd9d&req=fSAnE815nolcFb4f3HP0gODxxENKbdm52PTedvBIywdnFJMfl%2FjIIc7Csisr%0AfE03DWCycAfGxdTcFQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/900547383/8291868f14c4f8b848716cb8/Filters.gif?expires=1784333700&signature=41fdd6beac9ef8432ebd46c15e9cc1a89a2ad9ac9f2f1d245c1a9861ae69cd9d&req=fSAnE815nolcFb4f3HP0gODxxENKbdm52PTedvBIywdnFJMfl%2FjIIc7Csisr%0AfE03DWCycAfGxdTcFQ%3D%3D%0A)

---

# Filter Groups + Subgroups

Grouping filters allow you to create specific clusters of criteria. For example, in scholarship searches, you might have academic, financial, and extracurricular criteria. Grouping keeps each category organized. Then, you can decide how these groups relate to each other using logical connectors.

Filter grouping is introduced by adding 2+ filters. Continue reading to learn about adding filters.

*📙 Note: Filters of different Types cannot be combined into the same group, and their default behavior is ALL. For example, you cannot combine Application Student Type and Decision Status filters in the same grouping because they are defined in separate Types- **Users** and **Decisions**.*

---

# Adding Filters

## Adding the First Filter

1. Navigate to **Contacts** > **People**
2. Click the **"Add Filter"** button (as illustrated in the gif above).
3. Select a filter from the list or use the **Find Filter** bar to search for a filter. You can also narrow the list by choosing a Type from the drop-down menu at the top. A list of filter Types with descriptions are listed below in the next section.
4. Once you have selected the filter, you can **add conditions**.
5. Most conditions require a **constraint operator**(s) and **value**. Constraint operators and values will vary depending on the data. [Click here to learn more about constraint operators](https://help.element451.com/en/articles/1476149-filters-constraint-operators). Also, note that text field values are case-sensitive.
6. When you are finished configuring your condition(s), click **Submit**.
7. After adding the first filter, you can add additional filters to continue building upon your segment of users. [Steps for this are outlined in the next section](https://help.element451.com/en/articles/1476084-filters-overview#h_fa5283f398).
8. If you're finished adding filters, click apply to update your user list, clear it, or save it **as a new segment**.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/900688862/bb834248f5049b1f94c0acc5/Filter+Apply.png?expires=1784333700&signature=b01233616094b87d80a4406b7ecee4574eb82f4f4e036158953465813d133b9c&req=fSAnEMF2lYddFb4f3HP0gBKzt3sHBS%2BsDChQmAA3GaiUJg4XVfIAHFrx9gOV%0ApI0%3D%0A)](https://downloads.intercomcdn.com/i/o/900688862/bb834248f5049b1f94c0acc5/Filter+Apply.png?expires=1784333700&signature=b01233616094b87d80a4406b7ecee4574eb82f4f4e036158953465813d133b9c&req=fSAnEMF2lYddFb4f3HP0gBKzt3sHBS%2BsDChQmAA3GaiUJg4XVfIAHFrx9gOV%0ApI0%3D%0A)

## Adding Additional Filters

After adding the first filter, you can add additional filters to continue building upon your segment of users. In doing so, you will introduce filter grouping (as described above) and advanced logic that uses ANY + ALL operators.

To add a second filter, click **Add Filter** and follow the same steps as you did in adding your first filter.

## Same Filter Type

If the second filter you add is the **same Type** as the first, it will look something like the screenshot below:

[![](https://downloads.intercomcdn.com/i/o/900764281/8f00c02b87610c6c9610e401/Filters+-+Same+Type.png?expires=1784333700&signature=d2f304efa027334f3615c84ecdd2f94ff4135f6c8c8d99e17904aa7cc6b9e912&req=fSAnEc96n4leFb4f3HP0gL7oGwwEri6GOZBvtZaqby0AwWxuBXfFhpzMNAWj%0ALDtrMTZjqB3ruGZNeg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/900764281/8f00c02b87610c6c9610e401/Filters+-+Same+Type.png?expires=1784333700&signature=d2f304efa027334f3615c84ecdd2f94ff4135f6c8c8d99e17904aa7cc6b9e912&req=fSAnEc96n4leFb4f3HP0gL7oGwwEri6GOZBvtZaqby0AwWxuBXfFhpzMNAWj%0ALDtrMTZjqB3ruGZNeg%3D%3D%0A)

Now let's talk about this example in a bit more depth:

* We added a filter for *Intended Campus* and *Application Major*. A group was formed because both are associated with the User filter type (indicated by the blue color).
* A group is denoted by a light gray box encompassing the filters.
* Because they are in a grouping, you can change the **All** operator to the **Any** operator by using the drop-down in the top left corner, depending on if you want the user to meet all the criteria within the group or just one of the criteria. [You can learn more about All + Any Operators here](https://help.element451.com/en/articles/3648165-filters-all-any-operators).
* We have the **application major** filter, but let's say we also want to pull in the **intended major**. We can create a subgroup to achieve this.

  1. Hover over the filter you wish to add to and click the **plus sign**.

     [![](https://downloads.intercomcdn.com/i/o/900774766/2033c130eea707cc539b3d2d/Subgroup.png?expires=1784333700&signature=4db8f801853981fd63407565b4ab204f56edfddc9993241165d8b90389466b67&req=fSAnEc56modZFb4f3HP0gNGZ%2FAQqlXcFPGy2EboVjK%2FoPkEfrKx%2F2pcr5XFZ%0AlAo%3D%0A)](https://downloads.intercomcdn.com/i/o/900774766/2033c130eea707cc539b3d2d/Subgroup.png?expires=1784333700&signature=4db8f801853981fd63407565b4ab204f56edfddc9993241165d8b90389466b67&req=fSAnEc56modZFb4f3HP0gNGZ%2FAQqlXcFPGy2EboVjK%2FoPkEfrKx%2F2pcr5XFZ%0AlAo%3D%0A)
  2. Find the filter you wish to add and configure as needed; in this case, we are adding **Intended Major**. Note: Only filters corresponding to this **Type** will populate. It should look something like the screenshot below.

     + Notice that a new gray rectangle was formed within the original one— we call this a subgroup.
     + You should also notice that since it is a separate group now, it has its own All/Any operator. For this example, we selected Any because we want the student to match only one.

       [![](https://downloads.intercomcdn.com/i/o/900777974/8b392a793215fbedec0eb5fe/Subgrouping.png?expires=1784333700&signature=cf762b6195b8d460f570d20b72b7a4b1603830468c862fe313d39fad8e96a336&req=fSAnEc55lIZbFb4f3HP0gCeldT6xprCb5Iw5E2R9UH0pSBNq0a3671FLYV6S%0A6vI%3D%0A)](https://downloads.intercomcdn.com/i/o/900777974/8b392a793215fbedec0eb5fe/Subgrouping.png?expires=1784333700&signature=cf762b6195b8d460f570d20b72b7a4b1603830468c862fe313d39fad8e96a336&req=fSAnEc55lIZbFb4f3HP0gCeldT6xprCb5Iw5E2R9UH0pSBNq0a3671FLYV6S%0A6vI%3D%0A)

## Different Filter Type

If the second filter you add is a **different** **type** from the first, it will look something like the screenshot below:

[![](https://downloads.intercomcdn.com/i/o/900764606/e5ed8d94757d401745b18bbd/Filter+Different+Types.png?expires=1784333700&signature=3febe480d96e1f202b5ee7586803395bfccc0579c3369099456a763aafdc65e7&req=fSAnEc96m4FZFb4f3HP0gHq9%2FxxcaCYbmmi1yBMnjyxuTLTzg0ZEoHzWEmFS%0Ab%2FMJwO3qpeEGu1H3zA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/900764606/e5ed8d94757d401745b18bbd/Filter+Different+Types.png?expires=1784333700&signature=3febe480d96e1f202b5ee7586803395bfccc0579c3369099456a763aafdc65e7&req=fSAnEc96m4FZFb4f3HP0gHq9%2FxxcaCYbmmi1yBMnjyxuTLTzg0ZEoHzWEmFS%0Ab%2FMJwO3qpeEGu1H3zA%3D%3D%0A)

Now let's talk about this example in a bit more depth:

* We added a filter for *Intended Campus* and *Decision Status*. Because the two are associated with different Types, you will notice that they are not grouped. Therefore, by default, it will use the ALL logic, retrieving all records that have the values *Element Web* for their Intended Campus **AND** *Admitted* for their Decision status.
* From this point, you can add additional filters by clicking Add Filter. Adding a filter associated with a Type that already exists will automatically create a group. For example, a group would be formed if we added Intended Major = Accounting because it's also a User Type filter along with Intended Campus.   
  ​

  [![](https://downloads.intercomcdn.com/i/o/907776316/9d0bf5741f7666f9c3a7b7f0/Screenshot+2023-12-12+at+2.09.06%E2%80%AFPM.png?expires=1784333700&signature=ea8ad55859a626a445c607b9953af38a557cbb3baee431be48ecc4049f9940ab&req=fSAgEc54noBZFb4f3HP0gJF0avbsmb%2BCzBg4O6K1DyNIE7JlSPU9K9TJ2hJr%0AVAE%3D%0A)](https://downloads.intercomcdn.com/i/o/907776316/9d0bf5741f7666f9c3a7b7f0/Screenshot+2023-12-12+at+2.09.06%E2%80%AFPM.png?expires=1784333700&signature=ea8ad55859a626a445c607b9953af38a557cbb3baee431be48ecc4049f9940ab&req=fSAgEc54noBZFb4f3HP0gJF0avbsmb%2BCzBg4O6K1DyNIE7JlSPU9K9TJ2hJr%0AVAE%3D%0A)

**Once you have added filters, you can perform the following actions:**

* **Apply:** update your user list
* **Clear**: clear all your filters and start over
* **Save as a New Segment**: save your filtered list as a new segment

[![](https://downloads.intercomcdn.com/i/o/900671533/9da2b0d94eede747b5ebdf70/Filter+Apply.png?expires=1784333700&signature=b7a07f105b2a58407403fbb21f09bcfd7615feed5895762ff373962512d58231&req=fSAnEM5%2FmIJcFb4f3HP0gEtBsTPllSbP4VHnncWiJ0nMVluNaEmpkJ0uy6UG%0AwOGyng1u8oUL74fsgw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/900671533/9da2b0d94eede747b5ebdf70/Filter+Apply.png?expires=1784333700&signature=b7a07f105b2a58407403fbb21f09bcfd7615feed5895762ff373962512d58231&req=fSAnEM5%2FmIJcFb4f3HP0gEtBsTPllSbP4VHnncWiJ0nMVluNaEmpkJ0uy6UG%0AwOGyng1u8oUL74fsgw%3D%3D%0A)

---

# Filter Property Types

All filters are categorized by a Property Type. There are eight different Property Types— Users, Activity, Relationships, Tasks, Decisions, Documents, Surveys, and Appointments.

[Learn More: Property Types](https://help.element451.com/en/articles/8800347-filters-property-types)

---

# Any + All Operators

There is a small dropdown menu in the top left of your filters.The options here are "All" and "Any," and they act as "and" and "or" logic operators.

[Learn More: Any + All Operators](https://help.element451.com/en/articles/3648165-any-vs-all-operators-segment-builder)

---

# Constraint Operators

Constraint operators are the specific values of properties used to search for people and create Segments. Constraints vary depending on the type of field you select (and whether it is a text field, dropdown, date, or other field type).

[Learn More: Constraint Operators](https://help.element451.com/en/articles/1476149-what-are-constraints)

---

# All Properties | Has + Does Not Have

Many data groups in Element contain an "All Properties" filter option. These allow you to select conditions based on multiple properties associated with that data. For example, Application (All Properties) contains all the properties related to an application, such as term, status, student type, etc.

Within any **All Properties** filter, you can group filters within a property to generate a segment using the **HAS** or **DOES NOT HAVE** operator.

[Learn More: Advanced Filtering](https://help.element451.com/en/articles/7024581-advanced-filters-all-properties-has-and-does-not-have)

---