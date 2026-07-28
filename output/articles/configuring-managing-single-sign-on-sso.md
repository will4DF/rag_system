---
title: Configuring + Managing Single-Sign-On (SSO)
url: https://help.element451.com/en/articles/10542911-configuring-managing-single-sign-on-sso
collection: Settings + Permissions
---

# Overview

Element451 supports Single Sign-On (SSO) for both internal users (staff/faculty) and external users (students). This guide walks you through configuring SSO, managing metadata updates, and ensuring seamless authentication for your users. Internal users can now be matched on email, School ID, or SSO ID, so institutions whose IdPs return a non-email identifier can authenticate staff and faculty without forcing email as the matching attribute.

If you're looking for guidance on enabling SSO or other authentication methods, visit our [Security + Authentication Settings](https://help.element451.com/en/articles/8569773-security-authentication-settings) help article.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1376137531/1455490c785a7f31526070d148a7/Screenshot-2B2023-12-05-2Bat-2B12_25_30-E2-80-AFPM.png?expires=1784333700&signature=654f8808f6bbacf8ee073352c4abf081c1de8774ae1553c975c93002068ea752&req=dSMgEMh9moRcWPMW1HO4zTBrEpsJRy2ulLCA2i5gWUFLbsje4uZ7aTye%2Bp9x%0A5b9IPNCckXwUXR42Tjk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1376137531/1455490c785a7f31526070d148a7/Screenshot-2B2023-12-05-2Bat-2B12_25_30-E2-80-AFPM.png?expires=1784333700&signature=654f8808f6bbacf8ee073352c4abf081c1de8774ae1553c975c93002068ea752&req=dSMgEMh9moRcWPMW1HO4zTBrEpsJRy2ulLCA2i5gWUFLbsje4uZ7aTye%2Bp9x%0A5b9IPNCckXwUXR42Tjk%3D%0A)

---

# Configuration of SSO

To use your school's SAML2 SSO provider for either internal users (staff) or external users (students/contacts), you'll need to add your metadata to the SSO Authentication Settings:

1. **Navigate to SSO Settings**

   * Settings > Manage Users > Security  
     ​
2. **Find the Appropriate User Type Section**

   * SSO must be configured separately for **Internal Users** (staff/admins) and **External Users** (students).
   * On this page, locate the relevant section:

     + **SSO Authentication for Internal Users**
     + **SSO Authentication for External Users**  
       ​

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1376120731/bb38e5642981804f3d229b765dc9/Screenshot-2B2024-02-08-2Bat-2B2_07_40-E2-80-AFPM.png?expires=1784333700&signature=6d6aee80ea467489b3fbf3db3b182fad2028092178c36b1795ca7990e065948e&req=dSMgEMh8nYZcWPMW1HO4zbWOsPH%2FBuvk416rnpxbQfqvawu8yj8FmxJBvRcx%0A2vn2%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1376120731/bb38e5642981804f3d229b765dc9/Screenshot-2B2024-02-08-2Bat-2B2_07_40-E2-80-AFPM.png?expires=1784333700&signature=6d6aee80ea467489b3fbf3db3b182fad2028092178c36b1795ca7990e065948e&req=dSMgEMh8nYZcWPMW1HO4zbWOsPH%2FBuvk416rnpxbQfqvawu8yj8FmxJBvRcx%0A2vn2%0A)

---

# SSO for Internal Users (Admins/Staff/Faculty)

1. **Create a New SSO Configuration**

   * Click the **+ Create SSO Authentication** button under **SSO Authentication for Internal Users**.
2. **Enter Metadata**

   * Paste your **SSO Metadata URL** or **XML** provided by your Identity Provider (IdP). 📌 **Note:** If you're also prompted to enter a `single sign-on service provider URL`, please [contact Element451 Live Support](https://intercom.help/element451/en/articles/9717577-element451-live-support-access-assigning-seats) for assistance.
3. **Save** **your Configuration**
4. **Confirm that SSO is enabled** for Internal Users in Authentication Settings.

## Internal SSO User Matching

Internal SSO matching is **automatic** — there is no matching settings card for internal users. Element451 takes the value returned by your identity provider and checks it against three fields on each internal user, signing the user in if any of them match:

* **Email:** The user's primary email.
* **School ID:** A stable institutional ID, such as the value printed on a staff badge or used for HR and business records.
* **SSO ID:** The identifier your identity provider returns in its SAML response.

