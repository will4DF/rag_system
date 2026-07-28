---
title: Google Tag Manager Integration
url: https://help.element451.com/en/articles/5208134-google-tag-manager-integration
collection: Settings + Permissions
---

Use Element451's Custom Events for advanced actions in Google Tag Manager.

# Overview

Element451 offers a comprehensive Google Tag Manager (GTM) integration, delivering seamless and consistent tracking across all public-facing modules. This unified approach captures detailed user engagement data and conversion events, enabling you to measure your AI Workforce's performance and send events to platforms like Google Analytics and Meta Ads.

Google Tag Manager is a free service that allows you to manage multiple tracking pixels through a single interface. Adding your GTM container to Element451 modules enables you to track student activity and set up conversion events for various platforms.

---

# Universal Container Setup

Element451's GTM integration provides flexible configuration options with universal container support:

## Single Configuration Point

Set your GTM container ID once in **General** > **School** **Settings,** and it automatically deploys across all public-facing modules:

* Applications
* Appointments
* Bolt Discovery
* Events
* Forms
* Messenger
* Microsites
* Pages
* StudentHub
* Surveys

## Module-Specific Overrides

When needed, you can override the global container by setting a different container ID at the module level for specific use cases.

## Step 1: Find Your GTM Container ID

1. Visit [tagmanager.google.com](https://tagmanager.google.com/)
2. Locate your container in the list
3. Copy the Container ID from the third column (format: GTM-XXXXXXX)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717414293/e8773ba34cc3d6a2c6863412e1ff/Account-2BScreen.png?expires=1784333700&signature=bc348d23159bb280ef68691ce7881c8ce36cbe6e841639c471547e1278ec6828&req=dScmEc1%2FmYNWWvMW1HO4zZnvrC%2FspdJyMYM7brzz3dfD3fLgOq%2FAWOmLBpAl%0AAkmlxlqn0GZCxTUZcwM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717414293/e8773ba34cc3d6a2c6863412e1ff/Account-2BScreen.png?expires=1784333700&signature=bc348d23159bb280ef68691ce7881c8ce36cbe6e841639c471547e1278ec6828&req=dScmEc1%2FmYNWWvMW1HO4zZnvrC%2FspdJyMYM7brzz3dfD3fLgOq%2FAWOmLBpAl%0AAkmlxlqn0GZCxTUZcwM%3D%0A)

## Step 2: Set Your Global GTM Container

1. Navigate to **General > School Settings** in Element451
2. Locate the **Google Tag Manager ID** field
3. Enter your GTM Container ID
4. Save your settings

Your container will now automatically track events across all Element451 public modules.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717414292/6f9005fa8c957646cfff68572c12/CleanShot-2B2025-09-09-2Bat-2B12_53_09.png?expires=1784333700&signature=4f8cb01660e1056dfcf42a2696873fa7aef1473501a3e966d16144f0587913a7&req=dScmEc1%2FmYNWW%2FMW1HO4zbkABh4Zcjq9DYtrX%2FDUcIq2yzNEbZQkfSH3LVLT%0AbsxKrTaI9MYVhb0Ucl0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717414292/6f9005fa8c957646cfff68572c12/CleanShot-2B2025-09-09-2Bat-2B12_53_09.png?expires=1784333700&signature=4f8cb01660e1056dfcf42a2696873fa7aef1473501a3e966d16144f0587913a7&req=dScmEc1%2FmYNWW%2FMW1HO4zbkABh4Zcjq9DYtrX%2FDUcIq2yzNEbZQkfSH3LVLT%0AbsxKrTaI9MYVhb0Ucl0%3D%0A)

## Module-Specific Overrides (Optional)

If you need different containers for specific modules, you can override the global setting by updating the container at the module level. The container setting location is outlined below by module:

* **Applications**: Applications > Sites > [Select Site] > General tab > Setup
* **Appointments**: Engagement > Appointments > More Icon (⋮) > Page Settings
* **Bolt Discovery**: Engagement > Bolt Discovery > Settings
* **Events**: Data + Automations > Packs > Content Tokens > General tab
* **Forms**: Engagement > Forms > [Select Form] > Embed Code tab
* **Microsites**: Engagement > Microsites > [Select Site] > Settings > General tab
* **Pages**: Engagement > Pages > [Select Page] > Setup tab
* **StudentHub**: Engagement > StudentHub
* **Surveys**: Engagement > Surveys > [Select Survey] > Edit

When adding your container ID, ensure there are no spaces before or after it, as this will cause the script to fail.

