---
title: Advanced Knowledge Hub Strategy + Governance
url: https://help.element451.com/en/articles/10416357-advanced-knowledge-hub-strategy-governance
collection: Bolt AI
---

# Overview

Maintaining a healthy Knowledge Hub goes beyond adding sources. In this article, you’ll learn best practices for curation, setting up governance (including ownership and cadence), structuring access, and running a repeatable review/audit loop using Insights Dashboards and spot checks.

---

# Why Governance Matters

Your Knowledge Hub serves as the foundation for Bolt AI. It’s more than a repository of information—it powers the **semantic understanding** behind these tools.

Semantic search enables Bolt AI to analyze and retrieve the most relevant knowledge by understanding the meaning behind users’ questions (not just the keywords). This advanced capability makes the accuracy, clarity, and organization of your Knowledge Hub critical for the successful deployment of Bolt Agents and Bolt Discovery.

Without proper curation and regular maintenance:

* Your agents may deliver incomplete, outdated, or incorrect answers.
* Gaps in knowledge can lead to uncertain responses or unanswered queries.
* Students may lose trust in where they look for information.

By following these best practices, you can ensure your Knowledge Hub is a powerful, reliable resource for both your students and your team.

---

# Best Practices for Curating

## Add Sources Strategically

* **Use a mix of source types**: Text, URLs, website sitemaps, file uploads, and custom answers all help cover different knowledge needs.

  + **Website/URL Sources**: You can add your website pages in two ways—by entering individual URLs for specific pages (URL source) or by using your sitemap (website source). With the sitemap option, you can choose to ingest all of your pages or select from the indexed list.

    - 🚨 **Important:** While ingesting your entire site is possible, it’s important to review the content first. Any outdated, inconsistent, or irrelevant pages you include may surface in responses to students, so be sure the content you add is accurate and current.
  + **Custom Answers:** Because these are prioritized over other source types, custom answers are great for strategic, high-priority Q&A pairs. Add crucial or frequently asked questions here to ensure they’re top of mind for your AI tools.
  + **Text/Document Sources:** Use these for longer or more detailed knowledge, but remember to break up large blocks of text for easier human review.

## Organize with Folders + Categories

* **Folders**: Create custom [folders](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub) (e.g., Admissions, Academics) for quick access and management.

  + Use the **bulk action feature** to move multiple sources into a folder at once for easier organization.
* **Categories**: Tag sources by topic or functional area. Categories help you filter sources and control which agents have access to specific knowledge. To scope an agent's knowledge access, edit its [settings](https://help.element451.com/en/articles/8993375-bolt-agent-settings).

  + **Example:** For a financial aid agent, categorize all financial aid-related sources. By assigning that agent access only to the “Financial Aid” category, you ensure it only answers questions related to that topic.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1723073616/0c8e17848451953507b01b57cf8b/KB-2B--2BCategories.png?expires=1784333700&signature=2eecc6ae82d7aa5e402329addec2d1f5b5bdaff4ebb0cdff9a72ef3a5a193721&req=dSclFcl5nodeX%2FMW1HO4zbNxyRzbYf70s3z1ULNHqQw0p5CkdFM9JM%2FDsuDm%0AquzM%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1723073616/0c8e17848451953507b01b57cf8b/KB-2B--2BCategories.png?expires=1784333700&signature=2eecc6ae82d7aa5e402329addec2d1f5b5bdaff4ebb0cdff9a72ef3a5a193721&req=dSclFcl5nodeX%2FMW1HO4zbNxyRzbYf70s3z1ULNHqQw0p5CkdFM9JM%2FDsuDm%0AquzM%0A)

## Curate for Clarity + Accuracy (3 C's)

When adding knowledge, always prioritize these principles:

* **Curated:** Add sources that are relevant, accurate, and up-to-date.
* **Concise:** Use clear, concise language. Avoid unnecessary details—your agents and Discovery will handle making it conversational.
* **Clear:** Ensure knowledge is well-written, avoids ambiguity, and does not include conflicting information.

