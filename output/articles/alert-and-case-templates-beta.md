---
title: Alert and Case Templates [Beta]
url: https://help.element451.com/en/articles/14659708-alert-and-case-templates-beta
collection: Case Management (Beta)
---

Learn how to create reusable templates that pre-fill fields when creating alerts and cases—whether manually or through automated workflows.

## 🚀 Case Management is in Open Beta

Case Management is now in Open Beta and available to all customers on the Student Success package. It's actively evolving, so some capabilities are still on the way. To provide feedback and share with others, visit our [User Community Group](https://community.element451.com/c/case-management-open-beta/).

Alert Templates and Case Templates let you define a standard set of field values that can be applied the moment you create a new alert or case. Instead of filling in the same fields every time, you configure a template once and apply it on demand.

Templates are available in two places: the manual alert and case creation forms, and the **Create Alert** and **Create Case** actions in Rules and Workflows. Either way, selecting a template pre-fills the form so your team moves faster and stays consistent.

Alert Templates and Case Templates are configured separately under **Case Management Settings**, each with their own field set.

**This article covers:**

* Accessing Templates in Settings
* Creating Alert Templates
* Creating Case Templates
* Editing, Duplicating, or Deleting Templates
* Using Templates when creating manually
* Using Templates in Rules and Workflows

---

# Accessing Templates

Templates are managed in **Case Management Settings**. Navigate to **Engagement > Case Management**, then open the settings menu.

* **Alert Templates:** Settings > Alerts > Templates
* **Case Templates:** Settings > Cases > Templates

Each section displays a table with columns for **Name**, **Description**, and **Created At**. Use the search icon to filter templates by name. Click any template name to open and edit it.

For more information, check out our [Case Management Settings](https://help.element451.com/en/articles/13772418-alert-settings-closed-beta) help article.

---

# Creating an Alert Template

Navigate to **Settings > Alerts > Templates** and click **+ Add Template**. The template form opens with the following fields:

|  |  |  |
| --- | --- | --- |
| **Field** | **Description** | **Required?** |
| **Name** | Replace "Untitled" in the header with a template name | No |
| **Contact** | Pre-associate a student or contact | No |
| **Alert Type\*** | The category of alert | Yes\* |
| **Priority\*** | Urgency level | Yes\* |
| **Resolution** | Pre-set a resolution status | No |
| **Reviewer** | Assign a reviewer | No |
| **Description** | Add context or instructions for the team | No |
| **Due Date Type** | Define how the due date is calculated (see below) | No |

## Due Date Type

The **Due Date Type** field controls how due dates are set when the template is applied:

* **Exact** — Reveals a **Due Date** field with a date picker. Use this when the due date is always a fixed, known date.
* **Relative** — Reveals a **Due X Days from Execution** field. The due date is calculated relative to when the alert is created (e.g., 3 days after creation).

When finished, click **Save**.

---

# Creating a Case Template

Navigate to **Settings > Cases > Templates** and click **+ Add Template**. The template form opens with the following fields:

|  |  |  |
| --- | --- | --- |
| **Field** | **Description** | **Required?** |
| **Name** | Replace "Untitled" in the header with a template name | No |
| **Contact** | Pre-associate a student or contact | No |
| **Type\*** | Case type (e.g., Academic, Advising, Retention) | Yes\* |
| **Status\*** | Initial status when the case is created | Yes\* |
| **Priority\*** | Urgency level | Yes\* |
| **Assignee** | Team member responsible for the case | Yes |
| **Subscribers** | Additional team members to notify | No |
| **Private** | Toggle to restrict visibility to assigned members | No |
| **Description** | Add context or instructions for the team | No |
| **Due Date Type** | Define how the due date is calculated | No |

When finished, click **Save**.

---

# Editing, Duplicating, or Deleting Templates

Click the **⋮ (More)** icon on any template row to access options:

* **Edit** — Update the template's fields
* **Duplicate** — Create a copy to use as a starting point for a new template
* **Delete** — Permanently remove the template (confirmation required)

🚨 **Important:** Deleting a template does not affect alerts or cases already created from it. However, any Rules or Workflows using the deleted template will need to be updated.

---

# Using Templates When Creating Manually

When creating an alert or case manually, a **Create From Template** field appears at the top of the creation form.

1. Open the **Create Alert** or **Create Case** form
2. Click the **Create From Template** field and select a template
3. The form fields pre-fill based on the template configuration
4. Review and adjust any fields as needed
5. Click **Save**

🧠 **Good to Know:** Templates pre-populate fields but don't lock them. You can override any value before saving.

---

# Using Templates in Rules and Workflows

Alert and Case Templates integrate directly with Rules and Workflows via the **Create Alert** and **Create Case** actions.

1. Open a Rule or Workflow and add a **Create Alert** or **Create Case** action
2. In the action configuration, locate the **Alert Template** or **Case Template** field
3. Select the template you want to apply
4. The action fields pre-fill from the template
5. Adjust any fields as needed for the automation context

---