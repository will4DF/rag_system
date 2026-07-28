---
title: Event Messaging and Notifications
url: https://help.element451.com/en/articles/1524108-event-messaging-and-notifications
collection: Events
---

Enhance attendee engagement with customized email and SMS event confirmations to follow-ups, plus learn how to set up admin notifications.

# Overview

Keeping in touch before and after an event is a great way to keep people engaged. With Events, you can send various email and SMS messages to people who have registered for an event, such as a confirmation after registering or a reminder before the event. You can also send thank you messages to attendees or messages about similar events to people who registered but didn't attend or canceled their registration. Messages can be sent instantly or scheduled to be sent in the future.

Each event will have a couple of messages to give you a head start. On this page, we'll review how to edit and manage them. We'll also explain how to create new messages and send them to attendees based on their status, e.g., attended or canceled.

**Note:** Attendees marked as **Canceled** will not receive messages targeted to **Registered** attendees. Only attendees with a **Registered** status are eligible to receive event messages. If a canceled attendee is later re-registered, they will resume receiving these communications.

## Accessing Event Messages and Notification Settings

1. Navigate to **Engagement** > **Events** > **All** **Events**.
2. Click on the event's name or the **pencil** icon to open the editor.
3. Click on the **Signups** tab.
4. Click **Messages** from the left-hand menu.