By following the 3 C’s, you’ll set your AI tools up for success, ensuring they provide precise and reliable answers to users.

## Use Specific, Direct Information

When curating your Knowledge Hub, explicitly stating key facts, data, or answers ensures that Bolt Agents provide the most accurate and relevant responses. Agents perform best with explicit facts and data. For example:

* Instead of writing: “We offer graduate programs,” use: “We offer 10 graduate programs across business, education, and healthcare fields.”
* Instead of: “Our deadline is soon,” use: “Our application deadline for Fall 2024 is January 15, 2024.”

**Why this matters:** Specific information like the above ensures that Bolt Agents don’t rely on general statements or infer details from related sources. This is especially important for numeric or critical facts (e.g., deadlines, program counts, or event dates).

## Enable Daily Sync + New Page Detection for Websites & URLs

Daily Sync allows Bolt AI to automatically detect and index updates and new pages from your linked sources, keeping your Knowledge Hub current without manual effort.

---

# Best Practices for Governance

## Assign a Point Person/Team to Conduct Audits

Designate one or more team members to be responsible for maintaining your Knowledge Hub. Define clear roles and responsibilities, and create a plan for how and when audits will take place (e.g., monthly, quarterly). Regular audits are vital to ensuring your Knowledge Hub stays accurate and up-to-date.

* Establish a schedule for when audits should be conducted.
* Divide responsibilities among multiple team members.
* Establish processes for reviewing, updating, and retiring outdated sources.

If multiple team members are responsible for maintaining the Knowledge Hub:

* Assign clear roles for reviewing specific categories, source types, or tools (e.g., Bolt Agents vs. Bolt Discovery).
* Use shared logs or project management tools to track what’s been audited or updated.

For ideas on strategies to facilitate your audit, continue reading below on Leveraging the Insights Dashboards and Spotchecking Conversations.

## Test Bolt AI Tools

Start by testing your Bolt Agents and Discovery tools to ensure they’re performing as expected:

* Open an agent's configuration page and click Test Agent to simulate representative questions safely.
* Review Response Details to confirm which skills were evaluated, which skill matched, and which actions would execute.
* After the Test Agent results are correct, run a controlled live end-to-end test. Test Bolt Discovery separately with queries related to content in your Knowledge Hub.

