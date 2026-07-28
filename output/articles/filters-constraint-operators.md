---
title: Filters: Constraint Operators
url: https://help.element451.com/en/articles/1476149-filters-constraint-operators
collection: People
---

Learn about the basic and advanced constraints to improve your people searches: string, list, date, and geo constraints.

# Overview

Constraints are the specific values of properties used to search for people and create Segments. Constraints vary depending on the type of field you select (and whether it is a text field, text area, dropdown, date, or other field type).

Below, we cover each type of field and the operators that apply.

---

# String

The field contains letters and numbers describing the value. Examples include name, email address, and country.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083284705/bf6022f08854854b8a55e4e03bfe/Screen%2BShot%2B2020-01-07%2Bat%2B3_51_34%2BPM.png?expires=1784333700&signature=37385b4c1ed3eb57d06b56e80414772c5638a7592c8f28652c36628d022d38fe&req=diAvFct2mYZfXPMW1HO4zZUQ4tvqvsmPsKnmV5H8oLnapMNTgkB2%2FeFlIcaM%0AL2L%2B12%2F1JtCVdzglC2g%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083284705/bf6022f08854854b8a55e4e03bfe/Screen%2BShot%2B2020-01-07%2Bat%2B3_51_34%2BPM.png?expires=1784333700&signature=37385b4c1ed3eb57d06b56e80414772c5638a7592c8f28652c36628d022d38fe&req=diAvFct2mYZfXPMW1HO4zZUQ4tvqvsmPsKnmV5H8oLnapMNTgkB2%2FeFlIcaM%0AL2L%2B12%2F1JtCVdzglC2g%3D%0A)

The following operators apply to string fields:

|  |  |
| --- | --- |
| **Contains** | The user's field has the value in at least part of the field |
| **Does Not Contain** | The user's field does not contain the value in any part of the field |
| **Exists** | The user has a value in this field.    *Useful for finding users who have fields that are only generated in certain ways, such as email clicks or landing pages.* |
| **Does Not Exist\*** | The field does not exist for the user  * The ***Does Not Exist*** operator can't be used in Activity, Document, or Decision filters to identify missing data. Instead, [label users](https://help.element451.com/en/collections/124550-labels) with the required data and exclude them in your filter. |
| **Starts With** | The user's field starts with the value  * The ***Starts With*** operator supports multiple values. For instance, you can filter last names starting with A, B, and C by entering “[A-C]”. To filter non-sequentially, separate values with commas (e.g., [A,D,G]). * Values should be separated by commas only; using something else like pipes (e.g., A|B|C) will not work. |
| **Does Not Start With** | The user's field does not start with the value  * The ***Does Not Start With*** operator supports multiple values. For instance, you can filter last names starting with A, B, and C by entering “[A-C]”. To filter non-sequentially, separate values with commas (e.g., [A,D,G]). * Values should be separated by commas only; using something else like pipes (e.g., A|B|C) will not work. |
| **Ends With** | The user's field ends with the value |
| **Does Not End With** | The user's field does not end with the value |
| **Is Not** | The user's field is not exactly equal to the value |
| **Regexp** | Create a regular expression to compare against the user's field |

## Note on Text Area Fields

Text area fields store long-form text (such as essay responses or personal statements) and follow the same string format. However, because their content can be quite large, only the **Exists** and **Does Not Exist** operators are supported.

✨ **Pro Tip:** This is especially useful when filtering or segmenting on text area fields used in [Decision checklist conditions](https://help.element451.com/en/articles/9210688-decisions-checklists).

---

# List

List fields are made up of limited choices that the user could select from, such as terms and applications (or any dropdown fields you have in Field Management).

When filtering for these fields, you are given a list of options to choose as values. Multiple conditions may be added to list field filters.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083290624/96b8fbc1f5fb4745664eea009572/Screen%2BShot%2B2020-01-07%2Bat%2B3_55_33%2BPM.png?expires=1784333700&signature=b861c32b2b4ed1a0ae1cbdc66d097e3fd3e89ecd6074069ada2e7d85f6f649fa&req=diAvFct3nYddXfMW1HO4zQXuLMsea6ru%2FuAhq%2BvBAZznjrwqMAkMlG0RwdDY%0AApJT6E%2FfXFZnETUjB2M%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083290624/96b8fbc1f5fb4745664eea009572/Screen%2BShot%2B2020-01-07%2Bat%2B3_55_33%2BPM.png?expires=1784333700&signature=b861c32b2b4ed1a0ae1cbdc66d097e3fd3e89ecd6074069ada2e7d85f6f649fa&req=diAvFct3nYddXfMW1HO4zQXuLMsea6ru%2FuAhq%2BvBAZznjrwqMAkMlG0RwdDY%0AApJT6E%2FfXFZnETUjB2M%3D%0A)

