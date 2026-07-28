---
title: Preferred Time to Send
url: https://help.element451.com/en/articles/8857428-preferred-time-to-send
collection: Workflows + Rules
---

# Overview

When using the ***Send Communication*** action in a Workflow or Rule, you have the option to set the **Preferred Time to Send**.

This feature allows you to schedule emails for delivery at optimal times based on your students' daily lives. Send messages to high school students in the afternoons or the evenings for working adults.

[![](https://downloads.intercomcdn.com/i/o/941595950/3710c866181dc0efb3a04f52/Screenshot+2024-01-23+at+10.02.33%E2%80%AFAM.png?expires=1784333700&signature=ea3249cdd34371fc4ba54e9565f36a5956c985aa7eacfc76bd4f6216540dc8b3&req=fSQmE8B7lIRfFb4f3HP0gNkjcoimEjuts3OVDBe%2B1XVUloyTekklUcw9vgs0%0AJlzuaAZu9U0NQrM5dg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/941595950/3710c866181dc0efb3a04f52/Screenshot+2024-01-23+at+10.02.33%E2%80%AFAM.png?expires=1784333700&signature=ea3249cdd34371fc4ba54e9565f36a5956c985aa7eacfc76bd4f6216540dc8b3&req=fSQmE8B7lIRfFb4f3HP0gNkjcoimEjuts3OVDBe%2B1XVUloyTekklUcw9vgs0%0AJlzuaAZu9U0NQrM5dg%3D%3D%0A)

## Important Notes

* If you use any *preferred time to send* option other than immediate, you could introduce up to a 24-hour delay in the recipient receiving the email.

  + An example is if the student's preferred open time is morning and reaches this step in your workflow at noon, they will receive this email the following morning. Please remember this when you schedule email communication where timing is critical.
* If there has not been a preferred open time determined yet for a user, the email will be sent immediately. As we learn more about the user's email opening behavior, a preferred open time will be established for future sends.
* Times are based on the student's time zone from the **Last Seen Timezone** trait. If this trait is unavailable, the institution's time zone will be used as a fallback.

---

## Time Options + When Each Sends

|  |  |
| --- | --- |
| **Time Options** | **When Communication Sends** |
| **Immediately** | When the workflow step has been reached |
| **User** **Preferred** **Open** **Time** | Student's preferred open time (calculated trait) |
| **Morning** | 9:00 AM |
| **Noon** | 12:00 PM |
| **Afternoon** | 3:00 PM |
| **Evening** | 6:00 PM |
| **Night** | 9:00 PM |
| **Late Night** | 12:00 AM |

---