[Learn More: Testing Bolt Agents](https://help.element451.com/en/articles/8993362-testing-bolt-agents)

## Leverage the Insights Dashboards

The Insights Dashboards in Element451 provide comprehensive metrics for understanding how your Knowledge Hub is performing. Use these tools to identify gaps and prioritize updates:

### Conversations Dashboard (Bolt Agents)

* Go to Data + Automations > Insights > Conversations and select the Bolt Agents tab at the top to review performance metrics.  
  ​
* Key data points include:

  + **Knowledge Hub Gap Card:** Displays the number of times a Bolt Agent encountered an uncertain response due to missing knowledge.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340448814/4ce3dcdce24eb1b11ea1c6714066/KB%2B-%2BInsights%2B-%2BKB%2BGap%2BCard.png?expires=1784333700&signature=b0ce9ce8e38dff83b00ea5abd43c515bd4ea62d0b5d8045e29a4249e338a4252&req=dSMjFs16lYleXfMW1HO4zRlutiCvubreykHhSBKLoUUevqUrtPGRe6sKUulD%0AXQLe%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340448814/4ce3dcdce24eb1b11ea1c6714066/KB%2B-%2BInsights%2B-%2BKB%2BGap%2BCard.png?expires=1784333700&signature=b0ce9ce8e38dff83b00ea5abd43c515bd4ea62d0b5d8045e29a4249e338a4252&req=dSMjFs16lYleXfMW1HO4zRlutiCvubreykHhSBKLoUUevqUrtPGRe6sKUulD%0AXQLe%0A)
  + **Knowledge Hub Gap Log:** A detailed list of those interactions, each with a link to the specific conversation. Use this to review gaps and update your Knowledge Hub accordingly.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340449649/191b398f281818c5d064daeb6066/KB%2B-%2BInsights%2B-%2BKB%2BGap%2BLog.png?expires=1784333700&signature=64bbc256872bbb34569c92f4119b339d5c732d49ae8c96d57bc27b1354442515&req=dSMjFs16lIdbUPMW1HO4zZ0RcXYwOfaOgYQ1aG5IZJOQabrXt%2FC26uTuOQrw%0Aszjb%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340449649/191b398f281818c5d064daeb6066/KB%2B-%2BInsights%2B-%2BKB%2BGap%2BLog.png?expires=1784333700&signature=64bbc256872bbb34569c92f4119b339d5c732d49ae8c96d57bc27b1354442515&req=dSMjFs16lIdbUPMW1HO4zZ0RcXYwOfaOgYQ1aG5IZJOQabrXt%2FC26uTuOQrw%0Aszjb%0A)
  + **Knowledge Hub Article References:** Shows which articles are being used the most, helping you prioritize them for review and updates.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340450159/a1051179e81d301885bb4b1204f6/KB%2B-%2BInsights%2B-%2BKB%2BArticle%2BReferences.png?expires=1784333700&signature=4e29da9ac5d6c21969432cf145e284083d4b9bb6e6df2b1f92bb1410594ca3db&req=dSMjFs17nYBaUPMW1HO4zb3QRhqndjkDgMksMzUW0ubzx%2Fpzhainl7yrsvc0%0A6QDu%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340450159/a1051179e81d301885bb4b1204f6/KB%2B-%2BInsights%2B-%2BKB%2BArticle%2BReferences.png?expires=1784333700&signature=4e29da9ac5d6c21969432cf145e284083d4b9bb6e6df2b1f92bb1410594ca3db&req=dSMjFs17nYBaUPMW1HO4zb3QRhqndjkDgMksMzUW0ubzx%2Fpzhainl7yrsvc0%0A6QDu%0A)
  + **Gap Responses by Funnel Stage:** Look at a visualization to understand where students are most likely to encounter gaps in knowledge.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340450503/c6f19a544151e8106071f96c6cb8/KB%2B-%2BInsights%2B-%2BBy%2BFUnnel.png?expires=1784333700&signature=e528ff7200b68188c65884d7b96f06cee357eb2584eb566042ccb5882845796b&req=dSMjFs17nYRfWvMW1HO4zeVbCn6Y6DqCd0gSXec7zvNgWcEXBxBXE6aa0AJ7%0AGBnc%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340450503/c6f19a544151e8106071f96c6cb8/KB%2B-%2BInsights%2B-%2BBy%2BFUnnel.png?expires=1784333700&signature=e528ff7200b68188c65884d7b96f06cee357eb2584eb566042ccb5882845796b&req=dSMjFs17nYRfWvMW1HO4zeVbCn6Y6DqCd0gSXec7zvNgWcEXBxBXE6aa0AJ7%0AGBnc%0A)

