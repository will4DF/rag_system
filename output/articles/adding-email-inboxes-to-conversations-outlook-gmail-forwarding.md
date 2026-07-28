---
title: Adding Email Inboxes to Conversations (Outlook + Gmail Forwarding)
url: https://help.element451.com/en/articles/6321778-adding-email-inboxes-to-conversations-outlook-gmail-forwarding
collection: Conversations
---

Connect your individual or shared email accounts as inboxes in Conversations.

# Overview

You can connect either an individual or shared group email inbox (Google or Outlook) to your Element451 Conversations inbox to manage messages in one place. This setup works by forwarding incoming emails to Element451, allowing you to read and reply to student messages alongside other channel conversations without switching tools.

We recommend this feature primarily for shared addresses like [admissions@elementuniversity.edu](mailto:admissions@elementuniversity.edu), ideal for team-based communication with fewer private interactions.

You can also connect personal inboxes (e.g., [michael@elementuniversity.edu](mailto:michael@elementuniversity.edu)), but keep in mind that all users with Conversations access can see incoming emails unless marked private.

## Good to Know

* Mark threads as **private** when needed to limit visibility.
* If connecting a personal inbox, we suggest keeping the **[anonymous conversations](https://help.element451.com/en/articles/9688991-anonymous-conversations)** setting turned off. This ensures only emails from known contacts (with matching email addresses) appear in Conversations.

## Individual vs. Group: Choosing the Right Option

* **Individual account** → used when the inbox is configured as a standard email account (even if multiple people share the login).
* **Group account** → used when the inbox is a formal Google/Outlook group or distribution list that supports adding members.

---

# Connecting an **Individual** Email Inbox

Some inboxes, whether they belong to a single staff member (e.g., [michael@elementuniversity.edu](mailto:michael@elementuniversity.edu)) or a shared admissions address (e.g., [admissions@elementuniversity.edu](mailto:admissions@elementuniversity.edu)), are set up by your institution as **individual accounts**.

To connect one of these inboxes:

1. Go to **Engagement > Conversations > Settings**.
2. Click **+ Connect inbox** and select **Email**.
3. Choose your provider:

   * **Gmail** or **Outlook (Office 365)** → individual account.
   * **Other Email Account** → for non-Google or non-Outlook providers.
4. Next, follow the provider-specific instructions listed below in the collapsible sections to continue the setup process:

## Outlook

Below you will find a video guide for connecting your Outlook email address to an inbox in Conversations, along with a step-by-step outline that follows the video.

**Introduction to Email Forwarding** [0:00](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=0)

**How the Feature Works** [0:13](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=13)

**Ideal Use Cases** [1:16](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=76)

**Best Practices for Replying** [2:20](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=140)

## Setting Up Individual Outlook Inbox [2:57](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=177)

1. Go to **Engagement > Conversations > Settings**.
2. Click '**Connect Inbox**' > Select '**Email**' > Choose '**Outlook**'.
3. Configure settings:

   * **From** **Name**: Enter your name.
   * **From** **Address**: Select 'Custom Address' and enter your email.
   * Optional: Add email signature.
4. Click '**Create** **Inbox**'.
5. Copy Unique Forwarding Address [4:09](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=249)

   * Copy the unique address generated for forwarding.
6. Configure Outlook for Forwarding: In Outlook, you can configure forwarding in two different ways. [4:31](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=271)

   * **Option 1**: If you have a "forwarding" tab in your settings, you can use that. This method is the most straightforward. If you lack a "forwarding" setting, this could be due to your institution's settings or the version of Outlook you're using, so you'll have to use option 2.

     + Navigate to **Settings** > **Mail** > **Forwarding (**Note: Depending on your version of Outlook, this process may vary.)
     + Toggleon **"Enable** **forwarding**"
     + Paste your **unique Element451 forwarding address** in the "Forward my email to" field.
     + It's recommended that you check the box "**Keep a copy of forwarded messages**."
     + Click '**Save**'.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649715661/dedd32410778762f001a524da96e/Outlook+Forwarding+Setting%402x.png?expires=1784333700&signature=56a3a0dd5976c24fe02707feaa905566c2122e0cf8d6813d4a57be1252cef830&req=dSYjH85%2FmIdZWPMW1HO4zQWZjtPRJTuVwd%2BEBVvr3cBWCdv3tOWZ8K7dFTIt%0AquNV%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649715661/dedd32410778762f001a524da96e/Outlook+Forwarding+Setting%402x.png?expires=1784333700&signature=56a3a0dd5976c24fe02707feaa905566c2122e0cf8d6813d4a57be1252cef830&req=dSYjH85%2FmIdZWPMW1HO4zQWZjtPRJTuVwd%2BEBVvr3cBWCdv3tOWZ8K7dFTIt%0AquNV%0A)
   * **Option 2**: If you don't have a "forwarding" setting or you simply wish to use a rule instead, follow these steps:

     + Navigate to **Settings** > **Mail** > **Rules (**Note: Depending on your version of Outlook, this process may vary.)
     + Give your rule a name. We recommend using something like "Redirect to Element451" so it's easily identifiable.
     + Add your condition:

       - Use "**To**"
       - Type **your** **email** **address**.
     + Add your action(s):

       - Usethe **"Redirect**"

         * ⚠️ **Important**: Do not use the "Forward" action. In Rules, Microsoft handles forwarded emails differently by changing the “From” address to your own email (the account that set up the forward). This prevents Element451 from seeing the original sender’s address, which means messages cannot be matched to the correct contact or conversation. Using a redirect keeps the original sender information intact, allowing Element451 to associate incoming emails accurately.
       - We also recommend adding a second action to your rule to keep a copy of your email in your inbox. To do this, add the "Copy to" action and select either your inbox or specify a folder.

         * You could also create a second rule to handle this process, but ensure the rules are ordered so that both will execute. You will need to uncheck the box "stop processing more rules" on the first rule so that the second rule will be allowed to run.
     + Click '**Save**'.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649713988/b836e8d775ff24027505d48e7c0d/Outlook+Redirect+to+Element451+Rule%402x.png?expires=1784333700&signature=af392cfe5f130bd89ab537ce0dadc1f61bdc005ae43d924f0965c68e4f8b9d58&req=dSYjH85%2FnohXUfMW1HO4zSpf7%2B9JUEesuoLpyBB5qKCI0JadLUYEKsPFE6fz%0AJYsa%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649713988/b836e8d775ff24027505d48e7c0d/Outlook+Redirect+to+Element451+Rule%402x.png?expires=1784333700&signature=af392cfe5f130bd89ab537ce0dadc1f61bdc005ae43d924f0965c68e4f8b9d58&req=dSYjH85%2FnohXUfMW1HO4zSpf7%2B9JUEesuoLpyBB5qKCI0JadLUYEKsPFE6fz%0AJYsa%0A)
