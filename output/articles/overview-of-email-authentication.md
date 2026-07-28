---
title: Overview of Email Authentication
url: https://help.element451.com/en/articles/8810117-overview-of-email-authentication
collection: Settings + Permissions
---

How to prepare for Google and Yahoo's upcoming changes.

# Overview

In February 2024, Google and Yahoo implemented significant changes regarding email authentication, specifically focusing on the implementation of DMARC (Domain-based Message Authentication, Reporting, and Conformance) entries.The primary aim of these changes is to enhance email security and reduce the incidence of spam and phishing attacks.

In light of these revised requirements, Element451 began work in late 2023 to ensure that our platform and underlying technologies fully comply with these updated standards. This proactive approach ensured that there was no interruption or reduced delivery of emails sent from Element451 to domains subject to these policies.

To ensure your marketing emails sent via Element451 comply with the all authentication standards and sending policies enforced by these major email inbox providers, you must can connect your email sending domain to Element451. The domain connection process involves setting up four separate DNS record types in your DNS provider's settings. These records will configure DKIM, SPF, and DMARC for SendGrid (Element451's bulk email partner).

# 2024 Key Changes and Requirements

* **Email Authentication Mandate:** All email senders, particularly bulk senders, are required to set up DMARC, along with DKIM (DomainKeys Identified Mail) and SPF (Sender Policy Framework). This move ensures that emails originate from legitimate sources and are not altered during transit. These measures will significantly improve email security and efficiency.

* **Impact on Bulk Senders:** The new policies particularly affect bulk senders. For these senders, the implementation of DMARC, DKIM, and SPF becomes crucial. It's important to note that while Google has set a daily sending threshold of 5,000 emails for defining a "bulk sender," Yahoo has not specified such a limit, implying that their requirements apply regardless of the volume of emails sent.

* **Consequences of Non-Compliance:** Emails failing to meet these new authentication requirements will likely be blocked. This could lead to specific bounce responses for non-compliant messages, potentially resulting in more permanent blocks on specific IPs or domains.

* **Easy Unsubscription and Low Spam Rates:** Google and Yahoo are mandating the inclusion of a one-click unsubscribe feature in emails and are enforcing a spam rate threshold below 0.3%. Exceeding this threshold could negatively impact the sender's email infrastructure.

# Adding SPF & DKIM Records

