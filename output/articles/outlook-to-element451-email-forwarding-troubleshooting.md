---
title: Outlook to Element451 Email Forwarding Troubleshooting
url: https://help.element451.com/en/articles/9876273-outlook-to-element451-email-forwarding-troubleshooting
collection: Conversations
---

A guide to help you troubleshoot and resolve common problems when connecting your Outlook inbox to Element451 using email forwarding.

# Overview

When connecting your Outlook inbox to Element451 using email forwarding, you may encounter issues due to Microsoft 365 security policies. This guide will help you troubleshoot and resolve common problems.

---

# Configuration Checks + Solutions

## Check Organization Policies

By default, many organizations have policies preventing emails from being forwarded to external domains. This is a security measure, but it can interfere with connecting to Element451.

### Solution:

* Contact your IT department or Office 365 administrator.
* Request that they allow external forwarding to the @element451.io domain.

## Verify Anti-Spam Outbound Policy

Microsoft 365 Defender has an Anti-Spam outbound policy that may block external forwarding. You have two options to address this:

### Solution A: Adjust Your Global Anti-Spam Policy

1. Open [Microsoft 365 Defender](https://security.microsoft.com).
2. Navigate to Email & Collaboration > Policies & Rules > Threat policies.
3. Click on "Anti-spam."
4. Edit the Anti-spam outbound policy (Default).
5. Under "Automatic forwarding rules," select "On – Forwarding is enabled."
6. Save your changes.

![](https://downloads.intercomcdn.com/i/o/1179627491/aa0a16abc683fc16d3dfa821/Note.png?expires=1784430000&signature=d73a567c40617139651b9d6760455aa9b50bde0a6364be053534dc8185635199&req=dSEgH898moVWWPMW3Hu4gaFbpR3bVsiujtxmo2zzqYjdzyPBlRBlmLPi1G7v%0ACw%3D%3D%0A) This solution affects all users in your organization. Use with caution and consult your IT department.

### Solution B: Create a Specific Anti-Spam Policy

This is a more secure approach as it only allows forwarding for specific users or groups.

1. Open [Microsoft 365 Defender](https://security.microsoft.com).
2. Navigate to **Email & Collaboration** > **Policies & Rules** > **Threat Policies**.
3. Under the 'Rules' section, click on "Anti-spam."
4. Click on "Create policy" and select "Outbound."
5. Name your policy (e.g., "Element451 Forwarding Policy").
6. Under "Users and domains," you can either:

   * Select specific users or groups that need to be forwarded to Element451 or
   * Apply to all domains if you want this policy to be organization-wide
7. Click "Next" until you reach "Automatic forwarding rules."
8. Set "Automatic forwarding rules" to "On – Forwarding is enabled"
9. Review your settings and click "Submit" to create the policy

This policy will allow forwarding to @element451.io while keeping other external forwarding restricted if desired.

## Check Remote Domain Settings

The Remote Domain settings in Exchange Online control how your organization's email system interacts with external domains. You only need to set this up once for the @element451.io domain, and it will apply to all users connecting to Element451.

### Solution A: For IT Administrators (Using PowerShell)

If you're an IT administrator comfortable with PowerShell:

1. Connect to Exchange Online PowerShell
2. Run the following commands:

```
New-RemoteDomain Element451 -DomainName element451.io   
Set-RemoteDomain Element451 -AutoForwardEnabled $true
```

### Option B: For General Users (Using Exchange Admin Center)

If you're not comfortable with PowerShell, you can use the Exchange Admin Center:

1. Log in to the [Microsoft 365 Admin Center](https://admin.microsoft.com).
2. Go to "Admin centers" > "Exchange."
3. In the Exchange admin center, navigate to "Mail flow" > "Remote domains."
4. Click the "+" button to add a new remote domain.
5. Name it "Element451."
6. In the "Domain" field, enter `element451.io`.
7. Click "Save."
8. Find the newly created domain in the list and double-click to edit.
9. In the settings, find "Allow automatic forwarding" and set it to "On."
10. Click "Save."

This process creates a specific rule for the Element451 domain, allowing automatic forwarding to their email addresses.

##

---

# Verify Forwarding is Working

After checking the configurations above and making changes, you can verify that forwarding works correctly. Here's how to check:

1. In the Microsoft 365 admin center, go to the Message Trace tool.
2. Look for two entries related to your test email:

   * Inbound: from Element451 to your Outlook inbox
   * Outbound: from your Outlook to the Element451 inbox
3. The outbound message should show a "**Delivered**" status.

---

# Test Forwarding in Element451

Once you've verified that the message has been delivered on the Microsoft end, you can continue connecting your inbox to Element451 using the process outlined in [this video](https://www.loom.com/share/ce4d9db21d6547479b3d9b9f0683025f?sid=785ad91d-4f66-470b-882f-b7ef1e66e34a).

If you were at the point of testing the forwarding and experienced a spinning button, you can return to Conversation Settings to re-test forwarding.

This action will help clear any potential issues on the Element451 side.

---

# Additional Notes:

* These steps may require administrator access to your Microsoft 365 environment. You must work with your IT department if you don't have this access.
* There may be other organization-specific policies affecting email forwarding. Your IT team might need to investigate further if these steps don't resolve the issue.
* Please always make sure you follow your organization's security policies when making these changes.

##

---