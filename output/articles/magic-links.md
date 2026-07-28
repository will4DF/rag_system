---
title: Magic Links
url: https://help.element451.com/en/articles/8106669-magic-links
collection: People
---

Learn how to use Magic Links to bypass site authentication and pre-fill forms.

# Overview

Magic Links, unique alphanumeric **short-term** **identifiers** **created** **by** **login** **tokens**, are a powerful tool for Element451 to identify a student and link them to an existing record. They offer a time-saving solution by allowing students to bypass the authentication process, eliminating the need to log in.

Moreover, Magic Links can pre-fill known information on forms, a feature that significantly enhances the user experience. This is especially useful when students navigate between their inbox and your site, as it reduces friction and improves efficiency.

---

# How Do Magic Links Work?

1. Add a login token to an email or SMS Campaign.

   [![](https://downloads.intercomcdn.com/i/o/1067120116/7d673942538ffb8530eb0a35/Screenshot+2024-05-30+at+5_14_21%E2%80%AFPM.png?expires=1784333700&signature=17dbff5b33e09234a4515b2f280803ce30d0d3ed13ce4c25e98b5de308d8a6fc&req=dSAhEch8nYBeX%2FMW1HO4zYA36LFBBtfSi4%2BU6kpHbD0F7n06DOgMQ4U8obk4%0AoKkf%0A)](https://downloads.intercomcdn.com/i/o/1067120116/7d673942538ffb8530eb0a35/Screenshot+2024-05-30+at+5_14_21%E2%80%AFPM.png?expires=1784333700&signature=17dbff5b33e09234a4515b2f280803ce30d0d3ed13ce4c25e98b5de308d8a6fc&req=dSAhEch8nYBeX%2FMW1HO4zYA36LFBBtfSi4%2BU6kpHbD0F7n06DOgMQ4U8obk4%0AoKkf%0A)
2. Configure the login token properties. When you insert a login token, you'll be prompted to configure its properties:

   * Depending on the token selected, you'll need to specify specific things. For example, if you choose the **Application** **Login** **URL**, you must select an application, add your site URL, and configure other settings.
   * **Campaign, Source, Medium**: Add the UTM parameters you wish to track.
   * **TTL Unit:** Magic Link [expiration](#h_1fe5b2d02d) unit (days, weeks, etc.)
   * **TTL: Value**: Magic Link [expiration](#h_1fe5b2d02d) numerical value

   [![](https://downloads.intercomcdn.com/i/o/877656754/65ccf09466fcef0ceeef6d29/magic+link+token.png?expires=1784333700&signature=309d882d484357491e46b3f13263c77e3462a81e5ed97f003355950b4f83262c&req=fCcgEMx4moRbFb4f3HP0gAMTSJIRZDJtqQn%2BG08QdYukUtFdog0TIn9gX%2Flv%0Aw4c%3D%0A)](https://downloads.intercomcdn.com/i/o/877656754/65ccf09466fcef0ceeef6d29/magic+link+token.png?expires=1784333700&signature=309d882d484357491e46b3f13263c77e3462a81e5ed97f003355950b4f83262c&req=fCcgEMx4moRbFb4f3HP0gAMTSJIRZDJtqQn%2BG08QdYukUtFdog0TIn9gX%2Flv%0Aw4c%3D%0A)
3. Send the Campaign. When the Campaign is sent, a Magic Link is automatically generated using your configured token parameters.

   * The student can access the Magic Link by email or SMS.
   * You can access the Magic Link from the [student's profile card](#h_991b3560f3).

## Magic Link Expiration

* When configuring your token properties, you have two settings: TTL Unit and TTL Value. TTL stands for Time to Live, the duration a token remains valid.
* If TTL settings are left blank, the magic link will expire 48 hours after creation.

![](https://downloads.intercomcdn.com/i/o/1067098825/33f7138ea5736191b19ef6d6/Pro+Tip+-+Orng.png?expires=1784430000&signature=80f71b41086e065c5ac488fb07875442d2bbabf6fe619ebb52a35f3b05352919&req=dSAhEcl3lYldXPMW3Hu4gTAQ424oFi9oFlebgTDBZJnVUpWHYy1YI6CQxFDl%0AqA%3D%3D%0A) We recommend hyperlinking text or adding the token to a button for the best visual experience.

---

# Login Tokens that Generate Magic Links

You will see several different “login” tokens when adding a token to a Campaign. There are two types of Login Tokens: **Login** **URL** and **Login** **Token**.

* **Login URL**: Outputs a hyperlink URL containing the magic link the student can click.

  + Example: <https://training.app451.sites.451.io/login/SwOI4fzreBeYkRCtaekA>
* **Login Token**: Outputs the magic link alphanumeric code only.

  + Example: SwOI4fzreBeYkRCtaekA

The examples above show that the magic link is the same for both (SwOI4fzreBeYkRCtaekA). However, when you use the URL option, the URL is configured and generated for you.

In most cases, we recommend using the Login URL. When adding the Login URL, you are prompted to configure properties (such as the specific application, form, page, or microsite, and the campaign, source, and medium for tracking purposes) the system uses to create the URL.

When you want to create a URL manually using a non-expired magic link code, you can do so by following the steps in the [Magic Links Profile Card](#h_991b3560f3) section below.

---

# Login URL Options

|  |  |
| --- | --- |
| **Token Name**  `Shortcode/Token` | **URL Output Action** |
| **Application Login URL**  `[application:login_url]` | Directs students to a specific Application/Application Site.  * Students **without** an existing application land on the **registration** **form;** any known data will pre-populate fields. * Students **with** an existing application bypass the authentication process and can pick up where they left off. |
| **Form** **Login** **URL** ​`[form:login_url]` | Directs students to a specific Form and pre-populates fields based on known data. |
| **Site451** **Login** **URL** ​`[microsite:login_url]` | Directs students to a specific Microsite, bypassing the authentication process. |

# Login Token Options

|  |  |
| --- | --- |
| **Token Name**  `Shortcode/Token` | **Description** |
| **Application** **Login** **Token** `[application:login_token]` | Outputs the Magic Link alphanumeric code only. |
| **Form** **Login** **Token** `[form:login_token]` | Outputs the Magic Link alphanumeric code only. |
| **Site451** **Login** **Token** `[microsite:login_token]` | Outputs the Magic Link alphanumeric code only. |
| **Landing** **Page** **Token** `[landingpage:login_token]` | This token is used when you wish to pre-populate data fields on a form embedded on an Element451 Page. You can generate both URLs and codes depending on your use case. Explore this topic more in the [Pre-Populated Forms](https://help.element451.com/en/articles/9320127-pre-populating-forms-on-pages) article. |

---

# The Magic Links Profile Card

Active, non-expired Magic Link codes are visible on the student profile on the Magic Links Profile Card.

![](https://downloads.intercomcdn.com/i/o/1067128437/2e55259dcb62b0b3eca66d72/Note-Orng.png?expires=1784430000&signature=62d16ebbf10e01b2c58270cf5dc5434648d1a67ccb6bc9f62881c6096eb39e9c&req=dSAhEch8lYVcXvMW3Hu4gSKz9Ia5NU%2BnOJmP5xBrWhsOKeXhAuPqKMiaGvoj%0A7w%3D%3D%0A) The Magic Links card must be enabled for your profile template. For more information on profile templates, visit [this article](https://help.element451.com/en/articles/6449965-bolt-profile-templates).

[![](https://downloads.intercomcdn.com/i/o/780666854/933591ca695a97ec3be8e27e/Screenshot+2023-07-07+at+4.08.01+PM.png?expires=1784333700&signature=93cf26bd47d16b13461a1bb1d5afac68d5ebab69f665135380af4ffbca5cc7e8&req=cygnEM94lYRbFb4f3HP0gBDi8Lp78wBwl7U0BW9gZND8TkfClTqyNJ73Wx6A%0AeWNEJOGZbYXjvMHBPg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/780666854/933591ca695a97ec3be8e27e/Screenshot+2023-07-07+at+4.08.01+PM.png?expires=1784333700&signature=93cf26bd47d16b13461a1bb1d5afac68d5ebab69f665135380af4ffbca5cc7e8&req=cygnEM94lYRbFb4f3HP0gBDi8Lp78wBwl7U0BW9gZND8TkfClTqyNJ73Wx6A%0AeWNEJOGZbYXjvMHBPg%3D%3D%0A)

* Select the **eye** **icon** to reveal the code.
* Select the **square/paper** **icon** to copy the code.

You can use this feature if you need to manually send a link to a student to log into their application portal or a microsite and they have a non-expired magic link code.

To do this, add `/login/{{magic_link}}` to the end of the URL you are sending, using the code copied from the card where it says `{{magic_link}}`.

---

# Frequently Asked Questions

### When should I use Magic Links?

Since Magic Links allows you to log students into an Application Site or Microsite seamlessly, you could use them whenever you prompt your student to access those sites. Using the pre-populated form feature, you could also use them to get updated student information.

* Nudge students to finish and submit an application
* Send admitted students to a Microsite
* Collect updated or additional information from students

---