---
title: Adding Knowledge Hub Sources
url: https://help.element451.com/en/articles/12276752-adding-knowledge-hub-sources
collection: Bolt AI
---

Learn how to add knowledge hub sources, keep knowledge in sync, organize it, and maintain it efficiently.

# Overview

Your Knowledge Hub is only as strong as the sources you add to it. In this article, you’ll learn how to add and manage different source types — including text, URLs, website sitemaps, file uploads, and custom answers. You’ll also see how to keep your knowledge up to date with features like **Daily Sync** and **New Page Detection**, organize sources with folders and categories, and troubleshoot common issues.

By following the steps outlined here, you’ll build a well-structured, accurate Knowledge Hub that powers smarter, more reliable answers across Bolt Agents and Bolt Discovery.

---

# Add a Source (All Types)

1. Go to **Data + Automations > Knowledge**
2. Select **"Public"** or **"Private"** from the left-hand menu (the repository you want to add the source to)  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722936930/e29c539c495bbff6d19209f09d9c/Screenshot%2B2024-01-05%2Bat%2B9_01_34-E2-80-AFAM.png?expires=1784333700&signature=f61518d6109434235af287f6ba08d3af51b538ff07c5a64326a406c85b85ac51&req=dSclFMB9m4hcWfMW1HO4zQFb%2FQKmAEGj3UTjyMepVh11kDvgUU4igADqaBKo%0A5knN%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722936930/e29c539c495bbff6d19209f09d9c/Screenshot%2B2024-01-05%2Bat%2B9_01_34-E2-80-AFAM.png?expires=1784333700&signature=f61518d6109434235af287f6ba08d3af51b538ff07c5a64326a406c85b85ac51&req=dSclFMB9m4hcWfMW1HO4zQFb%2FQKmAEGj3UTjyMepVh11kDvgUU4igADqaBKo%0A5knN%0A)
3. Click **+ New Source** in the header
4. Configure:

   * **Title:** Use meaningful titles (“Admissions: Deadlines 2025”, “FA: SAP Policy”). It helps your team and also assists Bolt Agents in selecting the best source.
   * **Type:** Source types are explained in the next section
   * **Folder:** Optional, but highly recommended to keep your sources organized (see Folders section below for more details)
   * **Categories:** Optional, but highly recommended for organization, and also because you can scope a Bolt Agent's access to knowledge by Category
   * **Type-specific fields:** Upon selecting a source type, you'll be prompted to configure its specific details.

     + **Text**: Content
     + **URL**: URL, Sync Daily
     + **Website**: URL, Sync Daily, New Page Detection
     + **File** **Upload**: File
     + **Custom Answers**: Question and Answer
5. **Save**. The source will enter the "**Learning**" state and take a few minutes to be ingested.

---

# Source Types

## Text

Paste plain text (rich formatting/links aren’t retained)

* When pasting data from a table or similar source, ensure that it is clear which data relates to which other data
* Bolt AI can parse dense blocks of text, but you may want to organize it/make it legible to make it easier for a human editor can maintain it

## URL (Single Page) + Website (Sitemap)

You can load pages from your website into the Knowledge Hub using two methods: URL and Website sources:  
​

## 1) URL (Single Page)

Ingest a single, specific page (e.g., <https://school.edu/admissions-faq>)

* Enable optional **Sync Daily** (see Daily Sync section below)

📌 **Note**: When a URL source contributes to an answer in Messenger or Bolt Discovery, the source citation may be visible to the contact, depending on the feature and your settings. Refer to the Citations section below for more information.

## 2) Website (Sitemap)

Enter a root domain (auto-detect robots.txt/sitemap.xml) or a specific sitemap URL (.xml or .xml.gz). The sitemap will load, allowing you to choose which pages you wish to ingest.

* When a sitemap is loaded, you’ll see the **main file** Element451 used to discover related sitemaps (e.g., robots.txt, sitemap index). Related sitemaps are listed beneath it (e.g., news, video, events).
* Compressed `.xml.gz` files are supported and ingested just like standard XML sitemaps.
* If you enter a root domain (e.g., elementuniversity.edu), Element451 will look for a robots.txt or a standard sitemap.xml.
* If you enter a URL ending in .xml, Element451 treats it as the **explicit sitemap** and bypasses robots.txt.
* Enable optional **Daily Sync** and **New Page Detection** (see Daily Sync + New Page Detection section below)

### Filtering Sitemap Pages

Once your sitemap loads, the pages will be listed in a table with checkboxes for you to select which ones you want ingested. To help you narrow down the list, you can apply **filters** to control which pages appear in the table. This is especially useful for large sitemaps where you only want to ingest specific types of content.

You can apply one or **both** of the following filter operators:

* **Include** – Show only URLs that **contain** the specified text. If you enter multiple values, it will match **any** of them.
* **Exclude** – Hide any URLs that **contain** the specified text.

You can combine these filters to refine your results. For example:

* **Include:** academics
* **Exclude:** science

  This will show only pages with URLs that contain “academics” but do not contain “science.”

These filters help you focus on the most relevant content before selecting which pages to ingest into your knowledge base.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1816772220/2fbcd1f0a24751c5ecc347236b07/Website+Source+Include-Exclude+Filter.png?expires=1784333700&signature=ecc48e5d5d5b11a2332d6cbee68d0affdd5dc0c9bd0ff418612f94c12ea4e0e7&req=dSgmEM55n4NdWfMW1HO4zUYV1AwQnWtwpbwDNp0NTC%2BJTSCZlwb9gM8q2VU%2F%0A1tMZeReFS6afhO%2FOsVw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1816772220/2fbcd1f0a24751c5ecc347236b07/Website+Source+Include-Exclude+Filter.png?expires=1784333700&signature=ecc48e5d5d5b11a2332d6cbee68d0affdd5dc0c9bd0ff418612f94c12ea4e0e7&req=dSgmEM55n4NdWfMW1HO4zUYV1AwQnWtwpbwDNp0NTC%2BJTSCZlwb9gM8q2VU%2F%0A1tMZeReFS6afhO%2FOsVw%3D%0A)