To enable School ID or SSO ID matching, add the value on the internal user's profile under **Basic Info**. Whichever attribute your IdP sends, if it matches one of these fields on an internal user, that user is signed in.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2410506148/b5555dbee460eb1c319e20a716ad/CleanShot+2026-05-21+at+12_59_37.png?expires=1784333700&signature=86dece7b0f0976769abeae019976d2e896e204767a5bf1dcac57fc5f653d080e&req=diQmFsx%2Bm4BbUfMW1HO4zZGK%2BsR%2B7NoOcBTw%2BfPc64KAUZoF%2BQtSPXqFQ3M%2B%0AuvvqdLrzTQ9hJVXzXG0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2410506148/b5555dbee460eb1c319e20a716ad/CleanShot+2026-05-21+at+12_59_37.png?expires=1784333700&signature=86dece7b0f0976769abeae019976d2e896e204767a5bf1dcac57fc5f653d080e&req=diQmFsx%2Bm4BbUfMW1HO4zZGK%2BsR%2B7NoOcBTw%2BfPc64KAUZoF%2BQtSPXqFQ3M%2B%0AuvvqdLrzTQ9hJVXzXG0%3D%0A)

---

# SSO for External Users (Students)

1. **Create a New SSO Configuration**

   * Click the **+ Create SSO Authentication** button under **SSO Authentication for External Users**.
2. **Enter Metadata**

   * Paste your **SSO Metadata URL** or **XML** provided by your Identity Provider (IdP). 📌 **Note:** If you're also prompted to enter a `single sign-on service provider URL`, please [contact Element451 Live Support](https://intercom.help/element451/en/articles/9717577-element451-live-support-access-assigning-seats) for assistance.
3. **Save** **your Configuration**
4. **Confirm that SSO is enabled** for External Users in Authentication Settings.

## External SSO User Matching

Once SSO is enabled and configured for external users, an "External SSO User Matching" settings card will appear. This is where you choose how Element451 matches external users from your identity provider response.

* **Email (default):** Element451 matches the value returned by the identity provider against any of the user's email fields: primary email, email identity, or school email.
* **Identities:** Administrators can select a single identity attribute to match against. Options: Primary Email, Email Identity, School Email, School ID, or Username ID. When an identity is selected, matching occurs exclusively against that attribute.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2249769410/d0b7b8694375c0023001c3add06b/Config+SSO+-+External+User+Matching.png?expires=1784333700&signature=4513dd2cc6556c3aaa2d1eeafad7509a7070a43d3ad15adf19a013de6ef2877e&req=diIjH854lIVeWfMW1HO4zV0ltYwx30wp%2BrGzi6KkCKufWhNGp3P4XU56PoiI%0AO9kGh46Ty%2BFf28G7YB8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2249769410/d0b7b8694375c0023001c3add06b/Config+SSO+-+External+User+Matching.png?expires=1784333700&signature=4513dd2cc6556c3aaa2d1eeafad7509a7070a43d3ad15adf19a013de6ef2877e&req=diIjH854lIVeWfMW1HO4zV0ltYwx30wp%2BrGzi6KkCKufWhNGp3P4XU56PoiI%0AO9kGh46Ty%2BFf28G7YB8%3D%0A)

---

# 🚨 Important Notes

* **Service Provider (SP) URL:** If your IdP requires an SP URL before generating metadata, [contact Element451 Live Support](https://intercom.help/element451/en/articles/9717577-element451-live-support-access-assigning-seats).

* **NameID Mapping:** Ensure that the SAML2 **`NameID`** attribute maps to the value Element451 will match on. For most setups that's the **`emailAddress`** value, but for internal users you can also send School ID or SSO ID, and for external users you can configure matching against another identity attribute.

* For successful SSO login, the value returned in the SAML response must match a [user account](https://help.element451.com/en/articles/2735199-adding-managing-internal-users) in Element451 — by email, or by an identity value (School ID or SSO ID for internal users; the configured matching attribute for external users).

Learn how to add internal users to Element451 [here](https://intercom.help/element451/en/articles/2735199-adding-managing-internal-users).

---

# Renewing Your SSO Certificate

If your SSO signing certificate is set to expire, you'll need to update the certificate to maintain uninterrupted authentication. **Element451 does not actively monitor your metadata for updates**. Therefore, it's important to remember to update your metadata when your certificate is renewed:

1. Work with your SSO provider to regenerate your SSO signing certificate. Once this is done, the updated certificate will be reflected in your metadata URL/file.
2. Navigate to **Settings** > **Manage Users** > **Security**.
3. Locate the expired authentication.
4. Replace the current metadata with your updated metadata URL or file.
5. Save your changes.

---