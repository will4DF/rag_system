---
title: Zoom Integration: Troubleshooting
url: https://help.element451.com/en/articles/8927495-zoom-integration-troubleshooting
collection: Events
---

Learn how to troubleshoot common issues when using the Element451 + Zoom integration.

# Overview

This article walks you through troubleshooting common issues using the Element451 + Zoom integration.

---

# Frequently Asked Questions + Troubleshooting

* ### I can't access the Events module

  Check with an Element451 administrator at your institution to ensure you have the correct permissions for the Events module.   
  ​
* ### I received a "pre-approval" error from Zoom.

  [![](https://downloads.intercomcdn.com/i/o/957876034/b85360ab6fcafb46097a3457/Screenshot+2024-02-08+at+4.58.36%E2%80%AFPM.png?expires=1784333700&signature=c794aa0976d4f2bf8f8228b2a2fbed79f10363f33bf7b2acd8d9ba9b5eccb859&req=fSUgHs54nYJbFb4f3HP0gIkE4KOw6qYNO9FIjESFNvpTfNbViAQE53z3%2BxWY%0AeKY%3D%0A)](https://downloads.intercomcdn.com/i/o/957876034/b85360ab6fcafb46097a3457/Screenshot+2024-02-08+at+4.58.36%E2%80%AFPM.png?expires=1784333700&signature=c794aa0976d4f2bf8f8228b2a2fbed79f10363f33bf7b2acd8d9ba9b5eccb859&req=fSUgHs54nYJbFb4f3HP0gIkE4KOw6qYNO9FIjESFNvpTfNbViAQE53z3%2BxWY%0AeKY%3D%0A)

  If you received the "*Unable to install this app because it needs pre-approval by your account admin. Please contact your account admin for more details."* error when authenticating the integration, your Zoom administrator must grant a pre-approval for Element451 through the Zoom App Marketplace. Here's how:

  1. [Navigate to this link](https://marketplace.zoom.us/apps/eF70b_cBTLCTvlK3uy_VEQ), or open the Zoom App Marketplace and find Element451.
  2. Where it says Install Permissions, toggle on **Approve Install of this App.** If you are part of your institution's Zoom account, you may see a **Request Pre-Approval Option** instead. This will allow you to send a request to your administrator. The administrator will receive an email from Zoom with instructions.
  3. Once approval has been granted, you can continue adding the Element451 + Zoom integration.   
     ​
* ### My event attendees are not marked as 'attended' even though they attended the Zoom.

  Attendees **must sign into Zoom with an email address matching the email address on their record in Element451** to be marked Attended.  
  ​
* ### The Zoom meeting link won't add to my event.

  As a security measure, Zoom limits the number of meeting creation and update requests 3rd party applications can make in a single day. As of January 2024, the request limit is 100. However, in some cases, Element451 must make multiple requests when creating or updating an event. This limit is tied to your Zoom account and resets daily at midnight UTC.  
  ​
* ### I can't select multiple days of the week for my repeatable event.

  When setting up a recurring Zoom event date, the options work differently than when setting up a non-Zoom event. You can only choose **one** day of the week for the event to repeat on any particular event date. For example, if your event happens on both Mondays and Wednesdays, you should set up separate event dates for Mondays and Wednesdays instead of including them both on the same event date.

  [![](https://downloads.intercomcdn.com/i/o/1070354508/0f6074de6908b1116be5e420/Screenshot+2024-06-03+at+1_40_14%E2%80%AFPM.png?expires=1784333700&signature=4646b264a62175d5862206973507301ceddd4dbb3caf3bfca4396dad3c0317fc&req=dSAgFsp7mYRfUfMW1HO4zYnK0meE%2FXjEbg5oDOUEL0%2BeNc8FinyNVS6FoFV1%0A%2Fidn%0A)](https://downloads.intercomcdn.com/i/o/1070354508/0f6074de6908b1116be5e420/Screenshot+2024-06-03+at+1_40_14%E2%80%AFPM.png?expires=1784333700&signature=4646b264a62175d5862206973507301ceddd4dbb3caf3bfca4396dad3c0317fc&req=dSAgFsp7mYRfUfMW1HO4zYnK0meE%2FXjEbg5oDOUEL0%2BeNc8FinyNVS6FoFV1%0A%2Fidn%0A)

---