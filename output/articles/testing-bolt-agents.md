---
title: Testing Bolt Agents
url: https://help.element451.com/en/articles/8993362-testing-bolt-agents
collection: Bolt AI
---

# Overview

Test every Bolt Agent before launch. Start with Test Agent: open the agent at Engagement > Bolt Agents, click Test Agent, select a channel, test messages that should and should not trigger the expected behavior, and review Response Details for evaluated skills, matching, priority, and simulated tool actions. Repeat for each supported channel you plan to enable. Test Agent does not create contacts, send messages, place calls, complete registrations, or execute other live actions. Then complete a controlled live end-to-end test for each enabled channel.

---

# Controlled Live Test: Messenger

### Step-by-Step Tutorial

1. Create a test page (for help creating a page, [click here](https://help.element451.com/en/articles/2582895-creating-a-page)).
2. In the **setup** tab of your new page, toggle on **Activate Element Messenger.**
3. Navigate to Bolt Agents settings (**Engagement** > **Bolt Agents)**.
4. **Create your Agents**: Create as many agents as you would like to test. You can also test using only your default agent, but if you plan to utilize multiple agents, we recommend testing after you have created all of them.
5. **Create a Team**: Create a new Agent Team. Within the settings for that team, add a page URL condition. Use the URL of the test page you created in step one. This will limit the Team to only display on your test page.
6. Open the live URL of your test page.
7. Use the messenger widget and the Conversations module to chat and test.
8. Once done testing, delete the page or keep it for future testing and remove the condition.

---

# Controlled Live Test: Email and SMS

### Step-by-Step Tutorial

1. Create a test segment with only test users (for help creating a segment, [click here](https://help.element451.com/en/articles/1474208-creating-a-segment))
2. Navigate to Bolt Agents settings (**Engagement** > **Bolt Agents)**.
3. Locate the SMS Settings and Email Settings sections.
4. Open the test Team at Engagement > Bolt Agents > Teams. In its Email or SMS channel settings, enable Limit to a Segment and select the test segment created in step one.
5. Send an email and/or SMS message using a cell phone number or email associated with a user in your test segment.

###

---