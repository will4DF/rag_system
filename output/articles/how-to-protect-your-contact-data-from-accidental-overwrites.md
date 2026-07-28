---
title: How to Protect Your Contact Data from Accidental Overwrites
url: https://help.element451.com/en/articles/13920046-how-to-protect-your-contact-data-from-accidental-overwrites
collection: People
---

# Overview

Element451's power comes from a unified view of every student — one record that connects every interaction, informs every decision, and drives every Bolt Agent conversation. When that record is wrong, everything built on top of it is too. When a parent fills out a form on behalf of a student, when a counselor registers someone for an event using their own email, or when a simple typo matches an existing record — these moments can silently overwrite the contact data your team has spent months building.

Element451 offers a set of configurable tools to help you prevent accidental overwrites across Appointments, Events, and Forms.

This guide walks you through each option, where it's available, and how to set it up.

---

# Understanding the Problem

Element451 uses email as the primary identifier to match form submissions, event registrations, and appointment bookings to existing contact records. This works well in most cases—but it also means that in certain cases poeple can unintentionally overwrite information on that contact.

Common scenarios where this causes issues:

* **Siblings or family members share an email**, leading to repeated overwrites as each person interacts with your forms and events.
* **A counselor registers a student for an event** using their own email, which is associated with an influencer record in Element. The registration overwrites the counselor's record with the student's name and information.
* **A student makes a typo in their email** on a form submission, overwriting their correct email address.

These situations are especially common, where parents, counselors, and family members frequently interact with Element451 on behalf of students.

---

# Your Options at a Glance

Element451 gives you three levels of protection depending on your needs. Each option is designed for different scenarios, and you can mix and match across your forms, events, and appointments.

|  |  |  |
| --- | --- | --- |
| **Protection Level** | **Available For** | **What It Does** |
| **Email Verification** | Forms, Events, Appointments | Verifies the submitter owns the email address before data is written |
| **Require Login** | Events, Appointments | Forces the user to log in before registering or booking |
| **Authenticated Forms** | Forms | Requires the user to verify their identity against an existing record before accessing the form |

---

# Option 1: Email Verification

**Available for:** Forms, Event Registration, Appointment Booking

Email Verification adds a lightweight confirmation step before any data is written to the CRM. The person submitting must verify they own the email address they entered, ensuring that only the rightful owner of an email can create or update the associated contact record.

## How It Works

When enabled, the submitter receives a verification code at the email address they entered. They must enter the code to complete their submission. If they don't verify, no data is written — protecting the existing contact record from accidental changes.  
​  
During the verification process, if the email address is already associated with an Element451 account, the name linked to that email address and note that any updates submitted through the form—including name changes—will be applied to the existing record.  
​

If the person completing the form wishes to submit it for someone else (for example, to register for an event or book an appointment), they should start over and use a different email address.

### Verification Modes

You can choose from three modes depending on how much protection you need:

* **Never** (default) — No verification is required. Form data updates the matched record based on email, just as it always has.
* **Always** — Verification is required for every submission, regardless of whether a matching record already exists.
* **On Conflict** — Verification is triggered only when the submitted email matches an existing record *and* the submitted data conflicts with key fields: First Name, Middle Name, Last Name, SSN, Date of Birth, or Phone Numbers. This is a balanced option that avoids unnecessary friction for straightforward submissions while still catching potential overwrites.

## How to Enable It

**For Forms:**

1. Navigate to your Form's settings
2. Open the **Authentication & Verification** tab
3. Enable **Email Verification** and select your preferred mode

**For Events:**

1. Navigate to an individual Event's settings
2. Enable **Email Verification** and select your preferred mode

**For Appointments:**

1. Navigate to your Appointment Availability settings
2. Enable **Email Verification** and select your preferred mode

## When to Use It

* Public-facing inquiry forms, interest forms, and RFI forms where anonymous submissions are common
* Event registrations open to prospects and applicants who may not have an account yet
* Appointment booking for prospective students or external audiences

---

# Option 2: Require Login

**Available for:** Event Registration, Appointment Booking

