---
title: Getting Started with Workflows + Rules
url: https://help.element451.com/en/articles/1500265-getting-started-with-workflows-rules
collection: Workflows + Rules
---

Start here to learn the basics about Workflows and Rules and automating communications and actions in Element451.

# Overview

Workflows and Rules within Element451 are powerful tools designed to revolutionize how you automate communications, profile management, and other actions, ensuring operational efficiency and precision while maintaining engagement with students.

This article delves into the distinct capabilities of Workflows and Rules, from managing communication campaigns through Workflows to executing immediate, data-driven actions with Rules. With a clear understanding of their unique functionalities and applications, you'll be well-equipped to choose the solution that aligns with your needs.

## Glossary of Terms

* **Audience:** Individual contacts or segments added manually to a Workflow.
* **Triggers:**  The event or action that enrolls a contact in a Workflow or Rule when certain conditions are met. Triggers often involve actions taken by contacts, such as starting or completing an application, registering for an event, or entering a specific segment.
* **Steps**: The building blocks of Workflows and Rules, representing a sequence through which students or users progress.
* **Actions**: The specific activities or operations that occur at a particular step in a Workflow or Rule. A step can contain multiple Actions. Actions include things like assigning a label or sending a communication.
* **Conditions**: Criteria that provide control over the execution of actions within a step based on specific requirements.
* **Delays**: A feature exclusive to Workflows, a delay controls when a step happens. This setting is particularly beneficial in structuring communication strategies.

