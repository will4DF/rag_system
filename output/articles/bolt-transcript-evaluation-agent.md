---
title: Bolt Transcript Evaluation Agent
url: https://help.element451.com/en/articles/12639660-bolt-transcript-evaluation-agent
collection: Bolt AI
---

Automatically extract, analyze, and structure transcript data in seconds.

# Overview

The **Transcript Evaluation Agent** is an AI-powered feature that reads and processes uploaded high school and college transcripts. It automatically extracts structured academic data, summarizes key insights, and surfaces results directly within a student’s profile — all while linking back to the original document for context.

This agent is one of Element451’s **[AI Agents for Admissions](https://help.element451.com/en/articles/11610832-element-admissions-team)**, alongside the **[Application Reader Agent](https://help.element451.com/en/articles/10697700-bolt-app-reader-agent)** and **[Fraud Detection Agent](https://help.element451.com/en/articles/9927313-bolt-app-fraud-detector-agent)**, designed to help institutions evaluate applicants faster, more consistently, and with greater insight.

## Key Benefits

* **Speed:** Replace of manual transcript data entry and evaluation with instant AI evaluation.
* **Accuracy:** Standardizes GPA, course, and credit data across varied formats.
* **Insight:** Surfaces academic trends, rigor levels, and strengths at a glance. How It Works

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1819241268/c143a39a404d35f51f3f91c01753/Transcript+Eval+Gif_3gif.gif?expires=1784333700&signature=9273467f29cdda4637a0dafbbdb3e82dfc7607e52fdef631898a954d3d361c01&req=dSgmH8t6nINZUfMW1HO4zdIzb7RNKF4k75FC%2BaCQcw94JP7O5whgNcqWAJS0%0ALaTcedNLpyFMUC2r6HU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1819241268/c143a39a404d35f51f3f91c01753/Transcript+Eval+Gif_3gif.gif?expires=1784333700&signature=9273467f29cdda4637a0dafbbdb3e82dfc7607e52fdef631898a954d3d361c01&req=dSgmH8t6nINZUfMW1HO4zdIzb7RNKF4k75FC%2BaCQcw94JP7O5whgNcqWAJS0%0ALaTcedNLpyFMUC2r6HU%3D%0A)

---

# How it Works

🚨 **Important:** AI Transcript Evaluation only runs when the uploaded file is assigned a document type that has this setting enabled. If the document type isn’t enabled, no evaluation will occur.

1. **Enable AI Transcript Evaluation on a Document Type**

   * Internal users start by enabling **AI Transcript Evaluation** on the appropriate **Transcript Document Type**.
   * To access your document types, navigate to **Data + Automations** > **Documents** > **Document** **Types**.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1888614112/eda6a193e30dc4622e8ad5c8d8ee/CleanShot+2025-12-16+at+16_13_25.png?expires=1784333700&signature=3603199b631a5e853e95ea0068236b8385d496522ccc3fb25a36f7c8e9483872&req=dSgvHs9%2FmYBeW%2FMW1HO4zd8UOUeq1jGiuZHXHgCctjZsbm%2BBDBApKXAXIyuI%0A8ToS%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1888614112/eda6a193e30dc4622e8ad5c8d8ee/CleanShot+2025-12-16+at+16_13_25.png?expires=1784333700&signature=3603199b631a5e853e95ea0068236b8385d496522ccc3fb25a36f7c8e9483872&req=dSgvHs9%2FmYBeW%2FMW1HO4zd8UOUeq1jGiuZHXHgCctjZsbm%2BBDBApKXAXIyuI%0A8ToS%0A)
2. **Upload a Transcript (Student or Admin)**

   * **Student Uploads**: When a student uploads a transcript to a field (such as on an application), the evaluation automatically runs **if the document type assigned to that field has AI Transcript Evaluation enabled**. No additional action is required.
   * **Admin Uploads (Internal Users)**: When you upload a file to the **Transcript field** on a student’s **School Profile card**, you’ll be prompted to select a **Transcript Document Type**. To trigger the evaluation, be sure to select a document type with **AI Transcript Evaluation enabled**.
   * 📌 **Note:** The evaluation is triggered at the time of upload or when the document type is changed to an enabled transcript type.
3. **Automatic Processing**

   * Once uploaded, the Bolt Transcript Evaluation agent:

     + Detects whether the transcript is **high school** or **college**
     + Extracts structured transcript data automatically
   * No additional configuration or manual setup is required.  
     ​
