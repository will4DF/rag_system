---
title: Race & Ethnicity Field Group: Race Categories and Subgroups
url: https://help.element451.com/en/articles/14478232-race-ethnicity-field-group-race-categories-and-subgroups
collection: Data Management
---

Learn how the Race Categories and Subgroups field works in Element451, including categories, full subgroup lists, and how it aligns with the 2024 federal standard.

# **Overview**

The **Race Categories and Subgroups (Race/Ethnicity)** field group *[user-race-ethnicity-root]* in Element451 is designed to align with the **2024 federal race and ethnicity data collection standard**, replacing the legacy **1997 two-question format** with a unified approach.

Unlike the 1997 standard—which separated ethnicity and race into two individual fields—the 2024 standard is implemented in Element451 as a **single field group**. This group includes built-in conditional logic to guide users through selecting race categories, subgroups, and any applicable write-in responses.

🚨 **Important**: The 2024 federal standard must be adopted by all federal agencies by **March 2029**, making this structure essential for long-term compliance. IPEDS may choose to adopt this structure sooner, so when you choose to update your forms and applications may vary.

---

# **Understanding the Field Structure**

Unlike the two field setup for the 1997 standard **(**[user-race-hispanic] and [user-race-categories]), the **Race Categories and Subgroups** field [user-race-ethnicity-root] group consolidates all demographic selections into one experience.

Within this group, users can:

* Select one or more **race categories**
* Choose **subgroups** within each selected category
* Provide **“Other” write-in responses** when applicable

🧠 **Good to Know**: The conditional logic dynamically displays subgroup options based on the selected category, ensuring a clean and guided experience without additional configuration.

---

## Considerations for Exports & Integration

As of April 2026, not all SIS or external systems currently support the data structure required for these new federal standards.  
​  
If you leverage exports or integrations**—**including Element451 managed integrations**—**confirm compatibility before updating forms or applications to the new field group.

---

## **How This Differs from the 1997 Standard**

|  |  |
| --- | --- |
| **1997 Standard** | **2024 Standard** |
| Two separate fields | One unified field group |
| Ethnicity asked separately | Combined into one experience |
| Limited detail | Includes subgroups + write-ins |
| Static structure | Dynamic, conditional logic |

---

# **Race Categories**

The field includes the following federally aligned primary categories:

* American Indian or Alaska Native
* Asian
* Black or African American
* Hispanic or Latino
* Middle Eastern or North African
* Native Hawaiian or Other Pacific Islander
* White

---

# **Subgroups by Category**

Below is the full list of subgroups currently implemented in Element451 by default. You can adjust this list as needed using [data sources.](https://help.element451.com/en/articles/2066888-data-sources)

* **American Indian or Alaska Native**

  + Navajo Nation
  + Cherokee
  + Sioux
  + Chippewa
  + Choctaw
  + Other (write-in)
* **Asian**

  + Chinese
  + Indian
  + Filipino
  + Vietnamese
  + Korean
  + Japanese
  + Pakistani
  + Cambodian
  + Hmong
  + Thai
  + Other (write-in)
* **Black or African American**

  + African American
  + Jamaican
  + Haitian
  + Nigerian
  + Ethiopian
  + Somali
  + Ghanaian
  + Trinidadian and Tobagonian
  + Other (write-in)
* **Hispanic or Latino**

  + Mexican
  + Puerto Rican
  + Cuban
  + Salvadoran
  + Dominican
  + Colombian
  + Guatemalan
  + Honduran
  + Spaniard
  + Other (write-in)
* **Middle Eastern or North African**

  + Lebanese
  + Iranian
  + Egyptian
  + Syrian
  + Moroccan
  + Israeli
  + Iraqi
  + Jordanian
  + Palestinian
  + Other (write-in)
* **Native Hawaiian or Other Pacific Islander**

  + Native Hawaiian
  + Samoan
  + Chamorro
  + Tongan
  + Fijian
  + Marshallese
  + Other (write-in)
* **White**

  + German
  + Irish
  + English
  + Italian
  + Polish
  + French
  + Scottish
  + Norwegian
  + Dutch
  + Other (write-in)

📌 **Note**: Each category includes an **“Other” option with a write-in field**, allowing users to self-identify beyond predefined selections.

---

# **Why This Matters**

* **More Accurate Representation**  
  Users can select identities that more closely reflect how they self-identify, including detailed subgroup affiliations.  
  ​
* **Streamlined Data Collection**  
  A single, dynamic field group reduces complexity while capturing richer data.  
  ​
* **Federal Alignment**  
  This structure aligns with the 2024 federal standard to be fully implimented by 2029 and supports evolving reporting requirements such as IPEDS.

---