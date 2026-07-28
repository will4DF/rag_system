---
title: SFTP Management
url: https://help.element451.com/en/articles/9953382-sftp-management
collection: Settings + Permissions
---

# Overview

SFTP Management is a self-service tool that lets you create and manage access to your Element451 SFTP accounts. It gives you the flexibility to control access to your accounts securely and efficiently, all from within your General Settings.

To manage your SFTP accounts, you must be an Element451 administrator or have the  *SFTP Administrator* permission enabled on one of your custom permission groups.   
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203176467/e75a6cf460c2dbd038e1e9184d93/SFTP-Overview.png?expires=1784333700&signature=95b41fb6b427626ad9fc488437cdc496ae4f57e5f20e2ea1e0ac991578a3169b&req=dSInFch5m4VZXvMW1HO4zSBRR%2FQhyQDkkbQ7fn%2B0fXmgWYNRdF41Ox%2B68cOn%0A%2FC%2B5TXERNQ2dd0JE4Rw%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203176467/e75a6cf460c2dbd038e1e9184d93/SFTP-Overview.png?expires=1784333700&signature=95b41fb6b427626ad9fc488437cdc496ae4f57e5f20e2ea1e0ac991578a3169b&req=dSInFch5m4VZXvMW1HO4zSBRR%2FQhyQDkkbQ7fn%2B0fXmgWYNRdF41Ox%2B68cOn%0A%2FC%2B5TXERNQ2dd0JE4Rw%3D%0A)

## **Key Features**

* **Two Account Types**:

  + Password
  + SSH/RSA
* **Access Control Options**:

  + Full Access: Access all directories
  + Directory-Specific Access: Restrict access to a specific directory
* **Audit Logs**: Track account activities, including password reveals, instruction sharing, and recipient access to credentials.
* **Multiple Accounts**:

  + Create and manage multiple SFTP accounts, each with its own tailored access

## Accessing SFTP Management

1. Click on your avatar in the top right corner of the main navigation menu.
2. Navigate to **General Settings** > **SFTP Management**.

---

# How to Create an SFTP Account

## Password SFTP Account

