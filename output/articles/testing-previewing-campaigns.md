---
title: Testing + Previewing Campaigns
url: https://help.element451.com/en/articles/8901250-testing-previewing-campaigns
collection: Campaigns
---

Learn how to test your Campaign and preview your versions.

# Overview

Launching a Campaign with Element451 means creating personalized, targeted messages across multiple communication channels. To ensure each campaign reaches your audience effectively, we’ve developed tools to help you test and preview your content before it goes live.

Additionally, effective segment management is crucial for ensuring that your campaign reaches the intended audience and avoids errors. Always verify segment selections carefully before proceeding.

![](https://downloads.intercomcdn.com/i/o/1195029423/83945bfffdef2660ba833074/Important.png?expires=1784430000&signature=3281c770e0cc5b327b5ebe8d74b7d0cbbb245993050df8399d1a393f8297134b&req=dSEuE8l8lIVdWvMW3Hu4gSNzKEvXn%2FrBv3d0yieKo%2F11V1z0c52hTHfMjOkk%0AFA%3D%3D%0A) We recommend being familiar with how to create a segment of ***test*** users. If you wish to learn more about segments, [click here](https://help.element451.com/en/articles/1474208-creating-a-segment).

Following best practices such as verifying your segment selections and creating separate campaigns for testing versus final sending can prevent common errors.

## Test vs. Preview

**Test**: Allows you to send a real version of your Campaign to a designated email address, mobile number, or push notification. This step is crucial to get an accurate idea of how your message will appear and ensure all elements like content, links, and formatting work correctly. You can think of it as your final check before the actual send-off, providing you with the assurance that you’ve caught any errors or made necessary last-minute tweaks.

**Preview**: A visual verification tool within the Campaign builder itself. It gives you a snapshot of your content's appearance, including support for any tokens (email preview only) or personalization versions you’ve set up. While the preview may not fully simulate the complete rendering experience in the recipient’s inbox or device, it is designed to mirror the content as closely as possible.

**Email Renderings in Outlook**: To learn about the limitations of Outlook when it comes to displaying campaign emails, [check out this article](https://help.element451.com/en/articles/8549932-email-renderings-in-outlook).

---

# Testing Campaigns

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205825162/a6674033ea06c8b7971e271263f3/Campaign+Test.png?expires=1784430000&signature=505b1bef998667022206835976e1c03a8963b970bbe79189dac8b0a09485d265&req=dSInE8F8mIBZW%2FMW3Hu4gcT1gKu0s6qbBSEsTFS1Q%2FDLrgF%2BczqNrwoV4vPQ%0Apg%3D%3D%0A)

## Test Options by Channel

* **SMS**:

  + **Single Phone Number:** Does not support tokens or attachments.
  + **Sent to Segment:** Supports attachments, versions, and tokens.

* **Email**

  + **Single Email Address:** Does not support tokens or attachments. This is the case even if the email address is associated with a test record.
  + **Send to Segment**: Supports attachments, versions, and tokens.

* **Push Notifications**:

  + **Send to Segment**: Supports personalization and tokens.

## How-To: Send a Test (All Channels)

1. With your Campaign open, click the blue “**Test**” button in the top right corner.

   [![](https://downloads.intercomcdn.com/i/o/1194907297/062f3b78fe07f2c4ea4f8e67/Campaigns%2B-%2BTest%2BButton.png?expires=1784333700&signature=e3684a00058211c22a0a63e3b40043fe2d5c9c08f0bc47d0447ad81fff7e7ddd&req=dSEuEsB%2BmoNWXvMW1HO4zaSvaUrsz7Mi9QVfaQoW6xKY3zTJjaqlknf1mRNc%0AHzxv%0A)](https://downloads.intercomcdn.com/i/o/1194907297/062f3b78fe07f2c4ea4f8e67/Campaigns%2B-%2BTest%2BButton.png?expires=1784333700&signature=e3684a00058211c22a0a63e3b40043fe2d5c9c08f0bc47d0447ad81fff7e7ddd&req=dSEuEsB%2BmoNWXvMW1HO4zaSvaUrsz7Mi9QVfaQoW6xKY3zTJjaqlknf1mRNc%0AHzxv%0A)
2. **Select Channels**: If your Campaign uses multiple channels, you’ll be prompted to select which channel you wish to test. We recommend testing all channels.
3. **Send to Segment**: If sending to a test Segment:

   * Select the Segment you created for testing.
   * Use this option for full testing of tokens and personalization.
4. **Send to Individual**: If testing directly:

   * Enter an email address for email Campaigns

     + The field supports only one email address.
   * Enter a phone number for SMS Campaigns

     + The field supports only one mobile phone number.
     + You must include the country code (i.e., +1 for US numbers).
   * Push notification campaigns do not support individual testing.
5. When ready, click “**Test**” in the top right corner to initialize the test send.
6. Click the “**X**” in the top left corner to close and return to your Campaign.

# Important Notes:

* Always double-check your segment selection before sending tests or live campaigns.
* Avoid editing a campaign in multiple tabs or by multiple users simultaneously to minimize errors.

---

# Previewing Campaigns

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205824897/d50b32b001551ce79cf5cff21e70/Campaign+Preview+with+Token.png?expires=1784333700&signature=dd1a93b7659a49f3a3403e15ca2a8345131739a15e9e1976479b000eadbb5ed5&req=dSInE8F8mYlWXvMW1HO4zSym1pG3kEROQ62vxpDcoxYeUpOlgCaZIhK6leFs%0Ae5CpKsl%2Bq%2BTY7ymxBmw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205824897/d50b32b001551ce79cf5cff21e70/Campaign+Preview+with+Token.png?expires=1784333700&signature=dd1a93b7659a49f3a3403e15ca2a8345131739a15e9e1976479b000eadbb5ed5&req=dSInE8F8mYlWXvMW1HO4zSym1pG3kEROQ62vxpDcoxYeUpOlgCaZIhK6leFs%0Ae5CpKsl%2Bq%2BTY7ymxBmw%3D%0A)

## Preview Options by Channel

* **SMS**:

  + View a live, real-time preview of your text message in a mobile device mock-up on the right side of the builder.
  + You can also generate a shareable preview link to view and share the message.
* **Email**:

  + You can preview your email as it will appear to a specific contact, with all tokens and personalization applied.
  + Additionally, generate a shareable preview URL to allow others to view the email with current audience settings.
* **Push Notifications**:

  + Like SMS, push notification previews update live in a mobile device mock-up on the right side of the builder in real time as you make changes.

## How-To: Share Preview Link (Email + SMS)

The Public Preview Link is a shareable URL accessible by **anyone with the link**; logging into Element451 is not required. When viewing the public preview, viewers can:

* Toggle between email and SMS (if using both channels).
* Download a .HTML file (emails).
* Preview the Campaign in desktop or mobile formats (emails).
* View the default version only (if using personalized versions).

[![](https://downloads.intercomcdn.com/i/o/1195031982/b2b79cf72eebc891b7156e4e/Screenshot%2B2024-02-03%2Bat%2B4_01_03-E2-80-AFPM.png?expires=1784333700&signature=55b4b8e5f7102ff5c7cefb083c40ac395c0ae4b92068f37d9bf4a30fdc364bbe&req=dSEuE8l9nIhXW%2FMW1HO4zWmScK2uZtKQk1%2FzRFNKTOBScRweWL0D3d65RCh9%0AduamSN%2B3h7pLEAjen58%3D%0A)](https://downloads.intercomcdn.com/i/o/1195031982/b2b79cf72eebc891b7156e4e/Screenshot%2B2024-02-03%2Bat%2B4_01_03-E2-80-AFPM.png?expires=1784333700&signature=55b4b8e5f7102ff5c7cefb083c40ac395c0ae4b92068f37d9bf4a30fdc364bbe&req=dSEuE8l9nIhXW%2FMW1HO4zWmScK2uZtKQk1%2FzRFNKTOBScRweWL0D3d65RCh9%0AduamSN%2B3h7pLEAjen58%3D%0A)

### How-to Access + Copy the Preview Link

There are two ways to access and copy the public preview link for a Campaign:

#### Option 1 (Easiest + Preferred)

1. Open your Campaign.
2. In the heading, under the Campaign name, click **Preview**.
3. Share the URL.

   [![](https://downloads.intercomcdn.com/i/o/952603175/d3524dbae6ffde215dbca376/Screenshot+2024-02-03+at+4.19.21%E2%80%AFPM.png?expires=1784333700&signature=3212cf0aaf1072e0550c2ca30fca6619f121a956bcd644637f2f5b807940ebd5&req=fSUlEMl9nIZaFb4f3HP0gPMdBWlbfUfb7SqzOVnhc%2BKlG0%2FQDDNt4HS6WUlO%0AoPM%3D%0A)](https://downloads.intercomcdn.com/i/o/952603175/d3524dbae6ffde215dbca376/Screenshot+2024-02-03+at+4.19.21%E2%80%AFPM.png?expires=1784333700&signature=3212cf0aaf1072e0550c2ca30fca6619f121a956bcd644637f2f5b807940ebd5&req=fSUlEMl9nIZaFb4f3HP0gPMdBWlbfUfb7SqzOVnhc%2BKlG0%2FQDDNt4HS6WUlO%0AoPM%3D%0A)

#### Option 2

Because you will access the link in the **Configure** **Email** section, this option only works if you use the email channel for your Campaign. Note: The URL will be the same as option 1, so it will still be included if you use SMS.

1. Open your Campaign.
2. Click edit ![](https://downloads.intercomcdn.com/i/o/952594719/ea43bd4f190920a5a6a3d819/Screenshot+2024-02-03+at+3.48.42%E2%80%AFPM.png?expires=1784430000&signature=9cf0400a07ebbd1b9af12e5eb95b96830b7802ea9392a3cdd468cee5327d980b&req=fSUlE8B6moBWFb4X1HO4gbT4CLmkHqyS1qIE6U%2BBXGLAXAXDcu2PSBHH%2BHSa%0A) in the top right corner of the Campaign header.
3. Scroll down to the **Configure** **Email** section.
4. Click on the **Preview** tab in the right corner of the email editor.
5. Click the **link** **icon** in the top left corner of the email editor.

   [![](https://downloads.intercomcdn.com/i/o/952605833/1eb4bd435c389955fdd4a0f9/preview+link.png?expires=1784333700&signature=5337e2d79034f55edb51bf27177836596573abde77d282dcc68f93b102fd7510&req=fSUlEMl7lYJcFb4f3HP0gIb%2FlxHRs%2FOJMUu4VNtqQV7DJePrTM%2FFvijPd%2BFh%0Ay3I%3D%0A)](https://downloads.intercomcdn.com/i/o/952605833/1eb4bd435c389955fdd4a0f9/preview+link.png?expires=1784333700&signature=5337e2d79034f55edb51bf27177836596573abde77d282dcc68f93b102fd7510&req=fSUlEMl7lYJcFb4f3HP0gIb%2FlxHRs%2FOJMUu4VNtqQV7DJePrTM%2FFvijPd%2BFh%0Ay3I%3D%0A)
6. Share the URL.

##

## How-To: Preview Email Campaigns

Begin by accessing and **opening** the campaign you want to preview.

1. In the top right corner of the header, click **Edit**.
2. Once open, navigate to the **Configure Email** section.
3. In the right corner of the email builder, click on the **Preview** tab.

   [![](https://downloads.intercomcdn.com/i/o/952597173/93a306fecde4bfc6fdcebdc7/preview+campaign.png?expires=1784333700&signature=c71fcf946e6b2cd3bf7b6972d8bd4bbbf1b4dba2f701ca2d3f296f9771f258ef&req=fSUlE8B5nIZcFb4f3HP0gPe3Iqzhxf6dz0bY2xjPVR4bnsR68vyU7eRV7qzk%0ABEc%3D%0A)](https://downloads.intercomcdn.com/i/o/952597173/93a306fecde4bfc6fdcebdc7/preview+campaign.png?expires=1784333700&signature=c71fcf946e6b2cd3bf7b6972d8bd4bbbf1b4dba2f701ca2d3f296f9771f258ef&req=fSUlE8B5nIZcFb4f3HP0gPe3Iqzhxf6dz0bY2xjPVR4bnsR68vyU7eRV7qzk%0ABEc%3D%0A)
4. **Select a Contact for Preview**: Click on the person icon in the top left corner of the email editor. This will allow you to search for and select a contact whose information will be used to personalize the email preview.
5. **View the Personalized Preview**: Once you've selected a contact, the email preview will display the token and personalization content as it would appear for that specific recipient. This lets you see how the email looks and functions for individual contacts before sending.

## How-To: Preview SMS + Push Notification (Beta) Campaigns

If your Campaign has either an SMS message or push notification, a preview in the form of a mobile phone mock-up will appear to the right of each respective “Configure” section.

1. Begin by accessing and **opening** the campaign you want to preview.
2. In the top right corner of the header, click **Edit**.
3. Once open, navigate to the **Configure SMS** or **Push Notification** section to see the preview.
4. If using versions, you can adjust the preview by using the "**version**" dropdown next to the "Outbound Phone Number" and/or "SMS Text" fields.

   [![](https://downloads.intercomcdn.com/i/o/952599851/611f329835fc0bf7ddcfac58/Screenshot+2024-02-03+at+4.07.33%E2%80%AFPM.png?expires=1784333700&signature=35101fdf49a0909def13900b4cb905b71e294668baa49b662c4de941ee869776&req=fSUlE8B3lYReFb4f3HP0gHhn3S8NeHpCcsT00S9sMJs2PtsPFbPPZ4jOywJj%0AReI%3D%0A)](https://downloads.intercomcdn.com/i/o/952599851/611f329835fc0bf7ddcfac58/Screenshot+2024-02-03+at+4.07.33%E2%80%AFPM.png?expires=1784333700&signature=35101fdf49a0909def13900b4cb905b71e294668baa49b662c4de941ee869776&req=fSUlE8B3lYReFb4f3HP0gHhn3S8NeHpCcsT00S9sMJs2PtsPFbPPZ4jOywJj%0AReI%3D%0A)

![](https://downloads.intercomcdn.com/i/o/1071463217/7b654e589888725b9de57e1e/Note-Orng.png?expires=1784430000&signature=6f23974794e64cff266aa1a508876f88647f70e5d7ea4af0ca81668bba25e96e&req=dSAgF814noNeXvMW3Hu4gbB76UpzUidpaVLzOBVUOpDL856jAW%2FJLK%2Fg3Vwp%0AoA%3D%3D%0A) If the SMS text has not been configured for the selected version, a chat bubble icon with three dots will appear in the preview area. This indicates that there is no SMS content configured for that version yet.

---

# How to Preview Token Values + Magic Links

You can preview and test how tokens populate in a few different ways:

* **Testing**: When sending your campaign tests using the 'Send to Segment' option, the token values should populate based on the recipient's record data. You cannot use the individual email or phone number test, as tokens are not supported in those tests.

* **Previewing**: When previewing your campaigns, you can use two methods:

  + **Preview as Recipient**: You can use the preview feature to select a recipient to impersonate. The email will appear in the email builder as if it were being sent to that particular contact, with all tokens and personalization applied.
  + **Sent to Segment**: You can also use the “Send to Segment” option. When the recipients in your test segment receive the email, it should include all personalization and tokens based on their record data.

---

# Sendgrid URLs

In some cases, links in your email campaigns may preview as long SendGrid URLs instead of the original link. This happens because Element uses SendGrid to manage bulk email sends and track link clicks. To do this, SendGrid automatically replaces the original URL with a tracking link when the email is sent. This ensures that link clicks are tracked and the recipient is still directed to the original destination.

---