4. **Review Results in the Student Profile**

   * Evaluation results appear in the **Transcript Evaluations** card on the student’s profile. From there, staff can:

     + View summary insights
     + Open a detailed evaluation sidebar
     + Navigate directly to the source transcript file  
       ​
5. **Export Transcript Data (Optional)**

   * All structured transcript data is available for export using **Transcript Data Mappings** in **Import + Export**, making it easy to integrate transcript insights into downstream workflows.

# What Data is Extracted?

## High School Transcripts

### Overview

* Institution name, address, and codes
* Transcript Date
* Graduation Date
* Academic Overview

  + Trends
  + Strengths
  + Weaknesses
  + Rigor
* [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1827230814/822623a762dbb3ddb625ade22700/HS-Overview.png?expires=1784333700&signature=932575f3fe54f45ef38456f310e2df9265b5d0eaf55f68199e49abd0ef80b4c6&req=dSglEct9nYleXfMW1HO4zQWIDjRmYbhplgYGzZZzAVS4mZpI2ngCbJBUnNpe%0A4G7X%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1827230814/822623a762dbb3ddb625ade22700/HS-Overview.png?expires=1784333700&signature=932575f3fe54f45ef38456f310e2df9265b5d0eaf55f68199e49abd0ef80b4c6&req=dSglEct9nYleXfMW1HO4zQWIDjRmYbhplgYGzZZzAVS4mZpI2ngCbJBUnNpe%0A4G7X%0A)

### GPA and Class Rank info

* Class rank (rank, percentile, decile)
* Credits Completed
* Reported Weighted & Unweighted GPAs (When available)
* Converted Weighted & Unweighted GPA to 4.0 scale (When available)

## Courses

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1827283095/cab22c72c74240e32e11d084f655/HS-Courses.png?expires=1784333700&signature=b119ebffddf39364abb47d9463fffd029d254344216573a9451d2519a19cf697&req=dSglEct2noFWXPMW1HO4zQsb9fGdSjXqnFQKYS3ULPnrDqLqeA6ulvZ3JsrE%0AvCp9PiTaHQmd%2Fjz0gik%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1827283095/cab22c72c74240e32e11d084f655/HS-Courses.png?expires=1784333700&signature=b119ebffddf39364abb47d9463fffd029d254344216573a9451d2519a19cf697&req=dSglEct2noFWXPMW1HO4zQsb9fGdSjXqnFQKYS3ULPnrDqLqeA6ulvZ3JsrE%0AvCp9PiTaHQmd%2Fjz0gik%3D%0A)

* Course List

  + Academic Year / Term
  + Course Name
  + Subject Area

    - Sciences
    - Arts
    - English & Language Arts
    - History & Social Sciences
    - Mathematics
    - World Langue & Culture
    - Technology & Computer Science
    - Business
    - PE & Health
    - Electives/Others

  + Credits
  + Reported Grade
  + Recalculated Grade to 4.0 Scale
* Course Level Totals

  + AP
  + Honors
  + Dual Credit
  + College Prep
  + None/Other
* Subject Area Totals
* Highest Course in Subject Area

## College Transcripts

## Overview

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1827289137/d10e7c7b3a0981200a67a543e27b/College-Overview.png?expires=1784333700&signature=c3d4888d526c88d6aa56374deb882f729f260a1af344edeb4c48c98bce28f86a&req=dSglEct2lIBcXvMW1HO4zYF0Xg77xyxv8DvY4XeeO9YF12KtUOHlTHBFZwhS%0ASuoR648XSgqMsGTF1P0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1827289137/d10e7c7b3a0981200a67a543e27b/College-Overview.png?expires=1784333700&signature=c3d4888d526c88d6aa56374deb882f729f260a1af344edeb4c48c98bce28f86a&req=dSglEct2lIBcXvMW1HO4zYF0Xg77xyxv8DvY4XeeO9YF12KtUOHlTHBFZwhS%0ASuoR648XSgqMsGTF1P0%3D%0A)

* Institution Name & Type
* Institution Address
* Institutional Code
* File
* Document Type
* Transcript Date
* Academic Overview

  + Trends
  + Strengths
  + Weaknesses
  + Rigor

## Courses

* Degree and program information (level, majors, minors, concentrations)
* Comprehensive GPA breakdowns (institutional, cumulative, major, last 30 credits)
* Credit totals (attempted, earned, transfer)
* Upper-level course analysis (300-, 500-, 700-level)
* Highest course per academic area
* Course List

  + Academic Year
  + Term
  + Course Code
  + Course Name
  + Course Level