[![Screenshot of SFPT management interface](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203180458/0e424a9c0b096d697d434ffba354/SFTP-Password+Account.png?expires=1784333700&signature=759e311c576ec92d061caedac147320a75f8ce4b70d1cb296c78d64e04effc88&req=dSInFch2nYVaUfMW1HO4zRW%2FHPyfx8AdR87YJuSDfwDu7tvUlSU0D23kE5B7%0A9EEeHn5Uwy5aN0s%2F6Xg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203180458/0e424a9c0b096d697d434ffba354/SFTP-Password+Account.png?expires=1784333700&signature=759e311c576ec92d061caedac147320a75f8ce4b70d1cb296c78d64e04effc88&req=dSInFch2nYVaUfMW1HO4zRW%2FHPyfx8AdR87YJuSDfwDu7tvUlSU0D23kE5B7%0A9EEeHn5Uwy5aN0s%2F6Xg%3D%0A)

1. Click on the blue **“Add SFTP Account"** ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203177693/8eb6e2a13a8f09dad25c0b9c64b6/Add+SFTP+Account+-+Button.png?expires=1784430000&signature=cb5a9a330ab1f5a1d84c71ef7ba46cd52ef2dd0a2de116b99c6272706445ff11&req=dSInFch5modWWvMW3Hu4gbLCcnTdMrDCc5wJ%2Fs7SDFDP3X0j536nkSfo%2BlhW%0AHw%3D%3D%0A) button.
2. **Username**: Give your account a **username**/**slug**
3. **Type**: Select **“Password”** as your account type**.**
4. **Generate or Create a Password**:

   * Click on the **key icon** to automatically generate a secure password (recommended).
   * Alternatively, create your own password and confirm it in the “Confirm Password” field.
5. **Directory**:

   * **Full Access**: Leave this field empty if the account needs access to all folders, including the root.
   * **Directory**: If you wish to restrict a user's access to a specific folder, input the desired path (e.g., `folder/subfolder`).
6. **Save**: Click **Save** to create the SFTP account.
7. **Share the Configuration (Optional)**: Once the account is created, you may need to share the login details securely. For detailed steps, refer to the section “How to Share SFTP Configuration” below.

## SSH/RSA SFTP Account

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203182535/0e1a41ce3ef3f4e9abe56175a20b/SFTP-SSH-Add.png?expires=1784333700&signature=2b975c6aac99f8a57431770894d4e21cecc291f33d669c8929f05c89c4736cdd&req=dSInFch2n4RcXPMW1HO4zbLfXWrwWpHqZJS%2BytMEWi5BXBug7GO1knVYDAO1%0AxXNWJuHJATo8QhJGji0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203182535/0e1a41ce3ef3f4e9abe56175a20b/SFTP-SSH-Add.png?expires=1784333700&signature=2b975c6aac99f8a57431770894d4e21cecc291f33d669c8929f05c89c4736cdd&req=dSInFch2n4RcXPMW1HO4zbLfXWrwWpHqZJS%2BytMEWi5BXBug7GO1knVYDAO1%0AxXNWJuHJATo8QhJGji0%3D%0A)

1. Click on the blue **“Add SFTP Account"** ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203177693/8eb6e2a13a8f09dad25c0b9c64b6/Add+SFTP+Account+-+Button.png?expires=1784430000&signature=cb5a9a330ab1f5a1d84c71ef7ba46cd52ef2dd0a2de116b99c6272706445ff11&req=dSInFch5modWWvMW3Hu4gbLCcnTdMrDCc5wJ%2Fs7SDFDP3X0j536nkSfo%2BlhW%0AHw%3D%3D%0A)button.
2. **Username**: Give your account a **username**/**slug**
3. **Type**: Select **“SSH/RSA”** as your account type.
4. **SSH/RSA Public Key**: Add your public key
5. **Enter Account Details**: Provide a name and any other necessary information.
6. **Directory**:

   * **Full Access**: Leave this field empty if the account needs access to all folders, including the root
   * **Directory**: If you wish to restrict a user's access to a specific folder, input the desired path (e.g., `folder/subfolder`)
7. **Save**: Click **Save** to create the SFTP account.

Check out [this help article](https://help.element451.com/en/articles/9146573-securely-transferring-files-sftp#h_c1dc7d83a4) to learn how to generate your own RSA key pair.

---

# Managing Your SFTP Accounts

Once your SFTP accounts are created, they will be displayed in the account listing. From this list, you can view details or delete accounts as needed.  
​

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203193980/2931883e9403afb8cabd21146a30/SFTP-ManageAccounts.png?expires=1784333700&signature=9385aab8d4b170dccfa79217b25ca335b93fe81d199542f851bbc650bfccb279&req=dSInFch3nohXWfMW1HO4zU007vJk%2F7XjvskfaKkQnEHEURNT%2FxCEH%2Bi72GTb%0Ad9A2kjxVPjPBZlSLr%2Fs%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203193980/2931883e9403afb8cabd21146a30/SFTP-ManageAccounts.png?expires=1784333700&signature=9385aab8d4b170dccfa79217b25ca335b93fe81d199542f851bbc650bfccb279&req=dSInFch3nohXWfMW1HO4zU007vJk%2F7XjvskfaKkQnEHEURNT%2FxCEH%2Bi72GTb%0Ad9A2kjxVPjPBZlSLr%2Fs%3D%0A)

## Viewing an Account

Open an account to:

* See its configuration (server, port, username)
* Reveal or copy the account password (password accounts)
* Email configuration and password (password accounts)
* Access and download the **Audit Logs** to review account activity
* Create an SFTP [connector](https://help.element451.com/en/articles/9007788-data-connectors) for Element451 import/export

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1216711814/3f2f884e1dae3ea022e615969947/SFTP%2BAccount%2BConfig.png?expires=1784333700&signature=640a18d4b5901114990e284d4e9e7dbff7487db346a7e77e8c7ccd8abd2509ad&req=dSImEM5%2FnIleXfMW1HO4zf57LjOd%2FpxvyUU1yKvWo3DKnpVLChdd7GTYwZ8f%0A2HISR4m04MkCvDpNnl0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1216711814/3f2f884e1dae3ea022e615969947/SFTP%2BAccount%2BConfig.png?expires=1784333700&signature=640a18d4b5901114990e284d4e9e7dbff7487db346a7e77e8c7ccd8abd2509ad&req=dSImEM5%2FnIleXfMW1HO4zf57LjOd%2FpxvyUU1yKvWo3DKnpVLChdd7GTYwZ8f%0A2HISR4m04MkCvDpNnl0%3D%0A)

## Deleting an Account

If you need to change credentials or update or disable access, you must **delete the existing account**. Once deleted, the account and its credentials will no longer be active.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203209637/3489a278357715c60ef2f61e56a6/Important.png?expires=1784430000&signature=ae7a62fb1d6f7a08af41d43accc4a19bdef1dabf39efc63a395fbd7e6a04044e&req=dSInFct%2BlIdcXvMW3Hu4gZEzAiQt1qh15ald8kuq9%2FpPGY5KvuZeyYjAuxuP%0A7A%3D%3D%0A) Before deleting an account, we recommend downloading the audit logs for information retention.

---

# Audit Logs

## Tracking Account Activity

Each SFTP account has an attached **Audit Log** that provides a transparent overview of account activities:

* **Password Reveals**: When an internal user views the password.
* **Instruction Sharing**: When an internal user sends configuration instructions to a recipient, including the recipient’s email address.
* **Recipient Access**: When a recipient views the secure SFTP credentials.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203197365/27c418190e3dd6e3126ed427b13a/SFTP-AuditLogs.png?expires=1784333700&signature=b4212e2ea7c4d999fd7a79a22b45a0e8ab8fd09a8363714044aa8586ef639448&req=dSInFch3moJZXPMW1HO4zfAx0sF3Dm%2BAGVjxZuwfoRz8%2Bjoq9Os02ACwdR9o%0AebauNMThcUzkJouf4sg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203197365/27c418190e3dd6e3126ed427b13a/SFTP-AuditLogs.png?expires=1784333700&signature=b4212e2ea7c4d999fd7a79a22b45a0e8ab8fd09a8363714044aa8586ef639448&req=dSInFch3moJZXPMW1HO4zfAx0sF3Dm%2BAGVjxZuwfoRz8%2Bjoq9Os02ACwdR9o%0AebauNMThcUzkJouf4sg%3D%0A)

