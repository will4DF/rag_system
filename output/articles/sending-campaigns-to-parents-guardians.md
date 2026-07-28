---
title: Sending Campaigns to Parents/Guardians
url: https://help.element451.com/en/articles/8901542-sending-campaigns-to-parents-guardians
collection: People
---

Discover how to effectively send Campaigns to parents or guardians.

# Overview

Communicating effectively with parents or guardians is pivotal in nurturing a successful enrollment funnel. This article covers the process of sending Campaigns to parents or guardians and important things you should know, especially if you don't have separate parent records/profiles. We recommend reviewing the [Family Members and Relationships](https://help.element451.com/en/articles/8903525-family-members-relationships) article as a prerequisite to this article.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205094663/8c874ba713d2e85b585562b090d6/Note.png?expires=1784333700&signature=786a2dde6b23c1052904ae873c665d614bf36044e34b3aa2d350a53e92b4e1de&req=dSInE8l3mYdZWvMW1HO4zX%2Bhk342TfXZJt7iD2s7wVcTQfgkmKlcdICNqLzA%0ApXsOJZ%2FF8iZDAdS1MDo%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205094663/8c874ba713d2e85b585562b090d6/Note.png?expires=1784333700&signature=786a2dde6b23c1052904ae873c665d614bf36044e34b3aa2d350a53e92b4e1de&req=dSInE8l3mYdZWvMW1HO4zX%2Bhk342TfXZJt7iD2s7wVcTQfgkmKlcdICNqLzA%0ApXsOJZ%2FF8iZDAdS1MDo%3D%0A)

The push notification channel in Campaigns is intended for student communication only, as parents/guardians do not have access to StudentHub.

---

# Email Campaigns

## Tokens for Parent/Guardian Emails

There are two different tokens you can use to send email Campaigns to parents/guardians:

