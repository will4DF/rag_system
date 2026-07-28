---
title: Network: Connect Contacts with Internal Users
url: https://help.element451.com/en/articles/9884014-network-connect-contacts-with-internal-users
collection: StudentHub
---

# Overview

Element451's Network feature enables powerful student support by connecting students to their personalized **Network.**

A student's Network is a group of **internal** **users** like your staff and faculty who support their academic journey. Through [StudentHub](https://intercom.help/element451/en/articles/9827408-getting-started-with-studenthub), students can access comprehensive contact details, engage in direct communication, and manage appointments with their support team, all in one unified interface.

## Key Features

Each **Connection** within the **Network** is defined by a **Role**, detailing the internal user's specific support function for the student. This structured approach ensures students know who to contact for academics, housing, financial aid, and other support needs. We explain [connections](#h_a4a6c59d55) and [roles](#h_b43b5700e7) in subsequent sections.

### 🏫 Connection Details + Contact Info

Students can access detailed information about each connection in their Network, including:

* Name and assigned role
* Email address
* Office location: building\*
* Office location: room number\*
* Phone number\*

This information appears on the first card of the connection's details page. Email addresses and phone numbers are tappable, launching the student's native mobile apps for quick communication.

*\*These fields pull data from the internal user's profile. They can be edited in Manage Account (individuals) and Manage Users (administrators). Additionally, these fields appear on network details when data is provided.*

### 💬 Conversations Integration

Students can communicate **directly** with their connections through Element451's Conversations module:

* View their complete conversation history where the connection was the conversation assignee
* Start new conversations via messenger (live chat)\*
* When students initiate conversations through Network, the system automatically:

  + Assigns the conversation to the internal user (connection)
  + Marks the conversation as private

The Conversations card appears second on the details page, displaying the conversation history. When direct messaging is enabled, a chat button appears at the bottom of the page in your institution's primary color.

*\*Students can start new direct messenger conversations only if the connection has enabled “Allow Direct Messages from Network Connections?” This setting can be managed in **Manage Account** (for individuals) or **Manage Users** (for administrators). While internal users can reply to these messages, they cannot initiate new direct messenger conversations with students.*

### 🗓️ Appointments Integration

Students can view upcoming appointments with their connections and schedule new ones directly from the Network page.

The appointment information is displayed through two dedicated cards:

* **Upcoming Appointments**

  + Lists all scheduled appointments with the connection
  + Displays "No appointments" when none are scheduled
* **Book an Appointment**

  + Shows current availabilities for the connection
  + Students can select an available time to schedule directly from this list

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205107283/1012d9d56fc585c5551b7e3a8fb0/Untitled+design+%281%29.png?expires=1784333700&signature=496a69f6b58e1438c5df8e4bcb69568d424718cf6d0ec291dad1dcb50770084e&req=dSInE8h%2BmoNXWvMW1HO4zd9t9XFI%2BOKgWFlSKkiyH054b66zo8iJxqWj5nod%0ALd5%2FNpKKaeJz8CecrUQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205107283/1012d9d56fc585c5551b7e3a8fb0/Untitled+design+%281%29.png?expires=1784333700&signature=496a69f6b58e1438c5df8e4bcb69568d424718cf6d0ec291dad1dcb50770084e&req=dSInE8h%2BmoNXWvMW1HO4zd9t9XFI%2BOKgWFlSKkiyH054b66zo8iJxqWj5nod%0ALd5%2FNpKKaeJz8CecrUQ%3D%0A)

---

# Accessing + Viewing a Network

## Students via StudentHub

Network is exclusively available through **StudentHub** under the **Resources** section. Here, students can view all their connections and select any connection to access their details page. The details page provides comprehensive access to their connection's profile information, conversation history, and appointment management all in one place.

