---
title: Bolt Agent Handoffs
url: https://help.element451.com/en/articles/8993398-bolt-agent-handoffs
collection: Bolt AI
---

Handoffs allow unresolved Bolt Agent conversations to be passed to a human. Learn how to enable handoffs and rules to customize the process.

# Overview

This article covers the native Human Team Member Handoff for digital conversations. Use it when a Bolt Agent cannot resolve an inquiry or a student asks for a person, and a Conversation Rule should assign the conversation or run another follow-up action.

This native human handoff path requires configuration. It is separate from a Custom Skill's configured @Transfer Call and @Hand Off to Agent actions.

Two components drive native human handoffs. Configured Custom Skill @Transfer Call and @Hand Off to Agent actions do not require these components:

* **Team Member Handoff Skill**
* **Conversation Rule** with the **Bolt Agent Handoff Intent** condition

This article will explore each component in detail and explain how to configure both.

---

# Human Team Member Handoff Skill

Bolt Agents include various specialized skills to enhance its task-oriented capabilities. One such skill, Human Team Member Handoff, enables or disables the native human handoff flow for that agent. It does not control configured Custom Skill transfers or agent-to-agent Custom Skill handoffs. Agent skills are managed by navigating to Engagement > Bolt Agents. You can read more about agent skills here.

## Disabling Handoff

If you don't wish to use handoffs, simply disable the Human Team Member Handoff skill. When the agent cannot resolve a query or a student asks to speak with a representative, instead of offering to transfer to a member of your team, it will search your Knowledge Hub for contact information to share with the student. If you have the **Schedule Appointments** skill enabled, the agent can help the student book an appointment with someone from your team.

