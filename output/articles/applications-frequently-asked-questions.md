---
title: 📌 Applications: Frequently Asked Questions
url: https://help.element451.com/en/articles/10607698-applications-frequently-asked-questions
collection: Applications
---

This article answers commonly asked questions about Applications, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389644501/ccafa149b6f55622619caab5a445/Pardon+our+Progress.png?expires=1784333700&signature=83a243c2a7da823cb3b4bbbe5f4503913842565c1973a195de90dc216175a255&req=dSMvH896mYRfWPMW1HO4zZQMYlT2E3FgwL%2B7zrOJVrq5H2u29S%2BRbJb04Q%2Bq%0AJoo4WTO0Nd1kqyXqu7I%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389644501/ccafa149b6f55622619caab5a445/Pardon+our+Progress.png?expires=1784333700&signature=83a243c2a7da823cb3b4bbbe5f4503913842565c1973a195de90dc216175a255&req=dSMvH896mYRfWPMW1HO4zZQMYlT2E3FgwL%2B7zrOJVrq5H2u29S%2BRbJb04Q%2Bq%0AJoo4WTO0Nd1kqyXqu7I%3D%0A)

# General

## Can I delete a student's application submission or decision?

Yes, you can.

1. Navigate to the **Applications** profile card on the contact's profile.
2. Open the application.
3. Click the red **Delete Application** button at the bottom.

## Can I access a student's application portal or impersonate them to see what they’re seeing?

Yes, you can use the **"Login as User"** option on an application page to view the portal as a student. To do this:

1. Navigate to the **contact's profile.**
2. Locate the **Applications** profile card.
3. Click on the relevant application.
4. Click the **"Login as User"** button to access the application portal as the student.

## How can I preview or test an application before making it active for students?

Create a **test application site** that is not accessible to anyone else. Set your application to be available **only** on that test site. This lets you privately access and test the application before making it live. Once you're finished testing, update the settings to make the application available on your actual application site.

## When is application data saved to an applicant's profile?

Application data is saved automatically in real-time as the applicant progresses. This ensures that their work is never lost—they can start the application, leave, and return later to pick up where they left off. Their progress is continuously recorded, so they don’t need to worry about manually saving their work.

## Can the term or major field be left blank when starting an application?

Yes, the application form allows the term and major fields to be left blank, either by not including them on the registration form or by not making them required. However, duplicate applications with the same major and term combination are not allowed.

## Our AI Fraud Detector Agent is flagging legitimate international applicants as suspicious. What should we do?

Enable the option for the agent to expect international addresses. This tells it to anticipate IP addresses outside the U.S., reducing false fraud alerts for global applicants. You can find this setting in the application-level settings.

## We’re hosting an event where many students will apply from the same Wi-Fi network, and some are getting blocked. How can we fix that?

In the application-level settings, you can increase your **registration rate limit**. This allows more applications per minute from the same IP address—helpful for fairs, open houses, or group application events. Afterward, return the limit to a lower number to maintain normal protection.

## I set up a Submission Prevention Rule to prevent students from submitting multiple applications for the same term, but students can still submit.

The most common cause is using an inline **User Segment** condition in your rule's conditional logic. User Segment conditions are scoped to the current application only—the system evaluates data within that single application and cannot detect whether the student has already submitted a different application for the same term.  
​

To enforce cross-application logic, use a **User Segment Reference** condition instead. Create a saved segment on the People page that captures the criteria (e.g., students who have already submitted an application for the target term), then reference that segment in your rule. User Segment Reference conditions evaluate the student's full contact record and are not limited to the current application.  
​

*This same behavior applies to Payment Rules and Identity Verification Rules—use User Segment Reference when your condition needs to span multiple applications.*

---

# Application Sites/Dashboard

## Can I control the order in which applications appear on the application site when a student chooses which one to apply to?

Yes. You can reorder your application list from the **All Applications** screen (Applications > All Applications). This order will be reflected on your application site. Just note—this applies globally. The same order is used across all application sites; you can’t customize it per site.

