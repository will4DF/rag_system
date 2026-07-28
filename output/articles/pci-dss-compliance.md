---
title: PCI DSS Compliance
url: https://help.element451.com/en/articles/14054559-pci-dss-compliance
collection: General
---

Learn More About Element451, Payments and PCI DSS Compliance

# Overview

Element451’s platform is designed primarily to manage **student engagement, admissions, enrollment and retention data**. It has limited payment workflows for activities such as application fees, event registration fees, enrollment deposits, and other form-scoped payments.  
​

To ensure secure payment processing and minimize the handling of sensitive financial data, Element451 integrates with **trusted [third-party payment](https://help.element451.com/en/articles/3136121-getting-started-with-payments-how-to-add-and-connect-payment-providers#h_af94a46ab4) processors that maintain their own PCI DSS–compliant payment environments**.

These integrations allow institutions to collect and process payments securely while ensuring that payment credentials are handled directly within the payment processor’s secure environment.

---

# Cardholder Data Handling

Element451 is designed so that **cardholder data is not stored, processed, or transmitted within the Element451 platform infrastructure**.

Specifically, Element451 does **not collect or store**:

* credit card numbers (PAN)
* card expiration dates
* card verification values (CVV/CVC)
* magnetic stripe data
* payment authentication data

When a payment is initiated, users enter payment credentials directly into **secure payment interfaces hosted by the selected payment processor**. The processor then handles transaction authorization, settlement, and any applicable storage of cardholder data.  
​

Because Element451 does not directly handle cardholder data, **the cardholder data environment (CDE) is maintained by the payment processor rather than within the Element451 platform**.

---

# Payment Metadata Stored in Element451

While payment credentials are handled by the payment processor, Element451 may store **limited payment transaction metadata** to support admissions and enrollment workflows.  
​

Examples of metadata stored may include:

* transaction status (successful, failed, pending)
* payment amount
* payment timestamp
* processor transaction reference ID
* associated application, event, or form payment record

This information supports operational processes such as application tracking, reconciliation, reporting, and automated communications.  
​

This metadata **does not include cardholder data and is not considered PCI-regulated payment card data**.

---

# PCI DSS Scope and SAQ Alignment

Because Element451 fully outsources cardholder data collection and processing to PCI DSS–compliant payment processors, the platform’s PCI scope is significantly reduced.  
​

This architecture aligns with the **PCI DSS Self-Assessment Questionnaire (SAQ) A model**, which applies to merchants or service providers that:

* **fully outsource payment credential collection to validated third-party payment processors**
* **do not store, process, or transmit cardholder data within their own systems**

Under the SAQ A model:

* Payment processors maintain the **cardholder data environment (CDE)**
* Element451 systems **do not receive cardholder data**
* PCI DSS controls related to payment credential protection are managed by the processor

By contrast, **SAQ D applies to systems that store, process, or transmit cardholder data directly**, which would require significantly broader PCI DSS control coverage and infrastructure controls.  
​

Element451’s payment integration architecture is intentionally designed to **avoid direct handling of cardholder data**, thereby reducing PCI DSS scope while enabling secure payment workflows.  
​  
Our latest PCI DSS SAQ questionnaire is available at [trust.element451.com](https://trust.element451.com/).  
​

Institutions remain responsible for determining their own PCI DSS obligations based on their broader payment environment and institutional compliance requirements.

---

# Security Safeguards

Beyond PCI DSS requirements for a platform such as Element451, we maintain a **SOC 2 Type II audited security program**, which includes safeguards designed to protect platform data and maintain secure system operations.

These safeguards include:

* role-based access controls
* encryption of data in transit and at rest
* security monitoring and logging
* vulnerability management and penetration testing
* incident response procedures
* vendor risk management
* secure infrastructure and change management processes

Although Element451 is **not part of the cardholder data environment**, these controls help ensure that payment-related metadata and all other platform data are protected through strong operational security practices.

---