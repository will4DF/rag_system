---
title: Bolt App Reader Agent
url: https://help.element451.com/en/articles/10697700-bolt-app-reader-agent
collection: Bolt AI
---

# Overview

The Bolt App Reader Agent is a powerful tool built into the Decisions module that helps streamline your application review process. It acts as the "first reader" of an application, analyzing submitted materials and scoring the decision based on your defined [criteria](https://help.element451.com/en/articles/9210619-decisions-criteria) and AI instructions. This ensures a fast, consistent, and objective first review, allowing your admissions team to focus on engaging with applicants rather than getting bogged down in manual evaluations.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1469642793/c751e021e5e16641d83832503b0a/Bolt+App+Reader+Agent+-+HC+Graphic.png?expires=1784333700&signature=4eae167068fec4b05e3c297be18b2f6d623cc0e689b430de5e15dac0274b9ab1&req=dSQhH896n4ZWWvMW1HO4zbBXYvD65zSQlXz76fVbKS6gC1X%2BCE8KltHP4SKX%0AheDTdUMrEbEFJksgsF0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1469642793/c751e021e5e16641d83832503b0a/Bolt+App+Reader+Agent+-+HC+Graphic.png?expires=1784333700&signature=4eae167068fec4b05e3c297be18b2f6d623cc0e689b430de5e15dac0274b9ab1&req=dSQhH896n4ZWWvMW1HO4zbBXYvD65zSQlXz76fVbKS6gC1X%2BCE8KltHP4SKX%0AheDTdUMrEbEFJksgsF0%3D%0A)

---

# Enabling + Setting Up the Agent

Before the Bolt App Reader Agent can evaluate applications, you must add [AI Instructions](https://help.element451.com/en/articles/10697700-bolt-app-reader-agent) to at least one decision criterion you wish to evaluate.

Important: Changes to Criteria settings, including AI instructions, do not automatically alter previously scored applications. They apply to new decisions and to any existing decision that you manually re-run after the change.

## Configuring Decision Stages

You can enable the agent for specific stage(s) in your Decision Board. You can enable Bolt App Reader Agent for as many stages as you’d like. However, we recommend configuring your Decision Board so the agent reviews each application only once. If no stage is set, App Reader Agent will evaluate on application submission.

1. Go to **Applications** > **Decisions** > **Decision** **Settings**.
2. Click the **Board** tab.
3. Find the stage where you want to enable the reader agent.
4. Click the three horizontal dots icon in the top-right corner of the stage card.
5. Select **Enable AI** **App** **Reader**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471150501/6789c125b8e732a2e1231cfeeaf8/Reader+Agent+-+Enable+AI+App+Reader.png?expires=1784333700&signature=9516f593f46b723c170979cb2097b952dbee3c98d1657a19a236b73e30c60763&req=dSQgF8h7nYRfWPMW1HO4zVeRsPHPPBv%2FacaUgyVSP0ppz6f7AWWVlsTefRhZ%0Ak3sh%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471150501/6789c125b8e732a2e1231cfeeaf8/Reader+Agent+-+Enable+AI+App+Reader.png?expires=1784333700&signature=9516f593f46b723c170979cb2097b952dbee3c98d1657a19a236b73e30c60763&req=dSQgF8h7nYRfWPMW1HO4zVeRsPHPPBv%2FacaUgyVSP0ppz6f7AWWVlsTefRhZ%0Ak3sh%0A)
6. An orange lightning bolt icon will appear on enabled stage cards.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471147484/f0805192b6111913319191cb64a6/Reader+Agent+-+Board+Stages.png?expires=1784333700&signature=7a9b4fd31ad9b0f9a85917c5b29cdc3133d05cf21adbed64e966f415df5dcd78&req=dSQgF8h6moVXXfMW1HO4zW0Vuj4WkJ%2Ftn2jOsAca5uLyN7uPTG706CFNqesH%0AAdcc%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471147484/f0805192b6111913319191cb64a6/Reader+Agent+-+Board+Stages.png?expires=1784333700&signature=7a9b4fd31ad9b0f9a85917c5b29cdc3133d05cf21adbed64e966f415df5dcd78&req=dSQgF8h6moVXXfMW1HO4zW0Vuj4WkJ%2Ftn2jOsAca5uLyN7uPTG706CFNqesH%0AAdcc%0A)

## Adding AI Instructions

For the agent to evaluate a criterion, you must provide AI instructions:

