---
title: Private Conversations
url: https://help.element451.com/en/articles/9682245-private-conversations
collection: Conversations
---

Explore Private Conversations, a feature that ensures only authorized users can view specific convos that may contain sensitive information.

# Overview

Private Conversations in Element451 ensure that sensitive information is accessible only to the author, participants, and assignees (including Teams). This feature provides a secure way to handle confidential discussions.

## What Permissions Are Needed?

To manage and access Private Conversations, specific permissions must be included in one of your permission groups. Here’s a breakdown:

* **Access Conversations451**

  + This permission allows you to enable private mode on conversations you create, are a participant in, or have been assigned to. This means you must be involved in the conversation to access the “private” toggle.
* **Administer Conversations**

  + With this permission, you can enable private mode on any public conversation, regardless of whether you are the author, a participant, or have been assigned to it.
* **View All Conversations**

  + This permission allows you to view all conversations, regardless of privacy settings. However, it doesn’t override visibility group settings, meaning you won’t be able to see conversations for contacts you don’t have access to view.
  + This permission can be combined with *Access Conversations451* and/or *Administer Conversations* in a custom permission group. Without it, you cannot see any private conversations in which you are not involved.

## Setting Up Permissions

* **[Using System Groups](https://help.element451.com/en/articles/2735389-permission-groups-overview#h_deeebe4fbe)**: You can assign a user to the *Conversations User* or *Conversations Administrator* system groups, which already contain the relevant permissions.

  + ***Conversations User****:*

    - *Access Conversations451*
  + ***Conversations Administrator****:*

    - *Access Conversations451*
    - *Administer Conversations*
* **[Creating Custom Groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups)**: If the system groups don’t fit your needs, you can create a custom permission group. Choose the necessary [individual permissions](https://help.element451.com/en/articles/6590379-list-details-of-individual-permissions) and assign the custom group to the user.

---

# Enabling Private Conversations

## New Conversations

When starting a new conversation, you can easily mark it as private to ensure that only authorized individuals can view the content. Follow the process for creating a new conversation outlined in the [channel's respective help article](https://help.element451.com/en/collections/6074341-conversations-channels).

[![](https://downloads.intercomcdn.com/i/o/1130844319/f00b536ef2b05755ca0de144/Private+Convos.png?expires=1784333700&signature=7b58f84394ae63b54b1fb5b1bfdb47ac55b4de8ddaebf161d0c9b312114b0949&req=dSEkFsF6mYJeUPMW1HO4zXFjLuypOpHQfqtHuqYfrhGchz0iUc6MDutmBK1P%0AyZO%2BpEswr2YCejlQIqM%3D%0A)](https://downloads.intercomcdn.com/i/o/1130844319/f00b536ef2b05755ca0de144/Private+Convos.png?expires=1784333700&signature=7b58f84394ae63b54b1fb5b1bfdb47ac55b4de8ddaebf161d0c9b312114b0949&req=dSEkFsF6mYJeUPMW1HO4zXFjLuypOpHQfqtHuqYfrhGchz0iUc6MDutmBK1P%0AyZO%2BpEswr2YCejlQIqM%3D%0A)

## Existing Conversations

You can also enable private mode for existing conversations from within the **manage tab** of the conversation. You can find additional information on [accessing that tab here](https://help.element451.com/en/articles/1894279-getting-started-with-conversations#h_8b2248c1aa).

[![](https://downloads.intercomcdn.com/i/o/1132143518/70e67cc24d3ade1e0c47e016/private+convos+-+existing.png?expires=1784333700&signature=62753e1761c98af3214f5e021589fbd91d7a3eac34a3d357ac44e199dbf6d89f&req=dSEkFMh6noReUfMW1HO4zbXpNnDOdH07eeG4pLS1%2B08jWTHCJPo4sj1IMjc0%0A28h0qqmhMjz1auV2LAw%3D%0A)](https://downloads.intercomcdn.com/i/o/1132143518/70e67cc24d3ade1e0c47e016/private+convos+-+existing.png?expires=1784333700&signature=62753e1761c98af3214f5e021589fbd91d7a3eac34a3d357ac44e199dbf6d89f&req=dSEkFMh6noReUfMW1HO4zbXpNnDOdH07eeG4pLS1%2B08jWTHCJPo4sj1IMjc0%0A28h0qqmhMjz1auV2LAw%3D%0A)

---

# Identifying Private Conversations from Inbox

In your Conversations Inbox, private conversations are denoted with a ![](https://downloads.intercomcdn.com/i/o/1130843753/5e34ff27df062dd4b757c273/Screenshot+2024-07-31+at+9_00_29%E2%80%AFAM.png?expires=1784430000&signature=6d523eb92e8b721f763eeaca1ab3673a66a9e3e603aefd6335a806232b3859c6&req=dSEkFsF6noZaWvMW3Hu4gSM3uMrje%2FdjqyhJeeckSCVzbxsbXKnoYuFrz1XU%0A2w%3D%3D%0A)lock icon.

![](https://downloads.intercomcdn.com/i/o/1132102082/3be745e1619b308c29a683c4/Pro+Tip.png?expires=1784430000&signature=9972171c83f49f9a0befd19d3aa01f5147a2c88401c281f77ae93fcda1e9fe36&req=dSEkFMh%2Bn4FXW%2FMW3Hu4gYswAcvNIdAr1ZDZhcdqTndIT5kFJUXtSKHt%2B0xr%0AZQ%3D%3D%0A) You can use the advanced filter tool within your inbox to narrow the conversation list by privacy (public or private).

[![](https://downloads.intercomcdn.com/i/o/1130843345/828464825c84aa5919c1353c/Private+Convos+Indicator.png?expires=1784333700&signature=1251c612799a6f274c0f51a45e3219aea78a669aa22e2d6bc27fc0e0289679a5&req=dSEkFsF6noJbXPMW1HO4zaYFCPcrUigZFQ3mFApPOAqmbvW3N%2FniJcP16%2Bis%0ABPf2Bd6fR9FM8wBbPHk%3D%0A)](https://downloads.intercomcdn.com/i/o/1130843345/828464825c84aa5919c1353c/Private+Convos+Indicator.png?expires=1784333700&signature=1251c612799a6f274c0f51a45e3219aea78a669aa22e2d6bc27fc0e0289679a5&req=dSEkFsF6noJbXPMW1HO4zaYFCPcrUigZFQ3mFApPOAqmbvW3N%2FniJcP16%2Bis%0ABPf2Bd6fR9FM8wBbPHk%3D%0A)

You can explore more about inbox indicators and markings in our [Conversations Inbox](https://help.element451.com/en/articles/8507376-conversations-inbox) help article.

---

# Important Considerations for SMS Private Conversations

SMS messages are threaded based on number pairs. If you share an Element451 number with other departments, be aware that:

* Marking an existing conversation as private will hide the entire history and all future messages, regardless of which internal user takes the action.
* If an existing public conversation exists, and another user creates a new conversation with the same number pair but marks it as private, the original public setting will not change. We do not enforce the new private setting on the original conversation.

If you're interested in adding an additional Element451 phone number, please contact our Customer Success team via live chat or at [support@element451.com](mailto:support@element451.com)

[Explore More: SMS Threading](https://help.element451.com/en/articles/8506260-sms-text-message#h_e0b48929d9)

---