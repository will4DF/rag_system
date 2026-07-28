---
title: Bolt Agent Teams
url: https://help.element451.com/en/articles/12068259-bolt-agent-teams
collection: Bolt AI
---

# Overview

Bolt Agent **Teams** control how and where your agents are deployed across student communication channels—**Messenger, SMS, Email, and WhatsApp**. Simply activating an agent doesn’t make it accessible to students—it must be assigned to a team.

Teams let you decide when and where an agent appears using conditions such as Page URL, Path URL, UTM Parameters, or Conversation Channel. This enables the display of the right agent(s) to the right students at the right time.

👉 **Important:** Teams do **not** apply to the **Phone channel** or to **Bolt Agent Jobs**.

For example, you might create an **Athletics Team** that includes an Athletics Advisor and an Admissions Advisor, configured to appear only on pages containing “athletics” in the URL. This ensures the right audience connects with the right team for assistance.

---

# Key Considerations for Teams

* **Sequential order:** Teams are checked in order from top to bottom.
* **Conditions must be met:** The first team whose conditions are met becomes active.
* **Fallback team:** Always have one “default team” with no conditions, placed last in the list. This ensures there’s always a backup if no other team matches.
* **Logical grouping:** Build teams around areas of expertise (e.g., Financial Aid, Admissions, Athletics). This makes agent handoffs smoother and ensures students connect with the most qualified agent.

---

# Messenger vs. Other Channels

Teams are most **powerful and customizable on Messenger** because you can apply multiple conditions, including **Page URL, Path URL, and UTM Parameters.** This allows you to scope your deployment with precision.

Other channels do not use Messenger's Page URL, Path URL, or UTM conditions. Email can be limited by contact segment and connected Email address; SMS can be limited by contact segment and receiving phone number; WhatsApp can be limited by contact segment. These restrictions apply at the Team level and do not map a destination directly to one specific Bolt Agent.

---

# How-To: Add a Team

1. Navigate to **Engagement** > **Bolt Agents**.
2. Locate the **Teams** section.
3. Click **+ Add Bolt Agents Team.**
4. **Settings Tab**: Configure the **settings** for the team.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921092158/e90baef2ae40b46ea2c77cc74beb/CleanShot+2026-01-08+at+10_33_32.png?expires=1784333700&signature=081f6a093ced6f4f3305720d64c5d7152e615a2c5626881ff913de957a626e86&req=dSklF8l3n4BaUfMW1HO4zVGzumJIGxz6m%2BUX3VVyRH%2BpnT0Cuy29ypx7kHc9%0AhPuR%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921092158/e90baef2ae40b46ea2c77cc74beb/CleanShot+2026-01-08+at+10_33_32.png?expires=1784333700&signature=081f6a093ced6f4f3305720d64c5d7152e615a2c5626881ff913de957a626e86&req=dSklF8l3n4BaUfMW1HO4zVGzumJIGxz6m%2BUX3VVyRH%2BpnT0Cuy29ypx7kHc9%0AhPuR%0A)

   * **Name**: Enter a name for the team in the header.
   * **Channels**: Specify which conversation channel(s) the team of Agents will respond to inbound messages on: Live Chat, Email, SMS, and/or WhatsApp.

     + This setting serves as the central control to enable/disable the team.
     + When all chips are disabled (gray), all agents are disabled.
     + *📌 **Note:** The agent will optimize its response based on the channel (e.g., SMS responses will be approximately 160 characters, and email responses will include greetings).*
   * **Channel Settings**: Separate settings sections dynamically appear for each channel where the team is active. These settings are configured based on the channels enabled.

     + If you don’t see a specific channel’s settings card (e.g., Messenger, Email, SMS, or WhatsApp), it’s likely because the channel hasn’t been enabled. Ensure the desired channel is selected to make its corresponding settings card available.
     + For details on channel-specific settings, see the [Channel Settings](#h_f1291ac59e) section below.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921094526/4457bdeaa72cda0377f3b52e0a0b/CleanShot+2026-01-08+at+10_34_34.png?expires=1784333700&signature=8919d901e376affb689a7be670fa215616a128f247740466c93134867c8dce48&req=dSklF8l3mYRdX%2FMW1HO4zZ6uN4vQlv3UT3friTgD7WLBm3Seuy7l6tElMXed%0AOfh6%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921094526/4457bdeaa72cda0377f3b52e0a0b/CleanShot+2026-01-08+at+10_34_34.png?expires=1784333700&signature=8919d901e376affb689a7be670fa215616a128f247740466c93134867c8dce48&req=dSklF8l3mYRdX%2FMW1HO4zZ6uN4vQlv3UT3friTgD7WLBm3Seuy7l6tElMXed%0AOfh6%0A)
5. **Agents Tab:** Add Agent(s) to the team.

   * Use the checkboxes to select which agent(s) you wish to add to the team.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921099414/f7b112d742faa3f117823dc58bbd/CleanShot%2B2026-01-08%2Bat%2B10_35_20.png?expires=1784333700&signature=e5cde0e1627c63fc48bad55d21c048837f79eca501cf288cb1b96e210024c805&req=dSklF8l3lIVeXfMW1HO4zZmCjIGfTz%2BciFVnGUkiZCRc1VVnWSH%2Bet%2FNfvvp%0A0ZCP%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921099414/f7b112d742faa3f117823dc58bbd/CleanShot%2B2026-01-08%2Bat%2B10_35_20.png?expires=1784333700&signature=e5cde0e1627c63fc48bad55d21c048837f79eca501cf288cb1b96e210024c805&req=dSklF8l3lIVeXfMW1HO4zZmCjIGfTz%2BciFVnGUkiZCRc1VVnWSH%2Bet%2FNfvvp%0A0ZCP%0A)
