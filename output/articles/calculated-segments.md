---
title: Calculated Segments
url: https://help.element451.com/en/articles/7891959-calculated-segments
collection: People
---

# Overview

Calculated segments are a cornerstone of Element451, powering automation and personalization across the platform. These dynamic segments **update** **automatically** **based** **on predefined conditions/filters**, making them essential for organizing contacts, triggering workflows, and driving engagement through campaigns.

Because calculated segments are foundational, they can be used across multiple modules—including workflows, campaigns, and more. One of the most powerful applications is the **“Joined Segment”** trigger in workflows, which automates actions when a contact meets the defined criteria. This allows for seamless automation of processes like outreach, follow-ups, and enrollment tracking.

**Important:** Your contract includes a set number of calculated segments per year. This total also includes **visibility groups** and **territories** **with** **active conditions**. Any calculated segments beyond your contract limit will be subject to [usage-based pricing](https://help.element451.com/en/articles/10421758-usage-based-billing-credits). You can track your usage—including any additional segments that will incur overage fees—at the top of the **Segments** page.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1406560304/8bcca47e13da2130c2eb17a01d38/Calc+Segments+Card.png?expires=1784333700&signature=be454d47dcf2ae4b5649798383e8d051b53087d8ca920bb137c0650ba153b6bb&req=dSQnEMx4nYJfXfMW1HO4zaeYVpYKiU8DoVImVTcvN1%2FOkJkFQfsGgNPbyI%2FR%0Ag12DrvJAMGxhjVKfur8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1406560304/8bcca47e13da2130c2eb17a01d38/Calc+Segments+Card.png?expires=1784333700&signature=be454d47dcf2ae4b5649798383e8d051b53087d8ca920bb137c0650ba153b6bb&req=dSQnEMx4nYJfXfMW1HO4zaeYVpYKiU8DoVImVTcvN1%2FOkJkFQfsGgNPbyI%2FR%0Ag12DrvJAMGxhjVKfur8%3D%0A)

---

# How Segments Work

## What Happens When You Create and Save a Segment?

When you create a segment, you apply filters to student records. Element451 queries your database and returns the students who meet the filter criteria. Once saved, the segment is assigned a unique identifier, which allows other modules—like Campaigns and Workflows—to reference it without needing to re-run the original query. This speeds up performance and reduces system load.

## Limitations of Default Segments

By default, a segment only includes the students who met the filter criteria when it was created. It does **not** update automatically. If new students meet the criteria later, they **will not** be added unless you manually refresh the segment or convert it into a **calculated segment**.

[Explore More: Creating a Segment](https://help.element451.com/en/articles/1474208-creating-a-segment)

---

# What Are Calculated Segments?

A **calculated segment** automatically updates as student records change. When a student meets the segment criteria, they are added. If they no longer meet the criteria, they are removed—ensuring the segment always reflects the latest data.

## How Calculated Segments Are Evaluated

The system re-evaluates calculated segments whenever:

* Student data is added, removed, or modified.
* A new activity (such as form submission or event registration) occurs.

**Note:** Calculated segments do not update instantly. There may be a short delay before changes are reflected.

## Identifying Calculated Segments

When viewing your segment list, **calculated segments** are indicated by a **green icon** next to the segment name. This helps distinguish them from regular segments at a glance.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1406619371/c443110459d5c3cfed47348f4970/CleanShot+2025-03-04+at+10_04_17.png?expires=1784333700&signature=a58c3a4eebae271c101af3d14d5fd011b390e574daee7f03915b41820bd13447&req=dSQnEM9%2FlIJYWPMW1HO4zW0H%2BQ9jLTKANRJpYjz6GjreGJWCoWvu9mp35%2FZo%0AdUch6F%2FiD4XchvT0Dxw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1406619371/c443110459d5c3cfed47348f4970/CleanShot+2025-03-04+at+10_04_17.png?expires=1784333700&signature=a58c3a4eebae271c101af3d14d5fd011b390e574daee7f03915b41820bd13447&req=dSQnEM9%2FlIJYWPMW1HO4zW0H%2BQ9jLTKANRJpYjz6GjreGJWCoWvu9mp35%2FZo%0AdUch6F%2FiD4XchvT0Dxw%3D%0A)

---

# How-To: Convert Segment to Calculated Segment

You can enable calculated segments in the **Segments** module.

1. Navigate to **Contacts** > **Segments**.
2. Locate the Segment you wish to convert to Calculated.
3. Click the **three-dot icon** (⋮) to the far right of the Segment.
4. Select **Convert to Calculated** from the menu.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1404806735/5283988f4a6831cc87c5df7c407a/Calculated+Segment.png?expires=1784333700&signature=131069ffc0963bd0993b3c4c9c7f330f39e15985f3eafdcc601443864e669565&req=dSQnEsF%2Bm4ZcXPMW1HO4ze2f4DbzBIw76Q6hq1tuREJRvfNEzcGrz3w984eB%0A6Wr9xL2B1LP3I20Nwgw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1404806735/5283988f4a6831cc87c5df7c407a/Calculated+Segment.png?expires=1784333700&signature=131069ffc0963bd0993b3c4c9c7f330f39e15985f3eafdcc601443864e669565&req=dSQnEsF%2Bm4ZcXPMW1HO4ze2f4DbzBIw76Q6hq1tuREJRvfNEzcGrz3w984eB%0A6Wr9xL2B1LP3I20Nwgw%3D%0A)