## Downloading Audit Logs

You have the ability to download a CSV file containing the audit logs for an SFTP account. This is extremely useful when you need to delete an account as it allows you to preserve and retain the audit logs. To start the download:

1. Open the SFTP Account
2. Click the **“Download Audit Logs”** button in the top right corner.
3. The download should start immediately.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1216720438/922c4d05eb61ac39205d498fb15b/SFTP+Account+Config.png?expires=1784333700&signature=3308cb052e56b8d24113ac4709f3cb384815b54d6edaea2990341cfec6c436e9&req=dSImEM58nYVcUfMW1HO4zX397%2BvBp5ruHwVi6JEyXQwqEXMaY2uGCyuNETlL%0AU5wajfgmsZ232wl2if4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1216720438/922c4d05eb61ac39205d498fb15b/SFTP+Account+Config.png?expires=1784333700&signature=3308cb052e56b8d24113ac4709f3cb384815b54d6edaea2990341cfec6c436e9&req=dSImEM58nYVcUfMW1HO4zX397%2BvBp5ruHwVi6JEyXQwqEXMaY2uGCyuNETlL%0AU5wajfgmsZ232wl2if4%3D%0A)

---

# How to Share SFTP Configuration (Password Accounts)

For added security, password-based SFTP configurations should be shared using the secure send process:

1. Open the SFTP Account.
2. Click the **“Send Configuration”** button in the top right corner.
3. Enter the recipient’s email address. ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203172333/7697e99fa55f214d988105414c6c/Note.png?expires=1784430000&signature=0b856a7309da96ffe5ded0b86e2b067d136fded2494c154f5ee570a39f189c76&req=dSInFch5n4JcWvMW3Hu4gdKLxLJMZ76KSAsrCv5Cb5JEcw2apdlxqmpTre5%2B%0A1g%3D%3D%0A) The credentials will not be shared directly in the email for security reasons.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203198535/a5cef793c6cda3c6bb9892c3b458/SFTP-SendConfigEmail.png?expires=1784333700&signature=de123aaa5dd8fa3f69d473210dbce5a1fc2759b078577b0760c2e4b8fc8374be&req=dSInFch3lYRcXPMW1HO4zXRIimIHOiimgzNq6QxZRQ%2BX9TZAPc5EzZ4RjOL3%0AftHc%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203198535/a5cef793c6cda3c6bb9892c3b458/SFTP-SendConfigEmail.png?expires=1784333700&signature=de123aaa5dd8fa3f69d473210dbce5a1fc2759b078577b0760c2e4b8fc8374be&req=dSInFch3lYRcXPMW1HO4zXRIimIHOiimgzNq6QxZRQ%2BX9TZAPc5EzZ4RjOL3%0AftHc%0A)

## How does the recipient access the credentials?

1. The recipient will receive an email with a link to access the secure SFTP credentials.The recipient clicks the link in the email received. ***The link contained in the email is only active for 72 hours.***   
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203202873/37c37457b00c1bee40781ceb7400/SFTP-Email.png?expires=1784333700&signature=b6dfe0027be26c7735f39968503b1ecc839534eeec48a987609a3ff887f276a7&req=dSInFct%2Bn4lYWvMW1HO4zX2PBUbwV4FGo9AHrXER%2Fl3%2F%2F%2FTmZfUqmarnydAk%0AZRLL%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1203202873/37c37457b00c1bee40781ceb7400/SFTP-Email.png?expires=1784333700&signature=b6dfe0027be26c7735f39968503b1ecc839534eeec48a987609a3ff887f276a7&req=dSInFct%2Bn4lYWvMW1HO4zX2PBUbwV4FGo9AHrXER%2Fl3%2F%2F%2FTmZfUqmarnydAk%0AZRLL%0A)
2. A webpage will open, and the recipient can request a Verification Code, which is sent to their email address. When the code is entered, we'll share the SFPT config on-screen, including the password.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1211712015/c8612e5862702eb486db92a5e0f4/SFTP-EmailCode.png?expires=1784333700&signature=685ae771b99a013ffbd3228ea7bdc2ad5f6f3078e27c4cd1de34f414a1d22098&req=dSImF85%2Fn4FeXPMW1HO4zWwEMJCZlndOKI81oX%2FSbe%2F1e6B7dxqo5EnkqDcB%0ARKLp%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1211712015/c8612e5862702eb486db92a5e0f4/SFTP-EmailCode.png?expires=1784333700&signature=685ae771b99a013ffbd3228ea7bdc2ad5f6f3078e27c4cd1de34f414a1d22098&req=dSImF85%2Fn4FeXPMW1HO4zWwEMJCZlndOKI81oX%2FSbe%2F1e6B7dxqo5EnkqDcB%0ARKLp%0A)

   ​

---