---
title: Creating + Managing Organizations
url: https://help.element451.com/en/articles/9471960-creating-managing-organizations
collection: Organizations
---

Learn how to create, manage, and import organizations with Element451. Update details, manage members, and more.

# Overview

Element451’s Organizations module allows you to efficiently create, manage, and import organizational data. Easily add new organizations manually or through CSV imports, update details, and manage members. Utilize intuitive tools for viewing, editing, and deleting organizations to keep your database accurate and up-to-date.

---

# Creating Organizations

## Option 1: Manually

1. Navigate to **Contacts** > **Organizations**.
2. Click the **+ New Organization** button in the right corner of the header.

   [![](https://downloads.intercomcdn.com/i/o/1082343174/a9dc1d98bcff42634952ff74/Screenshot+2024-06-14+at+12_06_16%E2%80%AFPM.png?expires=1784333700&signature=527d2bb3450e0192c133d651689688715dd6fa5cb3ef84a7ba7818df173d2545&req=dSAvFMp6noBYXfMW1HO4zZKSQVQo6dstcScui19Od7Jph1apFJCtYiwr1swq%0AgPv1%0A)](https://downloads.intercomcdn.com/i/o/1082343174/a9dc1d98bcff42634952ff74/Screenshot+2024-06-14+at+12_06_16%E2%80%AFPM.png?expires=1784333700&signature=527d2bb3450e0192c133d651689688715dd6fa5cb3ef84a7ba7818df173d2545&req=dSAvFMp6noBYXfMW1HO4zZKSQVQo6dstcScui19Od7Jph1apFJCtYiwr1swq%0AgPv1%0A)
3. Complete the required fields to add a new organization:

   * **Information**

     + Name
     + Type
     + Domain
     + Website
     + Labels
     + Assignee
   * **Contact**

     + Phone Number
     + Location
     + Territory
4. Click **Save** in the top right corner.
5. Once the Organization has been created, you can open it to:

   * Add identities
   * Add members
   * Designate a primary contact  
     ​

## Option 2: Import

1. Navigate to **Contacts** > **Organizations**.
2. Click on the three vertical dots

   [![](https://downloads.intercomcdn.com/i/o/1082314030/b027144e0a1abf3e1e1af7e2/More+Icon2.png?expires=1784333700&signature=18e8de2470c92d01bd00de3b74357ecdb0ecfc111cde44d517955db30da8f685&req=dSAvFMp%2FmYFcWfMW1HO4zfPGsrhgQ0N1YK%2BJ2CDvGoot7Jqslza%2FrAkui3WD%0ABusP%0A)](https://downloads.intercomcdn.com/i/o/1082314030/b027144e0a1abf3e1e1af7e2/More+Icon2.png?expires=1784333700&signature=18e8de2470c92d01bd00de3b74357ecdb0ecfc111cde44d517955db30da8f685&req=dSAvFMp%2FmYFcWfMW1HO4zfPGsrhgQ0N1YK%2BJ2CDvGoot7Jqslza%2FrAkui3WD%0ABusP%0A)

   in the right corner of the header.
3. Select **Import Organizations**.

   [![](https://downloads.intercomcdn.com/i/o/1082316026/9a8bb10be633068c83edf179/Screenshot+2024-06-14+at+11_39_41%E2%80%AFAM.png?expires=1784333700&signature=74f59e037e262f1978aeb86564ec5883f5f460c6744e802b5fcf3d717b890840&req=dSAvFMp%2Fm4FdX%2FMW1HO4zQT4SihWaXuvMI3zOo4jW2rN56pYBVTY0neI2el7%0AFbRd%0A)](https://downloads.intercomcdn.com/i/o/1082316026/9a8bb10be633068c83edf179/Screenshot+2024-06-14+at+11_39_41%E2%80%AFAM.png?expires=1784333700&signature=74f59e037e262f1978aeb86564ec5883f5f460c6744e802b5fcf3d717b890840&req=dSAvFMp%2Fm4FdX%2FMW1HO4zQT4SihWaXuvMI3zOo4jW2rN56pYBVTY0neI2el7%0AFbRd%0A)
4. Download the .CSV template and add your data.

   [![](https://downloads.intercomcdn.com/i/o/1082336109/3b70e0a39552ac6650752925/download+csv.png?expires=1784333700&signature=58d1acc3e64b6de6c5742f8b921ee26740ebb212945aef9963219767fd82735a&req=dSAvFMp9m4BfUPMW1HO4za5MaNCXmFc%2Bpfg92Xg7RqVpQ4fgmlbTu5hVGdvo%0AW4d2%0A)](https://downloads.intercomcdn.com/i/o/1082336109/3b70e0a39552ac6650752925/download+csv.png?expires=1784333700&signature=58d1acc3e64b6de6c5742f8b921ee26740ebb212945aef9963219767fd82735a&req=dSAvFMp9m4BfUPMW1HO4za5MaNCXmFc%2Bpfg92Xg7RqVpQ4fgmlbTu5hVGdvo%0AW4d2%0A)
5. Select **Mode**: Choose what happens with the data from the template when re-imported. 🚨 **Important:** Ensure each organization has an identity value (CEEB Code, Custom ID, or SIS ID) to determine if it is new or existing. If an identity value is not provided, E451 will treat it as a new organization, potentially causing duplicates or being ignored, depending on the selected mode.

   * **Insert New**: Creates new organizations and ignores existing ones.
   * **Update Existing**: Updates existing organizations and ignores new ones.
   * **Insert New or Update Existing**: Creates new organizations and updates existing ones.

     [![](https://downloads.intercomcdn.com/i/o/1082340230/6223de5841461b658c169947/Screenshot+2024-06-14+at+12_03_19%E2%80%AFPM.png?expires=1784333700&signature=cec447c345eb1be2e8bfb3801a5e2c89d83435577f9101fa68c6aa54c630e868&req=dSAvFMp6nYNcWfMW1HO4zcpTcm3yPbonOSk6HSAs2bKiMGES7G75ah9LKW%2FY%0ASqVC%0A)](https://downloads.intercomcdn.com/i/o/1082340230/6223de5841461b658c169947/Screenshot+2024-06-14+at+12_03_19%E2%80%AFPM.png?expires=1784333700&signature=cec447c345eb1be2e8bfb3801a5e2c89d83435577f9101fa68c6aa54c630e868&req=dSAvFMp6nYNcWfMW1HO4zcpTcm3yPbonOSk6HSAs2bKiMGES7G75ah9LKW%2FY%0ASqVC%0A)
6. Click **Add File** and select the template to re-import.

   [![](https://downloads.intercomcdn.com/i/o/1082339664/171b654769989be831c04c62/Screenshot+2024-06-14+at+12_02_43%E2%80%AFPM.png?expires=1784333700&signature=ed5e4ca630ccdfe773f56254a86fda4203c57395033501ffcb6575746f945fde&req=dSAvFMp9lIdZXfMW1HO4zR3WyTSzKP%2F1p85y4DyESJ7UjrvOYy47nf6Sg%2B3c%0AhNeW%0A)](https://downloads.intercomcdn.com/i/o/1082339664/171b654769989be831c04c62/Screenshot+2024-06-14+at+12_02_43%E2%80%AFPM.png?expires=1784333700&signature=ed5e4ca630ccdfe773f56254a86fda4203c57395033501ffcb6575746f945fde&req=dSAvFMp9lIdZXfMW1HO4zR3WyTSzKP%2F1p85y4DyESJ7UjrvOYy47nf6Sg%2B3c%0AhNeW%0A)
7. Click **Import** in the top right corner. An import status will provide the breakdown of the results.

   [![](https://downloads.intercomcdn.com/i/o/1082341963/60cbae1969cd23113b52ecc6/Screenshot+2024-06-14+at+12_05_00%E2%80%AFPM.png?expires=1784333700&signature=34daa1b0d7f74792622720dc3f2a79b10bc56169bff0ae6bbc696f8539ac96f4&req=dSAvFMp6nIhZWvMW1HO4zdVk%2B%2FPF4s8yEEyLSicxFyrMIqjIRg22iH5Ld4uf%0A6pY6%0A)](https://downloads.intercomcdn.com/i/o/1082341963/60cbae1969cd23113b52ecc6/Screenshot+2024-06-14+at+12_05_00%E2%80%AFPM.png?expires=1784333700&signature=34daa1b0d7f74792622720dc3f2a79b10bc56169bff0ae6bbc696f8539ac96f4&req=dSAvFMp6nIhZWvMW1HO4zdVk%2B%2FPF4s8yEEyLSicxFyrMIqjIRg22iH5Ld4uf%0A6pY6%0A)

---

# Viewing + Editing Organizations

* To **view** an organization, click the three vertical dots

  at the end of the organization's row. Then, select **Open**. When viewing an organization, you can also update any of the fields just as you would in other modules in E451.

* To **edit** an organization, click the three vertical dots at the end of the organization's row. Then, select either **Open** or **Edit**.

✨ **Pro Tip:** You can use the Import feature to update your organizations in bulk. To do so, follow the same process outlined above in [Creating Organizations](https://help.element451.com/en/articles/9471960-creating-managing-organizations#).

---

# Deleting Organizations

* To **delete** an organization, click the three vertical dots at the end of the organization's row. Then, select **Delete**.

---

# Adding + Removing Organization Members

* To **add** members to an organization, open the organization and click the **plus** sign icon in the header.

  [![](https://downloads.intercomcdn.com/i/o/1082351840/6528de819c3fd6e6fbda94f9/Screenshot+2024-06-14+at+12_14_26%E2%80%AFPM.png?expires=1784333700&signature=2edf690673ab597dba8b7229fb14bbfc13870b6e0caf07a44f91acd3a1678066&req=dSAvFMp7nIlbWfMW1HO4zSrJx3sYMvMLgVS8mdt5pLcMp6iWAPlMq8GNxRNt%0A6Aef%0A)](https://downloads.intercomcdn.com/i/o/1082351840/6528de819c3fd6e6fbda94f9/Screenshot+2024-06-14+at+12_14_26%E2%80%AFPM.png?expires=1784333700&signature=2edf690673ab597dba8b7229fb14bbfc13870b6e0caf07a44f91acd3a1678066&req=dSAvFMp7nIlbWfMW1HO4zSrJx3sYMvMLgVS8mdt5pLcMp6iWAPlMq8GNxRNt%0A6Aef%0A)
* To **remove** members or **view** their profile, click the three vertical dots at the end of the member's row.

  [![](https://downloads.intercomcdn.com/i/o/1082354857/1010839253f3b8af5427c9f0/Screenshot+2024-06-14+at+12_16_21%E2%80%AFPM.png?expires=1784333700&signature=03a46fd1f1ccbe6d8aac01cafba86929d7f5ab6aac50fc589c702174a65f2a98&req=dSAvFMp7mYlaXvMW1HO4zSm1mjZJHPv%2F59BdEt%2BWmW3%2FpbLjmTifKUiFzih%2B%0ACwKH%0A)](https://downloads.intercomcdn.com/i/o/1082354857/1010839253f3b8af5427c9f0/Screenshot+2024-06-14+at+12_16_21%E2%80%AFPM.png?expires=1784333700&signature=03a46fd1f1ccbe6d8aac01cafba86929d7f5ab6aac50fc589c702174a65f2a98&req=dSAvFMp7mYlaXvMW1HO4zSm1mjZJHPv%2F59BdEt%2BWmW3%2FpbLjmTifKUiFzih%2B%0ACwKH%0A)

---

# Auto-Linked Student Members (CEEB Match)

Students are automatically linked as members of an Organization when their high school CEEB code matches the Organization's CEEB code identity. This means feeder high school Organizations populate themselves as new inquiries and applications come in — no manual member management required.

**How it works:**

* The Organization must have a **CEEB Code** identity set on it.
* Any contact with a high school entry whose CEEB code matches will appear as a member of that Organization, with the Relationship label **Student**.
* These auto-linked members update in real time as contact data changes — if a student's high school CEEB is updated or removed, they'll move in or out of the org accordingly.

**Important notes:**

* Auto-linked members **cannot be removed directly** from the Organization. The contact's high school data is the source of truth — to remove the link, edit or clear the matching High School entry on the student's contact record.
* Hovering the Relationship field on an auto-linked row shows: *"This student attended a High School matching the CEEB code for this organization. To remove this student from the organization, remove the matching High School data."*

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2426994518/c232bc9fda1769f7bd7e059a2d04/CEEB+Code+Match+-+Org%402x.png?expires=1784333700&signature=b1598f483a7bd6ed92f574807c8d74d49df1037ea4c2320289ea5304f8f26010&req=diQlEMB3mYReUfMW1HO4zQ6O8PGNeBb5FrmGLoh1VIB7EFx%2FgPGbyGskglJ%2F%0ACJvj%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2426994518/c232bc9fda1769f7bd7e059a2d04/CEEB+Code+Match+-+Org%402x.png?expires=1784333700&signature=b1598f483a7bd6ed92f574807c8d74d49df1037ea4c2320289ea5304f8f26010&req=diQlEMB3mYReUfMW1HO4zQ6O8PGNeBb5FrmGLoh1VIB7EFx%2FgPGbyGskglJ%2F%0ACJvj%0A)
* Auto-linked members are included in Organization-based segmentation and filtering alongside manually-added members.

---

# Designating a Primary Contact

A **Primary Contact** is the external point person at an organization — for example, the lead counselor at a feeder high school or the main coordinator at a community-based organization. This is different from the **Assignee**, which is the internal staff user responsible for managing the relationship from your side.

Each organization can have one primary contact, and that contact must already be a member of the organization. Once set, the primary contact is surfaced in the organization's sidebar and in the org header so staff can identify the right person at a glance. The current primary contact is also visually marked in the Members table.

* To **set** or **change** the primary contact:

  + From the **Primary Contact** card in the organization's sidebar, click into the field and select one of the org's members.
  + Or, from the **Members** table, click the three vertical dots at the end of a member's row and select **Set as Primary Contact**.
* To **clear** the primary contact:

  + From the **Primary Contact** card in the sidebar, clear the selected contact.
  + Or, from the row menu on the current primary contact in the Members table, select **Remove as Primary Contact**.

📌 **Note:** If the primary contact is removed from the organization's membership entirely, the Primary Contact field is automatically cleared — the primary contact must always be a current member of the organization.

---

# Adding + Managing Notes

Notes capture institution-level context, such as visit recaps, recruiting interactions, and reminders, directly on an organization's profile.

* To **add** a note:

  + Open the organization and navigate to the **Notes** section.
  + Click **+ New Note**, enter your content, and save.
* To **edit** a note:

  + Click the three vertical dots at the end of the note's row, then select **Edit**.
* To **delete** a note:

  + Click the three vertical dots at the end of the note's row, then select **Delete**.

---