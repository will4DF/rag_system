---
title: Getting Started with Case Management [Beta]
url: https://help.element451.com/en/articles/13764725-getting-started-with-case-management-beta
collection: Case Management (Beta)
---

An introduction to Case Management — what Alerts and Cases are, how they connect, and how to navigate the module from day one.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

# Overview

Case Management in Element451 provides a structured way for your institution to identify student risk signals and turn them into accountable, coordinated work. Whether a student has missed classes, is at academic risk, or has a wellbeing concern, Case Management gives your team a shared place to triage concerns, assign ownership, track progress, and close the loop with clear outcomes.

The module is organized around two core concepts that work together: Alerts and Cases. This article introduces both, explains how they connect, and walks you through the module experience so you can get up and running quickly.

---

# Understanding Alerts and Cases

Case Management is intentionally split into two distinct but connected concepts. Understanding the difference between Alerts and Cases is the key to using the module effectively.

## Alerts

An Alert captures a **one-time signal** that something happened and may require attention. Think of an Alert as a decision point.

Alerts answer the question: "Something happened — does this need action?"

Common alert signals include:

* Missed classes or attendance issues
* Academic or grade risk
* Lack of engagement
* Behavioral, wellbeing, or other institutional concerns

Alerts are designed to be:

* **Event-based** — they capture a specific moment in time, not ongoing work
* **Owned short-term** — a Reviewer triages and resolves them quickly
* **Lightweight** — they include only the fields needed for fast decision-making

## Cases

A Case represents the **ongoing work** staff do to help a student resolve an issue over time. Think of a Case as the system of record for that work.

Cases answer the questions:

* "Who is responsible?"
* "What work is happening?"
* "Where are we in resolving this?"

Cases are designed to be:

* **Stateful and long-lived** — they progress through statuses over time
* **Independently owned** — an Assignee is responsible for resolution
* **Containers for related work** — they can link to Alerts, Tasks, Conversations, Appointments, and Documents

## How they Connect

* Alerts and Cases are connected but **independent**.
* An Alert can be escalated to a Case when the signal requires deeper follow-up.
* Cases can also be created on their own—not every Case needs to originate from an Alert, and not every Alert needs to become a Case.

A student may have multiple Alerts and multiple Cases at the same time, reflecting different concerns or signals at various stages of resolution.

### 💡 Key Distinction

Alerts use the term "Reviewer" (the person triaging the alert), while Cases use "Assignee" (the person responsible for resolution). This naming is intentional — it reflects the different nature of the work: short-term triage vs. long-term ownership.

---

# Accessing + Navigating the Module

To access Case Management, navigate to **Engagement** > **Case Management**.

When you open Case Management, you'll see a left sidebar, a main content area with a list view, and action buttons at the top right of the page.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131462549/9e8fbacc0cdab6c3119ca67929e8/Case%2BManagement-402x.png?expires=1784333700&signature=412508f8c8ad45e18f1f728cc2708c44d66edd9b90256afc72a08515c4b27776&req=diEkF814n4RbUPMW1HO4zfg29KmpimPFsQ02D4kpOKu2OKhgyH%2BkMexIQvsv%0A8hFXVoSFSQuM6L52tPM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2131462549/9e8fbacc0cdab6c3119ca67929e8/Case%2BManagement-402x.png?expires=1784333700&signature=412508f8c8ad45e18f1f728cc2708c44d66edd9b90256afc72a08515c4b27776&req=diEkF814n4RbUPMW1HO4zfg29KmpimPFsQ02D4kpOKu2OKhgyH%2BkMexIQvsv%0A8hFXVoSFSQuM6L52tPM%3D%0A)

## Top-Right Actions

At the top right of the page, you'll find:

* **+ New Alert** — create a new Alert
* **+ New Case** — create a new Case
* ⋮ **(More menu)** — access Settings for Alert and Case configuration

## Sidebar Navigation

The sidebar is divided into two sections — Alerts and Cases — each with a set of pre-filtered views designed to support common workflows. Each view shows a count badge so you can see at a glance how many items need attention.

## Alert Views

