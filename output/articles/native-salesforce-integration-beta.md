---
title: Native Salesforce Integration [Beta]
url: https://help.element451.com/en/articles/12633650-native-salesforce-integration-beta
collection: Integrations
---

Sync Salesforce with Element451 to unlock real-time data sharing between your CRM and your AI-powered engagement tools.

📌 **Note:** This feature is currently in Beta. For access, reach out to your account manager or live support.

# Overview

Element451’s Salesforce integration makes it easy to connect your existing CRM with the powerful engagement and automation features of Element451. This native integration supports regular data syncs, giving your teams and AI Agents a consistent, up-to-date view of every student across both systems.

With a quick setup process, you can be up and running in minutes—no middleware or plugins required.

Whether you’re using Salesforce as your institutional system of record or combining data across tools, this connection ensures your workflows stay aligned without duplicating effort.

## Key Features

* Regular sync (every 15 minutes) between Salesforce and Element451
* Map data between systems with flexible field-matching
* Sync contacts and conversations
* Choose which system is the “source of truth” for key fields
* Easily configure and test your setup through a built-in interface

---

# How It Works

The integration uses APIs to move data directly between Element451 and Salesforce—no middleware or plugins required. You control how data flows, which fields sync, and what values take priority.

## Syncing + Field Mapping

You can sync two main data types—***Contacts*** and ***Conversations***. Any Element451 entity type can be mapped to any Salesforce object. You will be able to specify mapping when configuring the integration.

When mapping fields from Salesforce to Element451, you must select the key for each field, along with the key for the equivalent field in Element451.

* Element ID and Salesforce ID are required.
* Mapped fields must have a **single value** (string, integer, date, etc).
* Repeater fields are not supported, but multi-select (checkbox) fields are.

### Source of Truth

During setup, you’ll choose a canonical system—Salesforce or Element451. This setting defines which platform *owns* each field and, therefore, controls how data is written during sync. This setting is required for **every** mapped field. It works like this:

* All fields are assigned an owner based on the system you select.
* When a record is created in either platform, all available field values are written.
* When a record is updated, **only the fields owned by that system are updated**.
* Ownership is absolute—values aren’t compared or conditionally updated. For example, if *Intended Major* is “Business” in Element451 and empty in Salesforce, but the field is Salesforce-owned, the empty Salesforce value will overwrite Element451 during sync.

---

# Setting Up the Integration

## Setting Up Your External Client App in Salesforce

1. [Create an External Client App](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&type=5). This app should be exclusively used by Element451, but you can name it anything you’d like.
2. In the OAuth Settings, add the callback url: "<https://api.451.io/clients/integrations/salesforce/oauth2>"
3. Select the following OAuth scopes:

   * Manage user data via APIs (api)
   * Perform requests at any time (refresh\_token, offline\_access)
4. Find your "Consumer Key" and "Consumer Secret."

   * "Consumer Key" will be your Client ID
   * "Consumer Secret" will be your "Secret Key"
5. Enable these security settings:

   * Require secret for Refresh Token Flow
   * Enable Refresh Token Rotation

### Refresh Token Policy

Salesforce offers several settings for refresh token expiration setting:

* “Refresh token is valid until revoked”
* “Expire refresh token after specific time”
* “Expire refresh token if not used for specific time”

You can choose any of these options. The only unsupported setting is **“Immediately expire refresh token”** because Element451 must reuse the refresh token for multiple API calls during each sync.

## Connecting Salesforce to Element451

1. Click on your avatar/profile picture in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Integrations**.
3. From the left-hand menu, select **CRM Integrations.**
4. Select **Salesforce**.

   * 📌 **Note**: You can only sync one CRM at a time.
5. Configure the Connection Settings:

   * Salesforce URL
   * Client ID
   * Secret Key
6. Click '*Continue*' in the top left corner.
7. Sign in to your Salesforce account, and you will be redirected back to Element.
8. Once connected, you can configure and sync. Navigate through the tabs (Sync Preferences, Mappings, Test) to configure the settings. We explain these settings below.

### Conversation Sync Preferences

* **Sync Conversations**: When enabled, we will export conversation data and the contacts associated with those Conversations from Element451 and push them to Salesforce.  
  ​

  + **Conversation Entity**: Select the Salesforce object that corresponds to Conversations in Element451.  This is typically a custom entity or object.

### Contact Sync Preferences

* Contact syncing is enabled by default and cannot be turned off. Contacts will be continually synced automatically by the integration.   
  ​

  + **Contact Entity**: Select the Salesforce object that corresponds to Contacts in Element451.  This is typically “Contact” but could be “Opportunity” or even a custom object.    
    ​
  + **Import Mode**: How Element451 should handle incoming contacts from Salesforce.

    - By default, we will “Match Existing” contacts.
    - Optionally, you can opt to “Update Existing” or “Create New” contacts.  
      ​
  + **Export Mode**: How Element451 should attempt to update data in Salesforce.

    - By default, we will export every user related to the conversations being exported.
    - If export mode is set to **“Match Existing and Import New,”** we will not attempt to update any existing users in Salesforce. But, if the user is not found in Salesforce, we will insert them with the complete set of fields, including Salesforce-owned fields.
    - If export mode includes “**Update Existing and Import New,**” we will:

      * Export all Element451-owned mapped fields to the Salesforce user
      * If that creates a new Salesforce user, we will export all the mapped fields with values to it, including the Salesforce-owned fields.

---

# Mappings

Mappings determine which fields in Salesforce should be equivalent to certain fields in Element 451. Please note that we only support a specific set of fields. If you want to set up a custom mapping between Salesforce and Element 451, please use Import + Export or our API.

## Adding Mappings

Mappings are categorized by: *Contact* and *Conversation*. To get started mapping a field:

1. Click the "+ Add Mapping" button under the respective category
2. Select a value for the Element451 Field and a value for the Salesforce Field
3. Select the Canonical System (either Element451 or Salesforce)
4. Save

## Preview + Test

Preview the data mapped and test to verify that the mapping functions are correct and as expected.

* Import and Export have individual tests:

  + Import: You can optionally input a Salesforce ID or Element451 user
  + Export: You can optionally input a Salesforce ID or Element451 user
* You will be presented with a preview of the incoming and outgoing data.
* You will see a status chip that will say "*inserted*," "*updated*." "*unchanged*," "*ignored*," "deactivated," "upserted," or "failed" to indicate what the result of the real run would be.
* You can choose to "test" the process by actually importing the contact or exporting the selected user and their conversations.

---

# IntegrationLogs

You can view the individual contact/conversation history in the Integration Logs from the left-hand menu on the Integrations page.

There will be a record of every failed or successful contact imported, contact exported, or conversation exported.

Failed operations can be retried by viewing the error log and clicking "Retry" in the top right corner. When you retry, the Integration Logs page will be reloaded and the new run will appear at the top.

---