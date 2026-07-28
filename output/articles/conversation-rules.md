---
title: Conversation Rules
url: https://help.element451.com/en/articles/1930478-conversation-rules
collection: Conversations
---

Use conditions and actions to automate processes such as assign, tag, close, reply, and handoff in Conversations.

# Overview

Conversation Rules allow users to automate processes within Conversations. Users can configure rules that trigger customizable actions when specified conditions are met. The available actions include assigning conversations, adding participants, tagging, closing, replying, and running workflow rules. Conversation Rules provide a way to streamline conversation workflows based on defined criteria.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1557576523/b3df171d69a44a7e5698dac1087c/Convo+Rules+Flow+-+With+Content+Mod.png?expires=1784332800&signature=8fd633c03728428059a2e3add7b2409a331b267024f41183f2b2bd1101405b28&req=dSUiEcx5m4RdWvMW3nq%2BgWVllbK7MfnjphHZzLkwRVWOWdujckBRgFFfB0f2%0AFidR7Is5IMpBYJIeQoVpI00p1wQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1557576523/b3df171d69a44a7e5698dac1087c/Convo+Rules+Flow+-+With+Content+Mod.png?expires=1784332800&signature=8fd633c03728428059a2e3add7b2409a331b267024f41183f2b2bd1101405b28&req=dSUiEcx5m4RdWvMW3nq%2BgWVllbK7MfnjphHZzLkwRVWOWdujckBRgFFfB0f2%0AFidR7Is5IMpBYJIeQoVpI00p1wQ%3D%0A)

*Click the image to enlarge. ↗*

---

# When Do Rules Apply?

Conversation Rules are evaluated differently depending on whether Bolt Agents are involved. Let's break it down:

## Without Bolt Agents

Conversation Rules apply in the following scenarios:

