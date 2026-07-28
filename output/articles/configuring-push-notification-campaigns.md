---
title: Configuring Push Notification Campaigns
url: https://help.element451.com/en/articles/9923167-configuring-push-notification-campaigns
collection: Campaigns
---

# Overview

This guide focuses on configuring push notification-specific settings within your campaign after completing the general setup steps (e.g., choosing your campaign type, channels, audience, and communication settings).

Before configuring push notifications, please note the following:

* Push notifications work exclusively with StudentHub and are available to partners on the Engage package.
* The basics of Campaigns + push notifications:

  + [Creating a Campaign (All Channels)](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels)
  + [StudentHub + How Push Notifications Work](https://help.element451.com/en/articles/9888911-studenthub-push-notifications)

---

# 1. Configure Push Notification

After selecting the **push notification** channel during your [initial campaign setup](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels), you can begin configuring the push notification-specific settings:

## Title

The title is bolded at the top of the push notification and is typically the first thing that catches your attention. Keep it concise (aim for 30-40 characters or less to ensure it’s clear and visible on all devices), attention-grabbing, and relevant to the content of the message.

## Content (Body)

Provides the main message of the notification. Use clear and direct language to communicate the purpose of the notification. You can also include tokens to personalize the message for each student. You should aim to keep the content of the message around 120 characters or less.

## Parameters (Link)

Each notification includes a URL, so when students tap to open it, they’ll see a button at the bottom. For example, a “Time to Register for Classes” notification might have a URL that directs students to schedule an appointment with their advisor. You must use a fully qualified URL (including <https://>).

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205068534/32b9882d0f6e6e8be32ca9fc62af/Hub++Dash+-+Campaigns+-+Conf+Push%402x.png?expires=1784333700&signature=24c9a84e3d33c1d04c7b949816a0ca21deaf6d65496dfea2b1fc67e0cb9bb24c&req=dSInE8l4lYRcXfMW1HO4zWXUShpPSrDc31%2BjDKRBs1%2FTEuPjsLI5Qqzd9gQz%0Ami5gxa4ACbmuSX0CmIc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205068534/32b9882d0f6e6e8be32ca9fc62af/Hub++Dash+-+Campaigns+-+Conf+Push%402x.png?expires=1784333700&signature=24c9a84e3d33c1d04c7b949816a0ca21deaf6d65496dfea2b1fc67e0cb9bb24c&req=dSInE8l4lYRcXfMW1HO4zWXUShpPSrDc31%2BjDKRBs1%2FTEuPjsLI5Qqzd9gQz%0Ami5gxa4ACbmuSX0CmIc%3D%0A)

## Personalization Versions

The personalization feature with version conditions lets you customize each component of your push notification—the title, content, and link for each version.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205074736/fe2cdc6dcc5e8e5fbb279471b6db/Hub+-+Campaigns+-+Version+Cond%402x.png?expires=1784333700&signature=b7fc886d2ce7d4c6cc8ae18f0d3c6e26d68251d588a13fd36ea57f0c0c7e2b34&req=dSInE8l5mYZcX%2FMW1HO4zeNlu7pq6BnLuCX6tb4SlbHdEwMRbeRtJVNKhOH3%0A1lXfd6lHurO%2BZxNK3FE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205074736/fe2cdc6dcc5e8e5fbb279471b6db/Hub+-+Campaigns+-+Version+Cond%402x.png?expires=1784333700&signature=b7fc886d2ce7d4c6cc8ae18f0d3c6e26d68251d588a13fd36ea57f0c0c7e2b34&req=dSInE8l5mYZcX%2FMW1HO4zeNlu7pq6BnLuCX6tb4SlbHdEwMRbeRtJVNKhOH3%0A1lXfd6lHurO%2BZxNK3FE%3D%0A)

