---
title: Webhooks
url: https://help.element451.com/en/articles/7960898-webhooks
collection: Integrations
---

# Overview

Webhooks are automated messages sent from applications when something happens. They have a message—or payload—and are sent to a unique URL—essentially the app's phone number or address.

Webhooks allow Element451 to communicate with other systems, enabling efficient data exchange and, most importantly, event-driven interactions when combined with rules. Element451's webhooks can be used with middleware like *Zapier* *and Make* or work directly with other systems.

![](https://downloads.intercomcdn.com/i/o/1084885800/b126107b07c6ca3488868966/Note-Orng.png?expires=1784430000&signature=ba86f181932207f0013f5b73f5e6e05a684a7e09a48907ea7729eb1de0c5dbae&req=dSAvEsF2mIlfWfMW3Hu4gbBKEIs614%2BhAojSeFrQOhnMdc9R5HAzUYwltVfw%0A6g%3D%3D%0A) Element451 supports sending data for a single record and not receiving data.

## Accessing Webhooks

Navigate to **Data & Automation** > **Webhooks**.

[![](https://downloads.intercomcdn.com/i/o/1084887832/8e95d58feb809dce5e5e111e/Screenshot+2024-06-17+at+4_47_06%E2%80%AFPM.png?expires=1784333700&signature=eab00b45cf18f8f7577b8f3f145d6118086cb7256dc652613a343cba6f91fc37&req=dSAvEsF2molcW%2FMW1HO4zdQbYEusKNpJOlvocMg9ATE%2BApZ4bUW6mE0gVWIV%0AIpAt89rvEf6rY2wPRlw%3D%0A)](https://downloads.intercomcdn.com/i/o/1084887832/8e95d58feb809dce5e5e111e/Screenshot+2024-06-17+at+4_47_06%E2%80%AFPM.png?expires=1784333700&signature=eab00b45cf18f8f7577b8f3f145d6118086cb7256dc652613a343cba6f91fc37&req=dSAvEsF2molcW%2FMW1HO4zdQbYEusKNpJOlvocMg9ATE%2BApZ4bUW6mE0gVWIV%0AIpAt89rvEf6rY2wPRlw%3D%0A)

---

# Creating + Managing a Webhook

The Webhooks page (Data & Automation > Webhooks) displays current webhooks, the URL used to send data, and the HTTP method used.

## Creating a Webhook

1. To create a webhook, click the blue **+ Create Webhook** button at the top left.
2. Configure the webhook:

   * **Name the Webhook**: Enter a name at the top of the sidesheet.
   * **URL:** This is the URL to which to send data.
   * **Method:** This HTTP method is used to send data and will most likely be POST or PUT.
   * **Body Type:** You can select "TEMPLATE" to use and Element451 Template or "RAW JSON" to create your own layout. XML is not currently supported.
   * **Template or Body:**

     + If you selected Template, you must select an Element451 Template from your instance.
     + If you select Raw JSON, you must create your own JSON template. Clicking "Add Token" will allow you to insert tokens to merge data into the JSON template like you would add tokens when creating an email or microsite.
   * **Requests Limit Per Minute:** Some services limit the number of requests they can handle per minute, which can be entered here.
   * **Headers:** Any needed headers can be entered here. This may be an APIKey, version type, or other required header. If you selected "RAW JSON," it's best to add a header with a "Content-Type" key and "application/json" value.
3. Once the required fields are configured, click **Save**. Your webhook is now complete.

## Editing a Webhook

1. From the Webhooks page (Data & Automation > Webhooks), locate the webhook you wish to edit.
2. Click the **three-dot menu button** at the row's end, then click **edit**.

## Deleting a Webhook

1. From the Webhooks page (Data & Automation > Webhooks), locate the webhook you wish to delete.
2. Click the **three-dot menu button** at the row's end, then click **delete**. You'll be asked to confirm your action.

---

# Viewing and Testing a Webhook

After the webhook is created, you can open actions and view executions.

Executions allow you to see when the webhook was last run and the returned status. If you click the **three-dot menu button** and select **Open**, you can see any previous runs and the returned body. The left-hand side of the screen will also allow you to make adjustments to the webhook.

From this view, you can also test a webhook by clicking the blue **Test** button in the top left corner. You'll select a contact to use for the test and then click **Run**. Once the run is complete, you'll see the status code, header, and body that was returned. You can run this as often as needed to ensure the webhook is working as expected.   
​  
You can delete a webhook from either the main webhook page or from inside the webhook by clicking the **three-dot menu button** and then selecting **Delete**.

---

# Crafting a Webhook Body

Webhooks support sending an body as part the HTTP request. This body can be created in two ways.

## Using a Template for the Body

##

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203989/062e980e6d66c3fe0aa28d9bd090/Screenshot%2B2026-06-15%2Bat%2B10_36_41-E2-80-AFAM.png?expires=1784333700&signature=d7baeed55686c4ee120d5f4a1ccd70831209a17995622880b0b8715078859455&req=diQgHst%2BnohXUPMW1HO4zdnAMrsHezvj70okFX8p%2F2802FuGnmKHykctE1Lp%0Ao92kF5vMU1JGjEGrcDw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203989/062e980e6d66c3fe0aa28d9bd090/Screenshot%2B2026-06-15%2Bat%2B10_36_41-E2-80-AFAM.png?expires=1784333700&signature=d7baeed55686c4ee120d5f4a1ccd70831209a17995622880b0b8715078859455&req=diQgHst%2BnohXUPMW1HO4zdnAMrsHezvj70okFX8p%2F2802FuGnmKHykctE1Lp%0Ao92kF5vMU1JGjEGrcDw%3D%0A)

Selecting "Template" for the Webhook Body Type will prompt you to select a template. This list corresponds to the [Export Templates](https://help.element451.com/en/articles/9006851-creating-export-mapping-templates) configured under Data + Automations -> Import + Export -> Mapping Templates -> Export Templates.

When Template is selected, the Webhook body will output JSON with key names that correspond to the "Header and Sample row" Column of the template.

A template with Email, First Name and Last Name mapped like this..

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203991/3304d94449ca40a1d5b58438bb60/Screenshot%2B2026-06-15%2Bat%2B10_40_24-E2-80-AFAM.png?expires=1784333700&signature=9079cfe0be0e51659bf12d2606da07761f8160e7b7d6c3e05009a2fc2f421178&req=diQgHst%2BnohWWPMW1HO4zd8Tw52DouhShrdoM94g%2BYf34adlpPjIiJqFWN4y%0Abl4GS7IEsfffw6DLqSw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203991/3304d94449ca40a1d5b58438bb60/Screenshot%2B2026-06-15%2Bat%2B10_40_24-E2-80-AFAM.png?expires=1784333700&signature=9079cfe0be0e51659bf12d2606da07761f8160e7b7d6c3e05009a2fc2f421178&req=diQgHst%2BnohWWPMW1HO4zd8Tw52DouhShrdoM94g%2BYf34adlpPjIiJqFWN4y%0Abl4GS7IEsfffw6DLqSw%3D%0A)

..will produce an output like this:

```
{  
  "Email": "example@email.com",  
  "First Name": "First",  
  "Last Name": "Last"   
}
```

## Changing Key Names

To change the key name, edit the template column and adjust the Column name field to the desired name:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203990/ea2434fe4f89f79c363d442ce252/Screenshot%2B2026-06-15%2Bat%2B10_46_16-E2-80-AFAM.png?expires=1784333700&signature=356bd6cfcb5fafb847b060be86ac12d611c603cb2bcf74afe64a0666be17ae4b&req=diQgHst%2BnohWWfMW1HO4zdGxFm3I3peoZcNzeuFuMuCeE9gH0od0CTA7m71J%0A21Ep%2BmnChJyH0xgDRN0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203990/ea2434fe4f89f79c363d442ce252/Screenshot%2B2026-06-15%2Bat%2B10_46_16-E2-80-AFAM.png?expires=1784333700&signature=356bd6cfcb5fafb847b060be86ac12d611c603cb2bcf74afe64a0666be17ae4b&req=diQgHst%2BnohWWfMW1HO4zdGxFm3I3peoZcNzeuFuMuCeE9gH0od0CTA7m71J%0A21Ep%2BmnChJyH0xgDRN0%3D%0A)

## Applying Transformations

All transformations applied to a column will be reflected in the Webhook output.

In this example, the Intended Term would be output as the term code, as opposed to the name or other value type:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203987/192bee19d0056d045cc19456271e/Screenshot%2B2026-06-15%2Bat%2B10_47_24-E2-80-AFAM.png?expires=1784333700&signature=3b46795a6accdd79972f2e3fc9528cc3132779259546dc42a500ac16f9ffe500&req=diQgHst%2BnohXXvMW1HO4zWNgyR5AHeZqkSPEi8MZAuXDVLW9OScwQwhylW%2Bz%0AdJvUqFxfhSDMENX020E%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478203987/192bee19d0056d045cc19456271e/Screenshot%2B2026-06-15%2Bat%2B10_47_24-E2-80-AFAM.png?expires=1784333700&signature=3b46795a6accdd79972f2e3fc9528cc3132779259546dc42a500ac16f9ffe500&req=diQgHst%2BnohXXvMW1HO4zWNgyR5AHeZqkSPEi8MZAuXDVLW9OScwQwhylW%2Bz%0AdJvUqFxfhSDMENX020E%3D%0A)

