---
title: Email: Unsubscribe/Opt-Out + Federal Regulations
url: https://help.element451.com/en/articles/2608500-email-unsubscribe-opt-out-federal-regulations
collection: Campaigns
---

Learn how to integrate unsubscribe options in emails using Element451, ensuring compliance with the CAN-SPAM Act for trust and legality.

# Overview

Managing subscriber preferences effectively is crucial to maintaining trust and compliance in digital communication. This guide provides detailed instructions on integrating an unsubscribe option in your email campaigns using Element451. We'll explore both the use of pre-made footer blocks available within the platform and the steps to create a custom unsubscribe link or button manually.

Including an opt-out option in your communications is legally required under the CAN-SPAM Act. An option to opt out from receiving your marketing emails must be clear and straightforward for recipients. For more detailed information, review the [FTC CAN-SPAM Act Compliance Guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business).

---

# Transactional vs. Marketing Messages

Under the **CAN-SPAM Act**, bulk email communications fall into two categories: Marketing (Promotional) Messages and Transactional Messages. When configuring email communication in Element451, you can set the Communication Priority to either Marketing or Transactional to ensure proper handling and compliance.  
​  
While respecting a contact’s opt-out preferences is essential, CAN-SPAM provides more flexibility for Transactional Messages, allowing them to be sent even if a recipient has unsubscribed.

Use the collapsable sections below to review the differences between transactional and marketing communication priorities:

## Transactional Messages

Transactional emails provide essential updates, confirmations, or notifications about a student’s account, application, or activities. A specific student action usually triggers these messages, and they are not promotional in nature.

* **Highlights**

  + They do not require opt-in consent.
  + They can be sent even if a recipient has unsubscribed.

    - CAN-SPAM allows these messages to bypass email unsubscribe settings, but the best practice is to ensure they are truly transactional.
    - This contrasts with the TPCA, which does not allow for any SMS messages (transactional, marketing, or one-on-one conversation messages) to be sent to contacts who have opted out. [Read more about SMS unsubscribes here](https://help.element451.com/en/articles/8390046-sms-opting-in-and-out-understanding-us-regulations).
  + They are usually one-time notifications, not part of an ongoing campaign.
* **Examples**

  + Application Submission Confirmation
  + Event Registration Confirmation
  + Financial Aid Award Notice
  + Password Reset Request

## Marketing Messages

Marketing emails are designed to promote programs, events, or opportunities and are often part of a broader outreach campaign. Unlike transactional emails, these cannot be sent to unsubscribed contacts.

* **Highlights**

  + They require prior opt-in consent and must honor unsubscribe preferences.
  + They are typically part of ongoing engagement efforts/campaigns.
  + ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374156301/7bab87e7e57bbd94cf8423d7e848/Important.png?expires=1784430000&signature=036b8b01c06e045afe1993b6a637d41c075c445c9bb643b097ceb0e7b2cf9a73&req=dSMgEsh7m4JfWPMW3Hu4gXrR%2BWzU%2BLnx1e4M%2BEKF8yGj17fKtHtL64LVb5hQ%0AJA%3D%3D%0A) Sending Marketing emails incorrectly labeled as Transactional can violate CAN-SPAM, increase spam complaints, and damage your sender reputation.
* **Examples**

  + Application Deadline Reminder
  + Open House/Preview Day Invitation
  + Scholarship Opportunity Email
  + RFI Follow-Up Campaign

## Which One to Use?

