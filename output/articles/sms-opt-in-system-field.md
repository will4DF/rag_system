---
title: SMS Opt-In System Field
url: https://help.element451.com/en/articles/9007065-sms-opt-in-system-field
collection: Campaigns
---

Learn how to use the recommended system field for SMS opt-in effectively to ensure trust and compliance.

# Overview

Effective SMS communication starts with consent. At Element451, we stress the importance of securing a student's opt-in to uphold trust and [meet regulatory standards](https://help.element451.com/en/articles/8390046-understanding-sms-regulations-a2p-10dlc). Without this consent, messages risk being marked as spam, damaging your institution's reputation and trust score with carriers.

By leveraging the **`user-sms-updates`** field, you ensure your messaging practices are not only compliant but also respected and welcomed by students and other contacts, safeguarding your ability to engage effectively.

❗Important: These system fields **do not** automatically block SMS messages to students who haven't opted in. You are responsible for respecting and honoring students' opt-in preferences. By carefully segmenting your audience according to these fields, you ensure compliance with SMS marketing laws and maintain your students' trust.

Here's how you can effectively use the recommended system field:

---

# System Field Explained (`user-sms-updates`)

The **`user-sms-updates`** field is universally applicable across forms, events, applications, etc., reflecting a student's opt-in status for SMS communications across their entire record. When a student opts into SMS updates through any interaction point, this field is set to true, indicating their consent to receive SMS messages.

---

# Segmenting with SMS Opt-In System Field

To ensure that you only send SMS messages to students who have explicitly opted in, using a filter to segment your audience based on their opt-in value is essential. As a reminder, Element451 **does** **not** **automatically** **remove** **students** **without an opt-in value on their record** when sending SMS communications.

To avoid sending messages to those students who haven't opted in, you should use the following filter when creating a Segment:

[![](https://downloads.intercomcdn.com/i/o/976007686/dfcca7d42e64c79304a637f3/smsupdates.png?expires=1784333700&signature=3082044baa9ba74eace41467f1f2635ca3c50efaf85e2d347d4cbcef9b3cec1d&req=fSchFsl5m4lZFb4f3HP0gEB%2FnV3VXHehTDB%2BiaykHxHhS1g5%2ByoCi%2F1bc2ju%0Al0yzNJe90hTnqYnB%2FQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976007686/dfcca7d42e64c79304a637f3/smsupdates.png?expires=1784333700&signature=3082044baa9ba74eace41467f1f2635ca3c50efaf85e2d347d4cbcef9b3cec1d&req=fSchFsl5m4lZFb4f3HP0gEB%2FnV3VXHehTDB%2BiaykHxHhS1g5%2ByoCi%2F1bc2ju%0Al0yzNJe90hTnqYnB%2FQ%3D%3D%0A)

---

# Best Practice: Checking SMS Opt-In Status in Workflows/Rules

When sending SMS campaigns via workflows or rules, it’s best practice to include a condition to verify if the student is still opted in before each SMS step.

This is particularly important if your workflow includes delays, as students can remove their opt-in status at any time, like when completing a form that updates the SMS Opt-In field. If a student opts out during that delay, your workflow could still send a message.

---

# What about **`user-application-sms-updates`?**

While **`user-application-sms-updates`** exists, it is scoped specifically to applications and presents limitations due to its narrow scope. Institutions that completed implementation before late 2023 might still be using this field. However, we strongly recommend updating any applications or processes to utilize **`user-sms-updates`** instead. This shift will streamline your SMS opt-in process, ensuring a consistent and compliant approach to student communication.

---