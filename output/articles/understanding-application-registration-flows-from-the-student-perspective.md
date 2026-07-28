---
title: Understanding Application Registration Flows from the Student Perspective
url: https://help.element451.com/en/articles/9264459-understanding-application-registration-flows-from-the-student-perspective
collection: Applications
---

Learn about the different application registration flows for students with and without Element451 records.

# Overview

This article serves as a guide to the application registration process in Element451 from the student's viewpoint. It outlines three main scenarios: one for students without a record, another for those with a record but no password set, and a third for those with an existing account and password.

For more details on configuring your application registration form, refer to our [Creating + Managing Applications](https://help.element451.com/en/articles/9040630-creating-managing-applications#h_caf4aecfdf) help article.

---

# Step-by-Step: Application Registration Form

1. The student accesses your **Application** **Site**.
2. They click **Start** **Application** and select the relevant application.
3. The **registration** **form** for that specific application opens.
4. The student completes the form fields.
5. They click **Create** **Account**.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1038477266/bf3a8974ca7950ed59c306d9/apps+-+register+form.gif?expires=1784333700&signature=88f9904ac21d9d66d07859ee3e34cb47512b8a1c804014c0711df01464794b69&req=dSAkHs15moNZX%2FMW1HO4zbAHgrH9MQzhS3Zy9sjmg2oyJguauMeE%2FmIq59Z0%0ArKyt%0A)](https://downloads.intercomcdn.com/i/o/1038477266/bf3a8974ca7950ed59c306d9/apps+-+register+form.gif?expires=1784333700&signature=88f9904ac21d9d66d07859ee3e34cb47512b8a1c804014c0711df01464794b69&req=dSAkHs15moNZX%2FMW1HO4zbAHgrH9MQzhS3Zy9sjmg2oyJguauMeE%2FmIq59Z0%0ArKyt%0A)
6. Element451 then checks if the email address is associated with an existing record in your Element451 instance. Below, we'll outline what happens next in each scenario:  
   ​

   * [Scenario 1](#h_03d1717f7f): No email match/no record exists
   * [Scenario 2](#h_c9c1cb0c75): Email was found; student does not have password set
   * [Scenario 3](#h_e2bbd309ff): Email was found; student has a password set

💡 **Already have an account?** The registration form is titled **"First, create your account"** and includes a sign-in prompt — *"Already have an account? Log in instead"* — that directs returning applicants to log in rather than create a duplicate account.

---

# Scenario 1: Students Without a Record in Element451

Students without a record simply complete the registration form for the desired application, enabling them to create a password and proceed with their application.

* After clicking **Create** **Account**, the student is redirected to the application dashboard to begin completing the application.

---

# Scenario 2: Students With a Record in Element451 & No Password Set

Students may unknowingly fall into this scenario, particularly when records are generated through various means such as data imports, form completions, event registrations, or appointments. Since they haven't completed the application registration process, they might not be aware of their existing record in Element451. In such cases, the system initiates an email verification step to confirm their identity before proceeding with the application. This verification process ensures security and clarity, preventing confusion associated with password resets when no password has been set.

1. **Email Verification Triggered:** If the email is found but no password is set, the system will automatically prompt an email verification step. The system sends an email to the student's email address with a verification code. This step is crucial for confirming the student's identity and preventing unauthorized access. This cannot be disabled.

   [![](https://downloads.intercomcdn.com/i/o/1037343277/253468b39bd84a0af8b43451/App+Reg+Flow+Screenshot+Modal.png?expires=1784333700&signature=2794bb6f2df597c0d4f764ad48e66f47a13c708de45e0390b7e3abc98c1551e5&req=dSAkEcp6noNYXvMW1HO4zXuS4VN8Rr%2BzxZOOLSPxoD%2B2AIJ8cASFkktVW971%0A%2FiJH%0A)](https://downloads.intercomcdn.com/i/o/1037343277/253468b39bd84a0af8b43451/App+Reg+Flow+Screenshot+Modal.png?expires=1784333700&signature=2794bb6f2df597c0d4f764ad48e66f47a13c708de45e0390b7e3abc98c1551e5&req=dSAkEcp6noNYXvMW1HO4zXuS4VN8Rr%2BzxZOOLSPxoD%2B2AIJ8cASFkktVW971%0A%2FiJH%0A)
2. **Verification Code Entry:** To proceed, the student needs to retrieve this code from their email. Once they have the code, they should return to the application portal and enter it to complete the verification process.

   [![](https://downloads.intercomcdn.com/i/o/1037349998/223d5a667ffbc96f11cfde8c/App+Reg+Flow+-+Verification+Email.png?expires=1784333700&signature=392a9320eb937ecfafc9eea71dd4da23f32f1f5a8e3bb4aca11d500f3d141c6e&req=dSAkEcp6lIhWUfMW1HO4zTPqrkRY%2F5vJKuhAkH0Kh%2F9Ezb1RURR6MAfViKrM%0AZATG%0A)](https://downloads.intercomcdn.com/i/o/1037349998/223d5a667ffbc96f11cfde8c/App+Reg+Flow+-+Verification+Email.png?expires=1784333700&signature=392a9320eb937ecfafc9eea71dd4da23f32f1f5a8e3bb4aca11d500f3d141c6e&req=dSAkEcp6lIhWUfMW1HO4zTPqrkRY%2F5vJKuhAkH0Kh%2F9Ezb1RURR6MAfViKrM%0AZATG%0A)
3. After confirming their identity, they are seamlessly redirected to the application site to begin their application.

💡 **Imported applicants without a password:** If an imported applicant (for example, a student brought in through Common App) later returns and tries to **log in** with their email, they'll now be guided to set a password. After they enter an email that has no password on file, a **"Check Your Email"** message appears and Element451 emails them a secure link to create a password for future logins, with no staff password reset required.

---

# Scenario 3: Students With a Record in Element451 (Has Account + Password)

In this situation, Element451 identifies a pre-existing record associated with the same email address, where a password has been set, indicating the creation of an account in the past. Consequently, we present the student with a message informing them of the existing profile. They are then presented with three choices:

* **Back to registration**: Allows them to adjust their information
* **Go to login page**: Allows them to log in using their password
* **Reset your password:** Allows them to reset their password

  + 🚨 **Important:** For a student to receive the password reset email, the **[User Password Reset Request](https://help.element451.com/en/articles/9062223-application-settings#h_b95910375e)** autoresponder message must be active in your application settings (**Applications** > **Applications** > **Application** **Settings**).  
    ​

  [![](https://downloads.intercomcdn.com/i/o/1038496096/a3a6df878e499050b3b3d422/App+reg+form+-+existing+account.png?expires=1784333700&signature=1e9c646474c249df871552cb815839acc8b95cfc7b7d99c943112eb13d844768&req=dSAkHs13m4FWX%2FMW1HO4zdpWVErIJqpzi43UjywPXLbCrvwYIFJoYXcJ4iyn%0ATxTG%0A)](https://downloads.intercomcdn.com/i/o/1038496096/a3a6df878e499050b3b3d422/App+reg+form+-+existing+account.png?expires=1784333700&signature=1e9c646474c249df871552cb815839acc8b95cfc7b7d99c943112eb13d844768&req=dSAkHs13m4FWX%2FMW1HO4zdpWVErIJqpzi43UjywPXLbCrvwYIFJoYXcJ4iyn%0ATxTG%0A)

To reduce duplicate accounts, the registration form proactively encourages applicants who already have an account to **log in instead** of re-registering, before they reach this message.

---

# Returning Applicants: Your Application Dashboard

When a returning applicant signs in, the dashboard leads with a **"Your applications are waiting"** heading and surfaces their existing in-progress and submitted applications as prominent cards. Each card displays:

* The **application name**
* The **term and major**
* When the applicant **last logged in**
* The current **status** (a status pill or completion percentage)
* A dedicated **Open** button to return to that application

The **Start New Application** button remains available for starting an additional application, while existing applications take visual priority — reducing the chance that an applicant starts a duplicate.

---

# Starting a New Application While Signed In

When a signed-in applicant starts a new application, the modal title displays the **name of the selected application** rather than a generic label.

Because identity fields (name, date of birth) are pre-filled and locked to the account, a message appears at the top of the modal:

*"You are currently signed in as [Preferred or First Name] [Last Name] ([email]). Need to continue for another person? **Log out** and sign in or create a new account using a different email address."*

The **Log out** link ends the current session so a different person can register under their own email address.

---

# Locked Name Fields After Account Creation

To protect identity data, **name fields are locked once an account exists**. On the application, locked name fields display helper text: *"🔒 Name locked to your account. Edit to make a correction."*

Selecting **Edit** opens an **"Update your name?"** modal — with First Name, Middle Name, Last Name, and Preferred Name fields — that updates the name associated with the account. The modal also notes: *"Need to continue for someone else? Log out and create a new account."*

Email addresses are not locked; an applicant can change their email as long as it isn't already associated with another record.

---