Select the version you want to modify from the version drop-down in the respective field. This ensures your recipients receive the most relevant and personalized message possible.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205074242/63c9f83238659cfebba307c09a15/Hub+-+Campaigns+-+Push+Versions.gif?expires=1784333700&signature=312b409b5c3823676b5b93d027b82d8167b88574b7f2b46ffc551d8e981fc42a&req=dSInE8l5mYNbW%2FMW1HO4za1gnCKoZOrPWEc%2BObWXN4qs6biMDk7emzHRUB%2FG%0AWZ0XLE81%2BCkA0SsctxI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205074242/63c9f83238659cfebba307c09a15/Hub+-+Campaigns+-+Push+Versions.gif?expires=1784333700&signature=312b409b5c3823676b5b93d027b82d8167b88574b7f2b46ffc551d8e981fc42a&req=dSInE8l5mYNbW%2FMW1HO4za1gnCKoZOrPWEc%2BObWXN4qs6biMDk7emzHRUB%2FG%0AWZ0XLE81%2BCkA0SsctxI%3D%0A)

## Tokens + Emojis

Push notifications support tokens and emojis, allowing you to personalize and enhance messages.

* **Tokens**: Use the **Add Token** button to include data from the contact's record. For example, if you used `[user:first_name]`, it would replace the token with the recipient's first name when they receive the message.

  + [Click here](https://help.element451.com/en/articles/1524113-tokens) to read more on tokens.
* **Emojis**: Add emojis for a friendly touch and better engagement.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205078066/74c08dca2b06aa99f94165e38b09/Hub%2B-%2BCampaigns%2B-%2BEmoji%2BTokens-402x.png?expires=1784333700&signature=c5592d5d47f8321f046f69b3c5fe5fc5aa7774e3d2083112c51d83c0fb0daa0a&req=dSInE8l5lYFZX%2FMW1HO4zRlg%2FRuYbvwgfXKqgD9YitBsHjzRCELJidXxYvi6%0A0cvv6%2BrP51TKbFP1CzE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205078066/74c08dca2b06aa99f94165e38b09/Hub%2B-%2BCampaigns%2B-%2BEmoji%2BTokens-402x.png?expires=1784333700&signature=c5592d5d47f8321f046f69b3c5fe5fc5aa7774e3d2083112c51d83c0fb0daa0a&req=dSInE8l5lYFZX%2FMW1HO4zRlg%2FRuYbvwgfXKqgD9YitBsHjzRCELJidXxYvi6%0A0cvv6%2BrP51TKbFP1CzE%3D%0A)

---

# 2. Preview Your Push Notification

As you compose your push notification, the preview pane on the right displays how the notification will appear to recipients.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205067811/d688fca761320d98425686b5dbbb/Hub+Dash++Campaign+Preview%402x.png?expires=1784333700&signature=99b858d5e6a2b9dc0d4fd23be74298373f3cbbad214db57db19fbf5ce2046529&req=dSInE8l4moleWPMW1HO4zSPD62EEJ9BNVPAi1XtmTPrbpzvonyzzcYONHTqI%0AXP%2FftG8JC9FMH1LGhgo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205067811/d688fca761320d98425686b5dbbb/Hub+Dash++Campaign+Preview%402x.png?expires=1784333700&signature=99b858d5e6a2b9dc0d4fd23be74298373f3cbbad214db57db19fbf5ce2046529&req=dSInE8l4moleWPMW1HO4zSPD62EEJ9BNVPAi1XtmTPrbpzvonyzzcYONHTqI%0AXP%2FftG8JC9FMH1LGhgo%3D%0A)

---

# 3. Test + Review Versions

Once your push notification configuration is complete, we recommend testing the message to ensure everything displays as intended. You should also review each version to verify accuracy if you’ve set up personalized versions for different audiences.

[Explore More: Testing + Previewing →](https://help.element451.com/en/articles/8901250-testing-previewing-campaigns)

---

# 4. Send or Save Your Campaign

After finalizing your push notification content and testing it, proceed to send or save your campaign. This process is outlined in the [Creating a Campaign (All Channels)](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels)article.

---

# Push Notification Use Cases + Best Practice

Check out the [StudentHub: Push Notifications](https://help.element451.com/en/articles/9888911-studenthub-push-notifications) guide for a deep dive into how they work, how to use them effectively, and best practices to keep your students engaged.

[Explore More: Push Notifications →](https://help.element451.com/en/articles/9888911-studenthub-push-notifications)

---