[Learn More: Components of Workflows + Rules](https://help.element451.com/en/collections/124571-workflow-specifications)

## Timing + Evaluations of Workflows + Rules

* When working with Workflows + Rules, it is important to note that these features are optimized for efficiently processing bulk actions rather than for speed. Therefore, **triggers and actions are queued for evaluation**. The evaluation of a trigger varies on the trigger type, but for example, the joined and left segment trigger is evaluated about every five minutes, whereas the added/removed label trigger is evaluated about every minute.

## Helpful Tips

* **Plan**: Before creating a Workflow or Rule, it can be immensely helpful to think about the specific criteria and Contacts you want to target. We recommend drawing a map or flowchart or writing an outline.
* **Test**: After creating your Workflow or Rule, test them thoroughly. Ensure they capture the right Contacts and trigger at the intended times.
* **Review**: As your institution evolves, so will your target segments and relevant dates. Schedule and conduct regular reviews of your active Workflows and Rules to maintain their effectiveness.

---

# Accessing Workflows + Rules

* To access **Workflow:** Navigate to **Data + Automation** > **Workflows** > **All** **Workflows**
* To access **Rules**: Navigate to **Data + Automation** > **Workflows** > **Rules**

[![](https://downloads.intercomcdn.com/i/o/940565521/eeb5d9edba124849051576e0/Accessing+Workflows+and+Rules.gif?expires=1784333700&signature=85012b452f025cddb60a1d3381c506d3c104cac06691aeed18222cc1c00dd4dd&req=fSQnE897mINeFb4f3HP0gJDYZyiabHSutq7uA4i3zyUOgjo9uY8LEmj1F5ec%0AzgS%2FVWZdPT6FsvElxQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/940565521/eeb5d9edba124849051576e0/Accessing+Workflows+and+Rules.gif?expires=1784333700&signature=85012b452f025cddb60a1d3381c506d3c104cac06691aeed18222cc1c00dd4dd&req=fSQnE897mINeFb4f3HP0gJDYZyiabHSutq7uA4i3zyUOgjo9uY8LEmj1F5ec%0AzgS%2FVWZdPT6FsvElxQ%3D%3D%0A)

---

# Workflows vs Rules

At first glance, Workflows and Rules may appear similar in their creation and management processes. However, despite their seemingly parallel interfaces and functionalities, they harbor distinct differences. This section covers how each one functions and guides you in choosing the right one for your needs.

|  |  |  |
| --- | --- | --- |
|  | **Workflows** | **Rules** |
| **Step Delays** | ✅ | ❌ |
| **Initiation by Trigger** | ✅ | ✅ |
| **Initiation by Schedule** | ❌ | ✅ |
| **Run Limit** | ✅ | ❌ |

# What is a Workflow?

A Workflow in Element451 can be thought of as a dynamic process comprising a sequence of automated steps designed to manage and execute complex tasks with a high degree of precision, particularly in the context of student engagement and communication.

In a Workflow, actions are carried out in a specific order, with individuals automatically entering the Workflow due to certain changes in their information, such as their status as a prospect or applicant, or because of specific actions they take, like submitting a form or an application. At each stage of the Workflow, a designated action takes place—often incorporating timed delays between steps to enhance control.

At every step, individuals could either exit the Workflow, advance to the subsequent step or even transition to a different Workflow, depending on the Workflow's configuration. This feature is especially beneficial for managing communication campaigns, allowing for the strategic timing of messages to ensure that students receive information precisely when it's most relevant and impactful.

|  |  |
| --- | --- |
| **Audience** | Select individual contacts or segments to add to your Workflow. Adding the audience in this way will immediately enroll those contact(s) into the Workflow. |
| **Trigger** | Contacts are added asynchronously to a Workflow via Trigger(s), a specific action or event that starts the Workflow for that contact when certain conditions are met. |
| **Run Limit** | Workflows maintain a record of user participation, ensuring unique engagement per user in user-based scopes while allowing repetition in entity-based scopes, making them versatile for different scenarios. |
| **Delay** | Workflows allow for the introduction of delays between steps, enabling a controlled timing of actions, which is essential for spacing out communications and other time-sensitive tasks. |

### Example Use Cases

* Sending an email to students who submit your request for information form
* Creating a task for the Contact's assignee to follow up after submitting the request for information form
* Sending a series of email and SMS messages based on important dates, actions a Contact takes (e.g., clicking a link in an email), or a combination of both

# What is a Rule?

A Rule in Element451 is also a sequence of automated steps designed to manage and execute complex tasks. Once initiated, a Rule promptly and sequentially executes a series of predefined actions based on set conditions.

However, there are two types of Rules—**Triggered** and **Scheduled**—which you'll learn more about below:

|  |  |
| --- | --- |
| **Audience** | **Triggered** **Rule**: Unlike Workflows, Rules do not allow you to select or load contacts for an immediate run. The contacts enrolled in your Rule are determined dynamically based on the trigger.    **Scheduled** **Rule**: If using the **Scheduled** type for your Rule, you will be able to load a Segment when adding an Action. |
| **Trigger** | **Triggered Rule**: Contacts are added asynchronously to a Rule via trigger(s), a specific action or event that starts the Rule for that contact when certain conditions are met. The trigger options for a Rule are the same as for a Workflow.    **Scheduled** **Rule**: Using the Scheduled type of Rule, the schedule acts as the trigger. You can configure one-time or recurring execution, offering flexibility in managing tasks that need to occur at specific times or intervals.    When using the **Scheduled** type for a Rule, you are limited to the following actions:  * **Create Login Token** * **Create Profile** * **Validate Phone Numbers** * **Run Rule** |
| **Run** **Limit** | Unlike Workflows, Rules do not have participation limits for users. A user can be part of a Rule multiple times, allowing for repetitive actions in response to recurring events or conditions. |
| **Delay** | Delays are not available for Rules. Once initiated, steps within a Rule are executed sequentially and instantly, without any pause, ensuring immediate response to the trigger. |

### Example Use Cases

* Auto-submit a completed application on behalf of the student
* Creating sources
* Converting family member data to relationship records
* Adding an assignee to a person's record
* Adding an assignee to a territory
* Attaching labels or adding assignees during data import
* Assigning tasks to assignees based on specific student activities or missed appointments

---

# Creating a Workflow

Step-by-step guide to creating a Workflow

[Learn More: Creating a Workflow](https://help.element451.com/en/articles/1500282-how-to-create-a-workflow)

---

# Managing a Workflow

Editing, stopping, starting, and seeing who’s in a Workflow

[Learn More: Managing a Workflow](https://help.element451.com/en/articles/1500286-how-to-manage-a-workflow)

---

# Creating a Rule

Step-by-step guide to creating a Rule

[Learn More: Creating a Rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule)

---

# Managing a Rule

Editing, stopping, starting, and seeing who’s in a Rule

[Learn More: Managing a Rule](https://help.element451.com/en/articles/8860013-how-to-manage-a-rule)

---

# Frequently Asked Questions

Find quick answers to common questions about Workflows + Rules in our dedicated [FAQ article](https://help.element451.com/en/articles/10618199-workflows-rules-frequently-asked-questions).

​

---