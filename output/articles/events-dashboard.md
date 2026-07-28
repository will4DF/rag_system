---
title: Events Dashboard
url: https://help.element451.com/en/articles/6792609-events-dashboard
collection: Insights
---

Introduction and Overview of the Events Dashboard

# Overview

The Events dashboard analyzes the performance of events created in Element451. Explore performance metrics by event name, event type, and a variety of student dimensions.

## Accessing the Dashboard

The Events dashboard can be found via the Insights sub-menu. The Insights module can be accessed from the Data + Automations dropdown in the top navigation.

---

# **Dashboard Features**

The Events dashboard displays year-over-year comparisons, attendance status counts, and event logs.

Data can be viewed by overall performance, specific time frames, and/or within a subset of events.

***Global Controls***

* Event Type: Filter by one or more event types.
* Event Name: Filter by one or more event names.
* Event Series: Filter by one event series.
* Event Categories: Filter by one event category.
* Segments: Filter by one calculated segment.
* Student Term: Filter by one or more active student terms.
* Student Major: Filter by one or more active student majors.
* Student Type: Filter by one or more active student types.

---

# **Tabs**

Data on the Events dashboard is organized by registrations—to evaluate upcoming events—and performance—to analyze past events.

## Registrations Tab

### Unique Controls

* Event Registration | Registration To and From Dates: A date range filter.
* Registration Log | Dimension: Select a student dimension to group by.
* Registrations Year-Over-Year | Group By: Select a time dimension to group by.
* Registrations Year-Over-Year | Years Ago (Offset Year): A number representing the number of years in the past to compare current year counts with.
* Registrations Year-Over-Year | Registration Dates Between: Date range filter.

### Visualizations

* *Event Registrations*

  + Key performance indicator on the total counts of registrations during the selected time period.
  + Top 5 insight displaying the top event names by registration count during the selected time period.
  + Registration counts over time during the selected time period.
  + Registration counts over time by event type during the selected time period.
  + Median days between a student registering for an event and the event date during the selected time period. The vertical line at zero represents the event date. Negative days means the students registered before the event took place. Positive days means the student registered, or a staff member registered the student, after the event took place.

* *Registration Log*

  + Table of registration counts by event name and event date during the selected time period.
  + Table of registration counts by event name and selected student dimension during the selected time period.

* *Registrations Year-Over-Year*

  + Table of registration counts and percent differences by selected period for the current year, previous year, and selected offset year. The percent differences is between the current year and either the previous year or the selected offset year. A negative percent indicates the current year's registration count is less than either the previous year or the selected offset year.
  + Registration counts over time by the current year, previous year, and selected offset year.

## Performance Tab

### Unique Controls

* Event To and From Dates, located next to Event Performance: Sets the date range filter for the dashboard.
* Group By, located next to Event Performance Year Over Year: Select a time dimension to group the attendance counts and percent differences.
* Years Ago (Offset Year), located next to Event Performance Year Over Year: Select a number representing the number of years back you would like to compare this year's counts with.
* Event Dates Between, located next to Event Performance Year Over Year: Select a date range filter for the Year Over Year visualizations.

### Visualizations

* *Event Performance*

  + Key performance indicator on the total attendance count during the selected time period.
  + Top 5 insight displaying the event names with the highest no-show counts during the selected time period. No-shows are the number of students that do not have the status "Attended" or "Cancelled" in your Element451 instance.
  + Attendance status by event date during the selected time period.
  + Key performance indicator on the overall attendance rate during the selected time period. This calculation takes the total attendance of the events during the selected time period over the total number of registrations of the events during the selected time period.
  + Bottom 5 insight displaying the event names with the lowest attendance rates during the selected time period.
  + Event performance by event type during the selected time period. This efficiency chart takes the events that happened during the selected time period and calculates the overall percentage of attended, canceled, and no-show and displays by the event type.

* *Event Performance Table*

  + Table of registration, attended, canceled, and no-show counts along with attendance rates by event name and event date for the selected time period.

* *Event Performance Year Over Year*

  + Table of attendance counts and percent differences by selected period for the current year, previous year, and selected offset year. The percent differences is between the current year and either the previous year or the selected offset year. A negative percent indicates the current year's attendance count is less than either the previous year or the selected offset year.
  + Attendance counts over time by the current year, previous year, and selected offset year.

## Performance Explorer

### Unique Controls

* Funnel Stage Explorer of Attendees | Funnel Stage: Select a funnel stage.
* Dimension Explorer | Dimension: Select a student dimension to group by.
* Dimension Explorer | Funnel Stage 1-5: Select a preferred funnel stage order

### Visualizations

* *Funnel Stage Explorer of Attendees*

  + Map of attendees' location for the selected funnel stage. This visual can drill down into state, county, and zip code.
  + Top 10 bar chart of attendee counts by event name or event type for the selected funnel stage.
  + Pie chart of attendee counts by event name for selected funnel stage.
* *Dimension Explorer*

  + Table of attendance counts and funnel stage counts by event name and selected student dimension.

---

# Metric Definitions

|  |  |
| --- | --- |
| **Metric** | **Definition** |
| Attended | A student is marked as attended for an event in your Element451 instance. |
| Attendance Rate | The number of students attended over the total number of registrations for the event. |
| Cancelled | A student is marked as cancelled for an event in your Element451 instance. |
| No-Show | If a student is not marked as attended or cancelled for an event that has taken place, they are considered a no-show. |
| Registered | A student who has registered for an event. |

---

# **Troubleshooting & FAQ**

* ### Why is there no data?

  There are a variety of reasons an Insights report is blank. Try the following quick fixes:  
  ​

  + **Reset the report.** Visualizations may be filtering the report. Check the date controls. If the date is too far in the past, it may pre-date your activity in Element451. If the date is too far in the future, reports on the performance page will not display metrics since the event has not yet taken place.
  + **Check what fields are being used**. For example, if your institution is not marking students who attended or canceled events, the performance dashboard will not display counts.
  + If data is still missing, there may be issues with your data in Element. Check out [this guide](https://help.element451.com/en/articles/4404458-a-guide-for-data-clean-up) for data cleanup.
* ### **How can I pull a list of students that are being counted toward the visualizations and tables?**

  You can create a segment in your instance and utilize the Events (All Properties) filter to identify your list. If you want to filter the list with a student dimension like term, major, or student type, use the "Active" term, major, or student type fields. Active fields use the most recently collected term, major, and student type found on the student profile.
* ### **How often does the Event dashboard update?**

  The Event dashboard currently refreshes hourly. If you make any updates to the event and its attendance, you will see those changes at the top of the hour.

---