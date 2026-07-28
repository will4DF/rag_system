---
title: Accessibility
url: https://help.element451.com/en/articles/11841002-accessibility
collection: General
---

# Overview

At Element451, we believe digital experiences should be inclusive and accessible to as many people as possible. We are committed to aligning our platform with the Web Content Accessibility Guidelines (WCAG) version 2.1, Level AA standards.

This article outlines our current status, what we’re actively improving, and how to submit accessibility issues in a way that helps our team resolve them quickly and accurately.

---

# Our Accessibility Status

Element451 uses industry best practices to build accessible software and regularly evaluates our platform using both automated tools, deep product knowlege and industry best practices.

Based on our most recent Accessibility Conformance Report (ACR):

* Element451 currently **supports** or **partially** **supports** all WCAG 2.1 Level A and Level AA criteria.
* A limited number of criteria are partially met, including areas such as color contrast, focus visibility, and status messages.
* Improvements continue on a rolling basis across shared components and student-facing experiences.

It's important to note that some aspects of the platform—such as user-generated content and certain embedded third-party tools—may fall outside the scope of our internal accessibility testing.

---

# Supported Browsers and Operating Systems

As a web-based platform, Element451 is designed to be accessible through modern standards-compliant web browsers rather than being tied to a specific operating system. Older versions of browsers may lack features or standards.   
​

Accessibility testing and validation have been conducted using automated tools such as the WAVE Evaluation Tool and Siteimprove’s Accessibility Checker, alongside manual review.  
​

The platform is expected to be compatible with recent versions of:

* **Operating systems:** Windows, macOS, iOS
* **Browsers:** Current versions of Chrome, Firefox, Safari, and Microsoft Edge
* **Assistive technologies:** Commonly used screen readers and accessibility features supported by those browsers and operating systems (e.g., NVDA, JAWS, VoiceOver), as well as keyboard-only navigation and browser-level zoom and contrast tools

As with most web-based applications, accessibility is dependent on the user’s browser, operating system, and assistive technology configuration. We continuously work to improve compatibility and align with WCAG 2.1 AA guidelines.

---

# How We're Preparing for the 2027 Federal Guidelines

As of April 20, 2026, the DOJ has extended Title II web accessibility [compliance deadlines](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web). State and local government entities serving populations of 50,000 or more must now comply by **April 26, 2027**. Entities serving smaller populations or special districts have until **April 26, 2028**.

In late 2025-Mid-2026 we conducted a structured audit and remediation initiative ahead of the U.S. Department of Justice requirements for WCAG 2.1 Level AA. Current work focuses on our most visible student-facing tools, also known as Element451's Web Apps, to ensure they are compliant:

* Application Sites
* Appointment Sites
* Bolt Discovery
* Element Messenger
* Event Sites
* Pages
* StudentHub

## Identified Areas of Focus

### 1. Color Contrast & Visual Distinguishability

* Low-contrast UI elements across StudentHub, Messenger, and Applications
* Insufficient contrast on Messenger elements (labels, timestamps, icons)
* Dropdown highlight/focus indicator contrast too low

### 2. Keyboard Navigation, Focus Order & Focus Visibility

* Missing or inconsistent focus indicators across multiple Application button components
* Emoji picker not keyboard accessible
* Cookie banner does not receive focus on load
* Some interactive elements lack visible focus indicators or fail to show a clear active state
* Keyboard navigation challenges in StudentHub have been reviewed and improved

### 3. Structural & Semantic Issues (Headings, Landmarks, Roles)

* Pages missing required ARIA landmarks (e.g., <main>, <nav>, <header>)
* Heading levels increase incorrectly by more than one step at a time (e.g., jumping h1 → h3), impacting screen reader navigation
* Some templates missing explicit customizable alt text fields for images (e.g., Pages Billboard with CTA)
* Buttons coded as links but assigned ARIA button roles, causing inconsistent semantics
* Missing or duplicated heading structures corrected in various UI areas (such as StudentHub)

### 4. Non-Text Content & Alt Text

* Missing or insufficient alt text support in certain templates
* Some Pages components require new fields to allow alt text (e.g., Billboard with CTA)

### 5. Form Labels, Associations & Input Semantics

* Form options not properly associated with labels, creating issues for screen readers
* Some Form controls require updated for/id or aria-labelled by attributes to ensure proper association

