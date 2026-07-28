---
title: Fields, Validation, + Conditional Logic
url: https://help.element451.com/en/articles/9093505-fields-validation-conditional-logic
collection: Data Management
---

Unlock efficient form design in Element451 with dynamic fields, conditional logic, and validation for smarter data collection.

# Overview

Data fields are the foundation of data collection in Element451. Applications, Event registrations, Appointments, Forms, and more use data fields to allow students to submit information about themselves. This guide is your key to configuring data fields in Element451.

## Field Categories: Fields, Groupings, Custom, Markdown

When you 'Add a Field' to any form, you are presented with **three** **categories** of fields to select: **fields**, **field** **groupings**, and **custom** **fields**.

### Fields

[![](https://downloads.intercomcdn.com/i/o/1000072148/1974bb3fb6aca43c70ebd1e0/Fields+-+Fields.png?expires=1784333700&signature=b84a6cdf54d9a4c1ca3908b2584a109d57430169c39c1f52236dd3256cd7baa1&req=dSAnFsl5n4BbUfMW1HO4zT4iLuMLH1hp02Wm3YFiz%2FgLv3qbSK1c9W2rPrEo%0AorXqCT0uwbJHPhyRxQA%3D%0A)](https://downloads.intercomcdn.com/i/o/1000072148/1974bb3fb6aca43c70ebd1e0/Fields+-+Fields.png?expires=1784333700&signature=b84a6cdf54d9a4c1ca3908b2584a109d57430169c39c1f52236dd3256cd7baa1&req=dSAnFsl5n4BbUfMW1HO4zT4iLuMLH1hp02Wm3YFiz%2FgLv3qbSK1c9W2rPrEo%0AorXqCT0uwbJHPhyRxQA%3D%0A)

This tab contains single, pre-made fields. These are standard fields, such as name, date of birth, term, and major. These fields already have validation (covered in more detail below) and other options for you. For example, the country of citizenship field comes pre-populated with a list of countries, so you don't need to create that list for people to choose from.

[Explore More on Field Management →](https://help.element451.com/en/articles/9118615-field-management)

### Groupings

[![](https://downloads.intercomcdn.com/i/o/1000072457/ccec8720bf05b85e822743ad/Events+-+Groupings.png?expires=1784333700&signature=44cd33b7cfa3a2657fa115b65b2a672cb77fa94554e42fa2f3802c39c702a658&req=dSAnFsl5n4VaXvMW1HO4zcQO2wUSM0rdTYDaJoditRiXYYFYxCYR87vHBqlc%0AQ4tB3pysAn7lWEp6cJ8%3D%0A)](https://downloads.intercomcdn.com/i/o/1000072457/ccec8720bf05b85e822743ad/Events+-+Groupings.png?expires=1784333700&signature=44cd33b7cfa3a2657fa115b65b2a672cb77fa94554e42fa2f3802c39c702a658&req=dSAnFsl5n4VaXvMW1HO4zcQO2wUSM0rdTYDaJoditRiXYYFYxCYR87vHBqlc%0AQ4tB3pysAn7lWEp6cJ8%3D%0A)

Grouped fields consist of multiple fields. Address is a good example. You would select the grouped address field rather than manually adding the individual fields (street address, city, state, etc.). Groupings are great for standard information but are limited in that the fields in the grouping can't interact with each other as they can with conditional logic (explained below).

[Explore More on Field Groupings →](https://help.element451.com/en/articles/2582910-field-groupings)

### Custom

[![](https://downloads.intercomcdn.com/i/o/1000072538/9483dce6466556134f6b3235/Events+-+Custom.png?expires=1784333700&signature=ee7b4fe59ca05e5356ab4626d17bd0987f5783604ed807708d554ad06e71e3c0&req=dSAnFsl5n4RcUfMW1HO4zSQRO0mOOBCWGfyH0nmIDah%2FhjJ5y%2FwNAJAmaxGZ%0ADLoII0ys1%2Bisoq9PjT8%3D%0A)](https://downloads.intercomcdn.com/i/o/1000072538/9483dce6466556134f6b3235/Events+-+Custom.png?expires=1784333700&signature=ee7b4fe59ca05e5356ab4626d17bd0987f5783604ed807708d554ad06e71e3c0&req=dSAnFsl5n4RcUfMW1HO4zSQRO0mOOBCWGfyH0nmIDah%2FhjJ5y%2FwNAJAmaxGZ%0ADLoII0ys1%2Bisoq9PjT8%3D%0A)

Fields that you or your team members have already created. Event451 saves your fields here, so you don't have to recreate them. This is especially helpful for frequently used fields.

[Explore more on custom fields →](https://help.element451.com/en/articles/9118615-field-management#h_a1d5422c73)

### New, Markdown

[![](https://downloads.intercomcdn.com/i/o/1000072640/250b4ffd868386353557aaec/Event+-+Markdown.png?expires=1784333700&signature=dac462277eff20307c7d4a7d2ab1cc477e36ef1e966cf8b62844bde0314e53e4&req=dSAnFsl5n4dbWfMW1HO4zb2VNAJky6WyKLi9sevBqN32hXJsXaDrgxgvZNkp%0AX2x47Yit8LYbkDpkRkI%3D%0A)](https://downloads.intercomcdn.com/i/o/1000072640/250b4ffd868386353557aaec/Event+-+Markdown.png?expires=1784333700&signature=dac462277eff20307c7d4a7d2ab1cc477e36ef1e966cf8b62844bde0314e53e4&req=dSAnFsl5n4dbWfMW1HO4zb2VNAJky6WyKLi9sevBqN32hXJsXaDrgxgvZNkp%0AX2x47Yit8LYbkDpkRkI%3D%0A)

Rather than a field for gathering information, this is a field for displaying text within a form. You can format the text with markdown tags.

[![](https://downloads.intercomcdn.com/i/o/1000069718/4b06f2c828616ba03a1b210a/Note+-+Orng.png?expires=1784333700&signature=24af2ea6defdd1c41239004a3b26fc4db973c36adcd3fc3ca67253a769ba60e4&req=dSAnFsl4lIZeUfMW1HO4zcOylatSxAZUUNZii%2FXUO2YgpF%2Fmg6LJ%2F5eWcyfq%0Ah0L08u9rm%2FZ3mKiqdfA%3D%0A)](https://downloads.intercomcdn.com/i/o/1000069718/4b06f2c828616ba03a1b210a/Note+-+Orng.png?expires=1784333700&signature=24af2ea6defdd1c41239004a3b26fc4db973c36adcd3fc3ca67253a769ba60e4&req=dSAnFsl4lIZeUfMW1HO4zcOylatSxAZUUNZii%2FXUO2YgpF%2Fmg6LJ%2F5eWcyfq%0Ah0L08u9rm%2FZ3mKiqdfA%3D%0A)

Element451 can encounter rendering issues when generating PDFs of applications or forms that contain long Markdown fields. If a Markdown field extends beyond one page, it may cause problems such as cut-off content, blank pages, or other formatting anomalies.  
​

It is generally **not recommended to use lengthy Markdown fields**, especially for terms, conditions, or other long text blocks. It is best to link from your form to a webpage or other document that outlines all your Terms and Conditions.  
​

If you need to display long content, the best practice is to **split the text into multiple shorter Markdown fields** rather than placing everything in a single field.  
​

As a guideline, **one page of Markdown is approximately 2,400 characters**, or about **3–5 short paragraphs**.

---

# General

Once you've selected a field type from the list of pre-made fields or created a new field, you'll be able to customize it. This may mean adjusting settings or, in the case of new fields, entering them for the first time.

The General tab is where you'll enter the basic information required for your field and details about how it should be displayed. Depending on the type of field you selected, these options will be different.

[![](https://downloads.intercomcdn.com/i/o/1000073603/df0ae316657e994f4509d513/Fields+-+General.png?expires=1784333700&signature=088c9321ed9f823b282de99f7eb6dcdb76fdbc20df24699d93a4e5cd4bb01208&req=dSAnFsl5nodfWvMW1HO4ze%2Bvog41yOXg0RIMiJIL%2F%2B9TItwmE1wm6dxgnFZ8%0A9fkEsZ96PcMDvl3UXsk%3D%0A)](https://downloads.intercomcdn.com/i/o/1000073603/df0ae316657e994f4509d513/Fields+-+General.png?expires=1784333700&signature=088c9321ed9f823b282de99f7eb6dcdb76fdbc20df24699d93a4e5cd4bb01208&req=dSAnFsl5nodfWvMW1HO4ze%2Bvog41yOXg0RIMiJIL%2F%2B9TItwmE1wm6dxgnFZ8%0A9fkEsZ96PcMDvl3UXsk%3D%0A)

## General Section Configurations

* **Label:** The title of the field that will be displayed on the form. E.g., First Name.
* **Description:** This allows for an internal description of the field.
* **Required:** The field must be filled out. If it's skipped, the form won't submit.
* **Hidden**: The field will not be visible to the person completing the form. This option is useful when combined with a default value. This way, the person completing the form can't change the value. A great use case for this is when [embedding RFI forms on your program pages](https://help.element451.com/en/articles/9000414-embedding-forms-on-pages-external-sites).

  + When a Hidden field has a Default Value set, that value is automatically included when the form is submitted. This applies to standard submissions such as Forms, event registrations, and application registration forms.
  + Fields inside an application section behave differently: they save as the applicant interacts with them, and applicants never interact with hidden fields. For a hidden field's default value to save in an application section, enable the field's **Save Default Value** toggle. The value is captured when the applicant registers for (starts) the application, so the toggle must be on before registration.
* **Help Text:** This appears with the field. Use it to help guide people about what they should enter or the format they should use. Examples are good ways to provide help text.
* **Default Value:** Some fields allow you to have a value pre-populated. "Value" is simply the content in a field. For example, in a major field, the name of a major entered is the value.
* **Size:** How much of the screen should this field occupy? The choices are full, half, third, and fourth. You can have one, two, three, or four fields on a line, assuming the size of the other fields is set similarly.
* **New Line:** When this is toggled to Yes, your field will start on a new line. When combining fields onto one line, toggle this to No.
* **Autocomplete**: If you have **autocomplete** turned on, check the box next to the option you want to be pre-populated on the form.
* **Default Date:** This is the equivalent of autocomplete for date fields. You can choose "today" or a time in the past or future. Since these dates change, selecting "today" will always fill in the day when the form is viewed.
* **Options:** For fields like checkboxes, dropdown, and radio buttons that show a list of things for people to select from, you create the list by clicking Add Option and entering the information:
* **Label and Value:** The label is displayed to the person filling out the form; the value is what will be saved in the system when the form is submitted.

---

# Validation

Validation helps ensure that people enter the information you are looking for. For example, letters rather than numbers in a name field or a certain number of characters in a text area. Some things to keep in mind:

* You can add multiple validations to a single field.
* Validation options can be contingent upon other fields. For example, a field may only be required if another field chooses a certain option but can otherwise be skipped.
* You do not need to add a mask validation to like SSN and phone number. Element451 has system validation that ensures those fields are entered correctly.

## Validation Options Explained

[![](https://downloads.intercomcdn.com/i/o/1000082152/07c38488f94fa105494b076b/Events+-+Validation.png?expires=1784333700&signature=5d6ec7656fbbb77681febd55a446137a070e6762ad59685ff59c73e64b65cac7&req=dSAnFsl2n4BaW%2FMW1HO4zZQBwH4mEjxEBzbKwrB01qEm5IOhm5%2BZDqohKbXr%0AfAfrQunpJkzXq%2FkCdxc%3D%0A)](https://downloads.intercomcdn.com/i/o/1000082152/07c38488f94fa105494b076b/Events+-+Validation.png?expires=1784333700&signature=5d6ec7656fbbb77681febd55a446137a070e6762ad59685ff59c73e64b65cac7&req=dSAnFsl2n4BaW%2FMW1HO4zZQBwH4mEjxEBzbKwrB01qEm5IOhm5%2BZDqohKbXr%0AfAfrQunpJkzXq%2FkCdxc%3D%0A)

* **Required**: A value is required in the field.
* **Required If:** The person must provide a value in the field only if the parameters are met. When this option is chosen, you will be asked to choose the field and value(s) that will make this field required. For example, if you have a checkbox field with many choices and one of them is "Other, please explain," you can create a text field that is required if the "Other, please explain" option is checked to ensure that you get an explanation with the choice.
* **Letter Only:** The entered value must be letters only, no numbers. This is used mainly in name fields to standardize input.
* **Letters + Spaces Only**: The entered value can only contain letters and spaces.
* **Letters + Numbers Only**: The entered value can only contain letters and numbers.
* **Letters + Dash Only**: The entered value can only contain letters and dashes.
* **Min/Max Word Count:** For **text area** fields, you can set a minimum and/or maximum number of words. Respondents see a word count indicator and cannot submit unless their response falls within the specified range. Ideal for essay prompts and personal statements.
* **Numeric Only**: The entered value can only contain numbers.

  + [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356767614/7c314a35127844c7d3b1721ae842/Note.png?expires=1784333700&signature=611e71a4933062d9cf05420b56358a57a4c2603a8cc23d7ff1e936b446a9cffa&req=dSMiEM54modeXfMW1HO4zY0ZZjNbiH5EaxYPxgqzMtgbhOedALWOBruAwiEE%0A9PJr%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356767614/7c314a35127844c7d3b1721ae842/Note.png?expires=1784333700&signature=611e71a4933062d9cf05420b56358a57a4c2603a8cc23d7ff1e936b446a9cffa&req=dSMiEM54modeXfMW1HO4zY0ZZjNbiH5EaxYPxgqzMtgbhOedALWOBruAwiEE%0A9PJr%0A)

    When **Numeric** **Only** is combined with **Min/Max Length**, it treats the maximum value as a **numerical limit** rather than a character count. If you need to enforce a strict number of digits (e.g., ID number), you should use a **Mask Validation** instead.
* **SSN**: The entered value must be 9 digits, the value cannot be all one number, the value cannot be 123-45-6789, the value cannot have 00 as the middle number, and the value cannot have 0000 as the last number.
* **Email:** The entered value must fit the pattern of accepted email addresses.
* **URL**: The entered value must fit the pattern of a URL.
* **Max/Min Length:** The entered value must be below the maximum or above the minimum number of **characters**. Combining the two can guarantee the length of what is entered in the field.

  + [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356767614/7c314a35127844c7d3b1721ae842/Note.png?expires=1784333700&signature=611e71a4933062d9cf05420b56358a57a4c2603a8cc23d7ff1e936b446a9cffa&req=dSMiEM54modeXfMW1HO4zY0ZZjNbiH5EaxYPxgqzMtgbhOedALWOBruAwiEE%0A9PJr%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356767614/7c314a35127844c7d3b1721ae842/Note.png?expires=1784333700&signature=611e71a4933062d9cf05420b56358a57a4c2603a8cc23d7ff1e936b446a9cffa&req=dSMiEM54modeXfMW1HO4zY0ZZjNbiH5EaxYPxgqzMtgbhOedALWOBruAwiEE%0A9PJr%0A)

    You should not use Max/Min Length validation on fields that require only numbers. When **Min/Max Length** is combined with the **Numeric Only** validation, it treats the maximum value as a numerical limit rather than a character count. If you need to enforce a strict number of digits (e.g., ID number), you should use a **Mask Validation** instead.
* **Person** **Name**: The entered value can contain letters, apostrophes, hyphens, or numbers. Name validation allows numbers but restricts certain special characters. The following characters **cannot** be used in names:  
  ​

  `+ & | ! < > ( ) { } [ ] ^ " ~ * ? : @ # % = \ /`

  Name validation is inherently complex—while we aim to balance flexibility and accuracy, there’s no perfect rule set that covers every scenario. Similarly, we do **not** auto-correct or force capitalization, as name formatting varies widely.  
  ​
* **Mask**: The entered value must match a specific format, defined by you.

  + [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356773805/7c246f10f38d3493a6beebf4bb7e/Important.png?expires=1784333700&signature=32d0003c1a66817a851940850690e71fade68100c4cb86d13be31386dd85a533&req=dSMiEM55nolfXPMW1HO4zWDn%2F7qv1b5zSY008vajThBctPPKChkGRRZzumpe%0AgOye%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356773805/7c246f10f38d3493a6beebf4bb7e/Important.png?expires=1784333700&signature=32d0003c1a66817a851940850690e71fade68100c4cb86d13be31386dd85a533&req=dSMiEM55nolfXPMW1HO4zWDn%2F7qv1b5zSY008vajThBctPPKChkGRRZzumpe%0AgOye%0A)

    You should not add masks to special fields like **SSN** and **phone** **number**. Element451 has system validation that ensures those fields are entered correctly.
  + Examples:

    - 00000000 → Enforces exactly **8-digit numeric** entries (e.g., IDs).
    - 99/99/9999 → Enforces **MM/DD/YYYY date format**.
    - AA-0000 → Enforces a pattern of **two letters followed by four numbers** (e.g., ID formats like AB-1234).
* **Before/After Date:** For the date field, you can be sure the date value submitted is before or after a specified date.

---

# Field Options

For fields that use options (checkbox, dropdown, and radio button), you can use a **[data](https://help.element451.com/en/articles/2066888-data-sources)** [**source**](https://help.element451.com/en/articles/2066888-data-sources) to populate the options rather than creating them manually. A list of majors is a good example of when you would want to use a data source rather than entering items individually. This not only saves time but also ensures accuracy and consistency.

* To use a data source in a form, you must first create it by going to **Data** > **Data** **Sources** on the left-hand menu if the source hasn't been created yet.

[![](https://downloads.intercomcdn.com/i/o/1000082761/94c7eb08eb74a5a8190ce610/Events+-+Field+Options.png?expires=1784333700&signature=bbff0cd2826946f390ee73d9e2d4b8eb988ee711c845ce500c58b38df7bc4c85&req=dSAnFsl2n4ZZWPMW1HO4zVpgAEWIx24mL6dmwcoXczH5%2BW2I%2B05QMqbl0y1R%0AeQDWC2snfy7f8Z%2BdQBM%3D%0A)](https://downloads.intercomcdn.com/i/o/1000082761/94c7eb08eb74a5a8190ce610/Events+-+Field+Options.png?expires=1784333700&signature=bbff0cd2826946f390ee73d9e2d4b8eb988ee711c845ce500c58b38df7bc4c85&req=dSAnFsl2n4ZZWPMW1HO4zVpgAEWIx24mL6dmwcoXczH5%2BW2I%2B05QMqbl0y1R%0AeQDWC2snfy7f8Z%2BdQBM%3D%0A)

## Using a Data Source

1. Toggle **Use values from data sources?** to Yes.
2. Select the data source from the dropdown of all the available data sources. This list will include custom sources as well as system ones. Depending on the selected data source, you may see options to indicate:

   * **Name Field:** This is the field from the data source shown on the form. You can go to the data source (Data > Data Sources) to see what these options correspond to, as they will be different depending on the data source.
   * ​**Value Field:** This value will be saved when the form is submitted.

[Explore more on Data Sources →](https://help.element451.com/en/articles/2066888-data-sources)  
​

## Filters

Use filtering in your application, form, or event registration when using any of these fields: *majors*, *terms*, *degrees*, *campuses*, and *schools*. This method restricts field options based on previous answers. For example, if your institution only accepts nursing applications for the fall, adding a filter would automatically adjust the form to reflect that requirement.

[Explore more on Field Filtering →](https://help.element451.com/en/articles/7321011-field-filtering)

📌 **Note:** On **optional** dropdown and radio button fields, applicants can clear a previously selected value and return the field to a blank state, so a selection is never locked in. Required fields do not offer this, since a value must always be provided.

---

# Conditional Logic

Conditional logic allows you to tailor the form based on user responses, making it more intuitive. You control which fields are displayed to the person based on their previous answers or selections of other fields in the form, making the form seem less daunting and more personalized. In other words, "show this field if..."

If conditions are not met, the field will be hidden.

## Adding Conditional Logic

1. When configuring your field, you'll see a **Conditional Logic** section.
2. Click **Add Condition** to get started adding your first condition.

[![](https://downloads.intercomcdn.com/i/o/1000083434/5c42bc8caef002e98190b068/Events+-+Cond+Logic.png?expires=1784333700&signature=6efe0a03d4d3535b4d866ebc46c2a16e08bc93f90acbb90c88e5308f3e08055b&req=dSAnFsl2noVcXfMW1HO4zReLNJBKiozU1Vha3hKnKH5dQa1JOkfxQBsmqYYb%0Ain2dLIgzUmAha7saOm0%3D%0A)](https://downloads.intercomcdn.com/i/o/1000083434/5c42bc8caef002e98190b068/Events+-+Cond+Logic.png?expires=1784333700&signature=6efe0a03d4d3535b4d866ebc46c2a16e08bc93f90acbb90c88e5308f3e08055b&req=dSAnFsl2noVcXfMW1HO4zReLNJBKiozU1Vha3hKnKH5dQa1JOkfxQBsmqYYb%0Ain2dLIgzUmAha7saOm0%3D%0A)

* **Field:** The other field on the form this one depends on.
* ​**Operator:** The logical operator to use on the values we will specify next. These are classic logical operators.
* **Equals:** Displays the field if the value in the specified field is exactly equal to a single value.
* **Does Not Equal:** Displays the field if the value in the specified field is not equal to a single value.
* **In**: Displays the field if it matches any values in a set. You can specify multiple values to look for with this operator.
* **Not In:** Displays the field unless any of the values in the set are found in the specified field. You can specify multiple values with this operator.
* **Value(s):** Specify what value (**Equals** or **Does** **Not** **Equal**) or set of values (**In** or **Not** **In**) your operator will be looking for. So, for example, if the field you're adding is a text field asking how many guests a person is bringing to the event, and the field this field is dependent on asks, "Are you bringing a guest?" the value would be Yes or No.

**Important Notes**

* If the dependent field uses options (e.g., checkbox, radio button, dropdown), you can select the value from a list of the options for the field. If you can select multiple options with your operator, you can click the ones you want to include.
* You can add multiple conditions to achieve the desired behavior.
* Often, the best way to learn how your form fields interact is to try them out. Many of the modules where build forms allow you to preview.

---

# Troubleshooting + FAQ

Check out our [Data: Frequently Asked Questions](https://help.element451.com/en/articles/10606718-data-frequently-asked-questions) article for answers to some of our most commonly asked questions about fields, validation, and conditional logic.

---