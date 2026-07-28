---
title: Field Filtering
url: https://help.element451.com/en/articles/7321011-field-filtering
collection: Data Management
---

Learn how to limit options on a field in applications, events, and forms based on responses to other fields.

# Overview

🚨 **Important:** It is important to understand that you can **only** filter *majors*, *terms*, *degrees*, *campuses*, *schools, and student types* against one another.

Field filtering allows you to dynamically control which options appear in a field based on what a user has already selected in another field.

For example, if your institution only accepts nursing applications for the fall semester, or limits high school students to non-degree-seeking status, field filtering will automatically adjust the available choices as users complete the form — no lengthy explanations needed.

## Important: Use System Fields Instead of Custom Fields

When building applications or forms that capture data like major, degree, or student type, always use the **system fields** rather than creating custom fields—even if you only need to display a subset of options for certain scenarios.

It can be tempting to create custom fields to show a shorter, filtered list of options (for example, a custom dropdown showing only certificate-specific majors).

However, custom fields cause significant problems downstream:

* **Decisions**: Data stored in custom fields will not appear on student decisions.
* **Milestones**: Milestones are generated automatically as students progress through applications and decisions. Custom field data will not populate in milestones, leaving key fields like major and student type blank.
* **Reporting**: The Insights Funnel Dashboard relies on milestone data for funnel reporting. If major or student type aren't recorded in system fields, that data won't be filterable or visible in your reports.

Instead, use **field filtering** to narrow the options shown in a system field. This gives you the same user experience (a focused, relevant list of choices) while keeping your data visible across decisions, milestones, and reporting.

---

# Field Order for Proper Filtering

Each data source can only be filtered by another data source that appears to its right in the following order:

**Schools** → **Campuses** → **Degrees** → **Majors** → **Terms** → **Tests**

This means the order of fields in your application, form, or event matters. If a field appears before the field that is supposed to filter it, the filtering will not work.

**Examples**:

* ✅ If Major comes before Term, the Term list can be filtered by Major.
* ❌ If Term comes before Major, filtering Term by Major will not work.

Review the order of fields in your application or form to ensure they align with this left-to-right structure.

---

# Field Filtering Process

Setting up field filtering is a two-step process:

1. Configure "Available For" relationships in your Data Sources.
2. Enable filtering on the relevant fields in your application, form, or event.

## Step 1: Configure "Available For" in Data Sources

Before filtering will work, you need to define the relationships between your data source items. This is done through the "Available For" settings in your Data Sources.

1. Navigate to **Data and Automations** → **Data Sources**
2. Select the data source you want to configure (e.g., Majors)
3. Click the **edit (pencil) icon** on an individual item  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032855399/f3c884f2a6e06dab02ecd2f3a460/1.png?expires=1784333700&signature=78f1f57abe210d5aaa94a0167b6703d500a8694d9cfbf829b8dbea27da37ebb1&req=diAkFMF7mIJWUPMW1HO4zdl3NcPrn4dzqlfwMNu98WZr1eSnhMYd3OF4dCj%2F%0AI4re%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032855399/f3c884f2a6e06dab02ecd2f3a460/1.png?expires=1784333700&signature=78f1f57abe210d5aaa94a0167b6703d500a8694d9cfbf829b8dbea27da37ebb1&req=diAkFMF7mIJWUPMW1HO4zdl3NcPrn4dzqlfwMNu98WZr1eSnhMYd3OF4dCj%2F%0AI4re%0A)
4. Go to the "**Available For**" tab  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032858638/05694e7e11c64c87306fea980253/2.png?expires=1784333700&signature=152e0a247ae28605490b35125cd0fdb0b645f0b599bfdf96728d20e34b87d8fd&req=diAkFMF7lYdcUfMW1HO4zfK6dj3dvakuthukk9YKsCHraDG2tgmKxWQ8bf1%2F%0AiH6L%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032858638/05694e7e11c64c87306fea980253/2.png?expires=1784333700&signature=152e0a247ae28605490b35125cd0fdb0b645f0b599bfdf96728d20e34b87d8fd&req=diAkFMF7lYdcUfMW1HO4zfK6dj3dvakuthukk9YKsCHraDG2tgmKxWQ8bf1%2F%0AiH6L%0A)
5. Add the properties this item should be available for

For example, if the Accounting major is only offered as a Certificate and an Associate of Applied Science, you would add those two degrees under Accounting's "Available For" settings. If Accounting is available in Spring 2026, you would add that term as well.

