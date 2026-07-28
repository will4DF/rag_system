---
title: Getting Started with Bolt Staff Agent Plugins via Zapier (Beta)
url: https://help.element451.com/en/articles/11632278-getting-started-with-bolt-staff-agent-plugins-via-zapier-beta
collection: Bolt AI
---

⚠️ **Open Beta Feature**: This feature is still in active development, may undergo significant changes, and may contain bugs/produce unexpected results. We'd love your feedback as we continue to develop and refine this feature.

# Overview

**Bolt** **Staff Agent Plugins** extends the capabilities of your Bolt Staff Agent by connecting it to external applications through [Zapier](https://zapier.com). Instead of being limited to tasks within Element451, your agent can now interact with thousands of other tools, from CRMs to communication apps like Slack or Microsoft Teams.

In short, Staff Agent Plugins give your Staff Agent new “skills” beyond Element451, helping you break down data silos and streamline tasks across platforms.

## Example Use Cases

* Pull information from a third-party CRM into a staff chat
* Trigger a Slack notification when a specific question is asked
* Add rows to a Google Sheet based on agent conversation data
* Automate steps in complex workflows without switching between platforms

📌 **Note:** To access Staff Agent Plugins, you must be an Element451 administrator or have the ***Administer Staff Agent Plugins***permission added to one of your [custom permission groups](https://help.element451.com/en/articles/9020578-creating-managing-custom-permission-groups).

---

# How It Works

Behind the scenes, this feature uses a secure MCP (Model Context Protocol) server integration to connect your Bolt Staff Agent with external services. For now, Zapier is the only supported integration.

Here’s what happens once set up:

1. Admins configure Zapier actions that the agent is allowed to use.
2. The agent is granted limited access to those external tools via Zapier.
3. When a user requests something that fits, the agent automatically selects the right action and executes it — no manual steps or code required.

🧠 **Good to Know:** Access can be tightly scoped. You decide which tools and actions the agent is allowed to use, providing security and control over what it can (and can’t) do.

---

# Setting It Up

## Prerequisites

* You must have a [Zapier account](https://zapier.com) with access to the apps you want to connect.
* You must be an admin in Element451 with permission to configure Staff Agents.

## Step 1: Create an MCP Server in Zapier

1. Visit [mcp.zapier.com](https://mcp.zapier.com) and sign in with your Zapier account.
2. Click **+ New MCP Server**.
3. In the **New MCP Server** dialog:

   * **MCP Client**: Select **Other**
   * **Name**: Give it something recognizable (e.g., “E451 Outlook Connector”)

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627802075/f3f9561332307a67067cdab5fab8/CleanShot+2025-07-18+at+16_58_48.png?expires=1784333700&signature=de34ba7d3a4150fdbea0d6a891b02ed8297fc369b36ba4d3a5541d6278c36900&req=dSYlEcF%2Bn4FYXPMW1HO4zVSuxNvz%2Ft0Bt0Wgj0jPI249JdKkLnJeyiKohizc%0AeE87%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627802075/f3f9561332307a67067cdab5fab8/CleanShot+2025-07-18+at+16_58_48.png?expires=1784333700&signature=de34ba7d3a4150fdbea0d6a891b02ed8297fc369b36ba4d3a5541d6278c36900&req=dSYlEcF%2Bn4FYXPMW1HO4zVSuxNvz%2Ft0Bt0Wgj0jPI249JdKkLnJeyiKohizc%0AeE87%0A)
4. Click **Create MCP Server**.

## Step 2: Add Tools to Your MCP Server

1. From the **Configure** tab of your server:

   * You’ll see your selected client (“Other”)
2. Click **+ Add Tool**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627803526/aa49fa90452ce65e9d69aa4e1564/CleanShot+2025-07-18+at+16_59_43.png?expires=1784333700&signature=b764e0f51e642a4eb7349908389e3a0b18ed8489e49ff310a83cc691c52505b4&req=dSYlEcF%2BnoRdX%2FMW1HO4zd%2FaJxBXZljwc1xEqcV60Uj9vPGXPa0gWsvPqCzJ%0Ai9C%2B%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627803526/aa49fa90452ce65e9d69aa4e1564/CleanShot+2025-07-18+at+16_59_43.png?expires=1784333700&signature=b764e0f51e642a4eb7349908389e3a0b18ed8489e49ff310a83cc691c52505b4&req=dSYlEcF%2BnoRdX%2FMW1HO4zd%2FaJxBXZljwc1xEqcV60Uj9vPGXPa0gWsvPqCzJ%0Ai9C%2B%0A)
3. Search for and select the app you want to connect to (e.g., Gmail, Outlook, Google Sheets).
4. Choose whether to allow access to all tools within that app or select just one.
5. Authenticate your account when prompted.
6. Configure any additional app-specific settings.
7. Click **Save**.

🔁 You can repeat this to add multiple tools to the same server.

## Step 3: Copy the Server URL

1. Navigate to the **Connect** tab.
2. Under **Connect with server-specific URL**, click **Copy URL**.

   * This is the URL you’ll use in Element451 to link your plugin in the next step.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627806180/b9b51f88dd50bba1ce4a790b1e77/CleanShot+2025-07-18+at+17_01_26.png?expires=1784333700&signature=bb312727f44c794a4349e13fa04a48e363669c136ae121ebb6cec81781e35dd3&req=dSYlEcF%2Bm4BXWfMW1HO4zWBcIHjkP084fq3Kq4w10XCc0F%2BH5IqqpJJXojyS%0ASObx%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627806180/b9b51f88dd50bba1ce4a790b1e77/CleanShot+2025-07-18+at+17_01_26.png?expires=1784333700&signature=bb312727f44c794a4349e13fa04a48e363669c136ae121ebb6cec81781e35dd3&req=dSYlEcF%2Bm4BXWfMW1HO4zWBcIHjkP084fq3Kq4w10XCc0F%2BH5IqqpJJXojyS%0ASObx%0A)

##

## Step 4: Add the Zapier Plugin in Element451

1. Log in to Element451.
2. Click your profile icon in the top right corner.
3. Navigate to **Settings > Integrations**.
4. In the left-hand menu, select **Staff Agent Plugins**.
5. Click **+ Add Plugin**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627807284/d907499cca21f68f293ff1b3eceb/CleanShot+2025-07-18+at+17_04_21.png?expires=1784333700&signature=5ef0e1d212a7cffb36f588d18fafc6f6f6f1ea302b5949c915c18e322647a85f&req=dSYlEcF%2BmoNXXfMW1HO4zTuvkiBtg%2FInpfy1OpX9G9nyxD5n%2Br3LRwLNhP2W%0ACY%2FV%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627807284/d907499cca21f68f293ff1b3eceb/CleanShot+2025-07-18+at+17_04_21.png?expires=1784333700&signature=5ef0e1d212a7cffb36f588d18fafc6f6f6f1ea302b5949c915c18e322647a85f&req=dSYlEcF%2BmoNXXfMW1HO4zTuvkiBtg%2FInpfy1OpX9G9nyxD5n%2Br3LRwLNhP2W%0ACY%2FV%0A)
6. **Select Plugin Type**: Choose **Zapier**
7. In the plugin setup window:

   * **Identifier**: Enter an internal name for the plug-in. We recommend making it match the same name you used in Zapier.
   * **URL**: Paste the **Server URL** you copied from Zapier
   * **Headers** (optional): Add any HTTP headers if needed

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627808103/0906389a565412bf54f5f73bd9f5/CleanShot+2025-07-18+at+17_05_41.png?expires=1784333700&signature=d19308d096767baa1b007b4b55b54f41b7443235bc97a49f3574c981e418d9a6&req=dSYlEcF%2BlYBfWvMW1HO4zVSwXRgq3i3I%2BuSR6jk8Ik%2BVnF0VevMFrFXwAeqd%0AAjcd%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627808103/0906389a565412bf54f5f73bd9f5/CleanShot+2025-07-18+at+17_05_41.png?expires=1784333700&signature=d19308d096767baa1b007b4b55b54f41b7443235bc97a49f3574c981e418d9a6&req=dSYlEcF%2BlYBfWvMW1HO4zVSwXRgq3i3I%2BuSR6jk8Ik%2BVnF0VevMFrFXwAeqd%0AAjcd%0A)
8. Click **Create** (upper right).