SendGrid and Element451 configure the required SPF (Sender Policy Framework) and DKIM (DomainKeys Identified Mail) records. Element451 displays the data required for these DNS entries on the **[Sender Domain Authentication](https://help.element451.com/en/articles/8471334-general-settings#h_0f5c807c03)** [tab](https://help.element451.com/en/articles/8471334-general-settings#h_0f5c807c03) in General Settings. You must have the Element451 Administrator permission to access this setting.   
​

[![](https://downloads.intercomcdn.com/i/o/940768810/90e3964ce6017fab82a7b7cf/Screenshot+2024-01-22+at+3.02.05%E2%80%AFPM.png?expires=1784333700&signature=4223b9ca756a93bfc88f9b5629b4e5ef805bbbe3c6f37d44c3680e478c38e6f7&req=fSQnEc92lYBfFb4f3HP0gOADt7ZmHL%2FAOFARW0v%2FMByH3zR9ilc5kSUpgkOG%0AO8HGKzJCXeMk251NLg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/940768810/90e3964ce6017fab82a7b7cf/Screenshot+2024-01-22+at+3.02.05%E2%80%AFPM.png?expires=1784333700&signature=4223b9ca756a93bfc88f9b5629b4e5ef805bbbe3c6f37d44c3680e478c38e6f7&req=fSQnEc92lYBfFb4f3HP0gOADt7ZmHL%2FAOFARW0v%2FMByH3zR9ilc5kSUpgkOG%0AO8HGKzJCXeMk251NLg%3D%3D%0A)

This is a configuration that Element451 cannot do on your behalf and must be completed by your IT team or DNS domain administrator. Fortunately, adding a these CNAME records is a simple process that can be done quickly by them.

# Adding a DMARC Record

Setup of a properly configured DMARC record for your domain is a critical measure to bolster your email security and is necessary to meet the new requirements set forth by Gmail and Yahoo.

This is a configuration that Element451 cannot do on your behalf and must be completed by your IT team. Fortunately, adding a DMARC record is a simple process that can be done quickly by your IT team or domain administrator. [Learn more about DMARC configuration from our friends at SendGrid.](https://docs.sendgrid.com/ui/sending-email/how-to-implement-dmarc)

**Creating a DMARC Record**

Record Type: TXT

Host: \_dmarc.YOUR\_DOMAIN\_HERE.edu

Value: v=DMARC1; p=none

[![](https://downloads.intercomcdn.com/i/o/940771479/8a5a39da3b18be1ea9e3be29/Screenshot+2024-01-22+at+3.02.05%E2%80%AFPM+copy+2.png?expires=1784333700&signature=4db8c48435418a95e349f9cdca2461c35cde3825e13e67e0a737d0a90d5af724&req=fSQnEc5%2FmYZWFb4f3HP0gMURm2BnynP2I3DxaLzKjCpAcYVz3A65oEAFYlZY%0AE8YGteA1RLA1zDw01Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/940771479/8a5a39da3b18be1ea9e3be29/Screenshot+2024-01-22+at+3.02.05%E2%80%AFPM+copy+2.png?expires=1784333700&signature=4db8c48435418a95e349f9cdca2461c35cde3825e13e67e0a737d0a90d5af724&req=fSQnEc5%2FmYZWFb4f3HP0gMURm2BnynP2I3DxaLzKjCpAcYVz3A65oEAFYlZY%0AE8YGteA1RLA1zDw01Q%3D%3D%0A)

📝  **Note:** The DMARC record above is configured in its most basic and lenient form, with the policy set to "none." Your Information Security or IT team has the option to select a more stringent policy value, such as "quarantine" or "reject." We strongly recommend seeking guidance from your university's IT team to ensure alignment with your unique security requirements. Any valid DMARC policy value is acceptable for compliance with the updated standards.

## DMARC Policy values

A DMARC policy can be defined by adding a TXT record in your DNS provider settings, with a value that can include the following semicolon-separated properties:

## DMARC Values

* **v:** the DMARC version
* **p:** the policy type that dictates how to process emails that do not pass. The policy can be set to one of the following types:

  + **none:** used to collect feedback and gain visibility into email streams without impacting existing flows.
  + **quarantine:** filter emails that do not pass authentication into the recipient's quarantine.
  + **reject:** bounce emails that do not pass authentication.
* **sp:** used to apply a policy to a subdomain of the DMARC record.
* **pct:** the percentage of total unique sends that failed authentication to apply this policy to. For example, if your DMARC record included p=reject; pct=25, and 100 emails failed authentication, only 25 of them will be bounced, while the other 75 will be delivered to their recipients.

  + Defining this property can help slowly ramp up your authentication policy to ensure it's working as expected.
  + Note that this parameter is sometimes ignored by certain inbox service providers.
* **ruf & rua:** two optional parameters that specify an email address to send DMARC reporting data to. These must be provided in URI mailto format (e.g., mailto:[reporting@example.com](mailto:reporting@example.com)). The reporting data that's sent differs based on the parameter:

  + rua: an aggregate report of all your domain traffic.
  + ruf: failure reporting data that includes redacted copies of individual messages that failed authentication.
* **adkim & aspf:** specifies the alignment mode for DKIM and SPF. These should both be set to r (i.e., a relaxed alignment). A relaxed alignment should be the default setting for DMARC for DNS services.

Once you've added and verified the DMARC record in your DNS provider, all receiving email servers can authenticate incoming emails from your domain and handle any failures according to the policy you specified.

Once you've added and verified the DMARC record in your DNS provider, all receiving email servers can authenticate incoming emails from your domain and handle any failures according to the policy you specified.

## Example DMARC policies

You can customize your DMARC policy to fit your business needs. Here are a few examples:

## Neutral Policy

v=DMARC1; p=none;

This is an example of a neutral DMARC policy with no additional parameters. A neutral policy is useful for senders who're just starting to get familiar with DMARC. This is the bare minimum for DMARC to function.

## Strict policy with Aggregate Reporting

v=DMARC1; p=reject; rua=mailto:[reporting@example.com](mailto:reporting@example.com);

The example above defines a strict DMARC policy to bounce any emails that fail authentication, and provides an email address to send aggregate reporting data to.

## Quarantine Policy with Failure Reporting

v=DMARC1; p=quarantine; pct=25; ruf=mailto:[reporting@example.com](mailto:reporting@example.com);

This example defines a policy that will quarantine 25% of emails that fail authentication, while the other 75% of emails that fail authentication will be permitted for delivery. The policy also provides a reporting address where an individual notification email can be sent for each email that fails authentication.

Defining a value for the pct property can allow you to test a random sample of messages that failed DMARC to allow you to check that legitimate emails are still being delivered properly.

**Remember:** Element451 Support cannot help with DMARC record setup. The DMARC policy you set up is unique to your business needs and your DNS provider. You should consult your IT administrator or whoever manages your DNS settings for help setting up DMARC. You can also consult third-party DMARC consulting or reporting services for additional assistance.  
​  
​**Element451 only requires a neutral policy be in place, however more stringent policies may be appropriate for your institution.**

---