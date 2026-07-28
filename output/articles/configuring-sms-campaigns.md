---
title: Configuring SMS Campaigns
url: https://help.element451.com/en/articles/8901214-configuring-sms-campaigns
collection: Campaigns
---

Create and send visually appealing and personalized SMS messages for one-time or ongoing communication campaigns.

# Overview

This guide focuses on configuring SMS-specific settings within your campaign after completing the general setup steps (e.g., choosing your campaign type, channels, audience, and communication settings).

This article assumes you understand the basics of creating a Campaign. If you haven't already, please read [Creating a Campaign (All Channels)](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels) for guidance on the **initial** steps of creating a campaign.

![](https://downloads.intercomcdn.com/i/o/1193400783/52619b3218456d201599cc57/Important.png?expires=1784430000&signature=e0abbdfd5c0c616536efdc8cfb1e687add3f20dc615b47b967894d727d890d1a&req=dSEuFc1%2BnYZXWvMW3Hu4gS53DPtNk88pjQGw6I85Yr94aAq20utgy5F9ssmR%0A9Q%3D%3D%0A) Element451 cannot send SMS messages to VoIP numbers. Please make sure your contacts have valid mobile numbers for successful delivery.

---

# 1. Configure SMS

After selecting the **SMS** channel during your [initial campaign setup](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels), you can begin configuring the SMS-specific settings:

## Outbound Phone Number

The outbound phone number is the number your recipients will see as the sender of the SMS. You can choose your dedicated Element451 10-digit phone number or short code number. The short code number is ideal for sending large volumes of messages quickly.   
​  
Remember, the Element451 short code does not receive inbound messages.

## SMS Text

The SMS Text is the content of your message—where you compose the text. You can include text, emojis, tokens, and URLs in the message.

[![](https://downloads.intercomcdn.com/i/o/1193434408/ff159d24441c408c75887aab/Campaigns-2B-2BText.png?expires=1784333700&signature=cc371dc0ab13a641b4b912a3c79bbe09627de4b79e89c79d3b3e9ece6a734d47&req=dSEuFc19mYVfUfMW1HO4zd6yQL3d%2B1khYI%2FVo4qU%2BPZ51TQZgKiF%2Fi%2BC4Cwz%0AAlQIixE0Iosk2MTXkN4%3D%0A)](https://downloads.intercomcdn.com/i/o/1193434408/ff159d24441c408c75887aab/Campaigns-2B-2BText.png?expires=1784333700&signature=cc371dc0ab13a641b4b912a3c79bbe09627de4b79e89c79d3b3e9ece6a734d47&req=dSEuFc19mYVfUfMW1HO4zd6yQL3d%2B1khYI%2FVo4qU%2BPZ51TQZgKiF%2Fi%2BC4Cwz%0AAlQIixE0Iosk2MTXkN4%3D%0A)

* **Character Count**: SMS messages are limited to 1600 characters. However, best practice is to keep messages much shorter than that. We recommend 160 characters for the best technical and end-user experience.​
* **Tokens**: Use the **Add Token** button to include data from the contact's record. For example, if you used `[user:first_name]`, it would replace the token with the recipient's first name when they receive the message. [Click here](https://help.element451.com/en/articles/1524113-tokens) to read more on tokens.
* **Emojis**: Add emojis for a friendly touch and better engagement.
* **URLs**: We automatically apply URL shortening to make links in SMS messages more visually appealing and to track click-through rates. This helps us understand how people are interacting with the content we share. Additionally, when including links in your SMS messages, you **must** include the protocol (<https://>) with the link.

## Using Personalization in SMS Settings

Using the personalization feature with version conditions lets you customize various aspects of your SMS, including the **outbound phone number** and **text** for each version.

Select the version you want to modify from the version drop-down in the respective field. This ensures your recipients receive the most relevant and personalized message possible.

[![](https://downloads.intercomcdn.com/i/o/1193439448/f77e8e0317601e09aa40f3f0/Campaigns%2B-E2-86-92%2B%2BVersions%2Bin%2BSMS.png?expires=1784333700&signature=30c0adace3a8f49419fd7d1312686b942389ef541d0cd288c62c1132b44170c7&req=dSEuFc19lIVbUfMW1HO4zUd2sNUHuOi8iZPiu29dGFrA6EhOuI5trQIaKvNw%0ARS59zU2TywqhW8nnsPo%3D%0A)](https://downloads.intercomcdn.com/i/o/1193439448/f77e8e0317601e09aa40f3f0/Campaigns%2B-E2-86-92%2B%2BVersions%2Bin%2BSMS.png?expires=1784333700&signature=30c0adace3a8f49419fd7d1312686b942389ef541d0cd288c62c1132b44170c7&req=dSEuFc19lIVbUfMW1HO4zUd2sNUHuOi8iZPiu29dGFrA6EhOuI5trQIaKvNw%0ARS59zU2TywqhW8nnsPo%3D%0A)

## Unsubscribe Prompt

By law, all bulk SMS messages are required to provide instructions on unsubscribing from future messages. A default prompt is provided; however, if you choose, you can edit the prompt. Your prompt should include the word **UNSUBSCRIBE** or **STOP**.

[Explore More: SMS Opt-In + Opt-Out →](https://help.element451.com/en/articles/8390046-understanding-sms-opting-in-and-out)

## Attachment

You can attach an image, audio, or other media file to your text message. Click **Add a File** to make a selection from your media manager or upload a new file.

* MMS media is supported only for US numbers (+1).
* If you use .gifs, be sure to follow best practices for this media type.
* You should ensure attachments are no larger than 3MB, as messages with larger attachments will not be delivered.
* Some mobile operating systems automatically crop the preview image, so we recommended aspect ratios of 1:1, 9:16, or 4:3.

---

# 2. Preview Your SMS

As you compose your SMS message, the preview pane on the right displays how your SMS will appear to recipients.  
​

[![](https://downloads.intercomcdn.com/i/o/873815614/7c755f5c24aa95262ce48088/Campaigns+-+Configure+SMS+-+Preview.png?expires=1784333700&signature=55a27de37e84c3306aa1ed68c9463e1863da4bb45a9d0e846d40620ba28bc744&req=fCckHsh7m4BbFb4f3HP0gMfH2eLspAkYHJxlRpyMJ2pWyWLgKx1o%2F%2BxfDCOP%0ATdjR99xxZX2rkwpS8g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/873815614/7c755f5c24aa95262ce48088/Campaigns+-+Configure+SMS+-+Preview.png?expires=1784333700&signature=55a27de37e84c3306aa1ed68c9463e1863da4bb45a9d0e846d40620ba28bc744&req=fCckHsh7m4BbFb4f3HP0gMfH2eLspAkYHJxlRpyMJ2pWyWLgKx1o%2F%2BxfDCOP%0ATdjR99xxZX2rkwpS8g%3D%3D%0A)

---

# 3. Test + Review Versions

Once your SMS configuration is complete, we recommend testing the message to ensure everything displays as intended. You should also review each version to verify accuracy if you’ve set up personalized versions for different audiences.

[Explore More: Testing + Previewing →](https://help.element451.com/en/articles/8901250-testing-previewing-campaigns)

---

# 4. Send or Save Your Campaign

After finalizing your SMS content and testing it, proceed to send or save your campaign. This process is outlined in the [Creating a Campaign (All Channels)](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels)article.

---

# 5. View Campaign Analytics

You can use the in-app analytics to see how your SMS messages perform.

To view analytics, navigate to **Engagement** > **Campaigns** > **Analytics**.On this screen, you’ll see a list of communications and all their analytics.

[Explore More: Campaign Analytics →](https://help.element451.com/en/articles/1513688-campaign-analytics)

---

# Best Practices for Using .gifs in your MMS Message

Follow these best practices

## File Size

* Keep GIFs as small as possible. The recommended maximum is 600 KB to ensure broad carrier compatibility.
* The absolute maximum for MMS is 5 MB (including text), but most carriers have much lower limits for images/gifs (often 1 MB or less).

  + AT&T: 1 MB
  + T-Mobile: 1.5 MB
  + Verizon: 1 MB

## Dimensions & Resolution

* There is no strict pixel resolution limit, but larger images may be compressed or resized by the carrier to optimize deliverablity.
* For best results, use standard mobile-friendly dimensions such as 480x480 pixels or smaller.

## Animation Length & Complexity

* Shorter, simpler GIFs are more likely to render well on all devices.
* Limit the number of frames and avoid excessive animation length to keep file size down.

## Color Depth

* Use a limited color palette (fewer colors) to reduce file size.
* GIFs with fewer colors compress better and are more likely to be delivered successfully. Full color gifs may overly pixilate on compression.

## Compatibility

* Test your GIFs on multiple devices and carriers to ensure they display as intended.
* Some older devices or carriers may not support animated GIFs, or may display only the first frame.

## Format

* Use the .gif file extension and ensure the MIME type is set to image/gif.
* Avoid using transparency or advanced GIF features that may not be supported everywhere.

## Content

* Make sure your GIF content is appropriate and relevant to your message.
* Avoid flashing or strobing effects, which can be problematic for some users.

![Important](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2078291220/2ea96afce581db70eff6ebf84000/Important.png?expires=1784430000&signature=85b1fb8621d2dc4f28cf4726ae9708d24298bc92f40a421cfaf7a5150168cbfb&req=diAgHst3nINdWfMW3Hu4gfGGbnbLDXgRy%2B3sLYijzhLHz6Ip0IcI59LsTJwj%0AGA%3D%3D%0A) It is not recommended to use Element451 SMS Campaigns for large-scale, time-sensitive alerts, such as campus emergencies. Campaigns are not optimized for immediate delivery, and large or repeated sends can negatively impact your carrier reputation and future deliverability.

---