---
title: Element451 Tracking Pixel
url: https://help.element451.com/en/articles/5208086-element451-tracking-pixel
collection: Settings + Permissions
---

## Overview

The Element451 tracking pixel enables you to track student activity on your institution's website. When students visit your site, their page views and link clicks will appear in their Element451 profiles, allowing you to segment students based on website behavior and create targeted communications.

The tracking pixel is seamlessly integrated into the Messenger embed code, providing a streamlined implementation process. Even if Messenger is disabled or hidden on specific pages, the tracking pixel will still collect analytic data.

*Note: Depending on how your institution's website is managed, this may require involvement from your marketing, web team, or information technology.*

## What Gets Tracked

With the tracking pixel implemented, you'll see the following student activities from your website appear in their Element451 profiles:

* **Page views** - Which pages students visit and how often
* **Link clicks** - Which links students click and where they lead

This data appears in student profiles and can be used for segmentation, automation, and more.

---

# Implementation Options

The Element451 tracking pixel can be added to your website through:

* Google Tag Manager
* Direct placement on each page
* Other tag management software

## 1. GTM Implementation

### Step 1: Get Your Tracking Pixel Code

1. In Element451, navigate to **Engagement > Conversations > Settings**
2. Select **Messenger** from the left menu
3. Scroll to the **Embed Code** field and click the copy icon

*Note: The tracking pixel is included within the Messenger embed code, streamlining the setup process.*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717444833/67de9217b7d2f414a4211c567d58/Screenshot-2B2024-06-04-2Bat-2B4_59_44-E2-80-AFPM.png?expires=1784333700&signature=f67b5d3dcfd04f813045c8dd53e19bb3eca0b7e45d51aa1c5997f03a1097e3dd&req=dScmEc16mYlcWvMW1HO4zcYB5xyrA9d9wDibmXEqOnDkMpe3tSHLhYEAiUmw%0AQw%2F8RhcTvuAdpwFqadg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717444833/67de9217b7d2f414a4211c567d58/Screenshot-2B2024-06-04-2Bat-2B4_59_44-E2-80-AFPM.png?expires=1784333700&signature=f67b5d3dcfd04f813045c8dd53e19bb3eca0b7e45d51aa1c5997f03a1097e3dd&req=dScmEc16mYlcWvMW1HO4zcYB5xyrA9d9wDibmXEqOnDkMpe3tSHLhYEAiUmw%0AQw%2F8RhcTvuAdpwFqadg%3D%0A)

### Step 2: Create a Custom HTML Tag in GTM

