---
title: Grade Risk Detection for Courses
url: https://help.element451.com/en/articles/12824243-grade-risk-detection-for-courses
collection: Courses
---

# Overview

Grade Risk Detection automatically identifies students whose academic performance is trending downward, helping your team act when it matters the most.

This feature tracks pairs well with our [Native Courses Integrations for Learning Management Systems](https://help.element451.com/en/articles/11589065-native-courses-integrations-for-learning-management-systems-lms) and monitors student grades across all active course enrollments, analyzes metrics, and assigns a risk level. No setup or configuration is required—Element451 does the tracking and scoring automatically.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1831405698/1fd00829a9a841edc9973bfde8d8/Grade+Risk-Academic+Advisor+Agent+%282%29.png?expires=1784333700&signature=40fad8f95950d23961789ef1247684074f40be6261eeee3621946f175699bdc2&req=dSgkF81%2BmIdWUfMW1HO4zd8s%2BBIFzvMkqY1%2FZj7KSqLj7qiKV%2F1eZiZZ0nE7%0A2niCjgjlbV0S1Q%2BJwTU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1831405698/1fd00829a9a841edc9973bfde8d8/Grade+Risk-Academic+Advisor+Agent+%282%29.png?expires=1784333700&signature=40fad8f95950d23961789ef1247684074f40be6261eeee3621946f175699bdc2&req=dSgkF81%2BmIdWUfMW1HO4zd8s%2BBIFzvMkqY1%2FZj7KSqLj7qiKV%2F1eZiZZ0nE7%0A2niCjgjlbV0S1Q%2BJwTU%3D%0A)

---

# How Grade Risk is Determined

1. Grades for each course enrollment are monitored.
2. Using grade-based [metrics](#h_0a7cfac410), the system adds points to generate a total score
3. The total score maps to a [risk level](#h_97ed5528fa) (None, Watch, At Risk, Critical)

## Special Considerations

* *Grade data is monitored whether it’s imported through an integration or managed manually.*
* *Grade history tracking and risk evaluation began on **November 12, 2025**.*

  *Risk levels will only appear on enrollments with grade updates **on or after that date**. Earlier grade activity won’t generate a risk level or trend history.*

## Metrics

Element451 evaluates several grade-based metrics for each enrollment. Each metric adds 1–2 points depending on its severity. Together, these metrics form the risk score that determines the final [level](#h_97ed5528fa) (explained in the next section).

|  |  |
| --- | --- |
| **Metric** | **Points** |
| **Velocity Drop** ​-*How quickly grades are falling (points/day)* | ≤ -1.0 adds +2 ≤ -0.6 adds +1 |
| **Drop from Peak** ​-*Percent decline from the highest grade* | ≥ 20% adds +2 ≥ 12% adds +2 ≥ 8% adds +1 |
| **Downward Streak**  *-Consecutive grade declines* | ≥ 3 adds +2 ≥ 2 adds +1 |
| **Below Passing + Falling** ​-*Latest grade* is *below passing (60) and trending down* | adds +2 |

### Special Cases:

* **Static Low Fallback:** When a student is already below passing but doesn’t have enough grade history to show a clear trend, the system still assigns the enrollment the "Watch" risk level by default. This prevents low-performing students from appearing as “none” simply because there isn’t enough data to calculate a pattern.

* **Term Urgency Bump:** If an enrollment is close to its end date—within seven days—and the student is below passing with grades that aren’t improving, the system increases the risk level by one step. This urgency bump reflects the limited time left for recovery. For example, a student with `Watch` would be bumped to `At Risk` and a student with `At Risk` would be bumped to `Critical`.

## Risk Levels

Element451 uses a point-based system to evaluate how grades are changing within each enrollment. Each enrollment starts with a score of **0**, then gains points based on specific performance [metrics](#h_0a7cfac410) (explained above). The higher the total score, the higher the risk level assigned.

|  |  |  |
| --- | --- | --- |
| **Score** | **Risk Level** | **Description** |
| < 2 | None | No risk detected. There isn’t enough grade history, the enrollment is complete, or no negative patterns are found. |
| 2–3 | Watch | Early indicators of decline. Grade changes show mild downward trends or static low performance. |
| 4–5 | At Risk | Clear warning signs. Steady or accelerating decline, multiple negative metrics, or stagnant performance below passing. |
| ≥ 6 | Critical | Severe and urgent decline. Performance drops sharply, stays below passing, or worsens near term end. |

---

# Accessing Grade Risk Data

You can view grade risk information at the individual level and use Segments to widen your view. Below we explain how to access grade risk data.

## Section Enrollment Details

You can review a student’s grade risk in the **Section Enrollment Details** side sheet. When you open an enrollment (whether from the student’s profile or the Courses list), you’ll see a **Grade Risk** card with:

* The enrollment’s current risk level
* The last time the risk level was updated
* The complete grade history used to calculate the risk

This view gives you meaningful context. You’ll see exactly how grades have changed over time and why a particular risk level was assigned.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828757660/b571446efb844cff240f8cf9376f/CleanShot-2B2025-11-13-2Bat-2B09_02_29.png?expires=1784333700&signature=315246577b8c7ac5ff281e3cc454d4556e57c14900555bb0ace9199fa9f996c3&req=dSglHs57modZWfMW1HO4zVZPQhNLTArT90MT8rB8lJdTTy2F%2Bh0Ds5WKl7LC%0AdORlyEBi%2FYobVyFzET0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828757660/b571446efb844cff240f8cf9376f/CleanShot-2B2025-11-13-2Bat-2B09_02_29.png?expires=1784333700&signature=315246577b8c7ac5ff281e3cc454d4556e57c14900555bb0ace9199fa9f996c3&req=dSglHs57modZWfMW1HO4zVZPQhNLTArT90MT8rB8lJdTTy2F%2Bh0Ds5WKl7LC%0AdORlyEBi%2FYobVyFzET0%3D%0A)

📌 **Note:** You can also view a student's grade history from their contact record activity feed. This is helpful if you want to skim how grades have been changing, but note that it doesn’t show risk levels. We recommend using the activity feed for quick reference, then opening the Section Enrollment Details side sheet for the full story.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828820171/52e85694fecba736010794703cea/Grade%2Bupdated%2Bto%2B-E2-80-9C80-E2-80-9D%2Bin%2B-E2-80-9CComm1010-E2-80-9D.png?expires=1784333700&signature=b7fc53e1a995aa77de241f0b69b65ba1c7b00c70c5d0742e81697f0c596dc9de&req=dSglHsF8nYBYWPMW1HO4zUftYud0dohrj5OU9nDZipJ4FSaP9UeMNci4An5Q%0AAKOVYkOvLinm2Xi1TBk%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828820171/52e85694fecba736010794703cea/Grade%2Bupdated%2Bto%2B-E2-80-9C80-E2-80-9D%2Bin%2B-E2-80-9CComm1010-E2-80-9D.png?expires=1784333700&signature=b7fc53e1a995aa77de241f0b69b65ba1c7b00c70c5d0742e81697f0c596dc9de&req=dSglHsF8nYBYWPMW1HO4zUftYud0dohrj5OU9nDZipJ4FSaP9UeMNci4An5Q%0AAKOVYkOvLinm2Xi1TBk%3D%0A)

## Segments

To view risk across groups of students, filter by **`Courses`** `> Enrollment - Risk Level`in **Segments**. Use segments to:

* Monitor all students marked as watch, at risk, or critical
* Build target groups for workflows and Bolt Agent Jobs

Segments give you a population-level view, while the enrollment details give you the insight behind each individual case.

✨ **Pro Tip:** Add additional filters—like term, course, or section details—to drill deeper into where risk is concentrated. This helps you spot patterns, compare areas of concern, or focus support strategically.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828760504/f9c4c1b4c39cb5bef9fe72c9f1fa/CleanShot-2B2025-11-12-2Bat-2B16_41_43.png?expires=1784333700&signature=e2760b1ba7607a2a6b8b22e363304288c3f3a349cc3b2ce535d44e35f9333c8e&req=dSglHs54nYRfXfMW1HO4zS7Mh%2BVlKTFBESJIA8ymahvnzfpJc31o4%2Fi8tjUW%0A6zpDGEUM1Ibe%2FQ1%2BUec%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828760504/f9c4c1b4c39cb5bef9fe72c9f1fa/CleanShot-2B2025-11-12-2Bat-2B16_41_43.png?expires=1784333700&signature=e2760b1ba7607a2a6b8b22e363304288c3f3a349cc3b2ce535d44e35f9333c8e&req=dSglHs54nYRfXfMW1HO4zS7Mh%2BVlKTFBESJIA8ymahvnzfpJc31o4%2Fi8tjUW%0A6zpDGEUM1Ibe%2FQ1%2BUec%3D%0A)

---

# Automating with Risk Data

Once grade risk levels are identified, you can automate support and outreach using **Bolt Agent Jobs** and **Workflows**. These tools help your team respond quickly and consistently as student performance changes.

## Bolt Agent Jobs

Enroll students into [Bolt Agent Jobs](https://help.element451.com/en/articles/11131186-getting-started-with-bolt-agent-jobs) when their risk level changes to enable autonomous outreach by a Bolt Agent. This helps students connect with support resources and access AI-powered help 24/7.

You have several options to refine *exactly* who enters a job. When adding the **Grade Risk Changed** trigger, you can:

* Choose the risk level you want to target (Watch, At Risk, or Critical)
* Set the **risk level trajectory** to trigger on **any change**, **increases only**, or **decreases only**
* Scope the trigger to a **specific course**

✨ **Pro Tip:** Create a Job powered by an Academic Support Agent to contact students showing increased risk. The agent can help them schedule an advising or tutoring appointment, share support resources, and offer conversational guidance to keep them engaged and on track.

📌 **Note:** A student may have more than one course at the same risk level. When a Bolt Agent Job runs, the agent receives all of the student's course enrollments with their current risk levels, but it is not forced to name every at-risk course in its message. To have outreach reference all current at-risk courses, add an explicit instruction to the agent or job, such as "list every course currently at Critical or At Risk." Risk levels are refreshed on each new assessment.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828669456/d5eec3509e3a8ec1ac5664281ee2/CleanShot+2025-11-13+at+08_54_19.png?expires=1784333700&signature=718fe70c2b3a174900230a8b276e3b0e51c5d861078ecb5a0137e63e129d9a23&req=dSglHs94lIVaX%2FMW1HO4zRq94td7LvBiMNEYo6TlrkX65SQLpIFr2%2BYX1joO%0ArrNJfZ14rXRUKfltY6I%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828669456/d5eec3509e3a8ec1ac5664281ee2/CleanShot+2025-11-13+at+08_54_19.png?expires=1784333700&signature=718fe70c2b3a174900230a8b276e3b0e51c5d861078ecb5a0137e63e129d9a23&req=dSglHs94lIVaX%2FMW1HO4zRq94td7LvBiMNEYo6TlrkX65SQLpIFr2%2BYX1joO%0ArrNJfZ14rXRUKfltY6I%3D%0A)

## Workflows

Trigger students to enter a [Workflow](https://help.element451.com/en/articles/1500265-getting-started-with-workflows-rules) automatically based on their risk level.

This is ideal for creating internal tasks or automating early intervention steps for academic advisors and success teams. Workflows make it easy to ensure that no at-risk student is missed, while automating routine follow-up actions behind the scenes.

When adding the **Grade Risk Changed** trigger to a Workflow, you’ll have the same refinement options available in Bolt Agent Jobs:

* Choose the **risk level** you want to act on
* Set the **risk level trajectory** to **any**, **increase**, or **decrease**
* Scope the trigger to a **course**

These options give you precise control over when internal workflows fire and which cases they target.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828666306/1e6668f79d6338215d504e16a8d6/CleanShot+2025-11-13+at+08_52_12.png?expires=1784333700&signature=a21e1bf679aa7972218744e224acab0208802cf855c97e2b24c2a609a7c7016f&req=dSglHs94m4JfX%2FMW1HO4zZyyGEviQGGwwS%2FtFugvtG1FZyw850E15X7yQx5q%0AtUueVHoiGRYIpMJEpO8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1828666306/1e6668f79d6338215d504e16a8d6/CleanShot+2025-11-13+at+08_52_12.png?expires=1784333700&signature=a21e1bf679aa7972218744e224acab0208802cf855c97e2b24c2a609a7c7016f&req=dSglHs94m4JfX%2FMW1HO4zZyyGEviQGGwwS%2FtFugvtG1FZyw850E15X7yQx5q%0AtUueVHoiGRYIpMJEpO8%3D%0A)

## Segments

[As mentioned above](#h_289e915cde), you can also use the **`Courses`** `> Enrollment - Risk Level` filter to [segment](https://help.element451.com/en/articles/1474191-segments-overview) students with similar risks. This helps you monitor overall student success, analyze patterns, or target communication to specific risk levels.

---

✨ **Pro Tip:** Launch a layered success strategy using **Segments** for tracking, **Workflows** for task automation, and **Bolt Agent Jobs** for immediate, personalized outreach.

---