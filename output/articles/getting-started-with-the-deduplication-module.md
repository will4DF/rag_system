---
title: Getting Started with the Deduplication Module
url: https://help.element451.com/en/articles/2511116-getting-started-with-the-deduplication-module
collection: People
---

Learn how to manage duplicate records in Element451 effortlessly using the tools within the Deduplication Module.

# Overview

Element451 offers a robust Deduplication module to efficiently manage and merge potential duplicate records. The module can be easily accessed to review and merge duplicates, utilize search and filter options, and handle conflicts with customizable settings. Whether merging from a contact’s profile, using the dedicated module, or performing bulk merges, Element451 provides tools to ensure your data remains clean and accurate.

## Accessing the Deduplication Module

Navigate to **Contacts** > **Deduplication**.

[![](https://downloads.intercomcdn.com/i/o/1082459669/86ccbafb6dbbff506403cf2f/Screenshot+2024-06-14+at+2_05_27%E2%80%AFPM.png?expires=1784333700&signature=46be87df8451547674d4253ce6ea823d6b8932d61e5e6172eeaf52a72a3fae3f&req=dSAvFM17lIdZUPMW1HO4zRUo4VrFCbASiZ3sNNMz2jhta1rJswYGhl3aWwTJ%0AT%2BU3v3oKZt%2FiBENXTeE%3D%0A)](https://downloads.intercomcdn.com/i/o/1082459669/86ccbafb6dbbff506403cf2f/Screenshot+2024-06-14+at+2_05_27%E2%80%AFPM.png?expires=1784333700&signature=46be87df8451547674d4253ce6ea823d6b8932d61e5e6172eeaf52a72a3fae3f&req=dSAvFM17lIdZUPMW1HO4zRUo4VrFCbASiZ3sNNMz2jhta1rJswYGhl3aWwTJ%0AT%2BU3v3oKZt%2FiBENXTeE%3D%0A)

## Switching Between Bolt Deduplication and Legacy Deduplication

Element451 offers two deduplication experiences: **Bolt Deduplication**, the new AI-powered experience that analyzes duplicate pairs and guides your review, and the **legacy Deduplication module** documented in this article. When Bolt Deduplication is enabled for your instance, the **Contacts** > **Deduplication** navigation item opens Bolt Deduplication by default.

* **Switch to the legacy experience**: From the Bolt Deduplication page header, click **Switch to legacy deduplication**.
* **Switch back to Bolt Deduplication**: From the legacy module page header, click **Switch to Bolt Deduplication**.
* **Your choice is remembered**: Element451 remembers which experience you selected (in your browser), so the Deduplication navigation item continues to open your preferred experience until you switch again.

Use Bolt Deduplication when you want AI-assisted duplicate review with analysis and recommendations. Use the legacy module if you prefer the classic manual review and merge workflow described in the rest of this article. If Bolt Deduplication is not enabled for your instance, the legacy module always displays and no switch button is shown.

**Duplicate history**: Bolt Deduplication includes a history table of past resolution actions. Click the value in the **When** column to open the review details sidebar for that entry directly. When a reviewer provided feedback as part of a resolution, that feedback is displayed in the sidebar.

---

# The Deduplication Module Interface

Once you've accessed the Deduplication module, you'll find yourself in the Merge Duplicate People Records interface. This is where you are presented with a list of potential duplicate records that need to be reviewed.

## Searching + Filtering the List

* **Search**: Above the list of possible duplicates, a search bar allows you to search for specific contact records.
* **Filter**: To the far right of the search bar, a filter control allows you to filter the list to show only **unresolved** duplicates, **all** duplicates, or **ignored** suggestions. The filter is set to **unresolved** by default.

[![](https://downloads.intercomcdn.com/i/o/1082562492/599909be439ceb621c8f6ac5/Screenshot+2024-06-14+at+4_16_12%E2%80%AFPM.png?expires=1784333700&signature=674bf1195ce363b603ef6f3af0e3b499172fa121619cfd1f6a99a23c7ac4db9a&req=dSAvFMx4n4VWW%2FMW1HO4zblth2vZdr6Ix2tj8lwSybOoOYgrTRIRFwxy%2FqI%2B%0AxkBX8btw%2BzBiWnCv2uU%3D%0A)](https://downloads.intercomcdn.com/i/o/1082562492/599909be439ceb621c8f6ac5/Screenshot+2024-06-14+at+4_16_12%E2%80%AFPM.png?expires=1784333700&signature=674bf1195ce363b603ef6f3af0e3b499172fa121619cfd1f6a99a23c7ac4db9a&req=dSAvFMx4n4VWW%2FMW1HO4zblth2vZdr6Ix2tj8lwSybOoOYgrTRIRFwxy%2FqI%2B%0AxkBX8btw%2BzBiWnCv2uU%3D%0A)

## List Columns + Action Buttons

* You will notice there are two name columns in your list. The left column shows the suggested **Master Record**, while the right column shows the **Possible Duplicate**. The Possible Duplicate record shares similar attributes to the Master Record, which [triggered E451 to flag it as a candidate for merging](https://help.element451.com/en/articles/4935488-deduplication-logic).
* To the far right of each row on the list, the following is displayed: displays the following:

  + **Match**: Percentage of duplicate criteria that were met (confidence score).
  + **Status**: Status of the possible duplicate record (unresolved or ignored).
  + [![](https://downloads.intercomcdn.com/i/o/1082561251/8366173f04b95f52852e0aa6/eyeball2.png?expires=1784333700&signature=fc896fb1eff67e8f323c3ecfa733931946089a7859b161bdfe88fff2b0a1d3a5&req=dSAvFMx4nINaWPMW1HO4zebFJHUGFE7psbRfIb8FN22iGkOBFeg4U8vHtsDn%0Ab9nM%0A)](https://downloads.intercomcdn.com/i/o/1082561251/8366173f04b95f52852e0aa6/eyeball2.png?expires=1784333700&signature=fc896fb1eff67e8f323c3ecfa733931946089a7859b161bdfe88fff2b0a1d3a5&req=dSAvFMx4nINaWPMW1HO4zebFJHUGFE7psbRfIb8FN22iGkOBFeg4U8vHtsDn%0Ab9nM%0A)

    **View**: View a preview of the **possible** **duplicate** **record**.
  + [![](https://downloads.intercomcdn.com/i/o/1082558668/feb2ea8870fac70d33815d51/Merge-PersonIcon.png?expires=1784333700&signature=aef39f0b92278205f69a55e8dbea772afface2386257b3042d1bae7bab2f4eb6&req=dSAvFMx7lYdZUfMW1HO4zXE4ic6lJPLpnPLfiuPASoPRxM%2BkJ%2BPjniwRVSjB%0A8kyA%0A)](https://downloads.intercomcdn.com/i/o/1082558668/feb2ea8870fac70d33815d51/Merge-PersonIcon.png?expires=1784333700&signature=aef39f0b92278205f69a55e8dbea772afface2386257b3042d1bae7bab2f4eb6&req=dSAvFMx7lYdZUfMW1HO4zXE4ic6lJPLpnPLfiuPASoPRxM%2BkJ%2BPjniwRVSjB%0A8kyA%0A)

    **Merge**: Opens the merge interface, shown later in this article.
  + [![](https://downloads.intercomcdn.com/i/o/1082558906/3f3f654422c1539f6c1fb154/Ignore-Prohibition+Symbol.png?expires=1784333700&signature=11bb6f5f17b14f65e6437f121aa3f98d072bf3cdb40784c0632ff82fe3a20599&req=dSAvFMx7lYhfX%2FMW1HO4zaDIH5yDu4dGTHs8uaC08YOLqa7quUQyMRUNeml3%0AfKzy%0A)](https://downloads.intercomcdn.com/i/o/1082558906/3f3f654422c1539f6c1fb154/Ignore-Prohibition+Symbol.png?expires=1784333700&signature=11bb6f5f17b14f65e6437f121aa3f98d072bf3cdb40784c0632ff82fe3a20599&req=dSAvFMx7lYhfX%2FMW1HO4zaDIH5yDu4dGTHs8uaC08YOLqa7quUQyMRUNeml3%0AfKzy%0A)

    **Ignore**: Ignores the duplicate match and leaves both records unmerged.

    [![](https://downloads.intercomcdn.com/i/o/1082548964/557db48559ac34b328f7f04e/Screenshot+2024-06-14+at+3_54_42%E2%80%AFPM.png?expires=1784333700&signature=7948478be4cfb1b7000926589e6ff1ed99029d244a6c9d3262a3b6e42728d1f8&req=dSAvFMx6lYhZXfMW1HO4zYcLskPuwM%2F69bgM%2BeSIKaqOj%2BnpEyGvwbKeVD9A%0AJOXa%0A)](https://downloads.intercomcdn.com/i/o/1082548964/557db48559ac34b328f7f04e/Screenshot+2024-06-14+at+3_54_42%E2%80%AFPM.png?expires=1784333700&signature=7948478be4cfb1b7000926589e6ff1ed99029d244a6c9d3262a3b6e42728d1f8&req=dSAvFMx6lYhZXfMW1HO4zYcLskPuwM%2F69bgM%2BeSIKaqOj%2BnpEyGvwbKeVD9A%0AJOXa%0A)

---

# How Does Deduplication Work?

## Deduplication Logic

Element451 automatically checks for duplicates whenever a record is created or updated, using key identifiers like name, email, social security number, and date of birth. For a detailed explanation of how this works, refer to the full article below.

[Deduplication Logic →](https://help.element451.com/en/articles/4935488-deduplication-logic)

## Process of Merging Records

When records are merged, Element451 keeps the Element ID of the master record. Once the merge is complete, the duplicate record will be deleted/overwritten. Below is a description of how fields are prioritized and merged:

## Single Value Fields

Only one data point can be kept for basic fields such as person data and contact information. If there are conflicting fields, the information in the master record will be selected. If the Master field is empty, the duplicate data will be selected.

📌 **Special Note: Email Addresses**

If two different email addresses exist, you must select which one to use as the contact's primary email address. The email address not selected will be automatically added as an `Email Identity` and placed on the *Identities* [profile card](https://help.element451.com/en/articles/1475735-the-person-profile#h_8456eb5949). The Email Identity is also used in the [logic](https://help.element451.com/en/articles/4935488-deduplication-logic) when flagging duplicates.   
​

Here's an example:

* Primary Record **BEFORE** Merge:  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1187686524/5a06102fc068df8022cce385/CleanShot%2B2024-09-20%2Bat%2B15_33_48.png?expires=1784333700&signature=e1914fb47a8ca1f8603f8e095da12b042c41204b8726cc6b7d635840fc4a38e6&req=dSEvEc92m4RdXfMW1HO4zQOofZG5FvmQMuwMhSxkv3HkkR1tgr4mz%2Fr42spw%0ARDXZ%0A)](https://downloads.intercomcdn.com/i/o/1187686524/5a06102fc068df8022cce385/CleanShot%2B2024-09-20%2Bat%2B15_33_48.png?expires=1784333700&signature=e1914fb47a8ca1f8603f8e095da12b042c41204b8726cc6b7d635840fc4a38e6&req=dSEvEc92m4RdXfMW1HO4zQOofZG5FvmQMuwMhSxkv3HkkR1tgr4mz%2Fr42spw%0ARDXZ%0A)
* Primary Record AFTER Merge (notice how the Email ID was added):   
  ​

  [![](https://downloads.intercomcdn.com/i/o/1187686886/613249ab8bc851af018c3a3b/CleanShot+2024-09-20+at+15_34_52.png?expires=1784333700&signature=2f4a71445c9b14faf6182d8479052b01f3f5e807d36b4a1fc36394c2181a4fb5&req=dSEvEc92m4lXX%2FMW1HO4zfcbf0avhOxlICUfjJ4PleVuu5oeFVK28YgExksO%0A3Ohf%0A)](https://downloads.intercomcdn.com/i/o/1187686886/613249ab8bc851af018c3a3b/CleanShot+2024-09-20+at+15_34_52.png?expires=1784333700&signature=2f4a71445c9b14faf6182d8479052b01f3f5e807d36b4a1fc36394c2181a4fb5&req=dSEvEc92m4lXX%2FMW1HO4zfcbf0avhOxlICUfjJ4PleVuu5oeFVK28YgExksO%0A3Ohf%0A)

  ​

​

## Multi-Value Fields

**Notes, labels, and applications** from both student records are merged to the master record by default unless you specify not to merge them.

Similarly, for fields such as **evaluations, identities, event registrations, and surveys**, the default is to merge into the master record. If there is conflicting data, Element selects the master record's data. You can also specify to ignore or keep one when there is conflicting data.

For fields such as **education, addresses, milestones, and sources**, they are merged by default unless you specify another action, such as append, ignore, or keep both.

For **all other fields**, the system merges everything to the master record by default.

---

# Merging Records

Element451 offers flexible tools for managing duplicate records. You can merge duplicates directly from a contact’s profile, use the dedicated Deduplication Module, or perform bulk merges. Customize your approach to ensure clean and accurate data is efficiently collected. For a detailed explanation of how this works, refer to the full article below.

[Merging Duplicate Records →](https://help.element451.com/en/articles/9472960-merging-duplicate-records)

---