---
title: Data Connectors
url: https://help.element451.com/en/articles/9007788-data-connectors
collection: Data Management
---

Using Data Connectors is your way to manage how imports and exports are linked to external systems.

# Overview

Data Connectors are the different outlets you can pull data from and put data into besides just importing a file from your computer or exporting a report to your email.

Element451 distinguishes between **connector-level** problems (which disable the connector) and **task-level** problems (which fail only that individual import or export). See [Troubleshooting](#h_troubleshooting) below.

## Accessing Data Connectors

To access your Data Connectors, navigate to **Data + Automations > Import + Export > Connectors.**

[![](https://downloads.intercomcdn.com/i/o/976137076/466b0dc48da96e15e5bfe200/Screenshot+2024-02-27+at+10_12_58%E2%80%AFPM.png?expires=1784333700&signature=e95348c320f8da2dc6f62a68091f9ad8be48eaa2cbcb2cf0f05c14a1c755d60c&req=fSchF8p5nYZZFb4f3HP0gFlJ1DViCPSw%2Bu5DGmJZA0i%2BTzaeVqGdLNOMw0yq%0AqOwav4Sp%2FbuxM6HDhQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976137076/466b0dc48da96e15e5bfe200/Screenshot+2024-02-27+at+10_12_58%E2%80%AFPM.png?expires=1784333700&signature=e95348c320f8da2dc6f62a68091f9ad8be48eaa2cbcb2cf0f05c14a1c755d60c&req=fSchF8p5nYZZFb4f3HP0gFlJ1DViCPSw%2Bu5DGmJZA0i%2BTzaeVqGdLNOMw0yq%0AqOwav4Sp%2FbuxM6HDhQ%3D%3D%0A)

## Types of Data Connectors

* SFTP
* Google Drive
* Dropbox

---

# Adding + Managing Data Connectors

## Adding Data Connectors

1. Navigate to **Data + Automations** > **Import + Export**.
2. In the left-hand menu, select "**Connectors**."
3. Click the "**Create** **Connector**" button in the top right corner of the header.
4. Select which type of connector you wish to connect: **Dropbox**, **Google** **Drive**, or **SFTP**.

   * For Dropbox and Google, you will proceed through the authentication process that allows Element451 to connect with the 3rd party platform.
   * For SFTP, you will be prompted to provide the necessary credentials.

## Editing + Deleting Data Connectors

1. Navigate to **Data + Automations** > **Import + Export**.
2. In the left-hand menu, select "**Connectors**."
3. From the Connectors list, locate the one you wish to delete.
4. Click the **More (⋮)** icon at the end of that connector's row.
5. Select either **Edit** or **Delete**, based on your need.

---

# Special Notes on Google Drive

## Deleting Google Drive Connector / Revoking Access

To revoke Drive access, delete the Google connector here in Import + Export. If you remove access directly from your Google account, it will disconnect *all* Element451 integrations—including calendar access in Appointments, if that's also connected.

---

# Troubleshooting

## When a Connector Turns Off

A connector is only automatically disabled when Element451 can't connect to the third-party account at all. Common causes:

* The account's password was changed, or the connection was revoked from the Google, Dropbox, or SFTP side
* The refresh token has expired and can no longer renew automatically
* SFTP credentials, host key, or private key are no longer valid

If the connector turns off, you'll see an **error icon** next to the connector in the Connectors list — hover the icon to view the specific error message. You'll also find the explanation in the connector's details view. To restore it, open the connector, re-authenticate (Google Drive / Dropbox) or update the credentials (SFTP), and save.

## When a Task Fails but the Connector Stays On

If an individual import or export fails—but your connector is still active—the issue is almost always with a specific file or folder, not the connection itself. Common causes:

* The folder or file isn't shared with the connected account
* The file was moved, renamed, or deleted
* A temporary network error or rate limit (these will retry automatically)
* The SFTP path doesn't exist or the user lacks permission to that directory

Check the task's status under **Data + Automations > Import + Export > Tasks** to see the specific error. The connector itself does not need to be reconnected.

## "This app is blocked" Error (Google Drive)

If you see the error message "This app is blocked" when attempting to add a **Google Drive Import + Export Connector**, it is typically due to a misconfiguration of Google's OAuth settings within your institution's Google Workspace. Check out [this article](https://help.element451.com/en/articles/9999308-google-blocking-app-access-to-google-drive-in-import-export) for assistance in troubleshooting.

---