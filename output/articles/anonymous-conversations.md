---
title: Anonymous Conversations
url: https://help.element451.com/en/articles/9688991-anonymous-conversations
collection: Conversations
---

Learn how Element451 handles anonymous conversations by default and how to set your preferences for Email, SMS, and Messenger.

# Overview

Element451 lets you decide how anonymous messages are handled across **Email, SMS, and Messenger (Live Chat)**. The behavior varies slightly by channel and depends on whether Anonymous Conversations is enabled or disabled.

---

# Channel Behavior

## Email

* **Default**: Only messages from known contacts appear in your inbox.
* **Anonymous Conversations Enabled**: Any email sent to the connected address will appear in your inbox, even if the sender is not in your contact list.

## SMS

* **Default**: Only messages from known contacts appear in your inbox.
* **Anonymous Conversations Enabled**: SMS messages from unknown numbers will also appear in your inbox.

## Messenger (Live Chat)

Messenger works differently from Email and SMS. **By** **default**, **anonymous** **conversations** **are allowed**. If you disable this option, visitors must authenticate with an email address (and complete a short form if no record exists) before starting a conversation. Completing this form creates an inquiry before the conversation even begins.

* **Default**: Anonymous Conversations are enabled. Anyone can start chatting without needing to identify themselves.
* **Anonymous Conversations Disabled**:

  1. Visitors are prompted to enter their email address.
  2. Element451 sends a verification code to the email address.
  3. After entering the code:

     + **When the email matches an existing contact record**:

       - If no Prospect or Application milestone exists for the contact, they are presented with a ***short lead capture form.*** Upon completion, they will receive a Prospect milestone.
       - The contact is associated with that record, and their past chat history is displayed
     + **When the email does not match a record**:

       1. The visitor completes a form (first name, last name, phone number, intended major, and intended term), and

          - First and last name are required.
          - Phone, intended major, and intended term are optional.

            [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1707565185/551f1268ce4371b0d574bf8e7d14/CleanShot%2B2025-09-03%2Bat%2B12_43_58.png?expires=1784333700&signature=b8a87d8c439f1dedb6ea6cb0f7fafc75e06a55fe526c63d345031f28fe7b92cb&req=dScnEcx4mIBXXPMW1HO4zXGQbZ%2FfeQJay3noFtBRQ3oZ654dWH5gc4THKh3H%0AF%2FfQ%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1707565185/551f1268ce4371b0d574bf8e7d14/CleanShot%2B2025-09-03%2Bat%2B12_43_58.png?expires=1784333700&signature=b8a87d8c439f1dedb6ea6cb0f7fafc75e06a55fe526c63d345031f28fe7b92cb&req=dScnEcx4mIBXXPMW1HO4zXGQbZ%2FfeQJay3noFtBRQ3oZ654dWH5gc4THKh3H%0AF%2FfQ%0A)
       2. A new contact record is created and assigned a **Prospect Milestone with a date of inquiry**.
  4. After authentication or form submission, the visitor can begin a new conversation.

---

# Enabling/Disabling Anonymous Conversations

![](https://downloads.intercomcdn.com/i/o/1132114816/3c13bc2c5a8b484ba4e9b8b1/Important.png?expires=1784430000&signature=c3027301c62e52310bf61e027512dc45346e1ac2ac7e6ae7becd00c9f1da0f02&req=dSEkFMh%2FmYleX%2FMW3Hu4gexIIDjp5Vk56DR7uXJRRqEORphQiN0sAi9vvTm5%0Aqw%3D%3D%0A) This means no filtering will be applied to either channel. **All** emails and text messages, whether related to a contact or not, will create a new conversation. Before enabling anonymous conversations, it is a good idea to review what emails are sent to the email address you have connected to Element451.

1. Navigate to **Engagement > Conversations > Conversations Settings**.
2. Select the channel you want to configure (Email, SMS, or Messenger).
3. Use the **Enable Anonymous Conversations** toggle to enable or disable the feature.

[![](https://downloads.intercomcdn.com/i/o/1132122781/94548ca5550ca2945131486e/event+auto+responder+screenshot+%281%29.png?expires=1784333700&signature=eeac8465660f4477459ae18869d0f8152129255a8f57f543ec08fbffbbf8fa23&req=dSEkFMh8n4ZXWPMW1HO4zcmrpk2JK0nEBXw0tsQCljK5Xj4syZdATZ2lkBR0%0A69uKBbwgXYoZuz5zsl8%3D%0A)](https://downloads.intercomcdn.com/i/o/1132122781/94548ca5550ca2945131486e/event+auto+responder+screenshot+%281%29.png?expires=1784333700&signature=eeac8465660f4477459ae18869d0f8152129255a8f57f543ec08fbffbbf8fa23&req=dSEkFMh8n4ZXWPMW1HO4zcmrpk2JK0nEBXw0tsQCljK5Xj4syZdATZ2lkBR0%0A69uKBbwgXYoZuz5zsl8%3D%0A)

---

# Identifying Anonymous Conversations

If the identity of the conversation's external participant cannot be determined by Element451, the name will be listed as "Unknown Visitor."

![](https://downloads.intercomcdn.com/i/o/1132120939/4d10551b7f16af3973f447bd/Pro+Tip.png?expires=1784430000&signature=f7eed661d5eeb09686988e480f1ea68dba9150cb21aa669bfd5102effe283d8e&req=dSEkFMh8nYhcUPMW3Hu4gaf%2BqqL5Mz%2BX0Og6ZpvuYpttT8WAqTX7sI%2FCwfTH%0A8g%3D%3D%0A) You can use the advanced filter tool within your inbox to narrow the conversation list by their known status (anonymous or not anonymous).

[![](https://downloads.intercomcdn.com/i/o/1070508602/bdb0694c45652bc5b07db0f3/Unread+Convo.png?expires=1784333700&signature=6738c41c342b030c03a20bb7cfd5b9c3e53a55d6440b33c47c16b2c93a820ef2&req=dSAgFsx%2BlYdfW%2FMW1HO4zZvBvcZqbOZsEjSog1LuU9mQRafHT0tAixgN4Ci3%0AVHjqbHOYIuTAlAnQ3xI%3D%0A)](https://downloads.intercomcdn.com/i/o/1070508602/bdb0694c45652bc5b07db0f3/Unread+Convo.png?expires=1784333700&signature=6738c41c342b030c03a20bb7cfd5b9c3e53a55d6440b33c47c16b2c93a820ef2&req=dSAgFsx%2BlYdfW%2FMW1HO4zZvBvcZqbOZsEjSog1LuU9mQRafHT0tAixgN4Ci3%0AVHjqbHOYIuTAlAnQ3xI%3D%0A)

You can explore more about inbox indicators and markings in our [Conversations Inbox](https://help.element451.com/en/articles/8507376-conversations-inbox) help article.

---