* Academic Area

  + **Arts:** Music, Theatre, Dance; Visual Arts, Studio Art, Graphic Design; Film, Photography, Creative Writing; Architecture
  + **Humanities:** Philosophy, Ethics; History; Classics, Ancient Studies; English, Literature, Comparative Lit; Linguistics; Religious Studies, Theology; Cultural Studies
  + **Social Sciences:** Psychology; Sociology; Political Science; International Relations; Anthropology; Economics; Human Geography; Criminology, Criminal Justice; Archaeology; Gender Studies, Ethnic Studies
  + **Natural Sciences:** Biology, Biochemistry, Microbiology; Chemistry, Chemical Sciences; Physics, Astronomy; Geology, Earth Science, Oceanography; Environmental Science; Marine Biology; Neuroscience
  + **Mathematics & Statistics:** Mathematics; Statistics, Data Science
  + **Computer & Information Sciences:** Computer Science, Software Engineering; Information Systems, IT, Cybersecurity; Artificial Intelligence, Machine Learning
  + **Engineering & Technology:** Civil, Mechanical, Electrical Engineering; Chemical Engineering; Aerospace, Automotive, Industrial Engineering; Materials Science; Robotics, Systems Engineering; Construction, Manufacturing Technology
  + **Business:** Business Administration, Management; Accounting, Finance, Banking; Marketing, Advertising, Sales; Hospitality, Tourism, Event Management; Supply Chain, Operations Management
  + **Education:** Early Childhood Education; K-12 Education, Secondary Education; Special Education; Higher Education, Educational Leadership; Curriculum & Instruction
  + **Health Professions:** Nursing; Medicine (MD, DO); Public Health, Epidemiology; Pharmacy, Pharmacology; Dentistry, Dental Hygiene; Physical/Occupational Therapy; Veterinary Medicine; Nutrition, Dietetics
  + **Law / Legal Studies:** Law, Legal Studies, Pre-Law

    Public Administration / Policy: Public Administration; Public Policy; International Development
  + **Agriculture & Environmental Studies:** Agriculture, Agronomy; Forestry, Natural Resources; Animal Science; Food Science, Agricultural Economics; Environmental Studies
  + **Communications / Media / Journalism:** Journalism; Media Studies, Film Studies; Public Relations, Strategic Communication; Digital Media, Broadcasting
  + **Interdisciplinary Studies:** Cognitive Science; Global Studies, International Studies; Environmental Humanities; Science & Technology Studies (STS); Data Analytics (cross-disciplinary); Liberal Studies / General Studies
  + **Other:** Military Science; Trade / Vocational Programs; Undeclared / Unclassified

---

# Accessing + Reviewing Transcript Data

## Profile Card

* **Evaluated Transcripts** card lists processed files with institution and date

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1806626018/edfc7f6f87e42cb45be2b97f9ee0/Transcript-Eval-ProfileCard.png?expires=1784333700&signature=ccd53782e06154fcc089350c34a949d7179f0f26cf32289f3f7a15a3ebc269d0&req=dSgnEM98m4FeUfMW1HO4zQQIaA4VzoX%2FRvLKqzrz6ZiRHbaKu6YI7yNZgUTE%0ARzLBTqiXc8%2FicvM4aGc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1806626018/edfc7f6f87e42cb45be2b97f9ee0/Transcript-Eval-ProfileCard.png?expires=1784333700&signature=ccd53782e06154fcc089350c34a949d7179f0f26cf32289f3f7a15a3ebc269d0&req=dSgnEM98m4FeUfMW1HO4zQQIaA4VzoX%2FRvLKqzrz6ZiRHbaKu6YI7yNZgUTE%0ARzLBTqiXc8%2FicvM4aGc%3D%0A)

---

# About AI Insights

## Academic Trends

* Provides a high-level summary of the student’s academic trajectory over time. It highlights patterns such as early challenges, improvements, or consistency in performance. The agent analyzes grade data chronologically to identify trends like GPA progression, recovery from low grades, or sustained academic strength.
* *Example insight:* Notes improvement after a failing grade or identifies consistent high achievement across terms.

## Strengths

* Identifies areas where the student demonstrates strong academic or skill-based performance. The agent pinpoints disciplines or subjects with repeated success, persistence in overcoming earlier difficulties, or clear alignment with the student’s intended field of study.
* *Example insight:* Highlights consistent A-level performance in major-related courses or success in retaken subjects.

