---
title: Email Renderings in Outlook
url: https://help.element451.com/en/articles/8549932-email-renderings-in-outlook
collection: Campaigns
---

Learn about the limitations of Outlook when it comes to displaying campaign emails to your recipients.

# Overview

Element451's Campaigns module is designed to work best with modern web and mobile-based email clients. Some versions of Microsoft Outlook (notably Classic Outlook) use older rendering engines that do not support modern HTML and CSS features commonly used in modern email design, like those used in Element451. As a result, emails may not always display as expected in Outlook, even though they may look fine in other email clients (including the Element451 preview mode).

---

# Outlook Limitations to Note

* **Background images** are not supported in all versions of Outlook.
* **Inline images** are not supported in all versions of Outlook.
* **Dark Mode** may cause color shifts in email backgrounds and on images, especially those with transparent backgrounds.
* Some **advanced style options for buttons** may revert to basic styling (rounded vs. square buttons).
* **Outlook may render components slightly differently** from what you see in Element's Preview mode.

---

# Reasons for Outlook Limitations

Outlook's limitations are primarily due to its older rendering engine. Here’s a breakdown:

* **Limited HTML and CSS Support:** Microsoft Outlook uses its own rendering engine, which has limited support for modern HTML and CSS standards. Layouts are often heavily reliant on tables.

* **Table Layouts:** Outlook relies heavily on table-based layouts for rendering, which can lead to issues when using `<div>`-based layouts or non-table structures for your emails.

* **Differing Image Rendering:** Outlook may render images differently from other email clients. This can lead to image size, alignment, or quality discrepancies, especially when using background images or applying specific styling.

* **Outlook Version Variations:** Different versions of Outlook (e.g., Outlook 2010, 2013, 2016, Outlook for Office 365) may exhibit varying rendering behaviors.

---