* **New Conversations**: Rules are evaluated for the first message of a new inbound conversation. Rules don't apply to conversations you initiate from the dashboard or a student's profile.
* **Reopened Conversations**: If a closed conversation receives a new message, it's treated as a new conversation, and rules are re-evaluated.

  [![](https://downloads.intercomcdn.com/i/o/1178334616/1d69a54d86f5868df960fa36/Pro+Tip.png?expires=1784332800&signature=8c188a50f8af6ad86ef75fe9f65267285f99f7c33ddc84723fc43b5506993df5&req=dSEgHsp9mYdeX%2FMW3nq%2BgaPcz0qU5ynx2lZlV6GzcVumi1TW5bcnIVAJG3MO%0AZmTKuSFv1l0uhXpVOUEx6pF96gM%3D%0A)](https://downloads.intercomcdn.com/i/o/1178334616/1d69a54d86f5868df960fa36/Pro+Tip.png?expires=1784332800&signature=8c188a50f8af6ad86ef75fe9f65267285f99f7c33ddc84723fc43b5506993df5&req=dSEgHsp9mYdeX%2FMW3nq%2BgaPcz0qU5ynx2lZlV6GzcVumi1TW5bcnIVAJG3MO%0AZmTKuSFv1l0uhXpVOUEx6pF96gM%3D%0A)

  Close conversations when they're finished to ensure proper rule evaluation.

## With Bolt Agents

Generally, Conversation Rules don't apply when Bolt Agents are active in a conversation. However, there is one exception: **Bolt Agent Handoffs**.

If you have a rule with the "*Bolt Agent Handoff Intent*" condition, it will be evaluated when a handoff occurs. The "Team Member Handoff" agent skill (enabled at the agent level) disconnects the agent and triggers the conversation rules with handoff intent conditions. For a comprehensive look at Bolt Agent Handoffs, please read [this article](https://help.element451.com/en/articles/8993398-bolt-assistant-handoffs).

## Exception: Content Moderation Flags

Rules using the **“Moderation Flag”** condition are evaluated immediately when a flag is triggered by the content of a message, **regardless of whether the Bolt Agent is currently active or disabled**. This means that including or omitting the **“Disable Agent”** action in your flag settings has no impact on whether the rule will run.

However, there is one **important** limitation: Each **flag type** (e.g., *hate*, *self-harm*) can only be used **once across all conversation rules**. If the same flag type appears in multiple rules, **none** of those rules will run.

You can learn more about content moderation and flag configuration in [this article](https://help.element451.com/en/articles/9859790-bolt-agent-content-moderation).

---

# How are Rules Processed?

*This applies to conversations **without** Bolt Agents only.*

When an inbound message is received and matches the outlined criteria—a new message with no prior conversation history or a new message in a previously closed conversation—Element451 initiates a rule-checking process. The message is systematically compared against your custom rules in the **Conversation** **Settings** > **General** > **Automation** **Settings**.

1. This rule evaluation is conducted **sequentially**, from the top of your rule list to the bottom. This means the order in which your rules are arranged is critical; **rules are checked in the order they appear**.
2. The **first** **rule** that **meets** the conditions of the message is applied.
3. After applying this rule, the system ceases further checks for that message, ensuring that only the first matching rule is applied. Subsequent rules are bypassed.

### Special Case: Moderation Flag Conditions

Rules using the **“Moderation Flag”** condition work differently:

* They are evaluated **immediately when the content triggers a moderation flag**, regardless of whether a Bolt Agent is active or disabled.
* Only **one rule per flag type** (e.g., *hate, self-harm* ) can exist across your rules. If a flag type is used in multiple rules, **none of those rules will run**.

---

# Accessing Conversation Rules

To add rules, navigate to **Engagement** > **Conversations** > **Settings** > **General**.

[![](https://downloads.intercomcdn.com/i/o/860085843/8e623e52bc4c8fc7cb3f538c/Conversation+Rules.png?expires=1784332800&signature=79bde1509d50fb26920beabf7e7e40591327f38cb039c9d6433725e0f9215bca&req=fCYnFsF7lYVcFb4V1XW4gYvBL0nTkTSRBsCkwTcLXvPmr5EVsDsddGnV0g4%2B%0AKGBvw6CtsB9xTb%2FAFi0AkEAbDA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860085843/8e623e52bc4c8fc7cb3f538c/Conversation+Rules.png?expires=1784332800&signature=79bde1509d50fb26920beabf7e7e40591327f38cb039c9d6433725e0f9215bca&req=fCYnFsF7lYVcFb4V1XW4gYvBL0nTkTSRBsCkwTcLXvPmr5EVsDsddGnV0g4%2B%0AKGBvw6CtsB9xTb%2FAFi0AkEAbDA%3D%3D%0A)

---

# Adding a New Rule

To create a new rule:

1. Click **Add Rule** at the bottom of the **Automation** **Settings** section. Once clicked, a slide-out sheet will appear, allowing you to configure your new rule.

   [![](https://downloads.intercomcdn.com/i/o/860165051/cc40d7b23ed8185059c3f374/Add+Rule+Button.png?expires=1784332800&signature=da8aaed624192b44e30c75216a86896e70976f5ca4286a59b59eb10e22174c6a&req=fCYnF897nYReFb4V1XW4gWC6Rk3%2BqUUeIM3wwY%2Fi5SDZkW1CCFCwwBE1WWxU%0AZXuicJH8wTF4eSXW5hCbN1UM9g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860165051/cc40d7b23ed8185059c3f374/Add+Rule+Button.png?expires=1784332800&signature=da8aaed624192b44e30c75216a86896e70976f5ca4286a59b59eb10e22174c6a&req=fCYnF897nYReFb4V1XW4gWC6Rk3%2BqUUeIM3wwY%2Fi5SDZkW1CCFCwwBE1WWxU%0AZXuicJH8wTF4eSXW5hCbN1UM9g%3D%3D%0A)
2. Add a **name** for the rule at the top of the slide-out sheet.
3. Choose whether to enable it upon saving or leave it disabled (default). If you're going to test the new rule, we recommend leaving it disabled until you are ready to begin testing.
4. Add a **description** of the rule. This provides at-a-glance context of the rule when reviewing your list of rules on the Conversation Settings page.
5. Set your **condition(s)** for this rule. Each rule must have at least one condition. [You can learn more about the conditions below](#h_eb79d7d5ab).

   [![](https://downloads.intercomcdn.com/i/o/860159704/19486eeb060911ba316886d4/Convo+rules+-+add+condition+button.png?expires=1784332800&signature=98e7f2f91a01d1fb1df3e8f53e12ab669a716df0317e41412e92a66fa69aa75b&req=fCYnF8x3moFbFb4V1XW4gfDOQwBhh5HmaxcvhHwjrV1HJBYS0BUtSslb8hG6%0AKqbGM9fhneC56OyJYFy5wQJojQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860159704/19486eeb060911ba316886d4/Convo+rules+-+add+condition+button.png?expires=1784332800&signature=98e7f2f91a01d1fb1df3e8f53e12ab669a716df0317e41412e92a66fa69aa75b&req=fCYnF8x3moFbFb4V1XW4gfDOQwBhh5HmaxcvhHwjrV1HJBYS0BUtSslb8hG6%0AKqbGM9fhneC56OyJYFy5wQJojQ%3D%3D%0A)
6. Choose the **action(s)** for the rule to execute. Each rule must have at least one action. [You can learn more about the actions below](#h_30158d07f6).

   [![](https://downloads.intercomcdn.com/i/o/860160175/ae620f9774754bc443f76b72/convo+rules+-+add+action.png?expires=1784332800&signature=490d85aa98f21885a13929ca64cc6da075178f551bc019e126936cf0795c8fc7&req=fCYnF89%2BnIZaFb4V1XW4gaAJExlhOqaBnpiy801V7ib3ZgUBl5KaP3UwyH4I%0A%2FNCH5bhpysyMBuwADLumucgiag%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860160175/ae620f9774754bc443f76b72/convo+rules+-+add+action.png?expires=1784332800&signature=490d85aa98f21885a13929ca64cc6da075178f551bc019e126936cf0795c8fc7&req=fCYnF89%2BnIZaFb4V1XW4gaAJExlhOqaBnpiy801V7ib3ZgUBl5KaP3UwyH4I%0A%2FNCH5bhpysyMBuwADLumucgiag%3D%3D%0A)
7. Click **Save**
8. If you still need to enable your rule in step three, remember to enable it once you're ready to test or go live.

---

# Conditions and Actions

Conversation Rules are made up of **conditions** and **actions**.

## Conditions

Conditions define the criteria for the conversation rule to trigger and execute the specified action(s). Conditions allow you to target automation rules to specific situations and populations.

**If an inbound conversation meets the condition(s) of the rule, then the action will occur.**

### Condition Types

There are **five** types of conditions from which to choose, and you can **combine multiple types**:

* **Segment Reference**: This condition loads an existing user segment. For example, if you have a transfer student segment and want all inbound conversations by transfer students to be tagged 'transfer,' you could use this condition.
* **Segment Builder**: Creates a segment and filters your audience based on selected criteria.
* **Inbound Condition**: Allows the rule to apply only to messages from specific channels by specifying the conversation channel the message is received on, such as Email, SMS, WhatsApp, and Messenger (Live Chat).

  + This condition uses *Message Content* filters, where you can apply regex for more precise control over which messages trigger the rule. [Read more on using regex below.](#h_1e772f5d91)
* **Date Condition**: Triggers rules at specified dates and times. Multiple filters can create date ranges and combinations.
* **Bolt Agent Handoff Intent**: When using Bolt Agents, you can use this condition to trigger actions on a specific "message intent" or all messages **at the time of handoff**. For a comprehensive understanding of how Bolt Agent handoffs work, please review the [Bolt Agent Handoffs](https://help.element451.com/en/articles/8993398-bolt-agent-handoffs) article.
* **Moderation Flag Condition**: This condition allows you to automate specific actions when a conversation is flagged using our [Content Moderation](https://help.element451.com/en/articles/9859790-bolt-agent-content-moderation) tool.

## Actions

Actions are the tasks executed when an automation rule is triggered by its conditions being met. Actions allow the automation rule to take valuable measures in response to the conversation.

### Action Types

There are **seven** types of **actions** to choose from, and you can combine multiple types to accomplish more complex automation.

#### 1. Assignment

* Assign an individual or a Team to the conversation
* Assignment is a single action and will **only be executed by the first matching condition that the conversation meets**
* You can select the "**Contact Assignee**" token as the value for the Assigned To field, which dynamically assigns the conversation to the staff member assigned to the contact

  + A fallback assignment option is available to designate a specific user or team when the contact does not have an assignee or is an anonymous participant.
* You can also select a **Network Role** token as the value, which dynamically assigns the conversation to the internal user who holds that role for the contact—for example, their Academic Advisor or Financial Aid Counselor. Learn more in [Network: Connect Contacts with Internal Users](https://help.element451.com/en/articles/9884014-network-connect-contacts-with-internal-users).
* Conversations are only allowed one assignee

#### 2. Assignment and Mark as Private

* Assign an individual or a team to the conversation and mark it as private
* The same dynamic assignment tokens—**Contact Assignee** and **Network Role**—are available for this action.

#### 3. Add Participants

* Add internal users to a conversation

#### **4. Tag**

* Add a custom tag to a conversation for filtering

#### 5. Close

* Automatically close/end the conversation
* Close is a single action and will **only be executed by the first matching condition that the conversation meets**

#### 6. Reply

Send an automatic message reply

#### **7. Run Workflow Rule**

Executes a [workflow rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule)

---

# Using Regex in Message Content Filters

When creating Conversation Rules, the **Inbound Condition** type includes a **Message Content** filter under “Common Conditions.” This lets you evaluate incoming messages using operators like “contains,” “does not contain,” or “exists.” By using regex (regular expressions), you can make these filters more precise to avoid unintended rule actions.

For example, you might create a rule to auto-close conversations when a contact replies with “stop.” However, using “contains” with the word “stop” could unintentionally close conversations with messages like:

* *“Can I stop attending for one term?”*
* *“When can I stop by for a tour?”*

Regex allows you to refine this rule by matching only specific scenarios, such as messages that start with “stop” or contain it as a standalone word. This ensures the rule only applies to relevant messages and prevents false positives.

## How to Use Regex in Message Content Conditions

1. **Add a New Rule**

   * Navigate to *Engagement > Conversations > Settings > General > Automation Settings* and click **Add Rule**.
2. **Select the Inbound Condition Type**

   * Under **Conditions**, choose **Inbound Condition,** and set the **Message Content** filter under “Common Conditions.”
3. **Enter Your Regex in the “Value” Field**

   * Use the **contains** operator and input your regex pattern to match the desired message structure. We provide several [examples of regex patterns in the next section](#h_34a9a14e74).
4. **Save + Test**

   * Before activating a rule with regex, test it to ensure it works as expected. Try different phrases that should and should not trigger the rule. For example, if you used `^stop` as the value, the results should be:

     + *“Can I stop by for a tour?”* (Should NOT trigger)
     + *“Stop texting me.”* (Should trigger)

## Examples of Regex Patterns

|  |  |  |
| --- | --- | --- |
| **Pattern Type** | **Regex Syntax** | **Explanation + Examples** |
| **Starts With** | ^stop | Matches messages that begin with the word “stop.”    ✅ *“Stop sending me texts”*  ❌ *“Can I stop by for a tour”* |
| **Ends With** | stop$ | Matches messages that end with the word “stop.”    ✅ *“Please stop”*  ❌ *“Stop sending me texts”* |
| **Exact Match** | ^stop$ | Matches messages that contain only the word “stop.”    ✅ *“Stop”*  ❌ *“Stop texting”* |
| **Contains**  ​**Whole Word** | \bstop\b | Matches “stop” as a standalone word, not part of another word.    ✅ *“Please stop”*  ❌ *“Stopwatch”* |

---

# Managing Rules

To manage your rules, navigate to **Engagement** > **Conversations** > **Settings** > **General** > **Automation** **Settings.**

## Edit or Delete a Rule

To edit or delete a rule, click on the three dots to the far right of the rule.  
​

[![](https://downloads.intercomcdn.com/i/o/860089503/14c55d51cf14ca42cdd08a83/Convo+Rules+-+Edit+or+Delete.png?expires=1784332800&signature=39ff315f75de847d21d79b973f8e375223b5d39747ee76024f90dc8b5b982675&req=fCYnFsF3mIFcFb4V1XW4gYCRFhRRbQxn3WDjzmFRP%2B%2FHyvKP5%2FzdxD2DayRX%0AQIW0BtgVy5EHwddIOg6NEIU4ww%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860089503/14c55d51cf14ca42cdd08a83/Convo+Rules+-+Edit+or+Delete.png?expires=1784332800&signature=39ff315f75de847d21d79b973f8e375223b5d39747ee76024f90dc8b5b982675&req=fCYnFsF3mIFcFb4V1XW4gYCRFhRRbQxn3WDjzmFRP%2B%2FHyvKP5%2FzdxD2DayRX%0AQIW0BtgVy5EHwddIOg6NEIU4ww%3D%3D%0A)

## **Reorder Rules**

A new inbound conversation is executed against **all rules** based on their order in your list of rules in the Automation Settings section of Conversation Settings. To reorder the rules, use the two horizontal lines to drag rules up or down.  
​

[![](https://downloads.intercomcdn.com/i/o/860089660/5312eaeccc4f20db4888a460/Convo+Rules+-+Reorder.png?expires=1784332800&signature=f94c6976b518e3720bce1862de2b16f892dd5b1dcd6b454e5e3555fea26172a6&req=fCYnFsF3m4dfFb4V1XW4gX8Ufj12SfiQHPfO9444tL9bPWO9S4HjD%2FjtTtM8%0AhcgDl9yCjG4t0%2B87%2B6fwXOuqYQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860089660/5312eaeccc4f20db4888a460/Convo+Rules+-+Reorder.png?expires=1784332800&signature=f94c6976b518e3720bce1862de2b16f892dd5b1dcd6b454e5e3555fea26172a6&req=fCYnFsF3m4dfFb4V1XW4gX8Ufj12SfiQHPfO9444tL9bPWO9S4HjD%2FjtTtM8%0AhcgDl9yCjG4t0%2B87%2B6fwXOuqYQ%3D%3D%0A)

## Enabling/Disabling Rules

The enabled button should be turned on for active rules or turned off for unused ones.  
​

[![](https://downloads.intercomcdn.com/i/o/860092968/78a9b295a083ff35a5218d91/Convos+-+Enabled+and+Disabled.png?expires=1784332800&signature=1c670ac1b652e0fa4405cf3a39843354263000faebeb84335f491fa699b7a6f6&req=fCYnFsB8lIdXFb4V1XW4gbiMVB2NzRTscLL%2BHW5CIrkyyoqik5QZKS2SfHxA%0ArlGSU1X09owCfXxZjK6n5mqqBA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860092968/78a9b295a083ff35a5218d91/Convos+-+Enabled+and+Disabled.png?expires=1784332800&signature=1c670ac1b652e0fa4405cf3a39843354263000faebeb84335f491fa699b7a6f6&req=fCYnFsB8lIdXFb4V1XW4gbiMVB2NzRTscLL%2BHW5CIrkyyoqik5QZKS2SfHxA%0ArlGSU1X09owCfXxZjK6n5mqqBA%3D%3D%0A)

---

# Use Cases

Here are some ways that our partner institutions are using conversation rules:

* Assign a conversation to an admissions counselor
* Route conversations to the contact's assigned staff member using the 'Contact Assignee' assignment option
* Send an automatic reply when the office is closed for holidays
* Send an automatic reply during nights and weekends
* Assign a conversation or add a participant based on the intent of the conversation (e.g., financial aid or account balance)

​

---