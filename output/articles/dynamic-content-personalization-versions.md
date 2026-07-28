---
title: Dynamic Content: Personalization Versions
url: https://help.element451.com/en/articles/1513684-dynamic-content-personalization-versions
collection: Campaigns
---

Learn how to create different versions of the same messages for multiple audiences.

# Overview

Dynamic content in Campaigns allows you to create different versions of the same message for multiple audiences. This enables you to send one personalized message tailored to each recipient. Dynamic content with personalization can be used for both One-Time and Ongoing Communications.

For example, you can customize a paragraph in a prospect drip campaign email to be relevant to the student’s intended major or change the CTA link of a button to match the recipient’s funnel stage (apply versus deposit). You can also set various aspects of the email (subject line, content, sender) to change based on conditions you set for different groups of recipients. Conditions are filters that determine which version to display to the recipient based on attributes like geographic location or academic interest.

Another example of using dynamic content is communicating with recently admitted students and wanting to include a paragraph specific to in-state, out-of-state, and international students. Instead of building three different emails, create one email with personalization settings. All other message aspects can stay the same, or you can make additional customizations, such as different subject lines for each group.

## How does it work?

1. **Define Version Conditions:** Use conditions to narrow your audience. You can create more than one Version Condition.
2. **Add Content:** Enter text blocks, images, etc., that should change for recipients who meet a Version Condition.
3. **Auto Create:** Content will automatically matched to the condition a recipient meets.