[![](https://downloads.intercomcdn.com/i/o/999918539/e194a0ef1ac589fc34816a3f/Events+-+Accessing+Messages.png?expires=1784333700&signature=f6139f7dfa833cb7546480afe63e8553f31e9bd1f8631db7b8cbc7408fdbdde9&req=fSkuH8h2mIJWFb4f3HP0gJuEQxA79NkHMmSafAjLyRmC7WuFY7pkMdIMsPEg%0AF2ifD4%2FrxLz%2FK2gkUQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/999918539/e194a0ef1ac589fc34816a3f/Events+-+Accessing+Messages.png?expires=1784333700&signature=f6139f7dfa833cb7546480afe63e8553f31e9bd1f8631db7b8cbc7408fdbdde9&req=fSkuH8h2mIJWFb4f3HP0gJuEQxA79NkHMmSafAjLyRmC7WuFY7pkMdIMsPEg%0AF2ifD4%2FrxLz%2FK2gkUQ%3D%3D%0A)

---

# Default System Messages

All events have two standard email message templates branded to your institution that can be customized—the ***Event Registration Confirmation*** and the ***Event Reminder***.

|  |  |
| --- | --- |
| **Autoresponder** | **Details** |
| **Event Registration**  ​**Confirmation** | Sent immediately after someone registers for an event using email and SMS channels, as long as the email address and phone number are collected on the signup form.    **Exception: Events with Payments**  If your event requires payment and you allow registration without payment (pay later), the attendee will receive the confirmation once the payment has been received.    If your event has payments enabled, be sure to review the [section at the end of this article](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_25f0ab471d) on messages for events with payments. |
| **Event Reminder** | This message is sent via email and SMS 24 hours before the event starts, as long as the email address and phone number are collected on the signup form. |

**Important Notes about Template Messages**

* The two customizable template messages, *Event Registration Confirmation* and *Event Reminder*, can be edited but not deleted. Therefore, if you don't want to use them, use the **Active** toggle switch to deactivate them and prevent them from being used.
* These two emails **automatically** contain .ics attachments, allowing your attendees to quickly open the attachment and add the event to their calendar. For custom messages, you can add a [calendar token](https://help.element451.com/en/articles/6067308-tokens-for-events-messages) to provide a link to add the event to their calendar.

## How To: Previewing Template Messages

[![](https://downloads.intercomcdn.com/i/o/833463150/3f10f00b820ba7b4e9d63185/Preview+Event+Message+templates.png?expires=1784333700&signature=900e343e17e9e5cede219329b65f51ae63d9cf7a4810ada8b0d025adea535872&req=fCMkEs99nIRfFb4f3HP0gDjm09beOHfb65CrQ20FQcGW%2F4xzYeeEkC6WvC2c%0AwWr%2F7oWAAZF835Mfvw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/833463150/3f10f00b820ba7b4e9d63185/Preview+Event+Message+templates.png?expires=1784333700&signature=900e343e17e9e5cede219329b65f51ae63d9cf7a4810ada8b0d025adea535872&req=fCMkEs99nIRfFb4f3HP0gDjm09beOHfb65CrQ20FQcGW%2F4xzYeeEkC6WvC2c%0AwWr%2F7oWAAZF835Mfvw%3D%3D%0A)

If you want to preview what the template messages look like, or you want to take a look before editing them, there are two options to preview the message:

* **Option 1**: Preview the Message from the Editor

  1. Navigate to **Engagement** > **Events** > **All** **Events**.
  2. Click on the event's name or the **pencil** icon to open the editor.
  3. Click on the **Signups** tab.
  4. Click the **Messages** sub-tab from the left-hand menu.
  5. Locate the message you wish to preview.
  6. Click the **pencil** icon.
  7. Click the **Preview Message** button.

* **Option 2**: Preview the Message by Sending a Test

  1. Navigate to **Engagement** > **Events** > **All** **Events**.
  2. Click on the event's name or the **pencil** icon to open the editor.
  3. Click on the **Signups** tab.
  4. Click the **Messages** sub-tab from the left-hand menu.
  5. Locate the message you wish to preview.
  6. Click the **stamp** icon.
  7. Select which channel(s) you'd like to preview.
  8. Based on your channel selection, input the email, cell phone number, or both to which you wish to send the preview.

## How To: Editing Template Messages

[![](https://downloads.intercomcdn.com/i/o/833463150/3f10f00b820ba7b4e9d63185/Preview+Event+Message+templates.png?expires=1784333700&signature=900e343e17e9e5cede219329b65f51ae63d9cf7a4810ada8b0d025adea535872&req=fCMkEs99nIRfFb4f3HP0gDjm09beOHfb65CrQ20FQcGW%2F4xzYeeEkC6WvC2c%0AwWr%2F7oWAAZF835Mfvw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/833463150/3f10f00b820ba7b4e9d63185/Preview+Event+Message+templates.png?expires=1784333700&signature=900e343e17e9e5cede219329b65f51ae63d9cf7a4810ada8b0d025adea535872&req=fCMkEs99nIRfFb4f3HP0gDjm09beOHfb65CrQ20FQcGW%2F4xzYeeEkC6WvC2c%0AwWr%2F7oWAAZF835Mfvw%3D%3D%0A)

1. Navigate to **Engagement** > **Events** > **All** **Events**.
2. Click on the event's name or the **pencil** icon to open the editor.
3. Click on the **Signups** tab.
4. Click the **Messages** sub-tab from the left-hand menu.
5. Locate the message you wish to edit.
6. Click the **pencil** icon.
7. Click the **Edit Message** button.
8. A dialogue box will open, allowing you to modify the message content and settings. ![](https://downloads.intercomcdn.com/i/o/1124967671/9906709174fd3a4aeeffddb7/Note.png?expires=1784430000&signature=ec54b71782b2dbcb58d715386d915233abaabe098b47e7c5bcd08ed7494c58d4&req=dSElEsB4modYWPMW3Hu4gXM5lyViBziMrVyjpx42IjbKlLmConlkSxu1zg4c%0AeA%3D%3D%0A) When editing the message content section of the email message, you will notice two different options for editing: *Legacy* and *Email* *Builder*. The legacy option is an older editor that we no longer support. We recommend using the Email Builder, which allows you to edit the template using the same technology used in our Campaigns builder. We cover this feature in more detail [below](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_68898485a3).

---

# Custom Event Messages

![](https://downloads.intercomcdn.com/i/o/996594732/153c814875896d575b1ff902/Important+-+Orng.png?expires=1784430000&signature=093273980d219634fd6725afc2cbd75a81adc9da17cc7f82e09bfe5c4cfdc387&req=fSkhE8B6moJdFb4X1HO4gZB8E976a%2BTg5D9FVBTRHM4wUGQF%2BR6LZoUeAyqE%0A) If an attendee registers for an event **after** **a scheduled reminder** **has been sent**, they **will not** receive that message. For example, if an event starts tomorrow at 9 AM and a reminder is set to go out one day before, anyone who registers after 9 AM today will miss that reminder. Make sure to plan your messages so all attendees are updated!

## Send Options

When setting up custom event messages, you have three timing options: Immediately, After the Event, and Before the Event. Here’s what each means and how to use them:

* **Immediately**: Send your message as soon as it's created. If your event has multiple dates, decide whether to send it for one, several, or all occurrences.
* **After the Event**: Schedule your message to send after the event has ended. You must specify how many days after the event it should be sent.
* **Before the Event**: Schedule your message to send before the event starts. You must specify how many days before the event it should be sent.

## Creating + Sending Custom Event Message

### Step 1: New Message

1. Navigate to **Engagement** > **Events** > **All** **Events**.
2. Click on the event's name or the **pencil** icon to open the editor.
3. Click on the **Signups** tab.
4. Click the **Messages** subtab from the left-hand menu.
5. Under Sent Messages, click the **New** **Message** button.
6. The *new message form* will open for you to configure the settings:

   * **Send**: Select when to send your custom message: immediately, after, or before the event. For a definition of each, view [Send Options](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_77bc1bd51a) above.
   * **Status**: Limit the audience by selecting which status should receive your message.

     + When sending to attendees with the *Registered* status, anyone marked as *Canceled* will automatically be excluded. If an attendee is re-registered, they’ll be eligible to receive messages again.
   * **Message** **Name**: This is how your message will be saved in your event message list. This is for internal reference only.
   * **Custom**: Choose from a list of pre-made messages, or select **Custom** to create your own.

### Step 2: Edit Message

Once you have customized the settings, you can edit the message.

1. If creating a custom message without a pre-made message, click the **Edit** **Message** button to open the editor. If you select a pre-made message, the editor should open automatically.
2. Channels: Select whether to send your message via email, SMS, or both. By default, both options are checked. Selecting both options allows you to navigate between editing each message using the tabs.

   [![](https://downloads.intercomcdn.com/i/o/999943973/60b89973e360246c6e88f4ba/Events+-+Custom+Message+-+Channel+Tabs.png?expires=1784333700&signature=8f21ff1bcc9ae7a25c2df9c09366f304722c2394872ff4705ddcaf8322df10af&req=fSkuH819lIZcFb4f3HP0gPXrUpIzEIrdybgjsLS1jUZqP%2FmtLQJZ2KWmOI8A%0AXx4%3D%0A)](https://downloads.intercomcdn.com/i/o/999943973/60b89973e360246c6e88f4ba/Events+-+Custom+Message+-+Channel+Tabs.png?expires=1784333700&signature=8f21ff1bcc9ae7a25c2df9c09366f304722c2394872ff4705ddcaf8322df10af&req=fSkuH819lIZcFb4f3HP0gPXrUpIzEIrdybgjsLS1jUZqP%2FmtLQJZ2KWmOI8A%0AXx4%3D%0A)

   * **If sending an email,** enter the subject line for your email along with your sender information: name and email address. You can enter a separate reply email or use the sender's address.
   * **If sending an SMS**, enter the phone number from which the message will come. Enter the body content of your text message.
3. Add or edit the message content:

   * ![](https://downloads.intercomcdn.com/i/o/1124967671/9906709174fd3a4aeeffddb7/Note.png?expires=1784430000&signature=ec54b71782b2dbcb58d715386d915233abaabe098b47e7c5bcd08ed7494c58d4&req=dSElEsB4modYWPMW3Hu4gXM5lyViBziMrVyjpx42IjbKlLmConlkSxu1zg4c%0AeA%3D%3D%0A) When editing the message content section of the email message, you will notice two different options for editing: *Legacy* and *Email* *Builder*. The legacy option is an older editor that we no longer support. We recommend using the Email Builder, which allows you to edit the template using the same technology used in our Campaigns builder. We cover this feature in more detail [below](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_68898485a3).
   * ![](https://downloads.intercomcdn.com/i/o/999950574/6d84b615b97e387f8e5ea3ec/Pro+Tip+-+Orng.png?expires=1784430000&signature=c18e7cc499295c7e80ae75104b246046aaa7dce3ca8f62e4afa029a8afa40a3d&req=fSkuH8x%2BmIZbFb4X1HO4geghNWwHDGswSlK3IxLvBQA%2BX%2BhjkZEcqPp13uwf%0A) Use Tokens to personalize your message. For example, Dear [user:user-first-name]. You can also include a link to their personal registration page: [event:registration\_update\_url]. Additional information on tokens is provided at the [end of this article](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_0da9874eb3).
4. After editing your message, click **Done** to close the message editor and return to the *new message form*.
5. Click **Preview** **Message** to preview the message to ensure it looks as expected.

   * ![](https://downloads.intercomcdn.com/i/o/999944679/6ccc8a91f6cc1da9ff153c7e/Important+-+Orng.png?expires=1784430000&signature=f06b9b394427e8249eada771f38a47c467468d175340f7e0f9ea66e33f264c0a&req=fSkuH816m4ZWFb4X1HO4gU6hgwCpUxBJMiaMRh9r9ZK6jBtPVMclkVqSeOwi%0A) If you send an immediate message, the message will be sent as soon as you click **Done**. Therefore, be sure to preview your message before clicking Done.
6. When you're ready, click **Done** to send your message (immediate messages) or save (before- and after-event messages).
7. For messages sent **before** or **after** an event, use the **active** toggle to activate the message to send when an attendee meets the date condition. This control is also accessible from the main message page.

---

# Editing & Deleting a Custom Event Message

1. Navigate to **Engagement** > **Events** > **All** **Events**.
2. Click on the event's name or the **pencil** icon to open the editor.
3. Click on the **Signups** tab.
4. Click **Messages** from the left-hand menu.
5. Follow the steps below based on your desired action:

## How To: Deleting a Custom Event Message

1. Click the **trash** **can** icon next to the message you wish to delete.
2. Confirm the permanent deletion by clicking **Yes**.

## How To: Editing a Custom Event Message

1. Click the **pencil (edit)** icon next to the message you wish to edit.
2. Follow the [same steps outlined here](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_c802963eb1) as if you were creating a new message.

---

# Using the Email Builder for Event Messages

When editing the message content section of an email message (template or custom), you will notice two different options for editing: *Legacy* and *Email* *Builder*. The legacy option is an older editor that we no longer support. We recommend using the Email Builder, which allows you to edit the template using the same technology used in our Campaigns builder.  
​

[![](https://downloads.intercomcdn.com/i/o/1124969426/3b9f7b3c611659e541c1c863/event+auto+responder+screenshot+copy.png?expires=1784333700&signature=18f57f5201b3c2e6daa8c7c9edcc1ef7876e1a6cd629e5749e947ecda31a9e8f&req=dSElEsB4lIVdX%2FMW1HO4zV%2FlvZJkgBslfU5uNU4dfifRleLvDSCDhONIIY7t%0AQ7ErjTPPE4HWoFHPPH0%3D%0A)](https://downloads.intercomcdn.com/i/o/1124969426/3b9f7b3c611659e541c1c863/event+auto+responder+screenshot+copy.png?expires=1784333700&signature=18f57f5201b3c2e6daa8c7c9edcc1ef7876e1a6cd629e5749e947ecda31a9e8f&req=dSElEsB4lIVdX%2FMW1HO4zV%2FlvZJkgBslfU5uNU4dfifRleLvDSCDhONIIY7t%0AQ7ErjTPPE4HWoFHPPH0%3D%0A)

## Navigating the Email Builder

![](https://downloads.intercomcdn.com/i/o/1124982893/33d9d02d5eda02a6e4baa174/Pro+Tip.png?expires=1784430000&signature=367243d34e0bd639b0b53ccb0596ce623151329295c7e30a55c3129b696261eb&req=dSElEsB2n4lWWvMW3Hu4gcYw933HiUIWtZhG3wb8eFjm7O37N88FiwoEc4tt%0A7g%3D%3D%0A) We recommend using the full-screen feature to edit your campaign. Click the double-sided arrow icon to enter and exit full-screen mode.  
​

[![](https://downloads.intercomcdn.com/i/o/1124983111/3b6279cf1b1ede6f0f96c4c9/Screenshot+2023-12-16+at+3_46_39%E2%80%AFPM+%281%29.png?expires=1784333700&signature=66183653d839dc882fb07c105faea752c0e36dcf994975b1c1ab5ce4e7bb403f&req=dSElEsB2noBeWPMW1HO4zagGk9Z5nFAbIFIgrpPARojPszHa58qLDTkWATUR%0AgxPYq5FpDk4E%2FSysdAI%3D%0A)](https://downloads.intercomcdn.com/i/o/1124983111/3b6279cf1b1ede6f0f96c4c9/Screenshot+2023-12-16+at+3_46_39%E2%80%AFPM+%281%29.png?expires=1784333700&signature=66183653d839dc882fb07c105faea752c0e36dcf994975b1c1ab5ce4e7bb403f&req=dSElEsB2noBeWPMW1HO4zagGk9Z5nFAbIFIgrpPARojPszHa58qLDTkWATUR%0AgxPYq5FpDk4E%2FSysdAI%3D%0A)

* **Add Content Blocks + Elements:** Click the **+** sign in the top left corner to open the list of Content Blocks available to add. This allows you to select any of our prebuilt blocks to add and customize.

  + You can add the following Blocks: [Custom Components](https://help.element451.com/en/articles/1513676-creating-an-email-campaign#h_824b3aa5ba), *Row*, *Separator*, *Dividers*, *Alerts*, *Header*, *Bodies*, *CTA*, *Lists*, *Quotes*, *Signatures*, and *Footer*.
  + When you add a Row, you have the option to add individual elements such as a Text Block, Image Block, Button Block, HTML Block, Video Block, AI Text Prompt Block, and Ruler. Read more about these elements in our [Campaigns article](https://help.element451.com/en/articles/1513676-creating-an-email-campaign#h_64422d90a2).
* **Text Editing**:

  + Highlight the text within your message content to access the formatting toolbar.
  + Utilize ![](https://downloads.intercomcdn.com/i/o/1124995120/4b513e2bca643f724ac703fc/BoltAI.png?expires=1784430000&signature=501ecc80f2b6312567e8e85a6afb11b19144d7b288578d4bd7a40a885b6766ab&req=dSElEsB3mIBdWfMW3Hu4gVqttAl%2F04OBhfnMkstdYhqd1wscCDAjUNHG4GYr%0Aig%3D%3D%0A)[BoltAI Writing Tools](https://help.element451.com/en/articles/8380026-boltai-writing-tools) and apply various formatting options to enhance your text.
* **Email Settings**:

  + Click the gear icon to edit the email background image, adjust transparency, and modify font settings.
* **Undo and Redo**:

  + Use the undo and redo arrow buttons to easily correct mistakes and refine your email during the editing process.
* **Copy HTML**:

  + Click the copy button to copy the HTML of your email to your clipboard.
* **Device Preview**:

  + Use the phone, tablet, and computer icons to preview how your email will render on each device.
* **Edit and Preview Tabs**:

  + Toggle between the Edit and Preview tabs in the top right corner of the email builder to switch between editing and previewing your email.

---

# Event Messages for Events with Payments

## Payment at Event Registration

Attendees who pay the event fee at the time of registration will receive all event messages as usual (confirmation, event reminder, and custom emails), just like events without payments.

## Payment Later + Registration Expiration

When an attendee’s registration is set to expire due to non-payment (configured in your [event payment settings](https://help.element451.com/en/articles/1520669-event-registration-form-payments#h_82e2f94125)), two notification emails may be sent to attendees who choose to “pay later.” Currently, these emails cannot be edited or customized.

* **Registration Received - Payment Needed**  
  This email is sent when an attendee opts not to pay the event fee at the time of registration. It is sent instead of the event confirmation email. If payment is made before the expiration date, the attendee will receive the event confirmation email immediately after payment. The event reminder email and any other custom event messages you have configured will be sent as scheduled.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1056779982/2757449d41a4a2cc35d4a0fa/Payment+Reminder+Autoresponder.png?expires=1784333700&signature=eaafdc35ddc070fb693e5d4e365efe66458d745b1cc6655250f528361ced0485&req=dSAiEM55lIhXW%2FMW1HO4zQzpnfMAL7LDQu0SUriB6zMtVJVGgenkRZa3mBo4%0A0hFm%0A)](https://downloads.intercomcdn.com/i/o/1056779982/2757449d41a4a2cc35d4a0fa/Payment+Reminder+Autoresponder.png?expires=1784333700&signature=eaafdc35ddc070fb693e5d4e365efe66458d745b1cc6655250f528361ced0485&req=dSAiEM55lIhXW%2FMW1HO4zQzpnfMAL7LDQu0SUriB6zMtVJVGgenkRZa3mBo4%0A0hFm%0A)

* **Registration Expired - Payment Not Received**   
  This email is sent when an attendee opts not to pay the event fee at the time of registration and fails to pay by the expiration date.

  [![](https://downloads.intercomcdn.com/i/o/1056780755/c9e05dc73497448c02509351/Event+Payment+Email+-+Expiration.png?expires=1784333700&signature=483be8cfb0e611cd84244985080ae06e39d21b68ee42891a1513ad40fd2b825d&req=dSAiEM52nYZaXPMW1HO4zVt2qlKtt8LMV65nuussGAo3zoXwKInQbxUxHfMb%0AhvVN%0A)](https://downloads.intercomcdn.com/i/o/1056780755/c9e05dc73497448c02509351/Event+Payment+Email+-+Expiration.png?expires=1784333700&signature=483be8cfb0e611cd84244985080ae06e39d21b68ee42891a1513ad40fd2b825d&req=dSAiEM52nYZaXPMW1HO4zVt2qlKtt8LMV65nuussGAo3zoXwKInQbxUxHfMb%0AhvVN%0A)

---

# Event Message Tokens

You can personalize your event messages using tokens. Additionally, you can include the token `[event:registration_update_url]` to provide a link to their personal registration page and tokens to provide links to add the event to their calendars.

To learn more about using these tokens and to see a complete list of available tokens, explore our article, [Tokens for Event Messages](https://help.element451.com/en/articles/6067308-tokens-for-events-messages).

---

# Internal User Notifications

When an attendee registers for an event, you can configure internal users to receive a notification email. The notification email includes registration information and links to quickly view the attendee's profile and all attendees for that event.

Here is a preview of how the notification email appears:

[![](https://downloads.intercomcdn.com/i/o/996613977/1e0aa7962a25559c7123dc49/Screenshot+2024-03-19+at+7_35_49%E2%80%AFPM.png?expires=1784333700&signature=8cee5c74d7b071b5484d546fdc870b709ec38e0c388ca136e933144e6d081469&req=fSkhEMh9lIZYFb4f3HP0gMywY2qTWXVw0KKYKIb%2B%2B6R9LTkAqvxjJjb7gfo9%0Aa6nF06Np%2B7vD%2BaoQNg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/996613977/1e0aa7962a25559c7123dc49/Screenshot+2024-03-19+at+7_35_49%E2%80%AFPM.png?expires=1784333700&signature=8cee5c74d7b071b5484d546fdc870b709ec38e0c388ca136e933144e6d081469&req=fSkhEMh9lIZYFb4f3HP0gMywY2qTWXVw0KKYKIb%2B%2B6R9LTkAqvxjJjb7gfo9%0Aa6nF06Np%2B7vD%2BaoQNg%3D%3D%0A)

## How To: Add Notification Email

1. Navigate to **Engagement** > **Events** > **All** **Events**.
2. Click on the event's name or the **pencil** icon to open the editor.
3. Click on the **Signups** tab.
4. Click the **Notifications** sub-tab from the left-hand menu.
5. Click **+ Add Email Address.**
6. Input the user's email address.
7. Repeat steps 5 and 6 for additional users that need to be notified.

---

⚠️ If you are creating an event, this concludes the series of articles reviewing general event creation and customization processes. Now, we recommend that you become familiar with [Managing Event Attendees](https://help.element451.com/en/articles/1520725-manage-the-attendee-list).

---