---
title: 📌 Conversations: Frequently Asked Questions
url: https://help.element451.com/en/articles/10604714-conversations-frequently-asked-questions
collection: Conversations
---

This article answers commonly asked questions about Conversations, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389494835/75d14a54d301bc4a14ca8d26a269/Pardon+our+Progress.png?expires=1784333700&signature=d2f209222b0b6ae55d1df495f297d2a438ae2b9501147fc0e0f17140c6e336b7&req=dSMvH813mYlcXPMW1HO4zckdFCjJhC3Hejdd5z8rep9aUR0UA0XyrFmT6F7e%0AG7OD2XwthG%2BhqpG5xzg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389494835/75d14a54d301bc4a14ca8d26a269/Pardon+our+Progress.png?expires=1784333700&signature=d2f209222b0b6ae55d1df495f297d2a438ae2b9501147fc0e0f17140c6e336b7&req=dSMvH813mYlcXPMW1HO4zckdFCjJhC3Hejdd5z8rep9aUR0UA0XyrFmT6F7e%0AG7OD2XwthG%2BhqpG5xzg%3D%0A)

# Conversations Inbox + Management

#### Why are some emails not being forwarded to my connected inbox?

The most common reason emails from your connected email address do not appear in Element451 is that **Anonymous Conversations is disabled.**   
​  
When an email is forwarded to Element451, the system checks the **Anonymous Conversations** setting. If this setting is **disabled** and the sender’s email address **does not match an existing contact record**, the email is blocked and will not appear in your inbox. This is likely why some emails seem to be missing.  
​  
To resolve this, **enable Anonymous Conversations** by navigating to **Engagement** > **Conversations** > **Conversations Settings > Email.**  
​  
Once enabled, emails from **unknown senders** (including new email addresses and phone numbers) will be allowed into your inbox.  
​  
​[Explore More: Troubleshooting Connected Inboxes + Email Forwarding](https://help.element451.com/en/articles/8663239-email-inbox-and-forwarding-and-troubleshooting)

#### What does the smiley face displayed by inbound messages mean?

Element451 Conversations uses artificial intelligence (AI) powered [sentiment analysis](https://help.element451.com/en/articles/8267878-sentiment-analysis) to help you better understand how students feel during conversations.

#### Can I segment contacts by conversation tags?

No, the People module does not have a filter for segmenting contacts by conversation tags. However, you can use the conversation tag filter in the Conversations module to refine your inbox view.

#### Why is a message pre-populating when I start a new conversation?

You might notice that when you start a new conversation, the message field auto-populates with text from a previous conversation, sometimes addressing the wrong person. This can seem like a bug, but it’s actually related to how **drafts are saved in the Conversations module**.

Conversation drafts are saved based on your internal user session, not the specific contact you were messaging. This means if you start typing a message and don’t send it (close out of the sidesheet), the text remains saved as a draft. When you navigate away from that conversation—maybe to view another profile or a different part of the platform—and then open a new conversation, the draft you created earlier sticks and auto-fills in the message field.

**Example Scenario:**

1. You start a conversation with **Jane** and type, “Hi Jane, just checking in…”
2. You navigate away before sending the message—maybe to look at another profile or access a different part of the platform.
3. When you open a new conversation with **John**, the message field still shows “Hi Jane, just checking in…”

This happens because the message draft was never cleared or sent—it remained tied to your user session. To prevent this from happening, if you don't plan to send a message you've drafted, clear the message before navigating away.

#### Can I bulk reassign conversations in Element451 (e.g., an employee is leaving)?

Currently, there isn’t a direct bulk reassignment feature for conversations. However, you can:

* **Use [Conversation Rules](https://help.element451.com/en/articles/1930478-conversation-rules):** Assign **new** **inbound** **conversations** (action) from contacts that are assigned to the former employee (segment condition) to another employee.
* **Reassign individually:** Manually update assignees for existing conversations on an individual basis.

#### Can I disable Sentiment Analysis for Conversations?

Sentiment analysis is automatically applied to conversations and is always on. There is no setting to disable this behavior.

#### Can I automatically assign conversations to a contact's assigned staff member?

Yes. When creating a [conversation rule](https://help.element451.com/en/articles/1930478-conversation-rules) with an Assignment action, select the **Contact Assignee** token. This dynamically routes the conversation to the internal user assigned to the contact. You can also configure a fallback for contacts without an assignee.

#### What does it mean when a conversation shows "[Contact Name] started a conversation as a reply to [Link]?

This indicates the conversation was started when the contact replied to an Email or SMS campaign. The campaign name is a clickable link—click it to open the campaign directly and see what message the student received before reaching out.

#### Will I see campaign messages in the conversation thread?

Only when a student replies to a campaign does the originating campaign get noted at the top of the thread. The thread doesn't display every campaign message sent to that contact—just the context for how this specific conversation started.

---

# Conversation Channels

## SMS

#### How many characters should my SMS (text) be?

SMS messages are limited to 1600 characters. However, best practice is to keep messages much shorter than that. We recommend 160 characters for the best technical and end-user experience.

#### An international student did not receive an attachment on my SMS.

If you send a message with multimedia content (images or attachments), it will only be delivered to US numbers.

#### Why didn’t we receive a student’s text message?

By default, Element451 only allows inbound texts from **known senders** (contacts with a record in the People module) to appear in Conversations. This helps prevent spam.

If you didn’t receive a message, check:

* Whether the sender’s phone number is linked to a contact in the **People module**.
* If **Anonymous Conversations** is enabled in your settings. This allows messages from all senders, even if they aren’t in your system.

#### Can we send SMS messages to international phone numbers?

There is not broad support for delivery of for SMS messages sent from Element451 to non-US numbers.

As part of your onboarding, you’ll complete A2P 10DLC registration to authorize your US-based, SMS phone numbers to send messages to verified, SMS-capable US numbers.

While this registration does not apply to Canadian numbers, many Canadian carriers will still deliver SMS messages from US-based numbers that share the +1 country code.

For international numbers outside the US and Canada, Element451 will attempt delivery until we receive a hard bounce. Due to varying carrier rules and local regulations worldwide, international SMS delivery should be considered the exception rather than the rule. Some countries and international carriers will also not pass inbound messages to the Element451 SMS system based in the US so receiving text messages may be further limited from some countries.

## Email

#### Why Do Emails from Conversations Have a Unique Reply Address?

When you send an email through the Conversations module, the reply-to address includes a unique identifier (e.g., [67b77502924d3@element451.io](mailto:67b77502924d3@element451.io)). **This identifier ties the email to a specific conversation thread**.

This allows a student's reply to be automatically routed back into the correct thread in your Conversations inbox. While the reply address may look different from a standard email, it functions the same way.

💡**Pro Tip:** Configure a clear and trusted **“From Name”** in your **Email Settings** (Conversations Settings > General > Inboxes). This display name is what students will see in their email provider’s inbox, helping them recognize who the email is from at a glance. For example, instead of seeing a reply address like [67b77502924d3@element451.io](mailto:67b77502924d3@element451.io), they’ll see something like: **From:** Admissions Team <[67b77502924d3@element451.io](mailto:67b77502924d3@element451.io)>.

#### I want to send an email immediately. How can I do this?

You have two options, depending on your goal:

1. **Conversations:** Use this to email a single contact.
2. **Campaigns (One-Time):** Use this to send the same email to multiple contacts within a segment.

Both options allow you to send an email right away based on your needs.

#### When using a connected inbox, does Element451 store emails that are not otherwise shown Conversations?

Yes. While not accessible to users, email content and metadata for unmatched conversation emails is stored in Element451's inbound logs for 90 days. These emails may not be able to be matched and displayed because:

* Partner instance (subdomain) can't be identified
* Contact cannot be identified and the inbox does not accept anonymous email messages.
* Target inbox is inactive
* Inbound message is from an email address that we recognize as an admin user and that message would start a new conversation/thread

## Messenger (Live Chat)

#### When students enter their email in live chat, are their conversations automatically linked to their records?

No, the association is **not automatic**. When a student enters their **email address and name** in live chat, Element451 checks for an existing record. If a match is found, an **“Associate”** button appears in the **Profile** tab of the conversation. A user must manually confirm the association by clicking this button.

Alternatively, you can **manually search** for a user and associate the conversation with their record.

#### Can I turn off advanced voice mode in live chat/messenger?

Yes, if you wish to disable advanced voice mode in Messenger, you can turn it off in Messenger settings (Conversations > Settings > Messenger).

## Phone

#### How should I format phone numbers for call forwarding, and how does it work?

To set up call forwarding in Element451, enter the phone number with the **”+1”** prefix (e.g., **+13852485526**). Call forwarding only applies to **incoming calls**—when someone dials your Element451 number, the call will be forwarded to your designated number.

**Important Notes on In-App Calling:**

* **Caller ID Customization:** You can verify and connect additional phone numbers (e.g., your admissions office main line) to display as your **Caller ID** when making outbound calls. This ensures students see a familiar number when you call.
* **No Inbound Call Support:** Element451 does not support inbound calls directly. If a student tries to call back, they’ll reach the number displayed as your Caller ID, such as your main office line.
* **Verification Required:** Before using a custom number for Caller ID, you must **verify** it in Element451.

For more details, visit our help article: [In-App Calling + Phone Setup](https://help.element451.com/en/articles/8400679-in-app-calling-phone).

#### Can I make international calls with Element451's In-App Calling?

No. Outbound In-App calling supports calls to the United States and US Territories. While calls to Canadian numbers, may connect they are not officially supported via in-app calling. There is no support for calls to other international locations.

#### How do I stop FaceTime from interfering with in-app calls on a Mac?

If you use a Mac computer and FaceTime intercepts your in-app calls, you can change your default calling app, disable FaceTime, or adjust your browser settings.

**Option 1: Change the Default Calling App**

1. Open the **FaceTime** app.
2. Click **FaceTime** in the **menu bar** and select **Preferences**.
3. Go to the **Settings** tab.
4. Find **Default for calls** and select the **drop-down menu**.
5. Choose the app you want to use as your **default calling app**.
6. Close the **Preferences** window.

**Option 2: Adjust Browser Settings (Chrome & Safari)**

Your browser may be set to open call links with FaceTime. To change this:

* **For Chrome:**

  1. Open **Chrome** and enter chrome://settings/handlers in the address bar.
  2. Look for **FaceTime** under “Protocols.”
  3. Click **Remove** or select your preferred calling app.
* **For Safari:**

  1. Open **Safari** and go to **Preferences > Websites > Phone Number Handling**.
  2. Change the setting from **FaceTime** to your preferred app.

**Option 3: Turn Off FaceTime**

If you don’t need FaceTime on your Mac, you can **disable it** to prevent conflicts:

1. Open the **FaceTime** app.
2. Click **FaceTime** in the menu bar.
3. Select **Turn FaceTime Off**.

---

# Notifications

#### Can I turn off the notification emails for new messages?

Unfortunately, this cannot be turned off at this time. While the notification feature ensures you don't miss a conversation, we understand your inbox can get crowded. Consider leveraging your email provider's rules or filters to organize your notifications. For more information on configuring rules and filters, visit your email provider's help center ([Outlook Rules](https://support.microsoft.com/en-us/office/manage-email-messages-by-using-rules-c24f5dea-9465-4df4-ad17-a50704d66c59) | [Gmail Filters](https://support.google.com/mail/answer/6579?hl=en)).

---

# Rules

#### Why is my conversation automation rule not running?

To troubleshoot why your rule didn't run, it is helpful first to remember the process by which rules are applied and run:

Conversation rules are triggered on two occasions:

1. **Inbound** **messages** **with** **no conversation history**
2. **New messages in closed conversations**

When troubleshooting rule execution, there are a few things to consider:

* **Close Conversations**: Close conversations once they end so subsequent messages will be triggered for rule evaluation.
* **Review Rule Order**: Conversations are compared against your list of rules in the order in which the rules are listed, starting from the top. When it finds a rule that matches the incoming message, it applies that rule. After applying a rule, it stops checking the rest. Only the **first matching rule is applied**, and the rest are ignored for that particular message.   
  ​  
  ​[Explore more on conversation rules](https://help.element451.com/en/articles/1930478-conversation-rules).

​

---