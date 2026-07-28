---
title: Security + Authentication Settings
url: https://help.element451.com/en/articles/8569773-security-authentication-settings
collection: Settings + Permissions
---

Learn how to configure your internal and external user authentication methods.

# Overview

In Element451, you can configure authentication methods for internal users (staff and faculty) and external users (students) to ensure secure access to your platform.

These settings can be customized by navigating to **Settings > Manage Users > Security** in the admin dashboard.

📌 **Note:** Access to this screen requires one of the following individual permissions: Administer Security Settings, Manage SSO Settings, or Manage API Keys. Users will only see the sections relevant to their assigned permissions.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1325292791/5e1814d337b0325f4a41e6f820bc/Screenshot+2023-12-05+at+12_25_30%E2%80%AFPM.png?expires=1784333700&signature=ca701d1d7024de56e0e44b758411b4ccd81d6fcaa10881adefe0bc440bf48411&req=dSMlE8t3n4ZWWPMW1HO4zaFdV38%2Fno0IM2ck5FGPbMcakMePWL4TR2UmCJPE%0A7Rm%2F5YbACr7Bwz55qK0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1325292791/5e1814d337b0325f4a41e6f820bc/Screenshot+2023-12-05+at+12_25_30%E2%80%AFPM.png?expires=1784333700&signature=ca701d1d7024de56e0e44b758411b4ccd81d6fcaa10881adefe0bc440bf48411&req=dSMlE8t3n4ZWWPMW1HO4zaFdV38%2Fno0IM2ck5FGPbMcakMePWL4TR2UmCJPE%0A7Rm%2F5YbACr7Bwz55qK0%3D%0A)

---

# Internal Authentication Settings

This section allows you to specify how **internal** **users** (staff and faculty) log into Element451.

## Password (Element451-Provided Login)