Learn more about column transformations [here](https://help.element451.com/en/articles/9007047-column-setting-options-for-exports).

## Using Raw JSON for the Body

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478210927/adda0327dc77d1389973390361ae/Screenshot%2B2026-06-15%2Bat%2B10_52_41-E2-80-AFAM.png?expires=1784333700&signature=73e3ea70683e5ed6fb50fc686e912dae107d86007e3055f23781c3f0e730f766&req=diQgHst%2FnYhdXvMW1HO4zRkW1KOCHGc1EBcHIiJP5a6pIltMwrAIXBRo%2BsI6%0AIMi1JBEgHRSJUJsDvjw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2478210927/adda0327dc77d1389973390361ae/Screenshot%2B2026-06-15%2Bat%2B10_52_41-E2-80-AFAM.png?expires=1784333700&signature=73e3ea70683e5ed6fb50fc686e912dae107d86007e3055f23781c3f0e730f766&req=diQgHst%2FnYhdXvMW1HO4zRkW1KOCHGc1EBcHIiJP5a6pIltMwrAIXBRo%2BsI6%0AIMi1JBEgHRSJUJsDvjw%3D%0A)

Selecting "Raw JSON" for the Webhook Body Type allows you to create the webhook body directly. Student data can be passed into the webhook body using [Tokens](https://help.element451.com/en/articles/1524113-campaign-tokens). All tokens should be treated as strings and wrapped in double quotes to ensure the JSON on valid.

Tokens will be evaluated during each execution of the webhook. A body with these tokens..

```
{  
  "email": "[user:email_address]",  
  "first_name": "[user:first_name]",  
  "last_name": "[user:last_name]"  
}
```

.. will evaluate to this during execution:

```
{  
 "email": "example@email.com",  
 "first_name": "First",  
 "last_name": "Last"  
}
```

---

# Using a Webhook

Once a webhook has been created, you can use it in a **Workflow** or **Rule**.

* Select the **Execute Webhook***action*when adding actions to the workflow or rule.
* We generally recommend using a **rule**, as it allows a record to pass through multiple times, unlike a regular workflow that only permits a single pass. Once the rule is active, the webhook will run whenever triggered by the rule.
* The "People" tab will show which contact records the rule was executed for if the webhook execution was successful. However, it is essential to remember that "succeeded" means it was successful in sending the webhook, not that a 200 status was received or that the data was correctly received when it was sent.

---

# Retries

Element451 does support retries when a status of 408, 409, 502, 503, or 504 is received. After the first try, the request is delayed for 3 minutes before retrying, 30 minutes, and 180 minutes.   
​  
After the 3rd try, the webhook will fail and not attempt to send that data again.

---