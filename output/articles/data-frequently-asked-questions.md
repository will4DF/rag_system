---
title: 📌 Data: Frequently Asked Questions
url: https://help.element451.com/en/articles/10606718-data-frequently-asked-questions
collection: Data Management
---

Commonly asked questions about data-related topics, such as Import + Export, Data Sources, and Fields.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389599138/57eba481d1d8f64237e78aa05ec7/Pardon+our+Progress.png?expires=1784333700&signature=9d20d8e00a47ffed43a539ff4690448f0e36db49108594d5e75957555c2692bc&req=dSMvH8x3lIBcUfMW1HO4zWJULrYo5JYpzXLH1Ku9M%2BIPGuRqgIzutNFtxbav%0AJvbQxFj3%2F%2F3oqj2UiGw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389599138/57eba481d1d8f64237e78aa05ec7/Pardon+our+Progress.png?expires=1784333700&signature=9d20d8e00a47ffed43a539ff4690448f0e36db49108594d5e75957555c2692bc&req=dSMvH8x3lIBcUfMW1HO4zWJULrYo5JYpzXLH1Ku9M%2BIPGuRqgIzutNFtxbav%0AJvbQxFj3%2F%2F3oqj2UiGw%3D%0A)

# Import + Export

## General

### What does “Import New and Update Existing” mean when importing data?

When using this option, Element451 checks for matches against existing records:

* **If a match is found,** the record is updated, meaning any fields that differ in the import will overwrite existing data. However, fields already on the record but not included in the import will remain unchanged.
* **If no match is found,** a new record is created.

This ensures that existing records stay current without losing data that isn’t explicitly updated in the import.

### How can I ensure that labels are correctly imported in Element451?