## Can I adjust the "Pay Deposit" button color?

Yes. The button color on the application dashboard header uses the Primary Color set at the Application Site level. To change it, navigate to **Application** > **Applications** > **Sites**, select your Application Site, and update the Primary Color.

**Where can I adjust my application dashboard header color?**

Navigate to **Application** > **Applications** > **Sites** and click on your Application Site. From there, click the **Application** tab and locate the "**Header Design**" section. You can adjust the background color, add a gradient, or upload your own image.

## Can we turn off the confetti on the admitted or conditional offer greeting message?

Yes. Edit the application and go to **Content** > **Dashboard**. Click the pencil next to the **Greeting Message - Admitted** or **Greeting Message - Conditional Offer**, and in the **Acceptance Message Setup** section, switch **Show Confetti** off. Confetti is on by default, and the setting is applied per application, so turning it off affects only the application you edit.

---

# Request Information Forms

## How can I check if applicants have waived their right to view the "request information form" submitted for them (e.g., letters of recommendation, transcript requests, etc.)?

The system includes a built-in waiver question at the bottom of the applicant's form that asks, *“Do you waive your right to view information sent on your behalf?”* This question cannot be edited or removed and requires a yes or no response. Regardless of their answer, the recommender’s response is not visible to the applicant within the platform.

You can check an applicant's waiver status in two ways:

1. **Individual Check** – Navigate to the applicant’s profile and view the Activity card. Filter the activity to **Info Request** to see their waiver response.
2. **Bulk Search** – Use **Segments** to find multiple applicants based on their waiver status. Create a segment using the filter *Info Request > Received Recommendation* and select the **waiver property** to filter by *true*, *false*, or *blank*.   
   ​  
   Pro Tip: If you create a **calculated segment**, you can use it in a **workflow** to automatically add a label to contacts based on their waiver response. For example, you could create a label indicating applicants who did *not* waive their right.

---

# Majors, Terms, Degrees, Campuses

## How can I manage and configure application terms for students?

Application terms are managed in **Data Sources** (**Data + Automation > Data Sources**). Here, you can:

* **Add and configure terms** to define available application periods.
* **Set start and end dates** for each term.
* **Determine which applications, campuses, and schools** the term applies to.
* **Mark terms as active or inactive** to control availability.

---

# Payments + Deposits

## Can I allow applicants to submit their application without paying the application fee while still requiring it as a checklist item?

Yes, you can disable the payment requirement for submission while keeping it as a checklist item. To do this, edit the application and go to **Payment Settings**. Set **"Required to Submit"** to **"No."** This allows applicants to submit their application without immediate payment.

Since application fees are not automatically added as checklist items, you'll need to add a checklist item for the fee manually. We recommend making it a **conditional checklist item** with application filters applied (e.g., **"Application Payment Type is Credit Card"**) to ensure it is automatically marked as complete for your use case.

Additionally, include clear instructions in the checklist item on how to pay the fee, such as: *"To pay the fee, click 'Pay Fee' in the left-hand menu of your application dashboard."*

## Is there a way to hide the deposit button?

Yes, you can turn off deposits in the application settings by going to Applications > Applications > Application Settings > Deposits. The button will also automatically hide if you're using a payment rule and the student doesn’t meet the conditions.

---

# Supplemental Forms

## How do I send supplemental forms to students after they submit their applications?

Supplemental Forms are automatically added as a checklist item to the relevant application based on your configuration. To enhance the process, you could:

* Customize the **“Greeting Message - Submitted”** in the application dashboard settings to inform students about their next steps, such as completing a transcript request form.
* Create a **workflow** that sends communications guiding students through the next steps. Once a student joins a calculated segment of applicants who have submitted their application, they can be automatically enrolled in the workflow.

## Can I duplicate a supplemental form?

Supplemental forms cannot be duplicated at this time. You’ll need to create a new form from scratch if a copy is needed.

---