After selecting pages, and clicking "create," you’ll be presented with a confirmation dialogue with a summary of how many URLs will be added before ingestion begins.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1816810638/cb435c9a3c1c3ed7c1c7bbf620c5/Website+Source+Confirmation.png?expires=1784333700&signature=5e0c5f6e72884c6d92b48657653b167d7860eeb58b8e1597ef8c2a320fce2a50&req=dSgmEMF%2FnYdcUfMW1HO4zZtK1rqsYDQtQ8uW50mhEtGT%2FmAyPF59j%2FYNwH3s%0AbyDatoF03xgwhKVo0xw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1816810638/cb435c9a3c1c3ed7c1c7bbf620c5/Website+Source+Confirmation.png?expires=1784333700&signature=5e0c5f6e72884c6d92b48657653b167d7860eeb58b8e1597ef8c2a320fce2a50&req=dSgmEMF%2FnYdcUfMW1HO4zZtK1rqsYDQtQ8uW50mhEtGT%2FmAyPF59j%2FYNwH3s%0AbyDatoF03xgwhKVo0xw%3D%0A)

📌 **Note**: When a Website source contributes to an answer in Messenger or Bolt Discovery, the source citation may be visible to the contact, depending on the feature and your settings. Refer to the Citations section below for more information

Some websites will prevent our content scraper from accessing webpages. This may appear as a 403 error. If this is the case your web team may need to whitelist the following IP address: **54.82.10.251.**

### Daily Sync (URL + Website Sources)

When "Daily Sync" is enabled for a URL or Website source, Bolt AI detects updates via, in priority order:

* **HTTP headers**

  + **ETag**: Reindex if different from the previous value
  + **Last-Modified** header variations: `last-modified`, `x-last-modified`, `x-amz-meta-last-modified`
  + **Content hashes**: `x-content-hash`, `content-md5`, `x-checksum`
  + **AWS S3 version**: `x-amz-version-id`
* **Sitemap**

  + Fetches sitemap.xml (or sitemaps listed in robots.txt)
  + Checks the `lastmod` value for the specific page
* **HTML Meta** **Tags**

  + **Modified/Updated dates**: `article:modified_time`, `og:updated_time`, `last-modified`, `DC.date.modified`, `dcterms.modified`, `modified`, `updated`, `revised`
  + **Published/Created dates**: `article:published_time`, `og:article:published_time`, `DC.date`, `DC.date.created`, `dcterms.created`, `date`, `publish_date`, `publishdate`, `pubdate`, `created`
* **Structured Data**

  + **JSON-LD**: `dateModified`, `datePublished`, `dateCreated`
  + **Schema.org microdata**: `itemprop="dateModified"`, `itemprop="datePublished"`
  + HTML5 `<time>` tags with datetime attributes
* **RSS** item timestamps

  + Compares the `isoDate` field from RSS feed items against the last indexed date

If a change is detected, the page is re-indexed; if not, it’s skipped.

✨ **Pro Tip:** For the most accurate and timely updates, include at least one of the high-priority indicators—such as an ETag header, a `Last-Modified` header, or an accurate `lastmod` date in your sitemap.

### New Page Detection (Website Sources)

When Daily Sync is enabled for a **Website** Source, you have the option to turn on the **Detect New Pages** feature.