## You're Connected! Next Steps...

You’ll now see your Zapier plugin listed in the plugin list. Your Bolt Staff Agents can start using it to trigger actions in your connected apps.

Need to do more? Just repeat the process to add additional plugins for different tools or tasks.

---

# Video Setup Guide + Use Case Demo

The video below guides you through setting up a Staff Agent Plugin using Zapier's MCP, which connects your Staff Agent in Element451 to thousands of applications.

You'll learn:

* How to configure the plugin in Zapier
* How to connect the plugin in Element451
* How to utilize the plugin via a demo use case

---

# Managing Plugins

To edit your settings or delete a plugin in Element451:

1. Click your profile icon in the top right corner.
2. Navigate to **Settings > Integrations**.
3. In the left-hand menu, select **Staff Agent Plugins**.
4. Locate your plugin from the list and select the pencil icon to edit or the trash can icon to delete.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627810977/710cd5d7d2c21949892aab3358b7/CleanShot+2025-07-18+at+17_08_50.png?expires=1784333700&signature=7c8b232f57c05a6135e4b8f0db9d7d5a6b87a58833bf220165acf98ac9930ae5&req=dSYlEcF%2FnYhYXvMW1HO4zYJv1RUT5KTHodBghxcyfx3f2hovTYLQMRmxGpXR%0Ax2CR2Ftinh%2BFw7XMAd4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1627810977/710cd5d7d2c21949892aab3358b7/CleanShot+2025-07-18+at+17_08_50.png?expires=1784333700&signature=7c8b232f57c05a6135e4b8f0db9d7d5a6b87a58833bf220165acf98ac9930ae5&req=dSYlEcF%2FnYhYXvMW1HO4zYJv1RUT5KTHodBghxcyfx3f2hovTYLQMRmxGpXR%0Ax2CR2Ftinh%2BFw7XMAd4%3D%0A)

