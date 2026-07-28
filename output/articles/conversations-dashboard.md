---
title: Conversations Dashboard
url: https://help.element451.com/en/articles/6909340-conversations-dashboard
collection: Insights
---

Learn how to use the Conversations Dashboard in Insights to analyze and refine your Conversation metrics effectively.

# Overview

The Conversations dashboard analyzes the performance of all Conversations metrics. Explore performance metrics by date, segment, and various student dimensions.

## Accessing the Dashboard

The Conversations dashboard can be found via the Insights sub-menu. The Insights module can be accessed from the Data + Automations dropdown in the top navigation.

---

# **Dashboard Features**

The Conversations dashboard displays period-over-period comparisons, monthly changes in conversation performance rates, and a wide variety of performance measurements.

## **Global Controls**

The Conversations dashboard can be filtered and controlled in several ways. Find the global controls at the top of each tab. These global controls affect each tab. Filters applied on one tab will carry over to the others.

[![](https://downloads.intercomcdn.com/i/o/655841452/5b3df72fee39ad214888166b/image.png?expires=1784333700&signature=d13669bdcc293e0db2900d08d7572bf7b361d1b3d4d9a8bd00ad7d6b0abfd9a8&req=ciUiHs1%2FmYRdFb4f3HP0gJsAmvounWgZwy31YeYj14ZwrjzMWjHfGrohY94P%0AmSDFbA0bq800tIVJvg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/655841452/5b3df72fee39ad214888166b/image.png?expires=1784333700&signature=d13669bdcc293e0db2900d08d7572bf7b361d1b3d4d9a8bd00ad7d6b0abfd9a8&req=ciUiHs1%2FmYRdFb4f3HP0gJsAmvounWgZwy31YeYj14ZwrjzMWjHfGrohY94P%0AmSDFbA0bq800tIVJvg%3D%3D%0A)

Global controls feature filters for **segment, channel, major, funnel stage, identification status, student type, territory,** and **message origin**. Select one or many from most control categories and one segment at a time. You can also now filter your data based on whether or not **Bolt Agents** participatedin the conversation. If you toggle **Bolt Agent Participated** to "Yes" in the Overview tab, you will see ALL staff actions related to conversations where a Bolt Agent participated.

## **Segment Filters**

The Conversations report can only be filtered by certain dimensions by default. The segment filter is a great way to filter the report by dimensions that matter to you. Create a segment in the People module, and set it as a calculated segment.

Please allow 24 hours for new calculated segments to appear and filter correctly in Insights.

More on using [segments and Insights](https://help.element451.com/en/articles/6798155-using-segments-in-insights) together.

---

# **Tabs**

Data on the Conversations dashboard is organized by date as well as various dimensions selected in the controls menu.

## Overview Tab

### Visualizations

* *Highlights*

  + Period-over-period performance of conversations.
  + Filtered totals and changes metric rates for conversations opened, conversations closed, messages sent, messages received, and the average number of messages per conversation.
  + Page URLs for where conversations are originating.

* *Performance over time*

  + Weekly average response time by institutional staff to incoming messages.
  + Hourly breakdown of when conversations were initially opened.
* *Channels*

  + Overall distribution of conversations based on channel.
  + Breakdown of messages by character length according to channel.

* *Inbound/Outbound and Type*

  + The breakdown of messages based on whether they were initiated internally (outbound) or externally (inbound).
  + Conversations broken down by student type.

* *Phone Call Activity Over Time*

  + The breakdown of phone calls made during the selected time frame.
  + The average phone call duration (in seconds) during that time.

## Dimensions Table Tab

### Unique Controls

* Dimension selection: choose whether you want to view metrics by territory, funnel stage, citizenship status, state, gender, major, or student type.

### Visualizations

* *Table*

  + Breakdown of all available conversation metrics based on selected dimension.

## Bolt Agents Tab

### Unique Controls

* Dimension selection: choose whether you want to view metrics by territory, funnel stage, citizenship status, state, gender, major, student type, or a particular Knowledge Hub article. Select the Bolt Agent you would like to view by name or type.

### Visualizations

* *Highlights*

  + Time saved by Bolt Agents.
  + Conversations in which Bolt Agents participated.
  + Conversations handed off from Bolt Agents to internal user.
  + Knowledge Hub gap - conversations in which Bolt Agents were unable to answer questions.
  + Average messages per Bolt Agent conversation.
  + Page URLs for where conversations are originating.
* *Conclusion*

  + Are Bolt Agent conversations ended with Bolt Agents finishing the conversation, handing off to an internal user, or by being stopped by the contact?
* *Bolt Agent Activity*

  + Messages sent by Bolt Agent by name or type.
  + Usage of each Bolt Agent (by conversations that include them).
  + Average sentiment by Bolt Agent by name or type.
  + Number of references to specific Knowledge Hub articles.
  + Links to conversations where there was a Knowledge Hub gap.
* *Geography*

  + Bolt Agent conversations by location in map view.
* *Bolt Agents by dimensions*

  + A breakdown of the Knowledge Hub gap, average sentiment rating, and total conversations by various dimensions and over time.

---

# **Metric Glossary**

|  |  |
| --- | --- |
| **Metric** | **Definition** |
| Conversations | Total conversations that have taken place within selected controls. |
| Conversations closed | Conversations that have been officially closed within the conversations module. |
| Messages sent | The number of messages in all conversations from an internal user. |
| Messages received | The number of messages in all conversations from an external user. |
| Average messages per conversation | Average number of all messages (internal and external) sent in conversations. |
| Average response time | Average minutes to response. (Excluding 30 minute delays to eliminate outlier out of office data.) |
| Average duration | The number of takes it takes for a conversation to go from opened to closed. |
| Average internal response time | Average time between an incoming message and an internal response for any response being sent from an internal user. (Maximum session of 30 minutes) |
| Minutes worked by Bolt Agents | The actual amount of time it has taken Bolt Agents to respond to messages. |
| Human minutes saved | Time saved by utilizing Bolt Agents, multiplying your average internal response time by the number of Bolt Agent messages sent. |
| Average sentiment | Average sentiment (negative, neutral, positive) of all external users responding to Bolt Agents. |
| Phone Calls | The number of phone calls placed during a given time frame. |
| Average Duration Time | The average length of phone calls in seconds during the given time frame. |
| References | Number of times a particular Knowledge Hub article is used during a conversation with Bolt Agents. |
| After Hours Conversations | Conversations beginning before 8 a.m. or after 5 p.m. local time. |

---

# **Troubleshooting & FAQ**

* ## Why is there no data?

  There are a variety of reasons an Insights report is blank. Try the following quick fixes:  
  ​

  + **Reset the report.** Visualizations may be filtering the report. Check the date controls. If the date is too far in the past, it may predate your activity in Element451.
  + **Check** what fields are being used.
  + If data is still missing, there may be issues with your data in Element. Check out [this guide](https://help.element451.com/en/articles/4404458-a-guide-for-data-clean-up) for **data cleanup.**
* ### **How often does the Conversations dashboard update?**

  The Conversations dashboard currently refreshes once a day at 12:00 am Eastern.

---