1. Go to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click the **Criteria** tab.
3. Find and edit the criteria you want the agent to evaluate.
4. Go to the **General** tab in the **Edit** **Criteria** side panel.
5. Locate **AI** **Instructions** and enter specific guidance. Be clear and specific with your AI Instruction. Think of them as directions you'd give to a human reviewer to ensure consistency in scoring.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471153226/2d5e88b3a65650ac53a4ecf255dc/Reader+Agent+-+AI+Instructions.png?expires=1784333700&signature=d01ca9eb01b209a40e82c8b7a4c96c0d5c1e955915313e19927b63fc334618d8&req=dSQgF8h7noNdX%2FMW1HO4zWnNCFPT3ltTCVhO6X0krGgI96fGesKUXpNtjZpe%0AWL2a%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471153226/2d5e88b3a65650ac53a4ecf255dc/Reader+Agent+-+AI+Instructions.png?expires=1784333700&signature=d01ca9eb01b209a40e82c8b7a4c96c0d5c1e955915313e19927b63fc334618d8&req=dSQgF8h7noNdX%2FMW1HO4zWnNCFPT3ltTCVhO6X0krGgI96fGesKUXpNtjZpe%0AWL2a%0A)
6. Repeat for each criteria item as needed.
7. Once AI instructions are added to a criterion, a Bolt AI icon will automatically appear next to that row in the Criteria table, giving you a quick visual indicator of where AI guidance is applied.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1569474629/4381ca3bd437e9aa18547949df0b/CleanShot+2025-06-13+at+08_45_08.png?expires=1784333700&signature=c7d301cc17ad9148e5a4cc3682a118d8edb6d2f8d7de90eda63ce3dabc55a290&req=dSUhH815mYddUPMW1HO4zd4WDx9eJvajy%2Fb5pIniIVe34W8OnsjO5XIoMtxD%0AIhv9%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1569474629/4381ca3bd437e9aa18547949df0b/CleanShot+2025-06-13+at+08_45_08.png?expires=1784333700&signature=c7d301cc17ad9148e5a4cc3682a118d8edb6d2f8d7de90eda63ce3dabc55a290&req=dSUhH815mYddUPMW1HO4zd4WDx9eJvajy%2Fb5pIniIVe34W8OnsjO5XIoMtxD%0AIhv9%0A)

🚨 **Important**: The Bolt App Reader Agent will not score a criterion if AI instructions are not provided. If no criterion has AI instructions, the agent will skip that Decision.

## Writing Strong AI Instructions + Examples

AI instructions are critical to how the Application Reader interprets and scores each application. Poorly written or vague instructions can result in unexpected outcomes, like students being marked “Unqualified” despite strong records. Here’s how to write effective instructions:

* **Be Clear and Specific**

  + Use direct, plain language.
  + Focus on what matters mos**t** in the application for that criterion (e.g., GPA thresholds, coursework type, leadership roles).
  + Avoid vague terms like “strong background” unless you define what that means.
* **Use Examples When Possible**

  + Provide examples of both strong and weak application elements for context.
  + Example: *“Strong performance in math includes AP Calculus with a grade of B or better, or a SAT Math score over 650."*
* **Address Common Misunderstandings**

  + AI can’t “guess” your intention—be explicit.
  + Avoid relying solely on human judgment phrases like “good fit” or “leadership potential” unless you define what qualifies.

### Example

For *Academic Performance*, you might provide the following instructions:

```
Review the applicant’s GPA and transcript, comparing their academic record to the institution’s average admitted GPA of 3.2. Pay close attention to the difficulty of coursework, including AP, IB, honors, or other advanced-level classes, and note any academic trends—such as consistent performance or an upward trajectory over time.  
  
When scoring: assign a 7–10 to students with a GPA of 3.5 or higher who have completed at least three AP or honors courses. Students without any AP or honors coursework should receive no higher than a 5, regardless of GPA. Applicants with a GPA between 2.5 and 2.99 should receive a 2–3, while those with an overall GPA below 2.0 should receive a score of 1, regardless of course rigor.
```

This detailed guidance helps the agent evaluate applications consistently with your institution's specific admissions priorities.

## Best Practices

* Review each AI instruction carefully before deploying.
* Involve team members who understand the academic or admissions context when writing instructions.
* Revisit and revise instructions regularly, especially if you’re seeing unexpected decision outcomes.

---

# The Evaluation + Scoring Process

