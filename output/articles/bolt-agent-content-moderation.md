---
title: Bolt Agent Content Moderation
url: https://help.element451.com/en/articles/9859790-bolt-agent-content-moderation
collection: Bolt AI
---

Automatically flag inappropriate, harmful, or manipulative content for review and intervention, creating a safer environment.

# Overview

The Content Moderation feature helps you maintain a safe and respectful environment by automatically flagging conversations that may contain inappropriate, harmful, or manipulative content (both text and images). With customizable actions and flags, you can manage flagged content efficiently and tailor responses based on the nature of the content.

[![](https://downloads.intercomcdn.com/i/o/1179101624/6379c6ff71c34dd3b5ed4dac/Content+Moderation+-+Highlights.png?expires=1784333700&signature=7cce6d850db91d11cfd59842cba90fe720610886b0e4af6a848e74761e050b85&req=dSEgH8h%2BnIddXfMW1HO4zVal8qmV6ilTSV2GBJnFSwUqCPSZvE5v8sFvBCXC%0AbyC%2B5Kta5Mbpl4rhMf4%3D%0A)](https://downloads.intercomcdn.com/i/o/1179101624/6379c6ff71c34dd3b5ed4dac/Content+Moderation+-+Highlights.png?expires=1784333700&signature=7cce6d850db91d11cfd59842cba90fe720610886b0e4af6a848e74761e050b85&req=dSEgH8h%2BnIddXfMW1HO4zVal8qmV6ilTSV2GBJnFSwUqCPSZvE5v8sFvBCXC%0AbyC%2B5Kta5Mbpl4rhMf4%3D%0A)

We use OpenAI’s secure content moderation API to scan messages for potential risk indicators. OpenAI’s moderation models are trained on large, diverse datasets that include many real-world examples of content, enabling them to reliably identify common categories of harmful or sensitive material. While no automated system is perfect, this approach provides a generally accurate and dependable layer of content safety.

## Key Benefits of Content Moderation

* **Automated Safeguards**: Automatically flags harmful or inappropriate content, reducing the need for constant human oversight.
* **Customizable Responses**: Tailor your moderation settings based on the content category, ensuring a safe and respectful environment.
* **Efficient Management**: Easily filter and prioritize flagged conversations and automate actions to handle them efficiently.

## How it Works

1. Bolt AI monitors all inbound conversations where Bolt Agents actively participate.
2. When a message—whether text or image—matches one of the predefined flag categories ([listed and defined below](#h_1607d37fb3)), a flag is automatically added to the conversation; multiple flags can be applied if the message meets the description for more than one.
3. Flags are highlighted in yellow or red (depending on the '[type](#h_25c05a1aa2)' setting for that category) within your conversations inbox for easy visibility.
4. Custom [actions](#h_382c5c0e31) can be triggered immediately when the flag is applied to manage the conversation.
5. [Conversation rules](#h_d9938afb7a) can be configured to automate additional steps based on flagged content.

---

# Flag Types + Definitions

Each flag category, as listed below, is provided by OpenAI’s secure API integration, ensuring they are based on comprehensive, pre-set standards for identifying harmful or inappropriate content. These categories are predefined, meaning you cannot edit, delete, disable, or add new flag categories. However, you can customize the responses and actions when a conversation is flagged.

|  |  |
| --- | --- |
| **Flag Category** | **Description** |
| **Hate** | Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability, or caste. Harassment aimed at non-protected groups (e.g., chess players) is flagged under harassment. |
| **Hate/Threatening** | Hate speech that also includes threats of violence or serious harm towards the targeted group. |
| **Harassment** | Content that promotes or incites harassing language towards an individual or group. |
| **Harassment/Threatening** | Harassment that includes threats of violence or serious harm. |
| **Self-Harm** | Content that encourages or promotes self-harm, such as suicide, cutting, or eating disorders.  * Note: Self-harm-related flags do not have default actions because of their nature. You can add actions by editing the flag. |
| **Self-Harm/Intent** | Statements indicating intent or engagement in self-harm activities. |
| **Self-Harm/Instructions** | Content that provides advice or instructions on how to commit acts of self-harm. |
| **Sexual** | Content designed to arouse sexual excitement, promote sexual services, or describe sexual activity (excluding educational content). |
| **Sexual/Minors** | Sexual content involving minors under the age of 18. |
| **Violence** | Content that depicts death, physical violence, or injury. |
| **Violence/Graphic** | Content showing death, violence, or injury in graphic or explicit detail. |
| **Prompt Engineering\*** | Content that attempts to manipulate the agent by suggesting how it should behave or respond. While not always harmful, these instructions attempt to alter the bot’s intended functionality. |
| **Chatbot Behavior Instructions\*** | Content where the user tries to provide instructions that conflict with the agent's intended prompts, such as requesting false information. While protections exist to prevent this behavior from working, the flag highlights the intent. |

*\***Prompt Engineering** and **Chatbot Behavior Instructions** flags are not editable and cannot be modified.*

---

# Content Moderation Settings

## Accessing Settings

1. Navigate to **Engagement** > **Conversations > Settings**.
2. Click "Content Moderation" tab from the left-hand menu.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1922524707/464b6225095e10e43c68040c8cee/CleanShot%2B2026-01-08%2Bat%2B18_30_05-402x.png?expires=1784333700&signature=54da2f0f0c93f6f2861ba778885e860090372c3fe4b43ea281529cc377aa3cea&req=dSklFMx8mYZfXvMW1HO4zUWrtlwJCUPb8LuPNCNvrdnr9W%2F7%2FZ6SmQaTo7WW%0Aa4Nd%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1922524707/464b6225095e10e43c68040c8cee/CleanShot%2B2026-01-08%2Bat%2B18_30_05-402x.png?expires=1784333700&signature=54da2f0f0c93f6f2861ba778885e860090372c3fe4b43ea281529cc377aa3cea&req=dSklFMx8mYZfXvMW1HO4zUWrtlwJCUPb8LuPNCNvrdnr9W%2F7%2FZ6SmQaTo7WW%0Aa4Nd%0A)
3. Each flag category is listed here for your configuration.

   * Note: Self-harm-related flags do not have default actions because of their nature. You can add actions by editing the flag.
4. To configure the settings for a flag category, click the **three dots** and then **edit**. As a reminder, flag categories are predefined, meaning you cannot delete, disable, or add new flag categories.
5. From there, you can adjust the *message*, *priority*, and *actions*. Continue reading to learn about each setting.

   [![](https://downloads.intercomcdn.com/i/o/1177007904/6adde895fedce2586c572d8e/Conten+Moderation+-+Flag+Settings.png?expires=1784333700&signature=43099448b7f7c79e4c45614bc2b88e257e5a76731a3e976744c520324be363cb&req=dSEgEcl%2BmohfXfMW1HO4zeihgujAXIZLQIyCBlJamTAeK3DZdbvXmksPT8F1%0AEy2r%0A)](https://downloads.intercomcdn.com/i/o/1177007904/6adde895fedce2586c572d8e/Conten+Moderation+-+Flag+Settings.png?expires=1784333700&signature=43099448b7f7c79e4c45614bc2b88e257e5a76731a3e976744c520324be363cb&req=dSEgEcl%2BmohfXfMW1HO4zeihgujAXIZLQIyCBlJamTAeK3DZdbvXmksPT8F1%0AEy2r%0A)

## Message

You can configure a custom message to be displayed to the external participant when their message is flagged. If no custom message is added, no message will be shown.

**Multiple Flags Scenarios:** In cases where a conversation triggers multiple flags, we determine which message to display as follows:

1. The flag types are evaluated to determine which message is shown.
2. If one flag has a higher type (Alert), its custom message will be displayed.
3. If the flags have the same type (Alert or Warning) and one has a custom message, that message will be shown.
4. If the flags have the same type (Alert or Warning) and more than one has a custom message, we will randomly select one of those messages to display.

[![](https://downloads.intercomcdn.com/i/o/1177005463/6f4312731efa61ca59132fcf/Content+Moderation+Custom+Message.png?expires=1784333700&signature=46806603e61f2232668f23f5edb39c814db87db3b080eac34082b8fef19e7c89&req=dSEgEcl%2BmIVZWvMW1HO4zZJYgMrFbSk%2B2xrUL7ZlNh%2FL0piJe7usb3IBTjZe%0A8wdHVs%2BFbrdSvKy4gOw%3D%0A)](https://downloads.intercomcdn.com/i/o/1177005463/6f4312731efa61ca59132fcf/Content+Moderation+Custom+Message.png?expires=1784333700&signature=46806603e61f2232668f23f5edb39c814db87db3b080eac34082b8fef19e7c89&req=dSEgEcl%2BmIVZWvMW1HO4zZJYgMrFbSk%2B2xrUL7ZlNh%2FL0piJe7usb3IBTjZe%0A8wdHVs%2BFbrdSvKy4gOw%3D%0A)

## Type

Define how flagged conversations are highlighted in your conversations inbox:

* **Alert**: The conversation is highlighted in red.
* **Warning**: The conversation is highlighted in yellow.

**Multiple Flag Scenarios**: If a conversation triggers multiple flag categories with both types (Alert and Warning), the **Alert** type (red) will take priority for formatting.

An example of how they appear is provided in the [next section](#h_ebba69112c).

## Actions

Choose **one**, **both**, or **none** of these actions depending on what you want to happen when a conversation is flagged for this category:

* Disable Agent: Automatically turns off the Bolt Agent for the flagged conversation. This is an optional safety action. Conversation Rules that use the Content Moderation Condition run immediately and do not require the agent to be disabled.
* **Block Conversation**: Prevents the external participant from sending further messages in the flagged conversation.

![](https://downloads.intercomcdn.com/i/o/1177022465/207be830c02f73bcb7a24fc2/Note.png?expires=1784430000&signature=1ea98bf4c9dbe3f4c9f9edb0376210be7866353f7421bca32bec8ba6824baeba&req=dSEgEcl8n4VZXPMW3Hu4geuq6qka5O0UWzb5qtjWQlpRlsn0SAayAqa78e3j%0A6A%3D%3D%0A) Selecting no actions will **not** disable the flag. Conversations will still be flagged and formatted accordingly in your conversations inbox.

## Flag Setting Defaults

Below, we outline the default settings for each flag category, including the message displayed to external participants, the flag type, and the actions taken. You are welcome to customize these settings to fit your needs. However, please note that the **Prompt Engineering** and **Chatbot Behavior Instructions** flags are not editable and cannot be modified.

* **Sexual**

  + Message: “This conversation has been flagged for sexual content. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation
* **Hate**

  + Message: “This conversation has been flagged for hate speech. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Hate/Threatening**

  + Message: “This conversation has been flagged for threatening hate speech. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Harassment**

  + Message: “This conversation has been flagged for harassment. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Harassment/Threatening**

  + Message: “This conversation has been flagged for threatening harassment. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Self-Harm**

  + Message: No message provided
  + Type: Alert
  + Actions: No default actions

* **Self-Harm/Intent**

  + Message: No message provided
  + Type: Alert
  + Actions: No default actions

* **Self-Harm/Instructions**

  + Message: No message provided
  + Type: Alert
  + Actions: No default actions

* **Sexual/Minors**

  + Message: “This conversation has been flagged for sexual content involving minors. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Violence**

  + Message: “This conversation has been flagged for violence. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Violence/Graphic**

  + Message: “This conversation has been flagged for graphic violence. Please be aware that this is a violation of our community guidelines.”
  + Type: Alert
  + Actions: Turn off Agent, Block Conversation

* **Prompt Engineering (Not Editable)**

  + Message: “This conversation has been flagged.”
  + Type: Warning
  + Actions: Turn off Agent, Block Conversation

* **Chatbot Behavior Instructions (Not Editable)**

  + Message: “This conversation has been flagged.”
  + Type: Warning
  + Actions: Turn off Agent, Block Conversation

---

# Viewing + Managing Flags in Conversations

Viewing and managing your conversation flags is facilitated through your Conversations Inbox. We recommend being familiar with the layout and features of the inbox. This information can be found in the [Getting Started with Conversations](https://help.element451.com/en/articles/1894279-getting-started-with-conversations) and the [Conversations Inbox](https://help.element451.com/en/articles/8507376-conversations-inbox) articles.

## Viewing Flagged Conversations + Reasoning

### Inbox View

Flagged conversations are denoted by special formatting in your Conversations Inbox.

* **Red**: Alert Type Flag
* **Yellow**: Warning Type Flag  
  ​

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1221116929/c0c1d9c3d7542ad18104abe5568d/Content%2BModeration%2B-%2BInbox%2BFormatting.png?expires=1784333700&signature=0728f5f76ddf4efd07418cdf0bd804f1a662f2312f0f591e713495558041cf29&req=dSIlF8h%2Fm4hdUPMW1HO4zaKngB%2BIhLKefsi30tC5PXnTJD2Er5EDCgljQ%2FG6%0AXJFE%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1221116929/c0c1d9c3d7542ad18104abe5568d/Content%2BModeration%2B-%2BInbox%2BFormatting.png?expires=1784333700&signature=0728f5f76ddf4efd07418cdf0bd804f1a662f2312f0f591e713495558041cf29&req=dSIlF8h%2Fm4hdUPMW1HO4zaKngB%2BIhLKefsi30tC5PXnTJD2Er5EDCgljQ%2FG6%0AXJFE%0A)

### Conversation View

Once the flagged conversation is open, you can view more details about the flag:

* **Flagged Message**: The message bubble will be highlighted in red or yellow based on the flag type.
* **Flag Name**: Under the bubble, the text "This message has been flagged" will appear with the flag name listed.
* **Reasoning**: When a conversation is flagged, you can now hover over the "this message has been flagged" text to view the specific reasoning behind the content's flag. This reasoning, generated by Bolt, is tied directly to the flagged message, meaning not every instance of flagged content (e.g., self-harm or violence) will have the same explanation.   
  ​

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1221116130/7cc63371bbc53a5f5907abf72b46/content%2Bflag%2Bhover%2Breasoning.png?expires=1784333700&signature=8fd6caccb5be7fe1826eb007a6bcb84a5a3bc49f75179a40f7990a7ca9e91f64&req=dSIlF8h%2Fm4BcWfMW1HO4zd2%2FW1JMZuT%2Fbl4hvhzSQJjoxsyp1l%2BGVbw78YYG%0AXufj%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1221116130/7cc63371bbc53a5f5907abf72b46/content%2Bflag%2Bhover%2Breasoning.png?expires=1784333700&signature=8fd6caccb5be7fe1826eb007a6bcb84a5a3bc49f75179a40f7990a7ca9e91f64&req=dSIlF8h%2Fm4BcWfMW1HO4zd2%2FW1JMZuT%2Fbl4hvhzSQJjoxsyp1l%2BGVbw78YYG%0AXufj%0A)

## Adding + Changing + Removing Flags

Conversation flags are managed directly within the conversation. Go to the **Manage** tab in the right-side conversation panel to:

* Remove or change an existing flag.
* Manually add a flag to any conversation.

[![](https://downloads.intercomcdn.com/i/o/1176949346/ee8246c1ac5b30351c682f0a/Content+Moderation+-+Manage+Tab.png?expires=1784333700&signature=e8eb2fa0d5ce10115ed8b8d8b42c871c62b69280029e0e8a2414c405921cdc81&req=dSEgEMB6lIJbX%2FMW1HO4zQ3TSsuZtQfiGuPc0Hr4yLwtSW9fdfmtDK02KpNj%0Ae2qxKUKxBLhOZLZf5ms%3D%0A)](https://downloads.intercomcdn.com/i/o/1176949346/ee8246c1ac5b30351c682f0a/Content+Moderation+-+Manage+Tab.png?expires=1784333700&signature=e8eb2fa0d5ce10115ed8b8d8b42c871c62b69280029e0e8a2414c405921cdc81&req=dSEgEMB6lIJbX%2FMW1HO4zQ3TSsuZtQfiGuPc0Hr4yLwtSW9fdfmtDK02KpNj%0Ae2qxKUKxBLhOZLZf5ms%3D%0A)

## Filtering Conversations by Flags

You can filter your conversations inbox on moderation flags. This lets you quickly address flagged conversations based on their priority and content. [Explore more on conversation filter →](https://help.element451.com/en/articles/8507376-conversations-inbox#h_2d28443ba5)

[![](https://downloads.intercomcdn.com/i/o/1176972731/24f86570ff0ac9a4a843c3db/Content+Moderation+-+Filters.png?expires=1784333700&signature=c33fef71e5af842a82fa9a8994103eb84682bc501a23ca40c60f177ae653a710&req=dSEgEMB5n4ZcWPMW1HO4zR9EuaOr9%2FolXpB2F5V0CGcO4yHLSR87L2fY35%2BF%0AooHIcYx9ts5cLyoVlI4%3D%0A)](https://downloads.intercomcdn.com/i/o/1176972731/24f86570ff0ac9a4a843c3db/Content+Moderation+-+Filters.png?expires=1784333700&signature=c33fef71e5af842a82fa9a8994103eb84682bc501a23ca40c60f177ae653a710&req=dSEgEMB5n4ZcWPMW1HO4zR9EuaOr9%2FolXpB2F5V0CGcO4yHLSR87L2fY35%2BF%0AooHIcYx9ts5cLyoVlI4%3D%0A)

---

# Automating Flag Management with Conversation Rules

When a conversation is flagged, a conversation rule can automatically trigger an action. The most common action is **assigning the conversation to an internal user or team** for review.

Before setting up your rule, ensure you understand how [conversation rules](https://help.element451.com/en/articles/1930478-conversation-rules) work.

**Important**: Most conversation rules only run after the Bolt Agent disconnects. However, rules using the **“Content Moderation Condition”** are an exception. They execute immediately when triggered, even if the agent is still active. You do *not* need to add the “Turn Off Bolt Agent” action for these moderation rules to run.

## Setting Up Your Rule

* **Condition:** Use the **moderation flag** condition.
* **Action:** Choose one or multiple actions. We recommend the "**assignment**."

  + A benefit of using "**assignment"** is the ability to assign flagged conversations to a **team** instead of a single individual. This ensures that multiple team members, such as an **intervention team** or **counseling team**, receive the notification, allowing for a faster response and reducing the risk of a flagged conversation going unnoticed.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1377226631/81e9fd1d2c518a39df343aa3d6fa/Content-2BModeration-2B--2BConvo-2BRule.png?expires=1784333700&signature=f13dd81cbe3595bd879c6621221bb90be89001bfc8f05bf903ff7df480e0e885&req=dSMgEct8m4dcWPMW1HO4zRGAr6%2F9gybXrd2SPE7OfnL8gXI8h4kXo6g3lbl8%0Aov55LB5rtDSqbegpbGE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1377226631/81e9fd1d2c518a39df343aa3d6fa/Content-2BModeration-2B--2BConvo-2BRule.png?expires=1784333700&signature=f13dd81cbe3595bd879c6621221bb90be89001bfc8f05bf903ff7df480e0e885&req=dSMgEct8m4dcWPMW1HO4zRGAr6%2F9gybXrd2SPE7OfnL8gXI8h4kXo6g3lbl8%0Aov55LB5rtDSqbegpbGE%3D%0A)

## Email Notifications + Inbox Visibility

When a flagged conversation is assigned to an internal user, an **email notification** is sent automatically. These emails include a **prominent marker** at the bottom indicating the conversation was flagged.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1377227329/67524cbbaa9a09c95ca5f0b87364/Content%2BMod%2B-%2BEmail%2BNotification.png?expires=1784333700&signature=eb613ca27a5c41397ecd822bc8662ec83af24039f2c9da0881f637da74c41fec&req=dSMgEct8moJdUPMW1HO4zX4peDFYkROQZXlLIHEUTQm9Yg85BL9%2Fufy%2BOxAg%0Ac4X%2BRQAGUQaQMAAc1lc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1377227329/67524cbbaa9a09c95ca5f0b87364/Content%2BMod%2B-%2BEmail%2BNotification.png?expires=1784333700&signature=eb613ca27a5c41397ecd822bc8662ec83af24039f2c9da0881f637da74c41fec&req=dSMgEct8moJdUPMW1HO4zX4peDFYkROQZXlLIHEUTQm9Yg85BL9%2Fufy%2BOxAg%0Ac4X%2BRQAGUQaQMAAc1lc%3D%0A)

For even more inbox visibility, consider using your email provider’s filtering options. In **Gmail**, for example, you can:

1. Create a filter for emails from **[notifications@element451.io](mailto:notifications@element451.io)**.

2. Include the phrase **“this message has been flagged”** in the filter criteria.

3. Apply actions like labeling, marking as important, or forwarding for better management.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1377227328/ebffa846a276e7e284ed11aa263e/CleanShot%2B2025-02-12%2Bat%2B08_42_26.png?expires=1784333700&signature=efdb167ad3a3da942b8c84e406e2a2877578691302a20260aab8993528bb6551&req=dSMgEct8moJdUfMW1HO4zaAWUV5Ojy%2FnHlH0tJpUawF2Rg1PRgubdA3OkiNx%0AsO0TyU7JyYz4JzJlQyA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1377227328/ebffa846a276e7e284ed11aa263e/CleanShot%2B2025-02-12%2Bat%2B08_42_26.png?expires=1784333700&signature=efdb167ad3a3da942b8c84e406e2a2877578691302a20260aab8993528bb6551&req=dSMgEct8moJdUfMW1HO4zaAWUV5Ojy%2FnHlH0tJpUawF2Rg1PRgubdA3OkiNx%0AsO0TyU7JyYz4JzJlQyA%3D%0A)

***IMPORTANT****: Conversation rules help automate flag management and improve visibility, but they do not guarantee that all flagged conversations will be seen or acted upon. Email notifications may be affected by factors outside Element451’s control, such as spam filtering or inbox settings. We recommend that institutions regularly review flagged conversations within the platform and establish internal monitoring procedures to ensure timely intervention.*

[Explore More: Conversation Rules →](https://help.element451.com/en/articles/1930478-conversation-rules)

---