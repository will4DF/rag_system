---
title: Getting Started with Integrations
url: https://help.element451.com/en/articles/9791528-getting-started-with-integrations
collection: Integrations
---

Explore the different platforms that integrate with Element451.

# Overview

Element451 offers a variety of ways to connect with the other systems on your campus, from out-of-the-box native integrations to fully custom API builds. This article is your launching point: explore our integration offerings, see which platforms are covered, and learn how to build your own connection.

When it comes to connecting Element451 with other systems, the answer is almost always yes; what varies is the amount of setup. Native and managed integrations offer the fastest, most seamless connections to the systems we support directly. For everything else, flat file and API integrations can exchange data with virtually any system, with more custom setup involved. Integration platforms like Zapier and Make sit in between, offering no-code automation without building a direct connection.

🚀 **Pro tip:** Planning an integration? Start with our [Pre-Integration Readiness Checklist](https://integrations.element451.com/pre-integration-readiness-checklist-249) to make sure your team and data are ready before you build.

---

# Integration Types

Element451 offers four types of integrations. Understanding the differences helps you determine how your systems connect and what level of support or setup you’ll need.

## Native Integrations

Out-of-the-box integrations designed for quick, self-service setup. Native integrations power the **[Courses](https://help.element451.com/en/collections/13480296-courses)** feature in Element451, connecting to popular systems via API to sync course and enrollment-related data.

* **Learning Management Systems (LMS):**

  + [Canvas](https://help.element451.com/en/articles/11124554-courses-native-integration-canvas-lms)
  + [D2L (Brightspace)](https://help.element451.com/en/articles/11116105-courses-native-integration-d2l-brightspace-lms)
  + [Blackboard](https://help.element451.com/en/articles/11199263-courses-native-integration-blackboard-learn-lms)
* **Student Information Systems (SIS):**

  + [Ethos for Banner + Colleague](https://help.element451.com/en/articles/11586099-courses-integration-ethos-for-banner-colleague-beta)
* **Customer Relationship Managers (CRM):**

  + [Salesforce](https://help.element451.com/en/articles/12633650-native-salesforce-integration-coming-soon) (Beta)

## Managed Integrations

Full-service integrations between Element451 and an external system, built via API or flat file. Managed integrations are tailored to your specific data needs, often involve syncing with your Student Information System (SIS), and require coordination between your institution and Element451, plus setup and maintenance fees as outlined in your contract.

* Student Information Systems (SIS):

  + [Ellucian Colleague](https://help.element451.com/en/articles/12294737-managed-integration-ellucian-colleague)
  + [Ellucian Banner](https://help.element451.com/en/articles/12305739-managed-integration-ellucian-banner)
  + [PowerCampus](https://integrations.element451.com/powercampus-205)
  + [Populi](https://integrations.element451.com/populi-203)
  + [Anthology](https://integrations.element451.com/anthology-204)

##

## Flat-file Integration Templates

Ready-made templates designed to facilitate batch imports and exports between Element451 and an external system. Built to the third party's file specifications (for platforms such as Common App, Apply Texas, Scoir, and Parchment), templates can be quickly added to your Import + Export tasks so you don't have to build the mapping from scratch.

See the [Integrations by Platform](#h_1a2b3c4d5f) table below for the platforms with templates available.

## REST API

**Best for institutions with in-house technical resources.** Element451 offers a full, public REST API for real-time, system-to-system integration. External services can read and write most data in Element451, especially contact data, which makes it possible to build almost any custom integration: pushing inbound leads into your CRM, syncing records with your SIS, or connecting a campus system without a native integration. API integrations require technical resources to build and maintain, either on your team or through an Element451 services project.

[Explore More: API Documentation](https://integrations.element451.com/)

---

# Integrations by Platform

Explore the platforms currently supported by an Element451 integration product or service. Don't see your platform? Ask your account manager, or build your own integration using the tools below.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Platform** | **Flat-file Template** | **Managed Flat File** | **Managed API** | **Native** |
| Anthology Blackboard Learn |  |  |  | ✅ |
| Anthology Blackboard Ultra |  |  |  | ✅ |
| Anthology Student |  |  | ✅ |  |
| Apply Idaho | ✅ |  |  |  |
| Apply Texas | ✅ |  |  |  |
| Brightspace D2L |  |  |  | ✅ |
| CFNC |  |  | ✅ |  |
| Common App | ✅ | ✅ |  |  |
| Common Black College Application | ✅ |  |  |  |
| EAB Enroll360 | ✅ |  |  |  |
| Encoura | ✅ |  |  |  |
| Ellucian Banner |  |  | ✅ | ✅ |
| Ellucian Colleague |  |  | ✅ | ✅ |
| Instructure Canvas |  |  |  | ✅ |
| Parchment | ✅ |  |  |  |
| Populi Admit |  |  | ✅ |  |
| Salesforce |  |  |  | ✅ |
| Scoir | ✅ |  |  |  |
| Scribbles | ✅ |  |  |  |
| Workday Student Management |  |  | ✅ |  |
| ZeeMee | ✅ |  |  |  |

---

# Build Your Own: Integration Tools + Platforms

If your platform isn't covered by one of the offerings above, these tools let you build and monitor your own connection.

## Flat File Integrations

Flat file integrations move data between Element451 and your other systems by exchanging .csv files, typically delivered via SFTP. On a schedule you define, Element451 can ingest .csv files generated by another system (such as your SIS) and create .csv files for other systems to pick up, keeping both systems in sync without a direct connection.

Because you control the file contents, field mappings, and schedule, flat file integrations are a flexible way to connect systems that don't have a native or managed integration. You can build your own flat file integration using the **Imports + Exports** module.

[Explore More: Getting Started with Imports](https://help.element451.com/en/articles/9000459-getting-started-with-imports)

[Explore More: Getting Started with Exports](https://help.element451.com/en/articles/9006515-getting-started-with-exports)

## Zapier

Using the Element451 Zapier App, you have the option of creating your own integration. Creating a connection to your instance, setting up an integration, and running your “zap” (the process you created) is simple. This does require a Zapier feature token from Element451 to connect to your instance.

[Explore More: Zapier](https://help.element451.com/en/articles/6350700-integrate-your-tools-with-zapier)

## Make

Using the Element451 Make App, you have the option of creating your own integration with a variety of software services. Creating a connection to your instance, setting up an integration, and running your “scenario” (the process you created) is simple. This does require a feature token from Element451 to connect to your instance.

[Explore More: Make](https://integrations.element451.com/integration-options-76#_luOB-tcX)

## Webhooks

Webhooks allow Element451 to communicate with other systems, enabling efficient data exchange and, most importantly, event-driven interactions when combined with rules.

[Explore More: Webhooks](https://help.element451.com/en/articles/7960898-webhooks)

## Integration Log

The Integration Log empowers partners by providing transparent, detailed insights into their integration syncs. This feature helps to quickly diagnose and resolve integration issues, ensuring smoother and more efficient data integration processes.

[Explore More: Integration Log](https://help.element451.com/en/articles/9455171-integration-log-monitoring-troubleshooting-integrations)

#

---

# Plugins

## WordPress

### Bolt Discovery + Messenger Plugin

The **Element451 Plugin for WordPress** allows you to effortlessly add **Bolt** **Discovery** (AI-powered search) and **Messenger** (live chat) to your WordPress site.

* Easily embed Bolt Discovery anywhere on your site using a block or shortcode.
* Automatically enable the Messenger widget on all site pages, with visibility controlled in Element451.

[Explore More: Element451 Plugin for WordPress](https://help.element451.com/en/articles/10423713-element451-integration-plugin-for-wordpress)

### Event Plugin

Powered by Spark451, the **Element451 Event Plugin for WordPress** connects your CRM with your WordPress site, making event management easier than ever.

* Display events directly from your CRM with no coding required.
* Real-time sync ensures your site always shows the most up-to-date event information.
* Highlight featured events to draw attention to the most important activities.

[Explore More: Events Plugin for WordPress](https://help.element451.com/en/articles/8390940-element451-event-plug-in-for-wordpress-by-spark451)

## Zoom for Events

The Element451 + Zoom integration makes it easy to host your events in Zoom and to automatically take attendance for the students who log into the Zoom-hosted event.

[Explore More: Zoom Integration for Events](https://help.element451.com/en/articles/5108060-zoom-integration-getting-started)

##

###

##

---