✨ **Pro Tip:** Bulk Editing | You can also download your data source list as a spreadsheet, edit the "Available For" relationships outside of Element, and upload it back using the download and upload icons in the upper-right corner of the data source page. This is helpful when configuring a large number of items.

Repeat this for each item that needs filtered availability.

## Step 2: Enable Filtering on Your Fields

Once your "Available For" relationships are configured in Data Sources, apply filtering to the corresponding fields in your application, form, or event.

1. Open your application, form, or event in the editor
2. Select the field you want to filter (e.g., Major)
3. Scroll to the "**Field Options**" section
4. Toggle on "**Use Filters**"  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032863978/77ee02fe23dc0d40bf1dad93c1aa/3.png?expires=1784333700&signature=fa12c25ef24fcc6fbdbe578ca6b30b0733bb8be441c0df917c7c6a84c142719a&req=diAkFMF4nohYUfMW1HO4zdXoBb3%2BiX3LRS9mundplPDQSzUUyj9fcL8jziq%2B%0AbWSy%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032863978/77ee02fe23dc0d40bf1dad93c1aa/3.png?expires=1784333700&signature=fa12c25ef24fcc6fbdbe578ca6b30b0733bb8be441c0df917c7c6a84c142719a&req=diAkFMF4nohYUfMW1HO4zdXoBb3%2BiX3LRS9mundplPDQSzUUyj9fcL8jziq%2B%0AbWSy%0A)

You'll see two filtering options:

### Filter Available Options

This narrows the options shown in \*this\* field based on what the user selected in a previous field. For example, if Degree comes before Major on the form, you can filter the Major list to only show majors that are available for the selected degree.

* **Field**: Select which prior field should drive the filtering (e.g., Degree)
* **Dimension**: Select the "Available For" property that defines the relationship (e.g., Degree)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032866281/5531a1a026ed14439086c1fec881/4.png?expires=1784333700&signature=cbe2d43841e6b024866906363adc0356f27adada5df66489fa9ea29731f4008a&req=diAkFMF4m4NXWPMW1HO4zU7vHLLGzC5%2BuvL%2FmF19wX1vWoM8RVr%2FSCxsqU0f%0AAqd%2FZ46am8%2Fapa%2Bn70U%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2032866281/5531a1a026ed14439086c1fec881/4.png?expires=1784333700&signature=cbe2d43841e6b024866906363adc0356f27adada5df66489fa9ea29731f4008a&req=diAkFMF4m4NXWPMW1HO4zU7vHLLGzC5%2BuvL%2FmF19wX1vWoM8RVr%2FSCxsqU0f%0AAqd%2FZ46am8%2Fapa%2Bn70U%3D%0A)

### Filter Another Field

This filters a **downstream** field based on what the user selects in the current field. For example, selecting a Major could filter the Term list to only show terms that major is offered in.

* Field: Select which downstream field should be filtered
* Dimension: Select the "Available For" property that defines the relationship

Both options can be used on the same field simultaneously — a field can be filtered by a prior selection and also filter a later field.

✨ **Pro Tip:** The Field and Dimension dropdowns should typically share naming conventions. For example, if you're filtering by Degree, the Dimension should also reference the Degree relationship you configured in "Available For."

---

# Example Video: Filtering Majors by Campus

Watch the video below for an example of using field filtering to display majors based on campus:

---

# Troubleshooting

If your filters aren't working as expected:

1. **Check field order**. Make sure the field driving the filter appears \*before\* the field being filtered, and that the order follows the hierarchy: Schools → Campuses → Degrees → Majors → Terms → Tests.
2. **Check "Available For" configuration**. Navigate to Data Sources and verify that the items have the correct "Available For" properties set. If nothing is configured under "Available For," the filter will have nothing to reference.
3. **Check "Use Filters" is enabled**. Open the field settings in your application or form and confirm that "Use Filters" is toggled on with the correct Field and Dimension selected.

For additional troubleshooting steps, see [Troubleshooting Field Filtering](https://help.element451.com/en/articles/11321105-troubleshooting-field-filtering).

---

# Troubleshooting

Check out our [Troubleshooting Field Filtering](https://help.element451.com/en/articles/11321105-troubleshooting-field-filtering) help article for a step-by-step guide and video on troubleshooting common issues with field filtering.

[Field Filtering Troubleshooting Guide](https://help.element451.com/en/articles/11321105-troubleshooting-field-filtering)

---