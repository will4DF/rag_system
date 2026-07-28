---
title: 3 Essential Source Tracking Tactics
url: https://help.element451.com/en/articles/10269979-3-essential-source-tracking-tactics
collection: Data Management
---

Use these step-by-step examples to enhance your lead and prospect source tracking in Element451.

# Sources in Element451

Be familiar with [Sources in Element451](https://help.element451.com/en/articles/2066892-sources) before continuing.

In these examples, we'll create Custom Sources and automatically apply them to contacts when needed. These Sources will then be visible in the [Sources Dashboard](https://help.element451.com/en/articles/6916688-sources-dashboard), and can be exported in batch when [repeating on Source](https://help.element451.com/en/articles/9007317-creating-exports#h_32db4b2e5b).

## Example 1: Tracking College Fair Attendance

In this example, we'll add a Custom Source to each student that attended a college fair. We'll assume that you've tracked Event attendance using the [Event's module](https://help.element451.com/en/articles/1520520-getting-started-with-events), and already have an event for this particular college fair.

### Step 1: Create College Fair Source Codes

Define a "College Fair" Source Code and add Source Segments for the Fair. Add additional Source Segments for each Fair.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293692987/05f08381ae8619b1950218d133db/Screenshot+2024-08-20+at+3_46_20%E2%80%AFPM.png?expires=1784333700&signature=07673d2cab5fbc8ef55c67b9c25be9619f9da820a8cd9b413a39d85a3936984e&req=dSIuFc93n4hXXvMW1HO4zczD291YuIXCe1igNsQmbFOJtDRkXYN73GWx8Ehb%0A4tdloCaTv6BtXyvWkY0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293692987/05f08381ae8619b1950218d133db/Screenshot+2024-08-20+at+3_46_20%E2%80%AFPM.png?expires=1784333700&signature=07673d2cab5fbc8ef55c67b9c25be9619f9da820a8cd9b413a39d85a3936984e&req=dSIuFc93n4hXXvMW1HO4zczD291YuIXCe1igNsQmbFOJtDRkXYN73GWx8Ehb%0A4tdloCaTv6BtXyvWkY0%3D%0A)

### Step 2: Create a Workflow Rule

