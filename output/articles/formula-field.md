---
title: Formula Field
url: https://help.element451.com/en/articles/8857623-formula-field
collection: Workflows + Rules
---

Learn more about the formula field available when using specific user property action in Workflows + Rules.

# Overview

When using the [user property actions](https://help.element451.com/en/articles/1500292-actions#h_8c6d61d2b1) in Workflows + Rules, you have the capability to add custom-calculated fields by employing formulas, unlocking powerful data manipulation possibilities:

* *Set User's Custom Date Property*
* *Set User's Custom Property*
* *Set User's Property*

[![](https://downloads.intercomcdn.com/i/o/941661759/c44011758958803961f52b33/Screenshot+2024-01-23+at+10.57.42%E2%80%AFAM.png?expires=1784333700&signature=e70b822119d6747e0fe765ca19c127034777a32cda6fd9b0d759c4fcf94f6519&req=fSQmEM9%2FmoRWFb4f3HP0gAdcCuj0IaH6GFlOyBaKVIkYy58K%2Fi80Iy8%2F6ilz%0A60sCGSFImaSYpMzEuw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/941661759/c44011758958803961f52b33/Screenshot+2024-01-23+at+10.57.42%E2%80%AFAM.png?expires=1784333700&signature=e70b822119d6747e0fe765ca19c127034777a32cda6fd9b0d759c4fcf94f6519&req=fSQmEM9%2FmoRWFb4f3HP0gAdcCuj0IaH6GFlOyBaKVIkYy58K%2Fi80Iy8%2F6ilz%0A60sCGSFImaSYpMzEuw%3D%3D%0A)

---

# Adding a Formula

📙 Note: However, it's classified as an advanced feature, necessitating proficiency with the formula syntax similar to that used in our Import/Export functionality. Prior experience with this syntax is highly recommended to leverage this feature effectively.

When you select one of the [user property actions](https://help.element451.com/en/articles/1500292-actions#h_8c6d61d2b1), the Formula field will automatically display, allowing you to add your own formula. The formula field uses the same formulas as our Import/Export functions.

[Learn More: List of Formula Functions](https://integrations.element451.com/calculated-fields-37)

[Learn More: Common Calculated Fields](https://help.element451.com/en/articles/9007704-calculated-fields)

---

# Testing Your Formula

Once you have added your code, you can use the **Test Formula** section to preview the results based on a specific user.

1. Select a user from the drop-down menu.
2. Click the Evaluate button

   [![](https://downloads.intercomcdn.com/i/o/941675032/cbd1b4db0161928b1971f628/Screenshot+2024-01-23+at+11.08.53%E2%80%AFAM.png?expires=1784333700&signature=2b0703e0218bb5c1ea1f8f574be484a9001d4368f5f804a41036720d9e75141c&req=fSQmEM57nYJdFb4f3HP0gKsJWyya6Zi3brL6NPFckazxu7aUhW%2FSJp8pode1%0ARGk%3D%0A)](https://downloads.intercomcdn.com/i/o/941675032/cbd1b4db0161928b1971f628/Screenshot+2024-01-23+at+11.08.53%E2%80%AFAM.png?expires=1784333700&signature=2b0703e0218bb5c1ea1f8f574be484a9001d4368f5f804a41036720d9e75141c&req=fSQmEM57nYJdFb4f3HP0gKsJWyya6Zi3brL6NPFckazxu7aUhW%2FSJp8pode1%0ARGk%3D%0A)

   .
3. Review the *evaluated formula* output.

[![](https://downloads.intercomcdn.com/i/o/941671892/06634a37715f83128581a863/Screenshot+2024-01-23+at+11.06.35%E2%80%AFAM.png?expires=1784333700&signature=5c9f8f3e5bf4f9d5e289119f790c1bb6306c282cee6c7d223e3537388c96df23&req=fSQmEM5%2FlYhdFb4f3HP0gFs%2FFqqjNroVpSUKPC%2FPlPoDHHCVSTjHO1jYJrtV%0A7AfM2i7sA1sXBaD%2F%2Bw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/941671892/06634a37715f83128581a863/Screenshot+2024-01-23+at+11.06.35%E2%80%AFAM.png?expires=1784333700&signature=5c9f8f3e5bf4f9d5e289119f790c1bb6306c282cee6c7d223e3537388c96df23&req=fSQmEM5%2FlYhdFb4f3HP0gFs%2FFqqjNroVpSUKPC%2FPlPoDHHCVSTjHO1jYJrtV%0A7AfM2i7sA1sXBaD%2F%2Bw%3D%3D%0A)

---

# Writing to Fields Backed by Data Sources

When your formula sets a field that is backed by a data source, the formula's output must match a value that exists in that field's data source. If the formula returns a value the field does not support, the value may not be saved, and the field can appear blank on the person's profile even though the formula evaluated successfully.

Keep in mind that some system fields are locked to a fixed data source. For example, the *Are You Hispanic/Latino?* system field only accepts Yes/No values, even if a different data source appears to be selected in Field Management.

If you need to store options beyond what a system field supports (such as a "Not answered" value), create a custom field backed by a custom data source that includes those options, and have your formula write to that custom field instead.

---

# Use Cases

## Create Prospect Scores

Use a formula to evaluate multiple conditions of a Prospect's record, then assign a score all within a Rule.

## Condense Multiple Steps into One

Store multiple conditions in one formula instead of creating one step per condition. This can drastically reduce the number of steps in a Rule that populates a Person's Assignee or populates custom properties.

## Clean up Data without Export/Import

Clean up data at scale by using a formula to transform data or correct it.

---

# Formula Examples

## Age Calculation

### Current Age Calculation

```
DATE_DIFF("year", DATE_FORMAT([user-dob], "m/d/Y"), DATE_DEFAULT("m/d/Y"))
```

### Calculated Age at Term Start

```
IF(DATE_DIFF("year", DATE_FORMAT([user-dob], "m/d/Y"), DATE_FORMAT(DS_MAP([user-education-term],"data_source.terms","guid","start_date",""), "m/d/Y")) >= 24, "nontrad", "trad")
```

## Custom Scoring Calculation

📙 **Referencing the Engagement Score:** To use a person's Element451 Engagement Score in a formula, reference it as `[user-calculated-engagement_score-new]`. The `[user-engagement-score]` reference is not valid; it returns a "Sub expression is not valid" error and does not appear in the formula field picker. The value resolves to the person's engagement level, such as FAN, FOLLOWER, or LURKER, which you can map to points to build a yield or prospect score. See [Student Engagement Score](https://help.element451.com/en/articles/4957167-student-engagement-score) for how these levels are defined.

### Major

```
IF( DB_MAP("major", [user-education-prefered-major], "guid", "code", "") = "BUSI" | DB_MAP("major", [user-education-prefered-major], "guid", "code", "") = "HS11",  5, IF(DB_MAP("major", [user-education-prefered-major], "guid", "code", "") = "ACC", 3, 1))
```

### Citizenship

```
IF([user-citizenship-country] = "USA", "5", IF([user-citizenship-country] = "ENG" | [user-citizenship-country] = "FRA", "3", "1"))
```

### Denomination

```
IF([user-religion-name] = "ME", "5", IF(CONTAINS([user-religion-other], "Methodist") = TRUE, "5", IF([user-religion-name] = "BT" | [user-religion-name] = "EP", "4", IF([user-religion-name] = "EV" | [user-religion-name] = "LU", "3", "1"))))
```

### Rank

```
IF(  
	SUM([user-custom-training-score-major], [user-custom-training-score-relig], [user-custom-training-score-cit])>10  
	,"ideal"  
	,IF(  
		SUM([user-custom-training-score-major], [user-custom-training-score-relig], [user-custom-training-score-cit])>5  
		,"compatible"  
		,"potential"))
```

---