6. Click **Save** in the top right corner to save your new team.

---

# Channel Settings (Messenger, Email, SMS, WhatsApp)

Separate settings sections dynamically appear for each channel where the team is active. These settings allow you to add rules that control when the team should appear within that channel.

## Messenger

* **Messenger Conditions:** This setting allows you to specify the pages where agents will be active within Messenger using filters for Page URL, Path URL, and UTM Parameters.

## Email

* **Limit Email to a Segment:** Restrict Bolt Agent email replies to contacts in selected segments. When enabled, agents will only respond to emails from contacts who belong to the segment(s) you specify.

  + ✨ **Pro Tip:** This setting is a great way for you to test Bolt Agent email responses before enabling it for your students (add yourself and other testers to a test segment and select it here.)
* **Limit Email to Email Addresses**: Restrict Bolt Agent email replies to certain [connected email addresses](https://help.element451.com/en/articles/6321778-adding-email-inboxes-to-conversations-outlook-gmail-forwarding). When enabled, agents will only respond to emails sent to the address(es) you specify.  
  ​

## SMS

* **Limit SMS to a Segment:** Restrict Bolt Agent SMS replies to contacts in selected segments. When enabled, agents will only respond to SMS messages from contacts who belong to the segment(s) you specify.

  + ✨ **Pro Tip**: This setting is a great way for you to test Bolt Agent SMS responses before enabling it for your students (add yourself and other testers to a test segment and select it here.)
* **Limit SMS to Phone Numbers**: Restrict Bolt Agent SMS replies to specific [phone numbers](https://help.element451.com/en/articles/8400679-phone-calling). When enabled, agents will only respond to SMS messages sent to the number(s) you specify.

## WhatsApp

* **Limit WhatsApp to a Segment:** Restrict Bolt Agent WhatsApp replies to contacts in selected segments. When enabled, agents will only respond to WhatsApp messages from contacts who belong to the segment(s) you specify.

  + ✨ **Pro Tip**: This setting is a great way for you to test Bolt Agent WhatsApp responses before enabling it for your students (add yourself and other testers to a test segment and select it here.)

---

# How-To: Edit + Delete Team

1. Go to **Engagement > Bolt Agents**.
2. In the **Teams** section, find the team you want to edit or delete.
3. Click the three-dot menu on the right.
4. Select **Edit** or **Delete**. (If deleting, you’ll be asked to confirm.)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921485891/1a848dd217f1c507a89b59219da4/CleanShot+2026-01-08+at+12_28_57.png?expires=1784333700&signature=51e20a4c9a767ebc180f48db285676c3c243c791248b7d7230033a10985a036e&req=dSklF812mIlWWPMW1HO4zY%2BMRla05vpp2tojwYKa7LaJUXMkcfZA8BNaQ4L3%0A%2F4V5tmh8vxhEkgiOlWQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921485891/1a848dd217f1c507a89b59219da4/CleanShot+2026-01-08+at+12_28_57.png?expires=1784333700&signature=51e20a4c9a767ebc180f48db285676c3c243c791248b7d7230033a10985a036e&req=dSklF812mIlWWPMW1HO4zY%2BMRla05vpp2tojwYKa7LaJUXMkcfZA8BNaQ4L3%0A%2F4V5tmh8vxhEkgiOlWQ%3D%0A)

---

# Reordering Teams

Team conditions are evaluated **top to bottom**. Use the drag handles (represented by two horizontal lines) to adjust the order.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921489329/14643c428595dfdca02a7fe151f0/CleanShot+2026-01-08+at+12_29_58.png?expires=1784333700&signature=9d3b7eb934642cec7543975b8158737c3c80b2784235b768930d9b52b4ba9b1e&req=dSklF812lIJdUPMW1HO4zYc8ZnwMWJD6KM2xk4A4DBbAe%2BfUljS1aLScn3OG%0Al8XqvP1yQRELiJeLouI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1921489329/14643c428595dfdca02a7fe151f0/CleanShot+2026-01-08+at+12_29_58.png?expires=1784333700&signature=9d3b7eb934642cec7543975b8158737c3c80b2784235b768930d9b52b4ba9b1e&req=dSklF812lIJdUPMW1HO4zYc8ZnwMWJD6KM2xk4A4DBbAe%2BfUljS1aLScn3OG%0Al8XqvP1yQRELiJeLouI%3D%0A)

🚨 **Important**: Place your “default” team without conditions at the bottom, or any teams below it will be ignored.

---

# Automatic Team Handoffs

Bolt Agents can automatically hand off a query to another agent in the same team when that agent is better suited to help. This automatic team behavior is separate from a configured Custom Skill @Hand Off to Agent action.

* Automatic same-team handoffs: Automatic handoffs can only select another agent assigned to the same team. A configured Custom Skill @Hand Off to Agent action can target an agent outside that team.
* Automatic process: Same-team handoffs happen automatically and have no separate enable/disable setting. Explicit Custom Skill handoffs are configured, enabled, and prioritized on the source agent.
* **Internal Descriptions:** Each agent has an **internal description** setting (explained in the [Onboarding + Managing Bolt Agents for Students](https://help.element451.com/en/articles/11426404-onboarding-managing-bolt-agents-for-students) article). This field provides context about the agent's skills and knowledge areas. Internal descriptions are readable by other agents on the same team, enabling them to determine when a handoff is appropriate.
* Default Agent: The default agent does not use automatic team handoffs. It can use a configured Custom Skill @Hand Off to Agent action. Configure its Knowledge and built-in skills for its fallback role, then enable any explicit Custom Skills it should use.

---