Create a [workflow rule](https://help.element451.com/en/articles/8859695-how-to-create-a-rule) to automatically assign the "College Fair" Source Code to a student once they register for the event.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293695634/7ab04b0fe10bda99ea348c3fcfac/Screenshot+2024-08-20+at+4_00_09%E2%80%AFPM.png?expires=1784333700&signature=51f8476bc6ed62eae4c403c36ebb3a216040e61cd8dc51dc4e15f7d1cdedf3a9&req=dSIuFc93mIdcXfMW1HO4zU7H5o9lHLenwCycK27vPV%2FRHa3%2BLqKfupAWi7jc%0AHL4yt7QZSZ2ZEYGe8LI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293695634/7ab04b0fe10bda99ea348c3fcfac/Screenshot+2024-08-20+at+4_00_09%E2%80%AFPM.png?expires=1784333700&signature=51f8476bc6ed62eae4c403c36ebb3a216040e61cd8dc51dc4e15f7d1cdedf3a9&req=dSIuFc93mIdcXfMW1HO4zU7H5o9lHLenwCycK27vPV%2FRHa3%2BLqKfupAWi7jc%0AHL4yt7QZSZ2ZEYGe8LI%3D%0A)

**Set [Step Condition](https://help.element451.com/en/articles/1500294-conditions):** Use the "DOES NOT HAVE" operator on the Sources (All Properties) filter to ensure that the rule only applies to students who don't already have the College Fair Source associated with their contact. This prevents adding the same Source twice.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293696225/ad697e1ec7d0cd6155c19be953b9/Screenshot+2024-08-20+at+4_06_48%E2%80%AFPM_png.png?expires=1784333700&signature=09146b3e714e1a2e2d7312b175eb9ca62a0190477b3b0f849e0e8936bb46e310&req=dSIuFc93m4NdXPMW1HO4zQuHvK%2FWK9yl8q5R%2B7ME2GXkCdysB%2F8p44FWUmMr%0A9bIb8zwzdRS%2BYd%2BRpBg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293696225/ad697e1ec7d0cd6155c19be953b9/Screenshot+2024-08-20+at+4_06_48%E2%80%AFPM_png.png?expires=1784333700&signature=09146b3e714e1a2e2d7312b175eb9ca62a0190477b3b0f849e0e8936bb46e310&req=dSIuFc93m4NdXPMW1HO4zQuHvK%2FWK9yl8q5R%2B7ME2GXkCdysB%2F8p44FWUmMr%0A9bIb8zwzdRS%2BYd%2BRpBg%3D%0A)

**Specify the [Rule Step Action](https://help.element451.com/en/articles/1500292-actions):** In the workflow action settings, choose "Add custom source to user." Then, select the appropriate "Source Alias" (e.g., "College Fairs") and "Source Code Segment" (e.g., "Roosevelt HS").

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293696355/bea964093a0a288c254269e401cd/Screenshot+2024-08-20+at+4_08_30%E2%80%AFPM.png?expires=1784333700&signature=c935146df63ed305a14b664e55294989827e6c483938abc6b6bc15981a601e4a&req=dSIuFc93m4JaXPMW1HO4zdfvwI4UagFoW35jCypawXDDqJSazG8%2BieuwClfh%0A4V2R0qmPgJZMbhoG6XA%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1293696355/bea964093a0a288c254269e401cd/Screenshot+2024-08-20+at+4_08_30%E2%80%AFPM.png?expires=1784333700&signature=c935146df63ed305a14b664e55294989827e6c483938abc6b6bc15981a601e4a&req=dSIuFc93m4JaXPMW1HO4zdfvwI4UagFoW35jCypawXDDqJSazG8%2BieuwClfh%0A4V2R0qmPgJZMbhoG6XA%3D%0A)

Expand this Rule with more steps for each College Fair attended.

💡 Best Practice: "Why add Source when the Event registration already exists on the contact?" Adding a Source keeps all source-related data in one place. This enables the College Fair Source to be visible in the Sources Insights Dashboard, and includes the College Fair Source when exporting Sources.

## Example 2: Tracking Digital Marketing Sources

In this example, we'll create a Custom Source for a contact based on the UTM values in their Form Submission URL.

Note that Form Submission activities capture the URL of the page at which the Form was submitted, including marketing data such as UTMs that were appended to the URL of the page. Learn more about [Form Submission activities](https://help.element451.com/en/articles/9184596-understanding-form-submissions#h_1d02b003f7) and [Embedding Forms](https://help.element451.com/en/articles/9000414-embedding-forms-on-pages-external-sites).

In this example, we'll assume that you're running an ad on Instagram for a psychology program. You've configured the ad in [Meta Ads Manager](https://www.facebook.com/business/tools/ads-manager) and have added UTM parameters to the destination URL of your ad. The URL is to an [Element451 Page](https://help.element451.com/en/articles/9311641-pages-overview) with an [Element451 Form embedded](https://help.element451.com/en/articles/9000414-embedding-forms-on-pages-external-sites#h_ccab1dbac2).

### Step 1: Match UTMs to Sources

This is a logical exercise we're we'll determine how to represent UTM values as Custom Sources in Element451. Keep in mind, Element451 Source's only have two levels or hierarchy, while UTMs can have up to five (Source, Medium, Content, Campaign, Term). Decide which two UTMs to save as the Source.

In this example, we'll use the `utm_source` value as the Source Name, and the `utm_campaign` value as the Source Segment.

### Step 2: Create Sources in Element451

With our Source Name and Source Segment decided, we'll create a Source Name for "Instagram" and a Source Segment for "Psychology Retargeting", plus any other campaigns we may be running.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294900023/5118efe1a90fbbd11415ff19cf3f/Screenshot+2024-08-21+at+10_54_41%E2%80%AFAM+%282%29.png?expires=1784333700&signature=b02a873dedd737198d641ae747ee8e5a3aa826b0585fdba47818eb1ae3720530&req=dSIuEsB%2BnYFdWvMW1HO4zQDjgaGQivnabcQrmg1Z7TWndjZLWFvWu0zszz7h%0AJmC8YOrqW8V%2FlVJZsao%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294900023/5118efe1a90fbbd11415ff19cf3f/Screenshot+2024-08-21+at+10_54_41%E2%80%AFAM+%282%29.png?expires=1784333700&signature=b02a873dedd737198d641ae747ee8e5a3aa826b0585fdba47818eb1ae3720530&req=dSIuEsB%2BnYFdWvMW1HO4zQDjgaGQivnabcQrmg1Z7TWndjZLWFvWu0zszz7h%0AJmC8YOrqW8V%2FlVJZsao%3D%0A)

### **Step 3: Create a Rule to Assign Sources:**

Create a workflow rule that assigns a Source Code based on the UTM data of the form submission URL. The Rule can be triggered by a form submission or by joining a Segment.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294911284/15e2b4eb982b0e3c2be7a0202344/Screenshot+2024-08-21+at+10_43_46%E2%80%AFAM+%282%29.png?expires=1784333700&signature=755cde9e05e2b0cf373bb3b2d8f6ccb06037ff984d71611d6a1d12ed3f778b46&req=dSIuEsB%2FnINXXfMW1HO4zeNqYZXcSWoWFC9Kh%2FrHlA%2BFKWbZEowFTZpG2fgl%0AP18O2R7uxnO83Lqp4OQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294911284/15e2b4eb982b0e3c2be7a0202344/Screenshot+2024-08-21+at+10_43_46%E2%80%AFAM+%282%29.png?expires=1784333700&signature=755cde9e05e2b0cf373bb3b2d8f6ccb06037ff984d71611d6a1d12ed3f778b46&req=dSIuEsB%2FnINXXfMW1HO4zeNqYZXcSWoWFC9Kh%2FrHlA%2BFKWbZEowFTZpG2fgl%0AP18O2R7uxnO83Lqp4OQ%3D%0A)

**Set Rule [Conditions](https://help.element451.com/en/articles/1500294-conditions):** The step should only apply the Source if the contact has a Form Submission with specific UTM values and if the contact does not already have a Source of the same kind. Use to filters to reflect this:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294917630/d1d52b429f973b84912acd0c1780/Screenshot+2024-12-12+at+9_52_11%E2%80%AFAM.png?expires=1784333700&signature=3cedf9a5ce4553552f3bac6fb1d3cd682ff4962b07a49305eb67f11ca08645af&req=dSIuEsB%2FmodcWfMW1HO4zU4dKECYeZc%2FbCLb5waHJ%2BPWJ60YyU950wJNQt2j%0AvX6Wjd%2Fcmi89YmROe7g%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294917630/d1d52b429f973b84912acd0c1780/Screenshot+2024-12-12+at+9_52_11%E2%80%AFAM.png?expires=1784333700&signature=3cedf9a5ce4553552f3bac6fb1d3cd682ff4962b07a49305eb67f11ca08645af&req=dSIuEsB%2FmodcWfMW1HO4zU4dKECYeZc%2FbCLb5waHJ%2BPWJ60YyU950wJNQt2j%0AvX6Wjd%2Fcmi89YmROe7g%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294910880/3c3f5ecd89f868ad847817b77289/Screenshot+2024-08-21+at+12_04_26%E2%80%AFPM.png?expires=1784333700&signature=823ba1860f32e13a7b9d3f77e83383a09a4a1fa0eeddc5d4123a39c5d18bcf6d&req=dSIuEsB%2FnYlXWfMW1HO4zTDtCaLTbDM8SEdjWkPfqWXu6KzhRhtihfAj80lp%0AIWyl23hpwq8GGoVdsqY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294910880/3c3f5ecd89f868ad847817b77289/Screenshot+2024-08-21+at+12_04_26%E2%80%AFPM.png?expires=1784333700&signature=823ba1860f32e13a7b9d3f77e83383a09a4a1fa0eeddc5d4123a39c5d18bcf6d&req=dSIuEsB%2FnYlXWfMW1HO4zTDtCaLTbDM8SEdjWkPfqWXu6KzhRhtihfAj80lp%0AIWyl23hpwq8GGoVdsqY%3D%0A)

**Specify the [Rule Step Action](https://help.element451.com/en/articles/1500292-actions):** If the conditions are met, the step should apply the Source to the contact.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294910291/caee850cfea97f28bc9aeb9dc62b/Screenshot+2024-08-21+at+12_02_34%E2%80%AFPM.png?expires=1784333700&signature=6087b8df1330d933bbf747eeedb6deec4c91a3395f15f169703c1055990861ca&req=dSIuEsB%2FnYNWWPMW1HO4zWFkCh1HQGCfzOvaA4IzrvFkuZHg3mr%2FrnR%2F7P%2BC%0AgdkgxiBOMh1dq7psRJI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294910291/caee850cfea97f28bc9aeb9dc62b/Screenshot+2024-08-21+at+12_02_34%E2%80%AFPM.png?expires=1784333700&signature=6087b8df1330d933bbf747eeedb6deec4c91a3395f15f169703c1055990861ca&req=dSIuEsB%2FnYNWWPMW1HO4zWFkCh1HQGCfzOvaA4IzrvFkuZHg3mr%2FrnR%2F7P%2BC%0AgdkgxiBOMh1dq7psRJI%3D%0A)

Expand this Rule with more steps for each UTM Source and UTM Campaign you wish to track.

💡 Note: Even though Sources can only capture two data points (UTM Source and UTM Campaign in this example), all marketing data appended to the URL of the form submission page is still available on the [Form Submission activity](https://help.element451.com/en/articles/9184596-understanding-form-submissions#h_1d02b003f7). No data is lost.

## Example 3: Tracking Sources from Purchased Lists

In this example, we'll add a Custom Source to contacts whose information was purchased from a vendor, such as College Board. We'll assume that the vendor has sent us a .csv data file and we've already created an [Import Task](https://help.element451.com/en/articles/9001231-creating-imports) for this file.

### **Step 1: Create Purchased List Source Codes**

Define a Source Code for "Purchased List" and create Source Segments for each list provider. For example, "Cappex", "College Board", "EAB" and so on.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294965067/7a5689819f350120045f3283f961/Screenshot+2024-08-21+at+12_50_47%E2%80%AFPM+%282%29.png?expires=1784333700&signature=af0792ce509e1c7a35478ea8676afdc0c2eda7bf84ec8ac69cd5cb8ffd94043b&req=dSIuEsB4mIFZXvMW1HO4zelWcQqin6Y51oQ2qEmK23Ox0VEn8aDzVsIV5vp9%0AezO%2BSvWdDGxMiXroFpI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294965067/7a5689819f350120045f3283f961/Screenshot+2024-08-21+at+12_50_47%E2%80%AFPM+%282%29.png?expires=1784333700&signature=af0792ce509e1c7a35478ea8676afdc0c2eda7bf84ec8ac69cd5cb8ffd94043b&req=dSIuEsB4mIFZXvMW1HO4zelWcQqin6Y51oQ2qEmK23Ox0VEn8aDzVsIV5vp9%0AezO%2BSvWdDGxMiXroFpI%3D%0A)

### **Step 2: Map Source Code and Segment**

Map Calculated Columns at the bottom of the mapping tab to apply the Source Code and Source Segment GUIDs based on the list provider. For example, adding `"training.taxonomy.4119735"` to the formula of the Source Segment column will assign the College Board Source Segment to the contact.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294959610/f0569a81fbeff379b9d838af3a87/Screenshot+2024-08-20+at+9_54_37%E2%80%AFAM.png?expires=1784333700&signature=8df33ce4ffcedbeb45eb12149070185fb4016b8ddd8de9beb8d78e72dc61422e&req=dSIuEsB7lIdeWfMW1HO4zR0PnRT%2FthpmUXq%2Ftg0L93D7OMO8YoxjWf%2B8LVYM%0AiipVRgBcIKXZ6w4tWVw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1294959610/f0569a81fbeff379b9d838af3a87/Screenshot+2024-08-20+at+9_54_37%E2%80%AFAM.png?expires=1784333700&signature=8df33ce4ffcedbeb45eb12149070185fb4016b8ddd8de9beb8d78e72dc61422e&req=dSIuEsB7lIdeWfMW1HO4zR0PnRT%2FthpmUXq%2Ftg0L93D7OMO8YoxjWf%2B8LVYM%0AiipVRgBcIKXZ6w4tWVw%3D%0A)

---