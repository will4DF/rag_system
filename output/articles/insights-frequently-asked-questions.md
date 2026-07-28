---
title: 📌 Insights: Frequently Asked Questions
url: https://help.element451.com/en/articles/10629724-insights-frequently-asked-questions
collection: Insights
---

This article answers commonly asked questions about Insights Dashboards, providing quick solutions and key insights.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1394900017/6282c40f9b95bc2e277390ad590a/Pardon%2Bour%2BProgress.png?expires=1784333700&signature=2ac1740d70605646cb5ad8e7b2454b29f038c3f5be6f3f1d273a675c63149737&req=dSMuEsB%2BnYFeXvMW1HO4zSm%2FRmNvNySyNg%2F1m49y4uU52yJEsaZ2B%2BMXkSve%0AW3nI1XO0Ipk6X%2FPNby8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1394900017/6282c40f9b95bc2e277390ad590a/Pardon%2Bour%2BProgress.png?expires=1784333700&signature=2ac1740d70605646cb5ad8e7b2454b29f038c3f5be6f3f1d273a675c63149737&req=dSMuEsB%2BnYFeXvMW1HO4zSm%2FRmNvNySyNg%2F1m49y4uU52yJEsaZ2B%2BMXkSve%0AW3nI1XO0Ipk6X%2FPNby8%3D%0A)

#

# General

#### Why is no data populating?

There are a variety of reasons an Insights report is blank. Try the following quick fixes:

* **Reset the report.** Visualizations may be filtering the report. Check the date controls. If the date is too far in the past, it may pre-date your activity in Element451.
* **Check** what fields are being used.
* If data is still missing, there may be issues with your data in Element. Check out [this guide](https://help.element451.com/en/articles/4404458-a-guide-for-data-clean-up) for **data cleanup.**

#### How often are dashboards updated?

Each dashboard updates twice daily, once in the AM and once in the PM. The last refresh time/date is listed at the bottom of each tab on the dashboard.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1417423402/9c5cd83d4ae18fd3c0eafb2e3b43/Insights+Refresh+Datae.png?expires=1784333700&signature=2f8e894b7323e269374cd26eeed64dff9fb45801fe491227df418c7e82177eca&req=dSQmEc18noVfW%2FMW1HO4zZ4nzctBq7gUkgmU5pk3XnucHgus3pFSriiiJxbf%0AqjEnlCp4EZy0RzGlKG0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1417423402/9c5cd83d4ae18fd3c0eafb2e3b43/Insights+Refresh+Datae.png?expires=1784333700&signature=2f8e894b7323e269374cd26eeed64dff9fb45801fe491227df418c7e82177eca&req=dSQmEc18noVfW%2FMW1HO4zZ4nzctBq7gUkgmU5pk3XnucHgus3pFSriiiJxbf%0AqjEnlCp4EZy0RzGlKG0%3D%0A)

#### How is my data stored?

Element451 stores analytics data in Snowflake, a data warehouse. Here, data is modeled and sent to Insights.

#### How can I access my institution’s data?

You can access your institution's data in a variety of ways.

* Download raw data using the Export module. [Learn more.](https://help.element451.com/en/articles/9006515-getting-started-with-exports)
* Access all of your analytics data in real time using Snowflake. Download your data as needed, or connect it to your own data platform via API. Want to learn more about Snowflake? Reach out to Customer Success.

---

# Appointments Dashboard

#### How are multiple appointments for the same person counted in Insights? If an appointment is canceled and rescheduled, how will that be counted?

In Insights, each appointment is represented by one row. For instance, if one appointment is scheduled and canceled and then a new appointment is scheduled and attended, you will have two total appointments recorded—one canceled and one attended. This distinction is crucial for users analyzing appointment data.

---