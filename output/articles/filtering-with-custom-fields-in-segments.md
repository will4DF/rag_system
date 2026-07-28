---
title: Filtering with Custom Fields in Segments
url: https://help.element451.com/en/articles/10167508-filtering-with-custom-fields-in-segments
collection: People
---

# Overview

When creating segments using custom field data, it’s important to understand how “empty” states can impact your search results. Custom fields behave differently than system fields like `first-name`, depending on whether they have a value, are empty, or don’t exist in the database at all. These differences stem from how our database stores and retrieves custom field data, which can sometimes create unexpected results when building segments.

This article explains the nuances of how custom fields are stored, the states they can exist in, and how to build queries and segments that accurately reflect your data. For simplicity, we’ll use `favorite-color` as an example throughout the guide. As you read, consider applying these concepts to one of your own custom fields to make the examples more relevant to your needs.

## Common Issue: Contacts Are Missing from Segment

When using custom field data with the "Not In" operator, you might notice that certain contact records are unexpectedly missing.

This happens because the `Not In` operator only evaluates custom fields that **exist** **in the database**. Your segment will not include records where the custom field is completely missing in this configuration (explained in the "[Why Some Fields May Not Exist](#h_eabbdd7f1a)" section below).   
​  
​**You must combine "Not In" with the "Does Not Exist" operator to ensure these records are included**. We cover this process in detail below.

---

# Understanding Custom Field States

Custom fields like `favorite-color` can behave differently based on how data is stored or entered. These fields don’t always contain a value, and in some cases, they might not even exist in the database. This distinction is crucial for understanding query results and why some records appear (or don’t) in your filtered data.

To help clarify, a custom field can be in one of three possible states:

|  |  |  |
| --- | --- | --- |
| **State** | **Explanation** | **Example** |
| **Exists with a Value** | The field is present and contains data. | A student with `favorite-color = blue` will match a query for "favorite color is blue." |
| **Exists but Empty** | The field is present but has no data/null value. | A student with a `favorite-color` field that has no data/null value exists in the database but hasn't specified a color preference. |
| **Does Not Exist\*** | The field is absent from the database. | A student without `favorite-color` does not have the field stored in their database record, although it may appear in the user interface. Read more on this [below](#h_eabbdd7f1a). |

### \*Why Some Fields May "Not Exist"

Although you can see custom fields like `favorite-color` on the contact profile, they don’t always exist in the database. Here’s why:

* **Efficient Data Storage:** Data is stored in a way that optimizes performance. Custom fields without data are sometimes excluded from the database and only added when a value is entered. If the value is removed later, the field remains in the database as empty/null.
* **User Interface vs. Database:** The contact profile interface (what you see) shows all custom fields to maintain usability, even if they don’t exist in the database.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1324797404/7e8dac787e17b77d57757bba7951/Custom-2Bfields-2B--2Bprofile.png?expires=1784333700&signature=e2cd9c36c5031b1da5941205f81c6795c93761769ca4753234a08a5f28e35c64&req=dSMlEs53moVfXfMW1HO4zUlu1bNeRT%2F%2FHHZoKHAXDuRxiZ5oIf3iVUxRnbaz%0AL5VkR32Sk7G5kNMLfC8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1324797404/7e8dac787e17b77d57757bba7951/Custom-2Bfields-2B--2Bprofile.png?expires=1784333700&signature=e2cd9c36c5031b1da5941205f81c6795c93761769ca4753234a08a5f28e35c64&req=dSMlEs53moVfXfMW1HO4zUlu1bNeRT%2F%2FHHZoKHAXDuRxiZ5oIf3iVUxRnbaz%0AL5VkR32Sk7G5kNMLfC8%3D%0A)

#

---

# Query Operators and Their Behavior

When filtering custom fields, choosing the right operator for your specific goal is important. Each operator handles “empty” and “nonexistent” states differently, so understanding their behavior ensures your query captures the correct contact records.

Let’s explore the commonly used operator with examples of a `favorite-color` custom field:

### “Not In” Operator

#### Behavior

The `not in` operator excludes records that match specified values while including those that have no data/null value.

* **Includes**

  + Records where the field exists but doesn’t match specified values
  + Records where the field exists but has no data/null value
  + Records where the field does not exist
* **Excludes**

  + Records where the field matches the specified value

#### Example Segment

`favorite-color not in red`

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259885693/9514c3402189b3324f57e517f3ba/operator%2Bnot-in.png?expires=1784333700&signature=3934bea4d1c29ab2230bcd4ba84d5451e633768dc1707443e3aaef65e51d46e5&req=dSIiH8F2mIdWWvMW1HO4zUm%2B%2Bxp5OX4%2B9AjTXD4wHjd303CZ%2FlQzQepuhzPv%0A6eLX7aWUpvCswIah73I%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259885693/9514c3402189b3324f57e517f3ba/operator%2Bnot-in.png?expires=1784333700&signature=3934bea4d1c29ab2230bcd4ba84d5451e633768dc1707443e3aaef65e51d46e5&req=dSIiH8F2mIdWWvMW1HO4zUm%2B%2Bxp5OX4%2B9AjTXD4wHjd303CZ%2FlQzQepuhzPv%0A6eLX7aWUpvCswIah73I%3D%0A)

This segment will:

* **Include** students whose:

  + `favorite-color` field exists but is not "red"
  + `favorite-color` field exists but has no data/null value
  + `favorite-color` field doesn't exist in the database
