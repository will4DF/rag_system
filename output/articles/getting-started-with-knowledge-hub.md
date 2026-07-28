---
title: Getting Started with Knowledge Hub
url: https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub
collection: Bolt AI
---

Learn how to add/manage sources in public/private repositories for enhanced Bolt AI functionality.

# Overview

## What is the Knowledge Hub?

The Knowledge Hub is your centralized, curated repository that powers Bolt AI — including **Bolt Agents for Students**, **Bolt Staff Agents**, **Bolt Discovery**, and **Bolt Agent Jobs**.

Unlike keyword search, Bolt AI utilizes **semantic understanding** to provide answers based on meaning and intent, so the **clarity, accuracy, and organization** of your Knowledge Hub directly impact the quality of the answers.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722808302/e4556fc9c75548d0c54f1e0b716c/KB.png?expires=1784333700&signature=5c546a2e0c6c9e5ed02ebf910db71a92ef1d2c43f5c40db262145a0a71907be2&req=dSclFMF%2BlYJfW%2FMW1HO4zf42i1QCpsrZ4KsKPJK5fGBhky%2FBqpKP93JFS%2BVx%0A%2FIpB6qkgfZ5ejya4wew%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1722808302/e4556fc9c75548d0c54f1e0b716c/KB.png?expires=1784333700&signature=5c546a2e0c6c9e5ed02ebf910db71a92ef1d2c43f5c40db262145a0a71907be2&req=dSclFMF%2BlYJfW%2FMW1HO4zf42i1QCpsrZ4KsKPJK5fGBhky%2FBqpKP93JFS%2BVx%0A%2FIpB6qkgfZ5ejya4wew%3D%0A)

## Public vs Private

* **Public**: Student-facing tools (e.g., admissions, tuition, programs, policies).
* **Private**: Internal-only knowledge for staff (e.g., procedures, internal contacts, team workflows).

## Bolt Agent Access

* **[Bolt Agents](https://help.element451.com/en/articles/7173429-getting-started-with-bolt-agents-for-students)** [**for** **Students**](https://help.element451.com/en/articles/7173429-getting-started-with-bolt-agents-for-students) access the **public** repository in:

  + **Conversations** when they are managing and answering inbound conversations, and supporting a wide range of inquiries.
  + **Bolt Agent Jobs** when they are drafting content and responding to students working toward a goal completion.
* **[Bolt Agents for Staff](https://help.element451.com/en/articles/7173423-getting-started-with-bolt-agents-for-staff)**

  + **User Support Agent**: Can access **both** **public and** **private** repositories to answer internal questions. The private repository allows for including information specific to the departments/teams using Element451, such as internal policies and processes.
  + **Copywriter Agent**: Can access the **public** repository to draft content/ communications.
  + Bolt Page Builder Agent: Can access the public repository to build branded, ready-to-publish landing Pages.
  + **Campaign Creator Agent**: Can access the **public** repository to create complete drip **[Campaigns](https://help.element451.com/en/articles/8312170-bolt-campaign-creator-agent).**
* **[Bolt Discovery](https://help.element451.com/en/articles/9331910-bolt-discovery-overview)**: Leverages the **public** repository to provide accurate and relevant answers to questions, taking users beyond the conventional website search experience into a new era of interactive information discovery.

## View a table comparison of agent access

|  |  |  |
| --- | --- | --- |
| **Bolt AI Feature** | **Public** | **Private** |
| **Bolt Agents for Students** via Inbound Conversations (Messenger, Email, SMS, WhatsApp) + Bolt Agent Jobs  ​ (Recruiter Agent, Admissions Advisor Agent, Financial Aid Agent, Athletics Agent, Academic Advisor Agent, Campus Life Agent, Peer Advisor Agent, Career Counselor Agent, Lead Gen Agent, Chatbot Agent) ​ ​*\*Bolt Agents for Students access to knowledge can be scoped in their individual settings.* | ✅ | ❌ |
| **Bolt Discovery** | ✅ | ❌ |
| **Copywriter Agent** (Staff) | ✅ | ❌ |
| Bolt Page Builder Agent (Staff) | ✅ | ❌ |
| **Campaign Creator Agent** (Staff) | ✅ | ❌ |
| **User Support Agent** (Staff) | ✅ | ✅ |

---

# Quick Start Checklist

Here are some recommended quick-start items to get your Knowledge Hub up and running quickly.

1. **Plan your categories** (Admissions, Financial Aid, Academics, Housing)
2. **Add your sitemap** as a **Website Source**

   * Enable **Daily Sync** (+ **New Page Detection** if appropriate)
   * You can ingest your entire site, but it's recommended that you review it first. Outdated/conflicting content will surface in answers.
3. Add other **high-priority** **sources**:

   * **Single URLs** (e.g., FAQ, tuition, program pages) that are not added via your sitemap
   * **Custom Answers** for your 10 most frequently asked questions (deadlines, costs, how to apply)
   * **Upload files**
4. **Organize** your new sources with **Folders** + **Categories**
5. **Test by** asking sample questions with **Bolt** **Agents** and **Bolt** **Discovery**
6. **Assign a point person** and set a regular **audit cadence**

## Preparing Your Website(s) for Scraping

To ensure Element451’s website scraper can reliably access and detect updates to your webpages—especially when using the **Daily Sync** feature—please review the following requirements with your web or IT team.

1. **Whitelist the Element451 Website Scraper**  
   Some websites use firewalls, bot protection, or security services (such as Cloudflare, Akamai, or similar tools) that may block automated crawlers.  
   ​  
   To prevent access issues, whitelist the Element451 scraper’s IP address: `54.82.10.251`   
   ​  
   Whitelisting this IP ensures uninterrupted access to your public webpages. Without it, you may encounter a 403 Forbidden error or similar messages (depending on the platform) when previewing a knowledge source.  
   ​
2. **Confirm How Webpage Updates Are Signaled**  
   Element451 detects webpage updates using standard web signals and metadata. To ensure updates are captured correctly, confirm that your site uses at least one of [Element451’s supported methods](https://help.element451.com/en/articles/12276752-adding-knowledge-hub-sources#h_47fea9a044) for indicating content changes.  
   ​  
   If your site does not clearly signal updates, changes may not be detected during scheduled syncs.

---

# Next Steps + Additional Resources

## Adding Knowledge Hub Sources

Get step-by-step instructions for creating new sources, including text, URLs, website sitemaps, file uploads, and custom answers in the [Adding Knowledge Hub Sources help article](https://help.element451.com/en/articles/12276752-adding-knowledge-hub-sources).

## Editing + Managing Knowledge Hub Sources

Learn how to organize your Knowledge Hub with folders and categories, filter and sort sources, perform bulk actions, and keep everything accurate with editing and relearning tools in the [Managing Knowledge Hub Sources help article](https://help.element451.com/en/articles/12277392-managing-knowledge-hub-sources).

## Advanced Knowledge Hub Strategy + Governance

Explore best practices for curating clear, concise, and up-to-date knowledge, setting up governance, and using Insights Dashboards and spot-checks in the [Advanced Knowledge Hub Strategy & Governance help article](https://help.element451.com/en/articles/10416357-advanced-knowledge-hub-strategy-governance).

## Frequently Asked Questions

Our Knowledge Hub frequently asked questions can be found in our [Bolt AI: Frequently Asked Questions](https://help.element451.com/en/articles/10540370-bolt-ai-frequently-asked-questions) help article.

---