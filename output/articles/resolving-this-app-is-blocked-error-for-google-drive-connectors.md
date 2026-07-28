---
title: Resolving "This app is blocked" Error for Google Drive Connectors
url: https://help.element451.com/en/articles/9999308-resolving-this-app-is-blocked-error-for-google-drive-connectors
collection: Data Management
---

# Overview

If you see the error message "This app is blocked" when attempting to add a **Google Drive Import + Export Connector**, it is typically due to a misconfiguration of Google's OAuth settings within your institution's Google Workspace. This article will help walk you through how to resolve this issue.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434232944/ff0d381fbb6223916f60617ad0c6/app%2Bis%2Bblocked.png?expires=1784333700&signature=52e14e631b74f76fa6d10a6b4418c71c888c48a95be5f0b83b27aba42458da42&req=dSQkEst9n4hbXfMW1HO4zR1tHQ3T5wY1GrddV%2FEFoAA3nFOpRuVf8gpjvQTl%0ArvNGeKyTeREDR6DdV8w%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434232944/ff0d381fbb6223916f60617ad0c6/app%2Bis%2Bblocked.png?expires=1784333700&signature=52e14e631b74f76fa6d10a6b4418c71c888c48a95be5f0b83b27aba42458da42&req=dSQkEst9n4hbXfMW1HO4zR1tHQ3T5wY1GrddV%2FEFoAA3nFOpRuVf8gpjvQTl%0ArvNGeKyTeREDR6DdV8w%3D%0A)

---

# Troubleshooting Steps

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1231934214/8b7c21e94e56eb393fe381514e0c/Note.png?expires=1784430000&signature=aa1081a1be604af47b589c2118d96efc5fc282f0b45b9e612a60e781644f3d7a&req=dSIkF8B9mYNeXfMW3Hu4gZkptJiaLitFOVT86FW4nEZ8GJmQrXoQ8T4sRmvS%0A4A%3D%3D%0A) These steps apply only to **Google Workspace** accounts. If you are using a personal Google Drive linked to a @gmail.com account and the Element451 app is blocked, you'll need to choose a different export destination.

## Step 1: Use Incognito Mode

Sometimes, browser extensions or cached data can interfere with account connections. Using Incognito mode helps bypass these issues.

1. Open a new Incognito window in your browser.
2. Log in to your Element451 instance.
3. Try connecting your Google Drive again via Import + Export.

## Step 2: Check OAuth Settings in Google Workspace

If Incognito mode doesn't help, the next step is to check the OAuth settings in your Google Workspace.

For this step, you will need help from your institution's **Google Workspace Admin.** This will likely be someone from your IT team.

1. Log in to your institution's Google Admin account.
2. Navigate to the **Users** tab and double-check that the user(s) trying to connect Element451 are listed in this section.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434230536/23bdc5dd8e353ffe62af385147be/Google%2BWorkspace%2B-%2BUsers.png?expires=1784333700&signature=54cfc8e4eb7167b1ec933d924149312a5c988365aad06f5e3da3619377461846&req=dSQkEst9nYRcX%2FMW1HO4zUG9O0%2FOLxDgZdDiohia4lPUvTrMMB7Z%2FAdDXiPb%0ACZ6Y%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434230536/23bdc5dd8e353ffe62af385147be/Google%2BWorkspace%2B-%2BUsers.png?expires=1784333700&signature=54cfc8e4eb7167b1ec933d924149312a5c988365aad06f5e3da3619377461846&req=dSQkEst9nYRcX%2FMW1HO4zUG9O0%2FOLxDgZdDiohia4lPUvTrMMB7Z%2FAdDXiPb%0ACZ6Y%0A)
3. From the admin console, navigate to **Security > API Controls**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434230792/43ef49be30465040716cdcaa6e4a/Google%2BWorkspace%2B-%2BAPI.png?expires=1784333700&signature=d81b2b3862e4e4999e7cfa5f9d226e4f6b1539bffdaa781b1fd8f1b4292e9c2b&req=dSQkEst9nYZWW%2FMW1HO4zbkTa7lxFdAlYA2Zir%2FTPIHofx2Zdf5YdxQb2Djb%0AE0uN%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434230792/43ef49be30465040716cdcaa6e4a/Google%2BWorkspace%2B-%2BAPI.png?expires=1784333700&signature=d81b2b3862e4e4999e7cfa5f9d226e4f6b1539bffdaa781b1fd8f1b4292e9c2b&req=dSQkEst9nYZWW%2FMW1HO4zbkTa7lxFdAlYA2Zir%2FTPIHofx2Zdf5YdxQb2Djb%0AE0uN%0A)
4. Select **Manage third-party app access**.

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434231321/08abe047d56690dae2e8350acd18/third-2Bparty-2Bapp-2Baccess.png?expires=1784333700&signature=166108d130121f8007dcb189d02a78904f1d5b9db6874b4e605016f65f1a1c3f&req=dSQkEst9nIJdWPMW1HO4zU%2F4Uo0Y7coYj84ySnXPTVWrBNCP1U9KSYZGerF0%0APbPn%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1434231321/08abe047d56690dae2e8350acd18/third-2Bparty-2Bapp-2Baccess.png?expires=1784333700&signature=166108d130121f8007dcb189d02a78904f1d5b9db6874b4e605016f65f1a1c3f&req=dSQkEst9nIJdWPMW1HO4zU%2F4Uo0Y7coYj84ySnXPTVWrBNCP1U9KSYZGerF0%0APbPn%0A)
5. Ensure that **OAuth access** is enabled for all users and domains in the workspace. If not, grant the required access.

## Step 3: Add Element451 as a Trusted OAuth Client

If the above steps don't resolve the issue, you'll need to add Element451 as a trusted OAuth client:

1. Log in to your institution's Google Admin account.
2. Navigate to **Security > Access and data control > API controls**.
3. Under "App access control," click **Manage third-party app access**.
4. Click the **Add app** button.
5. Select **OAuth App Name or Client ID** from the dropdown menu.
6. Enter the Element451 Client ID: `380011789798-teilg48si673lnuakb2v0kfkk0qljh88.apps.googleusercontent.com`
7. Click **Search**.
8. Once Element451 appears, click **Select**.
9. Set the access level to **Trusted.**
10. Click **Save**.

After completing these steps, wait a few minutes for the changes to propagate through your Google Workspace environment, then try connecting Element451 to Google Drive again.

---