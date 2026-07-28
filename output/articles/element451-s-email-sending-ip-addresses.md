---
title: Element451's Email-Sending IP Addresses
url: https://help.element451.com/en/articles/10413535-element451-s-email-sending-ip-addresses
collection: Settings + Permissions
---

Ensure Element451 messages are delivered to your institution's email domain(s)

# Overview

When Element451 sends email on your behalf—such as notifications, marketing campaigns, or transactional messages—those messages are delivered through **dedicated sending IP addresses**. These IPs help ensure reliable delivery and maintain a strong sender reputation for your institution.

Because colleges and universities often use **stricter email filtering rules** than consumer providers like Gmail, Yahoo, or Outlook.com, trusted vendor traffic may be blocked unless it’s explicitly allowed. To ensure faculty, staff, and students consistently receive important messages from Element451, we strongly recommend adding our sending IP addresses to your institution’s allowed lists.

---

# Why Do We Share Our IP Addresses?

* **Whitelisting**: If your organization’s email filters or firewalls are strict, you might need to “whitelist” (approve) specific IP addresses so that emails from Element451 aren’t blocked or marked as spam.
* **Email** **Delivery** **Assurance**: By knowing our IP addresses, you can more easily troubleshoot any issues with email delivery or filtering.

---

# Current IP Addresses

We currently use the following IP addresses, each dedicated to specific email types:

* 149.72.207.3 – Conversations, Transactional Emails
* 149.72.212.156 – Marketing Emails
* 149.72.223.121 – System Emails
* 149.72.130.92 – Backup
* 149.72.24.235 – Backup

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1338566058/0c2a7f0fb791402641322fcb6c1b/Note.png?expires=1784430000&signature=1cdd6d3600bbddc1184229bfb4d5af134b259c59108c1912ecfe4c102774fbad&req=dSMkHsx4m4FaUfMW3Hu4gXIX1Rx8BPvCdJMgu5hygPMPrJLEpHoPPLsXLVfx%0A8A%3D%3D%0A) We may add or update these IPs in the future as we grow or adjust our email-sending infrastructure. Check back here for the latest information.

---

# Do I Need to Do Anything?

If your organization uses strict filters, we recommend having your IT team whitelist the IPs listed above to ensure smooth email delivery. However, if you’re already receiving our emails without any issues, there’s likely nothing you need to do. Should you encounter any problems, please contact our support team or collaborate with your IT department to confirm that these IPs are allowed in your environment.

---

# Security and Reliability

* **Reputation & Monitoring**: We use a reputable email service provider (SendGrid) that actively monitors IP health and blocks malicious activity.
* **Encryption & Authentication**: Our emails use standard protocols like SPF, DKIM, and DMARC to verify senders and protect against spoofing.
* **Ongoing Maintenance**: We regularly review the performance of our email-sending IP addresses. If we ever need to replace or add IPs, we’ll update this list.

[Explore More: Email Authentication →](https://help.element451.com/en/articles/8810117-overview-of-email-authentication)

---

# Special Considerations for Microsoft Exchange Online

Some institutions use **Microsoft Exchange Online** (Office 365) to receive email. Exchange Online applies multiple layers of filtering and policy enforcement that can sometimes reject legitimate, system-generated email **even when sending IPs are whitelisted**. In this case, we recommend also configuring an **Inbound Connector** in additionl to standard allow-list (whitelisting).   
​

This behavior is specific to **Exchange Online** and does **not** typically apply to:

* On-premises Microsoft Exchange servers
* Google Workspace (Gmail)
* Other third-party mail gateways or providers

## Why this happens in Exchange Online

Exchange Online evaluates incoming mail using several stages, including connection filtering, policy enforcement, and mail flow rules. While IP allow-listing is often sufficient to bypass spam filtering, **tenant-level policy rules may still reject messages** at an earlier stage.  
​

When this occurs, Exchange Online may return an error similar to:

```
550 5.4.1 Recipient address rejected: Access denied
```

This can happen even if:

* The sending IP is allow-listed
* SPF, DKIM, and DMARC are configured correctly
* Previous messages from the same IP were delivered successfully

Because this rejection occurs at the policy or transport layer, delivery can appear inconsistent without additional configuration.

Additionally, SMTP error 550 is a common rejection message that indicates the recipient's mail server has rejected the email. This can occur even if the sending IP is allow-listed and SPF, DKIM, and DMARC are configured correctly. Administrators should investigate the specific cause of the rejection and take corrective action.

## Recommended configuration for Exchange Online tenants

To ensure consistent delivery from Element451, Exchange Online administrators may need to configure **both** of the following:

1. **IP Allow-Listing**  
   Add all Element451 sending IP addresses (listed above) to your connection filter allow-list.
2. **Inbound Connector (Exchange Online only)**  
   Configure an **Inbound Connector** using the same IP list. An inbound connector explicitly tells Exchange Online to trust email originating from these IPs and helps prevent policy-level rejections that simple allow-listing may not override.

Inbound connectors are commonly used in higher-education environments for trusted vendor platforms that send automated or system-generated email, such as CRMs, admissions systems, and LMS integrations.

## Important notes

* Inbound connectors are **specific to Microsoft Exchange Online (Office 365)**
* They are **not required** for on-prem Exchange or most other email platforms
* Inbound connectors do **not** bypass malware scanning or authentication enforcement; they simply prevent tenant-level access denials

---

# Questions or Concerns?

If you have any questions about these IP addresses or how Element451 sends emails, contact our support team. We’re here to help you set up or troubleshoot your email environment.

---