### 6. Screen Reader Feedback & Announcements

* Error messages in certain pages are not announced by screen readers, requiring ARIA live region or status role updates
* Cookie banner accessible name does not match visible label (e.g., aria-label vs. button text), causing screen reader confusion

### 7. Zoom, Scaling & Responsive Issues

* Messenger becomes clipped and unusable at high zoom levels
* User-scaling behaviors across StudentHub
* High-zoom layout issues causing content to overflow or not reflow properly

### 8. Miscellaneous Functional Accessibility Gaps

* Backdrop overlays in modals interfering with assistive technology behavior
* Some components require improved role semantics and keyboard interaction patterns

These improvements began in Q3 2025, and most items were completed by May 1, 2026. Accessibility for our web apps remains an ongoing area of focus, and additional remediation will be prioritized based on impact and severity.

---

# Common Issues That Are User Addressable

Element451 provides tools for institutions to create and publish content across our web applications. While platform-managed (native) content is designed to meet accessibility standards, content created and managed by your institution may not be.  
​

Issues related to institution-managed content should not be submitted as accessibility bugs, as your team can update and remediate this content directly.

## Image & Media Content

* **Missing or inaccurate alt text** on images added in Pages or content blocks.
* **Videos without captions** when uploaded or embedded by the institution.
* Images or graphics used to convey information without appropriate text equivalents.

## Page Structure & Readability

* **Improper heading order** caused by removing or rearranging page components.
* **Skipped or inconsistent headings** introduced during content editing.
* **Content that does not meet reading-level expectations**, including overly complex or inaccessible text formatting.
* Use of custom HTML that may create inaccessible structures.

## Branding & Visual Design

* **Insufficient color contrast** resulting from institutional brand colors or theme selections (e.g., custom button colors, background/foreground palettes).
* **Contrast issues in text or buttons** where colors were chosen in institutional style settings and fall outside WCAG-compliant ranges.

## Links & Navigation

* **Link text that is unclear, vague, or non-descriptive** (e.g., “click here,” “read more”) in authored content.
* Missing context around links inserted via custom HTML or embedded widgets.

## Forms & Interactive Elements

* **Form-field labels missing or improperly associated** due to custom HTML or external widgets embedded into Pages.
* Use of non-standard or third-party form technologies that do not meet WCAG labeling requirements.
* Errors introduced by disabling or modifying recommended accessible components.

As part of our accessibility initiatives, we've enhanced the admin experience to help prevent and more easily resolve accessibility issues.

---

# Submitting Accessibility Issues

To support an efficient review process, accessibility reports must follow the guidelines below. This helps us distinguish between platform issues, content-level updates partners can resolve themselves, and items already in progress.

## Before You Submit: What We Need From You

When sharing accessibility concerns to Support, please do not simply send a spreadsheet audit report from a tool or person. Many automated tools will surface issues that can be addressed directly by your team using configuration settings, content updates, or standard platform controls, as noted above.

Instead, we ask that you:

1. **Confirm the issue cannot be resolved using platform settings.** Many items—such as color contrast, heading structure, or image alt text—can be fixed at the site or content level. You can review a list of common issues in [the section above](#h_42f51b3978).
2. **Submit only the issues that relate to Element451’s underlying system.** These are issues that cannot be addressed through configuration, content cleanup, or brand design updates.

Each reported item must include:

* The **specific WCAG 2.1 criterion** violated
* The **URL or location** where it occurs
* A short **description of the issue**
* Steps to reproduce (if applicable)
* Screenshots or examples

Providing this level of detail helps our engineering and design teams evaluate issues accurately. If you’re reporting multiple items, you may submit them in one list as long as each row includes all required information, noted above.

---

# What is Next?

Element451's remediation efforts through mid-2026 focused on our public, student-facing web applications. Throughout the remainder of 2026 and into 2027, we will be addressing additional remediation within our web applications.  
​

Building on this work, we're also partnering with an independent, third-party accessibility audit firm to expand our audit coverage across the platform, and to support ongoing compliance efforts and documentation.

---

# Need More?

For a breakdown of how our platform maps to WCAG criteria, you can request a copy of our most recent Accessibility Conformance Report (ACR/VPAT) visit our [trust center.](https://trust.element451.com/)  
​

We're proud of the work we've done already in this area and are committed to continuous improvement in both the near and long-term roadmap.

---