1. **Guardian Emails `[user:guardian_emails]`**

   * This token targets [family members](https://help.element451.com/en/articles/8903525-family-members-relationships#h_6b6eb6497c) with the internal type “guardian” (when family/guardian data was collected using the "Parent / Legal Guardian” field grouping (`user-family-root`) or imported using `user-family-guardian` mappings).
2. **Relationship Emails `[user_related:emails]`**

   * This token targets [separate family records](https://help.element451.com/en/articles/8903525-family-members-relationships#h_160b533338) with a relationship to the student record with a specified relationship type (when you store parent/guardian data as separate contact records).
   * When using this token, you will have the option to configure the token properties, which will allow you to **target** specific relations (parent-child, guardian-dependent, grandparent-grandchild, etc.).

## Using Tokens in Campaigns

### Option 1: Email from a Token (Guardian Emails)

[![](https://downloads.intercomcdn.com/i/o/952558947/31373d92ec62792733123330/Send+to+Guardian+Token.png?expires=1784333700&signature=ada5afe2e9e7f0deac32267bf90344c7b07a9aab5adae6cd3e8a7b5f986264a2&req=fSUlE8x2lIVYFb4f3HP0gMcFCdBKvDIr0Dnye5tiN7tsA7Gol48hIIJU6NDO%0ArF6tMC1cze3HeBUtOA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/952558947/31373d92ec62792733123330/Send+to+Guardian+Token.png?expires=1784333700&signature=ada5afe2e9e7f0deac32267bf90344c7b07a9aab5adae6cd3e8a7b5f986264a2&req=fSUlE8x2lIVYFb4f3HP0gMcFCdBKvDIr0Dnye5tiN7tsA7Gol48hIIJU6NDO%0ArF6tMC1cze3HeBUtOA%3D%3D%0A)

If you collect family/guardian data using the field grouping or import and do not store the data on separate contact records via a relationship, you can use the Guardian Emails token in the "Send To" field.

[![](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)

It is important to note the Send To field supportsonly a **single** email address. As a result, if the contact has multiple family members with email addresses on their record, only one family member will receive the Campaign. This approach is straightforward but might not be able to meet your comprehensive outreach needs.

[![](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)

Tokens used to personalize the email, like [user:first\_name], will be replaced with data from the student's record.   
​  
When using this method, email activity (received, opened, clicked) is tracked on the **student profile**, but you can see the email address to which the message was sent by viewing the activity details.

### Option 2: CC'ing Guardian and Relationship Emails

[![](https://downloads.intercomcdn.com/i/o/952559122/399558779273b89eb0bb83c6/CC+Guardian+Token.png?expires=1784333700&signature=c5a121bb8a753f125f77bc29d15d91e05ab60e329c28b79729c92797e424d738&req=fSUlE8x3nINdFb4f3HP0gCW8zfIPv2D9jvUnRnD4f03%2BIE8O1n1T9RxympoM%0APBIpnnhfVzY0DuvUVw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/952559122/399558779273b89eb0bb83c6/CC+Guardian+Token.png?expires=1784333700&signature=c5a121bb8a753f125f77bc29d15d91e05ab60e329c28b79729c92797e424d738&req=fSUlE8x3nINdFb4f3HP0gCW8zfIPv2D9jvUnRnD4f03%2BIE8O1n1T9RxympoM%0APBIpnnhfVzY0DuvUVw%3D%3D%0A)

A more inclusive alternative is to utilize the student's email in the "Send To" field and place one of the two email tokens in the CC (or BCC) field. Unlike the "Send To" field, **t**he CC and BCC fields can accommodate **multiple** email addresses, ensuring all listed family members receive the Campaign.

[![](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)

While this method ensures a broader reach, the student is the primary recipient, and therefore, any tokens used to personalize the email, like [user:first\_name], will be replaced with data from the student's record.

[![](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)](https://downloads.intercomcdn.com/i/o/1124769276/461dbf4da0d1418aa936cb13/Note.png?expires=1784333700&signature=594f44bc60201af379446735b52ef22a7b44d47fe361ee85c7ab8dd51bc4bcd6&req=dSElEs54lINYX%2FMW1HO4zcbJPmbxRX%2BTPMD7ekt0uC6l2Trkr8K%2Fli6qM5Pf%0Al6y0CbkaWFkEw5gp%2FR0%3D%0A)

Email activity for this method is also tracked on the **student profile**. The communication activity card and its details display only the primary (Send To) recipient's email address; CC'd and BCC'd addresses are not shown in the activity details.

To determine which token to use depends on how you store the family/guardian data:

* If separate records exist for parents/guardians, you can use either token. It depends on your needs and if you wish to target specific relationships.
* If separate records do not exist, you can only use the Guardian Emails token.

## Option 3: Create Separate Family Records

For a more direct and inclusive approach, consider using a Rule to generate separate records for each family member with data stored on the student's record. This option works best when your message targets **only** parents or guardians—perhaps starting with "Dear [Parent's Name]" or sharing specifics exclusively relevant to them.

This method guarantees that if a student has more than one parent with independent records, they will each receive the personalized Campaign.

Once a parent/guardian has a separate record, the process mirrors sending Campaigns to student records:

* [Create a parent/guardian Segment](#h_f1c9d378c9) using the filters of your choice, but you must use the Profile Type to exclude student and other record types.

  [![](https://downloads.intercomcdn.com/i/o/952566581/d5312e0f369072b8cd565808/Screenshot+2024-02-03+at+2.24.17%E2%80%AFPM.png?expires=1784333700&signature=3f5909cd3ed2203409f677a3ea95d8d649e07cbf816f7002dbb2a404feb0c7f1&req=fSUlE894mIleFb4f3HP0gIkMS4mtlxEaCA%2BFs5IEU29bDdjLqPaKJAzdQu4U%0AyFs%3D%0A)](https://downloads.intercomcdn.com/i/o/952566581/d5312e0f369072b8cd565808/Screenshot+2024-02-03+at+2.24.17%E2%80%AFPM.png?expires=1784333700&signature=3f5909cd3ed2203409f677a3ea95d8d649e07cbf816f7002dbb2a404feb0c7f1&req=fSUlE894mIleFb4f3HP0gIkMS4mtlxEaCA%2BFs5IEU29bDdjLqPaKJAzdQu4U%0AyFs%3D%0A)
* Use that Segment as your audience in your Campaign (one-time) or Workflow (ongoing).
* Configure your Campaign '*Send* *To'* setting to the Primary Email of the family record.

---

# SMS Campaigns

To send text message Campaigns to parents or guardians, you need to create separate records for them. You can follow the same steps as outlined in [Option 3](#h_423d815afe) for sending an email Campaign. Once you have separate records created, you can then create/select a segment of family records as your SMS audience. For the steps to create a parent segment, see the next section below.

---

# Create a Segment for Parent Communication

📙 **Note**: Before creating a parent Segment, you should have a basic understanding of [Segments](https://help.element451.com/en/collections/7833762-segments), [Campaigns](https://help.element451.com/en/collections/124581-campaigns), and [Workflows](https://help.element451.com/en/collections/124560-workflows-rules).

1. Navigate to **Contacts** > **People**
2. Click **Add** **Filter**

   [![](https://downloads.intercomcdn.com/i/o/958928879/fee74be16015c25b980fdfd4/Screenshot+2024-02-09+at+4.48.49%E2%80%AFPM.png?expires=1784333700&signature=c37f68ceea9becccef91053159a56f98427492e17a30fa57437f27f756870060&req=fSUvH8t2lYZWFb4f3HP0gG68hTGmgXynp0NsLGk1prSBBT6oVjQ8NokBwMsw%0Alqc%3D%0A)](https://downloads.intercomcdn.com/i/o/958928879/fee74be16015c25b980fdfd4/Screenshot+2024-02-09+at+4.48.49%E2%80%AFPM.png?expires=1784333700&signature=c37f68ceea9becccef91053159a56f98427492e17a30fa57437f27f756870060&req=fSUvH8t2lYZWFb4f3HP0gG68hTGmgXynp0NsLGk1prSBBT6oVjQ8NokBwMsw%0Alqc%3D%0A)
3. From the *Type* dropdown, select **Relationships**  
   ​

   [![](https://downloads.intercomcdn.com/i/o/958929387/6e7b5be2274b242b3335a66b/Screenshot+2024-02-09+at+4.49.30%E2%80%AFPM.png?expires=1784333700&signature=404cee84ece59b00cc8625cdac6a411a720b0a893149e3f14cbd12c235c64b16&req=fSUvH8t3nolYFb4f3HP0gJrhSCR5eOTxm1qGJzVGB8GBzkSizVlplrtCD0po%0AvdU%3D%0A)](https://downloads.intercomcdn.com/i/o/958929387/6e7b5be2274b242b3335a66b/Screenshot+2024-02-09+at+4.49.30%E2%80%AFPM.png?expires=1784333700&signature=404cee84ece59b00cc8625cdac6a411a720b0a893149e3f14cbd12c235c64b16&req=fSUvH8t3nolYFb4f3HP0gJrhSCR5eOTxm1qGJzVGB8GBzkSizVlplrtCD0po%0AvdU%3D%0A)
4. A new window will open, where you will configure your Segment.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/958929912/bbf5926f16f995d37838e94a/Screenshot+2024-02-09+at+4.50.55%E2%80%AFPM.png?expires=1784333700&signature=1b771888f7d97077fcce26e3b37f6d4a6ed2bbc5a5960a0713f13e441f39a929&req=fSUvH8t3lIBdFb4f3HP0gDcIdHk0rtYQGYH%2B8Xwm6ZRJYOEcqmaXdnB7H8%2Fs%0Axjo%3D%0A)](https://downloads.intercomcdn.com/i/o/958929912/bbf5926f16f995d37838e94a/Screenshot+2024-02-09+at+4.50.55%E2%80%AFPM.png?expires=1784333700&signature=1b771888f7d97077fcce26e3b37f6d4a6ed2bbc5a5960a0713f13e441f39a929&req=fSUvH8t3lIBdFb4f3HP0gDcIdHk0rtYQGYH%2B8Xwm6ZRJYOEcqmaXdnB7H8%2Fs%0Axjo%3D%0A)
5. Click the **Relationship** **is** dropdown to select your relationship type. For this case, we will want to choose the Parent-Child.
6. Additional configurations will appear. Since we are segmenting parent records, we will keep the default selection of **Parent**.   
   ​
7. Click **Add** **Filters** and choose the related student filter(s). Even though you're targeting parent records, **select filters related to student data**. For example, to target parents of students interested in a specific major, you could use the filter **intended major** = **accounting**.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/958937125/7c815cc70d07c0bfdc8ccf1c/Screenshot+2024-02-09+at+5.09.18%E2%80%AFPM.png?expires=1784333700&signature=cd674c8b2642da8eba0180146817daa414a30d36540913a7e0d831a33b8ac0dc&req=fSUvH8p5nINaFb4f3HP0gLb%2BYevFTwNU%2F5mqly08UNtZaoBkw6r3jODeGcPO%0Akvo%3D%0A)](https://downloads.intercomcdn.com/i/o/958937125/7c815cc70d07c0bfdc8ccf1c/Screenshot+2024-02-09+at+5.09.18%E2%80%AFPM.png?expires=1784333700&signature=cd674c8b2642da8eba0180146817daa414a30d36540913a7e0d831a33b8ac0dc&req=fSUvH8p5nINaFb4f3HP0gLb%2BYevFTwNU%2F5mqly08UNtZaoBkw6r3jODeGcPO%0Akvo%3D%0A)
8. Once you're finished adding filters, click **Submit**. You will be returned to the People list, where your new Relationship filter should be visible.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/958936922/464d6fa77e8e8969ad978ffa/Screenshot+2024-02-09+at+5.08.27%E2%80%AFPM.png?expires=1784333700&signature=d021bdc8883c726378f3c2b80fc3b9000cbe2a0bbe263ae9abd6820fb99a00ee&req=fSUvH8p4lINdFb4f3HP0gMno4HoRLjJXSm57zRaCxMHcvyxn0a7Lcm3hwNNI%0AxJ4%3D%0A)](https://downloads.intercomcdn.com/i/o/958936922/464d6fa77e8e8969ad978ffa/Screenshot+2024-02-09+at+5.08.27%E2%80%AFPM.png?expires=1784333700&signature=d021bdc8883c726378f3c2b80fc3b9000cbe2a0bbe263ae9abd6820fb99a00ee&req=fSUvH8p4lINdFb4f3HP0gMno4HoRLjJXSm57zRaCxMHcvyxn0a7Lcm3hwNNI%0AxJ4%3D%0A)
9. Click **Apply** to apply your Relationship filter.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/958937622/81084964ffd2461fb7f06f79/Screenshot+2024-02-09+at+5.10.12%E2%80%AFPM.png?expires=1784333700&signature=754c2055ca328a8f63f62c89383fec5e3252b7bc3f5124a6275efbe4d09e9ea7&req=fSUvH8p5m4NdFb4f3HP0gJbFkP4ZhBeIn4ckt509e6gKWPX5stOaEz5vbGhD%0ASh8%3D%0A)](https://downloads.intercomcdn.com/i/o/958937622/81084964ffd2461fb7f06f79/Screenshot+2024-02-09+at+5.10.12%E2%80%AFPM.png?expires=1784333700&signature=754c2055ca328a8f63f62c89383fec5e3252b7bc3f5124a6275efbe4d09e9ea7&req=fSUvH8p5m4NdFb4f3HP0gJbFkP4ZhBeIn4ckt509e6gKWPX5stOaEz5vbGhD%0ASh8%3D%0A)
10. You should now see your segmented parent records associated with students who match the specified filter (e.g., students with an intended major in accounting).   
    ​
11. You can then click **Save** **As** **New** **Segment** to retain your Segment for future use and the ability to load it into a Workflow. If you want the Segment to automatically update as data changes on records, be sure to convert it to a [calculated segment](https://help.element451.com/en/articles/7891959-calculated-segments).

---