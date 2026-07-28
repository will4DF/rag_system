---
title: Access Rules
url: https://help.element451.com/en/articles/12987558-access-rules
collection: Settings + Permissions
---

# Overview

The **Access Rules** feature is a security and functionality tool designed to solve two key problems: preventing known fraudulent or unwanted activity (blocking) and ensuring seamless interaction for known, safe users (whitelisting).

Rules can be configured based on IP address, country, or email domain.  
​

# The Two Purposes of Access Rules

## 1. Blocking (Preventing Fraud)

This function prevents applications and other entries from known fraudulent IP addresses, email domains, or countries where you are not conducting business from ever reaching your Element451 environment.  
​

## 2. Whitelisting (Improving Experience)

This function is critical when you have a high number of submissions coming from a "safe zone" or shared on-campus resource (like a computer lab or admissions office). Whitelisting these trusted IP addresses prevents the Element451 Fraud Agent from flagging applications from these locations as potentially fraudulent.

---

# Access Rules - Blocks (Blacklisting)

The blocklist prevents specific unwanted entities from accessing your public-facing entry points.  
​

## Block Rule Types

|  |  |  |
| --- | --- | --- |
| **Rule Type** | **Action** | **Notes** |
| **Email Domain** | Block Only | Use this to block disposable email address domains or known spam sources. |
| **IP Address** | Block (or Blacklist) | Block a single IP address or an entire IP address range. |
| **Country** | Block Only | Block submissions originating from a specific country (based on IP detection). |

When a rule is added to the blocklist, it affects the following activities in Element451:

* Submitting Forms
* Uploading Files
* Registering for Events
* Submitting Surveys
* Starting (Registering for) and Application
* Updating Application Data
* Submitting Applications
* Submitting Application Supplemental Forms
* Booking Appointments
* Logging into the Application Sites or StudentHub

---

# Access Rules - Whitelisting

Whitelisting is available for **IP addresses only**. It improves the user experience for students submitting applications from a shared, trusted IP address or range, such as a computer lab or office kiosk on campus or at a trusted partner site.  
​

## Whitelisting Benefits

By whitelisting a specific IP address or range, Element451 adjusts its behavior for users from that location:

1. **Relaxed Fraud Detection:** The system relaxes the rules around flagging applications from those IP addresses as potentially fraudulent, even if a high number of applications are submitted from the same IP address.
2. **Increased Rate Limit:** The rate limit for submissions from that IP address is raised, preventing blockages when many students are simultaneously working on applications in a single location.
3. **reCAPTCHA Disabled:** reCAPTCHA is disabled for all activities originating from the whitelisted IP addresses, as they are presumed to be safe and known.

---

# How to Set Up Access Rules

Setting up an Access Rule is a simple process accessible from your general settings.

1. **Navigate to Settings:** Go to your profile picture > **Settings** > **General**.
2. **Select Access Rules:** On the left-hand navigation, select the **Access Rules** tab.
3. **Add a Rule:** Click **Add a Rule**.
4. **Add Internal Note:** Enter a brief note explaining the purpose of the rule (e.g., "Blocking spam domain" or "Whitelisting campus computer lab"). This is for internal staff use.
5. **Select Rule Type and Action:**

   * **Rule Type:** Select **Email Domain**, **IP Address**, or **Country**.
   * **Action:** Depending on the rule type, select **Block** or **Whitelist** (if available).
6. **Enter Value:** Input the specific email domain (e.g., `spam-mail.com`), the IP address/range, or the country name.
7. **Create:** Click Create to activate the rule.

---

# Priority Handling: Block Rules Always Take Precedence

In the event of a rule conflict, a **Block Rule will always override a Whitelist Rule**.

That is,If a user's activity simultaneously meets the conditions of both a **Whitelist** and a **Block** rule, Element451 will **enforce the Block Rule and deny access.**  
​

This ensures that explicit security restrictions maintain ultimate control.

---

# Other Important Considerations

* **Internal Notes:** Always use the internal note field to document why a rule was created.
* **IP-Based Country Detection:** Country blocking is based on the IP address detected. If a user utilizes a VPN or other masking tool, Element451's system will be unable to detect their true country.
* **Whitelisting Limit:** Remember that **only IP addresses** can be whitelisted. Email domains and countries can only be blocked.

---