* If your message is purely informational, triggered by a student action, or they explicitly requested the information, it is **transactional** and does **not** require opt-in consent (but it's highly recommended).
* If your message promotes engagement, enrollment, or an event, it is **marketing** and **requires** opt-in consent.

---

# Unsubscribing (Opting Out)

Unsubscribing is when contacts revoke their consent and no longer wish to receive email messages from your institution.

## Unsubscribe Options + Adding Option to Emails

There are two different methods to add an unsubscribe link to your email Campaigns. Use the collapsable sections below to explore the methods:

## Add Unsubscribe via Footer Block

Element451 simplifies the inclusion of an unsubscribe link in your email communications through its pre-designed footer blocks, available in the Campaigns module. Each footer block features a built-in unsubscribe text link, which is directly tied to a unique unsubscribe token for each recipient.

### How It Works

* Add a footer content block to your email. The unsubscribe link in the footer block is already configured with a personalized unsubscribe token.
* When a recipient clicks on this link, Element451 automatically records this action as an unsubscribe request in the recipient's [profile](https://help.element451.com/en/articles/1475735-the-person-profile) based on the token.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374161751/b0996ce273706a2f0d2e0f4b8144/unsubscribe.gif?expires=1784333700&signature=05587d9a76c044ce823b73fc0894b205a33fde3a94f853eacf3c563786fb348b&req=dSMgEsh4nIZaWPMW1HO4zVMMSPXXT052HytLBGXHHkzllMLnT9ApVWvns%2FPP%0AWG4098e7ZRYT5H6DYBo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374161751/b0996ce273706a2f0d2e0f4b8144/unsubscribe.gif?expires=1784333700&signature=05587d9a76c044ce823b73fc0894b205a33fde3a94f853eacf3c563786fb348b&req=dSMgEsh4nIZaWPMW1HO4zVMMSPXXT052HytLBGXHHkzllMLnT9ApVWvns%2FPP%0AWG4098e7ZRYT5H6DYBo%3D%0A)

## Add Unsubscribe via Link

For those who prefer a more tailored approach, creating a manual unsubscribe link allows for customization of the message and placement within your email layout.

### Steps to Create a Manual Unsubscribe Link

1. **Choose Your Text**: Decide on the text that recipients will click to unsubscribe—common choices include "Unsubscribe from this list" or "Click here to opt out."
2. **Insert the Link**: Highlight your chosen text and click the ‘insert link’ button in your email editor.
3. **Add the Unsubscribe Token**: In the URL field of the hyperlink, input **`[custom:unsubscribe]`** as the destination. This token will generate a unique link for each recipient.
4. **Save Your Changes**: Ensure that all edits are saved and your email is ready to send with the new unsubscribe link in place.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374162836/44c6afa9d98f69c1a01db411dc40/unsubcribe.gif?expires=1784333700&signature=0872cccd556619d0442b619dc2f003ed0d38bd13ab79b229915bdffa01f61e75&req=dSMgEsh4n4lcX%2FMW1HO4zSsh07h4zOqtDA7u46T0Bd0JQXlwx7v4AVbFnlaS%0AnWacPW5fXKu6O2fZGKU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374162836/44c6afa9d98f69c1a01db411dc40/unsubcribe.gif?expires=1784333700&signature=0872cccd556619d0442b619dc2f003ed0d38bd13ab79b229915bdffa01f61e75&req=dSMgEsh4n4lcX%2FMW1HO4zSsh07h4zOqtDA7u46T0Bd0JQXlwx7v4AVbFnlaS%0AnWacPW5fXKu6O2fZGKU%3D%0A)

## Unsubscribe by Internal User

You have the option to unsubscribe a contact manually from the dashboard. This is particularly helpful if a contact calls or emails asking to be unsubscribed. To learn more about this process, explore our help article, [Email + SMS: Manually Unsubscribe Contacts](https://intercom.help/element451/en/articles/6066486-manually-unsubscribe-a-user-from-email-sms-communication).

[Explore More: Manually Unsubscribe →](https://help.element451.com/en/articles/6066486-email-and-sms-manual-unsubscribe)

## The Process of Unsubscribing (Milestone)

* When a person unsubscribes, the **`Email Unsubscribe Date`** [milestone](https://help.element451.com/en/articles/3419189-milestones) is added to that contact's profile. That milestone contains an associated email address. We only unsubscribe that single email address. This means:

  + Each email address must be unsubscribed independently.
  + An email address that has unsubscribed will stop receiving emails, even if included as a secondary recipient (e.g., CC or BCC).

    - For instance, if a parent’s email linked to a guardian token is unsubscribed, that email address will not receive any further emails. However, this does not impact the subscription status of the student’s own email address, which remains subscribed unless explicitly unsubscribed.
* Following this, they will no longer receive **marketing** email messages from you. The system automatically prevents this from happening, therefore, there is no action required on your end.
* Messages with the **Transactional** priority will still be sent to the contact regardless of whether they have an unsubscribed milestone.

  Element451 manages unsubscribes at the individual email address level, ensuring precise control over communication preferences. Below, we provide a comprehensive explanation of how unsubscribes are processed across different email contexts in the platform.

  ###

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1374292367/a22ae026f211bc8bbd1c5cee81b5/Pro+Tip.png?expires=1784430000&signature=c641972cddcb41036520e9f3ef81903ae6814512b70a089cca75097c479fb84d&req=dSMgEst3n4JZXvMW3Hu4gVbAbCBdGLkUdzlQvTd9v78L0C2s1EkG%2BIs5%2B94T%0Akw%3D%3D%0A) It is best practice to add a label to the contact's profile when they unsubscribe, as it provides an at-a-glance indicator. You can automate this process by creating a rule that is initiated by the 'joined segment' trigger.

---