[Explore More: StudentHub →](https://help.element451.com/en/articles/9854238-student-portals-pages-features-explained)

## Internal Users via Person Profile

You and your team members can access a student’s connections through their **Contact Profile**. The **Network** profile card displays all assigned roles and connections.   
​

[Explore More: Person Profile →](https://help.element451.com/en/articles/1475735-the-person-profile)

---

# Roles

The **Network Role** is a specific title or function assigned to internal users, indicating how they are connected to or support a student (e.g., Academic Coach, Program Advisor).

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205587894/7ced7695ad3eed2ec77f81b353c3/Hub+-+Network+Roles+Settings%402x.png?expires=1784333700&signature=8bc5dbaf9996b3828f07a11c24475ac2c280f2b08387c4d9866a2a25ad83d76b&req=dSInE8x2molWXfMW1HO4zRGkmBKzzl28qqzbsyTWcPAD0YelQZ%2BzvE79ihAU%0A2g5VKCLqbOaJpGqEaZM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205587894/7ced7695ad3eed2ec77f81b353c3/Hub+-+Network+Roles+Settings%402x.png?expires=1784333700&signature=8bc5dbaf9996b3828f07a11c24475ac2c280f2b08387c4d9866a2a25ad83d76b&req=dSInE8x2molWXfMW1HO4zRGkmBKzzl28qqzbsyTWcPAD0YelQZ%2BzvE79ihAU%0A2g5VKCLqbOaJpGqEaZM%3D%0A)

Before assigning connections, you must establish roles**.** You can add as many roles as you need, aligning with your institution's structure.

💡 **Network Roles power dynamic assignment across the platform.** Instead of naming a fixed person, you can assign work using a **Network Role token**, and the field resolves to whoever holds that role for the student—so a grade alert routes to that student's Academic Advisor and a financial case to their Financial Aid Counselor, automatically. Network Role is available as a dynamic assignee in:

* **Case Management**: set the **Reviewer** (Alerts) or **Assignee** (Cases) from Case Management Automation Rules or the Workflows + Rules module. See [Automating Case Management](https://help.element451.com/en/articles/14712713-automating-case-management-closed-beta).
* **Conversation Rules**: the **Assign To** and **Assign To and Mark as Private** actions. See [Conversation Rules](https://help.element451.com/en/articles/1930478-conversation-rules).
* **Workflows + Rules**: the **Create Task** action.

## How to Create a Role

1. Navigate to the **Contacts** > **Categories** > **Network** **Roles**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205592954/eca8833826d807c578d3f94d2b5d/Hub+-+Network+Role+Nav%402x.png?expires=1784333700&signature=b954903a7cb2ab070d633e726bd0d0c0cc15c2b08e667cf4d08714a928dc3959&req=dSInE8x3n4haXfMW1HO4zUZqJHWly4DxBCAZRNKXHPNCN%2F3yRNSvFRuTejYA%0ACqBa%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205592954/eca8833826d807c578d3f94d2b5d/Hub+-+Network+Role+Nav%402x.png?expires=1784333700&signature=b954903a7cb2ab070d633e726bd0d0c0cc15c2b08e667cf4d08714a928dc3959&req=dSInE8x3n4haXfMW1HO4zUZqJHWly4DxBCAZRNKXHPNCN%2F3yRNSvFRuTejYA%0ACqBa%0A)
2. In the top right corner, click the **+ Add Network Role** button in the top right corner.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205597067/b4254d518b5fe5089dcdef57d2cf/Hub+-+Network+-+Add+Network+Role%402x.png?expires=1784333700&signature=096407284152b70cc69abb6e3293e60f02b4b7822fa422b1252cec1ced5e186a&req=dSInE8x3moFZXvMW1HO4zVn%2BQtsT0wvMpc7rbA2Y%2FTVlzp4xozJI6AKkYhpo%0AzvY8%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205597067/b4254d518b5fe5089dcdef57d2cf/Hub+-+Network+-+Add+Network+Role%402x.png?expires=1784333700&signature=096407284152b70cc69abb6e3293e60f02b4b7822fa422b1252cec1ced5e186a&req=dSInE8x3moFZXvMW1HO4zVn%2BQtsT0wvMpc7rbA2Y%2FTVlzp4xozJI6AKkYhpo%0AzvY8%0A)
3. Add a name for your new network role and click **Save**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205599910/b98ac8472616450da9e33fa3063a/Hub+-+New+Network+Role+Name.png?expires=1784333700&signature=dbdb1bab51290cab11367ee3eb154119daaa036bf93ff69b85d48c93af3a4592&req=dSInE8x3lIheWfMW1HO4zVdSRH8M8J32N7UwjL6AuQmtGPrBZUR6GIMxpIm%2B%0AtKjn%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205599910/b98ac8472616450da9e33fa3063a/Hub+-+New+Network+Role+Name.png?expires=1784333700&signature=dbdb1bab51290cab11367ee3eb154119daaa036bf93ff69b85d48c93af3a4592&req=dSInE8x3lIheWfMW1HO4zVdSRH8M8J32N7UwjL6AuQmtGPrBZUR6GIMxpIm%2B%0AtKjn%0A)

## How to Edit + Delete a Role

* **Edit**: To **edit** a network role name, simply click on the name within the list to activate the text box, allowing you to make changes directly.
* **Delete**: To delete a network role, click the more icon (three vertical dots) and select delete.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205602090/a9403cfc1e3e3e09eff38c473c15/Hub+-+Network+-+Role+-+Edit+Delete.png?expires=1784333700&signature=b0c7e912d025a9f8d45153e0b40acb73428f6ed14f5427aacd15c7a3309aaddd&req=dSInE89%2Bn4FWWfMW1HO4zRlRjlfIawjJhCbXwI1OBa1WvttyKC47Jz0vRZ2e%0AnUQkaTHqxSdu0EOAEJg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205602090/a9403cfc1e3e3e09eff38c473c15/Hub+-+Network+-+Role+-+Edit+Delete.png?expires=1784333700&signature=b0c7e912d025a9f8d45153e0b40acb73428f6ed14f5427aacd15c7a3309aaddd&req=dSInE89%2Bn4FWWfMW1HO4zRlRjlfIawjJhCbXwI1OBa1WvttyKC47Jz0vRZ2e%0AnUQkaTHqxSdu0EOAEJg%3D%0A)

