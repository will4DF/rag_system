---
title: 📌 Campaigns: Frequently Asked Questions
url: https://help.element451.com/en/articles/10608654-campaigns-frequently-asked-questions
collection: Campaigns
---

This article answers commonly asked questions about Campaigns, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389719860/17818002be5edb2714e4069c4411/Pardon+our+Progress.png?expires=1784333700&signature=a2555bf41bd113b2572c673f41e466fbb19e72c066d3ea01d3a7cb4675b33892&req=dSMvH85%2FlIlZWfMW1HO4zSHoIpBzewUdnUmKgHt5anqaPFbnuhc5HAuWQLRy%0AFK1FEk2XuI07Jx0%2BYCM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389719860/17818002be5edb2714e4069c4411/Pardon+our+Progress.png?expires=1784333700&signature=a2555bf41bd113b2572c673f41e466fbb19e72c066d3ea01d3a7cb4675b33892&req=dSMvH85%2FlIlZWfMW1HO4zSHoIpBzewUdnUmKgHt5anqaPFbnuhc5HAuWQLRy%0AFK1FEk2XuI07Jx0%2BYCM%3D%0A)

# Email Campaigns

#### Why Can’t I Send Attachments in Bulk or Marketing Emails?

Attachments in bulk or marketing emails are **not supported** and **not recommended** due to the following risks:  
​

**🔴 Spam Filter Triggers**

Attachments (like `.exe`, `.zip`, `.pdf`, `.docx`) are commonly used to spread malware or phishing content. This makes them a red flag for spam filters, which may block or divert your emails.  
​

**📬 Inbox Provider Policies**

Major email providers like Gmail and Outlook often throttle or block bulk emails with attachments. Your emails may end up in the **Spam** or **Promotions** folders—or not be delivered at all.  
​

**⚠️ Sender Reputation Damage**

Attachments can increase complaint and bounce rates. Over time, this can damage your **domain** and **IP reputation**, hurting your deliverability across all future campaigns—even those without attachments.

**🐢 Slower Performance**

Large attachments slow down delivery and may trigger rate-limiting by receiving servers, leading to inconsistent or failed sending.

**✅ Best Practice**

Instead of attaching files, **host your content online** (e.g., via cloud storage or your website) and **include a download link** in your email. This is safer, faster, and improves deliverability.  
​

#### Why is my scheduled email not sending at the expected time, and where can I check my Element site's timezone settings?

The time of your scheduled email will depend on your **school's timezone settings**. To verify your timezone settings, go to **General Settings > School Settings**.

For **one-time, scheduled campaigns**, emails should be sent **around** the scheduled time. However, Element451 uses a **queue system** for optimized bulk processing. Once scheduled, emails enter a **“Reserved”** status, meaning they are in the queue and awaiting their turn to send. Then, they move to **“Sending”** status as they are actively being delivered.

If you’re experiencing **significant delays** beyond the expected queue processing time, please contact **Live Support** for assistance.

#### Why do some links in my campaign emails lead to a 404 or error page even though the URLs are valid?

There could be a number of causes. However, if you are linking to other software (such as student portals, Microsoft Bookings, Banner self-service, etc.), a common issue is **Element451 identity stitching**.  
​

To facilitate stitching, Element451 appends an `eid` URL parameter to links. For example, `https://school.edu/admissions` becomes `https://school.edu/admissions?eid=1234562`.  
​

This works perfectly for standard websites, but under certain circumstances the extra parameter can interfere with URLs for non-Element451 software, resulting in a 404 or other error. There are two easy fixes:  
​

**For standard inline text links:**  
Use an Element451 **`Link – URL`** token instead of manually typing the link. In the token options, set **Add EID** to **No**. This removes the parameter that may be interfering with the link.  
​

**For button links:**  
Buttons can’t use **`Link – URL`** tokens, but you can strip all parameters by placing `%%` in front of the URL, like this: `%%https://element451.com`.

---

# Tokens + Magic Links in Campaigns

#### What is a "token-based email" in Campaigns?

When sending an email campaign, the **Send To** field includes an option to select **"Token-Based Email."** This allows you to send the campaign to an email address stored on the contact’s record. We support the following email tokens:

* **Emergency Contacts Emails** `[user:emergency_contacts_emails]`
* **Guardian Emails** `[user:guardian_emails]`
* **High School Counselor Emails** `[user:hs_counselor_emails]`
* **Identity Emails** `[user:identity_emails]`

**Example:** If you collect family/guardian data using **field grouping** or **import** and do not store the data on separate contact records via a relationship, you can use the **Guardian Emails** token in the **Send To** field. For more details on sending campaigns to parents/guardians, review [Sending Campaigns to Parents/Guardians](https://help.element451.com/en/articles/8901542-sending-campaigns-to-parents-guardians).

**Important Note:** The **Send To** field supports **only a single email address**. If the selected token contains multiple emails (such as Guardian Emails), only the first listed email on the contact’s record will receive the campaign.

#### How can I test tokens and magic links sent in Campaigns before sending?

Check out our [help article on testing and previewing Campaigns](https://help.element451.com/en/articles/8901250-testing-previewing-campaigns) for our suggestion on this.

#### Why isn’t my token populating correctly when testing a campaign?

Tokens, like first name, only populate when you test using the “Send to Segment” option. If you use the individual email or phone number test, tokens will not populate because they aren’t supported in that testing method.

You can also use the "preview" feature to review your token output. When previewing you can use one of these two options:

* **Preview as Recipient** – Select a recipient in the preview feature to see how the email looks with their personalized data.
* **Send to Segment** – Send a test to a segment, and recipients will receive the email with tokens filled in based on their record data.

---