Because Events and Appointments are hosted on dedicated sites, you have the additional option to require users to log in before they can register or book. This goes a step further than Email Verification by ensuring the person is fully authenticated — helping prevent both accidental overwrites and the creation of duplicate contact records.

## How It Works

When Require Login is enabled, users are prompted to sign in before completing their registration or booking. They can authenticate using any of the login methods your institution has enabled, including Element username and password, Institutional SSO, Google authentication, or Magic Link.

## How to Enable It

**For Events:**

1. Navigate to your Event's settings
2. Enable **Require Login**

**For Appointments:**

1. Navigate to your Appointment Availability settings
2. Enable **Require Login**

## When to Use It

* Events or appointments intended for current students who already have accounts
* Scenarios where you want to completely eliminate anonymous registrations
* High-stakes bookings (advising sessions, orientation, housing-related events) where data accuracy is critical

---

# **Mix and Match: Granular Control Across Events + Appointments**

One of the advantages of both Email Verification and Require Login is that they're configured at the **individual event** **level** and **individual appointment availability** level — not globally. This means you can tailor your approach based on your audience:

* Require Login for a current-student orientation event
* Use Email Verification (On Conflict) for a prospect open house
* Leave verification off entirely for a low-stakes info session

This flexibility lets you balance security with accessibility depending on the situation.

***Important:*** *Email Verification and Require Login cannot be used together on the same event or appointment. If you enable Email Verification, the Require Login option will not be available, and vice versa. Choose the option that best fits the audience for each event or appointment.*

---

# Option 3: Authenticated Forms

**Available for:** Forms

For forms where you need to ensure the submitter is a known contact in Element451 before they can even access the form, Authenticated Forms provides the strongest level of identity verification.

## How It Works

When a user accesses an Authenticated Form, they are prompted to verify their identity using a unique identifier — such as their Email ID, School Email, School ID, Primary User Email, or Contact Experience. After entering their identifier, they receive a verification code via email and must enter it to gain access to the form.

Because this process matches the user to an existing record before the form is even loaded, Authenticated Forms prevent the creation of duplicate records entirely. Additionally, known information can be pre-filled, making the experience faster for the user and reducing the chance of data entry errors.

## How to Enable It

1. Navigate to your Form's settings
2. Open the **Authentication & Verification** tab
3. Enable the **Verification** setting
4. Select the **Identity Type** you want contacts to use for verification

## When to Use It

* Forms for current students, alumni, or anyone who should already have a record in Element451
* Gathering updated information from contacts further along in the admissions funnel
* Any form where preventing duplicate records is a top priority

**Note:** Because Authenticated Forms require an existing record in Element451, they are not suitable for initial inquiry or lead capture forms where the contact may not yet exist in your system. For those, use Email Verification instead.

---

# Choosing the Right Option

Here's a quick guide to help you decide:

### "We use a lot of public forms and see frequent overwrites."

* Enable **Email Verification** on your highest-traffic public forms.
* Start with the **On Conflict** mode for a balanced approach, or use **Always** if you want maximum protection.

### "Parents and counselors keep overwriting records during event registration."

* Enable **Require Login** on your Event Sites for known audiences
* Enable **Email Verification** for events open to prospects

### "We need to preserve anonymous access but still want protection."

* Use **Email Verification** with the **On Conflict** mode. This only adds a verification step when incoming data actually *conflicts* with an existing record — keeping things frictionless for straightforward submissions.

### "We want to make sure only known contacts can access a specific form."

* Use **Authenticated Forms**. This ensures the person has an existing record and verifies their identity before the form is even displayed.

---

# Other Resources

* [Authenticated Forms](https://help.element451.com/en/articles/9440971-authenticated-forms-june-2024)
* [Event Registration Authentication](https://help.element451.com/en/articles/13797957-event-registration-authentication)
* [Appointment Booking Authentication](https://help.element451.com/en/articles/13798820-appointment-booking-authentication)
* [Security + Authentication Settings](https://help.element451.com/en/articles/8569773-security-authentication-settings)

---