---

# Connections

The relationship that links a student to an internal user, defined by a designated role within the Network, is called a **Connection**.

You can create network connections between students and internal users manually or automatically using the Workflows + Rules module.

## How to Create a Connection - Manually

To **manually** create a connection:

1. Open the student's **Contact Profile**.
2. Locate and open the **Network** profile card.

   * [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205613496/59e4292f6cf34771fc338afd81fe/Note.png?expires=1784333700&signature=ecf6b4ae34764a50e5b6184117e6dfbd4393765a55f30277210900ef7a0ff3de&req=dSInE89%2FnoVWX%2FMW1HO4zaUq5As%2B6W9GxJKSa5dm%2Bagbue2jBoIITbzqFEqf%0AjmYR%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205613496/59e4292f6cf34771fc338afd81fe/Note.png?expires=1784333700&signature=ecf6b4ae34764a50e5b6184117e6dfbd4393765a55f30277210900ef7a0ff3de&req=dSInE89%2FnoVWX%2FMW1HO4zaUq5As%2B6W9GxJKSa5dm%2Bagbue2jBoIITbzqFEqf%0AjmYR%0A)

     You may need to add it to your [profile template](https://help.element451.com/en/articles/6449965-bolt-profile-templates) if you don't see it.
3. Click the **+ Add Network** button.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205612719/8c77358ab8a4102db98c83c66f29/Hub+-+Network+-+Add+new.png?expires=1784333700&signature=3dad74c5c692e7b80eb542235f86601488def6c3e6f3b2e58055b2cfcb3153fd&req=dSInE89%2Fn4ZeUPMW1HO4zU1I4Oq0Ir5YVLzeOm2%2BM7GqC3MD9gELS0h0jp8K%0AxpkA%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205612719/8c77358ab8a4102db98c83c66f29/Hub+-+Network+-+Add+new.png?expires=1784333700&signature=3dad74c5c692e7b80eb542235f86601488def6c3e6f3b2e58055b2cfcb3153fd&req=dSInE89%2Fn4ZeUPMW1HO4zU1I4Oq0Ir5YVLzeOm2%2BM7GqC3MD9gELS0h0jp8K%0AxpkA%0A)
4. Select the appropriate **Internal User** and the **Role** they will serve for that student, followed by **Save**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205614997/e1afe056954a7a8f94e76de236cc/Network+-+Add+Network.png?expires=1784333700&signature=0cd3af41c3ad138b9991272713b9817e99a62a7078a0cf03d29dcfccebca51df&req=dSInE89%2FmYhWXvMW1HO4zZrjsyR2quhcMc7CT6B0GJPycJNB4SDl8QTRh0kO%0A0kKQ%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205614997/e1afe056954a7a8f94e76de236cc/Network+-+Add+Network.png?expires=1784333700&signature=0cd3af41c3ad138b9991272713b9817e99a62a7078a0cf03d29dcfccebca51df&req=dSInE89%2FmYhWXvMW1HO4zZrjsyR2quhcMc7CT6B0GJPycJNB4SDl8QTRh0kO%0A0kKQ%0A)

## Adding Connections - via Workflows + Rules

Please note that you should have a working knowledge of creating workflows and rules before automating network connection creation.

### Step 1: Create the Workflow or Rule

If you're unfamiliar with this process, please refer to our help article, [Getting Started with Workflows + Rules](https://help.element451.com/en/articles/1500265-getting-started-with-workflows-rules), for assistance.

### Step 2: Add Step with "Add Network Connection" Action

Add the action type, **Add Network Connection**, within your new workflow or rule. This action automates the creation of the connection.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205659684/c6ea0eaf666ea15c86a6d4bd719e/Network+-+Workflow+Action.png?expires=1784333700&signature=5daf9bb5c587b4b1b20a2d5fb4c6a5c2d2db93d000400f258d77c93db5fcc00c&req=dSInE897lIdXXfMW1HO4zZ9vasyQlNU%2BDgjwZz12ZQTaWPctvpxnquICuv%2Bg%0Az5d%2FTa%2F2g8eIOlnAkQ0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205659684/c6ea0eaf666ea15c86a6d4bd719e/Network+-+Workflow+Action.png?expires=1784333700&signature=5daf9bb5c587b4b1b20a2d5fb4c6a5c2d2db93d000400f258d77c93db5fcc00c&req=dSInE897lIdXXfMW1HO4zZ9vasyQlNU%2BDgjwZz12ZQTaWPctvpxnquICuv%2Bg%0Az5d%2FTa%2F2g8eIOlnAkQ0%3D%0A)