Once configured, the Bolt App Reader Agent evaluates applications using a systematic approach. This section explains how the agent analyzes application materials, what settings it uses from your criteria configuration, how it handles documents and cross-checks information, and the categorical scoring system it uses to classify applications.

## How Applications Are Scored

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471372639/7c7223e767571ec51677ef5c3996/Evaluation%2BChip.png?expires=1784333700&signature=6df993cc05ba096d63955450e43d84936374acca13730eb440171961d7d44a46&req=dSQgF8p5n4dcUPMW1HO4zcR50Vz6hMVIGDE1kuz4DonB8QztoMl%2FSmWbqp5b%0A5WS%2FdqO2nFQDI%2BsUSPQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471372639/7c7223e767571ec51677ef5c3996/Evaluation%2BChip.png?expires=1784333700&signature=6df993cc05ba096d63955450e43d84936374acca13730eb440171961d7d44a46&req=dSQgF8p5n4dcUPMW1HO4zcR50Vz6hMVIGDE1kuz4DonB8QztoMl%2FSmWbqp5b%0A5WS%2FdqO2nFQDI%2BsUSPQ%3D%0A)

1. When an application reaches a stage where the Bolt App Reader Agent is enabled, it automatically activates and begins its evaluation process.
2. The agent reviews the application and all associated documents.
3. It evaluates each [criterion](https://help.element451.com/en/articles/9210619-decisions-criteria) for which you've provided AI instructions.
4. It assigns numerical scores to each criterion based on your max score settings.
5. It determines an overall categorical rating for the application.

**Important**: Unlike human reviewers, the Bolt App Reader Agent's scores do not contribute to the application's overall calculated score. This means:

* When only the agent has evaluated a decision, the overall score will still show 0.
* Settings like aggregate weight, score type, etc., do not apply to the agent's evaluation.
* The agent provides a categorical overall assessment instead (Highly Qualified, Qualified, etc.).

### Imported Applications

If you’re importing application data from another system into Element451 and creating a Decision [via a rule](https://help.element451.com/en/articles/9007767-importing-application-data?q=app+reader#h_04259716ff), the Application Reader Agent will follow the same process as it does for applications submitted directly in Element451, triggering at the stage(s) where the reader is enabled.

## Document Analysis + Cross-Checks

As part of the evaluation process, the agent:

* Identifies and analyzes relevant application documents for each criterion (transcripts, essays, resumes, etc.).
* The agent performs cross-reference checks to verify consistency across documents and flags inconsistencies that might impact scoring (like mismatched personal information). Where significant inconsistencies are detected, the agent will skip evaluating that criterion.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471162432/784b1e24b93a6c16a4712223360d/Reader+Agent+-+Cross+Check.png?expires=1784333700&signature=b0685db1384b18770366edb3f246d098be608c078af4d58132aa78450b11ff24&req=dSQgF8h4n4VcW%2FMW1HO4zRMQPcepEJxoikIqoLBw96xfBrtOvIQCFzUjMR3P%0Alxm1%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471162432/784b1e24b93a6c16a4712223360d/Reader+Agent+-+Cross+Check.png?expires=1784333700&signature=b0685db1384b18770366edb3f246d098be608c078af4d58132aa78450b11ff24&req=dSQgF8h4n4VcW%2FMW1HO4zRMQPcepEJxoikIqoLBw96xfBrtOvIQCFzUjMR3P%0Alxm1%0A)

The agent's thoroughness helps catch discrepancies that might be missed in a manual review, ensuring that scores are based on reliable information.

## Scoring System + Decision Categories

The Bolt App Reader Agent classifies applications into five categories:

* Highly Qualified
* Qualified
* Neutral
* Unqualified
* Highly Unqualified

These categories provide a quick assessment of an application's overall strength based on your institution's specific criteria and standards.

---

# Viewing & Using AI Analysis

The agent's evaluation results are integrated throughout the Decisions module interface. This section shows you where to find AI analysis results, how to interpret the different components of the analysis sidebar, and how to use the interactive document features to verify and understand the agent's assessment.

## Access Points

Here are the methods by which you can access the Bolt App Reader Agent's analysis:

1. **All Decisions Table**: Quickly scan the Bolt Analysis column for a high-level view of the agent’s score. To explore full analysis details, open the decision and use one of the other methods listed below (2–3).

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471167225/d339f8ec3eccb554da94ceb644f7/Reader+Agent+-+Decisions+Table.png?expires=1784333700&signature=920c3300dfe6a311c57b1e385be5943b08c450cce51c818ec66ad1fab5a405e5&req=dSQgF8h4moNdXPMW1HO4ze38Co%2BY8hvR1%2Bn%2BwCgyZpvsaSn36akxxq1PaT0a%0A7dQ5%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471167225/d339f8ec3eccb554da94ceb644f7/Reader+Agent+-+Decisions+Table.png?expires=1784333700&signature=920c3300dfe6a311c57b1e385be5943b08c450cce51c818ec66ad1fab5a405e5&req=dSQgF8h4moNdXPMW1HO4ze38Co%2BY8hvR1%2Bn%2BwCgyZpvsaSn36akxxq1PaT0a%0A7dQ5%0A)
2. **Decision Header:** Ideal for quickly reviewing the agent’s evaluation without leaving your current view. **Click the AI Analysis chip** in the decision header to open a side panel with the agent’s full reasoning and criterion-level scores.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471186876/62c7af98afe098df6b03e6b70517/Reader+Agent+-+Overall+Category.png?expires=1784333700&signature=711fd7ca06c0533eb7aac3643d6ca56764c6c4db52b0fe28e1ea8833cb867fea&req=dSQgF8h2m4lYX%2FMW1HO4ze2hpn44pVRB0bSLLol5eu9HVcXGbd%2FeW1%2F5WzJD%0AWuaS%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471186876/62c7af98afe098df6b03e6b70517/Reader+Agent+-+Overall+Category.png?expires=1784333700&signature=711fd7ca06c0533eb7aac3643d6ca56764c6c4db52b0fe28e1ea8833cb867fea&req=dSQgF8h2m4lYX%2FMW1HO4ze2hpn44pVRB0bSLLol5eu9HVcXGbd%2FeW1%2F5WzJD%0AWuaS%0A)
3. **Human Review View (Criteria Tab or Application Reader):** Use this method when scoring an application or reviewing human scores. The agent’s analysis appears alongside human input, offering numerical scores and reasoning for each criterion.  
   ​

   * **Criteria Tab:** Use this when scoring an application yourself or reviewing human scores. The agent’s numerical score and reasoning for each criterion appear under the “Bolt Application Reader Score” section.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471191002/4961747490d7ac5e02c98b92f874/Reader+Agent+-+Criteria+Tab.png?expires=1784333700&signature=c16b95b3622eab63e11d8d35fb1c45e9c9db50f705c6545c4f5490a57f08cd31&req=dSQgF8h3nIFfW%2FMW1HO4zTWLCZpM%2Bm%2FjKzzBZh9bm0Zqb9Tohwl3nLUxu4t7%0AX%2FE4%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471191002/4961747490d7ac5e02c98b92f874/Reader+Agent+-+Criteria+Tab.png?expires=1784333700&signature=c16b95b3622eab63e11d8d35fb1c45e9c9db50f705c6545c4f5490a57f08cd31&req=dSQgF8h3nIFfW%2FMW1HO4zTWLCZpM%2Bm%2FjKzzBZh9bm0Zqb9Tohwl3nLUxu4t7%0AX%2FE4%0A)
   * **Application Reader Interface:** Use this view when you want a snapshot of the agent’s evaluation alongside other application information. Shows the agent’s overall score and summary only.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471196905/0cba7eb178cc893c4e585127398f/CleanShot+2025-04-11+at+12_45_18.png?expires=1784333700&signature=f5de4bae68f607dc0da91d91d6e1eb107bcc0eb1d2b7125c4dfab0cc168fdbca&req=dSQgF8h3m4hfXPMW1HO4zfU%2B8ZNIkeUZfhXcKNyoo3OX4edy1JLCXCeZYgx5%0AcYhT%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471196905/0cba7eb178cc893c4e585127398f/CleanShot+2025-04-11+at+12_45_18.png?expires=1784333700&signature=f5de4bae68f607dc0da91d91d6e1eb107bcc0eb1d2b7125c4dfab0cc168fdbca&req=dSQgF8h3m4hfXPMW1HO4zfU%2B8ZNIkeUZfhXcKNyoo3OX4edy1JLCXCeZYgx5%0AcYhT%0A)

