---
title: Conditions
url: https://help.element451.com/en/articles/1500294-conditions
collection: Workflows + Rules
---

Learn to fine-tune Workflows and Rules through conditions.

# Overview

In Workflows + Rules, conditions guide the actions and paths for Contacts based on specific criteria. While the *Date Condition* controls actions based on time-related factors, *User Segment* and *User Segment Reference* conditions provide additional layers of customization based on Contact data and predefined segments.

---

# How Conditions Work

Think of conditions as filters. As people pass through each step of a Workflow or Rule, the condition will filter some to a "yes" path if they pass the conditions and others to the "no" path. You will use actions to define what happens for each path.

[![](https://downloads.intercomcdn.com/i/o/282151821/53b5b3ce3b11b4a446e771e0/Screen+Shot+2020-12-29+at+1.57.28+PM.png?expires=1784333700&signature=f5add08af4d4a91718e5e43f62fa49d5a21337439a0c6435d56d533b26130a66&req=diglF8x%2FlYNeFb4f3HP0gDaH0OXgv5caFFxzgsVuCiDA4jkIzAaqPZW73NU%2F%0AHdP%2F9avWJeLcU9vSpg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/282151821/53b5b3ce3b11b4a446e771e0/Screen+Shot+2020-12-29+at+1.57.28+PM.png?expires=1784333700&signature=f5add08af4d4a91718e5e43f62fa49d5a21337439a0c6435d56d533b26130a66&req=diglF8x%2FlYNeFb4f3HP0gDaH0OXgv5caFFxzgsVuCiDA4jkIzAaqPZW73NU%2F%0AHdP%2F9avWJeLcU9vSpg%3D%3D%0A)

For example, you could have an email sent to applicants who have completed but not yet submitted their applications. It asks them to click a link for “yes” if the school can submit their application on their behalf. Then, you could set a condition that checks to see if recipients clicked the link. If they click “yes,” their app is auto-submitted (the action). If they don’t click, a reminder email is sent (another action) 72 hours later, asking if they’re ready for the app to be submitted.

---

# Add a Condition

The process of adding Conditions is outlined in our help articles on creating Workflows + Rules:

* Workflows: [How to Create a Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow#h_933d1bb2aa)
* Rules: [How to Create a Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule#h_2d95dd7e1d)

---

# Condition Types

## Date Condition

This condition evaluates date and time-based criteria.

[![](https://downloads.intercomcdn.com/i/o/943708203/9537ff4fc3a068b1f3d9e98a/Screenshot+2024-01-25+at+8.31.37%E2%80%AFAM.png?expires=1784333700&signature=9090e40f1deaaf4b138a4ec97213548d9a50f182ca10e53bf12258f686f70640&req=fSQkEcl2n4FcFb4f3HP0gAETbcdudfyOZLHWnn%2FMZtUukPAIM7gb%2FCmqdg%2Ff%0A7O3fpU2ERxEwybK8aw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/943708203/9537ff4fc3a068b1f3d9e98a/Screenshot+2024-01-25+at+8.31.37%E2%80%AFAM.png?expires=1784333700&signature=9090e40f1deaaf4b138a4ec97213548d9a50f182ca10e53bf12258f686f70640&req=fSQkEcl2n4FcFb4f3HP0gAETbcdudfyOZLHWnn%2FMZtUukPAIM7gb%2FCmqdg%2Ff%0A7O3fpU2ERxEwybK8aw%3D%3D%0A)

* **Configuration**: When you select the Date Condition, you'll be prompted to define the condition further using operators and values.

  + **Operators**: Choose from a range of operators. Options include 'Before Date,' 'After Date,' 'Date is Equal to,' 'Day of Week is, 'Month is, 'Hour is,' and 'Minute is.' These operators allow you to create conditions based on precise time frames or recurring time periods.
  + **Value**: After selecting an operator, you'll enter the value, which could be a specific date, day of the week, month, hour, or minute, depending on the operator chosen. This value sets the exact parameter for the condition to meet.
* **Multiple Filters**: Incorporate multiple date-related filters within one condition, connected by 'AND' statements for complex scenarios. Each filter consists of an operator and a value, allowing for highly specific and tailored conditions.

## User Segment

This condition allows you to create a custom segment of Contacts based on specific properties from their Contact record (e.g., demographics, interaction history).

📙 **Note**: The configuration of this condition is similar to using filters in the People module. If you don't have much experience building segments using filters, it would be extremely helpful to review our [Filters Collection](https://help.element451.com/en/collections/7833759-filters) prior to using this condition.

[![](https://downloads.intercomcdn.com/i/o/943758198/2be8c496279914071e3b3e37/Screenshot+2024-01-25+at+9.10.37%E2%80%AFAM.png?expires=1784333700&signature=82ce46bddcf0e6bad1668be59c3b7c673350c1fcc138a4b78f2b5bc8b9710f68&req=fSQkEcx2nIhXFb4f3HP0gIABey4fv6%2FaKLqV%2FtyYniwpGXA5cn3YUHiLDxkG%0AEtiK9r%2FKVlfHdws%2BQw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/943758198/2be8c496279914071e3b3e37/Screenshot+2024-01-25+at+9.10.37%E2%80%AFAM.png?expires=1784333700&signature=82ce46bddcf0e6bad1668be59c3b7c673350c1fcc138a4b78f2b5bc8b9710f68&req=fSQkEcx2nIhXFb4f3HP0gIABey4fv6%2FaKLqV%2FtyYniwpGXA5cn3YUHiLDxkG%0AEtiK9r%2FKVlfHdws%2BQw%3D%3D%0A)

* **Configuration**: Add Contact properties like 'Intended Term' or 'Opened Email.' Each property can have constraints that further refine your segment.

  + **Example Constraint**: For the 'Opened Email' property, you might specify the email campaign and set a constraint that the email must have been opened at least three times.
* **Multiple Filters**: Combine multiple properties within a segment condition, using 'ALL' and 'ANY' operators, allowing for highly specific and tailored conditions.

## User Segment Reference

Utilize a pre-existing segment that you've created.

[![](https://downloads.intercomcdn.com/i/o/943773820/02bd697d8bd0f6c6dd8f10db/Screenshot+2024-01-25+at+9.22.32%E2%80%AFAM.png?expires=1784333700&signature=4aaeac196f14c03d0618685476689e3029a491457fbb9be9163c0d2b39d3346f&req=fSQkEc59lYNfFb4f3HP0gGt6pGFdqQMZDO6dITnouR5PxwKx2ODwsRwlE8NA%0AqbsO9XOWlB8bh09Ffw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/943773820/02bd697d8bd0f6c6dd8f10db/Screenshot+2024-01-25+at+9.22.32%E2%80%AFAM.png?expires=1784333700&signature=4aaeac196f14c03d0618685476689e3029a491457fbb9be9163c0d2b39d3346f&req=fSQkEc59lYNfFb4f3HP0gGt6pGFdqQMZDO6dITnouR5PxwKx2ODwsRwlE8NA%0AqbsO9XOWlB8bh09Ffw%3D%3D%0A)

* **Configuration**: Simply click the **Load Segment** button to select and add an existing segment as your condition.

---

# Combining Condition Types

**Multiple Conditions**: Within a single step, you can add multiple conditions of any type (*Date*, *User* *Segment*, or *User* *Segment* *Reference*), refining the path a Contact takes.

* **Mix and Match**: Feel free to combine different condition types. For instance, you might have a *Date* Condition to check if the day is within a particular period and a *User* *Segment* *Reference* to target a specific group of Contacts.
* **Logical Connectors**: You can connect these conditions using 'AND' statements. This means *all* conditions must be met.

---