*🧠 **Good to Know**: The GTM container ID can also be added to new Application Sites, Forms, Microsites, Pages, and Surveys during their creation.*

---

# Event Tracking Architecture

Element451 captures standardized events across all modules, including page loads, form submissions, appointment scheduling, and more. Every event includes rich metadata such as contact IDs, page paths, timestamps, and module-specific context for detailed analysis.

* **Discovery + Messenger Embeds**: Events automatically flow to your website's existing GTM container when Discovery or Messenger is embedded on your pages. When Bolt Discovery is accessed as a stand-alone page, it uses your global container configuration.

* **Consistent Data Structure**: Unified event naming and metadata format across all modules ensures reliable data collection and analysis.

Element451 pushes custom events and variables to the Google Tag Manager data layer, allowing Tag Manager to detect these events. You can then use these custom events as triggers within Tag Manager, enabling it to fire tags and pass variable values to other tools, such as Google Analytics.

## Complete Event Documentation (Events Tracked)

The following events and metadata are tracked across Element451 modules:

📌 ​*Note: A "guid" or Globally Unique Identifier is a unique ID for assets within Element451.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Module** | **Event Name** | **Fires When** | **Metadata** |
| Applications | Application Start | When a user completes the registration form and creates an account on the application site | applicationGuid, applicationName |
| Applications | Application Complete | When a user achieves an application completion percentage of 100% | applicationGuid, applicationName |
| Applications | Application Submit | When a user signs and submits an application | applicationGuid, applicationName |
| Appointments | Appointment User Selection | When a user selects from the Appointments Site | contactId, pagePath, clientName, method, staffSlug, card\_position |
| Appointments | Appointment Slot Selection | When a time slot on user availability is selected | contactId, pagePath, clientName, method, location, location\_type, staffSlug |
| Appointments | Appointment Scheduled | When a user successfully schedules an appointment | contactId, pagePath, clientName, method, location, location\_type, staffId, appointmentGuid, card\_position |
| Appointments | Appointment Canceled | When a user cancels an appointment | contactId, pagePath, clientName, appointmentGuid, method, location, staffId |
| Bolt Discovery | Discovery Used | When a user starts a Bolt Discovery thread | queryType, contactId, pagePath, messageLength, hasAttachments, formValid, threadSlug |
| Events | Event Registration | When a user submits an event registration form | contactId, eventName, eventGuid, eventCategories, eventDate |
| Forms | formSubmitted | When a user submits a form | pagePath, sourceUrl, formId, formName |
| Forms | formSubmittedLong | When a user submits a follow-up form | pagePath, sourceUrl, formId, formName |
| Forms | botSubmitDetected | When form submission is detected | pagePath, sourceUrl, formId, formName |
| Forms | formPaymentDone | When a user completes a form payment | pagePath, sourceUrl, formId, formName, couponCode, paymentAmount, paymentCurrency |
| Messenger | Messenger Chat Initiated | When the messenger widget is opened | contactId, channel (bot/human), locationPath |
| Messenger | Messenger User Message Sent | When a user sends a message or sends an attachment | contactId, messageType, conversationId, isNewConversation |
| Messenger | Messenger UI Button Clicked | When a user closes the messenger header, expands the header, or clicks a Conversation Starter | buttonType, location, buttonText, conversationId |
| Messenger | Messenger Voice Mode Activated | When a user activates Advanced Voice Mode | contactId, conversationId, assistantId |
| Messenger | Messenger Voice Mode Deactivated | When a user deactivates Advanced Voice Mode | contactId, conversationId, duration |
| Messenger | Messenger Chat Closed | When a user closes the messenger widget | contactId, sessionDuration, messagesExchanged |
| StudentHub | StudentHub Loaded | When StudentHub is loaded | contactId, pagePath, clientName |
| StudentHub | StudentHub Appointment ICS File Downloaded | When a user downloads an appointment ICS file | contactId, pagePath, clientName, fileName, sourceContext |
| Survey | Survey Completed | When a user submits a survey | contactId, surveyId, surveyName |

---

# Setting Up GTM to Capture Element451 Events

Follow this guide to configure Google Tag Manager to capture Element451 custom events and variables, enabling you to use them throughout Tag Manager.

*If you are not the Google Tag Manager administrator at your institution, you may need their permission to make these changes. Share this article for reference.*

## Step 1: Enable "Event" Built-In Variable

