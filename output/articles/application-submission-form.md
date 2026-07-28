---
title: Application Submission Form
url: https://help.element451.com/en/articles/10869730-application-submission-form
collection: Applications
---

# Overview

The Application Submission Form is the final checkpoint in your application process, designed to gather essential information from applicants before they finalize their submissions. This strategic component serves multiple critical functions:

* Collects sensitive but necessary information required for legal compliance or institutional criteria
* Provides a dedicated space for applicant consent and agreements
* Supports conditional logic to show relevant questions based on applicant circumstances
* Creates a standardized way to identify applications that may need additional review

The Submission Form appears as the last step before an application is completed, ensuring all critical information is captured before the applicant finalizes their submission. The form appears as a modal/pop-up.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1433946443/b441f5190d4665c845ff4fcf6b6b/Submission%2BForm.png?expires=1784333700&signature=5205527d0cabf7fec2170b8319a45bf38e1d7aaf447a6901c3f57d23582f4f8b&req=dSQkFcB6m4VbWvMW1HO4zRbjEyj1ZVDwmryRml3ILBw2%2BIgqFtizppUbfXj%2B%0AfH3GZlKViIlZWS%2BgpfA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1433946443/b441f5190d4665c845ff4fcf6b6b/Submission%2BForm.png?expires=1784333700&signature=5205527d0cabf7fec2170b8319a45bf38e1d7aaf447a6901c3f57d23582f4f8b&req=dSQkFcB6m4VbWvMW1HO4zRbjEyj1ZVDwmryRml3ILBw2%2BIgqFtizppUbfXj%2B%0AfH3GZlKViIlZWS%2BgpfA%3D%0A)

---

# Form Fields

## Default Fields

By default, the following fields are automatically added to the Submission Form section:

* Have you ever been expelled or academically dismissed from school? (`user-applications-submission-school-problems`)
* Please Explain (`user-applications-submission-school-problems-explanation`)
* Have you ever been convicted of a felony? (`user-applications-submission-convicted`)
* Please Explain (`user-applications-submission-convicted-explanation`)
* Markdown Field (custom text that corresponds to the agreement acknowledgment)
* I Agree (`user-applications-submission-legal-note-confirm`)
* Sign your name (`user-applications-submission-electronic-sign`)

You can edit these labels and help text in the submission form settings to better match your institution's terminology or requirements. Or, if you choose, you can delete the default fields.

## Custom Fields

You can customize the form by adding additional questions relevant to your institution's specific needs. Common additions include:

* Certification statements that require applicant acknowledgment
* Additional background questions specific to your program
* Consent fields for institutional policies

To edit your application's submission form, open the application editor and click "Submission Form" from the left menu under "Content."

---

# Using Conditional Logic

The Submission Form supports conditional logic, allowing you to create dynamic question paths based on applicant responses. This ensures that:

* Applicants only see questions relevant to their specific circumstances
* The submission process remains streamlined and focused
* You can collect additional details when necessary based on initial responses

For example, if an applicant indicates they have been academically dismissed, you can display follow-up questions requesting an explanation, documentation, or other pertinent information.

---

# Responses + Flagging for Review

All responses to the submission form questions will appear on the application preview and PDF for easy reference during the review process. This ensures that:

* Reviewers have immediate access to critical information
* All sensitive disclosures are properly documented
* The complete submission record is preserved in the application PDF

![pro tip icon](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1433968960/1c3bb7b00b8c8c014ce5d7ac641d/Pro+Tip.png?expires=1784430000&signature=8a868b7f59b03fea19f8a9df9dafb3f42f1257e5dc7696ba80435de44abe64ec&req=dSQkFcB4lYhZWfMW3Hu4gTZ9Cn%2FXk%2Bm%2BTGKMdIdOwuoQ4dEmS%2BGSYKKEZvLb%0Aew%3D%3D%0A) You can create a calculated segment of contacts who select "true" for fields on the submission form. This allows you to quickly identify contacts needing additional review based on their answers. For the default fields, you could use the two application filters: **`Discipline: Convicted`** and **`Discipline: School Problems`.**

You can take it a step further by using that segment in a workflow to:

* Assign review tasks to internal users
* Apply specific labels to these contacts
* Implement other custom processes based on your institution's workflow needs

Using segments and workflows can help streamline the review process.

---

# Best Practices

* Keep the Submission Form concise and focused on essential information
* Use clear language when asking sensitive questions
* Provide explanatory help text to guide applicants
* Regularly review your submission form settings

---