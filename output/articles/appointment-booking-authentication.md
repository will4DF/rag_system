---
title: Appointment Booking Authentication
url: https://help.element451.com/en/articles/13798820-appointment-booking-authentication
collection: Appointments
---

Add optional authentication steps to your booking forms.

# Overview

You can optionally control how users authenticate when booking an appointment. These settings allow you to either limit registration to known contacts or verify that the correct person is submitting the form before data is saved.

You may choose to:

* Require Login
* Require Email Verification
* Leave both disabled and not require any verification or authentication

**📌 Note:** ***Require Login*** and ***Email Verification*** cannot be used together. Enabling one will automatically disable the other.

## Accessing Appointment Authentication Settings

Authentication settings are configured at the **Appointment Type level**, and can be optionally adjusted at the individual **Availability level**.

### "Type" Level

1. Navigate to **Engagement** > **Appointments**.
2. Click the **three vertical dots** (⋮) menu.
3. Select **Types** from the dropdown.
4. Choose the **Appointment Type** you want to enable authentication for.
5. Locate the **Authentication** card.

### "Availability" Level

To optionally adjust at the Availability level:

1. Navigate to **Engagement** > **Appointments**.
2. Click the **three vertical dots** (⋮) menu.
3. Select **Types** from the dropdown.
4. Choose the **Appointment Type** you want to enable authentication for.
5. Locate the **Authentication** card.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097139732/4ecc96e9ff9f0d5baf0df12fc0fe/CleanShot-2B2026-02-23-2Bat-2B15_47_45-402x.png?expires=1784333700&signature=671d8e6163ffab49863f5ba95819107720a41343eaded3560b76c124f462d557&req=diAuEch9lIZcW%2FMW1HO4zY%2BzVO51AwBS7n%2FGqafiDtqdvKpBN%2F9AMonpUbcq%0A0AccjOeg4bHMohBY25c%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097139732/4ecc96e9ff9f0d5baf0df12fc0fe/CleanShot-2B2026-02-23-2Bat-2B15_47_45-402x.png?expires=1784333700&signature=671d8e6163ffab49863f5ba95819107720a41343eaded3560b76c124f462d557&req=diAuEch9lIZcW%2FMW1HO4zY%2BzVO51AwBS7n%2FGqafiDtqdvKpBN%2F9AMonpUbcq%0A0AccjOeg4bHMohBY25c%3D%0A)

---

# Require Login

**Require Login verifies an existing contact's identity before allowing booking to continue.** When enabled, a contact must sign in before they can book the appointment. ***This limits booking to contacts who already have an Element451 account.***

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097167954/4e4608fa3903ba2e9608a0cf6887/CleanShot+2026-02-23+at+16_01_31%402x.png?expires=1784333700&signature=bdc770101dc988affeee3a540037d3d268d062b9121e32a04346530c0f75559e&req=diAuEch4mohaXfMW1HO4zbOmcetrPJC1ORDwUwUs908%2FFJcLUUHZGLhj%2BnrZ%0ApLklmckctKCvkq83Mvk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097167954/4e4608fa3903ba2e9608a0cf6887/CleanShot+2026-02-23+at+16_01_31%402x.png?expires=1784333700&signature=bdc770101dc988affeee3a540037d3d268d062b9121e32a04346530c0f75559e&req=diAuEch4mohaXfMW1HO4zbOmcetrPJC1ORDwUwUs908%2FFJcLUUHZGLhj%2BnrZ%0ApLklmckctKCvkq83Mvk%3D%0A)

If **Require Login** is turned on:

* New contacts cannot be created through this booking
* Only authenticated, known users may complete booking
* Booking forms are pre-populated with key user data like name, email address. This data is locked and will not update as part of the appointment booking.
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

* Current student appointments, like advising and student life related appointments.
* Later funnel appointments for applications like interviews or FinAid counseling.

**Since new users can't be created *Require Login* Not recommended for:**

* Unrestricted public bookings
* Top of the funnel admissions appointments like personalized visits
* Other Inquiry-generating appointments where new contacts are expected

---

# Require Email Verification

While Require Login verifies an existing user’s identity before allowing booking to continue, **Email Verification ensures the right person is submitting the form before any data is saved to their record.**  
​

Unlike Require Login, **new contacts can still be created** when Email Verification is used.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097174494/e79797e28f2a138ef2bdea1f894b/CleanShot+2026-02-23+at+16_04_30%402x.png?expires=1784333700&signature=203892d07d5f18f0e83c56d322b158876c7612a0f20cd0095e77f7f70420e75d&req=diAuEch5mYVWXfMW1HO4zfblqb3%2B3ktlW0mrYF6GTh4WaUb9zC0J9eV7%2FYew%0AvC5ACbO%2FGU3WQQloF8s%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2097174494/e79797e28f2a138ef2bdea1f894b/CleanShot+2026-02-23+at+16_04_30%402x.png?expires=1784333700&signature=203892d07d5f18f0e83c56d322b158876c7612a0f20cd0095e77f7f70420e75d&req=diAuEch5mYVWXfMW1HO4zfblqb3%2B3ktlW0mrYF6GTh4WaUb9zC0J9eV7%2FYew%0AvC5ACbO%2FGU3WQQloF8s%3D%0A)

This feature is especially helpful when shared email addresses (e.g., family or generic inboxes) are used during booking. Without verification, one contact’s submission could overwrite an existing record in Element451 based solely on email matching.  
​

When enabled, users must verify ownership of the email address entered on the registration form before their booking is processed.

## Email Verification Settings (Always | On Conflict)

After toggling on **Use Email Verification**, you can choose the verification behavior:

* **Always:** Every booking requires email verification, regardless of whether a contact using that email address already exists in Element451 or not.

  + A verification code is sent to the email provided, and the user must enter that code before the registration is completed.
  + This option provides the highest level of data protection and ensures the person submitting the registration has access to the email address entered.
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

**Email Verification** and **Require Login** cannot be used together within the same availability, each serves a different purpose. You can use both features strategically across different events:

* Use **Require Login** when appointment bookings must be tied to known contacts only.
* Use **Email Verification** when accepting bookings from both new and existing contacts, but you want to safeguard against overwriting data.

---