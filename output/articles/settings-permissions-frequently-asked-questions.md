---
title: 📌 Settings + Permissions: Frequently Asked Questions
url: https://help.element451.com/en/articles/10602408-settings-permissions-frequently-asked-questions
collection: Settings + Permissions
---

This article answers commonly asked questions about Settings + Permissions, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389355281/2cf5d1bc609c0d1504e9d734533d/Pardon+our+Progress.png?expires=1784333700&signature=f3756b5ad50c0affcdaf06ddcf50f2a756c3b06c7e06f618c8c4de749d055ced&req=dSMvH8p7mINXWPMW1HO4zdh4IkUbXfDkJTbO5dzz1YZVIui7OjFwyQj3muXS%0AaXjEfmwIIYPA7fvDCUE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389355281/2cf5d1bc609c0d1504e9d734533d/Pardon+our+Progress.png?expires=1784333700&signature=f3756b5ad50c0affcdaf06ddcf50f2a756c3b06c7e06f618c8c4de749d055ced&req=dSMvH8p7mINXWPMW1HO4zdh4IkUbXfDkJTbO5dzz1YZVIui7OjFwyQj3muXS%0AaXjEfmwIIYPA7fvDCUE%3D%0A)

# Security: Authentication

#### How do I configure Single Sign-On (SSO) in Element451?

Element451 supports SSO for both internal users (staff/faculty) and external users (students/contacts). You can configure SSO by adding your institution’s SAML2 metadata in SSO Authentication Settings—a fully self-service process.

**Key Considerations:**

* **NameID Mapping:** Ensure the **SAML2 NameID** attribute is mapped to the **emailAddress** value in your IdP settings.

* **Matching Email:** The email address used for SSO must match a user account in Element451 for successful login.

For step-by-step instructions, visit our help article: [Configuring + Managing SSO](https://help.element451.com/en/articles/10542911-configuring-managing-single-sign-on-sso).

---

# User Management

#### What’s the difference between deactivating and deleting an internal user? And when should I delete?

* **Deactivating:** Keeps all historical data intact (messages, tasks, activities, analytics). The internal user can’t log in, but their records remain in the system.
* **Deleting:** Permanently removes the internal user and all related data. Any places where they were assigned (tasks, conversations, etc.) will display as “deleted user.”

When to deactivate:

* When you want to retain historical records for reporting, compliance, or audit purposes.
* When an internal staff member leaves, but you need to preserve their task and conversation history.

When to delete:

* When you’re certain that all related data is no longer needed.
* To permanently remove test or duplicate records that have no historical value.

---