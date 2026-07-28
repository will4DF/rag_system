---
title: Event Registration Form + Payments
url: https://help.element451.com/en/articles/1520669-event-registration-form-payments
collection: Events
---

Guide for event organizers on configuring signups in Element451: Set attendee limits, customize forms, and manage payments efficiently.

# Overview

This article is tailored for organizers who have enabled event signups (registration). It walks you through the configurations within the Signups tab of the event editor. You'll discover how to set default registration limits for attendees and guests and customize your registration form to gather relevant data on your attendees.

The Signups tab is also where you can customize messages to be sent to registrants, attendees, and no-shows and enable and configure event self check-in. However, these topics are covered in separate articles:

* [Event Messaging and Notifications](https://help.element451.com/en/articles/1524108-message-attendees)
* [Event Self Check-In](https://help.element451.com/en/articles/9650448-event-self-check-in)

Additionally, for events that require a registration fee, this guide provides step-by-step instructions on setting up payment collection.

---

# Creating a Registration/Event Signup Form

1. Navigate to **Engagement** > **Events** > **All** **Events**.
2. Click on your event's name or the **pencil** icon to open the editor.
3. Click the **Signups** tab.
4. The Signup Form editor should open. If not, click **Form** from the left-hand menu.
5. The editor is split into three sections: ***signup form*** *(settings)*, ***form content****, and **payment***. We'll guide you through each section below. Note: Changes to settings and form content are saved automatically as you make them.

---

# Signup Form (Settings)

The signup form settings allow you to control key functionality over your signup form.

## Signup Form Settings

* **Choose From Template:** Use the dropdown to apply an existing signup form template to your event. When selected, the fields from the chosen template will automatically populate the form. You can then customize the form further if needed—adding, editing, or removing fields.

  + **Want to create a new template?** Templates must be created by the Element451 team. To request one:

    1. Build your form on any event’s **Signup** tab.
    2. Contact customer support and include the event link.

       Once the form is converted, it will appear in the **Choose From Template** dropdown for future use.  
       ​
* **Registration Status:** Opens/closes registration for the event

  + Registration status is set to closed by default.

    - This hides the 'register' buttons from your landing page and only allows the dates/times to be seen. ​
  + You can set the 'Number of Attendees' for your event occurrence to enable the registration form to close automatically once that limit has been reached.

* **Default Attendees Limit:** The number you input here is the default attendance limit for any event occurrence that doesn't have a value set in the **[Event Date(s) and Times](https://help.element451.com/en/articles/9094765-event-dates-occurrences#h_f42ea158f1)** section of the Event Overview tab. This ensures there's always a control on attendance numbers, even if you miss setting it for a specific date.

* **Default Number of Guests:** The number you input here is the default guest limit for any event occurrence that doesn't have a value set in the **[Event Date(s) and Times](https://help.element451.com/en/articles/9094765-event-dates-occurrences#h_9571c0ee28)** section of the Event Overview tab.

* **Max Signups:** Add a number here if you wish to establish a limit on how many times a person can sign up for the same event. If not, leave the field empty.

* **Closing Date:** If enabled, this configures the registration status to close automatically on a specific date. You can choose once the event starts or ends or add a custom date.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356958637/21b8b8f8a3ffed4a432176b278b5/Evenets%2B-%2BForm%2BSettings.png?expires=1784333700&signature=736974396e9ff73d224bcecc84b096c6e340a11d926066a645ec5d34686949f4&req=dSMiEMB7lYdcXvMW1HO4zb5mg%2BNDmlbPy6rAB8pyZI%2BKW1pJ0sqHgKGVSCVr%0ALBl1LjY97PzqFvxylH4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356958637/21b8b8f8a3ffed4a432176b278b5/Evenets%2B-%2BForm%2BSettings.png?expires=1784333700&signature=736974396e9ff73d224bcecc84b096c6e340a11d926066a645ec5d34686949f4&req=dSMiEMB7lYdcXvMW1HO4zb5mg%2BNDmlbPy6rAB8pyZI%2BKW1pJ0sqHgKGVSCVr%0ALBl1LjY97PzqFvxylH4%3D%0A)

---

# Form Content

In the form content section, you create your form by adding/editing fields. You can add as many fields as you'd like and apply validation and conditional logic to create a dynamic experience that makes registering for your events easy.

![](https://downloads.intercomcdn.com/i/o/996042870/9c779b03f3d8856deb229604/Note-Orng.png?expires=1784430000&signature=8810832b8513112d2ebed7ebf89ae52b1753102c9f016cd95b494ce99c86dd9f&req=fSkhFs18lYZfFb4X1HO4gRdSe9M5s%2Fib5mJV9fAC8hg6AmcgLlhk9TDSrVnX%0A) This section assumes you have a solid understanding of Data Fields and Conditional Logic. If you need more experience in either or need a quick review, please take a moment to review [this help article](https://help.element451.com/en/articles/9093505-fields-validation-conditional-logic).

## How-To: Add + Manage Fields

* **Add Field:** Add new fields to your form by clicking the **Add** **Field** button.

  + When you add a new field, the field editor will open, allowing you to configure the advanced settings for that particular field, including things like help text, default value, field size, validation, conditional logic, and more.

* **Edit Field:** To edit a field, click the **pencil** icon.

* **Delete Field**: Click the trash can icon to delete a field.

* **Reorder Fields:** Click and drag the field using the up and down arrows, dropping it in a new place.

* **Make Field Required**: To require a value in the field, toggle on **Required**.

![](https://downloads.intercomcdn.com/i/o/996057564/9db46782eb35bd7310aa1939/Pro+Tip+-+Orng.png?expires=1784430000&signature=d0ef3126b5efcf5dbb1e0c3548440c4a9cf3be762f0b0c2d8b948d1f23c3c6a7&req=fSkhFsx5mIdbFb4X1HO4gb%2BontfzphKq7LBCKTaVP7f1TFlkEHjP9QMuTALM%0A) Use a [hidden form field to create](https://help.element451.com/en/articles/9093505-fields-validation-conditional-logic#h_409f60335e) an event that registers non-student participants.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356961933/106a86a254331a7886472aac850b/Events-2B--2BForm-2BContent.png?expires=1784333700&signature=5614a97257d36bdbf297b47bc906533a1b0da4834c740176de6f2ad0274496f3&req=dSMiEMB4nIhcWvMW1HO4zUqNKGsfOh846fi%2Ffud7zbXpIodO43jz%2BkwT5hN8%0AKukWeigAvXAu%2BJxjvP4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1356961933/106a86a254331a7886472aac850b/Events-2B--2BForm-2BContent.png?expires=1784333700&signature=5614a97257d36bdbf297b47bc906533a1b0da4834c740176de6f2ad0274496f3&req=dSMiEMB4nIhcWvMW1HO4zUqNKGsfOh846fi%2Ffud7zbXpIodO43jz%2BkwT5hN8%0AKukWeigAvXAu%2BJxjvP4%3D%0A)

---

# Payment

The payment section allows you to enable payments and collect a fee if required to attend the event.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2209453707/ad0991b4d1ad2ae74608a354d09f/Event-2BPayment.png?expires=1784333700&signature=05d173d12bae9c0a099244a1d3b0c27bb2cbfbc606a2659c35611c761a974b79&req=diInH817noZfXvMW1HO4zYCNHsLzQCuJwOeRwQ5KHBWXz7Wr5ZGeYT9BUGVR%0A9uYerzzE%2BGRYXbRAuD0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2209453707/ad0991b4d1ad2ae74608a354d09f/Event-2BPayment.png?expires=1784333700&signature=05d173d12bae9c0a099244a1d3b0c27bb2cbfbc606a2659c35611c761a974b79&req=diInH817noZfXvMW1HO4zYCNHsLzQCuJwOeRwQ5KHBWXz7Wr5ZGeYT9BUGVR%0A9uYerzzE%2BGRYXbRAuD0%3D%0A)

You must integrate your payment provider(s) to use Element451's event payment functionality. [Explore more about our payment providers](https://help.element451.com/en/articles/3136121-preferred-payment-providers).

## Payment Settings + Expirations

### Payment Settings

* **Active**: Use the **Active** toggle to enable payments.

* **Discounts**: Turning this toggle on permits discount codes to be used on this payment. Discount codes are configured in General Settings. To learn more about configuring discount codes, visit our [Discount Codes](https://help.element451.com/en/articles/9039727-discount-codes) article.

* **Payment** **Description**: Describe the product or service purchased.

* **Credit Card Provider:** If you have multiple credit card providers, you will be prompted to select one.

* **Account:** Input an account number or name for internal tracking.

* **Payment Type:** There are four payment types to choose from: ***fixed***, ***conditional***, ***calculated***, and ***user-defined***.

  + Additional fields will appear to configure the specific settings depending on the Payment Type chosen. You can explore our article, [Payment Types](https://help.element451.com/en/articles/9071731-payment-types), to gain further insight into each type and how to configure them.
  + If you wish to use payment rules, you will need to select the **Conditional** payment type.

![](https://downloads.intercomcdn.com/i/o/1010934141/54ad16232261616ca1b27528/Pro+Tip+-+Orng.png?expires=1784430000&signature=e2ac6e3927217fd2410f36e196a756621ff19871270eb1ee30ca32512e278776&req=dSAmFsB9mYBbWPMW3Hu4gYraj5i6%2FIQmUVFXn%2BTZxKBQsEOsTFNzgIXtObbh%0Amw%3D%3D%0A) Use the Calculated payment type to write a formula to include guest fees in the payment amount. To do this, use the `user-events-guest-number` field.

## Non-Payment Registration Expiration

##

* **Registration expires if person doesn't pay it in:** This setting determines the timeframe a registrant has to complete their payment *if they choose the "Pay Later" option*. Here are some important considerations:

  + **Timer Begins Immediately Upon Registration**: Keep in mind that this timer begins immediately upon submitting the event registration form, even before the user clicks "Pay Later." After this timeframe has ended, the registrant is marked as canceled.
  + **Avoid short timeframes:** We recommend setting this to at least 30 minutes and ideally 1 hour or more. Short durations (e.g., 10 minutes) can lead to registrations being canceled if the user gets interrupted or doesn't immediately complete the payment step.
  + **"Pay Later" and Email Reminders:** When a registrant selects "Pay Later," an email ("Complete your registration by submitting a payment!") is automatically sent to the registrant, which includes a link to complete payment. Please note that this email cannot be customized at this time. Longer expiration periods provide more flexibility for users to complete their payment after receiving this reminder.

    - Explore more on Event Messages with Events with Payments [here](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications#h_25f0ab471d).

## Process Flow for Registration with Payment

1. **Registration:** Attendee completes and submits the event registration form.
2. **Payment Modal:** A payment modal appears.
3. **Pay Now or Pay Later:** The attendee can choose to pay immediately by selecting their payment method, or there is an option to select "Pay Later."
4. **Expiration Timer:** The expiration time frame, explained in the payment settings section below, starts as soon as the registration form is submitted.
5. **"Pay Later" Reminder:** If the attendee chooses "Pay Later," they will receive an email reminding them to complete their payment.
6. **Registration Cancellation:** If the payment is not completed within the specified timeframe, the registration will be automatically canceled.

## Tracking Payment Status

Once payments are enabled, there are two ways to track payment status:

* **From the Attendees tab:** The event's Attendees tab includes a Payment column that displays each registrant's status as either "Paid" or "Pending Payment" (if registration without payment is allowed).
* **From Segments:** Use the *Event (All Properties)* filter to build a segment of attendees for a specific event filtered by payment status. This is useful for targeting follow-ups to registrants with outstanding payments.

---

# Authentication

These optional settings allow you to control if and how contacts authenticate when registering for an event. They allow you to either limit registration to known contacts or verify that the correct person is submitting the form before data is saved.

[Event Registration Authentication](https://help.element451.com/en/articles/1520669-event-registration-form-payments)

---

🛑 You're not done! If you are creating an event, we recommend reviewing two additional articles: [Event Page](https://help.element451.com/en/articles/1524123-event-page) and [Event Messaging and Notifications](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications).

---