## Understanding the AI Analysis Sidebar

When you access the AI Analysis Sidebar, you'll find two tabs: "Review and Reasoning" and "Feedback."

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471374693/3cde2cdc043d319d567a8bfe237f/Reader%2BAgent%2B-%2BTwo%2BTabs.png?expires=1784333700&signature=ed232561b338def954ed6e0c219d5280d45bf54ad256e33f15c1c4c1de4f3f1f&req=dSQgF8p5mYdWWvMW1HO4zXScWZCl%2FN055YJ%2FD%2Fdq%2FuwDV7o%2Byp3fQ%2BVCDn7G%0ArnAtKcJnOf8uzGxBBnY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471374693/3cde2cdc043d319d567a8bfe237f/Reader%2BAgent%2B-%2BTwo%2BTabs.png?expires=1784333700&signature=ed232561b338def954ed6e0c219d5280d45bf54ad256e33f15c1c4c1de4f3f1f&req=dSQgF8p5mYdWWvMW1HO4zXScWZCl%2FN055YJ%2FD%2Fdq%2FuwDV7o%2Byp3fQ%2BVCDn7G%0ArnAtKcJnOf8uzGxBBnY%3D%0A)

### Review Tab

* Overall summary and categorical score at the top

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471202479/f4e0717cd5eb07df891914a8d953/Reader+Agent+-+Review+-+General+Section.png?expires=1784333700&signature=aef269616692ed9d2c39662739fdb8a1fdd3b8f5a365102e453781e929526e51&req=dSQgF8t%2Bn4VYUPMW1HO4zRjmyuV3UTdESML5efVpcKQcEdODufz%2FRFsXQk8E%0Aa43C%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471202479/f4e0717cd5eb07df891914a8d953/Reader+Agent+-+Review+-+General+Section.png?expires=1784333700&signature=aef269616692ed9d2c39662739fdb8a1fdd3b8f5a365102e453781e929526e51&req=dSQgF8t%2Bn4VYUPMW1HO4zRjmyuV3UTdESML5efVpcKQcEdODufz%2FRFsXQk8E%0Aa43C%0A)
* Breakdown for each evaluation criterion with individual scores and summaries

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471204047/d2bda0828698a51b797ad0b9baf2/Reader+Agent+-+Review+-+Individual+Scores.png?expires=1784333700&signature=66a3b33e18b22811ef75d6b0b363a65853e603b0322fd80ea20dcd6bb7de940c&req=dSQgF8t%2BmYFbXvMW1HO4zac4RlwbBSUCVCpJ8LQZIh6fC1FR3vero0uSw3fh%0AXb8l%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471204047/d2bda0828698a51b797ad0b9baf2/Reader+Agent+-+Review+-+Individual+Scores.png?expires=1784333700&signature=66a3b33e18b22811ef75d6b0b363a65853e603b0322fd80ea20dcd6bb7de940c&req=dSQgF8t%2BmYFbXvMW1HO4zac4RlwbBSUCVCpJ8LQZIh6fC1FR3vero0uSw3fh%0AXb8l%0A)

