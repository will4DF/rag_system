---
title: Application Settings
url: https://help.element451.com/en/articles/9062223-application-settings
collection: Applications
---

Learn how to configure autoresponders, discount codes (waivers), deposits, submission prevention rules, and payment rules for applications.

# Overview

In the **Application Settings** section of Element451, you can customize some key functionality within the module. This overview introduces the key areas you can configure:

* **[Default Autoresponder Messages](#h_b95910375e)**: Automated responses to maintain timely communication with applicants.
* **[Discount Codes](#h_3dc4c16913)**: Set up and manage discount codes.
* **[Deposits](#h_9c6825b24c)**: Set up and manage enrollment deposit requirements.
* **[Submission Prevention Rules](#h_83579c2f10)**: Establish and manage condition-based rules to prevent application submissions.
* **[Identity Verification Rules](#h_identity_verification_rules)**: Establish and manage condition-based rules that control when identity verification is required and whether it must be completed before submission.
* **[Payment Rules](#h_2719ec0125)**: Establish and manage condition-based payment rules.

Each of these areas will be outlined in detail below, ensuring you have the information needed to effectively manage and streamline your application process, enhancing the experience for both your team and your applicants.

---

# Autoresponders

Autoresponder messages, sent via email, SMS, or both, are crucial in maintaining clear communication with applicants throughout their application journey.

In **Application Settings**, you can tailor the **default** autoresponder settings and content to your liking. You also have the option to fine-tune these settings [individually by Application](https://help.element451.com/) (except for information requests, which can be fine-tuned by the request type). Keep in mind that once you customize an autoresponder for a specific application, subsequent changes to the default settings here won't apply to that Application. A clear indicator of customization is the 'edited' tag appended to the autoresponder title, signaling it deviates from the original settings.   
​

[![Edited tag shown on a customized autoresponder message](https://downloads.intercomcdn.com/i/o/989302758/8b0b37e420e713e6d6a3c283/Autoresponder+-+Edited.png?expires=1784333700&signature=e5818545cb0bacd8fead399d546ef7d549cd66333b2a8ac81d2bfbc950886689&req=fSguFcl8moRXFb4f3HP0gJGbGNfXAaUNAEC1ZQfJ0ic3sktG93SM5%2BBqdghu%0Aumm7SP2DIIP4rZOe6w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/989302758/8b0b37e420e713e6d6a3c283/Autoresponder+-+Edited.png?expires=1784333700&signature=e5818545cb0bacd8fead399d546ef7d549cd66333b2a8ac81d2bfbc950886689&req=fSguFcl8moRXFb4f3HP0gJGbGNfXAaUNAEC1ZQfJ0ic3sktG93SM5%2BBqdghu%0Aumm7SP2DIIP4rZOe6w%3D%3D%0A)

**📌 Note:** When editing the message content section of the email message, you will notice two different options for editing: *Legacy* and *EmailBuilder*. The legacy option is an older editor that we no longer support. We recommend using the Email Builder, which allows you to edit the template using the same technology used in our Campaigns builder. We cover this feature in more detail below.

## Editing Autoresponders Using the Email Builder

When editing the message content section of an email message, you will notice two different options for editing: *Legacy* and *EmailBuilder*. The legacy option is an older editor that we no longer support. We recommend using the Email Builder, which allows you to edit the template using the same technology used in our Campaigns builder.

## Navigating the Email Builder

✨ **Pro Tip:** We recommend using the full-screen feature to edit your campaign. Click the double-sided arrow icon to enter and exit full-screen mode.  
​

[![Email Builder toolbar with full-screen option highlighted](https://downloads.intercomcdn.com/i/o/1124983111/3b6279cf1b1ede6f0f96c4c9/Screenshot+2023-12-16+at+3_46_39%E2%80%AFPM+%281%29.png?expires=1784333700&signature=66183653d839dc882fb07c105faea752c0e36dcf994975b1c1ab5ce4e7bb403f&req=dSElEsB2noBeWPMW1HO4zagGk9Z5nFAbIFIgrpPARojPszHa58qLDTkWATUR%0AgxPYq5FpDk4E%2FSysdAI%3D%0A)](https://downloads.intercomcdn.com/i/o/1124983111/3b6279cf1b1ede6f0f96c4c9/Screenshot+2023-12-16+at+3_46_39%E2%80%AFPM+%281%29.png?expires=1784333700&signature=66183653d839dc882fb07c105faea752c0e36dcf994975b1c1ab5ce4e7bb403f&req=dSElEsB2noBeWPMW1HO4zagGk9Z5nFAbIFIgrpPARojPszHa58qLDTkWATUR%0AgxPYq5FpDk4E%2FSysdAI%3D%0A)

* **Add Content Blocks + Elements:** Click the **+** sign in the top left corner to open the list of Content Blocks available to add. This allows you to select any of our prebuilt blocks to add and customize.

  + You can add the following Blocks: [Custom Components](https://help.element451.com/en/articles/1513676-creating-an-email-campaign#h_824b3aa5ba), *Row*, *Separator*, *Dividers*, *Alerts*, *Header*, *Bodies*, *CTA*, *Lists*, *Quotes*, *Signatures*, and *Footer*.
  + When you add a Row, you have the option to add individual elements such as a Text Block, Image Block, Button Block, HTML Block, Video Block, AI Text Prompt Block, Ruler, and Social. Read more about these elements in our [Campaigns article](https://help.element451.com/en/articles/1513676-creating-an-email-campaign#h_64422d90a2).
* **Text Editing**:

  + Highlight the text within your message content to access the formatting toolbar.
  + Utilize

    [![BoltAI icon](https://downloads.intercomcdn.com/i/o/1124995120/4b513e2bca643f724ac703fc/BoltAI.png?expires=1784333700&signature=4ee8b5805f0a426bd93e570f9e395824f16e13d21fd67dd7014dbb9be1d2f9c2&req=dSElEsB3mIBdWfMW1HO4zT42ep1O6Ie%2B402jR2AAT7cBYNaiYRnlSppkJgug%0AcGfT%0A)](https://downloads.intercomcdn.com/i/o/1124995120/4b513e2bca643f724ac703fc/BoltAI.png?expires=1784333700&signature=4ee8b5805f0a426bd93e570f9e395824f16e13d21fd67dd7014dbb9be1d2f9c2&req=dSElEsB3mIBdWfMW1HO4zT42ep1O6Ie%2B402jR2AAT7cBYNaiYRnlSppkJgug%0AcGfT%0A)

    [BoltAI Writing Tools](https://help.element451.com/en/articles/8380026-boltai-writing-tools) and apply various formatting options to enhance your text.
* **Email Settings**:

  + Click the gear icon to edit the email background image, adjust transparency, and modify font settings.
* **Undo and Redo**:

  + Use the undo and redo arrow buttons to easily correct mistakes and refine your email during the editing process.
* **Copy HTML**:

  + Click the copy button to copy the HTML of your email to your clipboard.
* **Device Preview**:

  + Use the phone, tablet, and computer icons to preview how your email will render on each device.
* **Edit and Preview Tabs**:

  + Toggle between the Edit and Preview tabs in the top right corner of the email builder to switch between editing and previewing your email.

## Autoresponder List

The twelve customizable autoresponders are below broken up by category:  
​

## Applications

* ***Application Preview***: Sent when a student requests a preview of their Application from the Application Dashboard.
* ***Application Submitted***: Sent when a student submits their Application.

## Application Payments

* ***CC Payment Successfully***: Sent when a student's application fee payment is successful.
* ***Deposit CC Payment Successful***: Sent when a student's deposit fee payment is successful.

## Request Information

Autoresponders for information/document requests can't be tailored for each Application but can be adjusted by Request Type. To edit, go to **Applications** > **Applications** > **Request Information**. New Request Types will inherit the default settings configured here in Application Settings, which you can customize as needed during editing. [Explore more on the Request Information feature.](https://help.element451.com/en/articles/8421103-request-information-in-applications)

* ***Document Received (to student)***: Sent to the student when the recommender completes the request.
* ***Document Request with Waiver***: Sent to the recommender when the student waives their right to view information sent on their behalf.
* ***Document Request without Waiver***: Sent to the recommender when the student does NOT waive their right to view information sent on their behalf.

## Registration Portal

* ***Password Reset Request Secondary Email Notification***: Sent to the student when requesting to change their password, and multiple email addresses are on file. The message informs the student that the reset link is sent to their primary email address.
* ***User Password Changed***: Sent to the student when requesting to change their password to confirm a successful password change.
* ***User Password Reset Request***: Sent to the student when requesting to change their password, with a link to reset.
* ***User Profile Changed***: Sent to the student after a change was made to their profile from the Application site.
* ***User Registered to Application***: This message is sent to the student after creating an account to start an Application. It encourages the student to continue their Application.

You can also enable or disable these messages at any time. For added convenience, a feature allows you to send a preview to yourself. This lets you see exactly what the applicant will receive, ensuring that every communication is perfectly crafted.

* To activate/deactivate an autoresponder, use the **Active** toggle.
* To edit an autoresponder, click the three vertical dots, then **Edit Message**.
* To send a preview, click the three vertical dots, then **Send Preview Message**.

---

# Discount Codes

By utilizing Discount Codes, applicants can remove or discount the application fee before submitting their Application.

To access Discount Codes, you can use the shortcut link here in Application Settings or navigate to your **Profile Picture/Avatar** > **Settings** > **Discount Codes**.

## Adding + Managing Discount Codes

To enable Discount Codes:

1. If you haven't already, **add a Discount Code** in General Settings.
2. When creating your discount code, be sure to specify which application(s) or deposit(s) it should work with (if needed).
3. Enable discounts on the payment section of your application or deposit

To learn more about managing Discount Codes and applying them to deposits and application fees, visit our [Discount Codes](https://help.element451.com/en/articles/9039727-discount-codes) article.

---

# Deposits

Element451 allows applicants to pay a deposit fee once the Decision has reached the **released** stage.

To enable this functionality, you'll need to:

1. Add a Deposit in Application Settings
2. Enable the Deposit on your Application

We outline those two steps below:

**📌 Note:** You must integrate your payment provider(s) to use Element451's deposit functionality. The Element451 Customer Success team facilitates this process during your implementation phase.

## 1- Creating a Deposit

1. Navigate to **Applications** > **Applications** > **Application Settings** > **Deposits**.
2. Click **+ Add Deposit.**
3. Configure the Deposit settings and information:

   * **Name**: Assign a name for internal reference.
   * **Active**: This toggle enables this deposit and makes it active. It is enabled by default, but you can disable it after creating the deposit.
   * **Discounts**: Turning this toggle on permits discount codes to be used on this payment. Discount codes are configured in General Settings. To learn more about configuring discount codes, visit our [Discount Codes](https://help.element451.com/en/articles/9039727-discount-codes) article.
   * **Payment Description**: Describes the product or service purchased.
   * **Credit Card Provider:** If you have multiple credit card providers, you will be prompted to select one. Note: Form Payments only work with Element451 preferred payment partners.
   * **Account:** You can input an account number or name for internal tracking.
   * **Payment Type:** There are four payment types to choose from: **fixed**, **conditional**, **calculated**, and **user-defined**.

     + Additional fields will appear to configure the specific settings depending on the Payment Type chosen. You can explore our article, [Payment Types](https://help.element451.com/en/articles/9071731-payment-types), to gain further insight into each type and how to configure them.
     + If you wish to use payment rules, you will need to select the **Conditional** payment type.
   * **Payment Dialog Title**: Add help text that appears on the modal/dialog box under the "Pay the Fee" title. This space supports adding links, which is great for including your payment/refund policies and more.
4. When finished, click **Create** in the top right corner to save your Deposit.

## 2- Adding Deposits to an Application

1. Navigate to **Applications** > **Applications** > **All Applications**.
2. Click the name of the Application to open the editor.
3. In the top right corner of the header, click the pencil icon to open the Application settings.
4. Scroll down to the bottom and look for the **Deposit** section.
5. Select an existing Deposit from the dropdown menu or click Add Deposit to add a new Deposit.
6. When you're finished, click **Save** in the top right corner.

### Setting: Deposit Unique to Registration

The setting 'Deposit Unique to Registration' allows you to require a separate deposit for each submission to that specific application. If disabled, a single deposit payment will apply across multiple submissions.

---

# Submission Prevention Rules

With Submission Prevention Rules, you can prevent users from submitting applications using custom criteria. While users are already prevented from submitting applications if they do not fill out the required fields or have already submitted an application for the same term and major combination, this feature allows further customization of these rules.

**⚠️ Important:** For the "Prevent Starting Application" setting to take effect, the user must have an existing record in Element451 **and** be included in the segment referenced. If they're not part of the segment, they can start the application but won't be able to submit it.

To enable this functionality, you'll need to add your Rule(s) here in Application Settings and then add that Rule to your Application. We'll outline those two steps below:

## Creating a Submission Prevention Rule

1. Navigate to **Applications** > **Applications** > **ApplicationSettings** > **Submission Prevention Rules**.
2. Click **+ Rule**.
3. Configure the Submission Prevention Rule settings and information:

   * **Name**: Assign a name for internal reference.
   * **Description**: Provide a brief description for internal reference.
   * **Message**: Message that will be displayed to the student when this Rule prevents submission.
   * **Prevent Starting Application**: Prevent students from beginning an application. *Note*: Only conditions utilizing user segment reference (using records that exist in your Element451 instance) can be used to prevent starting an application. Application scoped conditions will be ignored.)
   * **Conditional Logic**: Add the conditional logic required to prevent the user from submitting an Application. See [Condition Types](#h_condition_types) below for details on the available condition types and when to use each.
4. When you're finished, click **Create** in the top right corner.

## Condition Types

Submission Prevention Rules support three condition types. Choose the one that matches the data your rule needs to evaluate.

### User Segment

Build a segment directly in the Rule. **User Segment** conditions are scoped to the **current application only** and cannot evaluate data from a student's other applications.

**Use when:** Your rule only needs to evaluate data on the current application — for example, the value of a custom field on this application.

### User Segment Reference

Reference an existing saved segment. **User Segment Reference** conditions evaluate the student's **full contact record**, consistent with what you see on the People page.

**Use when:** Your rule needs to check data from outside the current application — for example, contact-level fields, behavior, or membership in a population defined by a saved segment.

**Note:** User Segment Reference is also the only condition type that works with the **Prevent Starting Application** setting.

### Application vs. Milestone

Block submission when the student already has a specified milestone on **another application** that shares a property value with the current application. This is useful when you want to prevent a student from re-applying based on what's already happened on a different application, without having to maintain a saved segment for each scenario.

* **Milestone Type**: The milestone to look for on the student's other applications (for example, *Application Submitted* or *Decision Released*).
* **Application Property**: The application field that must match between the current application and the prior application (for example, *Term*, *Program*, or *Campus*).

**Example — Prevent re-applying for the same term:**

* Milestone Type: *Application Submitted*
* Application Property: *Term*

If the student has an *Application Submitted* milestone on another application where the **Term** matches the current application's **Term**, the rule blocks submission on this application.

## Adding Submission Prevention Rules to an Application

1. Navigate to **Applications** > **Applications** > **All Applications**.
2. Click the name of the Application to open the editor.
3. From the lefthand menu, click **Submission Prevention Rules**.
4. Click **+ Add Submission Prevention Rule**.
5. Select the existing Rule from the 'Select Condition' dropdown menu.
6. Click **Save**.

---

# Identity Verification Rules

Identity Verification Rules allow you to apply identity verification more precisely to specific applicant populations instead of relying only on a single application-level setting.

Rules allow you to control both whether identity verification is required and whether it must be completed **before submission** or can occur **after submission**. This supports flexible workflows, such as requiring identity verification only for a specific program, only for certain residency groups, or only after an application has been flagged for possible fraud.

To use this functionality, you'll first create your Rule(s) in Application Settings. Then, you'll enable identity verification on the Application and apply Rules to a specific application.

## Creating an Identity Verification Rule

1. Navigate to **Applications** > **Applications** > **Application Settings** > **Identity Verification Rules**.
2. Click **+ Rule**.
3. Configure the Identity Verification Rule settings and information:

   * **Name**: Assign a name for internal reference.
   * **Description**: Provide a brief description for internal reference.
   * **Enable Identity Verification**: Choose whether identity verification should be turned on or off for the population matched by this Rule.
   * **Required to Submit**: Choose whether identity verification must be completed before the applicant can submit, or whether it can be required after submission.
   * **Conditional Logic**: Define who the Rule applies to. You can reference an existing user segment, build a segment directly in the Rule, or use application properties to match a custom field.

     + **Important:** When configuring conditional logic for Identity Verification Rules, **User Segment** conditions are scoped to the current application only. To target students based on cross-application data, use a **User Segment Reference** (saved segment) instead.
4. When you're finished, click **Create** in the top right corner.

## Adding Identity Verification Rules to an Application

1. Navigate to **Applications** > **Applications** > **All Applications**.
2. Click the name of the Application to open the editor.
3. In the top right corner of the header, click the pencil icon to open the **Edit Application** sheet.
4. Scroll down to the **Identity Verification** section.
5. Set the default [identity verification](https://help.element451.com/en/articles/13006508-identity-verification) state for the Application.
6. Add the Identity Verification Rule(s) you want to use for this Application.
7. If you add more than one Rule, arrange them in the correct order by dragging and dropping. The system evaluates Rules in order and presents the **first matching Rule** to the applicant.
8. When you're finished, click **Save**.

---

# Payment Rules

Applications can use conditional logic to display different payment options for deposits or application fees. This feature is particularly beneficial for institutions that need to show different payment options for different application types. For instance, you could use different payment processors for international applicants compared to domestic ones or charge varying fees for different applicant types.

You can add multiple payment rules for each Application. However, please keep in mind the order of payment rules as the top-most payment rule is weighted to activate first, followed by subsequent rules.

To access Payment Rules, you can use the shortcut link here in Application Settings or navigate to your **Profile Picture/Avatar** > **Settings** > **Payment Rules**.

## Creating + Managing Payment Rules

To enable Payment Rules, you need to:

1. If you haven't already, you need to **add a Payment Rule** in General Settings.
2. Enable payment on your application fee or deposit.
3. Select the **Conditional** payment type.
4. Select the **Payment Rule**.

To learn more about managing Payment Rules and applying them to deposits and application fees, visit our [Payment Rules](https://help.element451.com/en/articles/9071765-payment-rules) article.

---