* The **Password** option is the Element451-provided login method, allowing users to log in with an email address and password. You can learn more about adding users [here](https://intercom.help/element451/en/articles/2735199-adding-managing-internal-users).
* When the Element451 password is enabled for internal users, [Multi-Factor Authentication](#h_af2499dcc3) (MFA) is **required and cannot be toggled off**.
* Users will receive a one-time code via email or text message (SMS). This code must be entered into the on-screen modal to complete the login process.
* Requires the *Administer Security Settings* permission to modify these settings.

## Single Sign-On (SSO)

* SSO allows users to access Element451 through your institution’s SSO provider. While Element451 does not control MFA for SSO logins, we strongly recommend confirming with your SSO provider that MFA is enabled for added security.
* Configuring SSO requires the *Manage SSO Settings* permission.

[Explore More: Configuring SSO →](https://help.element451.com/en/articles/10542911-configuring-managing-single-sign-on-sso)

## Google

* Google Workspace login lets users authenticate through their Google accounts.
* As with SSO, MFA for Google is managed outside of Element451, and we recommend verifying MFA is enabled for Google Workspace accounts.
* Requires the *Administer Security Settings* permission to modify these settings.

## API Key

* An API key is an authentication token that functions as a secure access pass for API calls. It establishes authorization, allowing access to your integrations. More information on API keys can be found [below](#h_cac14e0cdb).
* Requires the *Manage* *API Keys* permission.

---

# External Authentication Settings

This section allows you to specify the ***default*** login methods **external** **users** (students) log into Element451 feature sites including: [Application Sites](https://help.element451.com/en/articles/9077560-application-sites), [Event Sites](https://help.element451.com/en/articles/1524123-event-landing-page), [Appointment Booking Site](https://help.element451.com/en/articles/11157302-appointments-site-settings) and [StudentHub](https://help.element451.com/en/articles/9827408-getting-started-with-studenthub).

## Password (Element451-Provided Login)

* The **Password** option is the Element451-provided login method. External users create their account credentials (email and password) when they register for an account using the application site’s [registration form](https://help.element451.com/en/articles/9040630-creating-managing-applications#h_caf4aecfdf).
* Unlike with internal users, [Multi-Factor Authentication](#h_af2499dcc3) (MFA)is **optional** for external users logging in with the Element451 password method.

  + If enabled, external users will follow the same MFA process as internal users, receiving a one-time code via email to verify their login.
* **Optional Phone MFA**: Admins can optionally turn on Phone MFA. This offers a backup option to code email code delivery.
* The *Administer Security Settings* permission is required to modify these settings.

## Single Sign-On (SSO)

* External users can log in through your institution’s SSO provider. We recommend confirming with your provider that MFA is enabled for external accounts.
* Configuring SSO requires the *Manage SSO Settings* permission.

[Explore More: Configuring SSO →](https://help.element451.com/en/articles/10542911-configuring-managing-single-sign-on-sso)

## Google

* Google Workspace accounts can also be used for external logins.
* As with SSO, enabling MFA through Google is strongly advised to ensure secure access.
* The *Administer Security Settings* permission is required to modify these settings.

## Magic Link

* Magic Links allow one-click login for those with existing Element451 accounts. When requested, a link is sent to the users known email address. Clicking the link will authenticate the user to the requested site.
* User requested Magic Links expire after 48 hours.
* The *Administer Security Settings* permission is required to modify these settings.

## Custom Web App Authentication Settings

In addition to the global external authentication settings above, you can configure login methods independently for each student-facing web application. This allows institutions to, for example, allow Element Password or Magic Link on Application Sites for prospective students who don't yet have institutional credentials, while enforcing School SSO on StudentHub for enrolled students.  
​

Each web app includes an **Override authentication methods** toggle. When **disabled** (default), the application inherits the global Web App (External) Authentication Settings. When **enabled**, the following methods can be configured independently for that application:

* **(Element) Password** with optional MFA
* **SSO**
* **Google**
* **Magic Link**

Applications that support per-application overrides:

* **StudentHub**
* **Application Sites**
* **Event Sites**
* **Appointment Booking Sites**

---

# Your API Keys

An API key is an authentication token that functions as a secure access pass for API calls. It establishes authorization, allowing access to your integrations.

Configuration of API Keys requires the *Manage API Keys* permission.

* When you create an API key, it is associated with your account and will be listed here under *Your API Keys.*
* To ensure better security and organization, we recommend creating a new internal user (e.g., Integrations) to generate the API key. This way, if there's a change in employees or someone else needs access, the API key won't be tied to a specific user's account, making transitions smoother.
* Even if Password authentication is disabled, API keys can still authenticate API calls.

## Disabling Username/Password Method + Using API

* If you've built your API integration before Dec 2023, disabling password login to enforce SSO **will break your integration**. Be sure to create an API key for authenticating your API calls.
* API integrations managed by Element451 are not affected if you turn off password login options.

---

# Multi-Factor Authentication (MFA)

MFA is a security measure that is part of the Element451 email/password authentication. MFA adds an extra layer of protection to the login process by requiring users to verify their identity using a one-time code.

### How MFA Works

* If the Element451 password authentication method is enabled, MFA is required for internal users and optional for external users.
* After successfully entering their email and password,the user will receive a one-time code via email. The code is valid for 10 minutes.
* The user must enter this code into the on-screen modal to complete the login process.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1376162592/c4e51d6f0653e199f30db909eff6/ABCD123.png?expires=1784333700&signature=d1638e84937a99b23b649933ad534ff0f462bdf79dc87545d724d20c25b5da91&req=dSMgEMh4n4RWW%2FMW1HO4zYJdP2QiT63IuaAA29ppQNYhtM66Rpq1ZVwoMRI7%0ATF5ZQAgAk7chjbm%2B4cg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1376162592/c4e51d6f0653e199f30db909eff6/ABCD123.png?expires=1784333700&signature=d1638e84937a99b23b649933ad534ff0f462bdf79dc87545d724d20c25b5da91&req=dSMgEMh4n4RWW%2FMW1HO4zYJdP2QiT63IuaAA29ppQNYhtM66Rpq1ZVwoMRI7%0ATF5ZQAgAk7chjbm%2B4cg%3D%0A)

### Benefits of MFA

* Provides enhanced security by protecting against unauthorized access.
* Reduces the risk of compromised passwords by requiring a second form of verification.

### Best Practices for SSO and Google Users

* Confirm with your SSO provider or Google Workspace administrator that MFA is enabled.
* Regularly review and update your login security settings to ensure compliance with institutional policies.

## Phone (SMS) MFA

To improve login reliability and security for internal users, Element451 offers **Phone Multi-Factor Authentication (MFA)** as an optional, administrator-enabled feature.

[![Login Method Modal](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2180166644/23981e4275de95d5b25557d28069/2-SMS-MFA-SELECT-METHOD.png?expires=1784333700&signature=8a6be91ef378e8cb6c6a2c738b676aca0d66e2898df56d3ca4ebe809f0eca6f1&req=diEvFsh4m4dbXfMW1HO4zf14I8QD8ItX3TR1uflQh06VonNvYjbUfN5fngvI%0AWR8dtrqcLzO%2BhNE%2BKHY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2180166644/23981e4275de95d5b25557d28069/2-SMS-MFA-SELECT-METHOD.png?expires=1784333700&signature=8a6be91ef378e8cb6c6a2c738b676aca0d66e2898df56d3ca4ebe809f0eca6f1&req=diEvFsh4m4dbXfMW1HO4zf14I8QD8ItX3TR1uflQh06VonNvYjbUfN5fngvI%0AWR8dtrqcLzO%2BhNE%2BKHY%3D%0A)

#### Why enable Phone MFA?

By default, internal users receive MFA codes via email. This works well in most cases, email delivery can occasionally be disrupted due to outages or delays outside of Element451’s control (e.g., institutional email downtime or provider-wide incidents).  
​

Phone MFA provides:

* **A backup authentication method** when email is unavailable
* **Improved login continuity** during outages
* **Greater flexibility** for internal users accessing the platform

Email MFA remains the primary method, but SMS can be used as an alternative when needed.

#### How to enable Phone MFA (Admin)

Administrators with the appropriate permissions can enable or disable Phone MFA for internal users:

1. Navigate to **Manage Users**
2. Select the **Security** tab
3. Toggle **Phone MFA** on or off

This setting is **optional** and can be configured based on your institution’s security policies.

#### What happens when enabled?

* Internal users will have the option to add and verify a **cell phone number** in their user profile
* Once verified, users can choose to receive MFA codes via **text message (SMS)** as an alternative to email during login
* Email MFA will still be sent by default; SMS acts as a **backup method**

**Note:** Cell phone numbers used for MFA are private and are not visible to students in StudentHub or other public facing listings.

---

# Session Duration

To ensure security, Element451 sessions are time-bound and require re-authentication regularly. However, we do not limit the number of concurrent sessions.

* **Element451 Username/Password**: 24 hours
* **SAML Single Sign-on**: 24 hours
* **Google**: 30 Days
* **Via Element451 Magic Links**: 48 Hours

**Good to Know**: Session expiration times are dynamically adjusted based on your login time and timezone to prevent logouts during work hours.

#

---