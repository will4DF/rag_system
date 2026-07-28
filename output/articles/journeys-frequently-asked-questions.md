---
title: 📌 Journeys: Frequently Asked Questions
url: https://help.element451.com/en/articles/10606462-journeys-frequently-asked-questions
collection: Journeys
---

This article answers commonly asked questions about Journeys, providing quick solutions and key insights.

# General

#### Do students receive notifications when they are added to a journey?

No, students do not receive notifications when they are added to a Journey. However, if this is something you'd like to explore doing, you could do so using a **workflow and an ongoing campaign**. To do this, create a **segment** using Journey filters, then use the **Join Segment** trigger to enroll students in a workflow that sends notifications.

#### How is a Journey different from a Workflow?

Unlike workflows, which are designed to **perform** **actions**, journeys are designed to **track user activity between two points**. A journey visualizes progress, helping you understand where users engage or drop off.

Workflows, on the other hand, are designed to perform actions. Think of Journeys as a tracking tool and Workflows as an action tool. Using Journeys to perform complex actions can be attempted, but it's not the optimal tool for that purpose.

#### What should I consider when deciding between Journeys and Workflows?

Consider your primary goal: if you want to track and visualize user progress through a specific pathway, use Journeys. If you need to perform actions or automate processes based on certain triggers, Workflows are more appropriate. While you can add some actions to Journeys, they were designed as an ancillary feature, not the primary purpose.

#### Is there a way to search for people enrolled in a Journey?

You can use the Segment filter → `Journey (All Properties)` to find which contacts have been enrolled in a specific Journey.

---

# Settings

#### What does the “Past Activities” setting do in Journeys?

The **Past Activities** setting lets you evaluate actions that happened *before* the Journey was activated.

* It applies to **Steps** and **Exit Events**
* It does **not** apply to **Journey Triggers**
* It will **not** enroll users based on past activity

Only users who are already in the Journey will be evaluated against past actions when this setting is toggled on.

**Example:** If you want to catch up students who submitted their application *before* the Journey was created, turning on *Past Activities* allows the system to recognize that the “Submitted Application” step has been completed for those already enrolled. This way, their progress reflects that submission, even though it happened before the Journey started.

---

# Triggers + Enrollment

#### Can a student enter a Journey more than once?

Yes, but only after they have **completed** the Journey. A student can re-enter a Journey only if the **trigger** provides a unique context each time. For example, if a Journey starts when a student submits an application, they can enter again for each new application they submit.

If the trigger does not provide unique context—like submitting the same form—it doesn’t make sense to track it again because the Journey would look exactly the same both times. If you need to trigger an action each time something happens (like sending a confirmation email whenever a form is submitted), consider using Workflows + Rules instead of Journeys. Journeys are designed to track progress, not repeat the same sequence of events.

---

# Steps

#### Can Journey steps be skipped?

No, steps cannot be skipped. Steps must be completed in sequential order. To avoid enrollees from getting "stuck," consider using [Exit Triggers](https://help.element451.com/en/articles/6825003-getting-started-with-journeys#h_ff185bffbd).

#### What's the proper way to set up Journey conditions?

When setting up Journey steps, it's important to use step conditions rather than user segment conditions if you want a step to be completed when a specific action occurs. User segment conditions determine if a user is eligible for a step, while step conditions determine when that step is considered complete.

#### Why might a step be marked complete unexpectedly?

If a step uses user segment conditions instead of step conditions, the step might be marked complete when any qualifying action occurs while the user matches those segment conditions. For users going through a Journey a second time, they may already match the segment conditions, causing steps to be marked complete prematurely.

#### What happens when a Journey is completed?

When all steps in a Journey are completed, the user's status for that Journey is marked as "completed." The completed users should remain in the Journey to help you analyze how many users completed all steps and identify where most users are getting lost in the process. This data is valuable for journey optimization.

---

# Exit Triggers + Completing Journeys

#### How do Exit Triggers work in Journeys, and when should I use them?

Exit Triggers automatically mark a contact as *exited* when certain conditions are met, stopping them from continuing in the Journey. This keeps your analytics accurate by counting only those still eligible to finish.

Use them when a contact’s action—like withdrawing—makes them ineligible to continue. Exit Triggers only apply to Journeys with **active** or **expired** status.

**Example:** If a student’s decision status changes to *withdrawn*, their Journey ends as *exited*, keeping your active count and conversion data clean.

---