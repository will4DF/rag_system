---
title: Configuring External Domains
url: https://help.element451.com/en/articles/9358702-configuring-external-domains
collection: Settings + Permissions
---

Learn how to configure external domains in Element451 to enhance your site's branding. Set up CNAME records for a branded, recognizable URL.

# Overview

When setting up your public-facing pages and sites in Element451, you’ll encounter two types of domains: a **primary** **domain** and an **external** **domain**. Understanding the differences between these is essential for maintaining your institutional brand identity and ensuring a seamless user experience.

## Primary Domain

Your public-facing pages and sites come with a default domain, known as the primary domain. This domain is provided by Elemente451 and cannot be edited. It typically looks something like this: `fireuniversity-2155.page451.sites.451.io`. While functional, this URL lacks the brand identity and trust associated with a .edu URL.

🚨 **Important:** Primary domains cannot be accessed by Google or other web crawlers. This prevents unbranded URLs from appearing in search results. Consequently, ad providers, including Google Ads, may not allow you to direct ads to the primary domain.

## External Domain

To enhance your site’s branding and user experience, you can configure external domains that point to your site. These external domains can mask or hide the primary domain, allowing you to use a more recognizable URL, such as yourschool.edu. To set this up, you’ll need to add a CNAME record in your Domain Name Services (DNS) tool that points your external domain to Element451. Then, you'll need to add it in the module settings in Element451.

The process of adding your external domains by module is listed below:

---

# Configuring External Domains

## Application Sites

#### Step 1: Create a CNAME Record

1. Decide on the custom URL (CNAME) you want to use, ideally in collaboration with your marketing department. For example, Fire University might choose **`apply.elementu.edu`** or **`start.elementu.edu`**.
2. Have your IT or web team point this CNAME to **`app451.sites.451.io`**.

#### Step 2: Add Your CNAME To Application Site Settings

1. Navigate to **Application > Applications > Sites** and locate the site.
2. Open the site editor and navigate to the **Domains** tab.
3. Click the **Add** **Host** button, enter your **CNAME**, and click **Save**.

[Explore More: Application Sites](https://help.element451.com/en/articles/9077560-application-sites)

## Appointment Site

#### Step 1: Create a CNAME Record

1. Decide on the custom URL (CNAME) you want to use, ideally in collaboration with your marketing department. For example, Fire University might choose **`appointments.elementu.edu`** or **`meet.elementu.edu`**.
2. Have your IT or web team point this CNAME to **`appointment451.sites.451.io`.**

#### Step 2: Add Your CNAME To Appointment Page Settings

1. Navigate to **Engagement > Appointments.**
2. Click the more icon (three vertical dots) in the top right corner of the header.
3. Click **Page** **Settings**.
4. Click the **Add** **Host** button, enter your **CNAME**, and click **Save**.

[Explore More: Appointments Site](https://help.element451.com/en/articles/8141376-getting-started-with-appointments-for-admins)

## Events Site

#### Step 1: Create a CNAME Record

1. Decide on the custom URL (CNAME) you want to use, ideally in collaboration with your marketing department. For example, Fire University might choose **`events.elementu.edu`** or **`visit.elementu.edu`**.
2. Have your IT or web team point this CNAME to **`event451.sites.451.io`**.

#### Step 2: Add Your CNAME To Event Settings

1. Navigate to **Engagement** > **Events > Event Sites.**
2. Select the Event Site you want to configure.
3. From the left-hand menu, click **Domains**.
4. Click the **Add** **Host** button, enter your **CNAME**, and click **Save**.

[Explore More: Events Site](https://help.element451.com/en/articles/8981854-event-settings-your-event-site)

## Microsites

**Step 1: Create a CNAME Record**

1. Decide on the custom URL (CNAME) you want to use, ideally in collaboration with your marketing department. For example, Fire University might choose **`admit.elementu.edu`** or **`newstudent.elementu.edu`**.
2. Have your IT or web team point this CNAME to **`microsite451.sites.451.io`**.

**Step 2: Add Your CNAME To Microsite Settings**

1. Navigate to **Engagement** > **Microsites** and locate the microsite.
2. Open the microsite editor and click on the eye icon ("visit the site") in the top right corner of the header.
3. Click the **Add** **Host** button, enter your **CNAME**, and click **Save**.

[Explore More: Microsites](https://help.element451.com/en/articles/9274424-getting-started-with-microsites)

## Pages

There are two ways of configuring your CNAME entries for Pages to show a branded URL. You can either create a CNAME for each page or use a wildcard. Your IT or web development team(s) will likely need to add/edit the CNAME entries.

**Step 1: Create a CNAME Record**

1. Decide on the custom URL (CNAME) you want to use, ideally in collaboration with your marketing department. For example, Fire University might choose **`info.elementu.edu`** or `academics.elementu.edu`.
2. Have your IT or web team point this CNAME to **`page451.sites.451.io`**.
3. For a wildcard setup, prepend an asterisk to your CNAME, like **`*.academics.fire.edu`**. We explain more about a [wildcard domain](#h_c61ca422b1) below.

**Step 2: Add Your CNAME To Page Settings**

1. Navigate to **Engagement** > **Pages** and locate the page.
2. Open the page editor and navigate to the **Domains** tab.
3. Click the **Add** **Host** button, enter your **CNAME**, and click **Save**.

### Using a Wildcard Domain

If you set up a wildcard, you can assign specific subdomains to different pages. For instance, if Fire University's wildcard CNAME is **`academics.fire.edu`**, we could use **`biology.academics.fire.edu`** for the biology program page and **`nursing.academics.fire.edu`** for the nursing page without having to create additional CNAME entries.

[Explore More: Pages](https://help.element451.com/en/articles/2582895-creating-managing-pages)

## StudentHub (Beta)

#### Step 1: Create a CNAME Record

1. Decide on the custom URL (CNAME) you want to use, ideally in collaboration with your marketing department. For example, Fire University might choose **`studenthub.elementu.edu`** or **`portal.elementu.edu`**.
2. Have your IT or web team point this CNAME to **`portal451.sites.451.io`.**

#### Step 2: Add Your CNAME To StudentHub Settings

1. Navigate to **Engagement > StudentHub.**
2. Scroll down to the **Domains** card.
3. Click the **Add** **Host** button, enter your **CNAME**, and click **Save**.

[Explore More: StudentHub Settings](https://help.element451.com/en/articles/9956808-studenthub-settings-configuration)

---

# For IT Administrators

Element451 has instituted a method to generate the required security certificates for the requested URL. This method leverages the work done by the non-profit entity Let's Encrypt to create and update the certificates. You can see details on how this works on their [website](https://letsencrypt.org/how-it-works/).

When using this method, neither your IT staff nor Element451 Support require support. The certificates will be automatically generated and installed every 90 days indefinitely.

---