---
title: Bolt Agent Skills
url: https://help.element451.com/en/articles/8993380-bolt-agent-skills
collection: Bolt AI
---

# Overview

This article covers the built-in system skills that help Bolt Agents provide information and complete standard Element451 tasks. These are separate from institution-authored Custom Skills.

To enable or disable a built-in system skill, navigate to Engagement > Bolt Agents and edit the agent's settings. Custom Skills are created at the instance level, then enabled and prioritized separately for each agent.

## Access to Skills

The Bolt Agent skills available to your team depend on the Element451 package you have. For example, if your plan does not include application management, your agents will not have access to application-related skills.

---

# Built-in System Skills

|  |  |
| --- | --- |
| **Human Team Member Handoff** | Enables the native human handoff flow when a student asks for a person or the agent cannot resolve the inquiry. Automatic agent-to-agent handoffs may select another agent in the same Team. A configured Custom Skill @Hand Off to Agent action can explicitly target an agent outside the Team and can be used by the default agent.    Explore more on handoffs in [this article](https://help.element451.com/en/articles/8993398-bolt-agent-handoffs). |
| **Start an Application** | Guides the student through starting and completing an application. |
| **Get Application Status** | Provides the student's current application status. |
| **Application Status Checklist** | Retrieves the status of the student’s application checklist. |
| **Register for Event** | Assists the student in registering for an event. |
| **Schedule Appointments** | When enabled, the agent will guide the student through scheduling an appointment.​Read how the Schedule Appointments skill works below. |
| **Common App Knowledge** | Utilizes data from Common App to provide relevant information. |
| **Financial App Knowledge** | Uses data from StudentAid.gov to help with federal student aid questions. |
| **Inquiry Flow** | The Inquiry Flow skill gathers key information from prospective students and submits an inquiry on their behalf. Think of it as a digital form.    Explore the Inquiry Flow skill more in the next section. |
| **User Data Access Skill** | Enables agents to access and share student record data stored in:  * Custom fields * Contact [network data](https://help.element451.com/en/articles/9884014-network-connect-contacts-with-internal-users) (The agent can answer questions like who the contact's academic advisor is when that data exists in Network)  Authentication required to access this info. ​ Once enabled, custom field visibility is controlled via *Settings > Permissions* on the individual Agent. Navigate there to search and select custom field(s). Upload-type fields are not supported. |
| **Schedule AI Follow Up (Email, SMS, Phone Call)** | Allows the agent to schedule a follow-up message to a student via email, SMS, or phone call at a future date and time. The agent will automatically reach out. |

---

# How Specific Skills Work

## Schedule Appointments

1. The student selects the appointment type and time.
2. The agent finds all users available for that type and time.
3. The agent checks if the student has an assignee in that list of available users.
4. If yes, the appointment is booked with that assignee.
5. If not, the agent moves to the next step.
6. The agent counts all appointments in the next 30 days for the users in the list of available users.
7. The agent books the appointment with the user who has the fewest appointments.

## Inquiry Flow

When an agent detects that the user intends to inquire about studying at your institution—whether through text chat or voice conversation—it will initiate the Inquiry Flow.

### Supported Channels

The Inquiry Flow skill works across multiple channels:

* **Text** **Chat** – Web chat, SMS, and other text-based conversations
* **Advanced** **Voice** **Mode** – Real-time phone conversations where the agent speaks naturally with the caller

### Triggering the Inquiry Flow

Phrases like these trigger the intent:

* "I am interested in studying at Fire University."
* "I am interested in studying Biology."
* "I am interested in taking courses in Biology."
* "Can you send me more info about Biology?"

For voice conversations, the agent listens for the same intent spoken aloud and responds conversationally.

### Required Information Collected

By default, the agent will require the student to provide:

* *First Name*
* *Last Name*
* *Email Address*

For inbound phone calls, the caller's phone number is also captured automatically.

### Optional Information Collected

When the skill is enabled you will be prompted to select ***additional*** fields the agent will try to collect when capturing lead information. This is not required and only allows you to collect these additional data fields if you choose.

* I*ntended Major*
* *Intended Term*
* *Date of Birth*.

### Actions Taken

After gathering the information, the agent will take the following actions:

* If the student has an existing record, a prospect milestone is added.
* If the student record does not exist, a user will be created with a prospect milestone.

### Important Notes

* **Skill** **Activation:** The Inquiry Flow skill must be enabled for the agent to launch the flow. Ensure the Inquiry Flow skill is activated in the agent's settings.
* **Advanced** **Voice** **Mode:** When AVM is enabled, the Inquiry Flow skill works with inbound phone calls. The agent will verbally ask for the required information and create or update the user record when the conversation completes. Callers from unknown numbers will have a new record created.
* **Majors** **and** **Terms:** When enabled, agents can also list available majors and terms.
* **No** **Authentication:** The agent-submitted inquiry does not authenticate the user via the email address provided. The inquiry flow behaves the same as submitting a form.
* **Major** **Matching:** Majors are matched using machine learning, which can result in mismatches, especially for majors with similar names.

### Check Out Inquiry Flow in Action

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1469261726/c1708f4c6439656042dc9c683611/Bolt-2BBot-2B--2BInquiry-2BFlow-2BSkill2.gif?expires=1784333700&signature=e5ed0df54602f0014184fc37581979b3dc53bd5909321036aabefbc620b3042e&req=dSQhH8t4nIZdX%2FMW1HO4zYkTxZ7OTMwNLEhxTKfn%2FAUJfO6IHES2S52n8vTE%0AjJWZ2WcjDsRVgGErYsQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1469261726/c1708f4c6439656042dc9c683611/Bolt-2BBot-2B--2BInquiry-2BFlow-2BSkill2.gif?expires=1784333700&signature=e5ed0df54602f0014184fc37581979b3dc53bd5909321036aabefbc620b3042e&req=dSQhH8t4nIZdX%2FMW1HO4zYkTxZ7OTMwNLEhxTKfn%2FAUJfO6IHES2S52n8vTE%0AjJWZ2WcjDsRVgGErYsQ%3D%0A)

### Pro Tip: Combine Convo Starters + Inquiry Flow

Combine Conversation Starters with Inquiry Flow

Make the Inquiry Flow even more effective by using conditional Conversation Starters to prompt students to kick off the flow. For example, set up a Conversation Starter on your biology program page that says, “I’m interested in studying biology.” When a student clicks on it, the agent will initiate the Inquiry Flow.

Benefits of Combining These Features:

* Drives more inquiries by prompting students in relevant contexts.
* Collects more qualified leads by targeting key pages like academic programs.
* Gathers more accurate major information since the major is directly prompted.
* Provides a smoother experience by initiating the flow from a student prompt.

### Did You Know?

Bolt Discovery also has an inquiry flow skill. It intelligently uses AI to determine if and when additional information may be needed, prompting users to complete a form to request it. The wording of the prompt may vary, but it essentially asks, “Would you like more information on this topic?” You can [read more about it here](https://help.element451.com/en/articles/9397400-bolt-discovery-settings#h_20a3c14404).

​

## User Data Access Skill

### Enabling the Skill + Permissions

* Enable the **User Data Access** skill to grant access to specific custom fields.
* Once enabled, custom field visibility is controlled via *Settings > Permissions* on the individual Agent. Navigate there to search and select custom field(s). Upload-type fields are not supported.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1999745022/fdf5ab345beeac00d4f067eac293/CleanShot%2B2026-01-28%2Bat%2B12_56_58.png?expires=1784333700&signature=e35ac04eb404e837a813293569ec01fbfcb1f816f3aa3c1971496ab117674989&req=dSkuH856mIFdW%2FMW1HO4zfb0xbaYgcveUyJDXqyfPfLOk6AKbRqvU4WeI%2FGD%0Am7B0%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1999745022/fdf5ab345beeac00d4f067eac293/CleanShot%2B2026-01-28%2Bat%2B12_56_58.png?expires=1784333700&signature=e35ac04eb404e837a813293569ec01fbfcb1f816f3aa3c1971496ab117674989&req=dSkuH856mIFdW%2FMW1HO4zfb0xbaYgcveUyJDXqyfPfLOk6AKbRqvU4WeI%2FGD%0Am7B0%0A)

### How Does the Skill Work

1. The student asks a question that relates to a custom field, like “What hold is on my account preventing me from registering for classes?”—which triggers the skill.
2. The agent asks the student to provide their email address.
3. A confirmation code is sent to that email.
4. The student enters the code in the chat to authenticate.
5. If that email address is associated with a contact record in Element451, the student is authenticated. If the email does not exist, the agent will reply with a similar message to "It seems that the email address you provided does not match our records. Please double-check the email or try a different one."
6. Once authenticated, the agent will access and share the specific custom field data the student inquired about.
7. A **log out** button appears at the bottom of the chat so students can end access at any time.

### Important Notes

* **Authentication via code sent to an email address associated with an existing Element451 record is required** before any personal data is shared.
* Agents will display a message during authentication: *Just a heads-up: After logging in, your data will be accessible in this chat until you log out.*

​

---