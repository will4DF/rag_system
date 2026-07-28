---
title: Troubleshooting Field Filtering
url: https://help.element451.com/en/articles/11321105-troubleshooting-field-filtering
collection: Data Management
---

# Overview

Below is a quick, step‑by‑step guide you can follow any time a drop‑down (Majors, Terms, Degrees, Campuses, or Schools) isn’t showing the choices you expect.

**Quick Reminder**: Filters read the live answers a student gives and compare them to the relationships you build in **Available For**. A mismatch at either point is what hides the options. Fix the relationship or the filter settings, publish, retest, and your drop‑down should snap back to life.

---

# 1. Confirm the Field Can be Filtered

Only the five data‑source families below can filter each other. If the drop‑down you’re troubleshooting isn’t one of them, filtering won’t work:

* Majors
* Terms
* Degrees
* Campuses
* Schools
* Student Type

---

# 2. Check the “Available For” Relationships in Data Sources

Filtering relies on the relationships you define in each item’s **Available For** panel.

1. Go to **Data Management › Data Sources**.
2. Open the data source that should appear in the drop‑down (e.g., *Majors*).
3. Edit the option that’s missing and verify that its **Available For** values include the selections the student made earlier (e.g., the right Term or Degree).
4. If you need to update many records, download the list, edit it in bulk, and re‑upload.

---

# 3. Verify Filter Settings on the Form/Application Field

Inside the form or application builder:

1. Open the field that should *receive* the filtering (e.g., **Major**).
2. In **Field Options**, toggle **Use Filters** ON.
3. Decide which switch to use:

   * **Filter available options?** – trims *this* drop‑down based on a previous answer.
   * **Filter another field?** – uses *this* answer to trim a later field.
4. In **Field**, choose the controlling field (the one answered earlier).
5. In **Dimension**, choose the matching data‑source name (it usually mirrors the field you picked).

**Tip:** Field and Dimension names should almost always match (Term ↔ Terms, Campus ↔ Campuses, etc.). Mismatches are the #1 cause of empty drop‑downs.

---

# 4. Check the Field Order on the Form/Application

The controlling field must appear *before* the field it filters. If the order is reversed, the filter has nothing to read, and the drop‑down will appear empty.

---

# 5. Save & Retest

1. Save changes.
2. Publish the form or application.
3. Use a fresh incognito window to test (caches can hold on to an old version).

---

# Still not working?

## Quick Diagnostics Chart

|  |  |  |
| --- | --- | --- |
| **What to look for** | **Why it matters** | **Fix** |
| **Blank “Available For”** on the option | No relationship = option is always hidden | Add the needed Term/Degree/Campus, etc. |
| **Duplicate integration codes** | Can cause mismatches in look‑ups | Ensure each item has a unique code |
| **Repurposed data sources** (e.g., *Schools* used for *Concentrations*) | Field/Dimension names might not match | Point **Field** to *Concentrations* and **Dimension** to *Schools* as documented |
| **Old browser cache/autofill** | Can show stale option lists | Hard refresh or use incognito |

## Troubleshooting Video Guide

---