---

# How-To: Revert Calculated Segment to Non-Calculated

While calculated segments are valuable for dynamic updates, we recommend converting them back to **regular segments** once you’re finished using them. This helps optimize performance, reduce unnecessary recalculations, and ensure you stay within your allotted number of calculated segments. Remember, any additional calculated segments beyond your allocation are subject to [usage-based billing](https://help.element451.com/en/articles/10421758-usage-based-billing-credits), so converting them when no longer needed helps manage costs effectively.

To convert a calculated segment back to a regular segment:

1. Navigate to **Contacts** > **Segments**.
2. Locate the Calculated Segment you wish to convert back.
3. Click the **three-dot icon** (⋮) to the far right of the Segment.
4. Select **Revert to Non-Calculated** from the menu.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1406592936/2a12bfcc7a914c64ba5dd95ed73f/CleanShot+2025-03-04+at+10_00_13.png?expires=1784333700&signature=a3f75068fc0bdd30759a085b73596dc1f099ba2d1c76c90d8e3de7ecb77ad671&req=dSQnEMx3n4hcX%2FMW1HO4zVqo9zfyn%2BXAnVEyvGvkKfKS9ycaFqqXTGNKZYhI%0A5wqmO8%2BDMPVqoKc%2Bchc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1406592936/2a12bfcc7a914c64ba5dd95ed73f/CleanShot+2025-03-04+at+10_00_13.png?expires=1784333700&signature=a3f75068fc0bdd30759a085b73596dc1f099ba2d1c76c90d8e3de7ecb77ad671&req=dSQnEMx3n4hcX%2FMW1HO4zVqo9zfyn%2BXAnVEyvGvkKfKS9ycaFqqXTGNKZYhI%0A5wqmO8%2BDMPVqoKc%2Bchc%3D%0A)

---

# Use Case: Automating Ongoing Communications

One of the best reasons to use a calculated segment is when you need dynamic, real-time updates for automated processes.

**Example: Nudging Students to Complete Applications**

Let’s say you want to create a drip campaign to remind students to finish their applications. Here’s how a calculated segment helps:

1. Create a **calculated segment** with a filter for students who have started their application.
2. Set up a **Workflow** that triggers when a student enters this segment.
3. As new students start their applications, they’ll automatically be added to the segment and receive the reminder emails.

---