![](https://downloads.intercomcdn.com/i/o/1072942653/58765d32191e2e8ef5451d2d/Important+-+Orng.png?expires=1784430000&signature=a6d1514130eec2efc9512c6d484a4672b2b9d05a12ba612b61f62553d86596fe&req=dSAgFMB6n4daWvMW3Hu4gZHbulJS8KT%2Fu5BYPZe7fF8WOUEq2v%2BH3LQFPrsT%0AdA%3D%3D%0A) If a recipient meets multiple conditions, they’ll receive the first condition version they meet in the order displayed in the Personalization section of the campaign builder. Learn more about reordering your versions [here](#h_5b96e1d451) to adjust their priority. If they don’t meet any conditions, they’ll receive the default version.

## What can be personalized?

Condition Versions can tailor the following components of a Campaign:

* **Email Campaigns**

  + Subject Line
  + Preview Text
  + Content Rows
  + Sender Name
  + Sender Email Address
  + Reply Address
  + CC
  + BCC
* **SMS Campaigns**

  + Outbound Phone Number
  + SMS Text / Attachment
* **Push Notifications**

  + Title
  + Content
  + Link

---

# Creating Personalized Campaigns

## Step 1: Define Version Conditions

1. If you haven't already, follow [these steps](https://help.element451.com/en/articles/9922192-creating-a-campaign-all-channels) to start building a Campaign.
2. Once you have the campaign started, click on the **Personalization** dropdown within **Communication Settings**in the Campaign editor.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1072933154/7638d10d3f80efa5d9db49f0/Screenshot+2024-06-05+at+4_29_17%E2%80%AFPM.png?expires=1784333700&signature=6a90a21b7a86c7dfbf580e85d9539fbb2aa8b68ad2465fe186c8fcecf1a022d6&req=dSAgFMB9noBaXfMW1HO4zW%2Bh6WnNFOITLi765whI0RXbNvnPz4OUklyy5Mc3%0AL6tg%0A)](https://downloads.intercomcdn.com/i/o/1072933154/7638d10d3f80efa5d9db49f0/Screenshot+2024-06-05+at+4_29_17%E2%80%AFPM.png?expires=1784333700&signature=6a90a21b7a86c7dfbf580e85d9539fbb2aa8b68ad2465fe186c8fcecf1a022d6&req=dSAgFMB9noBaXfMW1HO4zW%2Bh6WnNFOITLi765whI0RXbNvnPz4OUklyy5Mc3%0AL6tg%0A)
3. Click **Add Conditions**. The Version Condition side sheet will open.
4. **Name your version** by replacing 'Untitled Version Condition' in the header. Be concise and specific, as you'll need to refer back to these names when adding content.
5. Click **Add Condition** under Version Conditions. Additional instructions will guide you through creating your conditions. Your condition options are:

   * **Date Condition**: Evaluates date and time-based criteria.
   * **User Segment**: Create a custom segment of contacts using filters.
   * **User Segment Reference**: Choose a [pre-existing segment](https://help.element451.com/en/articles/1474191-segments-overview) that you've created.  
     ​

   [![](https://downloads.intercomcdn.com/i/o/1072942210/cde72f09051763968168a36d/Screenshot+2024-06-05+at+4_43_30%E2%80%AFPM.png?expires=1784333700&signature=446151b133b8a9fa1e2f5aa8e8d93ffc406181d083cb2abf8a49aacee24a6d1b&req=dSAgFMB6n4NeWfMW1HO4zf4%2BrJdlc%2B677YTpuhalgKpZ66Ujj33BXKiOfLFo%0AIZZw%0A)](https://downloads.intercomcdn.com/i/o/1072942210/cde72f09051763968168a36d/Screenshot+2024-06-05+at+4_43_30%E2%80%AFPM.png?expires=1784333700&signature=446151b133b8a9fa1e2f5aa8e8d93ffc406181d083cb2abf8a49aacee24a6d1b&req=dSAgFMB6n4NeWfMW1HO4zf4%2BrJdlc%2B677YTpuhalgKpZ66Ujj33BXKiOfLFo%0AIZZw%0A)
6. Once you have added your first condition, you can add additional conditions or save the Version Condition by clicking **Save** in the top right corner.

   * If more than one filter is added for a condition, the recipient must meet **all** of the criteria filters within that condition.
7. After adding your conditions, you can navigate back to the Campaign editor. The personalization section should now display your Version Conditions.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1072949352/e8b2733d96e9c1f937fde5c6/Screenshot+2024-06-05+at+4_55_22%E2%80%AFPM.png?expires=1784333700&signature=5909e94947244a9a6480248eb6cc8fd7c8068721210287c23fcf720d1db1a48a&req=dSAgFMB6lIJaW%2FMW1HO4zZIuBXLrQGR6gCsZcEI4hsRJ71Jaozs%2FkkA9ducy%0ASxW6%0A)](https://downloads.intercomcdn.com/i/o/1072949352/e8b2733d96e9c1f937fde5c6/Screenshot+2024-06-05+at+4_55_22%E2%80%AFPM.png?expires=1784333700&signature=5909e94947244a9a6480248eb6cc8fd7c8068721210287c23fcf720d1db1a48a&req=dSAgFMB6lIJaW%2FMW1HO4zZIuBXLrQGR6gCsZcEI4hsRJ71Jaozs%2FkkA9ducy%0ASxW6%0A)

## Step 2: Add/Edit Content for Each Version

### Select the Version + Edit Content (Except Email Content Rows)

1. Navigate to one of the campaign components listed [above](https://help.element451.com/en/articles/1513684-dynamic-content-personalization#h_810c3e1f5d) (an exception to this is the Content Rows within an email Campaign. That process is marginally different and discussed [below](https://help.element451.com/en/articles/1513684-dynamic-content-personalization#h_4a67b8b9e2)).
2. Use the **Version** dropdown menu to select the version you want to edit.

   * For example, in the screenshot below, the dropdown is shown on the subject line of an email campaign. If you select “First-Year,” you can modify the subject line specifically for recipients who meet the conditions for the “First-Year” version. Choose the version and make your edits to that component.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/1072958022/ed1d2d1eb821bc565a99efb1/Screenshot+2024-06-05+at+5_04_00%E2%80%AFPM.png?expires=1784333700&signature=6d0813bafe72fee2bfa3b9550e28763362ba4b405b7be6c7dc4b8b488ec6463b&req=dSAgFMB7lYFdW%2FMW1HO4zYDQ6WC8VHbKBIrSs3iV2%2BHDCCL05qzrh%2FQrePlT%0AWFAM%0A)](https://downloads.intercomcdn.com/i/o/1072958022/ed1d2d1eb821bc565a99efb1/Screenshot+2024-06-05+at+5_04_00%E2%80%AFPM.png?expires=1784333700&signature=6d0813bafe72fee2bfa3b9550e28763362ba4b405b7be6c7dc4b8b488ec6463b&req=dSAgFMB7lYFdW%2FMW1HO4zYDQ6WC8VHbKBIrSs3iV2%2BHDCCL05qzrh%2FQrePlT%0AWFAM%0A)

### **Select the Version + Edit Content (Email Content Rows Only)**

This process is slightly different than the others, where you select a version from the dropdown:

1. Click the row within the email builder to edit.
2. Select the **Audience** drop-down in the top purple header.

   [![](https://downloads.intercomcdn.com/i/o/1072963020/65caa4e1506cddc5b4bc4a1c/Screenshot+2024-06-05+at+5_18_32%E2%80%AFPM.png?expires=1784333700&signature=f1f968c675c0cebb9af03256a976977ac5a1fab5bb51136a1a2ac22ccee40c76&req=dSAgFMB4noFdWfMW1HO4zVGGc72otonAir9kbdj2eVRqu7oZqx15K9CQdfum%0AZJ3O%0A)](https://downloads.intercomcdn.com/i/o/1072963020/65caa4e1506cddc5b4bc4a1c/Screenshot+2024-06-05+at+5_18_32%E2%80%AFPM.png?expires=1784333700&signature=f1f968c675c0cebb9af03256a976977ac5a1fab5bb51136a1a2ac22ccee40c76&req=dSAgFMB4noFdWfMW1HO4zVGGc72otonAir9kbdj2eVRqu7oZqx15K9CQdfum%0AZJ3O%0A)
3. The Default version will already be listed, but you must click **+ Add Audience** to find and add your other versions.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/1072963704/a69d9c91980ed595b8e7650d/Screenshot+2024-06-05+at+5_19_52%E2%80%AFPM.png?expires=1784333700&signature=a1755a069ddd10014db9a8da4342a5ef11190d6957bfbe12790e8be8240b97e2&req=dSAgFMB4noZfXfMW1HO4zeGQuAEmUG2M8e65675ASc8bBNL4IIJqnstPjV0j%0AfVgC%0A)](https://downloads.intercomcdn.com/i/o/1072963704/a69d9c91980ed595b8e7650d/Screenshot+2024-06-05+at+5_19_52%E2%80%AFPM.png?expires=1784333700&signature=a1755a069ddd10014db9a8da4342a5ef11190d6957bfbe12790e8be8240b97e2&req=dSAgFMB4noZfXfMW1HO4zeGQuAEmUG2M8e65675ASc8bBNL4IIJqnstPjV0j%0AfVgC%0A)
4. **Select the Version** you wish to add and click **Add**.

   * You also have an option to select a template. This will replace the default content with the template of your choice.

     [![](https://downloads.intercomcdn.com/i/o/1072969569/bca5a5140f80cb367c510ba8/Screenshot+2024-06-05+at+5_27_38%E2%80%AFPM.png?expires=1784333700&signature=6aa30f9e20a707c5e9b70b04202972ffbfcfd1afc01d081987288c0e479d6565&req=dSAgFMB4lIRZUPMW1HO4zQm8LIb%2BEkreBH34rKnHqwcBb3Tbc8hj%2FsVhRI5A%0AYXMy%0A)](https://downloads.intercomcdn.com/i/o/1072969569/bca5a5140f80cb367c510ba8/Screenshot+2024-06-05+at+5_27_38%E2%80%AFPM.png?expires=1784333700&signature=6aa30f9e20a707c5e9b70b04202972ffbfcfd1afc01d081987288c0e479d6565&req=dSAgFMB4lIRZUPMW1HO4zQm8LIb%2BEkreBH34rKnHqwcBb3Tbc8hj%2FsVhRI5A%0AYXMy%0A)
5. Be sure to navigate through your entire email to check the audience on each row.
6. Also, if your Campaign is multi-channel, don't forget to edit the content for the other channel(s).

### Notes about Selecting the Version/Audience

* The "Default" version will go to any student who does not meet either of the version conditions.
* If you want to create multiple versions of the email content (in addition to different versions of the subject line, sender, etc.), go into the content editor and click on the row you would like to create multiple versions of.

Once you've finished adding and editing each version, you can preview and send your Campaign. The preview process is outlined in the [next section](https://help.element451.com/en/articles/1513684-dynamic-content-personalization#h_5727cb6a68).

##

---

# Previewing Campaigns with Condition Versions

You can use the **preview** **feature** to see how the different versions of the message will appear to your recipients. The preview feature also lets you see email campaigns **as one of your contacts**, including their specific token content and version.

[Explore More: Previewing Campaigns →](https://help.element451.com/en/articles/8901250-testing-previewing-campaigns)

---

# Managing Condition Versions

Once you have created version conditions within a Campaign, you can manage them from the same personalization section of the campaign editor.

[![](https://downloads.intercomcdn.com/i/o/1072979365/6d076d00042b00b9771521af/Screenshot+2024-06-05+at+5_48_52%E2%80%AFPM.png?expires=1784333700&signature=e8d432c6eac33dc12f18300e775f5ab6b24149fc0e4c11f0980790d2ab864184&req=dSAgFMB5lIJZXPMW1HO4zUBTNoOHRFlv9gJma7TYmzM%2BA2%2Fxy2WnGMe63lbH%0A6Vlvmav96rXH6Ndoj%2F0%3D%0A)](https://downloads.intercomcdn.com/i/o/1072979365/6d076d00042b00b9771521af/Screenshot+2024-06-05+at+5_48_52%E2%80%AFPM.png?expires=1784333700&signature=e8d432c6eac33dc12f18300e775f5ab6b24149fc0e4c11f0980790d2ab864184&req=dSAgFMB5lIJZXPMW1HO4zUBTNoOHRFlv9gJma7TYmzM%2BA2%2Fxy2WnGMe63lbH%0A6Vlvmav96rXH6Ndoj%2F0%3D%0A)

At the end of the row, you will find three icons that will allow you to manage your condition version.

* To **edit** your version, click the **pencil** icon.
* To **duplicate** your version, click the **copy/paper** icon.
* To **reorder** (change priority) or **delete** your version, click the three horizontal dots icon.

You can also **disable** a version by turning off the 'Enabled' toggle.

##

---