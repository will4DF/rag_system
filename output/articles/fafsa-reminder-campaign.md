---
title: FAFSA Reminder Campaign
url: https://help.element451.com/en/articles/6825340-fafsa-reminder-campaign
collection: Packs
---

Customize and install the FAFSA Reminder Campaign Pack.

# Overview

[![](https://downloads.intercomcdn.com/i/o/637882872/f09f3001fcebeb99b84f6728/image.png?expires=1784333700&signature=83bf711214a1d0806ac4fa5c9b4b099a25131da55b9197eaa80b91962e03dcbf&req=ciMgHsF8lYZdFb4f3HP0gDbYIgtNjBlzPhbNEmKCgF75TIPKmhJn80x%2FstQ9%0AsVxAGt3wFzNjJRvAuA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/637882872/f09f3001fcebeb99b84f6728/image.png?expires=1784333700&signature=83bf711214a1d0806ac4fa5c9b4b099a25131da55b9197eaa80b91962e03dcbf&req=ciMgHsF8lYZdFb4f3HP0gDbYIgtNjBlzPhbNEmKCgF75TIPKmhJn80x%2FstQ9%0AsVxAGt3wFzNjJRvAuA%3D%3D%0A)

The FAFSA Reminder Campaign Pack is an email and SMS campaign that sends reminder messages to encourage submitting the Free Application for Federal Student Aid (FAFSA). This is a crucial first step for most institutions' financial aid offices to begin building aid packages for prospective and current students.

​**​**This Pack can be used by any institution serving students who are eligible for federal student aid. One of the most important factors in ensuring students graduate from your school is securing the financial support needed to pay for their education. This Pack reminds recipients to complete their application and explain the benefits and steps required in filing their FAFSA, with content pre-written with information from the U.S. Department of Education Federal Student Aid website.

![](https://downloads.intercomcdn.com/i/o/1084660778/e2359b3e16e165752f58115f/Note-Orng.png?expires=1784430000&signature=24427dba22df56e425ae20f04091f32c5c4588590e24b5c768bd7434b37ed1ff&req=dSAvEs94nYZYUfMW3Hu4gdNc67aFMx%2F3LhkhjWpOYSUB%2FzG38vGU3qSRGBZT%0A9g%3D%3D%0A) To use any Pack in the Library, you must first set up your Packs Tokens. [Click here to learn more about Packs Tokens](https://help.element451.com/en/articles/6825249-guide-to-packs-tokens).

## Video Guide

## Pack Install Options

When installing the Pack, you’ll need to configure the following options.

* **Call-to-action button Link**

  + By default, the CTA link goes directly to the FAFSA landing page on studentaid.gov <https://studentaid.gov/h/apply-for-aid/fafsa>
  + Some institutions would prefer to use their own financial aid landing page to provide extra instructions and context for the user. Enter the URL for that page in this field if this is the case.
* **Audience segment**

  + You can pre-load a segment of prospective or current students with incomplete FAFSA applications here.
* **Completed FAFSA users segment**

  + Choose the segment of prospective or current students who have completed their FAFSA. This will be used to determine the send condition in the installed workflow. Users with a complete FAFSA (based on this segment) will not receive reminder emails.
  + Some schools may use a custom label to build this segment. [Learn more about applying labels to segments](https://help.element451.com/en/articles/1474167-apply-a-label-to-a-segment)
* **Contact information**

  + You can select your names and email addresses as displayed on the installed email/SMS components here.
* **Communication frequency**

  + Determines how often reminder messages are sent (weekly by default)

---

# Reviewing the Workflow and Email/SMS Messages

Before activating the campaign, you should review all the included components in this Pack. After installing the pack, you can see a list of these.

[![](https://downloads.intercomcdn.com/i/o/637883081/0d791e4f300b8424704ba8c4/image.png?expires=1784333700&signature=fa771a1db7495583ebd2c269e81b5234e3e5d7d147a9c7071fc8d60e1e084ac6&req=ciMgHsF9nYleFb4f3HP0gMrZaMVHdqYVLN%2F2k8gIFEXXxLt4x2Q0yAxCpPu8%0Ah6Mw3m%2Bt55oaXt4zZA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/637883081/0d791e4f300b8424704ba8c4/image.png?expires=1784333700&signature=fa771a1db7495583ebd2c269e81b5234e3e5d7d147a9c7071fc8d60e1e084ac6&req=ciMgHsF9nYleFb4f3HP0gMrZaMVHdqYVLN%2F2k8gIFEXXxLt4x2Q0yAxCpPu8%0Ah6Mw3m%2Bt55oaXt4zZA%3D%3D%0A)

## Email/SMS Components

The emails included with this campaign come with suggested pre-written content with tips and advice about the FAFSA from the Department of Education with call-to-action links to submit the application.

### Click here to preview an email

[![](https://downloads.intercomcdn.com/i/o/637883212/bd9e850477b0da01b981fe2d/image.png?expires=1784333700&signature=24d65e788e519bb22c4b9c10c147566d2697af6893a1fc121c4a5907162acc0f&req=ciMgHsF9n4BdFb4f3HP0gFQ6g1I%2FBXiM6DNY%2BUeGtQrqcfz2dy9kZQlfo3Nc%0AfHq0TdvSG6oDbISusw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/637883212/bd9e850477b0da01b981fe2d/image.png?expires=1784333700&signature=24d65e788e519bb22c4b9c10c147566d2697af6893a1fc121c4a5907162acc0f&req=ciMgHsF9n4BdFb4f3HP0gFQ6g1I%2FBXiM6DNY%2BUeGtQrqcfz2dy9kZQlfo3Nc%0AfHq0TdvSG6oDbISusw%3D%3D%0A)

This also includes the following tokens:

* **[user:first\_name, fallback="there"]**

  + Displays the user's first name with a fallback option in the event it isn't in the system (unlikely).
* **[client:name]**

  + Displays your institution's name as specified in your Pack tokens
* **[content:formula]**

  + Used to calculate the number of weeks since the FAFSA has been open. E.g., “The FAFSA has been open for 8 weeks now…”

**Feel free to edit the messages as you see fit or add any additional information or context for the recipient about the next steps in this process.**  
​

*You can access your email/SMS components under* **Engagement > Campaigns > Ongoing Communications**.

## Workflow Components

The installed workflow is available under **Data + Automations > Workflows > All Workflows**.

[![](https://downloads.intercomcdn.com/i/o/637884258/0380b15affc5c932127416d3/fafsa_workflow.gif?expires=1784333700&signature=3f06de11968efce67ef8ab7b201de95a56ff1f7017216c6ca8059c8ed42437f1&req=ciMgHsF6n4RXFb4f3HP0gALc3%2F0bn2gFZBsLMKMqFfBp1JsAhZRqRM9KsLNQ%0AEdWoY0KcespJTEaApQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/637884258/0380b15affc5c932127416d3/fafsa_workflow.gif?expires=1784333700&signature=3f06de11968efce67ef8ab7b201de95a56ff1f7017216c6ca8059c8ed42437f1&req=ciMgHsF6n4RXFb4f3HP0gALc3%2F0bn2gFZBsLMKMqFfBp1JsAhZRqRM9KsLNQ%0AEdWoY0KcespJTEaApQ%3D%3D%0A)

This will automate the campaign.

Each step in the workflow will determine if the user has completed their FAFSA application by checking to see if they have been added to the completed FAFSA segment specified in the Pack install options.

---

# Activating the Campaign

[![](https://downloads.intercomcdn.com/i/o/637884507/68375174bbbb58557086e497/fafsa_activate.gif?expires=1784333700&signature=d2a1d258ffc1d1e3c24169d25183b214b642ba838f73a29239f596a942ff9a39&req=ciMgHsF6mIFYFb4f3HP0gMSspRdqoAt7h29cWLjXB2dsMeBvEGcaneDj64zc%0AQl8hUfwS7txWsOlgPg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/637884507/68375174bbbb58557086e497/fafsa_activate.gif?expires=1784333700&signature=d2a1d258ffc1d1e3c24169d25183b214b642ba838f73a29239f596a942ff9a39&req=ciMgHsF6mIFYFb4f3HP0gMSspRdqoAt7h29cWLjXB2dsMeBvEGcaneDj64zc%0AQl8hUfwS7txWsOlgPg%3D%3D%0A)

After you have reviewed your email/SMS messages and your workflow, set your workflow status to ***active*** to begin running the campaign.

---