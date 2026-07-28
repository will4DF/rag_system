---
title: 📌 Events: Frequently Asked Questions
url: https://help.element451.com/en/articles/9354041-events-frequently-asked-questions
collection: Events
---

This article answers commonly asked questions about Events, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389336139/e2cb510f1727a5fb4d92a105a5ef/Pardon+our+Progress.png?expires=1784333700&signature=e3548b912b8ae19c89a93516dfd2d2efab7a4b20318ddaac9814a23264c47a23&req=dSMvH8p9m4BcUPMW1HO4zXqVyWg0Sef888i2Uj9pFtXV2WheCatSBpt%2Bm4S%2B%0A1wOz365zCDKYMg6IrJY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389336139/e2cb510f1727a5fb4d92a105a5ef/Pardon+our+Progress.png?expires=1784333700&signature=e3548b912b8ae19c89a93516dfd2d2efab7a4b20318ddaac9814a23264c47a23&req=dSMvH8p9m4BcUPMW1HO4zXqVyWg0Sef888i2Uj9pFtXV2WheCatSBpt%2Bm4S%2B%0A1wOz365zCDKYMg6IrJY%3D%0A)

# General

#### How can I update the gradient color on my event page header?

Currently, the gradient in your event page header is set automatically based on your primary and secondary color choices. It is not possible to modify the gradient header at this time.

#### What is the recommended format and size of the event photo?

The image format must be .png or .jpeg and no larger than 5MB. Images should also be square (1:1 aspect ratio) larger than 368x368, with a recommended size of 500x500. Images that are too small or in other aspect ratios may cause unintended cropping.

#### Why does my Events Site load slowly?

For first-time loads, it may take slightly longer as the site is being cached. Once cached, subsequent loads should be much faster. Additionally, if you have events with many occurrences, like campus tours, it’s best to add them as **[repeatable](https://help.element451.com/en/articles/9094765-event-dates-occurrences#h_f761898924)** [events](https://help.element451.com/en/articles/9094765-event-dates-occurrences#h_f761898924) instead of individually. This approach significantly improves the site’s load time.

#### How can I manage and view events effectively on the events page?

When viewing your events list/table from Engagement > Events > All Events, you can sort the table by `Title` or `Start Date`. To sort, click the column header.

---

# Registration

#### Does Events support group registration (multiple people + same form)?

Event Registrations are designed to be processed individually. Multiple people must complete the form and payment separately if they want to attend.

#### Can I customize the 'Thank You Note' for different events?

The Thank You Note is displayed for **all** events and is not event-specific. Event-specific communication can be facilitated through Event Messages, such as confirmation and reminder emails and text messages, which can be customized when editing an event. [Explore more](https://help.element451.com/en/articles/8981854-event-settings-your-event-site#h_b37d9d39cc).

#### How can I understand discrepancies between a student’s activity card and events card, and where should I verify their current event registration status?

The activity feed records historical actions, so if a student was marked as attended and later changed to a no-show, both actions will still appear. However, the event registration always reflects the current status.

To verify a student’s event registration, we recommend:

* Viewing the **Events profile card** on the contact record for an at-a-glance view.
* Check the event’s **Attendees tab** to see all registrants and their current status.

#### How do I create an event signup form template?

To create a reusable event signup form template:

1. Go to the **Signup** tab of any event and build your form with all required fields.
2. Once the form is ready, contact Element451 customer support and request that the form be converted into a template. Be sure to include the event link in your message.
3. Once the form is converted, it will appear in the **Choose From Template** dropdown for future use. You can still edit the form—adding or removing fields—after applying it to an event.

#### Why is the registration button missing from a published event?

If there are multiple events with the same name, it could lead to conflicts that hide the registration button. Navigate to your event list and confirm that no other event shares the same name as the problematic event. If a duplicate exists, rename the events to make each title unique.

#### Can I import event attendee data into Element451?

No, not at this time.

---

# Payments

#### How would I collect guest payments on event registration?

You can use the [Calculated payment type](https://help.element451.com/en/articles/9071731-payment-types#h_2685d6f36d) to write a formula to include guest fees in the total payment amount. To do this, use the `user-events-guest-number` data field.

#### How can I filter attendees by payment status?

Use the Event (All Properties) filter in Contacts > People to build a segment of attendees for a specific event filtered by payment status. This is useful for targeting follow-ups to registrants with outstanding payments.

---

# Messaging + Notifications

#### Is the event payment reminder email customizable?

No, not at this time.

#### When sending a Campaign (one-time or ongoing) to promote event registration, the event token I'm using is not rendering unless the contact is already registered for an event. Why?

To use the event tokens in a Campaign (and not the messaging feature within the Events module), without a user's registration in context, you must provide the GUID of the specific event date in the token. Event tokens will not render for non-registrants without the guid. When emailing event **registrants**, we recommend using the [messaging feature within the Events module](https://help.element451.com/en/articles/6067308-tokens-for-events-messages).

---

# Events Site + Event Landing Pages

#### How does event search work on the Events Site?

Search uses relevance-based ranking. Event titles are weighted higher than descriptions, so keyword matches in the title appear before matches in the description only.

---

# Event Self Check-In

#### Do event self check-in links expire?

No, self check-in links **do not have an expiration time**. However, they are only made available at a designated check-in time, which you can configure for each event.

**Here’s how it works:**

* You set when check-in should be available (before or after the event start time).
* At that time, registrants receive an email with the check-in link.
* “Check-In” button also appears on the Event Details page in StudentHub.

While the links remain active, they are intended for use around the event’s check-in period.

---