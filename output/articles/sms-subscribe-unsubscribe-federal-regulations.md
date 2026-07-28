---
title: SMS: Subscribe/Unsubscribe + Federal Regulations
url: https://help.element451.com/en/articles/8390046-sms-subscribe-unsubscribe-federal-regulations
collection: Campaigns
---

Information and best practices to ensure regulatory compliance and maintain deliverability for SMS / Text Messages sent via Element451.

# Overview

Using text messages (SMS) to communicate with students and other contacts is a great way to connect. But, you must follow certain regulations and best practices to ensure your messages are sent to those who want them and are ultimately received.

As part of your onboarding, Element451 registers your school and associated Element451 SMS-enabled phone numbers as the first step in A2P 10DLC compliance.

## Compliance Reminders

To maintain high SMS deliverability and prevent your sender numbers from being suspended or blocked, it is imperative that you follow our [best practices](#h_3a542546c2) and comply with federally mandated regulations.

1. **Only send SMS messages to contacts who have opted in.** Sending messages without consent violates anti-spam laws.
2. **Avoid prohibited SHAFT content** (sexual content, hate speech, alcohol and other drugs, firearms, tobacco) to prevent suspension or blocking.
3. **Non-compliance can harm deliverability.** High opt-out or spam complaint rates may lower your *carrier trust score*, reducing message success.

This article will guide you through the process of how recipients can choose to receive (opt-in) or stop receiving (opt-out) your messages, along with other important guidelines for effective and compliant SMS use.

---

# Subscribing (Opting In)

Subscribing, or opting in, refers to a contact consenting to receive SMS messages from your institution. This requires the contact to take **clear affirmative action** **to agree to receive messages**, such as checking a box or clicking a button.

When collecting cell phone numbers on **Forms**, **Applications**, or **Event** **Sign-Up Forms**, you should require user consent to receive SMS messages. We strongly recommend using the system opt-in field. You can explore more on the system opt-in field in [this article](https://help.element451.com/en/articles/9007065-understanding-sms-opt-in-system-field).

## Resubscribe a Contact

If a contact has previously unsubscribed, changes their mind, and wishes to re-subscribe to your SMS messages, they must send the keyword '**START**' to your Element451 phone number. When a user sends **START** to an Element number:

* **Milestone**: The associated *Unsubscribe Milestone* is automatically removed.
* **Activity**: A new *Resubscribed*activity is added to the activity feed, ensuring the opt-in is timestamped for accurate tracking.

You can manually delete unsubscribe milestones via the milestones profile card; however, **this will not resubscribe the contact**. They will still need to provide consent by texting the keyword 'START.'

---

# Unsubscribing (Opting Out)

Unsubscribing is when contacts revoke their consent and no longer wish to receive SMS messages.

## Unsubscribe Options + Adding Option to SMS

You must offer a simple way for contacts to opt-out, such as replying with STOP or clicking on an unsubscribe link. We explain the two methods below:

### Contact Self-Unsubscribe

## Opting-Out via Keyword Reply

Element451 recognizes the industry standard keywords for opting out of receiving SMS. While STOP is the one we use most often, any of the following keywords will opt-out a phone number:

* **STOP**
* **UNSUBSCRIBE**
* **END**
* **QUIT**
* **CANCEL**
* **STOPALL**

These keywords are case-insensitive, meaning "Stop" will be treated the same as "STOP" or "stop," but they do need to be the only content in the inbound message.

## Campaigns

When creating a **Campaign**, Element451 will require you to include an **Unsubscribe Prompt** in the Configure SMS section. By default, the prompt is set to "Reply STOP to unsubscribe," but if you choose, you can rewrite the prompt. However, you must include clear instructions on unsubscribing and using STOP or another recognized keyword.   
​

[![](https://downloads.intercomcdn.com/i/o/834054293/5a4c23356f4c409566d8f67e/SMS+Opt+Out+Prompt.png?expires=1784333700&signature=3746025d0e933dcca7dc5e146155c5bfeccd0ac4ce73043dcff7b46459e4ae7f&req=fCMjFsx6n4hcFb4f3HP0gDAq3mSqllE%2FyjHXrUF%2BRrYi9ExdSgr1W7X6hXrg%0AOH2w0%2BymivkY0aKeSQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/834054293/5a4c23356f4c409566d8f67e/SMS+Opt+Out+Prompt.png?expires=1784333700&signature=3746025d0e933dcca7dc5e146155c5bfeccd0ac4ce73043dcff7b46459e4ae7f&req=fCMjFsx6n4hcFb4f3HP0gDAq3mSqllE%2FyjHXrUF%2BRrYi9ExdSgr1W7X6hXrg%0AOH2w0%2BymivkY0aKeSQ%3D%3D%0A)

## Conversations

An opt-out message is not automatically included with SMS messages delivered from the Conversations module. However, a recipient can still reply with "STOP" or other recognized key word. and they will stop receiving messages.

### Unsubscribe by Internal User

As explained above, a contact can self-unsubscribe from your SMS communication, but you also have the option to unsubscribe them manually. To learn more about this process, explore our help article, [Email + SMS: Manually Unsubscribe Contacts](https://intercom.help/element451/en/articles/6066486-manually-unsubscribe-a-user-from-email-sms-communication).

[Explore More: Manually Unsubscribe →](https://help.element451.com/en/articles/6066486-email-and-sms-manual-unsubscribe)

## The Process of Unsubscribing (Milestones + Activities)

When a contact sends '**STOP'** to an Element number, the system adds both a milestone and activity to the contact's profile. We explain each one below:

### Milestone

When a person unsubscribes, the **`SMS Unsubscribe Date`** [milestone](https://help.element451.com/en/articles/3419189-milestones) is added to that contact's profile. Following this, they will no longer receive messages from you, whether through Conversations or Campaigns.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374207687/f8c9e00d07bc5acc7d96576d5efb/Important.png?expires=1784430000&signature=b636938108ad6f213c802b3b67c85c4c9021ef057dfd2ca8751a46e65559d867&req=dSMgEst%2BmodXXvMW3Hu4gRTkoyqe%2BNvWpmz2a6BTUdZqK%2FgPiDJU942aY1Lv%0AEg%3D%3D%0A)

1. An unsubscribe is tied to the **phone number**, so if the same number is used on multiple profiles (e.g., a student and parent record), all associated profiles will be unsubscribed and will no longer receive SMS messages. If you suspect this is the case, you can use the search bar to search for the phone number, look at the returned people's records, and check their milestones for an unsubscribe.
2. If your institution utilizes multiple Element451 numbers, the unsubscribe action will apply to **all** outbound numbers.

### Activity

A new *SMS Unsubscribed* activity is added to the contact's activity feed, capturing the exact time of the opt-out.

## Importance of Milestones + Activity Records

Milestones maintain the subscription status at a glance, while activity records provide a detailed timeline of when opt-in/out events occur. This ensures a more precise analysis of unsubscribe/subscribe trends, helping you:

* Track opt-in/out events by campaign or over time.
* Improve the accuracy of your engagement and retention metrics.
* Stay compliant with SMS marketing regulations.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374292367/a22ae026f211bc8bbd1c5cee81b5/Pro+Tip.png?expires=1784430000&signature=c641972cddcb41036520e9f3ef81903ae6814512b70a089cca75097c479fb84d&req=dSMgEst3n4JZXvMW3Hu4gVbAbCBdGLkUdzlQvTd9v78L0C2s1EkG%2BIs5%2B94T%0Akw%3D%3D%0A) It is best practice to add a label to the contact's profile when they unsubscribe, as it provides an at-a-glance indicator. You can automate this process by creating a rule that is initiated by the 'joined segment' trigger.

---

# Monitoring + Tracking SMS Subscriptions

Understanding how subscription changes are recorded in Element451 helps you monitor and analyze student engagement effectively, with precise date/time analytics tied to subscription activities.

* **Campaign** *or* **Time-Based Tracking**: You can track unsubscribe activity over time or by Campaign in the [Campaigns Insights dashboard](https://intercom.help/element451/en/articles/6788884-campaigns-dashboard) using the available control. This dashboard lets you identify trends, compare campaign performance, and refine your messaging strategies.

* **Individual Contact Tracking**: For contact-specific activity, check the [Activity Feed](https://intercom.help/element451/en/articles/5159877-activity-feed-overview) to view their SMS unsubscribe **`smsUnsubscribed`** and resubscribe **`smsResubscribed`** actions. You can also build a custom segment using the “Unsubscribed from SMS” and “Resubscribed to SMS” filters to identify these individuals easily.

This tracking process applies specifically to **SMS Campaigns**. Email campaigns use a similar milestone and activity structure to track subscription status, ensuring channel consistency.

---

# Transactional vs. Marketing Messages

Understanding the difference between transactional and promotional messages is key to managing communication effectively while respecting contact preferences and compliance regulations.

Use the collapsable sections below to review the differences between transactional and marketing communication priorities:

## Transactional SMS Messages

Transactional messages provide essential updates, confirmations, or notifications directly related to a student’s account, application, or engagement with your institution. These messages are typically triggered by a specific action taken by the student and are not promotional in nature.

* **Highlights**

  + They do not require [opt-in consent](https://help.element451.com/en/articles/8390046-sms-opting-in-and-out-understanding-us-regulations#h_c6d51aa2d5).

    - While it's not required, it's strongly recommended.
  + They are usually one-time notifications rather than part of an ongoing campaign.
  + They cannot be sent if a recipient has opted out.

    - TCPA regulations prohibit sending any messages to phone numbers that have opted out.
    - This contrasts with the CAN-SPAM Act, which allows *transactional* email messages to be sent to individuals who have opted out or unsubscribed. [Read more about email unsubscribe here](https://intercom.help/element451/en/articles/2608500-email-unsubscribe-opt-out-federal-regulations).
* **Examples**

  + Application Submission Confirmation
  + Event Registration Confirmation
  + Appointment Reminder
  + Password Reset Request

## Marketing SMS Message

Promotional messages are used for marketing purposes, encouraging students to engage with events, programs, or opportunities. These messages are typically part of an ongoing outreach campaign rather than being tied to a single action.

* **Highlights**

  + Require prior [opt-in](https://help.element451.com/en/articles/8390046-sms-opting-in-and-out-understanding-us-regulations#h_c6d51aa2d5) consent to be sent.
  + They cannot be sent to recipients who have opted out of SMS.
  + Often part of an ongoing engagement campaign rather than a one-time notification.
* **Examples**

  + Open House Invitation
  + RFI Drip Campaign Follow-Up
  + Scholarship Opportunities

## Which One to Use?

* If your message is purely informational, triggered by a student action, or they explicitly requested the information, it is **transactional** and does **not** require opt-in consent (but it's highly recommended).
* If your message promotes engagement, enrollment, or an event, it is **marketing** and **requires** opt-in consent.

---

# U.S. Regulations for SMS Messaging

The main laws governing SMS marketing in the U.S. are:

* TCPA (Telephone Consumer Protection Act) - prohibits sending messages to users without their consent using an auto-dialer. Consent can be given verbally, in writing, or electronically.
* CTIA (Cellular Telecommunications and Internet Association) - requires clear notice and user consent for sending any SMS messages. Messages must clearly identify the sender and provide opt-out information.

## What is A2P 10DLC?

A2P 10DLC stands for Application-to-Person 10-digit long code. This new SMS messaging framework by The Campaign Registry (TCR) provides companies with an optimized way to send SMS messages to consumers at scale. The 10-digit phone number(s) Element451 provides you is registered for A2P 10DLC compliance. This helps ensure deliverability with carriers by giving you a verified identity. No action is needed on your part other than maintaining good practices of providing a clear opt in and out process, creating content that provides value to the recipients and targeting your messages to the right audiences.

---

# Best Practices to Maintain High Deliverability

Telecom carriers monitor the activity of each phone number used to send SMS messages within their networks. If a number exhibits signs of sending unwanted messages or content that violates policies, carriers may limit or entirely block its message delivery.   
​  
While carriers don't generally share their exact metrics for filtering, to maintain higher deliverability rates, we recommend you adhere to the following best practices:

## Respect Opt-in & Opt-out Requests

This is the single best thing you can do to protect your deliverability. High opt-out rates or spam reports signal to carriers that recipients may not have willingly subscribed to your messages.

For mass communications, consider targeting more engaged prospects or students. Also, consider reducing the number of messages to individuals who have not interacted with your institution in over a year (or some other time horizon), as they are more likely to opt-out.

## Message Frequency

Be mindful of the frequency of marketing or promotional messages. Sending such messages too frequently (e.g., multiple times per week) can be counterproductive and drive higher-than-average opt-out rates. Transactional, confirmation, and targeted promotional messages to highly engaged individuals can be sent more frequently, provided they are timely and relevant.

## Identify Yourself

Ensure your messages clearly state who they are from. If recipients cannot immediately recognize the institution that is sending the message or their connection to the content, they are more likely to opt-out.

## Include Clear Calls to Action

Use clear call-to-actions to drive students to take the next step and drive students to trusted online resources of your university website, Element451 landing pages, applications, or microsites.

## Use Personalization

Employ personalization tokens (Like first name) in Element451 to tailor each message, showing recipients that you recognize them as individuals. This not only enhances the recipient's experience but also helps your messages bypass carrier filters.

## One-Time vs. Ongoing SMS Communications

Both One-Time and Ongoing communications can be used to send SMS messages. However, large batches (3,000+) sent via one-time campaigns are at higher risk of being filtered by some carriers, which could result in lower delivery rates, especially when those messages contain links and lack personalization. Therefore, it is best to reserve one-time campaigns for urgent or time-sensitive messages like impending deadlines.   
​  
For more routine messages, leveraging Ongoing Campaigns and Workflows to deliver messages asynchronously based on student actions is preferred. This approach spreads out the message distribution over a more extended period. Such a strategy helps to improve the overall deliverability of messages. As a bonus, it also reduces the manual steps required to set up one-time campaigns that you repeat on a regular basis.

### An Example to Dive a Little Deeper

**Example Scenario:** Communicating with Students Who Submitted an RFI Form

​**Using One-Time Communications:**

Imagine you decide to target students who filled out a Request for Information (RFI) form in the last week.

* At the end of each week, you compile a list of students who submitted the form that week. Let's say this amounts to 3,143 students who all receive the message at once, whether they submitted the form 7 days ago or 1 hour ago.

**Ongoing Communication Approach:**

Alternatively, you set up an on-going communication and workflow that activates once a student submits the RFI form.

* After a 5-day delay, the workflow sends out an SMS message encouraging the student to connect with an enrollment advisor.

Over a week, this approach also reaches a similar total number of students. However, it distributes the messages, sending approximately 450 messages each day rather than all at once. Moreover, these daily messages are spread out throughout the day.

**Advantages of Ongoing Communications:**

* ***Reduced Risk of Carrier Filtering:*** By avoiding a large blast of messages at once, ongoing communications are less likely to be flagged and filtered by carriers.

* ***Consistent Engagement:*** Spreading messages out provides consistent engagement with students. It also spreads out the inbound replies. Helping to avoid overwhelming staff at a single point in time.

* ***Personalized Interaction:*** This method feels more personalized, as messages are sent in response to a student's action (submitting the RFI form), enhancing the relevance and impact of the communication.

By adopting ongoing communications, you can ensure a smoother, more effective outreach that benefits your institution and students by fostering timely and more engaging interactions.

## Avoid Prohibited Content (SHAFT)

While not usually an issue for colleges or universities, avoid sending prohibited content, including but not limited to **SHAFT** content, as this can lead to immediate blocking and fines from carriers.

To help ensure compliance, **AI Content Review automatically scans outbound SMS messages** for SHAFT content before sending. If a message contains restricted terms, it will be blocked to prevent delivery. While this feature provides a safeguard, it’s always best practice to avoid terms that may be deemed as prohibited content. You can read more about our AI Content Review [below in the next section](https://help.element451.com/en/articles/8390046-sms-subscribe-unsubscribe-federal-regulations#h_b0b50a0b25).

### What is SHAFT?

**SHAFT** is an acronym representing categories of content that are **prohibited** or **restricted** due to regulatory and carrier compliance requirements.

These categories include:

* **Sexual Content**: Explicit sexual material or adult content.
* **Hate Speech**: Content promoting hate or violence against individuals or groups.
* **Alcohol**: Promotion or sale of alcoholic beverages (and other drugs).
* **Firearms**: Content related to the sale or promotion of firearms or weapons.
* **Tobacco**: Promotion or sale of tobacco products and other similar products, including cannabis, Delta-9, and CBD.

Carriers enforce strict guidelines to prevent such content from being transmitted over their networks to protect consumers from spam and potentially harmful messages. Violations can result in message filtering, fines, or suspension of messaging services.

It's crucial that you understand and adhere to these content restrictions to maintain compliance and ensure successful message delivery. This may mean that some academic programs, such as Cannabis Business or Cannabis Cultivation, may not be promoted via SMS.

![](https://downloads.intercomcdn.com/i/o/1075224342/3db7c32dae2370a098472d38/Pro+Tip+-+Orng.png?expires=1784430000&signature=0c8fa83a101e37f18aa4ae3cd50282a6268046b58d5f16f60cc31a5b5ef9d9a7&req=dSAgE8t8mYJbW%2FMW3Hu4gdKuKYbMf9sfybW4f%2FXSpyilWwgWsNE%2FHrNpK9%2F%2B%0ACA%3D%3D%0A) Keep your SMS campaigns compliant and engaging by **segmenting** students based on their interests + data. Sending personalized, relevant messages not only boosts engagement but also helps ensure you’re reaching the right audience without risking spam complaints. [Learn more about Segments](https://help.element451.com/en/collections/124543-segments).

---

# AI SHAFT Content Review

Bolt AI, Element451's AI platform, automatically evaluates outbound SMS messages in Conversations for potential spam, possible phishing attempts, or [SHAFT](#h_017dc23592) content before sending.

If a message is identified as potentially containing SHAFT content, it is blocked to protect you and Element451 from restrictions imposed by carriers. In these cases, a warning icon will appear, letting you know the message cannot be sent. If the message is deemed compliant, it is sent as usual.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1387625465/f180cf5e5701e1a8d47169ebddff/CleanShot+2025-02-19+at+11_28_21.png?expires=1784333700&signature=7b0cad652e167bd924bc063b8960e21a02261ca142692753991d0b97083e4d8d&req=dSMvEc98mIVZXPMW1HO4zVsP5RMIbVNaXN5s1MUR9%2F5uOr977ZAwauvxYHVp%0A3GDGpiAffsPXD7wAWMc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1387625465/f180cf5e5701e1a8d47169ebddff/CleanShot+2025-02-19+at+11_28_21.png?expires=1784333700&signature=7b0cad652e167bd924bc063b8960e21a02261ca142692753991d0b97083e4d8d&req=dSMvEc98mIVZXPMW1HO4zVsP5RMIbVNaXN5s1MUR9%2F5uOr977ZAwauvxYHVp%0A3GDGpiAffsPXD7wAWMc%3D%0A)

---