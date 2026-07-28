---
title: 📌 Bolt AI: Frequently Asked Questions
url: https://help.element451.com/en/articles/10540370-bolt-ai-frequently-asked-questions
collection: Bolt AI
---

Commonly asked questions about Bolt AI (Agents, Discovery, and Knowledge Hub), providing quick solutions and key insights.

# General

**My university doesn’t allow us to use ChatGPT or other AI tools due to data security concerns. How is Element451 different?**

Element451’s AI tools use enterprise-grade APIs from contracted LLM providers. Customer data is not used to train public models or for providers’ independent purposes. When an AI feature needs context to complete a request, only the relevant data is securely processed by those providers under contractual data-use and retention controls. Element451 does not store chat data outside the platform.

---

# Bolt Agents

**How do I create and manage Bolt Agents?**

Navigate to Engagement > Bolt Agents to manage your student-facing agents. From here, you can add new agents, edit existing ones, preview their interactions, and customize their settings, including their name, type, skills, avatar, greeting, voice, and descriptions. **Agents must be assigned to a team to be active**.

[Explore more here →  
​](https://help.element451.com/en/articles/7173429-getting-started-with-bolt-agents-for-students)

**What are Teams, and what is their purpose?**

Teams are groups of agents that determine where and when the agent is active. By applying condition filters like Page URL, Path URL, UTM Parameters, and Conversation Channel, you can specify the pages where a team of agents should appear. The system evaluates teams sequentially, activating the first team whose conditions are met.

[Explore more here →  
​](https://help.element451.com/en/articles/12068259-bolt-agent-teams)​

**What skills can be assigned to Bolt Agents?**

### Built-in Skills give Bolt Agents packaged capabilities such as Human Team Member Handoff, Start an Application, Get Application Status, Register for Event, Schedule Appointments, Common App Knowledge, Financial Aid Knowledge, and Inquiry Flow. Availability depends on your Element451 package and agent type. Custom Skills are institution-authored instructions and configured actions that administrators create at the instance level, then enable and prioritize for individual agents.

[Explore more here →  
​](https://help.element451.com/en/articles/8993380-bolt-agent-skills)

**How does Content Moderation work for Bolt Agents?**

Content Moderation automatically flags conversations containing inappropriate, harmful, or manipulative content based on predefined categories like hate speech, harassment, self-harm, and sexual content, using OpenAI's API. Customizable actions and flags allow efficient management of flagged content. Each flag can be configured with a custom message, priority, and actions (disable agent, block conversation).

[Explore more here →  
​](https://help.element451.com/en/articles/9859790-bolt-agent-content-moderation)

**How should I test my agents before making them live?**

Start in Test Agent to safely test Messenger, SMS, Email, and Voice behavior, review Response Details, and simulate configured actions without creating real side effects. Then run a controlled live end-to-end test: use an isolated page and Team for Messenger, test-only contacts for Email and SMS, and one live inbound call per Voice transfer destination.

[Explore more here →  
​](https://help.element451.com/en/articles/8993362-testing-bolt-agents)

**What are Handoffs, and how do I configure them?**

Bolt supports several handoff paths. Choose the setup that matches where the conversation should go:

1. For native staff takeover in digital conversations, enable Human Team Member Handoff and use a Conversation Rule to route the conversation to the appropriate team or user.
2. For explicit Custom Skill routing, use @Transfer Call for a phone transfer or @Hand Off to Agent for another Bolt Agent. These actions do not require Human Team Member Handoff or a Conversation Rule solely for the configured transfer.

Before creating a handoff rule, we strongly advise you to review [our documentation](https://help.element451.com/en/articles/8993398-bolt-agent-handoffs) for a complete understanding of the behavior.

[Explore more here →](https://help.element451.com/en/articles/8993398-bolt-agent-handoffs)

**How should I structure Bolt Agents?**

Balance specialized and generalist agents. Generalist agents should handle broad inquiries on general website areas, while specialized agents should focus on specific topics like academic programs or financial aid. Limit overlap in general contexts to avoid confusing responses and use internal descriptions to facilitate handoffs between agents. Always test your agents.

[Explore more here →  
​](https://help.element451.com/en/articles/9876034-best-practices-for-creating-bolt-agents-teams)

**What is the difference between Bolt Agents and Bolt Discovery?**

Bolt Discovery is a generative search tool that provides quick, accurate information from your Knowledge Hub, acting as an alternative to traditional website search.

On the other hand, Bolt Agents are personalized digital team members designed to have 1:1 conversations with students, providing tailored support and guidance using the same Knowledge Hub.

Bolt Discovery is ideal for instant information retrieval, while Bolt Agents are better suited for complex, nuanced interactions requiring personalized advice. However, because of their integration with one another through messenger handoffs, they can be extremely powerful when used together.  
​  
​[Explore more here →](https://help.element451.com/en/articles/9764775-bolt-discovery-vs-bolt-agents-understanding-the-difference)

**What's the difference between the various messenger conditions settings?**

* Conversations > Messenger > Conditions: Controls where the Messenger widget appears on your external website.
* Engagement > Bolt Agents > Teams: Controls which Team is active using conditions such as Page URL, Path URL, UTM parameters, and conversation channel.
* Engagement > Bolt Agents > Settings > Messenger Conditions: A Messenger-only alternative intended primarily for deployments that use only the default Agent; Teams provide more control.

## Detailed Explanation

* Conversations > Messenger > Conditions

  + These conditions control the visibility of the *Messenger widget* on your *external* website pages. These settings determine where the Messenger chat bubble appears (and thus where a user could *potentially* interact with your agents *if* it's configured for Messenger).

* Engagement > Bolt Agents > Settings > Messenger Conditions

  + This section is primarily intended for schools that *exclusively* use the default agent in Messenger and *don't* utilize Teams. It's a direct way to specify that your agent should be active in the Messenger channel. However, even in this case, we strongly recommend using Teams instead, as it offers greater flexibility and control. This setting is essentially a shortcut for setting a Team condition of "Channel = Messenger."

* Engagement > Bolt Agents > Teams

  + Teams are the central hub for managing agent deployment. You create a Team, add your agent(s) to it, and then set conditions *on the Team* to control *when* and *where* the agents appear. Teams allow you to group agents and apply conditions based on various criteria like Page URL, Path URL, UTM parameters, and *Conversation Channel*.

**Is it possible to use the direct chat link as a "normal" messenger without any agents responding?**

Yes. To do this, set up a new agent team specifically for the direct chat page.

1. Enable that team for **Messenger**.
2. Move the team to the **top of the team list** so its conditions are evaluated first.
3. Add a condition so the team is only used on the **direct page URL**.
4. Do **not** assign any agents to the team.

This allows the Messenger to appear on that page, but because the matched team has no agents in it, no Bolt Agents from that team will respond.

**An agent returned an answer that didn't match my Knowledge Hub.**

If you’ve checked your Knowledge Hub and confirmed that the content is accurate, here are some key things to consider:

1. **Understanding Semantic Search Across All Sources**

   * Agents use **semantic search** to retrieve the most relevant chunks of information from your Knowledge Hub, not the entire source. For example, if a student asks, “How many graduate programs do you offer?” the agent will extract snippets of text that best match the query, regardless of whether they’re from a URL, Text Source, or Custom Answer.

   * This means the agent's response may only reflect the retrieved chunks, which could lead to incomplete or misinterpreted answers if the content isn’t clear, concise, or well-structured.  
     ​
2. **Prioritization of Custom Answers**

   * Custom Answers are prioritized in agent replies because they are designed to provide direct, predefined responses to frequently asked questions. For example:

     + Anticipated Question: *“How many graduate programs do you offer?”*
     + Custom Answer: *“We offer 10 graduate programs, including programs in Business, Education, and Healthcare.”*

   By using Custom Answers for specific, high-priority questions, you can ensure that the agent provides accurate and comprehensive responses tailored to common inquiries.  
   ​
3. **Avoiding Duplicate or Conflicting Information**

   * Duplicate or conflicting content in your Knowledge Hub can lead to inconsistent answers. For example, if one source states, “We have 10 graduate programs,” and another incorrectly mentions “8 graduate programs,” the agent may retrieve conflicting chunks of information, causing confusion.

**What to do:**

* Regularly audit your Knowledge Hub for duplicate or outdated content.
* Use clear, specific language in your sources to avoid ambiguity.
* If there is critical information students often ask about, like program counts or deadlines, include it as a Custom Answer to ensure consistency.

**What should I name my agent?**

When naming your agent, choose something natural and engaging rather than a functional title like “Financial Aid” or “Admissions.” The agent's **title** (displayed next to its name) can provide added context, and the **description** can further explain its expertise.

Since the agent may reference its name in greetings, a more natural, human-like name will create a better experience. For example, instead of “Financial Aid,” consider a name like “Finley” with the title **Financial Aid Agent** to maintain clarity while keeping interactions more natural.

**Our Bolt Agent has given incorrect links to find more information for some questions. How do I prevent this from happening?**

Since Bolt Agents are grounded in your Knowledge Hub, the link likely came from one of your sources. Check your source list for the URL and review your Knowledge Hub for discrepancies or duplicate answers. Keep the most accurate, preferred information consistent and clear across sources.  
​

#### Will Agents understand what a student is replying to if they respond to an SMS or email campaign?

Yes. When a student replies to a campaign, Bolt includes the originating campaign message in its context, allowing it to correctly interpret short replies like "yes" or "I'm interested" without asking the student to clarify.

#### Why does it appear Agents sometimes respond accurately to a one-word reply like "yes" or "no"?

Bolt uses the available conversation context. When a student replies directly to a campaign, the originating campaign message is included, allowing Bolt to interpret short replies such as "yes" or "no."

---

# Bolt Agent Jobs

**What is a Bolt Agent Job?**

A Bolt Agent Job is a structured assignment that allows a Bolt Agent to proactively work toward a specific goal**, like getting students to submit an application or register for an event,** using a set of approved actions and instructions. Bolt Agent Jobs represent an evolution from reactive to proactive agents, enabling them to autonomously perform specific tasks aimed at achieving institutional objectives, such as calling or emailing students about application steps, taking proactive measures to increase application completions, or boosting attendance for recruitment events.

**How is a Job different from a Workflow or Rule?**

A Bolt Agent Job is an AI assignment designed to proactively drive enrollment outcomes (like application submissions or event sign-ups) autonomously. Unlike traditional Workflows, which follow a rigid, predefined series of steps, Agent Jobs allow AI agents to "think," adapt to student context, and make decisions to achieve complex goals dynamically. Workflows are linear, while Agent Jobs are goal-oriented and can intelligently adjust their approach.

**Can I use both a segment and a trigger in a job?**

Yes. You can enroll people using a segment and also set up a trigger (e.g., form submission) to automatically add additional contacts as they take action.

**Can a Bolt Agent be assigned to more than one job at a time?**

Yes. A Bolt Agent can run multiple jobs simultaneously. Each job operates independently with its own goal, audience, and action settings.

**What happens when a contact completes the goal?**

Once a contact meets the job’s goal (e.g., submits a form or registers for an event), they are marked as “Goal Completed” and the agent will stop taking actions for them within that job.

**What does “Thinking” mean in the contact status?**

“Thinking” means the agent is actively determining what action to take next for that contact. It may be evaluating approval rules, past actions, or context before proceeding.

**What does the “Urgent” toggle do?**

Urgent Mode reduces scheduling and monitoring delays so the Agent acts as soon as eligible. It does not bypass permitted local-time windows for SMS or Phone, consent requirements, or other safety and compliance safeguards.

**What does enabling “Past Activities” do?**

When Consider Past Activity is enabled, the Agent checks whether a contact met the Job goal before enrollment. If so, the enrollment is marked No Action Needed and no outreach begins. Goal Completed is reserved for goals achieved after enrollment while the Job is active.

**What is self-approval, and when should I use it?**

Self-approval allows the agent to take certain actions without human review. Only enable this for low-risk actions where you’ve provided clear guidelines. Use with caution.

**How do approval guidelines work?**

Approval guidelines are free-text instructions that help the agent decide whether to proceed with an action or request human approval. You can add multiple guidelines and reorder them.

**Can I edit a job after it’s been activated?**

Yes. You can edit job settings, actions, approvers, segments, and more at any time—even while the job is running.

**Can I cancel a job for a single contact?**

Yes. From the People tab in the job view, click the vertical ellipsis next to a contact and select “Cancel Job” to stop actions for that individual.

**Who gets notified when an action needs approval?**

Any user assigned as an Approver for the job will receive a notification in the “My Approvals” section when the agent requests review.

**Can I monitor how the job is performing?**

Yes. The All Jobs page provides summary metrics, and each individual job shows real-time progress, contact statuses, and actions taken.

**Can I control the communication channels the agent uses?**

Choose the allowed channels in the Job's Channels setting: Email, SMS, and/or Phone. Use General Instructions to guide the preferred order, cadence, and behavior within those enabled channels.

**Can I make changes to an active job?**

Yes. You can edit most job settings while it’s running, such as instructions, actions, and deadlines. However, you cannot change a job’s goal once it has been created.

**Is there a limit to the number of contacts a job can include?**

Each Job can have its own enrollment limit, up to the instance-level Jobs Enrollment Limit shown in Engagement > Bolt Agents > Settings. Contacts beyond a Job’s active limit remain Pending until space becomes available.

**What are job instructions for?**

Instructions guide the Agent’s strategy, including cadence, content focus, tone, and the preferred use or sequence of channels already enabled in the Channels setting. Instructions do not enable a channel.

**What is an example of an approval guideline?**

“If we’ve never contacted this student before, a human must approve the first action. If we’ve already contacted them three times, get approval before a fourth outreach.”

Approval guidelines are flexible and written in plain language to guide the agent’s decision-making.

**In Jobs, what’s the difference between a segment and a trigger?**

A segment is a static group of people you load into a job at setup. A trigger automatically adds new people to the job when they meet a condition, such as submitting a form. You can use both together. More trigger types are coming soon.

**Can I add people/contacts after I created my job?**

Yes, use the "Add People" button in the job header. You have the option to select contacts individually or load a segment manually.

**Why are people missing from the preview when I add a segment to an existing Job?**

When you add a segment to an existing Job using the Add People sheet, the preview list might look incomplete. Here are some reasons why that may happen:

* If some contacts in the segment are hidden from you due to **visibility group** settings, they won’t show in the preview. However, they’ll still be added to the Job.
* If a contact is already enrolled in the Job, they’re excluded from the preview to prevent duplication, but they’re still counted in the total.

This behavior is unique to the Add People sheet. To confirm who was added, check the People tab after saving.

**Can I configure a Bolt Agent’s “sleep” or "monitoring" period?**

No need—Bolt Agents are AI-powered and context-aware, so they intelligently determine when to pause and when to re-engage based on the situation. They automatically assess the right timing for their next action without requiring manual sleep settings.

**What is the enrollment limit for a Bolt Agent Job?**

The instance-level Jobs Enrollment Limit is shown in Engagement > Bolt Agents > Settings. Each Job can set a lower active-enrollment limit. Additional contacts remain Pending until capacity opens.

**Can a Bolt Agent Job run alongside my existing marketing campaigns and workflows?**

Yes. Jobs can run alongside campaigns and workflows. Agents can use supported context, including conversation summaries and campaign activity such as channel, engagement events, campaign title, Email subject line, and SMS or Push message content. Agents do not receive every message body, so review overlapping outreach and instructions to avoid redundancy.

**What campaign context does a Bolt Agent have access to?**

Bolt Agents can view supported campaign activity for Email, SMS, and Push notifications:

* **Email campaigns**: clicks, deliveries, opens, subject lines, and campaign title
* **SMS campaigns**: clicks, deliveries, message content, and campaign title
* **Push notification campaigns**: clicks, reads, sends, message content, and campaign title

Each activity record also includes the communication channel, user action taken, and a timestamp with relative time (e.g., “2 hours ago”). This allows agents to reference specific user interactions and tailor their outreach based on actual engagement patterns.

**How does the agent handle job-related communication timing (e.g., avoiding late-night messages)?**

Element451 has built-in safeguards to prevent agents from sending communications outside of reasonable hours. The agent will consider the student's time zone (based on their address or last-seen IP) or fall back to the institutional time zone. You can also include specific timing instructions in your prompts, such as "Do not send messages between 9 PM and 8 AM local time." The agent will also leverage known student preferences, such as "preferred open time," to schedule communications for optimal engagement.

**Can I control when the agent asks for human approval?**

Yes. For each **action**, you can enable "Self Approval" and set specific guidelines. For example, you can instruct the agent: "If this is the first time we've contacted the student, ask for human approval first. Otherwise, self-approve this action." This allows you to gradually give the agent more autonomy as you build confidence in its performance. Read more about action approvals [here](https://help.element451.com/en/articles/11646573-creating-a-bolt-agent-job#h_b336546463).

**Can agents see conversations their teammates have had with a contact**

Yes, agents can view summaries of other agents' and staff's past interactions with each contact, supporting seamless collaboration and handoffs.

**What does “No Action Needed” mean for enrollment status?**

This status indicates when goals were achieved via past activity, not by an agent, giving you more accurate reporting on agent-driven results.

**Will agents know if a contact recently received a campaign message?**

Yes, agents see recent campaign activity (email, SMS, push notifications) for each contact, helping avoid duplicate outreach and ensuring messages are relevant.

**Can I edit a message the agent proposed (in approvals)?**

Yes, you have two different options to edit the proposed message:

1) **AgentFeedback**: Use the ***ProvideFeedback*** option where you explain what you want changed, and the agent will return to the "thinking" state, rewrite the message, and send it back to you for approval.   
2) **ManualInlineEdits**: In the approval screen, you can edit the text content for SMS and email messages by clicking into the text boxes. You can also highlight text to edit/add formatting.

---

# Bolt Agents for Staff

**What are Staff Agents?**

Staff Agents are AI-powered tools integrated within Element451 that leverage large language models (LLMs) to automate tasks, streamline communication, and provide quick access to information. They help staff members increase efficiency by generating content, answering questions about Element451 features, completing tasks, and summarizing information, all within a conversational interface and specialized modules. By handling routine and repetitive work, Staff Agents free up staff time to focus on higher-priority activities.  
​

​[Explore more here →](https://help.element451.com/en/articles/7173423-getting-started-with-bolt-agents-for-staff)  
​

**Where can I access Staff Agents within Element451?**

Staff Agents are accessible through the Bolt Staff Agent Sidebar, which can be found via the Start Page or top navigation bar. Additionally, Staff Agent-powered tools are integrated throughout various modules within Element451, such as Campaigns, Conversations, and Pages. This pervasive integration ensures AI assistance is readily available wherever staff members are working.

​[Explore more here →](https://help.element451.com/en/articles/7173423-getting-started-with-bolt-agents-for-staff)  
​

**How do the Bolt Writing Tools enhance content creation and editing?**

Bolt Writing Tools, powered by the Copywriter Agent, streamline writing and editing within the Campaigns, Conversations, and Pages modules. These tools can generate custom replies, improve writing quality (e.g., fixing spelling and grammar), adjust tone, shorten or expand text, and translate content. They also offer a summarization feature, which creates shareable notes from conversations. These features save time and ensure content is polished and aligned with institutional brand guidelines.

​​[Explore more here →](https://help.element451.com/en/articles/8380026-bolt-writing-tools)  
​

**What are shortcuts, and how do they expedite common tasks?**

Shortcuts are pre-defined actions that allow users to quickly access information or perform tasks within Element451 without typing out full prompts. They are categorized as General, User, and Contact shortcuts and are accessible via the Shortcuts tab in the Bolt Staff Agent Sidebar. Examples include "Catch Me Up" (provides a summary of recent tasks and conversations), "Summarize Contact" (generates a summary of a student's profile), and "User Tasks" (retrieves tasks assigned to a specific user).

​[​​Explore more here →  
​](https://help.element451.com/en/articles/7173423-getting-started-with-bolt-agents-for-staff#h_95515f1181)

**How are Staff Agents context-aware?**

Staff Agents are designed to be context-aware, meaning they can automatically detect where you are within Element451 and tailor their responses and suggestions accordingly. For example, when viewing a student's record and using a shortcut like "Summarize Contact," the Staff Agent will automatically populate the student's name. This eliminates the need for manual searches and selection, reducing errors and saving time.

​[​​Explore more here →  
​](https://help.element451.com/en/articles/7173423-getting-started-with-bolt-agents-for-staff#h_1646b74156)

**What are the Brand Writing Style settings?**

Element451's Brand Writing Style settings allow you to customize the tone, voice, point of view, writing intent, language complexity, and formatting of content generated by Staff Agents. You can manually adjust these settings or use the "Infer from Example" feature, which analyzes sample text to generate suggested style settings. Regularly updating and refining these settings ensures consistency and alignment with the institution's communication objectives. The Brand Writing Style Settings are accessible via Settings > General > Branding.

​​[Explore more here →](https://help.element451.com/en/articles/9265392-brand-writing-style-settings-for-staff-agents)  
​

**What is the purpose of the Campaigns and Pages Agents?**

The Campaigns Agent helps create comprehensive drip campaigns (creates multiple communications + the workflow that powers them), including generating subject lines, preview text, and email content with tone and grammar checks.

The Pages Agent assists in developing ready-to-publish pages with branded headlines, text, and other components. Both agents use natural language prompts and leverage the Knowledge Hub and Content Tokens to personalize and tailor content.

​​[Explore more here (campaigns agent) →](https://help.element451.com/en/articles/8312170-bolt-campaign-creator-agent)

[Explore more here (pages agent) →](https://help.element451.com/en/articles/8377457-bolt-page-builder-agent)

**Can I ask Staff Agents to help me with Element451 features?**

Staff Agents can provide immediate answers to questions about Element451 features and functionalities. By asking questions in natural language within the Bolt Staff Agent Sidebar, users can receive information sourced directly from Element451 help articles and product documentation. This allows users to quickly learn about features and resolve issues without leaving their current workflow.  
​

​[Explore more here →](https://help.element451.com/en/articles/9926140-using-staff-agents-for-help-with-element451-features)

**Can I export data from the Application Agents (Fraud Detector/Reader)?**

For the Fraud Detection Agent, you can export the fraud category and explanation using the Import + Export module. Simply select those fields when mapping your export. At this time, you cannot export data related to the Application Reader Agent. You can only export the final decision.

**When do the Application Reader and Fraud Detector Agents run on imported applications?**

* **Application Reader**: The Application Reader Agent will read and score an imported application when a decision is created and it reaches the stage(s) at which you have the reader enabled.
* **Application Fraud Detector**: The Application Fraud Detector Agent evaluates an imported application at the time the decision is created.

---

# Bolt Discovery

**What is Bolt Discovery, and how does it differ from traditional search?**

Bolt Discovery is an AI-powered search tool within the Element451 platform that utilizes large language models (LLMs) and natural language processing (NLP) to provide quick, relevant, and human-like responses to user queries. Unlike traditional search, which typically returns a list of links, Bolt Discovery comprehends the intent behind questions, providing direct answers and maintaining a conversational flow with follow-up questions.  
​  
​[Explore more here →](https://help.element451.com/en/articles/9331910-bolt-discovery-overview)  
​

**How can I integrate Bolt Discovery?**

Bolt Discovery can be deployed in three main ways:

* **Element451 Pages:** Add it as a content block, customizing the design and adding thread starters. You can also configure buttons to trigger Bolt Discovery with a pre-defined question.
* **Website Embedding:** Embed a script into your website's header and use commands to trigger Bolt Discovery, or use the Element451 WordPress plugin for easier integration.
* **Shareable URL:** Share the direct Bolt Discovery URL in communications, campaigns, or as a QR code. You can append a pre-configured question to the URL to create personalized experiences.  
  ​  
  ​[Explore more here →](https://help.element451.com/en/articles/9397459-deploying-bolt-discovery)

**What are Thread Starters, and how do I configure them?**

Thread Starters are predefined prompts displayed under the search bar in Bolt Discovery, designed to guide users toward relevant information quickly.

* They are configured in Bolt Discovery Settings by navigating to Engagement > Bolt Discovery > Settings > Starters. You can add a Title (what the student sees) and a Message (the question sent to Bolt Discovery). Optional conditions based on Page URL, Path URL, or UTM Parameters can be added to tailor the starters to specific contexts.
* On Element451 Pages, starters are added and managed directly within the Content Block editor.

[Explore more here →](https://help.element451.com/en/articles/9397400-bolt-discovery-settings#h_fda3d521c0)

**How does the 'Lead Capture Form' work in Bolt Discovery?**

1. Bolt Discovery intelligently detects potential prospects based on their queries.
2. A follow-up question appears alongside search results and other intelligent follow-up questions.

   * The follow-up question button will have a paper/pencil emoji (📝) and typically displays a message like "I'd like to request more information about the `[program name]` and the application process."
3. When a prospect clicks the prompt, either a custom form (selected from existing prospect-type forms) or a default form (asking for First Name, Last Name, and Email Address) appears.
4. Upon submission, the system checks if the user exists in the database; if so, the record is updated, and if not, a new contact record is created. A prospect milestone, including a link to the conversation thread, is then assigned to the contact.

[Explore more here →](https://help.element451.com/en/articles/9331910-bolt-discovery-overview#h_c8bdf09d8c)

**Pro Tips for Accessing Prospects from Bolt Discovery**

* Use advanced filtering on the All Threads (Engagement > Bolt Discovery > All Threads) page to filter threads with submitted forms.
* Create a calculated segment that uses the filter `Milestone Name is BoltDiscovery`.

  + When a form is submitted from Bolt Discovery, a prospect milestone is added. This applies whether you use the default form or a custom one. However, using a custom form, you can also create a segment based on form submissions. Just be aware that if the form is accessible outside of Discovery, then contacts completing it in those locations will also be included in your segment.
  + A significant benefit to using this method is that you can also utilize the segment as a trigger in a workflow. When a contact joins the segment, you can automate processes like assigning a task to an admissions counselor to follow up or sending a campaign to the contact.

**How does Bolt Discovery integrate with Messenger?**

1. Bolt Discovery intelligently detects when the user could benefit from connecting with someone from your team.

   * **This feature is only available whenMessenger is enabled on the same page as Bolt Discovery**.
2. A follow-up question appears alongside search results and other intelligent follow-up questions.

   * The follow-up question button will have a chat bubble emoji (💬) and typically displays a message like "Can you connect me with someone who can provide more details about `[thread topic]`?" or "I have additional questions about `[thread topic]`. Can I speak to a representative?"
3. Clicking the button opens the Messenger widget, closes Bolt Discovery, and sends the original question via Messenger on the user's behalf.
4. If you have Bolt Agents enabled and the conditions are met for their execution, they will assist the student. Otherwise, your human staff can manage the conversation just like any other Messenger conversation.

[Explore more here →](https://help.element451.com/en/articles/9331910-bolt-discovery-overview#h_c8bdf09d8c)

**Where does Bolt Discovery get information, and how do I add to it?**

Bolt Discovery uses public Knowledge Hub sources available to the current context. By default, this is your public Knowledge Hub; configured Spaces can limit the sources used under matching conditions. Add sources under Data + Automations > Knowledge. Element451 also provides universal information from studentaid.gov and commonapp.org.

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)  
​

**What is the difference between Bolt Discovery and Bolt Agents?**

Bolt Discovery is a generative search tool that provides quick, accurate information from your Knowledge Hub, acting as an alternative to traditional website search.

Bolt Agents, on the other hand, are personalized digital team members designed to have 1:1 conversations with students, providing tailored support and guidance using the same Knowledge Hub.

Bolt Discovery is ideal for instant information retrieval, while Bolt Agents are better suited for complex, nuanced interactions requiring personalized advice. However, because of their integration with one another through messenger handoffs, they can be extremely powerful when used together.

[Explore more here →](https://help.element451.com/en/articles/9764775-bolt-discovery-vs-bolt-agents-understanding-the-difference)  
​  
​

---

# Bolt Knowledge Hub

**What is the purpose + importance of my Knowledge Hub?**

* The Knowledge Hub is the foundation for Element451's Bolt features (Bolt Agents, Staff Agents, and Bolt Discovery), providing the information these tools use to answer user queries and create content.
* It powers the semantic understanding behind these tools, enabling them to analyze the meaning behind questions and retrieve relevant knowledge.
* Maintaining a healthy Knowledge Hub ensures Bolt delivers accurate and contextual answers, empowering students, staff, and users while freeing up your team.

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)  
​

**What is the difference between the Public and Private Knowledge Hub?**

* The **Public** repository is used by Bolt Agents (both Student and Staff) and Bolt Discovery. It contains general knowledge accessible to students and staff.
* The **Private** repository is exclusive to Bolt Agents for Staff and is designed for internal institutional knowledge, such as internal policies and procedures. Use the Public repository for information you want both students and staff to access, and use the Private repository for information only internal staff should see. It is recommended to specify that the Staff Agent use information from the internal Knowledge Hub to avoid searching the Element451 help center.

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)

**What are the different types of sources that can be added?**

The Knowledge Hub supports several source types:

* **Text:** For adding knowledge directly as text. Best for simple information but remember that formatting will not be retained.
* **URL:** For linking to a single webpage. Ideal when you want updates to your website to automatically update the Knowledge Hub via daily sync.
* **Website:** For adding information from a collection of webpages via a website's sitemap. Useful for quickly adding content from multiple related pages. A best practice is to limit website knowledge sources to 20-30 pages.
* **File Upload:** For uploading documents. Use for existing documents but be mindful of file size (under 10MB is recommended). Formats supported include .eml, .html, .json, .md, .msg, .rst, .rtf, .txt, .xml, .jpeg, .png, .csv, .doc, .docx, .epub, .odt, .pdf, .ppt, .pptx, .tsv, .xlsx.
* **Custom Answers:** For creating specific question-and-answer pairs. Prioritized by Bolt AI and best for frequently asked questions and crucial information.

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)  
​

**How can I use the Insights Dashboards to improve the performance of Bolt AI?**

The Insights Dashboards provide metrics for understanding how your Knowledge Hub is performing.

* The **Conversations Dashboard** (for Bolt Agents) shows metrics such as the number of times an agent encountered an uncertain response (Knowledge Hub Gap Card and Log) and the most referenced articles.
* The **Bolt Discovery Dashboard** shows gaps in Discovery results, common search terms leading to unanswered queries, and top articles referenced. Use the Query Log to evaluate the accuracy of answers and identify areas for improvement. Identify common trends in the logs and keyword data to prioritize adding detailed content in specific areas.

[Explore more here (conversations dashboard) →](https://intercom.help/element451/en/articles/6909340-conversations-dashboard)

[Explore more here (discovery dashboard) →](https://intercom.help/element451/en/articles/9740909-bolt-discovery-dashboard)  
​

**An answer provided doesn't match the information in my Knowledge Hub**

First, ensure the information in your Knowledge Hub is accurate and clearly states key facts. If you’ve confirmed that the content is accurate, here are some key things to consider:

1. **Understanding Semantic Search Across All Sources**

   * Bolt Agents use **semantic search** to retrieve the most relevant chunks of information from your Knowledge Hub, not the entire source. For example, if a student asks, “How many graduate programs do you offer?” the agent will extract snippets of text that best match the query, regardless of whether they’re from a URL, Text Source, or Custom Answer.

   * This means the agent response may only reflect the retrieved chunks, which could lead to incomplete or misinterpreted answers if the content isn’t clear, concise, or well-structured.
2. **Prioritization of Custom Answers**

   * Custom Answers are prioritized in Bolt Agents because they are designed to provide direct, predefined responses to frequently asked questions. For example:

     + Anticipated Question: *“How many graduate programs do you offer?”*
     + Custom Answer: *“We offer 10 graduate programs, including programs in Business, Education, and Healthcare.”*

   By using Custom Answers for specific, high-priority questions, you can ensure that the agent provides accurate and comprehensive responses tailored to common inquiries.  
   ​
3. **Avoiding Duplicate or Conflicting Information**

   * Duplicate or conflicting content in your Knowledge Hub can lead to inconsistent answers. For example, if one source states, “We have 10 graduate programs,” and another incorrectly mentions “8 graduate programs,” the agent may retrieve conflicting chunks of information, causing confusion.

**What to do:**

* Regularly audit your Knowledge Hub for duplicate or outdated content.
* Use clear, specific language in your sources to avoid ambiguity.
* If there is critical information students often ask about, like program counts or deadlines, include it as a Custom Answer to ensure consistency.

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)

**Can I add my social media URLs (like Facebook and Instagram) as sources?**

The Knowledge Hub cannot ingest or retrieve content from your social media accounts, such as posts, comments, or updates. However, you can add your social media handles or URLs as a **Text Source** or **Custom Answer** to make them accessible for sharing with students.

* For example: *“You can check out Element University on Facebook at [www.facebook.com/ElementUniversity](http://www.facebook.com/ElementUniversity)!”*

This allows your Bolt Agents or Bolt Discovery to provide links to your social media pages when students ask how to find you online. Keep in mind that this is for sharing access to your pages—not the content within them.

**We've updated a page on our website, but Bolt returns outdated information.**

* Ensure you have daily sync enabled on the page in question. This will ensure that Bolt AI checks for updates on that page each day. Alternatively, you can use the "relearn" feature on a source to capture the most recent information.
* To ensure we only reindex pages with updated information, **Daily Sync** will reindex a webpage **onlywhenBolt AIdetectsthata change has been made**. Bolt AI verifies this by checking the following:

  + The **last-modified** header
  + The **etag** header
  + The **meta tag** in the HTML with name="date"
  + The **sitemap lastmod** date

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)

**Can I index my entire .edu site using a single website knowledge source?**

While it is technically possible to index entire websites (although larger sites may exceed our rate limit), there are downsides to this approach. One is that many college and university websites have outdated or contradictory information listed on different pages. By adding an entire site, we may inadvertently include information that could confuse Bolt Agents.

Using the Website loader, you can start at a path you are most confident in. For example, if you work in admissions like elementuniversity.edu/admissions. You can also select/deselect one or more pages/paths to include/exclude from your website knowledge source.  
​  
We recommend keeping individual website knowledge sources to, at most, 20-30 web pages.

[Explore more here →](https://help.element451.com/en/articles/10302715-getting-started-with-knowledge-hub)

**Why isn’t my website content being ingested as expected?**

Some websites use firewalls or security services (e.g., Cloudflare) that block automated crawlers from accessing their pages. If your website source isn’t pulling in content as expected, your web team may need to whitelist Element451’s crawler IP address to allow access.

**Crawler IP Address:** 54.82.10.251

After the IP is whitelisted, re-learn the source to confirm that the content is successfully ingested.

Element451 also protects certain paths commonly used by website CMS, LMS, SIS and other systems admin functions. We will always skip these paths to maximize security:

* /admin
* /administrator
* /phpmyadmin
* /mysql
* /db'
* /panel
* /cpanel
* /wp-admin
* /admin.php
* /administrator.php

---