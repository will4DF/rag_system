---
title: Generating + Accessing PDFs from Forms
url: https://help.element451.com/en/articles/7030166-generating-accessing-pdfs-from-forms
collection: Forms
---

Learn how to generate and export PDF files from form submissions.

# Overview

You can generate print-friendly PDFs for all types of forms in Element, including main and follow-up forms, and supplemental application forms (Applications > Applications > Supplemental Forms).

This guide will demonstrate how to configure and access these PDFs.

[![](https://downloads.intercomcdn.com/i/o/1158704459/1929dbc57a0c92deefae7021/Note.png?expires=1784333700&signature=42b3ced09befb49045486773c04a65465cf30c334063b23fcd0e328c2a186564&req=dSEiHs5%2BmYVaUPMW1HO4zaUPFneg7e2IKDebq1whCurXCIR9g8Sfe%2BsLoDPu%0A7PD2ctHHrXHGinxpX58%3D%0A)](https://downloads.intercomcdn.com/i/o/1158704459/1929dbc57a0c92deefae7021/Note.png?expires=1784333700&signature=42b3ced09befb49045486773c04a65465cf30c334063b23fcd0e328c2a186564&req=dSEiHs5%2BmYVaUPMW1HO4zaUPFneg7e2IKDebq1whCurXCIR9g8Sfe%2BsLoDPu%0A7PD2ctHHrXHGinxpX58%3D%0A)

To view/download the form submission PDF, you must have access to the documents card on the [profile view](https://help.element451.com/en/articles/6449965-bolt-profile-templates).

---

# Configuration for PDF Generation

The configuration process for PDFs is the same for all form types:

1. Navigate to **Engagement** > **Forms**.
2. Click on the form you'd like to generate PDFs from submissions. Main, follow-up, and embeddable forms are available in ***Engagement > Forms.***
3. In the form settings, toggle **Generate PDF for every form submission?** to active. You can also do this for a **follow-up form**.
4. The PDF you generate must be associated with an existing document type. You can add a new document type or manage existing document types by navigating to   
   ​***Data + Automations > Documents > Document Type.***

## Hiding Empty or Unused Fields (Optional)

By default, the generated PDF includes **all** form fields—even those a user left blank and conditional fields that were never shown to the user. If you'd prefer a cleaner, more concise PDF, you can opt in to hide these fields using the following toggles in the form's PDF settings:

* **Hide empty responses** — omits fields where the user did not provide an answer.
* **Hide unused conditional fields** — omits conditional fields that were never displayed to the user.

***📙 Note:***  *The default behavior remains "show all fields." These are opt-in settings—if you leave them off, your PDFs will continue to include every field, including hidden fields that may contain data (for example, prepopulated country codes or fields populated via API for conditional logic).*

## Important Notes

* If you generate a PDF for the main and follow-up forms, two separate PDFs will be created.
* Any markdown fields on a form will also appear in the generated PDF. If generating a PDF from a supplemental form, the PDF will also include additional information about the user, such as the application name, student type, term, degree, and major (if available).
* The font on the pdf is DejaVu Sans. While similar in look to Helvetica and Arial, it supports a broader array of Latin characters found in other alphabets, such as Cyrillic, Hebrew, Greek, and Arabic.

---

# Accessing PDFs Generated from Forms

The PDF documents generated from a form submission will be available on the user's [person profile](https://help.element451.com/en/articles/1475735-the-person-profile) in their **documents** profile card.

PDF documents generated from a Form submission are displayed on the student profile on the Documents card. You must have the Documents card displayed on your profile template in order to view the PDFs on the student profile. [Learn more about Bolt Profile Templates](https://help.element451.com/en/articles/1475735-the-person-profile).

1. Navigate to **Contacts** > **People** or use the search bar in the top right corner to search the student's name.
2. Locate the student you wish to view the PDF for and click on their name to open the profile.
3. Look for the **Documents** card on the user profile. You can also search for it using the search bar.

You can view and download the PDF by navigating to the user's profile from **Contacts > People**, opening their profile, and selecting the **documents** card. You can also search for this card.

***📙 Note:***  *It can take up to 10 minutes for a PDF to be generated following a form submission.*

[![](https://downloads.intercomcdn.com/i/o/679042297/6ffa3b8b5005c1493903d3ac/docscard.gif?expires=1784333700&signature=268b485b536d4e73b460c68b149bd3e738a0964aa7175215073f45da083f9d60&req=cicuFs18n4hYFb4f3HP0gPh%2BAv78C4Zh6H4lew4XfkS2qq5jKB%2BJzt5ePxkE%0AveQ66eIbBNXnvwiNqw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/679042297/6ffa3b8b5005c1493903d3ac/docscard.gif?expires=1784333700&signature=268b485b536d4e73b460c68b149bd3e738a0964aa7175215073f45da083f9d60&req=cicuFs18n4hYFb4f3HP0gPh%2BAv78C4Zh6H4lew4XfkS2qq5jKB%2BJzt5ePxkE%0AveQ66eIbBNXnvwiNqw%3D%3D%0A)

---