### Step 3: Configure Task Details

Once the action has been added, you will be prompted to configure the **user** and **role** of the connection:

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205662288/b959724a1ec9dd4b7b1a9631639e/Network+-+Workflow+Action.png?expires=1784333700&signature=0444a93e3ef04804390d306856c7343fd0d459d212712f408b587a14a11645ba&req=dSInE894n4NXUfMW1HO4zYQVFQkUlcbgz0gACnO7cDiAMBGqI4tqBZbwsP8J%0Ah%2B8FBjjnapKZQP0GsKU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205662288/b959724a1ec9dd4b7b1a9631639e/Network+-+Workflow+Action.png?expires=1784333700&signature=0444a93e3ef04804390d306856c7343fd0d459d212712f408b587a14a11645ba&req=dSInE894n4NXUfMW1HO4zYQVFQkUlcbgz0gACnO7cDiAMBGqI4tqBZbwsP8J%0Ah%2B8FBjjnapKZQP0GsKU%3D%0A)

### Step 4: Activate Your Workflow or Rule

Once you’ve configured all the necessary steps, actions, and triggers, your workflow or rule will handle the process for you. As students meet the criteria to enter the workflow or rule, they’ll automatically be assigned a network connection based on the settings established in Step 3. Sit back and let automation do the work!

## Editing + Deleting

1. Open the student's **Contact Profile**.
2. Locate and open the **Network** profile card.

   * [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205613496/59e4292f6cf34771fc338afd81fe/Note.png?expires=1784333700&signature=ecf6b4ae34764a50e5b6184117e6dfbd4393765a55f30277210900ef7a0ff3de&req=dSInE89%2FnoVWX%2FMW1HO4zaUq5As%2B6W9GxJKSa5dm%2Bagbue2jBoIITbzqFEqf%0AjmYR%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205613496/59e4292f6cf34771fc338afd81fe/Note.png?expires=1784333700&signature=ecf6b4ae34764a50e5b6184117e6dfbd4393765a55f30277210900ef7a0ff3de&req=dSInE89%2FnoVWX%2FMW1HO4zaUq5As%2B6W9GxJKSa5dm%2Bagbue2jBoIITbzqFEqf%0AjmYR%0A)

     You may need to add it to your [profile template](https://help.element451.com/en/articles/6449965-bolt-profile-templates) if you don't see it.
3. Click the more icon (three vertical dots).
4. Select **Delete**.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205667752/ebdcacf70294a6871609299f6d7e/Network+-+Delete+COnnection.png?expires=1784333700&signature=55d10a3da6b2ad1a61a241e4aeb61fe3e51fdfc780e138886885f9fd4f2cdd2d&req=dSInE894moZaW%2FMW1HO4zUrQQGfsTREtUoy9Gp3PmhFvnxz1a%2B5ziCU9FJTj%0AT%2BsrVQnMBi6t91Apnrc%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205667752/ebdcacf70294a6871609299f6d7e/Network+-+Delete+COnnection.png?expires=1784333700&signature=55d10a3da6b2ad1a61a241e4aeb61fe3e51fdfc780e138886885f9fd4f2cdd2d&req=dSInE894moZaW%2FMW1HO4zUrQQGfsTREtUoy9Gp3PmhFvnxz1a%2B5ziCU9FJTj%0AT%2BsrVQnMBi6t91Apnrc%3D%0A)

---

# Workflow/Rule Example

Below is an example of a rule that automates the connection creation process. In this example:

* The **Joined Segment** *trigger* determines which students are processed by the rule when they join the calculated segment (nursing students with last names A-L).
* The **Add Network Connection** action is then executed, creating a connection for the student and assigning the designated internal user to the **Academic Advisor** role.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205690651/b1674c336e96548b7a42baece849/Network+-+Workflow+Example2.png?expires=1784333700&signature=249e4cec03672f8c0359a2aa48a8e6c310e1051c380684d1362549428a76e260&req=dSInE893nYdaWPMW1HO4zQEJ6n0EtwztfNSG6uByqfPij%2Be%2B3pIhe6ua9pu%2F%0A3yeG3atLxWBecyNL8P8%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1205690651/b1674c336e96548b7a42baece849/Network+-+Workflow+Example2.png?expires=1784333700&signature=249e4cec03672f8c0359a2aa48a8e6c310e1051c380684d1362549428a76e260&req=dSInE893nYdaWPMW1HO4zQEJ6n0EtwztfNSG6uByqfPij%2Be%2B3pIhe6ua9pu%2F%0A3yeG3atLxWBecyNL8P8%3D%0A)

---