7. Test Forwarding Setup [5:50](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=350)

   * Back in Element451, click '**Test Forwarding**'.
   * Wait for the test email to arrive in Outlook (may take 2-10 minutes).
8. Confirm Test Email Receipt [7:25](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=445)

   * Check for the test email in Outlook.
   * Note: May contain a confirmation code (usually not needed).
9. Once the email has been received, you can return to Element451 and close out of the email configuration sheet.
10. Hard refresh the page to confirm the red circle icon (email not verified) has been removed. [8:08](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=488)

## Gmail

**Introduction to the Feature** [0:00](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=0)

**Understanding Email Forwarding** [0:15](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=15)

**Email Processing in Element 451** [0:56](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=56)

**Best Practices for Setup** [1:50](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=110)

**Responding to Emails** [2:21](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=141)

## Setting Up an Individual Gmail Account [4:09](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=249)

1. Go to **Engagement > Conversations > Settings**.
2. Select '**Connect** **an** **Inbox**' and choose **Gmail**.
3. Configure settings: [4:30](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=270)

   * **From** **Name**: Enter your name.
   * **From** **Address**: Select 'Custom Address' and enter your email.
   * Optional: Add email signature.
4. Click '**Create** **Inbox**'.
5. Copy Unique Forwarding Address
6. Configure Gmail for Forwarding [5:50](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=350)

   * Go to Gmail settings and select 'Forwarding and POP/IMAP'.
   * Add a forwarding address: use the unique forwarding address from Element451.
7. Confirm Forwarding Address [6:05](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=365)

   * Complete the confirmation process in Gmail.
   * Return to Element451 to confirm the forwarding.
   * Click the "**Confirm Inbox Forwarding**" button.
8. Enable Forwarding in Gmail

   * **Refresh** the Forwarding and POP/IMAP page in Gmail settings.
   * You should see forwarding disabled.
   * Enable forwarding by selecting the second radio button.
   * You may need to paste the address again in the "forward emails to" section.
   * Save your changes.
9. Test the Forwarding Setup [8:08](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=488)

   * Click 'Test Forwarding' in Element451.
   * Wait for a confirmation email from Element451.
10. Once the email has been received, you can return to Element451 and close out of the email configuration sheet.
11. Hard refresh the page to confirm the red circle icon (email not verified) has been removed.

---

# Connecting a **Group** Email Inbox

If your shared address (e.g., [admissions@elementuniversity.edu](mailto:admissions@elementuniversity.edu)) is configured as a **Google Group** or **Outlook Group**:

1. Go to **Engagement > Conversations > Settings**.
2. Click **+ Connect inbox** and select **Email**.
3. Choose:

   * **Google Group** → Gmail-based shared inbox.
   * **Outlook Group (Office 365)** → Microsoft shared mailbox.
4. You’ll then follow the detailed steps for your email client below. Instead of traditional forwarding, you’ll add Element451 as a **group member** so it can automatically receive messages.