### Reasoning & Feedback Tab

This tab provides a comprehensive history of all evaluation activity, including initial assessments, re-runs, and feedback requests. It shows:

* The complete evaluation flow and reasoning process.
* To see the detailed process, expand the "Reasoning" header.
* Explanation of which documents were read and analyzed.
* Clickable document chips that open referenced materials for quick review.
* The agent's opinion/evaluation summary for each criterion with assigned scores.

**When re-runs are initiated:**

* If feedback is tied to a specific criterion, the agent only re-evaluates that criterion and updates its score and summary.
* The final section always displays the most current evaluations from all previous runs, providing a comprehensive "final decision" view.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471358197/c8bb4a2d2a0bfab030853ac70ce4/Reader%2BAgent%2B-%2BReasoning%2BExpanded.png?expires=1784333700&signature=7df749a11d75c699ce501447038d03ea3217fab3ecdb059d49eb282ac314a781&req=dSQgF8p7lYBWXvMW1HO4zXMtFJW%2FDkVIDuZXS2VpnOUxR322SSgbGidC7dip%0AmCJz6FUZ2rRjyrWReqU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471358197/c8bb4a2d2a0bfab030853ac70ce4/Reader%2BAgent%2B-%2BReasoning%2BExpanded.png?expires=1784333700&signature=7df749a11d75c699ce501447038d03ea3217fab3ecdb059d49eb282ac314a781&req=dSQgF8p7lYBWXvMW1HO4zXMtFJW%2FDkVIDuZXS2VpnOUxR322SSgbGidC7dip%0AmCJz6FUZ2rRjyrWReqU%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471369916/c67a761799991a12c0e5373544ed/Reader+Agent+-+Opinion+and+Final+Summary.png?expires=1784333700&signature=c6b6b89eb95509c598772d84313ea9f7e55145892514ce4265a04abbd30fde43&req=dSQgF8p4lIheX%2FMW1HO4zSYGGLqB9qq4SdIezm%2FRv3bMo%2B95sUv4WwizKpvS%0A7nKgwIYu3rA4dWyw4ek%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471369916/c67a761799991a12c0e5373544ed/Reader+Agent+-+Opinion+and+Final+Summary.png?expires=1784333700&signature=c6b6b89eb95509c598772d84313ea9f7e55145892514ce4265a04abbd30fde43&req=dSQgF8p4lIheX%2FMW1HO4zSYGGLqB9qq4SdIezm%2FRv3bMo%2B95sUv4WwizKpvS%0A7nKgwIYu3rA4dWyw4ek%3D%0A)

