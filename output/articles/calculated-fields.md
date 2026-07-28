---
title: Calculated Fields
url: https://help.element451.com/en/articles/9007704-calculated-fields
collection: Data Management
---

Check out this list for helpful formulas to help you with your imports and exports

# Overview

Calculated Fields are a great way to build formulas to manipulate incoming data or outgoing data on Imports + Exports. We have put together a quick list of formulas we see our partners use the most.

To access our full list of formulas you can use in a calculated field, check out [this link](https://integrations.element451.com/calculated-fields-37).

---

# Common Import Formulas

📌 **Note:** [C#] is where you insert the column number from your import

## Make 'Year' field a Full Date

Helpful when you only have a student's graduation year. In this example, we assume the graduation date was June 1st.

```
DATE_READ(CONCAT(“06/01/”,[C#]), “m/d/Y”)
```

## Use Today's Date

Helpful when a timestamp is required by not available in the import file. For example, a import file might have the student's application, but not their application submit date. Use the following formula to insert today's date as the submit date.

```
DATE_DEFAULT("Y-m-d")
```

## Date Format is Missing Leading Zero

For example, if your date looks something like this, "1012022" you'll want to add the initial leading zero so the DATE\_READ formula will work.

```
DATE_READ(PAD([C#], "0", 8), "mdY")
```

**Note:** This formula will be helpful when importing date of birth from ACT files.

## Use a 'Year' to Create a Term Value

In this example, we have a student's graduation year and also want to map the term associated with that graduation. This example assumes you name your terms "Fall ####". You will want to tweak to fit your institution's naming convention

```
DB_MAP(“term”, CONCAT(“Fall “, [C#]), “name”, “guid”, ””)
```

## Split a Name or Word

In this example, the student's first name and last name are in the same field and you want to grab the first name. TITLECASE is used to capitalize the first letter of the name.

```
TITLECASE(SPLIT_INDEX([C1]," ",1))
```

## Remove Double-quotation Marks from a Word

In this example, we have some row values that have quotes around them and some that don't. Row 1 says is: "First Name 1"; while row 2 is: First Name 2. We want to remove the double-quotes so they don't appear in the data. By using REGEXP\_REPLACE, we can remove quotes on values that have them, and leave values without alone.

```
REGEXP_REPLACE([C1], """", "")
```

Row 1 Output: First Name 1

Row 2 Output: First Name 2

**Note**: The second parameter of the formula has 4 double-quotes. Two to wrap the parameter and two to target the double-quote character. To target double-quotes in the second parameter of the formula, we'll need to input the double-quote twice. Double-quotes are also the wrappers for parameters of the formula, so only inputting one will cause the formula to break.

## Map Incoming Data to Data Source Values

Sometimes your import file field for major is already mapped to an Element field, but you need to also have that same data populated in another field. When it comes to drop downs, it is super important that Element understands how the data is coming to correctly map it to the correct value on the data source.

```
DS_MAP([C1],"data_source.major","code","guid","")
```

The first parameter refers to the column in the import file. The second parameter is the data source name found under the data sources module in the URL of the data source you are using. The third parameter is the column from the data source that matches with what the import file is bringing in. The fourth parameter is the column from the data source that is what you want the data to be translated to typically the guid or value. The fifth parameter is a fall back, so if the system can't find a match, what do you want inserted into the field.

## Importing Labels

An import task can add one or more label's to each contact being imported.

These labels can be used to quickly Segment, or to initiate automations like Workflows or Intelligent Admissions Rules.

Map your calculated column to:

```
user-labels-import
```

To import one label, simply put it in between quotes:

```
"training.taxonomy.12345"
```

To import multiple labels, put them all in one set of quotes, comma separated, with no spaces in between:

```
"training.taxonomy.12345,training.taxonomy.78912,training.taxonomy.11235"
```

If you have several columns of data that need to feed into the label field the calculated field will need to glue together the columns. In this example, the columns are 2, 3, and 4 and are coming in as the name:

```
CONCAT(TAXONOMY_MAP([C2],"name","guid",""),",",TAXONOMY_MAP([C3],"name","guid",""),",",TAXONOMY_MAP([C4],"name","guid",""))
```

---

# Common Export Formulas

## Translate a Label or Taxonomy Code to it's Name

In this example, we want to export the name of user's label. By default, the user-labels-one, user-labels-two, etc. fields will output the GUID of the label. To output the label name, use the following formula:

```
TAXONOMY_MAP([user-labels-one] "guid", "name", "")
```

## List of Student's Multiple Races

In this example, we have students that selected their identification with multiple races. To export a list of all races check, use the following formula:

```
CHECKBOX_CHECKED([user-race-categories],",")
```

## Return Age from Student's Birthdate

In this example, we want to export the student's age rather than their birthday. Element451 doesn't store age by default. This formula compares the student's date of birth to the current date (date\_default). The difference in years is the student's age.

```
DATE_DIFF("year", [user-dob], DATE_DEFAULT("Y-m-d H:i:s"))
```

## Return Age of Student at Intended Term Start

In this example, we want to know what a student's age will be at the start of their intended term. This can help verify a student will be a legal adult. This formula compares the student's date of birth to the start date of their intended term. The student must have selected an intended term and the [term data source](https://help.element451.com/en/articles/3152502-adding-majors-terms-degrees-campuses-schools#h_19dcb4d278) must have a start date. The difference in years will be the student's age. Swap Intended Term for [Active Term](https://help.element451.com/en/articles/6960851-traits#h_b6be742207) or [Application Term](https://help.element451.com/en/articles/2582913-intended-vs-application-fields). Note: You can only use Application Term if the workflow is triggered by an Application event trigger so the Application scope is known.

```
DATE_DIFF("year", [user-dob], DATE_READ(DB_MAP("term", [user-education-term], "guid", "start_date", ""), "D M d H:i:s O Y"))
```

## Return Student's Next Birthday

In this example, we want to know the date of the next birthday. We first replace with the birthday "year" with the current year and compare that to the current date. If the modified birthday is greater than the current date, the modified birthday is returned. If the modified birthday is less than the current date, then the birthday has passed for the current year. So a year is added to the modified birthday and returned.

```
IF(DATE_COMPARE(DATE_DEFAULT("Y-m-d"), "<", CONCAT(DATE_DEFAULT("Y"), DATE_FORMAT([user-dob], "-m-d"))) = TRUE, DATE_READ(CONCAT(DATE_DEFAULT("Y"), DATE_FORMAT([user-dob], "-m-d")), "Y-m-d"), DATE_READ(CONCAT(DATE_DEFAULT("Y")+1, DATE_FORMAT([user-dob], "-m-d")), "Y-m-d"))
```

## Exporting a Specific Column from a Regular Data Source

In this example, we have a [custom field](https://help.element451.com/en/articles/9118615-field-management) connected to a [Regular Data Source](https://help.element451.com/en/articles/2066888-data-sources). The Regular Data Source has three columns: a name, a code and a second code.

By default, Exports will output the right-most column of the regular data source. In this case, that is the second code located in column 3. To export the name, use the following formula:

```
DS_MAP([user-custom-training-sport-participation], "training.data_source.7606", "column_3", "column_1", "")
```

Note: The "match" and "output" parameters are "column\_3" and "column\_1" respectively. While these columns are labeled "Name" and "Code 2" in Element, the database knows them as by their column number. To check the database names for each column, download the regular data source using the download icon in the Data Sources module.

## Exporting a Value Only if Multiple Conditions are Met

In this example, we want to export one field only if other fields have a certain value. If *all* conditions aren't met, we want the column to be blank. Lets pretend our data looks like this:

|  |  |  |
| --- | --- | --- |
| **Column 1** | **Column 2** | **Column 3** |
| Yes | Yes | "Sample 1" |
| Yes | No | "Sample 2" |

We only want to export Column 3 if both Column 1 and Column 2 equal "Yes". To do this, we'll use the following formula:

```
IF([column-1] = "Yes" & [column-2] = "Yes", [column-3], "")
```

Using this formula, row 1 will have an output of "Sample 1". This is because both conditions were met. Row 2 will have an output of "" because Column 2 failed to meet the condition.

**Note**: Unlike other examples, this example is *not* using valid Export fields. These fields are only for this example.

## Export a Value If Any of Multiple Conditions are Met

In this example, we want to export one field only if other fields have a certain value. If *any* conditions are met, the field will be exported. Otherwise, the column will be blank. Lets pretend our data looks like this:

|  |  |  |
| --- | --- | --- |
| **Column 1** | **Column 2** | **Column 3** |
| Yes | Yes | "Sample 1" |
| Yes | No | "Sample 2" |
| No | No | "Sampe 3" |

We want to export Column 3 if Column 1 and Column 2 equal "Yes". To do this, we'll use the following formula:

```
IF([column-1] = "Yes" | [column-2] = "Yes", [column-3], "")
```

Using this formula, row 1 will have an output of "Sample 1". This is because both condition were met. Row 2 will have an output of "Sample 2" because Column 1 fulfilled the condition, even those Column 2 was no. Row 2 will have an output of "" because neither Column 1 nor Column 2 met the condition.

**Note**: Unlike other examples, this example is *not* using valid Export fields. These fields are only for this example.

## Exporting Checkbox Fields as Individual Columns

In this example, we want to export a checkbox field with each checked value a single column, so there is not one field with 4 values, but 4 columns with a single value in each. A common use case is exporting the Race field as individual columns instead of one column with all the values.

```
SPLIT_INDEX(CHECKBOX_CHECKED([user-race-categories],","),",",1)  
SPLIT_INDEX(CHECKBOX_CHECKED([user-race-categories],","),",",2)  
SPLIT_INDEX(CHECKBOX_CHECKED([user-race-categories],","),",",3)  
SPLIT_INDEX(CHECKBOX_CHECKED([user-race-categories],","),",",4)
```

Using this formula, we make sure to first put the checkbox field in a format where there is commas in between using the CHECKBOX\_CHECKED formula. Then SPLIT\_INDEX allows us to separate all the items checked using the comma as the separator and then identify a specific position to pull out. What is great about these formulas, is if the user only selects 2 races in this example, the columns for Race 3 and Race 4 won't error out, they simply will just remain blank.

## Export Degree Associated with a Selected Major

In this example, we want to export the Degree associated to the Major that a student has selected. Lets assume that we ask a student for their Intended Major on a RFI form. We don't want to ask for Intended Degree in order to reduce the number of fields on the RFI, but we still want to export degree.

```
FIRST(DS_MAP([user-education-prefered-major], "data_source.majors","guid", "degrees", ""))
```

**Note**: Ensure that [each major is configured to be "available for" it's associated degree.](https://help.element451.com/en/articles/7321011-field-filtering) Otherwise, "degrees" will return null.

---

# Export Formula Evaluation (Preview)

When configuring a **calculated** **column**, you can evaluate or preview your formula with data from an existing contact before running the export. This helps ensure the formula will produce the desired output when you run the task.

After adding your formula, you can evaluate by selecting a contact and clicking the blue **Evaluate** button. The evaluated formula will appear under the Evaluated Formula heading in the black code box.

[![](https://downloads.intercomcdn.com/i/o/1018596354/cd5e26110b291d12edcae906/Export+form.png?expires=1784333700&signature=ba602c41cc8defad653e19d3dc5f3ee6b63828899cbbe9a035cb2984d49e6ff5&req=dSAmHsx3m4JaXfMW1HO4zesxLALgl8zvWlk%2FFTGhIehuH%2FsxMpYHY%2BZ3w8Vv%0ABUmIIuvxBzuhSb0Dcwg%3D%0A)](https://downloads.intercomcdn.com/i/o/1018596354/cd5e26110b291d12edcae906/Export+form.png?expires=1784333700&signature=ba602c41cc8defad653e19d3dc5f3ee6b63828899cbbe9a035cb2984d49e6ff5&req=dSAmHsx3m4JaXfMW1HO4zesxLALgl8zvWlk%2FFTGhIehuH%2FsxMpYHY%2BZ3w8Vv%0ABUmIIuvxBzuhSb0Dcwg%3D%0A)

---