[Learn More: Convos Dashboard](https://help.element451.com/en/articles/6909340-conversations-dashboard)

### Bolt Discovery Dashboard

* Go to Data + Automations > Insights > Discovery and select the Overview tab at the top to review performance metrics.  
  ​
* Key metrics include:

  + **Knowledge Hub Gap Card:** Similar to the Conversations/Bolt Agents dashboard, this shows gaps in Discovery results.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340470947/45f7b6a5ac7a5d3fa52681fe9a5d/Discovery+-+Insights+-+KB+Gap.png?expires=1784333700&signature=449972c9aa3b25a99be71277ca175ae1f1be1131673037ea8f9955f0c9cdd714&req=dSMjFs15nYhbXvMW1HO4zfutL1hv3p85nJwpR2RFqUpcw2hTQK%2BMWPphd%2Fhf%0Ann9t%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340470947/45f7b6a5ac7a5d3fa52681fe9a5d/Discovery+-+Insights+-+KB+Gap.png?expires=1784333700&signature=449972c9aa3b25a99be71277ca175ae1f1be1131673037ea8f9955f0c9cdd714&req=dSMjFs15nYhbXvMW1HO4zfutL1hv3p85nJwpR2RFqUpcw2hTQK%2BMWPphd%2Fhf%0Ann9t%0A)
  + **Knowledge Hub Gap Keywords:** Review common search terms that led to unanswered queries.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340471186/c11c5d46987adc6deb07f9929373/Discovery+-+Insights+-+Keyword+Gap.png?expires=1784333700&signature=b98add61f423239675aad9eff9bd42da738e165143dfa0a9897c958456127101&req=dSMjFs15nIBXX%2FMW1HO4zYnGAY%2F0O3M5sy%2BuDQIYkbR0zp1hss1%2Ft4tiTN7a%0AYC5o%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340471186/c11c5d46987adc6deb07f9929373/Discovery+-+Insights+-+Keyword+Gap.png?expires=1784333700&signature=b98add61f423239675aad9eff9bd42da738e165143dfa0a9897c958456127101&req=dSMjFs15nIBXX%2FMW1HO4zYnGAY%2F0O3M5sy%2BuDQIYkbR0zp1hss1%2Ft4tiTN7a%0AYC5o%0A)
  + **Top Knowledge Hub Articles Referenced:** Identify your most-used articles to ensure their content is accurate and current.
  + **Knowledge Hub Metrics by Topic or Date:** Review trends to see which areas of knowledge are being referenced most frequently or need improvement.  
    ​
* Use the **Query Log** tab to access a complete list of all queries made and the responses provided. This allows you to evaluate the accuracy of answers and pinpoint areas for improvement. Each log entry also includes a link to the corresponding thread.

  + [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340482644/c5ebe352fcf94c4f0ad666562dea/Pro+Tip.png?expires=1784333700&signature=cb3e51d3fdbed88e2ee7652fb3252dd4c825a88e584b3cfee90d0239289f7097&req=dSMjFs12n4dbXfMW1HO4zRRXyDadK3%2BWYlYLhVC0Z7JKLVXP%2FQCTW%2BUuhWq%2F%0AH59k%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340482644/c5ebe352fcf94c4f0ad666562dea/Pro+Tip.png?expires=1784333700&signature=cb3e51d3fdbed88e2ee7652fb3252dd4c825a88e584b3cfee90d0239289f7097&req=dSMjFs12n4dbXfMW1HO4zRRXyDadK3%2BWYlYLhVC0Z7JKLVXP%2FQCTW%2BUuhWq%2F%0AH59k%0A)

    To quickly identify areas needing attention, use the **Knowledge Hub Gap** control filter and set it to “Yes.” This will generate a focused list of queries where gaps occurred, helping you prioritize updates to your Knowledge Hub efficiently.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340474227/16fb906c388e334fed454cb59007/Discovery+-+Insights+-+Query+Log.png?expires=1784333700&signature=d1040e85e7f4838ce1fe6964480a0ba40cd9fd9383f926fa9f0b5f98b7222054&req=dSMjFs15mYNdXvMW1HO4zVPn3stBvLALTIq2MB3UZ9VtSm%2Fv6i6%2Bogy436aY%0Azi3U%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1340474227/16fb906c388e334fed454cb59007/Discovery+-+Insights+-+Query+Log.png?expires=1784333700&signature=d1040e85e7f4838ce1fe6964480a0ba40cd9fd9383f926fa9f0b5f98b7222054&req=dSMjFs15mYNdXvMW1HO4zVPn3stBvLALTIq2MB3UZ9VtSm%2Fv6i6%2Bogy436aY%0Azi3U%0A)

