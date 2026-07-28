---
title: Accessibility Compliance Settings Checklist
url: https://help.element451.com/en/articles/15889548-accessibility-compliance-settings-checklist
collection: General
---

A checklist of Element451 settings to review to ensure your environment is configured for accessibility compliance.

# Overview

Element451 maintains WCAG 2.1 AA conformance on student-facing surfaces at the platform level: focus indicators, screen reader labels, heading structure, and keyboard navigation are handled for you. What the platform cannot control are the colors, images, and content choices your institution configures. This article is a checklist of those settings so you can verify your Element451 environment is configured accessibly.

This is a settings checklist, not a design guide. For background on Element451's accessibility approach, see our [Accessibility](https://help.element451.com/en/articles/11841002-accessibility) article.

📝 **Note on compliance dates:** The Department of Justice's rule under ADA Title II adopts WCAG 2.1 Level AA as the standard for public institutions' web content. In April 2026, the DOJ extended compliance dates by one year: entities serving populations of 50,000 or more now have until **April 26, 2027**, and smaller entities until **April 26, 2028**. The underlying non-discrimination obligations remain in effect, so we recommend completing this review now rather than waiting.

---

# How to Check Color Contrast

Most items below are contrast checks. WCAG 2.1 AA requires a contrast ratio of at least **4.5:1** for normal text and **3:1** for large text and user interface components. Use a free tool like the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/): enter the foreground and background hex values from your settings, and the tool tells you whether the pair passes.

---

# Settings Checklist

## 1. Branding Colors

**Location:** Settings > General > Branding

Your primary and secondary brand colors cascade into Pages, StudentHub, Application Sites, and more, making them the most common source of contrast issues. Check your brand colors against the backgrounds they appear on (especially white and your page backgrounds) for 4.5:1 (text) or 3:1 (buttons and UI components).

## 2. Cookie Acceptance Banner

**Location:** Settings > General > Privacy Policy

If **Show Cookie Acceptance Message** is enabled, review these color settings:

* **Cookie Banner Background** vs. the text displayed on it
* **Cookie Accept Button** vs. its label text
* **Privacy Policy Text Color** vs. the banner background

🚨 **Important:** Secondary brand colors applied to the accept button are a real-world failure we've seen. If your button color fails contrast, choose a darker variant here; it does not need to match your brand exactly.

## 3. Pages + Microsites Color Settings

**Location:** within each Page or Microsite > Setup > Color Settings

* Check primary, secondary, and **Link Color** against your page background. Link color is editable, so if links (including the privacy policy link in the footer) blend into the background, set a compliant color here.
* Review each page visually: buttons, text over background images, and custom color choices.

## 4. Form Field Labels

**Location:** form settings within Applications, Forms, and Surveys

A **field label font color** setting lets you darken labels that fail contrast against your form background. Also prefer short labels with details in the Help Text field rather than long labels.

## 5. Messenger (Live Chat) Widget

**Location:** Engagement > Conversations > Settings > Messenger

The widget inherits your primary brand color by default. If that color fails contrast within the widget, use the **Messenger color** setting to override it with a compliant alternative. Also confirm any header background image doesn't reduce the readability of the greeting text.

## 6. StudentHub

**Location:** Engagement > StudentHub

StudentHub inherits your branding colors, so any issue found in item 1 appears here too. Subtext color can now be darkened for compliance; if you previously couldn't get StudentHub subtext to pass contrast, re-check it and set a darker value.

## 7. Image Alt Text

**Location:** Media Manager, plus each image placement in Pages and Campaigns

Every meaningful image needs alt text describing its content. Add alt text in the [Media Manager](https://help.element451.com/en/articles/9718138-all-media-media-manager); it carries over automatically when the image is added to Pages. For email campaigns, click the gear icon on an inserted image to open its settings and confirm the alt text is set. Decorative images can have empty alt text.

## 8. Embedded Video

Element451 supports YouTube and Vimeo embeds on Pages. Captions come from the video host, not Element451, so confirm every embedded video has accurate captions at its source.

---

# What Element451 Handles for You

Platform-level accessibility on public-facing surfaces (focus management, ARIA labels, keyboard navigation, semantic structure, and the cookie banner's focus behavior) is maintained by Element451 and requires no configuration. If you find an issue in these areas, report it to support rather than trying to fix it with settings.

---

# Related Resources

* [Accessibility](https://help.element451.com/en/articles/11841002-accessibility)
* [General Settings](https://help.element451.com/en/articles/8471334-general-settings)
* [Messenger (Live Chat)](https://help.element451.com/en/articles/6249763-messenger-live-chat)

---