---
title: Campaigns Dashboard
url: https://help.element451.com/en/articles/6788884-campaigns-dashboard
collection: Insights
---

Learn how to use the Campaigns Dashboard in Insights to analyze and refine your Campaign metrics effectively.

# Overview

The Campaigns dashboard analyzes the performance of both email and SMS campaigns. Explore performance metrics by campaign name, segment name, and tags.

📌 **Note:** Campaign Insights counts **unique** activity, so each recipient is counted once. The "Emails sent" total here reflects unique recipients (**Unique Sent**), not the total send events shown as **Sent** on the campaign page. For ongoing campaigns that send to the same person multiple times, the Sent total on the campaign page will be higher than the figure in Insights. This is expected.

## Accessing the Dashboard

The Campaigns dashboard can be found via the Insights sub-menu. The Insights module can be accessed from the Data + Automations dropdown in the top navigation.

---

# **Dashboard Features**

The Campaigns dashboard displays year-over-year comparisons, monthly changes in campaign performance rates, and a wide variety of performance measurements.

Data can be viewed by overall performance, in specific time frames, and/or within a subset of campaigns.

## Global Controls

* Campaign Name: Filter your data for one or more campaigns.
* To and From Date: Sets the date range filter for the dashboard.
* Previous Period To and From Date: Sets the date range filter for the Previous Period data for comparison.
* Time Aggregation: For all "rate" charges, choose whether you want to see the data by day, week, or month.
* Segments: See your email/sms performance by calculated segment.
* Demographics: Filter your data by state, major, or student type.
* Tags: Filter campaigns by the tags you have added to them in the campaigns module.
* Workflows: Choose a workflow to see how all included campaigns are performing.
* Test Record Toggle: Choose to filter out all records with the "Test Record" label from the data you are viewing in the dashboard.
* IP Address Exclusion: Type in an IP Address to exclude data from users at a single IP Address.

## Segment Filters

The Campaigns report can only be filtered by certain dimensions by default. The segment filter is a great way to filter the report by dimensions that matter to you. Create a segment in the People module, and set it as a calculated segment.

Please allow 24 hours for new calculated segments to appear and filter correctly in Insights.

[Explore more on using segments and Insights together →](https://help.element451.com/en/articles/6798155-using-segments-in-insights)

---

# Tabs

Data on the Campaigns dashboard is organized by date as well as the name of the campaign, segment, or tag.

## Emails

### Visualizations

* Performance of metric rates by day, week, or month
* Performance of all campaign metrics broken down by one-time and ongoing campaigns

  + Note: These tables are grouped by campaign name, Element ID, and day. A student who clicks a link or opens the email several times in the same day will only be counted once.
* Email interactions by device
* Email metrics by time and day of the week
* Email bounces by bounce category
* Email link clicks by link
* Period-over-period performance of emails
* Performance of different versions of emails

## SMS

### Visualizations

* Performance of metric rates by day, week, or month
* Performance by campaign and metric category
* SMS interactions by device
* SMS metrics by time and day of the week
* SMS bounces by bounce category
* SMS link clicks by link
* Period-over-period performance of SMS communications
* Performance of different versions of SMS communications

---

# Metric Glossary

All metrics are calculated based on "sent date." All metrics other than sent reflect the date the communication was originally sent, not the date of the metric (open, delivery, click, etc.). For further explanation and updates on Campaigns analytics, read [this help article](https://help.element451.com/en/articles/1513688-campaign-analytics#h_ecd8224705).

|  |  |
| --- | --- |
| **Metric** | **Definition** |
| Sent | A communication is sent to an individual, but not necessarily delivered. In Insights, Sent reflects unique recipients (each person counted once), so it aligns with Unique Sent on the campaign page rather than the total Sent count. |
| Delivery | The communication is delivered to the email or SMS inbox of the intended individual. |
| Open | The communication is opened by the user. |
| Click | A url is clicked within a communication. |
| Click-Through Rate | The number of clicks divided by the number of deliveries. |
| Open-To-Click Rate | The number of clicks divided by the number of opens. |
| Bounce | A communication is sent, but not delivered. |
| Email Unsubscribe | A communication is opened and the user chose to unsubscribe for future emails. |
| SMS Unsubscribe | A communication is opened and the user chose to unsubscribe for future text messages. |
| SMS Resubscribe | After a user unsubscribes from receiving text messages, the user resubscribes to resume receiving text messages. |

---

# Troubleshooting

### Sorting Pivot Table Data on the Campaigns Dashboard

The Campaigns dashboard includes standard and pivot tables, which behave differently when sorting.

* **Standard** **tables** (e.g., the Ongoing Email Performance table) allow you to click a column header to sort all data in the table, just like a spreadsheet.
* **Pivot** **tables** (e.g., the One-Time Email Performance table) structure data hierarchically, meaning sorting behavior depends on whether campaigns are expanded or collapsed.

Because pivot tables structure data hierarchically, sorting works differently than in standard tables. Here’s how to sort effectively when working with pivot tables.

#### How-To Sort Pivot Tables

* **Sorting Within a Campaign:** If you sort by a metric (such as sends, opens, or clicks) while campaigns are **expanded**, the system will sort only the data within each individual campaign. It does **not** reorder campaigns themselves—just the entries inside them.

* **Sorting All Campaigns:** To sort the entire list of campaigns (instead of just sorting within them), you need to:

  1. Click **Campaign Name** in the table header.
  2. Choose the field you want to sort by (e.g., total opens, total sends).
  3. Select ascending or descending order.

If campaigns are **collapsed**, sorting at the campaign level will be more visible since only summary rows are shown.

#### Key Takeaways

* Sorting a metric sorts **only within each campaign** (if expanded).
* Sorting by **Campaign Name** allows you to reorder all campaigns.
* Collapsing campaigns makes sorting at the campaign level easier to see.

This behavior is due to the way pivot tables structure data.

---