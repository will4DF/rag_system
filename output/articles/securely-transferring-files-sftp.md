---
title: Securely Transferring Files (SFTP)
url: https://help.element451.com/en/articles/9146573-securely-transferring-files-sftp
collection: Data Management
---

# Overview

This article explains SFTP and FileZilla, walks you through connecting to FileZilla and shows how to use Data Connectors in Element451 to complete the setup.

## **What is SFTP?**

SFTP (Secure File Transfer Protocol) securely transfers sensitive files over an encrypted network (SSH). Unlike FTP or other file transfer methods, SFTP protects your data from vulnerabilities by encrypting the transfer.

## **What is FileZilla?**

**FileZilla** is a free and open-source **FTP (File Transfer Protocol) client** that allows users to transfer files between their local computer and a remote server. It supports FTP, **SFTP (Secure File Transfer Protocol)**, and **FTPS (FTP Secure)**, providing flexibility and security for users who need to manage files on remote servers. FileZilla is widely used by web developers, IT professionals, and anyone who needs to upload, download, or edit files on a server.  
​  
You can use FileZilla to access your Element451 provided SFTP site or other SFTP site you may have data delivered to.   
​  
FileZilla is only one client you might opt to use. There are many options that can interface with Element451.

---

# Setting up SFTP

## Step 1: Install + Set Up FileZilla

1. Start by installing [FileZilla](https://filezilla-project.org/).

   * Select the gray box labeled **Download FileZilla Client – All Platforms** and download the correct version for your operating system.
2. Run the installer, skipping any additional software offers.
3. Once installed, open FileZilla.
4. In the top menu, go to **File** and click **Site Manager**.
5. Click **New Site** to create a new connection. A settings box will appear.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1218439247/c6078d048c11bfa240e00530103d/Connecting%2Bto%2BSFTP%2B1.gif?expires=1784333700&signature=df516757d3dca3ac94b7f51a6ca3321ff8e2564d717ab4a2777e0ebf8d95cf6b&req=dSImHs19lINbXvMW1HO4zdMAgmzhUNJgWu5M1UwhViop5nyhLqQjNY7FRZ4V%0A9RZ%2B%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1218439247/c6078d048c11bfa240e00530103d/Connecting%2Bto%2BSFTP%2B1.gif?expires=1784333700&signature=df516757d3dca3ac94b7f51a6ca3321ff8e2564d717ab4a2777e0ebf8d95cf6b&req=dSImHs19lINbXvMW1HO4zdMAgmzhUNJgWu5M1UwhViop5nyhLqQjNY7FRZ4V%0A9RZ%2B%0A)
6. From the **Protocol** dropdown, choose **SFTP – SSH File Transfer Protocol**.
7. Next, you'll need to generate your login details.

   * Login details are created by adding a new SFTP account in SFTP Management (General Settings > SFTP Management). Click [here](https://help.element451.com/en/articles/9953382-sftp-management#h_389f980aa0) to review our help article on creating a new account to generate your login details.
8. Add the login details you created in step 7 and click **Connect**.
9. If you see an **Unknown Host Key** prompt, this is normal. It’s a **Trust on First Use** behavior. Check the box to "Always trust this host; add this key to the cache."
10. Once connected, you’ll see a success message in the status dialog box. Your new directory folder will appear in the **Remote Sites** panel (middle right). This is where you will upload files for secure transfers.
11. Now, log in to Element451 and continue with the steps below.

##

---

# Using an RSA Key Pair

While a username and password are the most common methods for SFTP connections, Element451 also supports RSA key pairs.

For an Element451 SFTP server connection using an RSA key pair, you have two options:

1. Generate your own key pair and provide us with the public key.
2. We can generate the key pair for you and provide the private key.

Instead of entering a password, you’ll copy the text from the private key into the **Private Key** field.

## Generating Your Own RSA Key Pair

To generate your own RSA key pair:

1. Use a terminal command like the one below, depending on your operating system:

   ```
   ssh-keygen -t rsa -m pem
   ```
2. You’ll be prompted to enter a file name or location.
3. Then, you’ll be asked twice to enter a passphrase. Leave this blank, as Element451 does not currently support passphrase-protected keys.
4. Press **Enter** again, and your key pair will be generated. It should look similar to the screenshot provided below:

[![](https://downloads.intercomcdn.com/i/o/618853984/1c248c68f99097549d7e21c0/Screen+Shot+2022-11-17+at+2.49.01+PM.png?expires=1784333700&signature=2a20ff74c62f64dfff00a146cc78cb54b75178752cbbb7739d98c1cda03dc6f8&req=ciEvHsx9lIlbFb4f3HP0gETXEdPvddeh%2B38vmF1muehjrpF1oqquIloN%2BfeZ%0A%2F2pyqHST%2B49bt6ahuw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/618853984/1c248c68f99097549d7e21c0/Screen+Shot+2022-11-17+at+2.49.01+PM.png?expires=1784333700&signature=2a20ff74c62f64dfff00a146cc78cb54b75178752cbbb7739d98c1cda03dc6f8&req=ciEvHsx9lIlbFb4f3HP0gETXEdPvddeh%2B38vmF1muehjrpF1oqquIloN%2BfeZ%0A%2F2pyqHST%2B49bt6ahuw%3D%3D%0A)

---

# SFTP Management (Self-Service)

Element451 has a self-service tool that allows you to create and manage access to your SFTP accounts. It gives you the flexibility to control access to your accounts securely and efficiently, all from within your General Settings.

[Explore More: SFTP Management →](https://help.element451.com/en/articles/9953382-sftp-management)

---

# Notes When Using Other FTP Clients

* **DMZ File Transfer**

  + Getting a directory connection error when connecting to Element451? Try using the "Blind Download" option to skip directory listing.

---