* Element451 automatically detects and ingests new pages added to your sitemap.
* Use the **New Pages Filter** to limit automatic detection to specific URL patterns—like "blog" so only relevant new pages are ingested as they’re added to your website.

  + If no filter is set, **all new pages** found in your sitemap will be ingested by default.
  + You can refine this filter using the **Include** (shows only URLs that contain the specified text) and **Exclude** (hides URLs that contain the specified text) operators. You can also combine these operators for a more refined search.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722933497/a383689583e2916ac15a5efe868b/Detect-2BNew-2BPages.png?expires=1784333700&signature=d839f450696528f5adaa50eb8302414640debfac5a6084d151fdf2b68af110af&req=dSclFMB9noVWXvMW1HO4zaPsA8984T1eSy23U2pqr4rwMvRr4safvm5UvVn1%0A%2BdjPcno9FymXw1nlL78%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722933497/a383689583e2916ac15a5efe868b/Detect-2BNew-2BPages.png?expires=1784333700&signature=d839f450696528f5adaa50eb8302414640debfac5a6084d151fdf2b68af110af&req=dSclFMB9noVWXvMW1HO4zaPsA8984T1eSy23U2pqr4rwMvRr4safvm5UvVn1%0A%2BdjPcno9FymXw1nlL78%3D%0A)

## RSS Feed

Ingest content from an RSS feed URL (e.g., a campus events feed or news blog). Bolt AI reads the articles published to the feed and learns their content. RSS feeds are checked daily for new articles automatically.

**Setup:**

1. Select **RSS** **Feed** as the source type

2. Enter the **URL** of the RSS feed

3. Optionally assign a **Folder** and **Categories** for organization

4. **Save**

**Key points:**

* RSS feeds are checked daily for new articles—no toggle needed, this is the default behavior
* Bolt AI ingests both the linked page content and any plain text content published directly in the feed
* Useful for dynamic content like campus events, news, and blog posts that update frequently

## File Upload

File types supported: .eml, .html, .json, .md, .msg, .rst, .rtf, .txt, .xml, .jpeg, .png, .csv, .doc/.docx, .epub, .odt, .pdf, .ppt/.pptx, .tsv, .xlsx

⚠️ Particularly large files can cause parsing errors. While there is no strict file size maximum, files exceeding 10MB tend to have a higher failure rate. While you can simply retry to learn the file, we recommend breaking larger files into smaller content chunks of approximately 10MB or less.

Note: When a File Upload source contributes to an answer in Bolt Discovery, its citation is displayed by default. To hide it from contacts, disable Show File in Citations? on that source. Refer to the Citations section below for more information.

## Custom Answers (Groups of Q&A Pairs)

Custom answers are predetermined question-and-answer pairs for your most frequently asked and important questions (think high-impact FAQs and precise facts).

Custom Answers are given **priority** but are **not** **repeated** **word-for-word**. See the Custom Answer Behavior section below for more details.

### Adding Custom Answers + Importing/Exporting

To add a new custom answer or group of customer answers:

1. Click the **+** **sign**. The sidesheet will open for you to add your question and answer pairs. *Note: You do not need to add each custom answer as a separate source. You can add as many relevant questions and answers to this "group" as you would like.*  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722918944/b520506d9df513760762505a5974/Custom%2BAnswers%2Bexample.png?expires=1784333700&signature=c238634a63cdee2bfbc064b7a2e0cf42a5dc8dbea03dd357b9b69071e7304e6a&req=dSclFMB%2FlYhbXfMW1HO4zTBNnOCPtkz2KxwlgziCoYs10PGszmhgM4Sd8g7y%0AfIzT%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722918944/b520506d9df513760762505a5974/Custom%2BAnswers%2Bexample.png?expires=1784333700&signature=c238634a63cdee2bfbc064b7a2e0cf42a5dc8dbea03dd357b9b69071e7304e6a&req=dSclFMB%2FlYhbXfMW1HO4zTBNnOCPtkz2KxwlgziCoYs10PGszmhgM4Sd8g7y%0AfIzT%0A)
2. Give the source a **title** at the top of the page. For example, if you add questions about the application process, you can title it "application process."
3. Type your question (e.g., How do I apply?)
4. Type your answer (e.g., You can apply to Training University by completing a common application or using the TU application at apply.training.edu.)
5. You can add additional Q&A pairs to this "group" of custom answers by clicking the **+ sign** again, or if you are finished, click **Save**.

## Importing and Downloading Custom Answers

