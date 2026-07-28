---
title: Visibility Groups
url: https://help.element451.com/en/articles/5214533-visibility-groups
collection: Settings + Permissions
---

Learn how to control which person records your internal users have access to see.

# Overview

As your list of internal users grows, tailored access to Element451 becomes essential. Whether it's athletic coaches monitoring recruits, international agents tracking applicants, or faculty reviewing applications for specific programs, ensuring individuals see only the Contact Records/Profiles relevant to their roles is crucial. Visibility Groups is your tool for fine-tuning that access with ease, including controlling access to conversations associated with those Contact Records.

---

# Accessing Visibility Groups

Navigate to **Settings** > **Manage** **Users** > **Visibility** **Groups**

[![](https://downloads.intercomcdn.com/i/o/962252729/15be1e044444b22d78fe4874/Visibility+Groups.gif?expires=1784333700&signature=3a2bac74ceb9da208a5629c3516dbb120fab561776f1bda293572841a42c2be3&req=fSYlFMx8moNWFb4f3HP0gF%2BnfQngMi1%2F5xr5Q1awpWhRSEvupbF3d%2BucBITT%0AJ1ZJnjg6JTtyh4ETBw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/962252729/15be1e044444b22d78fe4874/Visibility+Groups.gif?expires=1784333700&signature=3a2bac74ceb9da208a5629c3516dbb120fab561776f1bda293572841a42c2be3&req=fSYlFMx8moNWFb4f3HP0gF%2BnfQngMi1%2F5xr5Q1awpWhRSEvupbF3d%2BucBITT%0AJ1ZJnjg6JTtyh4ETBw%3D%3D%0A)

---

# How Visibility Groups Work

Visibility Groups allow you to manage access to contact records (including a contact's conversations) at a granular level. You can create up to two levels of subgroups to define what records are accessible to different team members.

## Understanding Subgroups

Subgroups inherit the primary group's conditions and add their specific filters for even more precise control. Being a subgroup changes how users and visibility filters behave.

* **Filter inheritance (AND logic):** A subgroup automatically includes the parent group's visibility filters, shown as read-only. Any filters you add to the subgroup apply as an AND condition on top—narrowing the record set further, never expanding it.

  + *Example: Parent group is filtered to "Intended Campus = Element HQ." A subgroup adds "Major = Business." Result: users in the subgroup only see Business majors from Element HQ—without having to rebuild the campus filter on every subgroup.*

* **User inheritance:** Users assigned to a parent group are automatically inherited by all of its subgroups. Inherited users appear as read-only within the subgroup and must be managed from the parent. A user added to the parent is in every subgroup beneath it—you cannot assign someone to only some subgroups.

* **Nesting limit:** You can nest up to two levels deep (parent → subgroup → sub-subgroup). Groups at the maximum depth will not have the option to create additional subgroups beneath them.

## Planning Your Group Structure

* **Using the parent group for power users:** You don't have to assign anyone to the parent group—or you can use it strategically. A common pattern is to assign directors or admins at the parent level so they automatically inherit access to all subgroups, while individual staff are assigned only to the subgroup relevant to their role.

  + *Example: A Director of Admissions is assigned to the parent "Undergraduate" group and automatically sees all records across every program subgroup. A Business admissions counselor is assigned only to the "Business" subgroup. A Biology admissions counselor is assigned only to the "Biology" subgroup.*

* **Subgroups vs. standalone groups:** The same outcome as a subgroup structure can be achieved with independent single-level Visibility Groups—just create multiple groups each containing the same base filter.

  + Use subgroups when:

    - Multiple groups share a common base filter and you don't want to rebuild it on every group
    - You have power users (directors, admins) who need access across all related groups
  + Use standalone groups instead when users need to belong to some—but not all—related groups. Because a user added to a parent group automatically inherits access to every subgroup beneath it, there is no way to limit them to only certain subgroups.

## Common Use Cases for Using Subgroups

* **Athletics:** Parent group for the coaching staff, with individual subgroups per sport. A head athletic director at the parent level sees all recruits; individual sport coaches are assigned only to their sport's subgroup.
* **Admissions by program:** Parent group filtered by campus or enrollment type (undergraduate/graduate), with subgroups per academic program. The director sits at the top and sees everything; program counselors are assigned only to their program's subgroup.
* **Territory-based recruiting:** Parent group filtered by region, with subgroups per territory. Regional directors at the top; individual recruiters assigned to their territory subgroup only.

---

# Creating + Managing Existing Visibility Groups

## Creating Visibility Groups

1. Navigate to **Settings** > **Manage** **Users** > **Visibility** **Groups**
2. Click the **+ New Visibility Group** button

   [![](https://downloads.intercomcdn.com/i/o/962202834/e9cd2984bde50c8cee94da16/Screenshot+2024-02-13+at+11_25_42%E2%80%AFAM.png?expires=1784333700&signature=5f0ebada6d7b72b24c98514916c52df25e139b57c65bbb35d7d98afbaf25f8ab&req=fSYlFMl8lYJbFb4f3HP0gJ9mqavnWapH0VtuOxMhVgLmlzodagP3omwE0R%2Ft%0AhN8%3D%0A)](https://downloads.intercomcdn.com/i/o/962202834/e9cd2984bde50c8cee94da16/Screenshot+2024-02-13+at+11_25_42%E2%80%AFAM.png?expires=1784333700&signature=5f0ebada6d7b72b24c98514916c52df25e139b57c65bbb35d7d98afbaf25f8ab&req=fSYlFMl8lYJbFb4f3HP0gJ9mqavnWapH0VtuOxMhVgLmlzodagP3omwE0R%2Ft%0AhN8%3D%0A)
3. Name your visibility group by replacing 'Untitled Group' at the top of the form
4. **Settings**: Provide a brief description of your visibility group that clearly identifies its purpose  
   ​

   [![](https://downloads.intercomcdn.com/i/o/962255269/ac5e1a158dc580de2df6a164/Screenshot+2024-02-13+at+12_17_51%E2%80%AFPM.png?expires=1784333700&signature=c9c539ce488d01670ae164bddca50a255b2fdceafe21757e16bb801640ba0d75&req=fSYlFMx7n4dWFb4f3HP0gF9FT01X13IgeemQLnvfis8NUFQtrLnCOFcT5CPs%0AyJQ%3D%0A)](https://downloads.intercomcdn.com/i/o/962255269/ac5e1a158dc580de2df6a164/Screenshot+2024-02-13+at+12_17_51%E2%80%AFPM.png?expires=1784333700&signature=c9c539ce488d01670ae164bddca50a255b2fdceafe21757e16bb801640ba0d75&req=fSYlFMx7n4dWFb4f3HP0gF9FT01X13IgeemQLnvfis8NUFQtrLnCOFcT5CPs%0AyJQ%3D%0A)
5. **Visibility**: This is where you will establish the main filters for the group. You can also opt to load an existing segment from the segment dropdown for quicker setup. As you apply filters, the number of people who match the criteria of selected filters will be displayed for your review.

   [![](https://downloads.intercomcdn.com/i/o/962255442/55fab8cad0104e34099439c4/Screenshot+2024-02-13+at+12_18_01%E2%80%AFPM.png?expires=1784333700&signature=54dd8a113a36b98153644e9d8c25e0042e00c21164df8f5f9da2c295aed06d61&req=fSYlFMx7mYVdFb4f3HP0gJXWnq2veyyaS4PoCQPBemHO9ZD%2FVKlZEVYw42dU%0AXo4%3D%0A)](https://downloads.intercomcdn.com/i/o/962255442/55fab8cad0104e34099439c4/Screenshot+2024-02-13+at+12_18_01%E2%80%AFPM.png?expires=1784333700&signature=54dd8a113a36b98153644e9d8c25e0042e00c21164df8f5f9da2c295aed06d61&req=fSYlFMx7mYVdFb4f3HP0gJXWnq2veyyaS4PoCQPBemHO9ZD%2FVKlZEVYw42dU%0AXo4%3D%0A)
6. **Subgroups** (Optional): Further narrow down access by creating up to two levels of subgroups within your primary group. Apply **additional** filters to each subgroup to achieve the desired level of visibility. Subgroups inherit all filters from their parent group (shown as read-only), as well as all users assigned to the parent group. Users added directly to the parent will automatically appear in any subgroups beneath it.

   [![](https://downloads.intercomcdn.com/i/o/962255577/29dcbd39788d7acc206d0f3b/Screenshot+2024-02-13+at+12_18_12%E2%80%AFPM.png?expires=1784333700&signature=c348fed204e46731c6a1ea08aa8b8f3626ab3f0da70df07f74486c6ffda454e4&req=fSYlFMx7mIZYFb4f3HP0gPf6YBL%2FRD%2FAO7YjbFNG0Vk7%2BNq2xEmIYe9vvBTK%0A3kE%3D%0A)](https://downloads.intercomcdn.com/i/o/962255577/29dcbd39788d7acc206d0f3b/Screenshot+2024-02-13+at+12_18_12%E2%80%AFPM.png?expires=1784333700&signature=c348fed204e46731c6a1ea08aa8b8f3626ab3f0da70df07f74486c6ffda454e4&req=fSYlFMx7mIZYFb4f3HP0gPf6YBL%2FRD%2FAO7YjbFNG0Vk7%2BNq2xEmIYe9vvBTK%0A3kE%3D%0A)
7. **Add** **Users:** Individually search and add internal users to the visibility group.

   [![](https://downloads.intercomcdn.com/i/o/962255717/fab6c26f60a42ab4fe97e4e6/Screenshot+2024-02-13+at+12_18_22%E2%80%AFPM.png?expires=1784333700&signature=1bdc01cb0039969314abc3285b42ffd69a4d11b5af1efe348fdeb2eb90dab9df&req=fSYlFMx7moBYFb4f3HP0gKlNxoeF4trpooY8kEovJgV%2B4mh%2BIYukaN4eYvJL%0A75g%3D%0A)](https://downloads.intercomcdn.com/i/o/962255717/fab6c26f60a42ab4fe97e4e6/Screenshot+2024-02-13+at+12_18_22%E2%80%AFPM.png?expires=1784333700&signature=1bdc01cb0039969314abc3285b42ffd69a4d11b5af1efe348fdeb2eb90dab9df&req=fSYlFMx7moBYFb4f3HP0gKlNxoeF4trpooY8kEovJgV%2B4mh%2BIYukaN4eYvJL%0A75g%3D%0A)
8. As a final step, you will need to enable the '***Restrict the people visible to this use***r' setting for each user you added in Step 7. To do this:

   * Navigate to the user's profile (**Settings** > **Manage** **Users**).
   * On the user's profile, click on the **Visibility** **Groups** tab.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/963457948/30b5d4c5b011c7aac7758c5b/Screenshot+2024-02-14+at+2_26_21%E2%80%AFPM.png?expires=1784333700&signature=6269ead1ad8fe37f58ab5b4453f7bed68a9020921a57dcab2c4fe6097bab6e84&req=fSYkEsx5lIVXFb4f3HP0gFJ4MTZQsafupFK9mBieNacoGH6L6KzMQxkaJeE0%0AKw4%3D%0A)](https://downloads.intercomcdn.com/i/o/963457948/30b5d4c5b011c7aac7758c5b/Screenshot+2024-02-14+at+2_26_21%E2%80%AFPM.png?expires=1784333700&signature=6269ead1ad8fe37f58ab5b4453f7bed68a9020921a57dcab2c4fe6097bab6e84&req=fSYkEsx5lIVXFb4f3HP0gFJ4MTZQsafupFK9mBieNacoGH6L6KzMQxkaJeE0%0AKw4%3D%0A)
   * Enable the '***Restrict the people visible to this use***r' setting by toggling it on.  
     ​

     [![](https://downloads.intercomcdn.com/i/o/963462988/1200050bef2c36166ab07f11/Screenshot+2024-02-14+at+2_32_42%E2%80%AFPM.png?expires=1784333700&signature=84e57769a7dd4ca0da574407a4dc6391938ff8d9787fa5fb162b322126bb15aa&req=fSYkEs98lIlXFb4f3HP0gNaZCBGjHhuXZI%2F%2BN89LO4C%2FmaIajyX1Qy%2F2hpqm%0AASM%3D%0A)](https://downloads.intercomcdn.com/i/o/963462988/1200050bef2c36166ab07f11/Screenshot+2024-02-14+at+2_32_42%E2%80%AFPM.png?expires=1784333700&signature=84e57769a7dd4ca0da574407a4dc6391938ff8d9787fa5fb162b322126bb15aa&req=fSYkEs98lIlXFb4f3HP0gNaZCBGjHhuXZI%2F%2BN89LO4C%2FmaIajyX1Qy%2F2hpqm%0AASM%3D%0A)
   * The visibility group should already be selected for this user if you added them during the creation process (Step 7). You can also add additional visibility groups to the user by checking the relevant boxes.

## Adding + Removing Users

Managing users in a Visibility Group can be done in two ways: directly from the group or via the user's profile. Your choice depends on your needs. For multiple changes in the same group, the first option is more efficient.

**Option 1**: Adjust user access within the Visibility Group:

1. Navigate to **Settings** > **Manage** **Users** > **Visibility** **Groups**.
2. Click on the Visibility Group of your choosing.
3. From the Users tab, add or remove users.

**Option 2**: Adjust user access within the user's profile:

1. Navigate to **Settings** > **Manage** Users.
2. Click on the user's name.
3. Click on the Visibility Groups tab at the top.
4. Check/uncheck the boxes of the visibility groups you wish to add/remove.

## Editing a Visibility Group (Subgroups, Visibility)

1. Navigate to **Settings** > **Manage** **Users** > **Visibility** **Groups**.
2. Click on the Visibility Group of your choosing.
3. Make your edits

   * To edit the visibility filters/segments, use the **Visibility** tab at the top. After making your adjustments, be sure to click the blue **Apply** button to save your changes.
   * To edit the subgroups, use the **Subgroups** tab at the top. You have the option to add additional subgroups, edit an existing subgroup (pencil icon), or delete a subgroup (trashcan icon).

## Deleting a Visibility Group

1. Navigate to **Settings** > **Manage** **Users** > **Visibility** **Groups**.
2. Click the three vertical dots icon to the right of the Visibility Group you wish to delete.
3. Click delete. You'll be asked to confirm your action.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/963486762/5346db694c6c7ae1749f42b2/Screenshot+2024-02-14+at+2_59_18%E2%80%AFPM.png?expires=1784333700&signature=8c43b77f473d109aee8ba8dd9e75e79ef725073db7d1c8cf99b59814258ae007&req=fSYkEsF4moddFb4f3HP0gJlkO4x9L6KrkkpeZaeLAqpZ2%2Bp69rSr1BaagOAp%0APqc%3D%0A)](https://downloads.intercomcdn.com/i/o/963486762/5346db694c6c7ae1749f42b2/Screenshot+2024-02-14+at+2_59_18%E2%80%AFPM.png?expires=1784333700&signature=8c43b77f473d109aee8ba8dd9e75e79ef725073db7d1c8cf99b59814258ae007&req=fSYkEsF4moddFb4f3HP0gJlkO4x9L6KrkkpeZaeLAqpZ2%2Bp69rSr1BaagOAp%0APqc%3D%0A)

**Note:** Deleting a parent group automatically deletes all of its subgroups. If you want to preserve a subgroup, delete or reassign it before removing the parent group.

📌 Important: If a user is added as the assignee to a contact record they will gain access to that contact regardless of visibility group settings.

---

# Visibility Groups & Related Entities

Visibility Groups control access to contact records by limiting which users can view specific contact profiles.  
​

These restrictions also affect related data across the platform. See how Visibility Groups impact each feature below.  
​

## Conversations

Users who do not have access to a contact **cannot see conversations** associated with that contact in the Conversations inbox.  
​

**Exception:**  
If a conversation is assigned to a user or their team, they will still have access to that specific conversation.

## Tasks

Users who do not have access to a contact **cannot see tasks** associated with that contact in the Tasks list.  
​

**Exceptions:**

* If a task is assigned to a user or their team, they will still have access to that task
* Users subscribed to a task will also retain visibility, regardless of Visibility Group restrictions

## Appointments

Users who do not have access to a contact **cannot see appointments** associated with that contact in the Appointments list.

​**Exception:**  
If an appointment is assigned to a user or their team, they will still have access to that specific appointment.

​  
​

---