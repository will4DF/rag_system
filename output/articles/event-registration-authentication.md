---
title: Event Registration Authentication
url: https://help.element451.com/en/articles/13797957-event-registration-authentication
collection: Events
---

Add optional authentication steps to your event sign-up forms.

# Overview

You can optionally control how users authenticate when registering for an event. These settings allow you to either limit registration to known contacts or verify that the correct person is submitting the form before data is saved.

You may choose to:

* Require Login
* Require Email Verification
* Leave both disabled and not require any verification or authentication

**📌 Note:** ***Require Login*** and ***Email Verification*** cannot be used together. Enabling one will automatically disable the other.

## Accessing Event Authentication Settings

Authentication settings are configured at the **Event level**.

1. Navigate to **Engagement > Events**.
2. **Edit the desired event**.
3. Click the **Sign-Ups** tab.
4. From the left-hand menu, select **Authentication**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097215082/80777c58a3e9e4c0b613b6fbcc25/CleanShot-2B2026-02-23-2Bat-2B16_12_27-402x.png?expires=1784333700&signature=12a46a341ff46a0fabc011f0b504364b6e5ad8d8004c4ea69c6f8d173552e0d7&req=diAuEct%2FmIFXW%2FMW1HO4zTfloGgS%2F%2BVLbrWDUhnj7LAkQO2rkj9mwmH2jGC9%0AdvkrKJpkvB6eK10iMhU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097215082/80777c58a3e9e4c0b613b6fbcc25/CleanShot-2B2026-02-23-2Bat-2B16_12_27-402x.png?expires=1784333700&signature=12a46a341ff46a0fabc011f0b504364b6e5ad8d8004c4ea69c6f8d173552e0d7&req=diAuEct%2FmIFXW%2FMW1HO4zTfloGgS%2F%2BVLbrWDUhnj7LAkQO2rkj9mwmH2jGC9%0AdvkrKJpkvB6eK10iMhU%3D%0A)

---

# Require Login

**Require Login verifies an existing contact's identity before allowing registration to continue.** When enabled, a contact must sign in before they can register for the event. ***This limits registration to contacts who already have an Element451 account.***

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097204777/1547cd1095015f7fa0762ee230df/CleanShot+2026-02-23+at+16_16_28%402x.png?expires=1784333700&signature=824c5031dcd86d6984e3c9a156e63f8f3340ad1096f0ad191d842cb06e1eab8d&req=diAuEct%2BmYZYXvMW1HO4zWlFjXIvFlcB142uFLmqYq5E6pgp5QctyRGfMiNE%0Ax5brXhG9fHNC%2FevvkuM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097204777/1547cd1095015f7fa0762ee230df/CleanShot+2026-02-23+at+16_16_28%402x.png?expires=1784333700&signature=824c5031dcd86d6984e3c9a156e63f8f3340ad1096f0ad191d842cb06e1eab8d&req=diAuEct%2BmYZYXvMW1HO4zWlFjXIvFlcB142uFLmqYq5E6pgp5QctyRGfMiNE%0Ax5brXhG9fHNC%2FevvkuM%3D%0A)

If **Require Login** is turned on:

* New contacts cannot be created through this event
* Only authenticated, known users may complete registration
* Sign-up forms are pre-populated with key user data like name, email address. This data is locked and will not update as part of the event registration.
* Once authenticated, users can use the Update Profile option to update otherwise locked fields.

The login experience is part of our **Universal Login**, which provides a consistent sign-in experience across Event Sites, Application Sites, Appointment Booking Sites, and StudentHub.

Depending on your institution’s configuration, users may sign in using:

* Element username and password
* Institutional SSO
* Google authentication
* Magic Link (one-click login link sent to their email)

Login methods are controlled in your [system settings](https://help.element451.com/en/articles/8569773-security-authentication-settings) and can be enabled or disabled based on your institution’s preferences.  
​

***Require Login* is best for:**

* Current student events
* Orientation or admitted student programming
* Internal or invite-only experiences

**Since new users can't be created *Require Login* Not recommended for:**

* Unrestricted public events
* Top of the funnel admissions events like campus tours, visits or open houses
* Other Inquiry-generating events where new contacts are expected

---

# Require Email Verification

While Require Login verifies an existing user’s identity before allowing registration to continue, **Email Verification ensures the right person is submitting the form before any data is saved to their record.**  
​

Unlike Require Login, **new contacts can still be created** when Email Verification is used.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097209578/e20f9d501f6e578ca61122d7f3b3/CleanShot+2026-02-23+at+16_18_36%402x.png?expires=1784333700&signature=07f169847ae38eafa34ad1bba2247514a1c260d57ec800d1883becb277253b0a&req=diAuEct%2BlIRYUfMW1HO4zWPaOdABMmnVgYLwcnML4M7RuzjVvoxkKRF1U6%2FS%0AtyPswG2J6ZfUUsIDqbE%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097209578/e20f9d501f6e578ca61122d7f3b3/CleanShot+2026-02-23+at+16_18_36%402x.png?expires=1784333700&signature=07f169847ae38eafa34ad1bba2247514a1c260d57ec800d1883becb277253b0a&req=diAuEct%2BlIRYUfMW1HO4zWPaOdABMmnVgYLwcnML4M7RuzjVvoxkKRF1U6%2FS%0AtyPswG2J6ZfUUsIDqbE%3D%0A)

This feature is especially helpful when shared email addresses (e.g., family or generic inboxes) are used during registration. Without verification, one contact’s submission could overwrite an existing record in Element451 based solely on email matching.  
​

When enabled, users must verify ownership of the email address entered on the registration form before their registration is processed.

### Email Verification Settings (Always | On Conflict)

After toggling on **Use Email Verification**, you can choose the verification behavior:

* **Always:** Every registration requires email verification, regardless of whether a contact using that email address already exists.  
  ​  
  A verification code is sent to the email provided, and the user must enter that code before the registration is completed.  
  ​  
  This option provides the highest level of data protection and ensures the person submitting the registration has access to the email address entered.
* **On Conflict:** Verification is only triggered if the email already exists in Element451 **and** one or more of the following fields do not match the existing record:

  + First Name
  + Middle Name
  + Last Name
  + SSN
  + Date of Birth
  + Phone Numbers

    💡 **Pro Tip:** Use **On Conflict** to reduce friction for new prospects while still safeguarding existing data from being overwritten.

---

# 🧠 Good to Know

Email Verification and Require Login cannot be used together within the same event, each serves a different purpose. You can use both features strategically across different events:

* Use **Require Login** when event registrations must be tied to known contacts only.
* Use **Email Verification** when accepting registrations from both new and existing contacts, but you want to safeguard against overwriting data.

---