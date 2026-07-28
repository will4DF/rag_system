---
title: Tokens for Events Messages
url: https://help.element451.com/en/articles/6067308-tokens-for-events-messages
collection: Events
---

Learn how to personalize events messages.

# Overview

In this article, you will learn how to personalize [event messages](https://help.element451.com/en/articles/1524108-event-messaging-and-notifications) with tokens, as well as the different tokens you can use.

---

# How to Use Tokens

Including a token in your event email and SMS messages is simple.

* **Legacy Builder**: When using the **legacy** builder, you should select a token from the toolbar when editing an email. This builder supports a limited number of tokens and selecting one from the list ensures compatibility.
* **Email Builder**: When using the email builder, you can select a token from the toolbar or manually add one. If manually adding a token, enter the token text enclosed in brackets [ ]. Tokens can be used in the subject line of an email or the body of an email or SMS message.

[![](https://downloads.intercomcdn.com/i/o/1001999886/8f44505a3ab281363f630919/Events+-+Insert+Token.gif?expires=1784333700&signature=8733c552e69c46d78a24dd14f0ed008203709301c5d936c828b13c480ff7d451&req=dSAnF8B3lIlXX%2FMW1HO4zd%2FbDzcp6pXS%2FQrBqHK2z2QZM9xH8bB5pdmSvNou%0AtG0nuuAmhBwKAkDu1%2Fk%3D%0A)](https://downloads.intercomcdn.com/i/o/1001999886/8f44505a3ab281363f630919/Events+-+Insert+Token.gif?expires=1784333700&signature=8733c552e69c46d78a24dd14f0ed008203709301c5d936c828b13c480ff7d451&req=dSAnF8B3lIlXX%2FMW1HO4zd%2FbDzcp6pXS%2FQrBqHK2z2QZM9xH8bB5pdmSvNou%0AtG0nuuAmhBwKAkDu1%2Fk%3D%0A)

***See Example of Using Brackets***

The following screenshot shows you what tokens look like in the editor of an event message and then in the email that an attendee receives.

Notice that all of the tokens are inside brackets in the message editor. You can see that tokens were used for the attendee's name, event name, event date, and personal registration URL for the attendee.

The personal registration URL is where people can manage their registration, e.g., change the date or cancel.  
​

[![](https://downloads.intercomcdn.com/i/o/839522081/4b1ca705552d5e5d3619d488/image.png?expires=1784333700&signature=61e7e55e7d33fee6f5db8b038a0a6b76d4d5fb7c44827b12455c98358731fbf4&req=fCMuE8t8nYleFb4f3HP0gJJJ6qmmeeJYUM4jCCZi4Ln422ukt7QGuVjQf8OO%0A0TKR36o0A8eVMkbbHA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/839522081/4b1ca705552d5e5d3619d488/image.png?expires=1784333700&signature=61e7e55e7d33fee6f5db8b038a0a6b76d4d5fb7c44827b12455c98358731fbf4&req=fCMuE8t8nYleFb4f3HP0gJJJ6qmmeeJYUM4jCCZi4Ln422ukt7QGuVjQf8OO%0A0TKR36o0A8eVMkbbHA%3D%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/839522082/1b0a264ee7e1b63f1b5ce4f3/image+%281%29.png?expires=1784333700&signature=6d49d67e521f295f5cd81110ff578de4ece0461c0d76c116985c8d601935b339&req=fCMuE8t8nYldFb4f3HP0gFuCZV0Ah9m8k2Ru718lO%2BP%2B8IWZ963pvPnWewOr%0A7jpxhNTPSgpH7EHipw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/839522082/1b0a264ee7e1b63f1b5ce4f3/image+%281%29.png?expires=1784333700&signature=6d49d67e521f295f5cd81110ff578de4ece0461c0d76c116985c8d601935b339&req=fCMuE8t8nYldFb4f3HP0gFuCZV0Ah9m8k2Ru718lO%2BP%2B8IWZ963pvPnWewOr%0A7jpxhNTPSgpH7EHipw%3D%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/46838859/a293f3ecd8652a5a0bbaca03/image.png?expires=1784333700&signature=b29807d3b94a8bfe4d044dabc77281562fff1312c4499f6235bb9cce40604523&req=cCYvFcF2mIgTWLcX3D%2B5htHf7cV4Ohei6U3o6Lq3iDwAy7K%2Fj%2BoyOocJqH91%0AHdd8SlefxJRkD6LP%0A)](https://downloads.intercomcdn.com/i/o/46838859/a293f3ecd8652a5a0bbaca03/image.png?expires=1784333700&signature=b29807d3b94a8bfe4d044dabc77281562fff1312c4499f6235bb9cce40604523&req=cCYvFcF2mIgTWLcX3D%2B5htHf7cV4Ohei6U3o6Lq3iDwAy7K%2Fj%2BoyOocJqH91%0AHdd8SlefxJRkD6LP%0A)

---

# Token List

The following is a list of available tokens in Events. Remember, if you manually add these tokens, enclose them in brackets [ ].

## User

|  |  |
| --- | --- |
| user:user-first-name | First name of user |
| user:user-last-name | The last name of the user |
| user:email\_address | The email address of the user |

## Registration

|  |  |
| --- | --- |
| event:registration\_guid | User's unique registration ID |
| event:registration\_update\_url | User's unique registration URL. Can be used to update the registration information. |
| event:registration\_date | Date of the event that the attendee registered for, including time. |
| event:registration\_create\_date | The date that the user's registration record for this event was first created |
| event:attendee\_registered\_for\_date | The specific date the attendee registered to attend. |

## Payment

|  |  |
| --- | --- |
| event:payment\_id | Unique payment ID |
| event:payment\_created\_date | The date the payment was collected |
| event:payment\_amount | The amount of the payment |

## Add to Calendar

📌 **Note**: System-generated emails (*Event Confirmation* and *Event* *Reminder*) automatically have ICS file attachments for the registrant to easily add the event to their calendar.

|  |  |
| --- | --- |
| event:add\_to\_google\_url | Link to add the event to a Google Calendar |
| event:add\_to\_outlook\_url | Link to add the event to an Outlook Calendar |
| event:add\_to\_office365\_url | Link to add the event to an Office365 Calendar |

## Event

Use these tokens for ***general*** event information. For specific user registration details, see [Registration Tokens](#h_c1c6830871).

|  |  |
| --- | --- |
| event:event\_site\_url | The URL of the events site homepage |
| event:event\_url | The URL of the specific event landing page |
| event:event\_name | The name of the event |
| event:event\_image | The URL of the event image |
| event:event\_type | The type of the event |
| event:event\_categories | All of the event categories  (separated by commas) |
| event:event\_start\_date | The first date this event occurs |
| event:event\_end\_date | The last date this event occurs |
| event:event\_start\_time | The start time of the event |
| event:event\_end\_time | The end time of the event |

## Venue

|  |  |
| --- | --- |
| event:event\_venue\_name | The name of the event location |
| event:event\_venue\_address | The street address of the location (does not include building name or room number) |
| event:event\_venue\_building | The building name of the event location |
| event:event\_venue\_room | The room number of the event location |
| event:event\_venue\_city | The city of the event location |
| event:event\_venue\_state | The state of event location |
| event:event\_venue\_country | The country of event location |

---

# Using the Right Date Tokens in Event Messages

Event messages can reference either the **event’s overall date range** or the **specific date an attendee registered for**. For recurring events, choosing the right token ensures your message reflects the attendee’s actual appointment instead of the first or last date of the event.

For the examples below:

* The event is set up as a **recurring campus tour**
* It runs from **November 6, 2025 through July 4, 2026**
* It repeats three times a week from **12:00–2:00 PM**
* The attendee registered for the **November 19, 2025 at 12:00 PM** occurrence

With that in mind, here’s how each token behaves and when to use it:

## Tokens That Show the Attendee’s Booked Date

* **[event:attendee\_registered\_for\_date]**
* **[event:registration\_date]**

  + **Output:** Wed, November 19, 2025 at 12:00 PM EST

These tokens return the **exact occurrence the attendee selected**. Therefore, they are ideal to use when:

* You’re sending confirmations, reminders, or any message tied to a person’s actual appointment.
* Your event is **recurring** and you want to reference the attendee’s specific date and time.

## Tokens That Describe the Event’s Overall Date + Time

These tokens describe the **full date range** **and time** of the event. They do *not* reflect a specific attendee’s booking in recurring events.

The values returned by these tokens come directly from the **event settings**—the start date, end date, and daily time window you entered when creating or editing the event. 🚨 **Important:** If you plan to use these tokens in messaging, it’s a good idea to double-check those settings to confirm they reflect what you want to populate.

* **[event:event\_start\_date]**

  + **Output:** Thursday, November 6
* **[event:event\_end\_date]**

  + **Output:** Friday, July 4
* **[event:event\_start\_time]**

  + **Output:** 12:00 PM
* **[event:event\_end\_time]**

  + **Output:** 2:00 PM

These tokens are ideal to use when:

* You have a single date event
* You want to explain the event’s overall operating window
* You’re describing how the event works (e.g., “Tours run 12–2 PM”)
* You’re writing promotional or informational content about the event setup

---

# Using URL Tokens

💡**Tip**: When using a URL token, hyperlink the text and use the Token as the URL. This way, it hides the long URL from your recipient.

In the example above, you could have used:

"If you need to change any of your registration information or cancel your registration, please your personal registration URL" and link the text to the [event:registration\_update\_url] token.

---