---
title: Territory Management
url: https://help.element451.com/en/articles/3990795-territory-management
collection: People
---

Automatically assign records to dynamic territories

# Overview

Territories in Element451 are designed to be dynamic and user-friendly. Administrators have the ability to define specific conditions that automatically assign individual records to appropriate Territories. This process eliminates the need for separate workflows.

The conditions for Territory assignment are highly versatile, allowing you to use common segment filters like address (including state, county, and country), major, and funnel stage, among others. These conditions are continuously checked to ensure that each person's record remains current and accurately placed within the right Territory.

**Note**: Making a territory conditional requires the use of a calculated segment. As a result, this will count toward your calculated segment usage. When viewing a contact’s calculated segments, the segment name won’t match the associated territory name. Instead, it will be labeled with **[TERRITORY]** to indicate that it’s a territory rather than a standard segment.

For example:

* A territory URL may appear as: `territories/elementu.taxonomy.4140206`
* In a contact’s profile card, the corresponding calculated segment will be listed as: `[Territory] elementu.taxonomy.4140206`

After configuring your dynamic Territories, you can create a [Workflow or Rule to assign staff members, such as admissions counselors, to those Territories](https://help.element451.com/en/articles/8813617-user-people-assignees).

💡**Pro** **Tip**: Choose clear, concise names for your Territories. Skip the abbreviations. This keeps your data clean and user-friendly, not just for now but for the future of your Element451 instance.

---

# Accessing Territory Management

To manage your Territories, navigate to **Contacts** > **Categories** > **Territories**.

[![](https://downloads.intercomcdn.com/i/o/931251992/c54fd3d3d1bdbee9463a1601/Territories.gif?expires=1784333700&signature=935f77195f08e0483330be0934fc486cfb0cd6d0a0577affc0d036e1b3229b47&req=fSMmFMx%2FlIhdFb4f3HP0gFvKL1DCgaihsdGjmEWEIn03bHsdXS9bGKABooG7%0AsG20W5v0mi7L3K3KAA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/931251992/c54fd3d3d1bdbee9463a1601/Territories.gif?expires=1784333700&signature=935f77195f08e0483330be0934fc486cfb0cd6d0a0577affc0d036e1b3229b47&req=fSMmFMx%2FlIhdFb4f3HP0gFvKL1DCgaihsdGjmEWEIn03bHsdXS9bGKABooG7%0AsG20W5v0mi7L3K3KAA%3D%3D%0A)

---

# Configuring Territories

📙 Note: To configure Territories, you must have the ***Administer Territory*** permission.

Each dynamic territory combines a territory segment and a set territory workflow into a single configuration.

**Important Notes:**

* Which territory a person is assigned is determined by two factors: (1) The **condition filters** associated with a particular territory and (2) the territory **order of precedence**.
* Since a record can only belong to **one** **territory**, it is assigned to the first match on the territory list. Generally speaking, this means smaller, more specialized populations should be at the top of your territory list, with more generalized territories at the bottom. ​

**Example:** Consider Element University which has two small graduate programs and several UG territories. The undergraduate territories include an international territory, a transfer territory, and 4 geographic territories for first-year applicants. As a graduate, international and transfer territories "override" the undergraduate geography-based territories, they have set their territory list in this order:

1. Graduate - MBA
2. Graduate - Education
3. Undergraduate - Transfer
4. Undergraduate - International (F-1 Visa required)
5. Undergraduate - Eastern US
6. Undergraduate - Central US
7. Undergraduate - Mountain US
8. Undergraduate - Pacific US

---

# When are Territories Calculated?

People records are evaluated on an **ongoing** **basis** to determine if a territory update is needed.

This evaluation can be triggered by:

* A person record is created manually
* Changing/updating information on a person record
* An import or API integration updates or creates a person record
* Adding/removing/updating condition filter(s) for a specified Territory
* Reordering the order of precedence on the territory list

**📙 Note:** This process is asynchronous and may take several minutes to complete updates, especially when creating or editing territories.

---

# Territory List

Each configured Territory is displayed as a row on the Territory list.

* Territory Name
* Territory Code
* The number of people currently assigned to that Territory.
* Active Toggle (Only active territories will be assigned and used in Territory logic)
* Menu

  [![](https://downloads.intercomcdn.com/i/o/931267972/e1e006ea7a4dfda62b37a9de/Screenshot+2024-01-11+at+5.11.53%E2%80%AFPM.png?expires=1784333700&signature=41cebd429f446921feb9a8a59b6fb62923f88999446cb93ff3b9bdc7ead08e5e&req=fSMmFM95lIZdFb4f3HP0gMK2I9EMRz1MxuslAJMzNqgqAQptwj9QC6CAMft0%0Ao2o%3D%0A)](https://downloads.intercomcdn.com/i/o/931267972/e1e006ea7a4dfda62b37a9de/Screenshot+2024-01-11+at+5.11.53%E2%80%AFPM.png?expires=1784333700&signature=41cebd429f446921feb9a8a59b6fb62923f88999446cb93ff3b9bdc7ead08e5e&req=fSMmFM95lIZdFb4f3HP0gMK2I9EMRz1MxuslAJMzNqgqAQptwj9QC6CAMft0%0Ao2o%3D%0A)

  (open, edit, or delete a Territory)

[![](https://downloads.intercomcdn.com/i/o/931273008/cba3299d529768892a1090fd/Screenshot+2024-01-11+at+5.23.44%E2%80%AFPM.png?expires=1784333700&signature=925b1ab9fe0703f3004c0d7f11811b3f9f6f58cf959ea08606d45d517b21b9b6&req=fSMmFM59nYFXFb4f3HP0gDK9AfA7CSv5KFyKhNRKlK60v4nwuS%2FM9lWywvlU%0Abrng5lLOWGhG9ypUbQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/931273008/cba3299d529768892a1090fd/Screenshot+2024-01-11+at+5.23.44%E2%80%AFPM.png?expires=1784333700&signature=925b1ab9fe0703f3004c0d7f11811b3f9f6f58cf959ea08606d45d517b21b9b6&req=fSMmFM59nYFXFb4f3HP0gDK9AfA7CSv5KFyKhNRKlK60v4nwuS%2FM9lWywvlU%0Abrng5lLOWGhG9ypUbQ%3D%3D%0A)

**List Formatting**

* **Gray Row Background**: Territories with condition filters active/applied
* **White Row Background**: Territories with no conditions active/applied

  + While these will not factor into assignment logic, they can be used for manual assignments.

## Reordering Your Territory List

Remember that since a record can only belong to **one** **territory** and it is assigned to the first match on the territory list, we recommend organizing your list with smaller, more specialized populations at the top with more generalized territories at the bottom.

**To reorder your list**:

* Use the two vertical lines

  [![](https://downloads.intercomcdn.com/i/o/931275741/c09c8b76c1429f3e3e0549e9/Screenshot+2024-01-11+at+5.30.52%E2%80%AFPM.png?expires=1784333700&signature=040bd5445c46e4013814b6fea6fd3015541cae1bf922dfcedffee7ca7d47c2b2&req=fSMmFM57moVeFb4f3HP0gLeFkphAFkj897NNOfi94w%2BBRJndps4z1isObJyq%0Ac4I%3D%0A)](https://downloads.intercomcdn.com/i/o/931275741/c09c8b76c1429f3e3e0549e9/Screenshot+2024-01-11+at+5.30.52%E2%80%AFPM.png?expires=1784333700&signature=040bd5445c46e4013814b6fea6fd3015541cae1bf922dfcedffee7ca7d47c2b2&req=fSMmFM57moVeFb4f3HP0gLeFkphAFkj897NNOfi94w%2BBRJndps4z1isObJyq%0Ac4I%3D%0A)

  to click and drag/drop the row to your desired location in the list. ​

---

# Adding + Managing Terrorities

## Adding a New Territory

1. Navigate to **Contacts** > **Categories** > **Territories**
2. Click the **plus + button** in the right corner of your Territory List

   [![](https://downloads.intercomcdn.com/i/o/931258516/f915448449878c562099db39/Screenshot+2024-01-11+at+4.52.40%E2%80%AFPM.png?expires=1784333700&signature=5b5cc304c73e62a8031d98277080023a328ba97a35feda154390c1c729cafc58&req=fSMmFMx2mIBZFb4f3HP0gJmU6%2F3tRWZSGR2p4aAtFi5PYXe4uls81UGWCTUf%0ACE4%3D%0A)](https://downloads.intercomcdn.com/i/o/931258516/f915448449878c562099db39/Screenshot+2024-01-11+at+4.52.40%E2%80%AFPM.png?expires=1784333700&signature=5b5cc304c73e62a8031d98277080023a328ba97a35feda154390c1c729cafc58&req=fSMmFMx2mIBZFb4f3HP0gJmU6%2F3tRWZSGR2p4aAtFi5PYXe4uls81UGWCTUf%0ACE4%3D%0A)
3. Complete the fields:

   * **Name:** Your name should be short and specific (e.g., "Last Name = A-G" or "Texas")
   * **Code:** The code will prepopulate based on the Name you provide, but it can be adjusted
   * **Description:** Give your Territory a description to help explain it to others who may also be working in this Module now and in the future
   * **Condition** **Active** (this enables your Territory to be evaluated on an ongoing basis)

     + **Note**: Making a territory conditional requires the use of a calculated segment. As a result, this will count toward your calculated segment usage.

   [![](https://downloads.intercomcdn.com/i/o/931265417/f54c5b0040164e8fa728e433/Screenshot+2024-01-11+at+5.05.57%E2%80%AFPM.png?expires=1784333700&signature=abe78c1f03dc1364bdb17419d62344f657a3793be43548b82c3543a95a482dce&req=fSMmFM97mYBYFb4f3HP0gAZe6AdeJHad15inHvXhB61LT3E2XZLV6ILskEhu%0Alts%3D%0A)](https://downloads.intercomcdn.com/i/o/931265417/f54c5b0040164e8fa728e433/Screenshot+2024-01-11+at+5.05.57%E2%80%AFPM.png?expires=1784333700&signature=abe78c1f03dc1364bdb17419d62344f657a3793be43548b82c3543a95a482dce&req=fSMmFM97mYBYFb4f3HP0gAZe6AdeJHad15inHvXhB61LT3E2XZLV6ILskEhu%0Alts%3D%0A)
4. **Add Filters** (this will determine which students are assigned to this territory)
5. When you're finished configuring the Territory, click Save

   [![](https://downloads.intercomcdn.com/i/o/931266206/37ecea4ddee9fd96df766893/Screenshot+2024-01-11+at+5.07.25%E2%80%AFPM.png?expires=1784333700&signature=e71617e47d4555917c0f82ceffe5f75fd80a0d14ddcf50eef266b1d433d4046a&req=fSMmFM94n4FZFb4f3HP0gHBlkiwBMggKjUpX1N9phYL5HNseGDmz2xLGrZZ7%0Aj4k%3D%0A)](https://downloads.intercomcdn.com/i/o/931266206/37ecea4ddee9fd96df766893/Screenshot+2024-01-11+at+5.07.25%E2%80%AFPM.png?expires=1784333700&signature=e71617e47d4555917c0f82ceffe5f75fd80a0d14ddcf50eef266b1d433d4046a&req=fSMmFM94n4FZFb4f3HP0gHBlkiwBMggKjUpX1N9phYL5HNseGDmz2xLGrZZ7%0Aj4k%3D%0A)

   in the top right corner.

## Opening, Editing + Deleting Territories

To open, edit, or delete an existing Territory from your list:

1. Click the **three horizontal dots**

   [![](https://downloads.intercomcdn.com/i/o/931267972/e1e006ea7a4dfda62b37a9de/Screenshot+2024-01-11+at+5.11.53%E2%80%AFPM.png?expires=1784333700&signature=41cebd429f446921feb9a8a59b6fb62923f88999446cb93ff3b9bdc7ead08e5e&req=fSMmFM95lIZdFb4f3HP0gMK2I9EMRz1MxuslAJMzNqgqAQptwj9QC6CAMft0%0Ao2o%3D%0A)](https://downloads.intercomcdn.com/i/o/931267972/e1e006ea7a4dfda62b37a9de/Screenshot+2024-01-11+at+5.11.53%E2%80%AFPM.png?expires=1784333700&signature=41cebd429f446921feb9a8a59b6fb62923f88999446cb93ff3b9bdc7ead08e5e&req=fSMmFM95lIZdFb4f3HP0gMK2I9EMRz1MxuslAJMzNqgqAQptwj9QC6CAMft0%0Ao2o%3D%0A)

   at the end of the Territory's row
2. Select open, edit, or delete based on the action you wish to take

   * **Open**: View the Territory information and the people assigned to that Territory
   * **Edit**: Edit the basic information and filter conditions for that Territory
   * **Delete**: Permanently delete the Territory

---

# Manually Setting a Territory

Territory assignments are evaluated continuously and are updated when data on a person profile changes. However, there are times when a user may need to be excluded from the standard territory assignment process. In this case, you can manually set (or clear) a Territory from a record and/or opt that record out from future territory assignment calculations from the System card located in the sidebar of the person profile.

**To manually change or clear a Territory**:

1. Navigate to the [person's profile/record](https://help.element451.com/en/articles/1475605-searching-for-a-user-by-name-email-or-characteristic)
2. Locate the System card and click on the Territory chip. (**Note:** Depending on the configuration of your [Bolt Person Profiles](https://help.element451.com/en/articles/6449965-bolt-profile-templates), the Territory settings may not appear on one or more of your profile templates.)   
   ​

   [![](https://downloads.intercomcdn.com/i/o/931879923/eaf00a56dffcfb08b0692922/Screenshot+2024-01-12+at+9.32.34%E2%80%AFAM.png?expires=1784333700&signature=09be9e2e5d54a7d160e6e4515305829f10820330afe08b5613aeb4a3b6a27707&req=fSMmHs53lINcFb4f3HP0gHkgoKcqrAk0cMnNVHi02tGnx%2FZI%2BMULtxWKfA0g%0ApC4%3D%0A)](https://downloads.intercomcdn.com/i/o/931879923/eaf00a56dffcfb08b0692922/Screenshot+2024-01-12+at+9.32.34%E2%80%AFAM.png?expires=1784333700&signature=09be9e2e5d54a7d160e6e4515305829f10820330afe08b5613aeb4a3b6a27707&req=fSMmHs53lINcFb4f3HP0gHkgoKcqrAk0cMnNVHi02tGnx%2FZI%2BMULtxWKfA0g%0ApC4%3D%0A)
3. Once you click on the Territory chip, you can select the **X** to clear the Territory or simply select a new Territory from the drop-down list.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/931892790/7f6cd219324edc5ad954bbe2/Screenshot+2024-01-12+at+9.44.45%E2%80%AFAM.png?expires=1784333700&signature=1c0fed44086f997de907e87c33224c0be62c4db39dcd06d1e114b1cd6be28244&req=fSMmHsB8mohfFb4f3HP0gLnuL3J%2B%2FLw7jTIxqJSxKE%2FDTrryDwD2XJ6XnnhO%0A49w%3D%0A)](https://downloads.intercomcdn.com/i/o/931892790/7f6cd219324edc5ad954bbe2/Screenshot+2024-01-12+at+9.44.45%E2%80%AFAM.png?expires=1784333700&signature=1c0fed44086f997de907e87c33224c0be62c4db39dcd06d1e114b1cd6be28244&req=fSMmHsB8mohfFb4f3HP0gLnuL3J%2B%2FLw7jTIxqJSxKE%2FDTrryDwD2XJ6XnnhO%0A49w%3D%0A)
4. **Toggle on** *Opt-Out From Automatic Territory Assignment*: If the student still meets the conditions in your dynamic Territory configurations, Element451 will revert the Territory back unless the opt-out toggle is enabled.

   [![](https://downloads.intercomcdn.com/i/o/931900135/89f237c7d7b964e894d50904/Screenshot+2024-01-12+at+9.44.17%E2%80%AFAM.png?expires=1784333700&signature=cf4ae920a399ed80ab98fca19373e4554daad5bdb7cc76bdef039a1de649c78a&req=fSMmH8l%2BnIJaFb4f3HP0gMJ%2BbBUF9uVV0AxrmnHd4f%2FSJdpYkPVNAaPdgVnr%0AiEg%3D%0A)](https://downloads.intercomcdn.com/i/o/931900135/89f237c7d7b964e894d50904/Screenshot+2024-01-12+at+9.44.17%E2%80%AFAM.png?expires=1784333700&signature=cf4ae920a399ed80ab98fca19373e4554daad5bdb7cc76bdef039a1de649c78a&req=fSMmH8l%2BnIJaFb4f3HP0gMJ%2BbBUF9uVV0AxrmnHd4f%2FSJdpYkPVNAaPdgVnr%0AiEg%3D%0A)

---

# Video: Territories

---

# Adding Assignee (Staff Member) Based on Territory

Using a Workflow or Rule, you can automate the process of assigning staff members (or a Team) to user/people records based on their Territory assignment.

[Learn More: User Assignees](https://help.element451.com/en/articles/8813617-user-people-assignees)

---

# FAQs

**Q:** Why don't the **people who match this filter** count territory **People Count** match?   
​**A:** "People who match this filter" looks at the records that could be included in that territory based on the filter(s) selected. The territory People Count are those who are actually assigned to the territory. These numbers will rarely match exactly. Some common impacts:

* Records manually added or removed from a territory.
* A person matched another territory higher on the order of precedence.
* A territory admin has recently updated the filters, and the territory is pending a large update.

**Q:** I have older territories with no logic assigned to them, and I'm ready to set up dynamic territories. What should I do first?   
​**A:** First, turn off or modify any workflows that include the "set territory" function. Once you get your dynamic territories set up, they will drive your territory assignments moving forward. By disabling/updating those workflows, you'll avoid any potential conflicts between the logic. The "Set Territory" workflow action combined with the "opt out of automatic territory assignment' is still useful to create exceptions to your standard territory logic.   
​  
​**Q:** Are there character limits for Territory names and descriptions?  
​**A:** Yes. Territory Names are limited to approx. 150 characters and descriptions 250. Exceeding these limits will not allow the territory to save.

---