1. In Google Tag Manager, open the **Variables** tab from the left-side menu
2. Find the **Built-in Variables** section and click **Configure**
3. From the menu, select **Events** under Utilities

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717422581/1e30101dffad7f110d562e7535dd/Screenshot-2B2023-01-12-2Bat-2B3_46_34-2BPM.png?expires=1784333700&signature=42194db7e1a9d4599c22af68f788b8559a02b82d3b481b0e0c6dbb8439eb3a44&req=dScmEc18n4RXWPMW1HO4zVDUPQzYdRB3BZhQ8%2BXJ5LlaJABhss0OavIYk0T%2B%0AYeaAZXY8moyFIk586xw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717422581/1e30101dffad7f110d562e7535dd/Screenshot-2B2023-01-12-2Bat-2B3_46_34-2BPM.png?expires=1784333700&signature=42194db7e1a9d4599c22af68f788b8559a02b82d3b481b0e0c6dbb8439eb3a44&req=dScmEc18n4RXWPMW1HO4zVDUPQzYdRB3BZhQ8%2BXJ5LlaJABhss0OavIYk0T%2B%0AYeaAZXY8moyFIk586xw%3D%0A)

## Step 2: Create Custom Variables for Element451 Data

Under the **Variables** tab, locate the **User-Defined Variables** section and select **New** to create variables for the metadata you want to track:

1. Title the variable after the Element451 metadata field (e.g., "Element451 applicationGuid")
2. Click the **Variable Configuration** card to edit
3. Choose **Data Layer Variable** from the menu
4. For **Data Layer Variable Name**, enter the exact metadata field name (e.g., "applicationGuid")
5. Click **Save**

Repeat this process for any metadata fields you want to capture from the event documentation table above.