[Learn More: Discovery Dashboard](https://help.element451.com/en/articles/9740909-bolt-discovery-dashboard)

**Pro Tip:** Use the logs and keyword data to identify common trends. For example, if multiple gaps are related to financial aid queries, prioritize adding more detailed financial aid content.

## Spot-Check Conversations and Threads

To ensure both **Bolt Agents** and **Bolt Discovery** are performing optimally, it’s important to review their interactions with users regularly. Spot-checking conversations and threads helps you verify that responses are accurate, aligned with your institution’s tone, and deliver the desired results.

* **Why it matters:** Insights Dashboards will highlight Knowledge Hub gaps and metrics, but they don’t account for cases where an agent or Discovery gave an answer that might not be accurate or ideal.

### Spot-Checking Bolt Agents

* Navigate to **Engagement** > **Conversations** > **All** **Conversations** and [filter your inbox](https://help.element451.com/en/articles/8507376-conversations-inbox#h_2d28443ba5) by adding the “**Bolt Agent - Participated**” filter to view only those conversations.
* Use the **Advanced Filter Sidesheet** at the bottom to save this filter as a [Custom View](https://intercom.help/element451/en/articles/10223032-custom-conversation-views) for easy access in the future.
* Once filtered, review a sampling of these conversations to ensure the agent provided correct and appropriate answers.

### Spot-Checking Bolt Discovery

To efficiently review and evaluate Bolt Discovery’s performance, use the **Query Log** within the Insights dashboard:

* Navigate to **Data + Automations > Insights > Bolt Discovery** and click on the **Query Log** tab at the top. This provides a detailed list of all user queries and the responses given by Bolt Discovery.
* The Query Log includes powerful filters to help you narrow down the data:

  + **Date:** Review queries within a specific time range.
  + **Source Type, Title, or Category:** Drill down into specific sources to analyze their performance.
  + **Knowledge Hub Gap:** Filter by “Yes” to instantly generate a list of queries where Discovery encountered a knowledge gap. This is a great way to identify areas where additional content is needed or where existing content could be improved.

**Pro Tip:** Set a recurring schedule to review the Query Log weekly or monthly. Focus on queries with knowledge gaps first, as addressing these will have the greatest impact on improving Bolt Discovery’s performance.

### What to Do If You Spot Issues

* If you identify incorrect responses, review the Knowledge Hub sources associated with the query.
* Update, rewrite, or add sources to fill any identified gaps.
* For questions that aren’t answered well, even with proper knowledge, consider creating a **Custom Answer** for a more precise response.

---

# Final Thoughts

A well-maintained Knowledge Hub is essential for empowering your Bolt AI tools to deliver accurate, helpful, and engaging experiences for users. By following these best practices, you can ensure your Knowledge Hub remains a valuable resource and your AI-powered tools perform at their best.

If you’re ready to start curating or auditing your Knowledge Hub, check out our Getting Started with Knowledge Hub and Adding Knowledge Hub Sources articles for detailed instructions!

---

# Additional Knowledge Hub Resources

## Getting Started with Knowledge Hub

Understand what the Knowledge Hub is, how Bolt AI uses it, and the key steps to set up your knowledge base in the [Getting Started with Knowledge Hub help article](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub).

## Adding Knowledge Hub Sources

Get step-by-step instructions for creating new sources, including text, URLs, website sitemaps, file uploads, and custom answers in the [Adding Knowledge Hub Sources help article](https://help.element451.com/en/articles/12276752-adding-knowledge-hub-sources).

## Editing + Managing Knowledge Hub Sources

Learn how to organize your Knowledge Hub with folders and categories, filter and sort sources, perform bulk actions, and keep everything accurate with editing and relearning tools in the [Managing Knowledge Hub Sources help article](https://help.element451.com/en/articles/12277392-managing-knowledge-hub-sources).

## Frequently Asked Questions

Our Knowledge Hub frequently asked questions can be found in our [Bolt AI: Frequently Asked Questions](https://help.element451.com/en/articles/10540370-bolt-ai-frequently-asked-questions) help article.

---