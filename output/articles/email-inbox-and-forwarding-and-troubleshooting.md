---
title: Email Inbox and Forwarding and Troubleshooting
url: https://help.element451.com/en/articles/8663239-email-inbox-and-forwarding-and-troubleshooting
collection: Conversations
---

Common issues and solutions when configuring and using shared inboxes and email forwarding.

# Overview

This article provides solutions and best practices for common issues partners experience when configuring and using connected email inboxes in Conversations.

Below, you will find a list of common issues and how to troubleshoot them:

---

# Inbox Forwarding + Setup

## The "Test Forwarding" button is spinning

​**Issue**: After connecting and configuring an email account, I am performing a forwarding test, but the button remains in a spinning state.

​**Solution**: The spinning button indicates our system is awaiting the forwarded email. If it persists, there might be a configuration issue.

* Review your email client's policies regarding forwarding to external/remote domains. There may be policies/rules preventing Element451 from receiving the test email. Navigate to your email client settings to double-check your configuration and investigate any potential policies blocking the forward. Then, retry the test.
* If unsure how to check your email policies/rules, consult your IT department or refer to your email provider's help center for assistance.

**Using Outlook?** Check out our [guide to troubleshooting](https://help.element451.com/en/articles/8663239-email-inbox-and-forwarding-and-troubleshooting#3:%20Spinning%20Button%20When%20Testing%20%20Issue:%20After%20connecting%20and%20configuring%20an%20email%20account,%20I%20am%20performing%20a%20forwarding%20test,%20but%20the%20button%20remains%20in%20a%20spinning%20state.%20%20%20%20%20Solution:%20The%20spinning%20button%20indicates%20our%20system%20is%20awaiting%20the%20forwarded%20email.%20If%20it%20persists,%20there%20might%20be%20a%20configuration%20issue.%20Review%20your%20email%20client's%20policies%20regarding%20forwarding%20to%20external/remote%20domains.%20It's%20possible%20there%20are%20policies/rules%20preventing%20Element451%20from%20receiving%20the%20test%20email.%20Return%20to%20your%20email%20client%20settings%20to%20double-check%20your%20configuration%20and%20investigate%20any%20potential%20policies%20blocking%20the%20forward.%20Then,%20retry%20the%20test.%20If%20unsure%20of%20how%20to%20check%20your%20email%20policies/rules,%20consult%20your%20IT%20department%20or%20refer%20to%20your%20email%20provider's%20help%20center%20for%20assistance.) forwarding inboxes to Element451 from Outlook for a list of configuration checks and solutions.

## Unable to confirm email inbox

​**Issue:** I've set up the forwarding according to the instructions, but I'm unable to confirm the inbox.

​**Solution**: Sometimes, your organization's email settings include a rule preventing email forwarding to external organizations, including @element451.com. To confirm this, contact your organization's IT support and see if there is such a rule in place and if there is a way to whitelist the Element451 domain. Search for the term 'forwarding' in your inbox and look for an email from Outlook that contains something similar to this:  
​

[![](https://downloads.intercomcdn.com/i/o/1183090891/5191a35f059f194b9d95c813/Unable%2Bto%2Bconfirm%2Binbox.png?expires=1784333700&signature=39b14e923b48ec417d3bb902dd3e52821fb1e694575c9be0407cd9b78500215e&req=dSEvFcl3nYlWWPMW1HO4zfCtKMJZB2IjNiKtDzax%2BEV6zklUDWEkjf5PE6YN%0A97rYpOhLI00oAju8Y%2FE%3D%0A)](https://downloads.intercomcdn.com/i/o/1183090891/5191a35f059f194b9d95c813/Unable%2Bto%2Bconfirm%2Binbox.png?expires=1784333700&signature=39b14e923b48ec417d3bb902dd3e52821fb1e694575c9be0407cd9b78500215e&req=dSEvFcl3nYlWWPMW1HO4zfCtKMJZB2IjNiKtDzax%2BEV6zklUDWEkjf5PE6YN%0A97rYpOhLI00oAju8Y%2FE%3D%0A)

---

#

## Troubleshooting Outlook forwarding

When connecting your Outlook inbox to Element451 using email forwarding, you may encounter issues due to Microsoft 365 security policies. This guide will help you troubleshoot and resolve common problems.  
​

[Explore Help Article →](https://help.element451.com/en/articles/9876273-troubleshooting-outlook-to-element451-email-forwarding)

#

---

# Email Display + Threading

## Emails are missing from Element451

**Issue:** I have connected and configured my email account, but only some of my emails appear in my Element451 inbox.

**Solution**: Only emails matching existing records in Element451 will be forwarded to Conversations and attached to student records **unless you enable the anonymous conversations setting**.

* **Default Behavior**: When you add an inbox to Element451, emails sent to your connected custom address will be forwarded to Element451. We will then search for a match to an existing person record (student) in Element451. If we find a match, a threaded conversation will be created. However, if no match is found, we will exclude/not retain that email. This means only emails sent to you from an email address associated with a user’s record in your Element451 instance will be displayed in your inbox.
* **Anonymous Conversations**: You can enable *anonymous conversations* to allow your Element451 inbox to receive messages from *unknown* numbers and email addresses. This feature enhances communication flexibility by allowing messages from new or prospective contacts to reach you directly.  
  ​

  [Explore More: Anonymous Convos →](https://help.element451.com/en/articles/9688991-anonymous-conversations)

## Blank "FW" email/SMS

​**Issue**: An external user (student) is receiving blank emails and/or SMS messages that start with "FW:" like the example below:  
​

[![](https://downloads.intercomcdn.com/i/o/1183088754/e6e3ec445de4c713d0c0ab99/Forwarding%2BIssue.png?expires=1784333700&signature=bf8b79c1e5cca79e19dee625eba4c8aa02d9cf7742ef6a9e77dded4b06897b39&req=dSEvFcl2lYZaXfMW1HO4zS2rsIoAybqEVRIO2m%2B0n8Lo4EIe7rn1jNsFWOOq%0ALfQLZXkUvPP4ZNsuW9E%3D%0A)](https://downloads.intercomcdn.com/i/o/1183088754/e6e3ec445de4c713d0c0ab99/Forwarding%2BIssue.png?expires=1784333700&signature=bf8b79c1e5cca79e19dee625eba4c8aa02d9cf7742ef6a9e77dded4b06897b39&req=dSEvFcl2lYZaXfMW1HO4zS2rsIoAybqEVRIO2m%2B0n8Lo4EIe7rn1jNsFWOOq%0ALfQLZXkUvPP4ZNsuW9E%3D%0A)

​**Solution**: This is likely the result of forwarding emails to an email address you have configured as an inbox in Element451. Do not forward emails between addresses set up as connected inboxes. This will result in our system thinking the forwarded message is a reply and will be sent to the student. We will talk more in-depth about this [below](https://help.element451.com/en/articles/8663239-email-inbox-and-forwarding-and-troubleshooting#h_2e75d855be).

#

## Email replies creating separate threads

When a student replies to an email sent from Element451, their response should be threaded into the original conversation (if you have email forwarding correctly configured).

However, if a staff member replies from their personal email (e.g., Gmail or Outlook) instead of responding directly within Element451, Element451 has no way of tracking that message. This can cause unexpected behavior, such as replies creating separate threads.

We recommend always replying to emails from Element451. This way, when email forwarding is correctly configured, the student’s response will be added to the original thread.

---

# Other Important Topics

## Avoid forwarding autoresponder emails to connected inboxes

When using connected inboxes in Element451, it’s important to avoid forwarding **conversation autoresponder emails** (e.g., “You’ve received a new message!”) to an internal email address that is also set up as a connected inbox. Doing so can unintentionally link unrelated messages to existing conversations.

* **What is a conversation autoresponder?** When a conversation assignee or participant receives a new inbound email message, they will receive an automatic notification email from [notifications@element451.io](mailto:notifications@element451.io) with the subject line "You've received a new message!"

## Understanding Forwarding in Two Contexts

For this topic, it's important to understand the two different types of "forwarding" that are involved in this topic:

1. **Inbox Forwarding (Configured in Element451 + Gmail/Outlook)** – This is how Element451 receives inbound emails. When a connected inbox is set up, emails sent to that address are automatically forwarded to Element451.
2. **Manual Forwarding of Autoresponder Emails** – This occurs when an internal user manually forwards an automatic system email (such as a “new message” notification) to another internal user.

## Why This Can Cause Issues

Let’s look at an example:

* Your general admissions email address (let's say [admissions@element.edu](mailto:admissions@element.edu)) is set up as a connected inbox in Element451, meaning all emails sent to the group email address are automatically forwarded to Element.
* An admissions counselor, Tom, receives an autoresponder email from Element451 saying, “You’ve received a message!” because a student, Sarah, replied to his conversation in Element451.
* Tom is on vacation, so he manually forwards that autoresponder email to the admissions email, asking for someone to please assist Sarah in his absence.
* Since the admissions email address is a connected inbox, Gmail automatically forwards Tom's forwarded email to Element451, just as it does with all incoming emails.

Now, here’s the problem:

* That autoresponder email contains a conversation ID that ties it to Tom + Sarah's original message.
* When Element451 receives the forwarded autoresponder, it will mistakenly identify it as a response to Sarah's conversation and attach it to the existing thread—potentially causing confusion.

  + ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1368989978/1e2bc8247d7a96983bcfa886e5aa/Important.png?expires=1784430000&signature=e78a990f95aad32ad6d71185feb6bceeea771cbac75f7f7fa0c1baae66aef69e&req=dSMhHsB2lIhYUfMW3Hu4gcW4OjdV%2BTYF69Fo9Pwp1dBib%2BIV4PMwDBJUKHW9%0A6w%3D%3D%0A) This means the student/contact will also get notified because it will be recognized as a new reply to that conversation.

## Best Practice

To avoid this issue, never manually forward autoresponder emails to a connected inbox. Instead, if someone needs help responding to a message, they should:

* Communicate internally about a conversation.
* We recommend adding a **private note** to the conversation thread and **mentioning** the other internal user or team. To use the mentioned feature, type the "@" symbol and select a user or team (as demonstrated in the image below). The mentioned user/team will receive an email notification.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1368991122/871eae918e862dde911145628efd/Screenshot-2B2024-07-24-2Bat-2B9_40_12-E2-80-AFAM.png?expires=1784333700&signature=19ff8eb4cb339c0d6182c21a74d2341056c0536e7a63dc20f955f9232742834a&req=dSMhHsB3nIBdW%2FMW1HO4ze5%2BrEEHp%2BhMxlyQPaDnaTVnVwHM71w0htKG05mW%0AxqZp%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1368991122/871eae918e862dde911145628efd/Screenshot-2B2024-07-24-2Bat-2B9_40_12-E2-80-AFAM.png?expires=1784333700&signature=19ff8eb4cb339c0d6182c21a74d2341056c0536e7a63dc20f955f9232742834a&req=dSMhHsB3nIBdW%2FMW1HO4ze5%2BrEEHp%2BhMxlyQPaDnaTVnVwHM71w0htKG05mW%0AxqZp%0A)

## Can I respond to replies from my email client (Gmail or Outlook) if the message was sent from Element451?

Technically, you can, but it’s **not recommended.** Element451 can only track emails sent through its platform. If you reply from your email client (e.g., Gmail or Outlook), Element451 won’t know the message was sent. It may also cause conversation threads to duplicate if the student replies again.

#

---