When importing a label in Element451, ensure that the line in the import is a calculated line with the quotations in the formula. In your CSV import, use the taxonomy code instead of the label name. The taxonomy code follows a format similar to `organization.taxonomy.number`. If multiple labels need to be imported, place each taxonomy code inside the quotations with commas in between each label. Check out our article on [Calculated Fields](https://help.element451.com/en/articles/9007704-calculated-fields) to learn more about custom import/export formulas.

### Can we create a backup of all our student data to a CSV file?

Yes, you can create a one-time or scheduled export with as many fields as you'd like that will be sent to you daily to serve as a backup.

### How can I export all activity and conversation data from a student's profile?

Unfortunately, there's no direct way to download or export all Activity and Conversations from a specific student profile. To get this information, you would need to review and document the information manually. Using the Import + Export module, you can export repeat fields based on contact data, applications, decisions, decisions checklist, education, emergency contacts, employment, evaluations, events, holds, milestones, networks, notes, payments, and sources.

### Do API keys expire?

No, API keys do not have an expiration date.

### After importing data, I see some characters are garbled or missing.

When preparing files for import into Element451, be sure to save them with **UTF-8 encoding**. This ensures that all characters—such as accented letters, special symbols, and non-English text—are read correctly by the system. If a file isn’t saved with UTF-8 encoding, you may see garbled characters, missing data, or import errors.

When saving .csv from Excel note the following:

1. **Windows Excel (most versions):** When you save a file as `.CSV`, Excel typically uses **ANSI encoding** by default, *not* UTF-8. This can cause issues with special characters (like ñ, ü, é).
2. **Mac Excel:** Usually saves `.CSV` files as **UTF-8 by default**, so it’s less of a problem.
3. **Excel 2016+ (Windows):** Microsoft added a “CSV UTF-8 (Comma delimited) (\*.csv)” option, which you must explicitly choose to get UTF-8 encoding.

## Document Exports

### Is there a limit to how many documents I can export at once?

Document exports perform best on batches of up to **10,000 files**. Larger exports aren't guaranteed to complete reliably and may fail during processing or delivery. For high-volume needs, use the filters under **Files > Advanced Settings** (such as Date, User Segment, or Size) to split the export into smaller batches, or schedule recurring exports.

### Can I filter my document export using document tags?

Yes, when exporting documents from either the *General Bin* or *User Bin* source, you can add a document tag filter condition.

### How do I automatically add a document tag to exported documents?

1. When creating or editing an export, go to the **Files** tab.
2. Click the **Tag Exported Documents** button.
3. Make sure the tag already exists by adding it to a document in the **Documents Bin** first.

### After importing data, I see some characters are garbled or missing.

When preparing files for import into Element451, be sure to save them with **UTF-8 encoding**. This ensures that all characters—such as accented letters, special symbols, and non-English text—are read correctly by the system. If a file isn’t saved with UTF-8 encoding, you may see garbled characters, missing data, or import errors.

When saving .csv from Excel note the following:

1. **Windows Excel (most versions):** When you save a file as `.CSV`, Excel typically uses **ANSI encoding** by default, *not* UTF-8. This can cause issues with special characters (like ñ, ü, é).
2. **Mac Excel:** Usually saves `.CSV` files as **UTF-8 by default**, so it’s less of a problem.
3. **Excel 2016+ (Windows):** Microsoft added a “CSV UTF-8 (Comma delimited) (\*.csv)” option, which you must explicitly choose to get UTF-8 encoding.

---

# Document Management

### How can I manage documents from repeat applicants and create new fields without causing issues in an open application?

To prevent repeat applicants' previous documents from linking to a new application, you can update the fields used. For instance, if a document was uploaded to a field like user-custom-smwc-lor, you can create a new field for the current year, such as user-custom-smwc-lor-2025, ensuring all documents are directed to the new field. When creating new fields with an open application, future submissions will store information in these new fields. Depending on your data management needs, you may need to manually add data to the new fields or ensure both old and new fields are included in any segments, exports, workflows, etc. This approach helps maintain data integrity and organization.

### Can I change the name of a document that a student uploaded?

Yes, you can rename a student-uploaded document from the Documents Bin. To do this:

1. Navigate to **Data + Automations** > **Documents** > **Documents** **Bin**.
2. Locate the file you want to rename.
3. Click the **eye** **icon** to open the document.
4. Click anywhere on the document name to edit it.
5. Your changes will be saved automatically.

### How do I add a document tag?

To add a document tag:

1. Navigate to **Data + Automations → Documents → Documents Bin**.
2. Locate the document you want to tag.
3. Click the **View (👁️)** icon.
4. Scroll to the bottom and click **+Add Document Tag(s)**.
5. Select an existing tag or type a new tag name and press **Enter** to create it.
6. Click **Add** to save.

*Note: This is also how you create a new tag—there is currently no centralized location for managing document tags. The tag must be added to at least one document to exist.*

### Are documents uploaded by contacts/students scanned for viruses/malware?

Yes. Any file uploaded by contacts—whether through forms, applications, or other upload fields—is automatically scanned for malware and viruses. Element451 uses **[BucketAV](https://bucketav.com/)**, a cloud-based antivirus tool designed for secure file scanning.

---

# Data Sources

### How can I ensure the correct terms, majors, etc., appear in my application?

Use a **Reference Data Source** to filter and display only the relevant Majors, Terms, Degrees, and more. Reference Data Sources allow you to create sub-groupings based on specific properties (e.g., Fall 2024 Majors) to ensure your forms pull only the appropriate options. This is especially useful for limiting selections to active terms rather than including past ones. [Learn more here](https://help.element451.com/en/articles/2066888-data-sources#h_cd7ad1d087).

### Why doesn’t the order of my data sources match on profile cards?

All options on profile cards are automatically sorted alphabetically. This is system-defined behavior and may differ from the custom order you see in your data sources list. Index weights only apply to student-facing items, such as forms and applications.

---

# Fields

### What field type is best for adding an agreement statement/clause at the end of my application?

Markdown fields and other fields within Element451 are not designed for large amounts of text that span multiple paragraphs. Our recommendation if you were looking for a solution to display content similar to a 'terms and conditions' would be to include a short amount of text and link to another source (e.g., Do you agree to the following terms and conditions regarding payment of fees and student conduct? The full terms can be found at fire.edu/terms).

### When should I use the "Toggle" display option for form fields?

Use the Toggle option only for short lists with two to three concise options, such as Yes/No. Toggle is **not** optimized for long lists or lengthy text. On mobile devices, options may not fit the screen properly. For fields with many options or longer labels, keep the display set to **Default**. This ensures your form stays clean, readable, and mobile-friendly.

---

# Conditional Logic

### If a field is required and a person doesn't meet the conditional logic, will that prevent them from moving forward?

If a field in an application is marked as required but has conditional logic applied that the applicant's responses do not satisfy, the field will not be shown to the applicant. In such cases, the requirement for that field is effectively bypassed, enabling the applicant to submit the application without completing that specific field.

---

# Validation

### The error message “Sorry, something went wrong” appeared when submitting a form. What should I check?

This error often occurs due to issues with form field validation. Start by reviewing your form fields, especially those using numeric validation. Check if any fields use Numeric Only validation combined with Max Length or Min Length. This can cause unexpected behavior because Max Length is treated as a maximum numerical value, not a character limit.

* To configure fields that require a specific number of numeric digits, the best practice is to the **Text** field type with **Mask** validation (e.g., For an **8-digit ID field**, apply **Mask Validation** with 00000000. This guarantees exactly 8 digits and prevents letters from being entered.).

---