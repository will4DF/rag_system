---
title: Adding Majors, Terms, Degrees, Campuses & Schools
url: https://help.element451.com/en/articles/3152502-adding-majors-terms-degrees-campuses-schools
collection: Data Management
---

Learn how to individually add your majors, terms, and campuses.

![](https://downloads.intercomcdn.com/i/o/1144673438/3b9d6a490e35b18ebf386f1b/Important.png?expires=1784430000&signature=ce57bc1e6b7c1519d991466e366cf9bf194c7759a7bad5aff2be18db7965fdbc&req=dSEjEs95noVcUfMW3Hu4gXMxPIMXSsEEsppiiDI5SyMVeWsAM2Km%2FgnIC8yk%0Adw%3D%3D%0A) We automatically filter out majors, terms, degrees, and other options that are not available for a particular application. If you’re wondering, “Why is X term not showing up as an option on this application?”—make sure to check the data sources to confirm that the term, major, degree, etc., has a value in the “Available For” tab.

# **Overview**

Majors, Terms, Campuses, and Schools are all essential features for organizing your data in Element451 and integrating it with other systems you might use. If you provide them, students will select from these lists when filling out RFI forms and applications.

If you're integrating Element with a Student Information System, having your Major, Term, and Campus codes in Element Data Sources will ensure data can be correctly imported and exported.

You can find these Data Sources by navigating to **Data + Automations** > **Data** **Sources**.

---

# **Adding Items Manually**

By default, your Element451 instance does not have any Majors, Terms, Campuses, or Schools. Follow these steps to add your items to each Data Source.

1. Navigate to **Data + Automations** > **Data** **Sources**.
2. Select the tab of the category to which you wish to add (e.g., majors, terms).
3. Click the blue plus icon in the bottom right corner.
4. Under the **General** tab, add the **name** and the **code**.

   * Let's use a Biology major as an example. The name is a label that Element users and students will see. The code is used to integrate with other software when exported.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/134766967/d485d2b842dc04ac36d7ff73/Screen+Shot+2019-07-16+at+4.43.44+PM.png?expires=1784333700&signature=e22539f656adadb6d3bb871df379ed8c800e480376dc77f8b62a247ff3632618&req=dSMjEc94lIdYFb4f3HP0gLL8Osi6b0aE22BkRzV20kg9AYJddbq1mCnULJpu%0A6ak%3D%0A)](https://downloads.intercomcdn.com/i/o/134766967/d485d2b842dc04ac36d7ff73/Screen+Shot+2019-07-16+at+4.43.44+PM.png?expires=1784333700&signature=e22539f656adadb6d3bb871df379ed8c800e480376dc77f8b62a247ff3632618&req=dSMjEc94lIdYFb4f3HP0gLL8Osi6b0aE22BkRzV20kg9AYJddbq1mCnULJpu%0A6ak%3D%0A)
5. Click on the **Available For** tab. Here you will add a property to further define the major, term, or campus.

   * In this example, let's add the property **term** and specify that this major should be used for students interested in Fall 2020. ![](https://downloads.intercomcdn.com/i/o/1084909856/16325ddec49fbe3a2ebf9e63/Pro+Tip+-+Orng.png?expires=1784430000&signature=95dfc4d678ad788640953e6cc1fb0d0f0777ad0c2bbcaaa85579ce41851627b8&req=dSAvEsB%2BlIlaX%2FMW3Hu4gTWA6Vf1gJoQ4gK7RlDyth7SMUC0RRlAUONEZVV7%0AOw%3D%3D%0A) By applying Properties to these sources, you're able to build Reference Data Sources to only display subsets of values. For Example, if you create a major that has a property where the Term is Fall 2020, you can now build a Reference Data Source that will only display Majors where the term equals Fall 2020.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/134768347/358b8eb94e38cfec9b65f9b2/Screen+Shot+2019-07-16+at+4.48.20+PM.png?expires=1784333700&signature=cd55c8ca7fae386a20cb692b124a854dcc7865cb7b8484b3bea41d067c82b2ac&req=dSMjEc92noVYFb4f3HP0gAL1FWEqAnbxoERY2vQKXF8tFl9svMyFf9JVjQcN%0AIVI%3D%0A)](https://downloads.intercomcdn.com/i/o/134768347/358b8eb94e38cfec9b65f9b2/Screen+Shot+2019-07-16+at+4.48.20+PM.png?expires=1784333700&signature=cd55c8ca7fae386a20cb692b124a854dcc7865cb7b8484b3bea41d067c82b2ac&req=dSMjEc92noVYFb4f3HP0gAL1FWEqAnbxoERY2vQKXF8tFl9svMyFf9JVjQcN%0AIVI%3D%0A)
6. The last tab is **Integration Code.** Integration Codesare a common set of codes to map with other systems like Common App or Hobsons. Unless you're integrating systems, this can be left blank.

---

# Adding Items Automatically via Upload

Do you have a lot of items to add? Upload a list to make the process faster. Follow these steps:

1. Create an example item in **each** Data Source and fill in all the information.
2. Find the **download** button in the top right of the window. It looks like this:

   [![](https://downloads.intercomcdn.com/i/o/631122782/caf404ea3086fb6c0bf55599/download-upload-button.png?expires=1784333700&signature=19117e85cb36921b32a70a280bb65ca6d75f7d2d16bd9f62db4de4556d915f88&req=ciMmF8t8moldFb4f3HP0gAclQJG9gJhHFaYqTxmQ2hsbUByleG2vp4Q4CYdJ%0Av0E%3D%0A)](https://downloads.intercomcdn.com/i/o/631122782/caf404ea3086fb6c0bf55599/download-upload-button.png?expires=1784333700&signature=19117e85cb36921b32a70a280bb65ca6d75f7d2d16bd9f62db4de4556d915f88&req=ciMmF8t8moldFb4f3HP0gAclQJG9gJhHFaYqTxmQ2hsbUByleG2vp4Q4CYdJ%0Av0E%3D%0A)
3. Download the Data Source file and observe how the columns and data are structured.
4. Use a spreadsheet tool like Excel or Google Sheets to edit this file and add all of your items.

   * ![](https://downloads.intercomcdn.com/i/o/1084911811/c8b0ec82708de53f24cbec5f/Important+-+Orng.png?expires=1784430000&signature=2fe711d769dc9ce6c31f3255d3aaadb6837e9eac3efc3efde983e5fd5d1d1658&req=dSAvEsB%2FnIleWPMW3Hu4gX9M83fba2pUs2YHt7bXAdSgG61BIgdR5aKLKMdZ%0ANw%3D%3D%0A) *Leave the "guid" field blank*. GUID is an identifier specific to Element451. A GUID will be automatically generated for each new item you upload.
5. Once complete, save your file as a CSV.
6. In Element451, find the **upload** button next to the download button.
7. Select your file and upload it.
8. If needed, remove your example item.

---

# **Field Glossary**

Explore the information that should go in each item's field.

## Majors

Majors are typically used to denote programs or specific areas of study.

|  |  |  |
| --- | --- | --- |
| **Field** | **Recommended Data** | **Description** |
| Active | N/A | Set the Major to "Active" if the Major is still in use. Students will be able to select active majors when applying. |
| Name | A reader-friendly label. | The name will be seen by Element users and students when selecting this major. |
| Major Code | A code of letters or numbers. | The major code is best used for SIS integrations. Match the code with how the major is listed in your SIS. Not integrating with an SIS? Just copy the name. |

## Terms

Terms are typically used to group class start and end dates. Some follow seasons such as Fall and Spring. Others are based on quarters or other yearly divisions. Terms can be used to denote any period of time important to your institution.

|  |  |  |
| --- | --- | --- |
| **Field** | **Recommended Data** | **Description** |
| Active | N/A | Set the Term to "Active" if the Term is still in use. Students will be able to select active terms when applying. |
| Term Name | A reader-friendly label. | The name will be seen by Element users and students when selecting this term. |
| Term Code | A code of letters or numbers. | The term code is best used for SIS integrations. Match the code with how the term is listed in your SIS. Not integrating with an SIS? Just copy the name. |
| Term Start Date | A Date | Term Start Date should be set to the first day of the term, when classes or activities begin for students. |
| Term End Date | A Date | The Term End Date should be set to the last day of the term when classes or activities for students end. |
| Term Academic Year Starting In | A Year | The Term Academic Year is the academic year in which the term takes place. For example, Fall 2022, Winter 2022, and Spring 2023 traditionally take place in the 2022 Academic Year. |

## Degrees

|  |  |  |
| --- | --- | --- |
| **Field** | **Recommended Data** | **Description** |
| Active | N/A | Set the Degree to "Active" if the Degree is still in use. |
| Name | A reader-friendly label. | The name will be seen by Element users and students when selecting this degree. |
| Degree Code | A code of letters or numbers. | The degree code is best used for SIS integrations. Match the code with how the degree is listed in your SIS. Not integrating with an SIS? Just copy the name. |

## Campuses

Campuses are typically used for institutions that operate in multiple locations.

|  |  |  |
| --- | --- | --- |
| **Field** | **Recommended Data** | **Description** |
| Active | N/A | Set the Campus to "Active" if the Campus is still in use. |
| Name | A reader-friendly label. | The name will be seen by Element users and students when selecting this campus. |
| Country | A country name. | The country in which the campus is located. |
| Street | A street address. | The street address at which the campus is located. |
| City | A city name. | The city address at which the campus is located. |
| Zip/Postal | A ZIP code. | The ZIP code at which the campus is located. |

## Schools

Schools are typically used to list the academic departments within an institution.

|  |  |  |
| --- | --- | --- |
| **Field** | **Recommended Data** | **Description** |
| Active | N/A | Set the School to "Active" if the School is still in use. |
| Name | A reader-friendly label. | The name will be seen by Element users and students when selecting this school. |
| Code | A code of letters or numbers. | The school code is best used for SIS integrations. Match the code with how the school is listed in your SIS. Not integrating with an SIS? Just copy the name. |

---