[![A screenshot of the Google Tag Manager interface, showing the settings and buttons required to complete the above.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717423891/8395483e4cf998523ee8f1fe82a0/Screenshot%2B2023-01-12%2Bat%2B3_47_38%2BPM.png?expires=1784333700&signature=9fefe1eec43a1b3d5175f1b191aa63b488679e626c605e01a86b6d825a9542df&req=dScmEc18nolWWPMW1HO4zRI8Gf0vOMszv717jieadb%2FnddO9M%2B1P3ZuQgU7W%0Au6wZAY1GAPHWjbaJn88%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717423891/8395483e4cf998523ee8f1fe82a0/Screenshot%2B2023-01-12%2Bat%2B3_47_38%2BPM.png?expires=1784333700&signature=9fefe1eec43a1b3d5175f1b191aa63b488679e626c605e01a86b6d825a9542df&req=dScmEc18nolWWPMW1HO4zRI8Gf0vOMszv717jieadb%2FnddO9M%2B1P3ZuQgU7W%0Au6wZAY1GAPHWjbaJn88%3D%0A)

## Step 3: Create Triggers for Element451 Events

1. In Google Tag Manager, open the **Triggers** tab
2. Select **New** to create a trigger
3. Name the trigger (e.g., "Element451 - Form Submitted")
4. Click **Trigger Configuration** to edit
5. Select **Custom Event** under Other
6. For **Event Name**, enter the exact Element451 event name (e.g., "Form Submitted")
7. Save the trigger

Repeat this process for each event you want to track, as listed in the event documentation table above.

Completing this setup allows Tag Manager to detect Element451's events, store Element451 variables for use in tags, and trigger tags based on custom events.

[![A screenshot of the Google Tag Manager interface, showing an example trigger discussed above.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717424613/fd644fd62ac9b79ae820465d3273/Screenshot-2B2023-01-12-2Bat-2B3_49_14-2BPM.png?expires=1784333700&signature=f3952c260a753e3cf9935da24c958acd2b5af77cd6e71ddb5434c49a8d86c422&req=dScmEc18mYdeWvMW1HO4zd4Nz593JMzvD7jLM7CXbWGEpfh4w5xJ%2F%2B20Btj3%0AKHxcbuFIOWyRdqE%2FET4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717424613/fd644fd62ac9b79ae820465d3273/Screenshot-2B2023-01-12-2Bat-2B3_49_14-2BPM.png?expires=1784333700&signature=f3952c260a753e3cf9935da24c958acd2b5af77cd6e71ddb5434c49a8d86c422&req=dScmEc18mYdeWvMW1HO4zd4Nz593JMzvD7jLM7CXbWGEpfh4w5xJ%2F%2B20Btj3%0AKHxcbuFIOWyRdqE%2FET4%3D%0A)

## Google Analytics (GA4) Integration

Create tags in Google Tag Manager to log events in Google Analytics when triggered by Element451 events.

*Before you begin, ensure you have created a [Google Analytics 4 Configuration Tag](https://support.google.com/tagmanager/answer/9442095?hl=en) in your Google Tag Manager container.*

## Creating a GA4 Event Tag

1. Open the **Tags** tab and select **New**
2. Name the tag (e.g., "Element451 - Milestone - Form (GA4)")
3. Click **Tag Configuration** and select **Google Analytics: GA4 Event**
4. For **Configuration Tag**, select your GA4 Configuration Tag
5. For **Event Name**, enter a descriptive name (e.g., "Milestone")
6. In **Event Parameters**, add relevant parameters:

   * Name: "action" | Value:
   * Name: "form\_id" | Value:
   * Name: "form\_name" | Value:
7. Set triggers to fire on relevant Element451 events  
   ​

   [![a screenshot of the Google Tag Manager interface, showing the settings of an example Tag discussed above.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717425704/02ca049915c259f9e9ea972a4468/Screenshot-2B2023-01-12-2Bat-2B3_57_54-2BPM.png?expires=1784333700&signature=df0ecd9aeb068e1e2cbaa80e44a3b4f3c00eea731a6c22ebe878d39cf99d5d28&req=dScmEc18mIZfXfMW1HO4zd%2B4FxZPYm%2FIFWlTOVCYORu23lMaRqH1offlOnUh%0AMUvK%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717425704/02ca049915c259f9e9ea972a4468/Screenshot-2B2023-01-12-2Bat-2B3_57_54-2BPM.png?expires=1784333700&signature=df0ecd9aeb068e1e2cbaa80e44a3b4f3c00eea731a6c22ebe878d39cf99d5d28&req=dScmEc18mIZfXfMW1HO4zd%2B4FxZPYm%2FIFWlTOVCYORu23lMaRqH1offlOnUh%0AMUvK%0A)

*Note: The parameter values use variables set up in Step 2 above. Use the lego plus icon next to the field to insert variables.*

## Example GA4 Event Configurations

**Application Events**

* Event Name: "Milestone"
* Parameters: action (), guid (), app\_name ()
* Triggers: Application Start, Application Complete, Application Submit

**Event Registration**

* Event Name: "Milestone"
* Parameters: action (), guid (), event\_name ()
* Triggers: Event Registration

*Why "Milestone"? These activities roughly correspond to Milestones within Element451, but you can use any event name that fits your analytics strategy.*

---

# Meta Ads Manager / Meta Pixel

The [Meta Ads Manager](https://www.facebook.com/business/tools/ads-manager) requires the [Meta Pixel](https://www.facebook.com/business/tools/meta-pixel) to be deployed on each page where page views and conversion events are logged.

## Deploying the Meta Pixel on Element451 Pages

If your Google Tag Manager instance already has a tag for the Meta Pixel, ensure that the tag will fire on Element451 pages. If the tag is triggered by "All Pages," this should work without issue. If the tag is triggered only on some pages, you may need to adjust the trigger to include your Element451 pages.

## Meta Pixel Deployment Options

* **Custom HTML Deployment**: Deploy via a Custom HTML tag by manually pasting the pixel code. Note that additional events beyond page views need to be configured in the code.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717427233/9dc2676ccdba98dd31302db28733/Screenshot%2B2024-02-29%2Bat%2B8_57_17-E2-80-AFAM.png?expires=1784333700&signature=a88dab91ba558cb1a3cbe54290ccd67eaa0cd6d8be4a6cebc93bdda4bce61bcc&req=dScmEc18moNcWvMW1HO4zVOk4oH945iCr4gj2w0BFEDXQZg7AgKJ9dTx0NR7%0AuS3C%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717427233/9dc2676ccdba98dd31302db28733/Screenshot%2B2024-02-29%2Bat%2B8_57_17-E2-80-AFAM.png?expires=1784333700&signature=a88dab91ba558cb1a3cbe54290ccd67eaa0cd6d8be4a6cebc93bdda4bce61bcc&req=dScmEc18moNcWvMW1HO4zVOk4oH945iCr4gj2w0BFEDXQZg7AgKJ9dTx0NR7%0AuS3C%0A)
* **Facebook Pixel Tag (Community Template)**: A more user-friendly option using the Community Template Facebook Pixel Tag from Meta. This template provides an interface where the Pixel ID can be easily added and events selected.  
  ​

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717427621/f7fd9e9d7884ad37e92dc7222239/Screenshot%2B2024-02-29%2Bat%2B8_52_53-E2-80-AFAM.png?expires=1784333700&signature=6c934abc7a2cc2ee8d909bb031eda07ed4793daa7f60df04ec8b727b10c5d1c5&req=dScmEc18moddWPMW1HO4zXzIAzLoXcXxPI%2FKGiMAKUr507qSDWgXofwQDw74%0AsBo%2F%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717427621/f7fd9e9d7884ad37e92dc7222239/Screenshot%2B2024-02-29%2Bat%2B8_52_53-E2-80-AFAM.png?expires=1784333700&signature=6c934abc7a2cc2ee8d909bb031eda07ed4793daa7f60df04ec8b727b10c5d1c5&req=dScmEc18moddWPMW1HO4zXzIAzLoXcXxPI%2FKGiMAKUr507qSDWgXofwQDw74%0AsBo%2F%0A)

## Element451 → Meta Event Mapping

Element451 events correspond to Meta Ads [standard events](https://www.facebook.com/business/help/402791146561655). Here are a few examples of how you could map them:

* **Form Submitted** → Lead
* **Application Submit** → SubmitApplication
* **Event Registration** → CompleteRegistration

## Creating Meta Pixel Tags

1. Open the **Tags** tab and select **New**
2. Name the tag (e.g., "FB - Element451 - Form Submit")
3. Click **Tag Configuration** and select **Facebook Pixel** from [Community Templates](https://help.element451.com/en/articles/5208134-advanced-tracking-with-google-tag-manager#h_d7e5bd4914)
4. For **Event Name**, select the appropriate Meta event (e.g., "Lead")
5. In **Object Properties**, add:

   * Property Name: "content\_name" | Property Value:
6. Set triggers to fire on relevant Element451 events
7. Repeat this process for other events using the parameters and triggers. For example:

   * **FB - Element451 - Application Start Tag**

     + Event Name: “CompleteRegistration”
     + Event Parameters:

       - Name: “content\_name”
       - Value:
     + Triggers**:**

       - Element451 - Custom Event - Application Start
   * **FB - Element451 - Event Registration Tag**

     + Event Name: “Milestone”
     + Event Parameters:

       - Name: “content\_name”
       - Value:
     + Triggers:

       - Element451 - Custom Event - Event Registration  
         ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717438144/bfbe62459e32f2357484acbc6b48/Screenshot%2B2024-02-29%2Bat%2B11_36_41-E2-80-AFAM.png?expires=1784333700&signature=bbf244b5c07ff8aa222e69ba69d7762e339223fd06e386fb5d5656effa42a3f1&req=dScmEc19lYBbXfMW1HO4zTzXKw8d2BANTzG%2FsxeNcjaiBVUH2YYDlg9L9AnB%0AGmf3%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717438144/bfbe62459e32f2357484acbc6b48/Screenshot%2B2024-02-29%2Bat%2B11_36_41-E2-80-AFAM.png?expires=1784333700&signature=bbf244b5c07ff8aa222e69ba69d7762e339223fd06e386fb5d5656effa42a3f1&req=dScmEc19lYBbXfMW1HO4zTzXKw8d2BANTzG%2FsxeNcjaiBVUH2YYDlg9L9AnB%0AGmf3%0A)

## Meta Ads Domain Verification

Meta Ads requires [domain verification](https://developers.facebook.com/docs/sharing/domain-verification/verifying-your-domain#html) for conversion tracking. Only the DNS TXT file method works with Element451 pages if you have configured an [external domain](https://help.element451.com/en/articles/9358702-configuring-external-domains):

* **Subdomain configuration** (e.g., "info.university.edu"): Add TXT file to your main website's DNS
* **Separate domain** (e.g., "universityadmissions.com"): Add TXT file to this domain's DNS

---

# Common Use Cases

* **Logging custom events in Google Analytics** - Track student engagement and conversion milestones
* **Logging ad conversions in digital ad platforms** - Measure ROI on Google Ads and Meta campaigns
* **Triggering retargeting ads** - Create audiences based on specific Element451 interactions

📌 *Note: These use cases are configured entirely within Google Tag Manager or other third-party platforms. The Element451 Customer Success team can confirm the presence of your Google Tag Manager container on pages where it is deployed, but cannot verify configurations within Google Tag Manager or third-party platforms.*

---

## Advanced Configuration Tips

1. **Test your setup** using Google Tag Manager's Preview mode to verify events fire correctly
2. **Use consistent naming conventions** for tags, triggers, and variables to maintain organization
3. **Document your configuration** for future reference and team collaboration
4. **Monitor data quality** regularly to ensure accurate tracking across all modules
5. **Start simple** - implement basic event tracking before adding complex custom parameters

This comprehensive GTM integration eliminates the complexity of managing multiple tracking implementations while providing unprecedented visibility into user engagement across your entire Element451 ecosystem.

---