* You can **import** an existing list of questions and answers via a CSV file. Click the **upload** button and attach your file (it must contain two columns: **question** and **answer**). If you are editing an existing group of custom answers, importing a CSV file will **overwrite** the current data with the questions and answers from the imported file.
* To **export** or **download** this group of custom answers, click the **download** button to initiate a CSV file download.

  [![](https://downloads.intercomcdn.com/i/o/823595263/049b75134be11c3952069e8d/Export+and+Import+Custom+Answers.png?expires=1784333700&signature=c2d5ad488cf9308ab3043f298fd447bed6cece501733fb3b36c88629a6862b7b&req=fCIkE8B7n4dcFb4f3HP0gNhlYot5VEbaPCamXnUUBqd6WIzLIRXwf8eirnIe%0AzV4%3D%0A)](https://downloads.intercomcdn.com/i/o/823595263/049b75134be11c3952069e8d/Export+and+Import+Custom+Answers.png?expires=1784333700&signature=c2d5ad488cf9308ab3043f298fd447bed6cece501733fb3b36c88629a6862b7b&req=fCIkE8B7n4dcFb4f3HP0gNhlYot5VEbaPCamXnUUBqd6WIzLIRXwf8eirnIe%0AzV4%3D%0A)

  If you need to update an existing group of custom answers, we recommend using the download feature, editing the CSV file provided, saving your changes, and then importing the updated CSV file back into Element451.

### Important: Custom Answer Behavior

Custom Answers are prioritized over other sources, and Bolt Agents may **paraphrase** these answers appropriately and include additional information from other relevant sources.

For example, let's take this Custom Answer:

Q: "How many programs are offered at Element University?

A: There are 20 undergraduate programs, 10 graduate programs, and 5 certificate programs."​

When asked about the programs at Element University, the agent might say, "Element University offers a total of 35 programs."​

While this paraphrase is accurate, it's not a word-for-word match. The agent uses the content of the Custom Answer but adapts it based on the conversation's context.

## Zendesk (Closed Beta)

Connect your Zendesk Help Center directly to Bolt Knowledge to ingest articles via the Zendesk API—no web crawling required. This is ideal for institutions that maintain a Zendesk-based help center, especially when crawler access is blocked by security tools like Cloudflare.

### Setup:

1. Select **Zendesk** as the source type
2. Enter your **Zendesk subdomain** (e.g., elementcollege from elementcollege.zendesk.com)
3. Enter the **Email** associated with your Zendesk account
4. Enter an **API token**

   * Generated in Zendesk Admin → Channels → API.

### Options:

* **Include staff-only articles** — Toggle on to ingest articles restricted to internal staff
* **Include login-required articles** — Toggle on to ingest articles that require Zendesk authentication to view
* **Sync daily?** — Enable to automatically re-sync articles from Zendesk on a daily basis

### Selecting articles:

Once connected, a table displays all available Zendesk Help Center articles with their titles and URLs. Use **Select All** or **Deselect All** to control which articles Bolt AI should learn from.

If you are interested in participating in the Zendesk closed beta, please contact support.

---

# Citations in Answers

When a **URL**, **Website**, or **File Upload** source contributes to an answer, the source citation may be visible to the contact, depending on the feature and your settings.

The citation enables contacts to access more context and directly view the sources that informed their answers, thereby improving trust, usability, and engagement.

## Show File in Citations? toggle

For **File Upload**, **URL**, and **Website** source types, you can control whether a source appears as a citation in **Bolt Discovery** by toggling **Show File in Citations?** on the source. Turn this off to use a web-based source for answers (with Daily Sync keeping it current) without exposing the underlying URL to end users.

|  |  |  |
| --- | --- | --- |
| **Bolt AI Feature** | **Source Type** | **Citation Behavior** |
| **Bolt Agents via Messenger Channel** | -URL  -Website | Not displayed by default.    You must enable "Display Knowledge Sources to User" in Bolt Agent Settings. |
| **Bolt Discovery** | -URL  -Website  -File Upload | Displayed by default. Hide a specific source from Bolt Discovery citations by disabling **Show File in Citations?** on that source. |

---

# Next Steps + Additional Resources

## Getting Started with Knowledge Hub

Understand what the Knowledge Hub is, how Bolt AI uses it, and the key steps to set up your knowledge base in the [Getting Started with Knowledge Hub help article](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub).

## Editing + Managing Knowledge Hub Sources

Learn how to organize your Knowledge Hub with folders and categories, filter and sort sources, perform bulk actions, and keep everything accurate with editing and relearning tools in the [Managing Knowledge Hub Sources help article](https://help.element451.com/en/articles/12277392-managing-knowledge-hub-sources).

## Advanced Knowledge Hub Strategy + Governance

Explore best practices for curating clear, concise, and up-to-date knowledge, setting up governance, and using Insights Dashboards and spot-checks in the [Advanced Knowledge Hub Strategy & Governance help article](https://help.element451.com/en/articles/10416357-advanced-knowledge-hub-strategy-governance).

## Frequently Asked Questions

Our Knowledge Hub frequently asked questions can be found in our [Bolt AI: Frequently Asked Questions](https://help.element451.com/en/articles/10540370-bolt-ai-frequently-asked-questions) help article.

---