## Document References + Viewing

The Bolt App Reader Agent provides clickable document chips that let you quickly verify its assessment by seeing exactly what it used when scoring:

* **Clickable Document Chips:** Documents referenced in the analysis appear as clickable chips.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471397445/2b40454c8d6a171fcc2fd4b04326/Reader+Agent+-+Reading+Documents.png?expires=1784333700&signature=7310c94f9d9b05470f16c05bd2563c9d83fd815f66346fb7cb26eab96e0cc4bf&req=dSQgF8p3moVbXPMW1HO4zVpgNpjAf5BsBt28tMwGfxiC1d60btltfvdJpg3a%0AuN8X%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471397445/2b40454c8d6a171fcc2fd4b04326/Reader+Agent+-+Reading+Documents.png?expires=1784333700&signature=7310c94f9d9b05470f16c05bd2563c9d83fd815f66346fb7cb26eab96e0cc4bf&req=dSQgF8p3moVbXPMW1HO4zVpgNpjAf5BsBt28tMwGfxiC1d60btltfvdJpg3a%0AuN8X%0A)
* **Contextual Document Viewing:** Clicking a chip opens the document in a side panel, keeping you in context.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471396769/4e47d35b5fb13e54222c6da42fc6/CleanShot-2B2025-04-11-2Bat-2B14_33_30.png?expires=1784333700&signature=25f74e3bad32826a89510f517171d8c482919e2600be0439aba851265ae48b69&req=dSQgF8p3m4ZZUPMW1HO4zTaUm0tiG3Obn3mADXeNNSqtBNfaCrkUHggIJ%2BSL%0ASisL%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471396769/4e47d35b5fb13e54222c6da42fc6/CleanShot-2B2025-04-11-2Bat-2B14_33_30.png?expires=1784333700&signature=25f74e3bad32826a89510f517171d8c482919e2600be0439aba851265ae48b69&req=dSQgF8p3m4ZZUPMW1HO4zTaUm0tiG3Obn3mADXeNNSqtBNfaCrkUHggIJ%2BSL%0ASisL%0A)
* **Cross-Check Warnings:** The agent clearly explains any inconsistencies it detected across documents.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471398034/be24e31ec7431621cdfdf0ff50c7/Reader+Agent+-+Cross+Check.png?expires=1784333700&signature=fc2648764af013b266404f0a4bb1ea4e9e8e34140486fadfe583e07f65aa800f&req=dSQgF8p3lYFcXfMW1HO4zcaSRXgtswcKVSCVdolkf%2Byxep6iAtx86jAHjPVw%0AyM%2Fv%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471398034/be24e31ec7431621cdfdf0ff50c7/Reader+Agent+-+Cross+Check.png?expires=1784333700&signature=fc2648764af013b266404f0a4bb1ea4e9e8e34140486fadfe583e07f65aa800f&req=dSQgF8p3lYFcXfMW1HO4zcaSRXgtswcKVSCVdolkf%2Byxep6iAtx86jAHjPVw%0AyM%2Fv%0A)

---

# Providing Feedback + Re-Running Evaluations

The Bolt App Reader Agent is designed to work collaboratively with your admissions team. This section covers how to enhance the AI evaluation with your expertise through feedback, access the feedback feature, and initiate re-evaluations when application information changes or settings are updated.

## Feedback-Based Re-Evaluation

