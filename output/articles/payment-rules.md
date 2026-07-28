---
title: Payment Rules
url: https://help.element451.com/en/articles/9071765-payment-rules
collection: Settings + Permissions
---

Learn how to create, manage, and apply Payment Rules to adjust pricing based on conditions like audience segments and dates.

# Overview

Payment Rules in Element451 offer a flexible way to customize how payments are applied to applications, deposits, events, or forms, ensuring each person is charged appropriately based on specific criteria or conditions. These rules can adjust the payment amount, enable discounts, and more once certain conditions—such as applicant type or registration date have been met.

Payment rules can only be used for **conditional** **payment** **types**. This article will teach you how to create, manage, and apply these rules to adjust pricing based on conditions like audience segments and dates.

---

# Accessing Payment Rules

1. Navigate to **Settings** > **General**
2. Clickon **Payment Rules** from the left menu.
3. Your payment rules are provided in a list format.

![](https://downloads.intercomcdn.com/i/o/1009384966/d00b2c0654d0aa6f418089f7/Pro+Tip+-+Orng.png?expires=1784430000&signature=b74f128af7dc8d76a96513f1bed029de350bce6d50d2494b130c02f7747453a9&req=dSAnH8p2mYhZX%2FMW3Hu4gb24ofpLkVOiT4bEc30U%2FnaPH68KcQA4kJqswjhJ%0AOQ%3D%3D%0A) You can filter the list using the toggle in the header to show only the rules that work with a particular module.

[![](https://downloads.intercomcdn.com/i/o/1010940683/7b8564deed4ffe148bf9b39d/Pmt+Rules.png?expires=1784333700&signature=a7cb6ee1481725a110419d7c24c025b85c38f8c62fe03328bb73d66eb027bab6&req=dSAmFsB6nYdXWvMW1HO4zZ%2F8DT%2FBhghBE42Z%2FIYEz7xGA%2BOGPLqhy0CFJFiR%0ANinycfnSTjE7WP%2BTS1k%3D%0A)](https://downloads.intercomcdn.com/i/o/1010940683/7b8564deed4ffe148bf9b39d/Pmt+Rules.png?expires=1784333700&signature=a7cb6ee1481725a110419d7c24c025b85c38f8c62fe03328bb73d66eb027bab6&req=dSAmFsB6nYdXWvMW1HO4zZ%2F8DT%2FBhghBE42Z%2FIYEz7xGA%2BOGPLqhy0CFJFiR%0ANinycfnSTjE7WP%2BTS1k%3D%0A)

---

# Managing Payment Rules

## Adding a Payment Rule

1. Navigate to **Settings** > **General** > **Payment Rules**.
2. Select the **module** to which you'd like to apply the payment rule. Payment rules can only be applied to one category/module.

   [![](https://downloads.intercomcdn.com/i/o/1011002803/5530bb5591848187f58529ff/payment+rules+-module+filter.png?expires=1784333700&signature=30de7794061ce2a12fe6b9b77c711c6cd25f6f587459c78101dfadf4323d7f03&req=dSAmF8l%2Bn4lfWvMW1HO4zcbE0zpKaOrEA%2FWQrZHiL6Kz7ep86dy1WF0DV9df%0AjCDS%0A)](https://downloads.intercomcdn.com/i/o/1011002803/5530bb5591848187f58529ff/payment+rules+-module+filter.png?expires=1784333700&signature=30de7794061ce2a12fe6b9b77c711c6cd25f6f587459c78101dfadf4323d7f03&req=dSAmF8l%2Bn4lfWvMW1HO4zcbE0zpKaOrEA%2FWQrZHiL6Kz7ep86dy1WF0DV9df%0AjCDS%0A)
3. Click either the **+ sign** in the header or the **+ Add Payment Rule** button at the bottom of the list.
4. Replace '**Name**' in the header with a name for your payment rule.
5. **Works** **For**: You selected this module in Step 2. To change this, close out the side sheet and repeat steps 2-3.
6. **Rule** **Description**: Briefly describe the rule's purpose for internal reference.
7. **Rule** **Settings**: Configure the payment **rule settings** based on your needs. Details on each configuration are in the next section.
8. **Conditional** **Logic**: Configure the payment **conditions** based on your needs. The next section provides details on each configuration.
9. When finished, click **Create** in the top right corner to save your payment rule.
10. As a final step, you must activate payment rules on your chosen payment(s). Details on this process are in the last section of this article

![](https://downloads.intercomcdn.com/i/o/1011769715/3d998225090ed076c6f6790a/Important+-+Orng.png?expires=1784430000&signature=4cafe466c7a1b87fdd2253a6061336592f79099499415f017c14229e672a9459&req=dSAmF854lIZeXPMW3Hu4gSZc0n3sbyA%2BqN5SRyyNdq1hhIdfKaGiLOvr51bo%0AIA%3D%3D%0A) When adding multiple payment rules to a single payment setup, the order in which you arrange them matters. The system applies the first rule (working from the top down) that a student meets the criteria for and does not consider any subsequent rules.

## Editing + Deleting a Payment Rule

1. Navigate to **Settings** > **General** > **Payment Rules**.
2. Locate the payment rule you wish to edit or delete, and click the **three vertical dots** at the end of that row.
3. Select **edit** or **delete** based on your desired outcome. If deleting, you'll be asked to confirm the action.

---

# Payment Rule Configurations

When you create or update a payment rule, you'll encounter two main components to configure: **Payment Settings** and **Conditional Logic**. Understanding how these elements work together to customize the payment process effectively is important.

**Payment Settings** specify how payments are processed once a rule's condition is met. This can include enabling discount codes, setting a specific payment amount, and other configurations directly affecting the transaction.

**Conditional Logic** defines the precise scenarios under which the Payment Settings will be applied. These can range from targeting a specific audience, like re-applicants, to setting date-based criteria. When someone fits the criteria outlined by these conditions, the Payment Settings you've established for that rule take precedence, overriding the default payment settings for that application, event, etc.

Let's look at an example for clearer insight:

*Suppose you have set your application fee at $100 in application settings. You then set up a payment rule that includes Payment Settings to reduce the fee to $25 for re-applicants. The condition for this rule is being in a segment that identifies the student as a re-applicant. Once the system identifies them as meeting this condition, the Payment Settings kick in, and they are charged the reduced fee of $25, overriding your standard $100 fee.*

## Payment Settings

* **Active**: When enabled, the rule will run.
* **Discounts**: Choose whether you want the discount to be a fixed amount or a percentage off.
* **Personal** **Check**: Users can pay by check instead of credit card when enabled. *This option is only available for Applications*.
* **Payment** **Description**: Describes the product or service purchased.
* **Credit** **Card** **Provider**: If you have multiple credit card providers, you will be prompted to select one.
* **Account**: Input an account number or name for internal tracking.
* **Payment** **Type**: There are four payment types to choose from: **fixed**, **conditional**, **calculated**, and **user-defined**.

  + Additional fields will appear to configure the specific settings depending on the Payment Type chosen. You can explore our article, [Payment Types](https://help.element451.com/en/articles/9071731-payment-types), to gain further insight into each type and how to configure them.
  + If you wish to use payment rules, you will need to select the **Conditional** payment type.

##

## Conditional Logic

1. Click the **+ Add Condition** button.
2. Select the condition type you wish to use:

   * **User Segment Reference:** Utilize a pre-existing segment that you've created.
   * **User** **Segment:** Create a custom segment of Contacts based on specific properties from their Contact record (e.g., demographics, interaction history).

     + **Important:** **User Segment** conditions are scoped to the current application only. If your payment rule needs to evaluate data across all of a student's applications, use a **User Segment Reference** (saved segment) instead. User Segment Reference conditions evaluate the student's full contact record and are not limited to the current application.
   * **Date** **Condition:** Evaluate date and time-based criteria.
   * **Application** **Custom** **Field**: Evaluate an application property criteria. This applies only to payment rules for Applications.
3. If you want to add additional conditions, repeat steps 1-2.
4. At the top, select if you want to match on **ALL** or **ANY** of the conditions.

   * With "ALL" (the AND operator), you specify that **all conditions must be met**. It's like saying, "Show me users who match ALL of these criteria."
   * With "ANY" (the OR operator), you're casting a wider net. It's like saying, "Show me users who match ANY of these criteria."
5. Click 'Create' in the top right corner when finished.

---

# Enabling Payment Rules by Module

These instructions are meant for those who have already created an Application, Deposit, Event, or Form. If you still need to create any of these, you can enable payments and payment rules during the creation process.

Payment Rules only apply to the Conditional Payment Type. You must first activate payments and select the conditional payment type to enable or add payment rules.

To access each payment section by module, follow these steps:

## Application Fees

1. Navigate to **Applications** > **Applications** > **All** **Applications.**
2. Edit the Application of your choosing.
3. Click the **pencil** **icon** in the right corner of the header.
4. Scroll down to the **Payment Info** section.

[Explore more on Application Payments →](https://help.element451.com/en/articles/9040630-creating-managing-applications)

## Deposits

1. Navigate to **Applications** > **Applications** > **Application Settings**
2. Click on **Deposits** from the left-hand navigation menu.
3. Edit the Deposit of your choosing.

[Explore more on Deposit Payments →](https://help.element451.com/en/articles/9062223-application-settings)

## Event Payments

1. Navigate to **Engagement** > **Events** > **All** **Events.**
2. Edit the Event of your choosing.
3. Click on the **Signups** tab.
4. Scroll down to the **Payment** section.

[Explore more on Event Payments →](https://help.element451.com/en/articles/1520669-event-registration-form-payments)

## Form Payments

1. Navigate to **Engagement** > **Forms**.
2. Edit the Form of your choosing.
3. Click on the **Content** tab.
4. Click on **Payment** from the left-hand navigation menu.

[Explore more on Form Payments →](https://help.element451.com/en/articles/9001082-creating-managing-forms)

---