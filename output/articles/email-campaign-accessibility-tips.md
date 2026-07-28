---
title: Email Campaign Accessibility Tips
url: https://help.element451.com/en/articles/15825094-email-campaign-accessibility-tips
collection: Campaigns
---

Guidance for building accessible email campaigns in Element451: WCAG-compliant link styling, the format-first editor workaround, stylesheet support, and how auto-replies are handled.

# Overview

This article covers common accessibility questions about the email campaign editor, including how to style links to meet WCAG guidance, how the editor's formatting toolbar behaves, and how text sizing and images work.

---

# Accessible Links (WCAG 1.4.1 – Use of Color)

[WCAG 1.4.1 (Use of Color)](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html) requires that color is not the only visual means of identifying a link. You do not need font-size control to meet this requirement — pairing color with a non-color indicator is sufficient. In the campaign editor, **underline + color** (and/or bold) satisfies WCAG 1.4.1.

📙 **Editor tip — format first, then link:** Apply your text formatting (underline, bold, size) *before* applying the link. When you click directly on an existing link, the editor shows a link-specific toolbar with only link management options (open, edit, remove, text color, highlighter). The full formatting toolbar only appears when you select text. To reformat already-linked text, select across additional characters to trigger the full toolbar, or remove and re-apply the link after formatting.

---

# Text Sizing and Headings

Text sizing in the campaign editor is driven by the built-in style presets (Normal, Heading 1, Heading 2, and the smaller size options) rather than arbitrary, independent font sizes.

To keep emails accessible, apply the appropriate **Normal** and **Heading** styles to structure your content instead of trying to resize text manually. Using the heading styles in a logical order also gives assistive technology a clear reading structure.

---

# Images and Video

* **Alt text auto-fills from the Media Manager** — when you insert an image into a campaign, its alt text is pre-populated from the value saved on the image in the Media Manager. You can still customize the alt text for each placement, which is often a good idea so it fits the context of the specific email. Note that editing an image's alt text in the Media Manager later does not retroactively update emails you have already built.

* **Add alt text to video blocks** — the Video block has its own Alt Text field, separate from image alt text. Fill it in when embedding video so screen readers can convey the video's purpose.

---

# General Accessibility Best Practices

* **Alt text** — give images meaningful alternative text so screen readers can convey their purpose; use empty alt text for purely decorative images.
* **Descriptive link text** — prefer link text that describes the destination (for example, "View your application checklist") over generic phrases like "click here."
* **Color contrast** — keep sufficient contrast between text and background colors, especially for links and buttons.
* **Logical structure** — use headings and short paragraphs in a logical reading order so content is navigable by assistive technology.

---

# Frequently Asked Questions

#### Does the Element451 Campaign builder support style sheets?

The email builder does not currently support a full custom stylesheet. Use the editor's formatting tools to style text, links, and buttons directly within each campaign or template.

---