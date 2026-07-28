---
title: Data Quality Guide
url: https://help.element451.com/en/articles/9006443-data-quality-guide
collection: Data Management
---

Use this quick guide to ensure your Import brings in clean data.

# Overview

Before importing data, it is incredibly important that the data be imported correctly and cleanly the first time. Use this guide to double check you have everything you need to import your data.

---

# Mapping Tab

On the Mapping tab, make sure:

* **Map at least one identity field**: Identity fields can be ID numbers, emails, and SSNs. Mapping one identity field will ensure that you can set up matching rules and prevent duplicate profiles from getting created when possible.
* **Map milestones when necessary**: Milestones are a criticaldata point within Element451. They will help you track students progression through your funnel. When importing form submissions, also map a Date of Inquiry Milestone. When importing applications, also map a Application Submitted Milestone. Learn more about [Milestones](https://help.element451.com/en/articles/3419189-milestones-an-overview).

  + **Map Milestone Terms & Dates** - When mapping milestones, map both the Term and Date. This is the bare minimum for making your milestones effective.
* **Double check all column settings are set up as intended**: Check that date, dropdown, checkbox, and radio fields all have proper transformations set up.

---

# Preview Tab

After creating you mappings and setting up all the column settings, head to the **Preview** tab. You will want to make sure the right column, labeled **Output**, is displaying the following formats:

|  |  |  |
| --- | --- | --- |
| **Field** | **Format** | **Example of Output Preview** |
| Dates | Y-m-dTH:i:s | 2022-06-01T00:00:00+00:00 |
| Majors | Guid Code | demo.majors.1234 |
| Terms | Guid Code | demo.terms.1234 |
| Campuses | Guid Code | demo.campus.123 |
| Sources | Taxonomy Code | demo.taxonomy.123456 |
| Source Segments | Taxonomy Code | demo.taxonomy.123456 |
| Labels | Taxonomy Code | demo.taxonomy.123456 |
| Degrees | Code | UG |
| Address State | Alpha 2 | NC |
| Address County | Alpha 3 | USA |

---

# Data Encoding

When preparing files for import into Element451, be sure to save them with **UTF-8 encoding**. This ensures that all characters—such as accented letters, special symbols, and non-English text—are read correctly by the system. If a file isn’t saved with UTF-8 encoding, you may see garbled characters, missing data, or import errors.

When saving .csv from Excel note the following:

1. **Windows Excel (most versions):** When you save a file as `.CSV`, Excel typically uses **ANSI encoding** by default, *not* UTF-8. This can cause issues with special characters (like ñ, ü, é).
2. **Mac Excel:** Usually saves `.CSV` files as **UTF-8 by default**, so it’s less of a problem.
3. **Excel 2016+ (Windows):** Microsoft added a “CSV UTF-8 (Comma delimited) (\*.csv)” option, which you must explicitly choose to get UTF-8 encoding.

---