To manage the plugin's tools and Zapier settings, you will need to do so from your Zapier account. Visit [mcp.zapier.com](https://mcp.zapier.com) and sign in with your Zapier account.

---

# Use Case Examples

Curious about how you could use Bolt Staff Agent Plugins? Here are a few examples of applications you could connect to and how you could use them.

🎥 Be sure to check out our [setup guide video](https://www.loom.com/share/640c9b39cdd54b8bb25f2170ec99d327?sid=07aebb37-4d59-4547-bb0e-51182610f935), where we walk you through each of these use case examples.

## Outlook: Finding, Summarizing, + Forwarding Email

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632800020/e4e40ee7fcb8cef3c1ee272a5107/CleanShot+2025-07-22+at+10_59_07.png?expires=1784333700&signature=49307279ffbf47469513fde39ba5505ee6240279a2de3e4169452209687dd40a&req=dSYkFMF%2BnYFdWfMW1HO4zTXhVoTTDxsJHeQ3x4boDn49iFeIYrL%2BbKunikzT%0AmUF3sStTNHHW%2BbzeF90%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632800020/e4e40ee7fcb8cef3c1ee272a5107/CleanShot+2025-07-22+at+10_59_07.png?expires=1784333700&signature=49307279ffbf47469513fde39ba5505ee6240279a2de3e4169452209687dd40a&req=dSYkFMF%2BnYFdWfMW1HO4zTXhVoTTDxsJHeQ3x4boDn49iFeIYrL%2BbKunikzT%0AmUF3sStTNHHW%2BbzeF90%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632803648/27fef3b69a4327dd22877208e5e1/CleanShot+2025-07-22+at+10_59_59.png?expires=1784333700&signature=16c9cbd6095dc31217cb097c622593ad835a62b516beade48f2daf641ff855fc&req=dSYkFMF%2BnodbUfMW1HO4zUM8uIkMhUQ6hiulSo5qHUwaPt3OtzH8d2tTHVI8%0AOxG%2FZyHN8Yyya77U5yM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632803648/27fef3b69a4327dd22877208e5e1/CleanShot+2025-07-22+at+10_59_59.png?expires=1784333700&signature=16c9cbd6095dc31217cb097c622593ad835a62b516beade48f2daf641ff855fc&req=dSYkFMF%2BnodbUfMW1HO4zUM8uIkMhUQ6hiulSo5qHUwaPt3OtzH8d2tTHVI8%0AOxG%2FZyHN8Yyya77U5yM%3D%0A)

## Typeform: Retrieving Form Response Data

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632796410/6ae9aa67f89143097e5c86a1bd3c/CleanShot+2025-07-22+at+10_51_39.png?expires=1784333700&signature=c5f7995a19c1d2df85be3b25f1c99a640a41ab4b4095407e6b2bce9b4647aea0&req=dSYkFM53m4VeWfMW1HO4zVp7d7zZVWFF%2BRFcfD7u4Z7EQ9W9sb0woVUE5v9o%0ASvT4kOsljfdGeBvHycU%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632796410/6ae9aa67f89143097e5c86a1bd3c/CleanShot+2025-07-22+at+10_51_39.png?expires=1784333700&signature=c5f7995a19c1d2df85be3b25f1c99a640a41ab4b4095407e6b2bce9b4647aea0&req=dSYkFM53m4VeWfMW1HO4zVp7d7zZVWFF%2BRFcfD7u4Z7EQ9W9sb0woVUE5v9o%0ASvT4kOsljfdGeBvHycU%3D%0A)

## Microsoft Excel: Looking Up Tuition Rate

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632805526/e977194949b6abea027861058945/CleanShot+2025-07-22+at+11_01_57.png?expires=1784333700&signature=32182dd6c86731d8c6bb045ec48f468b4844297e32fce9e389dd367f51abdfbb&req=dSYkFMF%2BmIRdX%2FMW1HO4zdgBeyMUYB9GawXuRueU%2FbdbwAOH1djXZliMTiVq%0AJc88Zv%2B45T7h2X1XZL0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1632805526/e977194949b6abea027861058945/CleanShot+2025-07-22+at+11_01_57.png?expires=1784333700&signature=32182dd6c86731d8c6bb045ec48f468b4844297e32fce9e389dd367f51abdfbb&req=dSYkFMF%2BmIRdX%2FMW1HO4zdgBeyMUYB9GawXuRueU%2FbdbwAOH1djXZliMTiVq%0AJc88Zv%2B45T7h2X1XZL0%3D%0A)

---