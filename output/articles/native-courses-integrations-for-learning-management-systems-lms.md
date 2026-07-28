---
title: Native Courses Integrations for Learning Management Systems (LMS)
url: https://help.element451.com/en/articles/11589065-native-courses-integrations-for-learning-management-systems-lms
collection: Courses
---

# Overview

Element451’s native LMS integrations allow you to automatically sync course and enrollment data from your institution’s Learning Management System directly into the platform. This enables real-time access to academic insights that power segmentation, automation, and personalized student support.

**These integrations are** **read-only**, meaning Element451 ingests data from your LMS but does not write any data back. Currently, only one LMS integration can be active at a time per instance.

Native LMS integrations are available for Canvas, Brightspace, and Blackboard, with support for Open LMS coming soon. You can access these integration settings from **Settings** > **Integrations**.

To get started, review the synced data fields and follow the setup guide for your institution’s LMS below.

---

# LMS Data Sync + Field Mapping

The native LMS integration pulls three key types of data into Element451: **Courses**, **Sections**, and **Enrollments**.

## Field Mapping

We’ve outlined the exact LMS-to-Element451 field mappings for each integration in their respective setup guides. These tables show which fields are supported and how they map into the Courses module in Element451:

* [Canvas Field Mapping](https://help.element451.com/en/articles/11124554-courses-integration-canvas-lms#h_1967a39667)
* [Brightspace Field Mapping](https://help.element451.com/en/articles/11116105-courses-integration-brightspace-lms#h_87cb7ee2b4)
* [Blackboard Field Mapping](https://help.element451.com/en/articles/11199263-courses-integration-blackboard-lms#h_6ce0e5b293)

⚠️ Field availability may vary depending on the platform and your LMS configuration. Not all LMSs support every field.

## Sync Timing

* **Canvas**: Real-time updates via live events.
* **Brightspace + Blackboard**: Nightly sync (data is refreshed once per day).

## Data Scope

* **Canvas**: All available data is synced.
* **Brightspace + Blackboard**: Admins can select which semesters to include in the sync.

---

# LMS Integration Setup Guides

For detailed configuration instructions, refer to the setup guide for your LMS platform:

* [Canvas](https://help.element451.com/en/articles/11124554-beta-canvas-lms-integration-setup)
* [Brightspace](https://help.element451.com/en/articles/11116105-beta-brightspace-lms-integration-setup)
* [Blackboard](https://help.element451.com/en/articles/11199263-beta-blackboard-lms-integration-setup)

*Support for Open LMS is coming soon.*

---

# Troubleshooting

If you notice missing data or fields not populating as expected:

* **Check LMS Configuration**: Ensure the fields are properly configured and populated in your source LMS.
* **Review Permissions**: Verify that the integration has appropriate read permissions for all required data.

---