The following conditions apply to list fields.

|  |  |
| --- | --- |
| **Is** | The value matches the user's field |
| **Is Not** | The value does not match the user's field |
| **In** | The user's field matches any of a number of choices in the value. You are able to select more than one choice using "In." |
| **Not In** | The user's field does not match any of the values chosen |

---

# Date

Date fields contain data on when a user completed an action, such as submitting an application or survey, or their birth date. The When Operator is the most important aspect of Date fields. This operator can be relative or exact.

## Relative

Relative dates are measured from a certain point relative to the present. They are built using this format: "From X to Y days/weeks/months/years ago."   
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083292449/2a6b4afc6ba4113cb9fdf20ed895/Screen%2BShot%2B2020-01-07%2Bat%2B3_57_32%2BPM.png?expires=1784333700&signature=b950b21cfcf886e748e298236a351ef868b725d452b1f34879aaad62668d6926&req=diAvFct3n4VbUPMW1HO4zWMeXVlkVVQy0cJbTfvfCxn94Bkis3Hq4JbNoxKR%0ANLHPyWdmCbLc5iC5i1Q%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083292449/2a6b4afc6ba4113cb9fdf20ed895/Screen%2BShot%2B2020-01-07%2Bat%2B3_57_32%2BPM.png?expires=1784333700&signature=b950b21cfcf886e748e298236a351ef868b725d452b1f34879aaad62668d6926&req=diAvFct3n4VbUPMW1HO4zWMeXVlkVVQy0cJbTfvfCxn94Bkis3Hq4JbNoxKR%0ANLHPyWdmCbLc5iC5i1Q%3D%0A)

To use this filter, you would fill in the following fields:

|  |  |
| --- | --- |
| **From** | Number of days/weeks/months/years |
| **To** | Number of days/weeks/months/years |
| **Ago** | Select days/weeks/months/year |

## Exact Dates

**Exact** dates are measured with a start and end date, each with a day, month, and year.

[![](https://downloads.intercomcdn.com/i/o/175138086/b4b8c8d3783ff8842f5f943c/Screen+Shot+2020-01-07+at+4.02.10+PM.png?expires=1784333700&signature=22407d53818ecb568ea9abffcb4fe4152ceee856ac518792001eb8ff6155def8&req=dSciF8p2nYlZFb4f3HP0gMAWVflM0bWpeTCZBJ5%2FHkzVl%2B%2FzJ9GZ8mAKukWJ%0A%2FJly7%2F0zhMF7Ums5Dg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/175138086/b4b8c8d3783ff8842f5f943c/Screen+Shot+2020-01-07+at+4.02.10+PM.png?expires=1784333700&signature=22407d53818ecb568ea9abffcb4fe4152ceee856ac518792001eb8ff6155def8&req=dSciF8p2nYlZFb4f3HP0gMAWVflM0bWpeTCZBJ5%2FHkzVl%2B%2FzJ9GZ8mAKukWJ%0A%2FJly7%2F0zhMF7Ums5Dg%3D%3D%0A)

---

# Geo

Geo fields allow you to filter by the distance from a given point.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083296430/b3f8c3ee2aa80dba9ef3d22128ad/Screen%2BShot%2B2020-01-07%2Bat%2B4_03_59%2BPM.png?expires=1784333700&signature=b5f81412bedeaa1d31ed99f648ba6c45fdd3c533f038bcc79099b98fa64c3642&req=diAvFct3m4VcWfMW1HO4zXMpGAEofmVPinX1gXky9uiAForRkG0vmj7v2SD%2B%0Aqldmz6RcBcFShCkiFCA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2083296430/b3f8c3ee2aa80dba9ef3d22128ad/Screen%2BShot%2B2020-01-07%2Bat%2B4_03_59%2BPM.png?expires=1784333700&signature=b5f81412bedeaa1d31ed99f648ba6c45fdd3c533f038bcc79099b98fa64c3642&req=diAvFct3m4VcWfMW1HO4zXMpGAEofmVPinX1gXky9uiAForRkG0vmj7v2SD%2B%0Aqldmz6RcBcFShCkiFCA%3D%0A)

The following operators are used for geo fields:

|  |  |
| --- | --- |
| **Address** | The address from which to measure. Beginning to type here will bring up an auto-complete using Google Maps to assist you in finding the exact address. |
| **Value** | The number of miles/kilometers you would like to set as a maximum distance from the chosen address |
| **Unit** | Choose to measure in miles or kilometers |

---

Now that you're familiar with constraints put them to use by learning how to create a segment.

[Learn More: Creating a Segment](https://help.element451.com/people/segments/creating-a-segment)

---