## Outlook

Below you will find a video guide for connecting your Outlook email address to an inbox in Conversations, along with a step-by-step outline that follows the video.

## Setting Up Group Email Address [8:34](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=514)

1. Go to **Engagement > Conversations > Settings**.
2. Click '**Connect** **Inbox**' > Select '**Email**' > Choose '**Outlook** **Groups**'.
3. Configure settings:

   * **From** **Name**: Enter group name.
   * **From** **Address**: Select 'Custom Address' and enter group email.
   * Optional: Add email signature.
   * Click '**Create** **Inbox**'.
4. Add Element451 as Group Member [9:35](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=575)

   * In Outlook, go to your group settings.
   * Paste your unique forwarding address as **a new member of the group.** Note: No forwarding needs to be set up for a group. You simply add a new member to your group and use the copied address as the member.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649730984/c5f00f6efe331068b24e394659cc/CleanShot+2025-08-01+at+14_57_44%402x.png?expires=1784333700&signature=cc403f042baace8346fbfeecff785f4901070a88555b34f23153e24772db09ad&req=dSYjH859nYhXXfMW1HO4zbShO0nSVDYPFYjFr22GoP1jJvHXl0k1m74ab%2FfM%0AN05d%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649730984/c5f00f6efe331068b24e394659cc/CleanShot+2025-08-01+at+14_57_44%402x.png?expires=1784333700&signature=cc403f042baace8346fbfeecff785f4901070a88555b34f23153e24772db09ad&req=dSYjH859nYhXXfMW1HO4zbShO0nSVDYPFYjFr22GoP1jJvHXl0k1m74ab%2FfM%0AN05d%0A)
5. Enable External Email for Group [10:23](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=623)

   * In your group settings, ensure the setting to allow external members to email the group is **enabled**.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649732677/ca3f6821b8d6678682c9fb490881/CleanShot+2025-08-01+at+14_58_53%402x.png?expires=1784333700&signature=4ca03034168dff7b28b762ec2f77e0c87fb2046eef28f728b892b4de8f0cac4a&req=dSYjH859n4dYXvMW1HO4zdmnyZIjgLDCPlSRQBO%2FiGN7CBVEr679jjJXg3AM%0AeF1M%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1649732677/ca3f6821b8d6678682c9fb490881/CleanShot+2025-08-01+at+14_58_53%402x.png?expires=1784333700&signature=4ca03034168dff7b28b762ec2f77e0c87fb2046eef28f728b892b4de8f0cac4a&req=dSYjH859n4dYXvMW1HO4zdmnyZIjgLDCPlSRQBO%2FiGN7CBVEr679jjJXg3AM%0AeF1M%0A)
6. **Test Group Email Forwarding** [10:50](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=650)

   * Navigate back to Element451 and click '**Test Forwarding**'.
   * Wait for the test email to arrive in Outlook. Note: This could take anywhere from 2 to 10 minutes. Do not close the sheet before the email arrives.
7. **Confirm Group Email Receipt** [11:01](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=661)

   * Check for the test email in Outlook.
8. Once the email has been received, you can return to Element451 and close out of the email configuration sheet.
9. Hard refresh the page to confirm the red circle icon (email not verified) has been removed.

**Troubleshooting** [12:00](https://loom.com/share/15b9fc8bea9444dd97701c2a2c577e72?t=720)

* If issues arise, check with IT for organizational policies affecting email forwarding.
* Use the message trace tool in the Microsoft Admin Center for troubleshooting.

## Gmail

## Setting Up a Group Email Account [9:33](https://loom.com/share/3e7be0384e164c3081fc52d836df9460?t=573)

1. Go to **Engagement > Conversations > Settings**.
2. Select '**Connect an Inbox**' and choose **Google Groups**.
3. Configure settings:

   * From Name: Enter your name.
   * From Address: Select 'Custom Address' and enter your email.
   * Optional: Add email signature.
4. Click 'Create Inbox'.
5. Copy Unique Forwarding Address
6. Add Element451 as a member of the group in Gmail.

   * In Google Groups, locate your group and go to your **group settings**.
   * Add Element451's unique address as a member of the group.
7. Return to Element 451 to confirm the forwarding.

   * Click 'Test Forwarding' in Element451.
   * Wait for a confirmation email from Element451.
8. Once the email has been received, you can return to Element451 and close out of the email configuration sheet.
9. Hard refresh the page to confirm the red circle icon (email not verified) has been removed.

---

# Troubleshooting

Experiencing an issue with configuring your email inbox through forwarding? Check out our troubleshooting articles below:

[General Troubleshooting →](https://help.element451.com/en/articles/8663239-group-email-forwarding-troubleshooting)

[Outlook Troubleshooting →](https://help.element451.com/en/articles/9876273-outlook-to-element451-email-forwarding-troubleshooting)

---