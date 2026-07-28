---
title: Decisions: Checklists
url: https://help.element451.com/en/articles/9210688-decisions-checklists
collection: Decisions
---

Customize and manage application checklists to guide students through requirements, enhancing organization and clarity.

# Overview

The Checklist feature in the Decisions module is a powerful tool that can be customized to suit the unique needs of your application process. Each checklist item can be tailored to display for all selected applications or targeted to specific populations using segments, ensuring that students see only the relevant checklist items in their application portal. This feature helps applicants stay organized and aware of what needs to be completed both before and after admission decisions are released.

Students can view and complete checklist items, track which items have been fulfilled, and easily stay informed about any requirements that apply at different stages of the admissions process.

This article will cover the various checklist item types, detailing those automatically marked as complete and those requiring manual intervention by reviewers.

🚨 **Important:** In order for the checklist card to display in the student's application site/portal, the following items must be true:

1. You must enable the "checklist" card in the [application dashboard](https://help.element451.com/en/articles/9040630-creating-managing-applications#h_caf4aecfdf).
2. A decision must exist, meaning the application must be submitted.
3. A checklist item must exist for that decision.

## Accessing Checklists

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Checklist** tab.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259742443/32b6b269c96e65b66e4184c6b6aa/Checklist%2B%2BOverview.png?expires=1784397600&signature=298afa2c8c7b5433333f42c7d13a9104591b2365a33a572db0f7b17885962ddb&req=dSIiH856n4VbWvMW3nq%2BgUkHp9mG0npd7lrWWtjvbK%2B4L7s7KOyEJppKv1%2Bh%0Ag4zDJGMByFiT6ZEgB3WGINMHZ3E%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259742443/32b6b269c96e65b66e4184c6b6aa/Checklist%2B%2BOverview.png?expires=1784397600&signature=298afa2c8c7b5433333f42c7d13a9104591b2365a33a572db0f7b17885962ddb&req=dSIiH856n4VbWvMW3nq%2BgUkHp9mG0npd7lrWWtjvbK%2B4L7s7KOyEJppKv1%2Bh%0Ag4zDJGMByFiT6ZEgB3WGINMHZ3E%3D)

---

# Creating a Checklist

Checklist items can be applied to one or more applications. To create a checklist for an application, follow the steps outlined below:

## Step 1: Create a Checklist Item