|  |  |
| --- | --- |
| **View** | **What It Shows** |
| **Triage (default)** | Alerts in the Triage resolution status — this is designed to be a landing view for day-to-day review and decision-making |
| **All Alerts** | All alerts with no filters applied |
| **Unassigned Alerts** | Alerts with no Reviewer assigned — useful for delegation and load balancing |
| **Your Alerts** | Alerts where you are the assigned Reviewer |
| **Created by You** | Alerts you created — useful for tracking submitted alerts and follow-ups |
| **Your Team Alerts** | Alerts assigned to any member of your team |

## Case Views

|  |  |
| --- | --- |
| **View** | **What It Shows** |
| **All Cases** | All cases with no filters applied |
| **Your Cases** | Cases where you are the assigned owner (assignee) |
| **Created by You** | Cases you created |
| **Your Team Cases** | Cases assigned to any member of your team |
| **Subscribed Cases** | Cases you are subscribed to — supports awareness and collaboration without ownership |

## Stats Bar

At the top of each list view, a stats bar provides a quick summary of key metrics. The stats shown depend on whether you're viewing Alerts or Cases.

### Alert Stats (Triage View)

|  |  |
| --- | --- |
| **Metric** | **Description** |
| **Need Triage** | Count of alerts currently in the Triage status |
| **Overdue** | Count of alerts past their due date (shown in red) |
| **Unassigned** | Count of alerts with no Reviewer |
| **Due Today** | Count of alerts due today (shown in red if non-zero) |

### Alert Stats (All Other Views)

|  |  |
| --- | --- |
| **Metric** | **Description** |
| **Total Alerts** | Total count of alerts in this view |
| **Overdue** | Count of alerts past their due date (shown in red) |
| **Unassigned** | Count of alerts with no Reviewer |
| **Due Today** | Count of alerts due today (shown in red if non-zero) |

### Case Stats

|  |  |
| --- | --- |
| **Metric** | **Description** |
| **Total Cases** | Total count of cases in this view |
| **Overdue** | Count of cases past their due date (shown in red) |
| **Unassigned** | Count of cases with no Assignee |
| **Due Today** | Count of cases due today (shown in red if non-zero) |

---

# Sharing Alerts and Cases

Every alert and case has its own **unique, shareable URL** that opens the item's detail view directly. This makes it easy to:

* Loop in a teammate by pasting the link in a Slack message or email
* Reference a specific alert or case in internal comments and notes
* Hand off work or escalate without making the recipient hunt for the right item