* **Exclude** students whose:

  + `favorite-color` field is "red"  
    ​

### "Exists" Operator

#### Behavior

The `exists` operator finds records where a field is present and contains any value.

* **Includes**

  + Records where the field exists and contains any value
* **Excludes**

  + Records where the field exists but has no data/null value
  + Records where the field does not exist

#### Example Segment

`favorite-color exists`

This segment will:

* **Include** students whose:

  + `favorite-color` field exists and contains any color value
* **Exclude** students whose:

  + `favorite-color` field exists but has no data/null value
  + `favorite-color` field doesn't exist in the database

### “Does Not Exist” Operator

#### Behavior

The `does not exist` operator finds records where a field is either missing from the database or has no data/null value.

* **Includes**

  + Records where the field does not exist in the database
  + Records where the field exists but has no data/null value
* **Excludes**

  + Records where the field exists and contains any value

#### Example Query

`favorite-color does not exist`

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1261390008/cd775d636b05aeba3c030c40a922/does-2Bnot-2Bexist.png?expires=1784333700&signature=7124fd7a534e19c2adf90d9bf6377fee7dd4bd725a06c17b9a4a77ba812e2f35&req=dSIhF8p3nYFfUfMW1HO4zfUv280F091uBlRN3OQLbqc%2Fk2pyuNPz6%2BaTNgtS%0A4UtzleaCcRuCSkzLkOk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1261390008/cd775d636b05aeba3c030c40a922/does-2Bnot-2Bexist.png?expires=1784333700&signature=7124fd7a534e19c2adf90d9bf6377fee7dd4bd725a06c17b9a4a77ba812e2f35&req=dSIhF8p3nYFfUfMW1HO4zfUv280F091uBlRN3OQLbqc%2Fk2pyuNPz6%2BaTNgtS%0A4UtzleaCcRuCSkzLkOk%3D%0A)

This segment will:

* **Include** students whose:

  + `favorite-color` field is missing from the database
  + `favorite-color` field exists but has no data/null value
* **Exclude** students whose:

  + `favorite-color` field exists and contains any value

### “Is Empty” Operator

#### Behavior

The `is empty` operator finds records where a field exists but has no data/null value.

* **Includes**

  + Records where the field exists but has no data/null value
* **Excludes**

  + Records where the field does not exist
  + Records where the field contains any value

#### Example Query

`favorite-color is empty`

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1261390499/b06556613ae3b3ccf944a9511513/is%2Bempty.png?expires=1784333700&signature=81445dd85ca90afd8f41fd1542268801196faaba5e72c028bda75e6c387cd57c&req=dSIhF8p3nYVWUPMW1HO4zSigArp3YMxjwgZExM20CH7iNSSxg6sN1ly8ruDz%0AP0PZIrQHp3T69qT5jr0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1261390499/b06556613ae3b3ccf944a9511513/is%2Bempty.png?expires=1784333700&signature=81445dd85ca90afd8f41fd1542268801196faaba5e72c028bda75e6c387cd57c&req=dSIhF8p3nYVWUPMW1HO4zSigArp3YMxjwgZExM20CH7iNSSxg6sN1ly8ruDz%0AP0PZIrQHp3T69qT5jr0%3D%0A)

This segment will:

* **Include** students whose:

  + `favorite-color` field exists but has no data/null value
* **Exclude** students whose:

  + `favorite-color` field doesn't exist in the database
  + `favorite-color` field contains any value

###

---

# Common Filtering Scenario

Understanding how to filter custom field data requires careful consideration of how the data is stored and retrieved. Different scenarios may require different operators—or combinations of operators—to ensure your results are accurate and complete. This is especially important when dealing with records where fields are empty or don't exist in the database.

Here is the most common scenario and the filtering strategy to handle it:

## Excluding Specific Values While Including Missing Data

#### Use Case

When planning student outreach campaigns, you may want to exclude students with certain preferences while ensuring you don't miss anyone with incomplete data.

For example, you're planning a series of campaigns and want to exclude students who selected "red" as their favorite color while including those who haven't provided their color preference.

#### Filter(s)

`favorite-color not in red` -OR- `favorite-color does not exist`

This combination will find:

* Students whose `favorite-color` exists with any value except "red"
* Students whose `favorite-color` exists but has no data/null value
* Students whose `favorite-color` field doesn't exist in the database

The combination with `does not exist` is necessary because `not in` only evaluates existing fields in the database.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1261428798/165869251b853f0e88d67adc6b34/not%2Bin%2Bred%2Band%2Bdoes%2Bnot%2Bexist.png?expires=1784333700&signature=30f832885b378f4ce16a4112f5f05aa05eb0a15fb100472fb97a2d6f7a697927&req=dSIhF818lYZWUfMW1HO4zWmPM28Hxxnn8mKbUuX%2Bz9Cw51Gm7Z000P95hH3l%0AZV30HufaVb0q%2F5It%2FYM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1261428798/165869251b853f0e88d67adc6b34/not%2Bin%2Bred%2Band%2Bdoes%2Bnot%2Bexist.png?expires=1784333700&signature=30f832885b378f4ce16a4112f5f05aa05eb0a15fb100472fb97a2d6f7a697927&req=dSIhF818lYZWUfMW1HO4zWmPM28Hxxnn8mKbUuX%2Bz9Cw51Gm7Z000P95hH3l%0AZV30HufaVb0q%2F5It%2FYM%3D%0A)

---