The first step in creating a checklist is adding each checklist item. Once your items are set, you can proceed to enable the checklist card on the application.

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Checklist** tab.
3. Click the blue plus sign button in the bottom right corner.
4. You will be prompted to provide initial setup information using three tabs: ***General***, ***Works For***, and ***Visible To***. We will explain the configurations within each tab below:  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259580233/89f5d6f579bfd7c0a9c95289a0b0/New+Checklist+Form.png?expires=1784397600&signature=a54ce9d0ed8086669696ae77ab36b9bc2060d6e0a5947b5aba3b45c99e14c205&req=dSIiH8x2nYNcWvMW3nq%2BgVTV%2B31pHUh8pGnUGWCEYqhwYC37tcyNW2oIODVf%0A%2Bl5z%2Fkv1tyQFOFD8%2FBMolPg10Fo%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259580233/89f5d6f579bfd7c0a9c95289a0b0/New+Checklist+Form.png?expires=1784397600&signature=a54ce9d0ed8086669696ae77ab36b9bc2060d6e0a5947b5aba3b45c99e14c205&req=dSIiH8x2nYNcWvMW3nq%2BgVTV%2B31pHUh8pGnUGWCEYqhwYC37tcyNW2oIODVf%0A%2Bl5z%2Fkv1tyQFOFD8%2FBMolPg10Fo%3D)

   ## General

   * **Active**

     + Enabling this option makes the checklist item live and adds it to all applicable checklists.
     + Checklist items are dynamic, meaning that once activated, the item will appear on checklists for both **current** applicants and **new** applicants moving forward.
   * **Require**

     + Enabling this option categorizes the checklist item as **Required**, helping applicants identify items they must complete.
     + Items not marked as required will appear under the **Optional** section of the checklist card, providing flexibility for applicants to decide whether to submit them.
     + The checklist card automatically organizes items into these two categories—**Required** and **Optional**—based on this setting.
   * **Post-Admit**

     + Enable this option to keep the checklist item visible to applicants after an admission decision is released. For more details, [see the section below](#h_32117e61c9).
   * **Type**

     + Choose one of the five checklist item types. Detailed explanations for each type are provided [in the section below](#h_0218dafdac).
   * **Name** + **Description**

     + Enter a name and description for the item. These will be **visible to applicants**, so include clear details or instructions if needed.

   ## Works For

   * Use this setting to specify the application(s) where the checklist item should appear.
   * If you have multiple applications, you can use the **“All Applications”** toggle to apply the checklist item to all applications. Alternatively, you can go through your list of applications and individually toggle the **“Apply”** setting for specific ones.

   ## Visible To

   * Use this setting to define who can see the checklist item by adding conditions with **User Segment** or **User Segment Reference**. For example, you might display the item to applicants with specific test scores or require a TOEFL/IELTS exam for applicants whose citizenship is outside the United States.
   * **Important:** This setting only determines visibility—it does not affect the behavior of how the checklist item's status is updated.
5. After configuring your new checklist item, click **Create** in the bottom right corner.
6. Your next steps depend on the checklist item type:

   * **Custom**, **Transcript**, or **One-off**: Proceed to [Step 2](#h_251e02cdb3) or add more checklist items by repeating Steps 1–6, as needed.
   * **Conditional**: Add the condition(s) that will automatically mark the item as **complete** and/or **waived**. The **Set Conditions** side sheet should open automatically after clicking **Create**. If it doesn't, use the icons next to the checklist item to open it:

     + **Check mark icon**: Set the conditions that will automatically mark the checklist item as **Complete** (*Mark Complete When…*).
     + **Flag icon**: Set the conditions that will automatically mark the checklist item as **Waived** (*Mark Waived When…*).

     ​

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259624812/ccb5875643cc279b2a596a264fc7/checklist+condition.png?expires=1784397600&signature=80dfc1481b08e3897015e950bf4f6496d59904aaab0ff5498b4715e2bb204fb9&req=dSIiH898mYleW%2FMW3nq%2BgT073Si%2Fhc2MiIjDO9xeGVhfg13jI1uD3xT4SXsl%0A11ucWe9Z58pUBzKw%2FC%2FViCf2SPI%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259624812/ccb5875643cc279b2a596a264fc7/checklist+condition.png?expires=1784397600&signature=80dfc1481b08e3897015e950bf4f6496d59904aaab0ff5498b4715e2bb204fb9&req=dSIiH898mYleW%2FMW3nq%2BgT073Si%2Fhc2MiIjDO9xeGVhfg13jI1uD3xT4SXsl%0A11ucWe9Z58pUBzKw%2FC%2FViCf2SPI%3D)
7. Once you've added your condition(s), proceed to [Step 2](#h_251e02cdb3) or add more checklist items by repeating Steps 1–6.

## Step 2: Add the Checklist Card to the Application

After creating your checklist item(s), you need to add the checklist card to the application. **Applicants won't see the item(s) until this step is complete**.

Follow these steps to add the checklist card:

1. Navigate to **Applications** > **Applications** > **All** **Applications**.
2. Click on the application name where you want to display the checklist item. This will open your Application editor.
3. In the left menu, under **Content**, click on **Dashboard**.

   [![](https://downloads.intercomcdn.com/i/o/915870112/d096dd88957fa728b581625c/Screenshot+2023-12-21+at+3.01.38%E2%80%AFPM.png?expires=1784397600&signature=6a385aec946e5d19e94032d867005a86cc82526bd4b1b6818ecd8b0b6c3393cc&req=fSEiHs5%2BnIBdFb4V1XW4gWsuNagrhhnZ3%2FyBq6zBDqpzOy%2BuGUOVD0fzp3I8%0AoLhKegjI124eh2aMMQA6BvZ47g%3D%3D)](https://downloads.intercomcdn.com/i/o/915870112/d096dd88957fa728b581625c/Screenshot+2023-12-21+at+3.01.38%E2%80%AFPM.png?expires=1784397600&signature=6a385aec946e5d19e94032d867005a86cc82526bd4b1b6818ecd8b0b6c3393cc&req=fSEiHs5%2BnIBdFb4V1XW4gWsuNagrhhnZ3%2FyBq6zBDqpzOy%2BuGUOVD0fzp3I8%0AoLhKegjI124eh2aMMQA6BvZ47g%3D%3D)
4. Under **Cards**, click the button that says **+ Add Card.**

   [![](https://downloads.intercomcdn.com/i/o/915869906/e5cc17a080fce17cec889b30/Screenshot+2023-12-21+at+3.01.12%E2%80%AFPM.png?expires=1784397600&signature=ae61222265057c519859e11b01daf3314c815709a2459bfd7431ab55710e46cc&req=fSEiHs93lIFZFb4V1XW4gX2pKGnsHOyVwxStiTq6X59Rg7ki%2FDxLAZv3tRJ%2F%0AWThgL9Dn9QiJkYYxBnUyjDiASQ%3D%3D)](https://downloads.intercomcdn.com/i/o/915869906/e5cc17a080fce17cec889b30/Screenshot+2023-12-21+at+3.01.12%E2%80%AFPM.png?expires=1784397600&signature=ae61222265057c519859e11b01daf3314c815709a2459bfd7431ab55710e46cc&req=fSEiHs93lIFZFb4V1XW4gX2pKGnsHOyVwxStiTq6X59Rg7ki%2FDxLAZv3tRJ%2F%0AWThgL9Dn9QiJkYYxBnUyjDiASQ%3D%3D)
5. Complete the fields on the Add Card side sheet:

   * **Title:** Enter a name for the card. This will appear at the top of the checklist card in the student's application portal (e.g., *Your Admissions Checklist*).
   * **Type:** Select **Checklist Card** from the options.
   * **Conditional Logic:** (Optional) Add conditions to determine which students will see this card.**Title**: Give the card a name. It will be displayed at the top of the checklist card in the student's application portal (e.g., Your Admissions Checklist)
6. When you are finished completing the fields, click **Add** in the top right corner.

---

[![](https://downloads.intercomcdn.com/i/o/915869830/ad8d9b36ded582b5bc9dd13b/Screenshot+2023-12-21+at+3.01.02%E2%80%AFPM.png?expires=1784397600&signature=7080f4de8c8b9bc37dafd863e84c41b2e22eb8856fec6a7c3c86043225329095&req=fSEiHs93lYJfFb4V1XW4gdaibVLXJC4UPIq8BDwAFN5RjDGAZWbt19ftl4ZZ%0ABJKoDoYIg29jzdewMRELiY%2FVRQ%3D%3D)](https://downloads.intercomcdn.com/i/o/915869830/ad8d9b36ded582b5bc9dd13b/Screenshot+2023-12-21+at+3.01.02%E2%80%AFPM.png?expires=1784397600&signature=7080f4de8c8b9bc37dafd863e84c41b2e22eb8856fec6a7c3c86043225329095&req=fSEiHs93lYJfFb4V1XW4gdaibVLXJC4UPIq8BDwAFN5RjDGAZWbt19ftl4ZZ%0ABJKoDoYIg29jzdewMRELiY%2FVRQ%3D%3D)

# Checklist Item Types

There are five different types of checklist items. No matter the type, the student will see a title, description, and if the item is required.

🚨 **Important:** For transcripts and supplemental forms, add only **one checklist item per type**. The system automatically adds multiple items based on the information provided. More details are listed below with each respective type.

## Condition

Conditional checklist items are automatically marked as **Complete** or **Waived** when predefined conditions are met. These conditions allow you to streamline checklist management by leveraging automated completion and waiver rules.

**Purpose:** Use this type when you want to **automate** checklist completion or waiver based on user segments or specific data criteria.

### Setting Conditions

Conditional checklist items use two independent rule sets, accessed from the icons next to the checklist item:

* **Mark Complete When…** (**check mark icon**): The conditions that, when met, automatically mark the item as **Complete**.
* **Mark Waived When…** (**flag icon**): The conditions that, when met, automatically mark the item as **Waived**.

You can set one or both. For each rule set, you can either load an existing segment or build custom conditions by adding individual data filters (such as “Submitted Form”).

### How Completion and Waiver Conditions Interact

**Completion takes precedence over waiver:**

* If the **completion** conditions are met, the item is marked **Complete** — regardless of whether the waiver conditions are also met.
* If the **waiver** conditions are met but the completion conditions are not, the item is marked **Waived**.
* If neither set of conditions is met, the item remains incomplete until conditions are met or it is updated manually.

### Important Behavior

* Once an item is automatically marked **Complete** or **Waived** by the system, the status will not revert if the applicant later no longer meets the conditions.
* Condition checklist items cannot be manually changed back to **Not Completed** once the system has set their status. For more flexibility in manually updating statuses, use the **Custom** or **One-Off** checklist item types.

**Example:** You're managing official ACT/SAT scores. Under **Mark Complete When**, you load a calculated segment of applicants who have official test scores on file—when an applicant enters this segment, the item is automatically marked **Complete**. Under **Mark Waived When**, you add a condition for applicants whose program does not require test scores—those applicants have the item automatically marked **Waived** instead.

📌 **Note:** Text area fields can only be filtered using **Exists** and **Does Not Exist**. This applies both when building custom conditions directly on a checklist item and when creating segments.

✨ **Pro Tip:** Leverage the item description to provide detailed instructions to the student on completing the checklist item. This description can include links to relevant resources and step-by-step guidance.

## Custom

Custom checklist items require **manual** **oversight**, giving you full control over when and how the item is marked as completed. This type is ideal for requirements that need personalized review or verification before completion.

**Purpose:** Use this type when you need flexibility to manually update the item's status based on your review process, rather than relying on automated conditions.

**Example**: Imagine you need to verify residency. Using the **Custom** type, you can review the residency documentation submitted by the applicant and then manually mark the item as complete. This ensures you have thoroughly assessed the requirement before updating its status.

✨ **Pro Tip:** Provide clear instructions to applicants through the **item description**, helping them understand how to fulfill the requirement. Include links to relevant resources, step-by-step guidance, or other materials to make the process seamless for the student.

Unlike condition-based checklist items, **Custom** items allow you to manually change their status at any time. This flexibility is especially useful for requirements that require judgment or review on a case-by-case basis.

## Transcript

Transcript checklist items are specifically designed to track transcripts required from applicants. This type streamlines checklist management by automatically marking the item as complete when the required transcript has been uploaded. **Important:** Only one transcript checklist item should be added per application, regardless of the number of transcripts required. The system will automatically handle multiple transcripts. See [Applications with Multiple Transcripts](#h_885f18bece) for more details.

**Purpose:** Use this type to efficiently manage transcript submissions, ensuring that requirements are automatically updated without manual intervention.

**How It Works:** The item is automatically marked complete **only** when a transcript is uploaded through one of these methods:

1. **By the applicant:** When the student uploads a transcript as part of their application using the **transcript field** within the **school field grouping**.
2. **By an internal user:** When a transcript is uploaded from the **school card** on the student's profile.

   * 📌 **Note:** Do not upload transcripts through the **documents card** on the student's profile. Transcripts uploaded this way will **not** mark the checklist item as complete.

### 🚨 Important: Applications with Multiple Transcripts

Managing multiple transcripts on an application is simple with the system's automated process. Here's what you need to know:

#### Add Only One Checklist Item

Add **one** transcript checklist item to each application, no matter how many transcripts are required. The system will automatically create separate checklist items for each school the applicant includes in their application.

#### Use a Generic Title

For the transcript checklist item, choose a generic title like “Transcript.” This is important because the system automatically appends the school name in parentheses to differentiate between individual checklist items. The format will look like this: **Checklist Item Title (School Name).**

#### Example

If you use “Unofficial Transcript” as your item title and the applicant lists two schools—**Element Senior High School** and **Element Community College**—the system will generate these checklist items:

* Unofficial Transcript (Element Senior High School)
* Unofficial Transcript (Element Community College)

📌 **Note:** The system generates a transcript row for each school associated with the applicant, including prior high schools, so a high school transcript row can appear even on a graduate application's transcript item. The **Works For** setting controls which applications the checklist item appears on, but it does not limit which schools generate rows. To collect only specific transcripts (for example, college transcripts only), use a **Custom** or **Condition** checklist item in place of the Transcript type.

## Supplemental Form

Supplemental Form checklist items are specifically designed to track supplemental forms required from applicants. This type streamlines checklist management by automatically marking the item as complete when the form is submitted. **Important:** Only one supplemental form checklist item should be added per application, regardless of the number of forms required. The system will automatically handle multiple forms. See [Applications with Multiple Supplemental Forms](#h_485a743452) for more details.

**Purpose:** Use this type to efficiently manage and track the submission of additional forms, such as residency verifications, enrollment agreements, or other required documents.

**How It Works:** The item is automatically marked complete once the student submits the supplemental form.

### 🚨 Important: Applications with Multiple Supplemental Forms

Managing multiple supplemental forms on an application is simple with the system's automated process. Here's what you need to know:

#### Add Only One Checklist Item

Add a single supplemental form checklist item to each application, regardless of the number of forms required. The system will automatically create separate checklist items for each form attached to the application.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259687812/5d920d9380dea0dc3ca815491a22/supp+forms+-+apps.png?expires=1784397600&signature=2032a9bb422458eec9d8115860560b0274b0a58528da04343e8917dddd420380&req=dSIiH892moleW%2FMW3nq%2BgathUs7ssdUl8RodA738GJSxuRkPjmdOO7zUfG4J%0AE0TFvG01bfrw%2B8PwF4dC9qzuCXI%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259687812/5d920d9380dea0dc3ca815491a22/supp+forms+-+apps.png?expires=1784397600&signature=2032a9bb422458eec9d8115860560b0274b0a58528da04343e8917dddd420380&req=dSIiH892moleW%2FMW3nq%2BgathUs7ssdUl8RodA738GJSxuRkPjmdOO7zUfG4J%0AE0TFvG01bfrw%2B8PwF4dC9qzuCXI%3D)

#### Use a Generic Title

For the supplemental form checklist item, choose a generic title like “Supplemental Form.” This is important because the system automatically appends the form name in parentheses to differentiate each checklist item in the format: **Checklist Item Title (Form Name).**

#### Example

If you use “Supplemental Form” as your item title and the applicant has two forms attached to their application—**Parent/Guardian Info** and **Residency Verification**—the system will generate these checklist items:

* Supplemental Form (Parent/Guardian Info)
* Supplemental Form (Residency Verification)

#### Important to Note

If you mark the supplemental form checklist item as required and multiple forms are attached, all forms will be marked as required. Be sure this aligns with your application process.

#### Need More Help?

For a step-by-step guide on adding the Supplemental Form checklist item type, watch our video tutorial below:  
​

## One-Off

One-Off checklist items are designed for unique situations where you need to manually add an item to a student's checklist. Unlike other types, these items are not automatically populated and require manual oversight.

**Purpose:** Use this type for individual, non-standard requirements that do not fit into other predefined checklist categories, such as specific residency verifications or fee waivers.

**How It Works:**

* After creating and enabling the checklist item, you can manually add it to a student's checklist **through their decision**.
* The status of a One-Off checklist item must be manually marked as complete by an internal user.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259741252/b48a8220a787b0877cd4edbf089d/one+off.png?expires=1784397600&signature=14bc241c75f0a3d41334e13f495efac953cf5ad6ee68f12835784015a10abd76&req=dSIiH856nINaW%2FMW3nq%2BgbLAynM9kgNn2ag8PTKxs%2B5bNgI%2FJU%2F1pWW35s4g%0ARGOVjZolwHyXQAsvuUFa8odWXT4%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259741252/b48a8220a787b0877cd4edbf089d/one+off.png?expires=1784397600&signature=14bc241c75f0a3d41334e13f495efac953cf5ad6ee68f12835784015a10abd76&req=dSIiH856nINaW%2FMW3nq%2BgbLAynM9kgNn2ag8PTKxs%2B5bNgI%2FJU%2F1pWW35s4g%0ARGOVjZolwHyXQAsvuUFa8odWXT4%3D)

**Example**: You might use a One-Off checklist item to request additional documentation from a student for a unique situation, such as verifying eligibility for a fee waiver or resolving a special residency requirement.

---

# Post-Admit Setting

Enable the “Post-Admit” setting to keep specific checklist items visible **after** a student is admitted. This is useful for collecting post-admission documents, such as final transcripts, immunization records, or enrollment forms.

When enabled, these items will remain on the checklist card post-admit. All other items without this setting will disappear once a decision is released, even if they're incomplete or waived.

📌 ***Note****: When the checklist is first generated, it displays **all items** attached to the decision, regardless of the post-admit setting. The filtering only takes effect after the student is admitted.*

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259737762/e1e0baa8c53c033b1f9165543ca3/post+admit+toggle.png?expires=1784397600&signature=49aab6be6144894b733ff3e7730e80bd81f4a6dfb0b98e71b3f09048634a99cc&req=dSIiH859moZZW%2FMW3nq%2BgXgsLLkPrWYaTDwoGCp%2BN7YayIuGL%2BaPKEFzphu%2B%0AjfeO65yGrjnfDyuToyJa31OlEmQ%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259737762/e1e0baa8c53c033b1f9165543ca3/post+admit+toggle.png?expires=1784397600&signature=49aab6be6144894b733ff3e7730e80bd81f4a6dfb0b98e71b3f09048634a99cc&req=dSIiH859moZZW%2FMW3nq%2BgXgsLLkPrWYaTDwoGCp%2BN7YayIuGL%2BaPKEFzphu%2B%0AjfeO65yGrjnfDyuToyJa31OlEmQ%3D)

---

# Manually Updating Checklist Item Status

To update the status of a checklist item, navigate to the **Checklist** tab of the student's **Decision.** Use the **Status** dropdown to select one of the following options: *not completed*, *received*, *completed*, or *waived*.

* **Not Completed** — the item has not yet been fulfilled.
* **Received** — materials have arrived, but review or processing is still in progress. Use this when you want to acknowledge receipt without implying the requirement is finished.
* **Completed** — the item has been fulfilled and review is finished.
* **Waived** — the requirement no longer applies for this applicant.

## 🚨 Important: Condition + Supplemental Checklist Items

* Condition and Supplemental Form checklist items cannot be manually set back to **Not Completed** once the system has automatically marked them as **Completed** or **Waived**.
* When the system marks an item as **Completed** or **Waived**, it stops evaluating it, and the status will not change, even if the original conditions are no longer met.
* For Condition items, remember that **completion conditions take precedence**: if both **Mark Complete When…** and **Mark Waived When…** conditions are met, the item is marked **Complete**.
* For more flexibility in manually updating statuses, consider using the **Custom** or **One-Off** checklist item types.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259716686/0ce8e4c377842eca708acbabc048/checklist+tab.png?expires=1784397600&signature=a3c81d61101a0d47f5afccb406baabd4c9a2240fe507c65d0b74f685a9228f13&req=dSIiH85%2Fm4dXX%2FMW3nq%2BgcUBPq76S2dCA3p9K0oz30%2Fp2rmTxFw6GiF7nx8D%0A9b970ByI9PdnWeDB3WMUNnU6xN0%3D)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1259716686/0ce8e4c377842eca708acbabc048/checklist+tab.png?expires=1784397600&signature=a3c81d61101a0d47f5afccb406baabd4c9a2240fe507c65d0b74f685a9228f13&req=dSIiH85%2Fm4dXX%2FMW3nq%2BgcUBPq76S2dCA3p9K0oz30%2Fp2rmTxFw6GiF7nx8D%0A9b970ByI9PdnWeDB3WMUNnU6xN0%3D)

---

# Using Checklist Filters in Segments

Checklist filters allow you to build a [segment](https://intercom.help/element451/en/articles/1474191-segments-overview) of contacts based on a specific checklist or checklist items that meet your needs. Whether you're identifying students who've completed their application requirements or targeting those missing key documents, these filters give you the flexibility to find the right group. For example, you might use these filters to send a campaign to encourage next steps or celebrate milestones.

* **Checklist Status:** Use this filter to identify whether the entire checklist is marked as completed (completed = true) or not (completed = false).
* **Checklist Completed:** This filter focuses on completed checklists, allowing you to narrow results further by scoping to properties such as application, term, or degree.
* **Checklist Item:** Filter by an individual checklist item and its status (e.g., completed or incomplete). You can also scope by specific items to refine your results further.
* **Updated Checklist Item:** Filter by individual checklist items with more advanced scoping options, such as item type, new checklist item status, or related properties like application or term.

---