## Weaknesses

* Outlines areas with limited performance or challenges that may impact the overall academic record. It includes notes on subjects where grades were lower, repeated, or withdrawn, as well as gaps in breadth or quantitative coursework.
* *Example insight:* Mentions lack of advanced-level courses, a poor grade in a specific area, or a low mark that continues to affect GPA.

## Rigor

* Assesses the overall academic challenge reflected in the coursework. The agent evaluates factors such as course level (lower- vs. upper-division), credit type (transferable vs. non-transferable), honors or advanced courses, and alignment with typical college standards.
* *Example insight:* Indicates whether coursework primarily reflects lower-division community college rigor or includes evidence of advanced study.

# GPA Conversion

The Transcript Evaluation agent will convert reported grades to a standard 4.0 scale, eliminating the need to convert letter grades and 100 point scales manually.

* 97–100 = A+ = 4.0
* 93–96 = A = 4.0
* 90–92 = A- = 3.7
* 87–89 = B+ = 3.3
* 83–86 = B = 3.0
* 80–82 = B- = 2.7
* 77–79 = C+ = 2.3
* 73–76 = C = 2.0
* 70–72 = C- = 1.7
* 67–69 = D+ = 1.3
* 65–66 = D = 1.0
* 60–64 = D- = 0.7
* 0–59 = F = 0.0

Pass/Fail, Audit, W, I = Excluded from GPA.

---

# Pricing

How Transcript Evaluation usage is counted depends on which usage model your plan uses:

* **Usage Caps plans:** Transcript Evaluations are one of your usage categories, measured in evaluations, with an amount included in your contract. See **[Understanding Usage Caps](https://help.element451.com/en/articles/15934464-understanding-usage-caps)** for details.
* **[Usage Credits plans](https://help.element451.com/en/articles/10421758-usage-based-billing-credits):** Transcript Evaluation usage is **free through July 31, 2026**. After that date, contact your account manager for pricing.

Not sure which model you're on? Go to **Settings > General Settings** — a credit balance means you're on Usage Credits, while usage shown as caps in natural units means you're on Usage Caps.

---

# ​Frequently Asked Questions (FAQ)

#### Does the Bolt Transcript Evaluation Agent use OCR technology for reading transcript data?

No. We do not use legacy Optical Character Recognition (OCR) technology to parse transcripts. Traditional OCR can only extract raw characters and often fails when transcript layouts, course tables, or grading formats vary across schools.   
​  
Instead, we use advanced **AI Vision models** (multimodal vision transformers) that understand the *structure, context, and meaning* of the document—accurately identifying course names, terms, credits, grades, and GPA patterns even when formats differ. After extraction, we apply additional **LLM-based processing** to generate insights such as academic trends, summaries, and course classifications.  
​  
This combined approach allows Element451 to deliver accurate, standardized, ready-to-use transcript data without templates, manual cleanup, or custom rules.

#### How does the Bolt Transcript Evaluation Agent handle international transcripts?

The Bolt Transcript Evaluation Agent is designed primarily for U.S.-based and English-language transcripts, including common grading scales, credit systems, and academic structures.

For international transcripts, the Agent can:

* Translate non-English transcripts into English
* Extract and normalize key academic data (e.g., grades, credits, course information)
* Provide a structured summary to support admissions review

This allows institutions to more efficiently review international academic records within their existing admissions workflows. ***However, results may vary depending on the format, language, and structure of the transcript and International transcript data should be reviewed carefully by staff.***

Is the Bolt Transcript Evaluation Agent a replacement for WES or other NACES-member credential evaluation services?

No. The Bolt Transcript Evaluation Agent is **not a replacement** for credential evaluation services such as WES or other NACES-member organization

While the Agent helps standardize and summarize transcript data, it does **not**:

* Provide official equivalency determinations (e.g., U.S. degree equivalence)
* Perform country-specific credential validation
* Deliver compliance-grade evaluations required for admissions or regulatory purposes

Institutions that require official international credential evaluations should continue to use recognized evaluation services alongside Element451.

#### What happens if a transcript is unreadable or poor quality?

The Transcript Evaluation Agent does not send a separate alert or notification when a transcript cannot be read. Instead, the evaluation output itself will indicate when part of a document could not be interpreted. Because the agent always links back to the original file, review the evaluation results alongside the source transcript, and manually review any transcript that is low quality, damaged, or older and harder to read.

# ​

---