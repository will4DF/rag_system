---
title: Emergency Data Backup & Restoration Policy
url: https://help.element451.com/en/articles/14792428-emergency-data-backup-restoration-policy
collection: General
---

Learn Element451 backups, when a restoration may be possible, and what to expect during a restoration request.

# Overview

Element451 maintains database backups for disaster recovery. In rare emergencies, we have the ability to manually restore data from these backups. Restorations are not a routine self-serve feature—they exist to protect against catastrophic data loss, not to undo regular mistakes.

---

# How Backups Work

We maintain backups of your instance on the following schedule:

|  |  |  |
| --- | --- | --- |
| **Backup type** | **Frequency** | **Retention** |
| Point-in-time restore | Continuous | Last 72 hours |
| Hourly snapshot | Every hour | 3 days |
| Weekly backup | Saturdays | 1 month |
| Monthly backup | End of month | 1 year |

Backups are stored securely within Element451's infrastructure and are used internally for disaster recovery. We do not share backup files directly with customers, and snapshots are *not* available in a self-serve format.

---

# When a Restoration is Possible

If a significant data loss event occurs, Element451 may be able to manually roll your instance back to a prior backup, or in some limited cases restore specific data from a snapshot into your live instance.

Restorations are reserved for **true emergencies**. Examples of events that would qualify:

* An infrastructure failure results in data loss
* A customer’s API integration causes unintended deletion of a large volume of records that cannot be recovered through normal product workflows

Please note that whether a situation qualifies as an emergency is at **Element451's sole discretion**.

Restorations are **not** intended for situations such as:

* Reverting an individual user's edits or routine mistakes
* Undoing a workflow, automation, or import that performed as configured
* Recovering data deleted through standard product features, such as contact deletion, segment-based deletion, or integrations
* Rolling back configuration changes that can be re-created manually

For these everyday situations, please use the product's built-in tools, audit logs, and integration history to recover or rebuild the affected data.

---

# What to Expect When a Restoration Happens

* **Restorations are complex:** Backup-based restorations require manual review and engineering coordination. They are handled case by case and are not guaranteed to be available for every type of data or every scenario.
* **Potential Data loss between snapshots:** A restoration may move your instance back to a point in time. Any data created, edited, or imported after that snapshot may be lost. This trade-off is why restorations are reserved for emergencies.
* **Scope:** Depending on the situation, Element451 may restore an entire instance or attempt to isolate specific data from a backup and merge it into production. We cannot guarantee that every record can be restored perfectly in every scenario.
* **Timing:** Restorations are performed as quickly as possible, but the timeline depends on the complexity of the issue and the scope of the restore. Your Account Manager and support team will keep you informed throughout.

---

# How to Request a Restoration

If you believe you have experienced an event that requires a restoration, contact your Account Manager or open a live support ticket immediately. Please include:

1. A description of what happened and when
2. The approximate time the data loss occurred so we can identify the right backup
3. The records, objects, or areas of the platform affected
4. Any business-critical context, including deadlines or downstream impacts

Our team will assess the request, determine whether it qualifies for a backup-based restoration, and coordinate next steps with you.