1. Open your GTM container for your website
2. Go to **Tags > New**
3. Choose "Custom HTML" as the tag type  
   ​

   [![A screenshot of the Google Tag Manager interface, showing which tag type to select when creating a Tag.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717445291/d74f3a27f9c2c44f75a7a2dc9839/Google-Tag-Manager-2B-281-29.png?expires=1784333700&signature=8faafc99b03d082d31d88e9976eceb18d8288905b9983af7aa9018cf2a139bc6&req=dScmEc16mINWWPMW1HO4zcvIOtMic1sr7O1N2YHMLEDbhYsjMCTu7qLNrqpj%0AZhdn%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717445291/d74f3a27f9c2c44f75a7a2dc9839/Google-Tag-Manager-2B-281-29.png?expires=1784333700&signature=8faafc99b03d082d31d88e9976eceb18d8288905b9983af7aa9018cf2a139bc6&req=dScmEc16mINWWPMW1HO4zcvIOtMic1sr7O1N2YHMLEDbhYsjMCTu7qLNrqpj%0AZhdn%0A)
4. Paste your Element451 tracking pixel code

   [![A screenshot of the Google Tag Manager interface, showing the field in which to paste the Live Chat embed code.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717446020/460a5b09ff54da63c97a61d6d30b/Google-Tag-Manager-2B-282-29.png?expires=1784333700&signature=3715fc090a0d8a0e52d48cd163a62d4c9204797187987c7bb8bdad5ddc5a5e2d&req=dScmEc16m4FdWfMW1HO4zYjgb73ohUbv9r%2FuhL1jiWsOqsOXcnt5tAzf2Wfa%0ADl62%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1717446020/460a5b09ff54da63c97a61d6d30b/Google-Tag-Manager-2B-282-29.png?expires=1784333700&signature=3715fc090a0d8a0e52d48cd163a62d4c9204797187987c7bb8bdad5ddc5a5e2d&req=dScmEc16m4FdWfMW1HO4zYjgb73ohUbv9r%2FuhL1jiWsOqsOXcnt5tAzf2Wfa%0ADl62%0A)
5. Set the trigger to "All Pages except Element451 Pages" (see Step 3 below)
6. Save and publish your container

### Step 3: Exclude Element451 Pages from GTM Tag

Since the tracking pixel is already embedded on Element451 Application Sites, Event Sites, Forms, Microsites, and Pages, adding your GTM container to these pages can cause duplicate tracking. To avoid this:

**Identify Your Element451 URLs**:

* List URLs for Pages, Application Sites, and Events (e.g., "events.yourinstitution.edu")
* Include any custom domains or subdomains you use for Element451 modules

**Create an Exclusion Trigger in GTM**:

1. Select **Triggers** from the left menu
2. Click **New** to create a new trigger
3. Name your trigger (e.g., "All Pages except Element451")
4. Select **Page View** and set the trigger to fire on **Some Page Views**
5. Add conditions for each URL in your list:

   * Page URL **does not contain** [your Element451 URL]
   * Create a separate condition for each Element451 domain/subdomain
6. Save the trigger and apply it to your tracking pixel tag

### Step 4: Verify Implementation

1. Visit your website and check that the pixel is firing in GTM Preview mode
2. Student activities should begin appearing in Element451 profiles
3. Verify that the pixel is NOT firing on Element451 pages to avoid duplicate tracking

## 2. Direct Page Implementation

If you prefer not to use GTM, you can add the tracking pixel directly to your website:

1. Get your tracking pixel code from Element451 (Step 1 above)
2. Add the code to the `<head>` section of each page on your website
3. Ensure the code appears on all pages where you want to track activity

## 3. Other Tag Management Platforms

The Element451 tracking pixel can be implemented through other tag management systems following similar principles:

1. Create a custom HTML tag with your Element451 pixel code
2. Set the tag to fire on all pages of your website
3. Exclude Element451 pages to avoid duplicate tracking
4. Test and verify implementation

---

# Controlling Messenger Display

The Element451 tracking pixel is embedded within the Messenger code for simplicity. This single piece of code gives you both website tracking and the option to display Messenger chat functionality. However, you can hide Messenger while keeping tracking active, as the tracking pixel operates independently of Messenger visibility.

## On Non-Element451 Pages (Your Website)

Configure display conditions in Element451:

1. Navigate to **Engagement > Conversations > Settings**
2. Select **Messenger** from the left menu
3. Under **Conditions**, click **Add Filter**
4. Choose a filter type (Page URL, Path URL, UTM Parameters)
5. Set the **Operator** and **Value** for the filter
6. Add as many filters as needed

## On Element451 Pages

Enable Messenger on your internal Element451 pages and sites by activating the 'Activate Messenger' setting for each module. This doesn't require any additional coding. For more details on this process, [click here](https://help.element451.com/en/articles/6249763-messenger-live-chat#h_ed141f49a4).

*Important: Always configure conditions in Element451 rather than GTM. This ensures that the tracking pixel still fires even if Messenger is hidden.*

---

# Hiding the GTM Tag from Element451 Pages and Sites

Since the tracking pixel is already embedded on Element451 Application Sites, Event Sites, Forms, Microsites, and Pages, adding your GTM container to these pages can cause duplicate tracking. To avoid this:

1. **Identify URLs**:

   * List URLs for Pages, Application Sites, and Events (e.g., "events.yourinstitution.edu").
2. **Create a Trigger in GTM**:

   * Select **Triggers** from the left menu.
   * Click **New** in the top right to create a new Trigger.
   * Name your Trigger (e.g., "All Pages except Element451").
   * Select **Page View** and set the trigger to fire on **Some Page Views**.
   * Add conditions for each URL in your list (Page URL **does** **not** contain the URL).
   * Create a condition for each URL on your list.
   * Save the Trigger and apply it to your tracking pixel / Messenger embed Tag.  
     ​

     [![A screenshot of the Google Tag Manager interface, showing the settings to configure for the Trigger listed above.](https://downloads.intercomcdn.com/i/o/652153574/4cf53a98960ce6f7d983b653/Screenshot+2023-01-13+at+2.39.16+PM.png?expires=1784333700&signature=1427db4928743014095a17f2f530d714b6d9ed5461991310dd587f6688534def&req=ciUlF8x9mIZbFb4f3HP0gLv1VsTSQJ7tyKLUkvijKohQUUTj75893EwAMS0Z%0A96c%3D%0A)](https://downloads.intercomcdn.com/i/o/652153574/4cf53a98960ce6f7d983b653/Screenshot+2023-01-13+at+2.39.16+PM.png?expires=1784333700&signature=1427db4928743014095a17f2f530d714b6d9ed5461991310dd587f6688534def&req=ciUlF8x9mIZbFb4f3HP0gLv1VsTSQJ7tyKLUkvijKohQUUTj75893EwAMS0Z%0A96c%3D%0A)

---

# Best Practices

1. **Test thoroughly** - Use GTM Preview mode to verify the pixel fires correctly on your website but not on Element451 pages
2. **Monitor data quality** - Check Element451 profiles to confirm website activities are appearing correctly
3. **Document your setup** - Keep track of which domains and pages you've excluded from tracking
4. **Coordinate with your team** - Ensure your web/marketing teams understand the tracking setup
5. **Review regularly** - As you add new Element451 modules or change domains, update your exclusion triggers accordingly

---

# Troubleshooting

**Pixel not firing on website**:

* Check that the GTM tag is published
* Verify the trigger is configured correctly
* Confirm the Element451 embed code is complete and unmodified

**Duplicate tracking on Element451 pages**:

* Review your GTM trigger exclusions
* Ensure all Element451 domains are properly excluded
* Check that you haven't added the pixel code directly to Element451 modules

**Activities not appearing in profiles**:

* Verify students are known contacts in Element451
* Check that the pixel code matches your institution's configuration
* Confirm GTM container is published and active

---

# Pro Tip: Add Your Google Tag Manager ID

For complete tracking coverage, consider also utilizing [Google Tag Manager](https://claude.ai/chat/link-to-gtm-article) to capture detailed events from Element451 modules and send them to analytics platforms. The two implementations work together to provide comprehensive tracking:

* **Tracking Pixel**: Website activity → Element451 profiles
* **GTM Integration**: Element451 events → Analytics platforms

#

---