To grab the link, open the alert or case and click **Copy Link** on the edit sidebar (or copy the URL from your browser's address bar).

📙 **Note:** If the recipient doesn't have access to the alert or case—or the item has been deleted—they'll see a "Failed to load" message and land on the main Case Management page.

---

# The Alert Lifecycle at a Glance

Alerts follow a straightforward lifecycle from signal to resolution:

1. **An Alert is created**, either manually by staff, submitted by faculty, or generated through automation.
2. **A Reviewer triages it** by reviewing the details and deciding what action to take.
3. **The Alert is resolved** by dismissing it, resolving it directly, or escalating it to a Case for further work.

For a detailed walkthrough of creating, triaging, and resolving Alerts, see [Alerts](https://help.element451.com/en/articles/13771971-working-with-alerts-closed-beta).

---

# The Case Lifecycle at a Glance

Cases progress through statuses as work is completed:

1. **A Case is created** manually, from an Alert, or via automation.
2. **An Assignee owns it** with optional Subscribers who follow along for awareness.
3. **Work is tracked** through related Tasks, Conversations, Appointments, and Documents.
4. **The Case is resolved or cancelled** moving it to a final status.

For a detailed walkthrough of creating, managing, and resolving Cases, see [Cases](https://help.element451.com/en/articles/13772190-working-with-cases-closed-beta).

---

# Related Work on a Case

One of the most powerful aspects of Cases is that they act as **containers for related work**. A Case doesn't replace your existing tools — instead, it brings related items together in one place so all the work around a student's issue lives in a single view.

Cases can be linked to:

* **Alerts** — typically connected through the escalation process
* **Tasks** — action items owned by staff
* **Conversations** — outreach, follow-ups, and check-in threads
* **Appointments** — advising sessions, counseling meetings, and other scheduled interactions
* **Documents** — incident reports, accommodation letters, academic plans
* **Bolt Agent Jobs** — AI agents running proactive outreach tied to the case

Related objects retain their native behavior and remain accessible in their original modules. You can relate items from within the Case detail panel or directly from each object's own module.

📙 **Note:** When you close a Case, any active Bolt Agent Job enrollments that were created from that Case are automatically canceled, preventing proactive outreach from continuing after the case is resolved. Enrollments created from other sources are not affected.

For a full walkthrough, see [Relating Objects to Cases](https://help.element451.com/en/articles/13772358-relating-objects-to-cases-closed-beta).

---

# Timeline

Every Alert and Case includes a **Timeline** — a chronological activity feed showing what changed, who changed it, and when. The Timeline gives your team full auditability and makes handoffs seamless, since context never has to be reconstructed from memory or scattered notes.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2531035191/2aca7f77de4e02a99e1a57cd5c25/CleanShot+2026-07-09+at+10_44_16%402x.png?expires=1784333700&signature=6bee537977daa573872fb33579d0789d46d8afc4270a93cdf0e91efc4053da25&req=diUkF8l9mIBWWPMW1HO4zROgYcT3H22SC4zSvnzC0CPJiMPQg9tOTpxMfpWW%0AK7UjDXbX48MTJ3mbAdc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2531035191/2aca7f77de4e02a99e1a57cd5c25/CleanShot+2026-07-09+at+10_44_16%402x.png?expires=1784333700&signature=6bee537977daa573872fb33579d0789d46d8afc4270a93cdf0e91efc4053da25&req=diUkF8l9mIBWWPMW1HO4zROgYcT3H22SC4zSvnzC0CPJiMPQg9tOTpxMfpWW%0AK7UjDXbX48MTJ3mbAdc%3D%0A)

* **On Alerts** — the Alert details sheet has two tabs, Overview and Timeline. The Timeline is a single chronological feed of the alert's activity, capturing changes such as priority, resolution status, reviewer, due date, escalations to Cases, and internal notes added to the alert.
* **On Cases** — the Timeline is a dedicated tab on the Case detail page, directly after the Information tab. It mirrors the activity feed on a contact profile, with shortcut filters down the left side to focus on a specific type of activity. It shows case-level activity (status, assignee, priority, due date, subscribers, privacy) alongside internal notes, Bolt Analysis runs, and when related items (tasks, conversations, appointments, documents, and alerts) are linked to or unlinked from the case.

📌 **Note**: These detailed alert and case activities appear on the Alert and Case Timelines only. A contact's own profile activity feed still shows just the high-level activities (when an alert or case is created or resolved) so profiles stay uncluttered while the full history stays with the case or alert.

---

# AI Analysis: Bolt Analysis for Cases

Every Case includes **Bolt Analysis** — a persistent, AI-generated briefing that reads the case and the student's record, then summarizes what's happening, what matters about the student, and what to consider doing next. You don't have to ask for it: it's generated automatically when the case is created and refreshes as the case evolves.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2451469526/94a4534e7240e812a459548ea295/Bolt+AI+Analysis+for+Cases.png?expires=1784333700&signature=2ff7ecc54187a7fa2decd04a927b18f1281d1400acd8fed146c0dd0a392ddcd2&req=diQiF814lIRdX%2FMW1HO4zcX2YNjWCxcGcFnOlekvrV1cA6a6XAhvmUcM21DD%0AptosEmLcyLvOnwMT3uE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2451469526/94a4534e7240e812a459548ea295/Bolt+AI+Analysis+for+Cases.png?expires=1784333700&signature=2ff7ecc54187a7fa2decd04a927b18f1281d1400acd8fed146c0dd0a392ddcd2&req=diQiF814lIRdX%2FMW1HO4zcX2YNjWCxcGcFnOlekvrV1cA6a6XAhvmUcM21DD%0AptosEmLcyLvOnwMT3uE%3D%0A)

You'll find it on the Case's **Information** tab, structured into three consistent sections:

* **Case Summary** — a plain-language read on what's happening with the case right now
* **Student Context** — the signals from the student's record that matter for this specific case
* **Recommended Next Steps** — prioritized, specific suggestions for moving the case forward, actionable right from the panel

For a full walkthrough — including how the briefing adapts to the case's phase, what data it considers, and how to act on its recommendations — see [Bolt Analysis for Cases](https://help.element451.com/en/articles/15265836-bolt-analysis-for-cases-closed-beta).

---

# Notifications: Daily Digest Email

To help staff stay on top of Alert and Case activity without constantly checking the module, Case Management sends a once-daily digest email to internal users. The digest summarizes relevant activity from the previous 24 hours and surfaces a heads-up on items with upcoming due dates.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2430669809/cfd7a6f39160b494ef19f27263b2/CM-Daily+Digest+Emaio%402x.png?expires=1784333700&signature=f7ad2d015b9b193f959948edf395b6fa935db59083f79c3c67b165e7bfb6befd&req=diQkFs94lIlfUPMW1HO4zWkdSfXrVP%2F%2F4M8b6yZ%2Fe%2BXNvsVE0jJUhpGsR25v%0AMp6O4lgrPs3G2wNfTSo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2430669809/cfd7a6f39160b494ef19f27263b2/CM-Daily+Digest+Emaio%402x.png?expires=1784333700&signature=f7ad2d015b9b193f959948edf395b6fa935db59083f79c3c67b165e7bfb6befd&req=diQkFs94lIlfUPMW1HO4zWkdSfXrVP%2F%2F4M8b6yZ%2Fe%2BXNvsVE0jJUhpGsR25v%0AMp6O4lgrPs3G2wNfTSo%3D%0A)

## What's in the Digest

The email is grouped by object type (Alerts, then Cases), and within each section by individual Alert or Case. Each item is a **direct link to the specific alert or case** so you can jump straight into the detail view—no searching through the list.

If a Case had multiple changes in one day (for example, status moved Triage → In Progress → Resolved), the digest shows only the terminal state, not each intermediate transition.

## Alert Notifications

|  |  |
| --- | --- |
| **Event** | **Who Receives It** |
| An Alert has been assigned to you | Reviewer |
| Alert priority has changed | Reviewer |
| Alert status has changed | Reviewer |
| Alert is due within the next 7 days | Reviewer |

## Case Notifications

|  |  |
| --- | --- |
| **Event** | **Who Receives It** |
| A Case has been assigned to you | Assignee |
| You've been added as a subscriber to a Case | Assignee, Subscriber |
| Case priority has changed | Assignee, Subscriber |
| Case status has changed | Assignee, Subscriber |
| Case is due within the next 7 days | Assignee |

## Upcoming Due Dates

In addition to activity from the past 24 hours, each digest includes a section listing Alerts and Cases assigned to you that are due today or within the next 7 days. Items due that day are visually distinguished (red, bold) so they're easy to spot.

## Delivery Details

* **Frequency:** Once per day
* **Send time:** Around 7:00 AM in your institution's configured timezone
* **Sender:** [notifications@element451.io](mailto:notifications@element451.io)
* **Recipients:** Internal users who had at least one qualifying event or have an Alert or Case due in the next 7 days
* **No content, no email:** If you have no qualifying events and nothing due in the next 7 days, no email is sent that day
* **Unsubscribing:** These are transactional emails tied to your responsibilities in the platform, so there is no in-app unsubscribe. If you'd like to filter or archive them, use inbox rules in your email client (such as Gmail or Outlook)

---

# Automation

Case Management supports two complementary automation engines that can route, assign, and create Alerts and Cases without manual effort.

* **Case Management Automation Rules** — a dedicated, trigger-based engine built into Case Management Settings. Use it for routing and handling — assigning Reviewers and Assignees, setting priority, escalating to Cases, creating follow-up Tasks, and enrolling contacts in Bolt Agent Jobs.
* **Workflows + Rules module** — Element451's cross-platform automation engine. Use it when Alert or Case activity needs to coordinate with broader actions like student communications, segment-based enrollment, or platform-wide journeys.

Both engines can act on the same triggers (Alert Created, Case Created), and they work well together — an Automation Rule can enroll a contact in a Workflow as one of its actions.

💡 **Dynamic assignment with Network Roles:** When automation creates or updates an Alert or Case, you can set the **Reviewer** or **Assignee** to a **Network Role token** instead of a fixed person. The field resolves to whoever holds that role for the student—so a grade alert routes to that student's Academic Advisor automatically. See [Network: Connect Contacts with Internal Users](https://help.element451.com/en/articles/9884014-network-connect-contacts-with-internal-users).

For the full guide — including how to find and configure Automation Rules, the conditions and actions reference, assignment behavior, worked examples, and a side-by-side comparison with the Workflows + Rules module — see [Automating Case Management](https://help.element451.com/en/articles/14712713-automating-case-management-closed-beta).

---

# Reporting & Insights

Alert and Case data doesn't stay contained within Case Management — it flows across Element451 so you can report on it, segment from it, and act on it from the tools your team already uses.

* **Segments** — Alert and Case properties are available as filter criteria when building contact segments. Build populations like *students with an open Critical alert*, *students whose case was resolved in the last 30 days*, or *students with overdue cases on your team*.
* **Student Success Dashboard** — student-level activity across three Case Management tabs: Alerts, Cases, and the Escalation Funnel. Use it to monitor volume, priority, resolution timelines, and conversion rates.
* **Management Dashboard** — staff-level activity for team leads and managers. Track who's assigned what, resolution rates, on-time performance, overdue work, and workload balance.

For a full walkthrough, see [Using Case Management Data: Segments + Insights](https://help.element451.com/en/articles/14656928-using-case-management-data-segments-insights-closed-beta).

---

# Permissions Basics

Access to Case Management is controlled by your permission group, and what you can see and do depends on several layers working together:

* **Individual permissions** — your Alert and Case permission levels.
* **Alert & Case Type visibility** — which Alert and Case types your permission group can see.
* **Contact visibility groups** — which students fall within your scope.
* **Case privacy** — private cases are limited to the creator, assignee, and users with View All Cases.
* **Related object permissions** — objects inside a case keep their own native permissions.

A user must pass every applicable check to see a given Alert or Case. For the full breakdown of each layer, the permission levels, and how to configure them, see [Permissions and Visibility in Case Management](https://help.element451.com/en/articles/15465236-permissions-and-visibility-in-case-management).

---

# Configuring Case Management

Administrators control the building blocks of Alerts and Cases — the types, priorities, statuses, and templates available to your team — through Case Management Settings. Click the **⋮ (more menu)** at the top right of the Case Management page to open Settings.

* **Alert Settings** — manage Alert **Types** (with optional Course Related behavior), **Priorities** (custom colors and icons), and **Templates** for pre-filled Alert fields.
* **Case Settings** — manage Case **Types**, **Statuses** (custom statuses layered onto four fixed system status groups: To Do, In Progress, Resolved, Cancelled), **Priorities**, and **Templates**.

For full configuration details, see [Alert Settings](https://help.element451.com/en/articles/13772418-alert-settings-closed-beta) and [Case Settings](https://help.element451.com/en/articles/13775536-case-settings-closed-beta).

---

# Faculty Access

For internal users who need to submit and track Alerts but don't need access to the full Element451 platform, the **Portal for Case Management** provides a streamlined, lightweight interface.

Portal users can:

* View a list of students
* Submit Alerts individually or in bulk
* Track the status of Alerts they have created

When an admin adds a new internal user to Element451, they choose whether the user is a **Platform** user (full Element451 access) or a **Portal** user (lightweight Portal UI only). Portal users log in at the same Element451 URL as Platform users and are automatically routed to the Portal interface.

For a full walkthrough of the Portal experience — including the My Students and My Alerts tabs, submitting Alerts individually or in bulk, and what Portal users can and cannot do — see [Portal for Case Management](https://help.element451.com/en/articles/13772401-portal-for-case-management-closed-beta).

---

💬 **Still have questions?** Check out the [Case Management Frequently Asked Questions](https://help.element451.com/en/articles/13775881-case-management-frequently-asked-questions-closed-beta) for quick answers to common questions about Alerts, Cases, permissions, and settings.

---