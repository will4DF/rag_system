---
title: 📌 Forms: Frequently Asked Questions
url: https://help.element451.com/en/articles/10602253-forms-frequently-asked-questions
collection: Forms
---

This article answers commonly asked questions about Forms, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389354794/828294d933cf0fcf38e6a3c8557f/Pardon+our+Progress.png?expires=1784333700&signature=003b41804d19d40ff73a2026000fc9e955a50f070a1aca9999d9279d5aa6dd1d&req=dSMvH8p7mYZWXfMW1HO4zW2Ssseor0hT44Ia3CZOLgRq01PFiZHReaZw9iDR%0AhJ8rwwNqLs87xAx7fLA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389354794/828294d933cf0fcf38e6a3c8557f/Pardon+our+Progress.png?expires=1784333700&signature=003b41804d19d40ff73a2026000fc9e955a50f070a1aca9999d9279d5aa6dd1d&req=dSMvH8p7mYZWXfMW1HO4zW2Ssseor0hT44Ia3CZOLgRq01PFiZHReaZw9iDR%0AhJ8rwwNqLs87xAx7fLA%3D%0A)

# General

## How can I share a form URL?

To share a form URL, click the **“Preview Form”** button in the header when viewing the form. This opens the form in a new tab, where you can copy the URL directly from your browser.

For an easy sharing option, you can also generate a **QR code** using the QR code button next to the preview button. This creates a scannable shortcut to the same URL.

---

# Creating Forms

## How can I add a data source to a form?

You can't add a data source directly to a form. You have to add the data source to a field, then add the field to the form. Here is the correct order to follow:

1. Create a regular data source.

   (Data + Automation > Data Sources > Add Data Source)
2. Create a custom field.   
   (Data + Automation > Field Management > Custom Fields)
3. Select "Use data source" on the custom field to link them.
4. Add the custom field to the form.

## Can I use query string parameters to control form fields?

Not currently. Because we recommend using iframe embeds for forms, the form itself does not have access to query string parameters. We recommend using [Conditional Logic](https://help.element451.com/en/articles/9093505-fields-validation-conditional-logic) and [Field Filtering](https://help.element451.com/en/articles/7321011-field-filtering) within the form itself to show or hide fields based on user responses dynamically. This lets you control the form experience without relying on query string parameters.  
​

## Can group field subfields share a line with other fields?

No. **Group Fields**, such as Phone or Address, are designed to keep their sub-fields visually grouped together on forms. A group will always display at full width and forces a new line after the group. As a result, sub-fields within a Group Field cannot share a line with other fields.

## Do hidden fields save their default values when a form is submitted?

Yes, for standard form submissions (Forms module, event registrations, appointment scheduling, and application registration forms), a Hidden field's Default Value is automatically saved with every submission.

The exception is fields inside an application section. Those fields only save their hidden default if the field's **Save Default Value** toggle is enabled. If default values aren't saving on applications, check that toggle first. Note that the value is captured when the student registers for the application, not at submission, so enabling the toggle only affects future registrations.

---

# Form Submission Process

## Does submitting a form create a Date of Inquiry milestone?

It depends on the form type (Prospect or Simple). You can adjust the form type based on your preference:

* **Prospect:** Creates a Date of Inquiry milestone when submitted
* **Simple:** Does **not** create a Date of Inquiry milestone.

## A user got an error message when trying to submit a form. Why?

If your form uses [access rules](https://help.element451.com/en/articles/12987558-access-rules) that restrict who can submit it, forms display a error message when a visitor does not meet the access criteria. Confirm the user has access.

---

# Validations

## Can I set a word count requirement on a text field?

Yes. Text area fields support Min/Max Word Count validation. Edit the field → Validation tab → add a Min Word Count or Max Word Count rule.

---

# Troubleshooting

## There is an error message when attempting to complete my form.

Here are two common reasons why an error message may appear:

* All Forms must contain the Email Address `user-email-address` field. If you remove this field and try to submit the form, you will get an error.

* Errors can occur due to **field** **[validation](https://intercom.help/element451/en/articles/9093505-fields-validation-conditional-logic)** issues. Start by reviewing your form field. Check if any fields use **Numeric Only** validation **combined with Max Length or Min Length**. This can cause unexpected behavior because Max Length is treated as a maximum numerical value, not a character limit. To configure fields that require a specific number of numeric digits, the best practice is to use the **Text** field type with **Mask** validation (e.g., For an **8-digit ID field**, apply **Mask Validation** with 00000000. This guarantees exactly 8 digits and prevents letters from being entered.).

---