The feedback feature lets you enhance the agent's evaluation with expertise and contextual knowledge.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471406043/4a6ac2bf522033b445cfdf798997/Reader+Agent+-+Add+Your+Feedback.png?expires=1784333700&signature=90a11fd808d176027377199d78952ee5871397f2ade86c41dfb8986968722b5e&req=dSQgF81%2Bm4FbWvMW1HO4zUkFYKV9lVkToM1yYlq%2BkbZjjHlWOYCpup%2BSyM7Z%0AgZBsaGfdhtb1iYxWJGY%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471406043/4a6ac2bf522033b445cfdf798997/Reader+Agent+-+Add+Your+Feedback.png?expires=1784333700&signature=90a11fd808d176027377199d78952ee5871397f2ade86c41dfb8986968722b5e&req=dSQgF81%2Bm4FbWvMW1HO4zUkFYKV9lVkToM1yYlq%2BkbZjjHlWOYCpup%2BSyM7Z%0AgZBsaGfdhtb1iYxWJGY%3D%0A)

Use feedback when:

* You have additional information about an applicant not captured in their submitted documents.
* Special circumstances or contexts should be considered in the evaluation.
* Certain achievements or challenges need more weight in the assessment.
* You want to ensure consistency with your institution's holistic review approach.
* The agent may have missed nuanced elements in complex application materials.

Targeted feedback helps create a more comprehensive and accurate evaluation, combining AI efficiency and human insight.

## Where + How to Provide Feedback

### Accessing the Feedback Form

* **From the Decision Header:** Click the AI Analysis chip to open the sidebar, then navigate to the **Reasoning & Feedback** tab.

* **From the Criteria Tab:** When viewing a decision's criteria, each criterion has a feedback button that serves as a shortcut, opening the sidebar directly to the feedback area for that specific criterion.

### Providing Feedback

1. Select from the dropdown which context you want to provide feedback for:

   * Choose a specific criterion to provide feedback on that item.

     + Select "General" to provide overall feedback that doesn't pertain to a specific criterion.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471408639/38033e01d2b6c9e14ff0763abb95/Reader+Agent+-+Feedback+Select+Criteria+Context.png?expires=1784333700&signature=4ef2de50093c112dcef81684964c7ca64dc11f2326f4a49fe19ada4875d02ac5&req=dSQgF81%2BlYdcUPMW1HO4zYdv5hy%2Flcrif0GPhUKzWIQ%2F5ZWLaw0B6SORM6ye%0AHnRw%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1471408639/38033e01d2b6c9e14ff0763abb95/Reader+Agent+-+Feedback+Select+Criteria+Context.png?expires=1784333700&signature=4ef2de50093c112dcef81684964c7ca64dc11f2326f4a49fe19ada4875d02ac5&req=dSQgF81%2BlYdcUPMW1HO4zYdv5hy%2Flcrif0GPhUKzWIQ%2F5ZWLaw0B6SORM6ye%0AHnRw%0A)
2. Add your feedback or additional context.
3. Click "Submit" to initiate the re-run.
4. Repeat steps 1-3 for each criterion you want to provide feedback on.

## Manual Re-Runs

You may need to re-run an evaluation without providing feedback in several scenarios:

* When application information has been updated
* After changing the criteria settings (like max score values)
* When you want a fresh evaluation

To manually re-run an evaluation:

* **Full Application Re-Run:** Click the "Re-Run" button in the top right corner of the AI Analysis sidebar.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1477091760/d356c2031d624f77722794ed6f2d/Reader%2BAgent%2B-%2BRerun%2BButton.png?expires=1784333700&signature=dbaf748decd02a9a813eff1a9faf22b5286a41d2ee8de13cc68085259a58edaa&req=dSQgEcl3nIZZWfMW1HO4zcWN%2BrONjlxvxuVNtaJE4RE86k8CQYhjfRBL4NWc%0A5U0l%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1477091760/d356c2031d624f77722794ed6f2d/Reader%2BAgent%2B-%2BRerun%2BButton.png?expires=1784333700&signature=dbaf748decd02a9a813eff1a9faf22b5286a41d2ee8de13cc68085259a58edaa&req=dSQgEcl3nIZZWfMW1HO4zcWN%2BrONjlxvxuVNtaJE4RE86k8CQYhjfRBL4NWc%0A5U0l%0A)
* **Individual Criterion Re-Run:** From the Criteria tab of the decision, you can re-run the evaluation for a specific criterion (useful when you've only changed settings for that criterion).

---