![](https://downloads.intercomcdn.com/i/o/1060307242/a73ed1aa3ff6c44032cbecb5/Pro+Tip+-+Orng.png?expires=1784430000&signature=ab6b7501a80279fe805f0efca0bfa448d7f412fde41850eb1f2d9894dac1872a&req=dSAhFsp%2BmoNbW%2FMW3Hu4ga%2FOIetC%2BtODTC7ERcWsHSFW9Pr0T5yZNRxuvXZj%0AlA%3D%3D%0A) Disabling this skill can be useful during extended university closures, like winter break. For more recommendations on managing handoffs when your campus is closed, check out [this article](#h_0d084e0e07).

## Enabling Handoff

When you enable the Human Team Member Handoff skill, the agent will initiate a handoff (offer to connect them with a human team member) if it exhausts all help options or the student requests a human agent. Once the student confirms they want to be connected with someone, the agent will disconnect itself, and the conversation will be unassigned.

Since the agent doesn’t know who to assign the conversation to, you must add a **Conversation Rule** with the **Bolt Agent Handoff Intent** condition. This rule can also be configured to perform other actions besides assigning the conversation to an individual or team. Read on to learn more.

---

# Conversation Rules + Bolt Agent Handoff Intent Condition

Once the agent initiates a handoff, you can trigger specific actions for that conversation using a custom [Conversation Rule](https://help.element451.com/en/articles/1930478-conversation-rules) with the Bolt Agent Handoff Intent condition. These rules are evaluated at the time of handoff when the agent disconnects from the conversation.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481746475/72691c41a021df897a16c8473186/Convo%2BRules%2BEval%2BProcess.png?expires=1784333700&signature=c18490c1e6df50761c1ad312f6bc737163307330a18c918834e2dcda66ba1be8&req=dSQvF856m4VYXPMW1HO4zQDO0nR2eutUAmuG12EsUI%2FMfPlxccq%2FxZTuY9Pv%0Av%2F2Bp03OxvM10hmxXuM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481746475/72691c41a021df897a16c8473186/Convo%2BRules%2BEval%2BProcess.png?expires=1784333700&signature=c18490c1e6df50761c1ad312f6bc737163307330a18c918834e2dcda66ba1be8&req=dSQvF856m4VYXPMW1HO4zQDO0nR2eutUAmuG12EsUI%2FMfPlxccq%2FxZTuY9Pv%0Av%2F2Bp03OxvM10hmxXuM%3D%0A)

This feature allows you to tailor the handoff process to different situations. You can configure actions to assign the conversation to an individual or team, add participants, tag, close, reply, run a workflow rule, or a combination of these actions.   
​  
​![](https://downloads.intercomcdn.com/i/o/1060287007/570de7d8d05e73b7f7e889a4/Note-Orng.png?expires=1784430000&signature=7d7c708af2ea4b6cc805ff788ed05b76eae8cc8b03dc156ce6f420d5589cf04b&req=dSAhFst2moFfXvMW3Hu4gUPYOGJYs97T%2BPq335IbmYqgxdROyBQJisX%2Fhg3p%0AZw%3D%3D%0A) If there is no “assignment” action within the rule, the conversation will remain unassigned. This is the same outcome if no rule is matched to a conversation. No further action will be taken; the conversation will be unassigned.

## Handoff Intent Types

* **Specific Intent**: Use this type to fine-tune the actions **based on the conversation’s intent**. For example, you can set specific intents like “financial aid,” “financial assistance,” and “FAFSA” to ensure the conversation is assigned to the financial aid team. You can create multiple rules with specific intents. Enter short, clear keywords separated by commas; exact matches aren’t required.

  + ![](https://downloads.intercomcdn.com/i/o/1060276628/9c6b83d05d6b8aecb9b5a2d0/Important+-+Orng.png?expires=1784430000&signature=9f3030ec15f6d2c4b57aea8baa3bc4db259a862b54beb42dc26a7c556af971b4&req=dSAhFst5m4ddUfMW3Hu4gXe92f1ur2MfvukYyfB9ttkf6fn9hB0eh2fyB4iN%0Akg%3D%3D%0A) If you have multiple rules, they are evaluated in **bulk** (unlike other conversation rules that are evaluated in order). **BoltAI will determine which rule the conversation best matches based on the Intent and any other conditions**. Since only one rule will apply to a conversation, if you want multi-actions to occur, such as assigning the conversation to a specific individual/team AND sending an automatic reply, you should add both actions to the same rule as the assignment action.

* **All**: Use this type to **apply the same actions to all handoff conversations**, regardless of intent. For instance, if you have a reception desk or a student worker handling inbound conversations, you can use this type to assign all conversations to a specific internal user.

  + ![](https://downloads.intercomcdn.com/i/o/1060276628/9c6b83d05d6b8aecb9b5a2d0/Important+-+Orng.png?expires=1784430000&signature=9f3030ec15f6d2c4b57aea8baa3bc4db259a862b54beb42dc26a7c556af971b4&req=dSAhFst5m4ddUfMW3Hu4gXe92f1ur2MfvukYyfB9ttkf6fn9hB0eh2fyB4iN%0Akg%3D%3D%0A) Only **one** conversation rule should use the All Intent type.

---

# How to Configure Agent Handoff

## Step 1: Create a Conversation Rule

1. Navigate to **Engagement > Conversations > Settings > General**.
2. Under Automation Settings, click **Add Rule**.
3. Rename the Rule: Replace "Untitled Rule" at the top with a name for your rule.
4. Configure **Settings**:

   * **Enabled**: Toggle this on now or later to activate your rule.
   * **Description**: Provide a description for internal purposes.
5. Configure **Conditions**:

   * Click **+ Add Condition** and select **Bolt Agent** **Intent**. The Bolt Agent Handoff Intent side sheet will open.

     + **Intent Type**: Choose between Specific Intent or All, as explained in the previous section above.
     + **Handoff** **Intent**: If you selected Specific Intent, enter the keywords separated by commas, as explained in the previous section above.
     + Click **Save** to return to the side sheet.
6. Configure **Actions**:

   * Click **+ Add Action** and select the desired action. Depending on the chosen action, define additional details (e.g., if you selected the Assignment action, specify the individual or team for the assignment).
   * Add additional actions if needed.
7. Click **Save** in the top right-hand corner of the side sheet.
8. **Activate the Rule**: Ensure the rule is enabled in the settings section to make it active.

## Step 2: Enable Team Member Handoff Skill

Skills are configured for each agent. Therefore, you need to edit the agent to enable the handoff skill.

1. Navigate to **Engagement** > **Bolt Agent.**
2. In the **Agents** section, locate the agent you wish to enable the skill for.
3. Click the **three vertical dots** ![](https://downloads.intercomcdn.com/i/o/1065902804/5578171f2643346025bfdad3/More+Icon2.png?expires=1784430000&signature=b601f1adcff116fb64315af0a53f44768691368b76c7509da0dcdfa09d62f3af&req=dSAhE8B%2Bn4lfXfMW3Hu4ga5M9tHtAAC4tAKnmRLK8eyfeKu0KQiTASxFJbBK%0AoA%3D%3D%0A) icon at the end of the row.
4. Click **Edit**.
5. Where it says **Select Bolt Agent Skills**, click the **Team** **Member** **Handoff** chip. It will turn blue when it's enabled.

Learn more about adding and editing Bolt Agents in [this article](https://help.element451.com/en/articles/8993375-bolt-agent-settings).

---

# Handoff Rule Example

Let's take what we learned above and apply it to a rule. In this example, we want to ensure that any unresolved agent conversations about financial aid are assigned to the financial aid team, and we only want this to happen Monday-Friday, 8 AM-5 PM.

## Rule Conditions

First, let's examine the rule's conditions. You'll see we added two: **Bolt Agents** **Handoff** **Intent** and **Date** **Condition**. This is because we want two criteria items checked before executing the actions: we want to make sure the conversation is financial aid-related and that it's during regular office hours. When multiple conditions exist, the conversation must meet **all** of the conditions.  
​

[![](https://downloads.intercomcdn.com/i/o/1061214157/b101820081f1ac41ea155f9d/Screenshot+2024-05-24+at+11_21_47%E2%80%AFAM.png?expires=1784333700&signature=7360db411c78de49ead29b2aa26cb5b6a0c4cec79b5d31b65755a056d76fce82&req=dSAhF8t%2FmYBaXvMW1HO4zU5Pih38HWbZrCzIz1oneyZoWL8VWKSzbZ8eg5mq%0AZAu%2FLXWtli43px0j99I%3D%0A)](https://downloads.intercomcdn.com/i/o/1061214157/b101820081f1ac41ea155f9d/Screenshot+2024-05-24+at+11_21_47%E2%80%AFAM.png?expires=1784333700&signature=7360db411c78de49ead29b2aa26cb5b6a0c4cec79b5d31b65755a056d76fce82&req=dSAhF8t%2FmYBaXvMW1HO4zU5Pih38HWbZrCzIz1oneyZoWL8VWKSzbZ8eg5mq%0AZAu%2FLXWtli43px0j99I%3D%0A)

## Condition 1: Bolt Agent Handoff Intent

We selected the **Specific** **Intent** type to ensure actions are applied only to conversations about financial aid. We used the keywords “financial aid,” “financial assistance,” and “FAFSA,” separated by commas. Remember, these keywords don’t need an exact match, but keeping them short and specific helps the system accurately identify the conversation's intent.  
​

[![](https://downloads.intercomcdn.com/i/o/1061151879/f77a6625d264087494263e83/Screenshot+2024-05-24+at+11_25_26%E2%80%AFAM.png?expires=1784333700&signature=49f20fa205ee111d040b97ce00c2b08eedb405ec7f59f608719125feb6ec22f9&req=dSAhF8h7nIlYUPMW1HO4zbiStxtrB7Z%2F%2F2at%2FNflcg8ghyp9eoJ0cIdurQBr%0AWM0Se4fCKM%2Ft5tvua3U%3D%0A)](https://downloads.intercomcdn.com/i/o/1061151879/f77a6625d264087494263e83/Screenshot+2024-05-24+at+11_25_26%E2%80%AFAM.png?expires=1784333700&signature=49f20fa205ee111d040b97ce00c2b08eedb405ec7f59f608719125feb6ec22f9&req=dSAhF8h7nIlYUPMW1HO4zbiStxtrB7Z%2F%2F2at%2FNflcg8ghyp9eoJ0cIdurQBr%0AWM0Se4fCKM%2Ft5tvua3U%3D%0A)

## Condition 2: Date Condition

Next, we added a second condition—a date condition—and configured it to M-F 8 AM—5 PM. This ensures that the handoff only happens during regular business hours.

[![](https://downloads.intercomcdn.com/i/o/1061160157/51b9acd8b6b279bd8e74da0f/Screenshot+2024-05-24+at+11_25_36%E2%80%AFAM.png?expires=1784333700&signature=7297f0dd5519dad666f125c24294a4d604981c0757138f2067778289a64eb25a&req=dSAhF8h4nYBaXvMW1HO4za%2FQmKkZTbNEVkypQ1CakSrQXDElLrJ%2BFrgGaa6T%0AZPXUfKdrmQit%2B8o47n8%3D%0A)](https://downloads.intercomcdn.com/i/o/1061160157/51b9acd8b6b279bd8e74da0f/Screenshot+2024-05-24+at+11_25_36%E2%80%AFAM.png?expires=1784333700&signature=7297f0dd5519dad666f125c24294a4d604981c0757138f2067778289a64eb25a&req=dSAhF8h4nYBaXvMW1HO4za%2FQmKkZTbNEVkypQ1CakSrQXDElLrJ%2BFrgGaa6T%0AZPXUfKdrmQit%2B8o47n8%3D%0A)

## Rule Actions

Next, let’s look at the actions for this rule. We added two: **Assignment** and **Reply**. We chose these actions because we want conversations that meet the conditions above to be assigned to the financial aid team and to send an automatic reply informing the student that help is on the way.

## Action 1: Assignment

[![](https://downloads.intercomcdn.com/i/o/1061230332/3d18e5958ee5b33b58e9e331/Screenshot+2024-05-24+at+12_40_52%E2%80%AFPM.png?expires=1784333700&signature=18ecef34468f5cb7a229474c347592dbcaf424b0cbde7c6011bb0bf0a89e08c5&req=dSAhF8t9nYJcW%2FMW1HO4zQeqTDi0cCGCqv%2FVH6JzsEwPIcC2W73xtA%2FBhBoi%0AuF2DLfbi5XTV0lnvmeg%3D%0A)](https://downloads.intercomcdn.com/i/o/1061230332/3d18e5958ee5b33b58e9e331/Screenshot+2024-05-24+at+12_40_52%E2%80%AFPM.png?expires=1784333700&signature=18ecef34468f5cb7a229474c347592dbcaf424b0cbde7c6011bb0bf0a89e08c5&req=dSAhF8t9nYJcW%2FMW1HO4zQeqTDi0cCGCqv%2FVH6JzsEwPIcC2W73xtA%2FBhBoi%0AuF2DLfbi5XTV0lnvmeg%3D%0A)

## Action 2: Reply

[![](https://downloads.intercomcdn.com/i/o/1061230602/4e6dfceaf46c9e74bb537ad1/Screenshot+2024-05-24+at+12_41_04%E2%80%AFPM.png?expires=1784333700&signature=ab5122b70ec0eed7a87a9f814c2d9d55522864f249cd3c0761ee6975553e8ceb&req=dSAhF8t9nYdfW%2FMW1HO4zR1FNYCsTLWf%2F1DplDxXuu%2BpXC0YYHoZ0%2Bicx2u1%0AeG1uFE3jRI2rxJ%2BxMyQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1061230602/4e6dfceaf46c9e74bb537ad1/Screenshot+2024-05-24+at+12_41_04%E2%80%AFPM.png?expires=1784333700&signature=ab5122b70ec0eed7a87a9f814c2d9d55522864f249cd3c0761ee6975553e8ceb&req=dSAhF8t9nYdfW%2FMW1HO4zR1FNYCsTLWf%2F1DplDxXuu%2BpXC0YYHoZ0%2Bicx2u1%0AeG1uFE3jRI2rxJ%2BxMyQ%3D%0A)

## Student POV

Now that our rule with our conditions and actions has been configured and enabled, let's examine it from the student's point of view. For this example, we use the Live Chat feature on an Element451 landing page.  
​

```
Student: Hello. Can I speak with a financial aid representative about the status of my award?  
  
Agent: I can help you with general financial aid questions, but for specific details about your award status, it's best to speak directly with a financial aid representative. Would you like me to connect you with a human team member for this?  
  
Student: Yes, please.  
  
Agent: Great, a financial aid representative will reach out to you soon to discuss the status of your award. If you need anything else in the meantime, feel free to ask!
```

​

[![](https://downloads.intercomcdn.com/i/o/1061255611/c142a997f565e593f12a8090/Screenshot+2024-05-24+at+1_06_46%E2%80%AFPM.png?expires=1784333700&signature=e0a7bf2cbfe98ab70b7e1c9cbe077de9b83eeaf20b16d32543df4e4e71cadacd&req=dSAhF8t7mIdeWPMW1HO4zXTrVODKU1W59ceamVIbR9DRLfplwy5mJhBwjaIU%0AoFK%2FNNiEp5jAatKUu0s%3D%0A)](https://downloads.intercomcdn.com/i/o/1061255611/c142a997f565e593f12a8090/Screenshot+2024-05-24+at+1_06_46%E2%80%AFPM.png?expires=1784333700&signature=e0a7bf2cbfe98ab70b7e1c9cbe077de9b83eeaf20b16d32543df4e4e71cadacd&req=dSAhF8t7mIdeWPMW1HO4zXTrVODKU1W59ceamVIbR9DRLfplwy5mJhBwjaIU%0AoFK%2FNNiEp5jAatKUu0s%3D%0A)

* In the example conversation, the student indicated they needed assistance with their financial aid award. Because the agent does not have access to specific financial aid award details, it offered a handoff.
* You'll notice that we prompted the student to enter their email address. This is because the student was unknown. Had we known who they were, we would not have asked that.
* Finally, you can see that our rule was successfully executed because the last message received, "Hello! Someone from our financial aid team will be with you shortly. ⌛️" was the result of our rule's second action.

​

## Internal POV

Now, let's look at how the conversation appears in your Element451 inbox.

[![](https://downloads.intercomcdn.com/i/o/1061274025/305b5fa97d7b1654f0b771f1/Screenshot+2024-05-24+at+1_22_45%E2%80%AFPM.png?expires=1784333700&signature=303c3a6bec7da7d944cdf385f0d662e65012292feb8b81c728f7b3e787d2a3cb&req=dSAhF8t5mYFdXPMW1HO4zWeyjNKOrPk9Br7Xo4mbwlBvdcGm9Dsrc4gjhV8r%0A5XZf8ruMSYoHs3GxsDw%3D%0A)](https://downloads.intercomcdn.com/i/o/1061274025/305b5fa97d7b1654f0b771f1/Screenshot+2024-05-24+at+1_22_45%E2%80%AFPM.png?expires=1784333700&signature=303c3a6bec7da7d944cdf385f0d662e65012292feb8b81c728f7b3e787d2a3cb&req=dSAhF8t5mYFdXPMW1HO4zWeyjNKOrPk9Br7Xo4mbwlBvdcGm9Dsrc4gjhV8r%0A5XZf8ruMSYoHs3GxsDw%3D%0A)

* Throughout the conversation, we display the activity in a small gray font under the timestamp so you can observe what’s happening.
* Once the student agrees to connect with a team member, the agent is disabled. At this point, the system checks for rules with the handoff intent.
* The system message, “Fire University assigned this conversation to Financial Aid Team,” and the reply, “Hello! Someone from our financial aid team will be with you shortly. ⌛️” indicates that the Financial Aid Handoff Rule ran successfully. These are denoted with the rule name by the system.

## Rule Processing

Notice that we have two active conversation rules in our list. Both have a handoff intent condition, but only the first rule ran. This is because rules are processed in the bulk, and only the first matching rule is applied to the conversation. Since this example conversation met the conditions of the “Financial Aid Handoffs” rule, the second rule, “All Handoffs - Test,” was ignored. Had this conversation happened on a Saturday, it would have failed the date condition of the first rule, and the system would have selected the second rule to evaluate if the message met its conditions.

Another important thing to keep in mind is if you have other conversation rules to manage other types of conversations that don’t involve agents, those don’t matter during this evaluation process. Only rules with handoff intent conditions are evaluated at handoff.

[![](https://downloads.intercomcdn.com/i/o/1061286897/925a6ba73fdd0291e1da0785/Screenshot+2024-05-24+at+1_39_27%E2%80%AFPM.png?expires=1784333700&signature=f4c7f5e4e1b76b6adfdc5e257cd2f50a53b5946cfac2dbd3a4e0ebc29af6532c&req=dSAhF8t2m4lWXvMW1HO4zWSiqEwUF76WubPTA668V5MlQC0Fthbc6xt9UmsK%0ATSsFzaqlLZpV7wqCwL8%3D%0A)](https://downloads.intercomcdn.com/i/o/1061286897/925a6ba73fdd0291e1da0785/Screenshot+2024-05-24+at+1_39_27%E2%80%AFPM.png?expires=1784333700&signature=f4c7f5e4e1b76b6adfdc5e257cd2f50a53b5946cfac2dbd3a4e0ebc29af6532c&req=dSAhF8t2m4lWXvMW1HO4zWSiqEwUF76WubPTA668V5MlQC0Fthbc6xt9UmsK%0ATSsFzaqlLZpV7wqCwL8%3D%0A)

---

# Managing Handoffs When Campus is Closed

Even when your institution is closed, your students can still receive around-the-clock assistance thanks to the power of Bolt Agents. However, there will be times after hours or during closures when the agent can’t answer a question or the student asks to speak with a human. Here is how we recommend handling handoffs when you’re not able to monitor and reply to them:

## Long-Term Closures (Holidays + Breaks)

As mentioned earlier, you can prevent the agent from handing off conversations by disabling the Team Member Handoff Skill. When disabled, instead of offering to connect the student to a team member, the agent will search your Knowledge Hub for contact information to share with the student. Alternatively, if you have the Schedule Appointments skill enabled, the agent will attempt to help the student book an appointment with someone from your team.

Since turning the agent's skills on and off is a manual process and you likely want to avoid managing that daily, we recommend using this approach only for cases where you have no live support agents available to handle handoffs or during longer campus closures, like holiday breaks.

## After Hours + Weekends

For short-term closures like weekends and after hours, we recommend leaving handoffs enabled and creating a rule to send a **reply** to conversations that get handed off, letting students know your office is closed. This creates an automated process with minimal manual work. Once your team returns to the office, you can review and resolve the handed-off conversations.

To set up this rule, use two conditions: **Bolt Agent** **Handoff** **Intent** and **Date** **Condition**, and one action: **Reply**.

* **Bolt Agent Handoff Intent:** Use the ALL intent type to apply the action to all handoff messages.
* **Date Condition:** Define the dates and times when you want to send the automatic reply.
* **Reply Action:** Create a message like, “Hey there 👋! We apologize, but our offices are closed. Our business hours are M-F from 8 am-5 pm. We’ll reply as soon as we can. Go Embers! 🔥”

---