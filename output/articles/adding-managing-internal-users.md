---
title: Adding + Managing Internal Users
url: https://help.element451.com/en/articles/2735199-adding-managing-internal-users
collection: Settings + Permissions
---

Explore how to manage internal user accounts (add, delete, deactivate), adjust permissions and visibility, and change passwords.

# Overview

In Settings, **Manage Users** is your hub for adding, editing, and viewing all internal user accounts. It's also where you adjust permission and visibility settings for groups. This guide will walk you through navigating the **Users** section of the Manage Users page and provide links to articles about the other sections.

In Element451 documentation, we refer to you and your colleagues as "internal users." To add or manage internal users, you'll need the **Administer** **Internal** **Users** permission.

🚨 **Important:** Before you add internal users, you must understand the functions of [permission groups](https://help.element451.com/en/articles/2735389-permission-groups-overview) and [visibility groups](https://help.element451.com/en/articles/5214533-visibility-groups).

## Accessing Internal Users

From your profile picture/avatar in the top right corner, navigate to **Settings** > **Manage** **Users**.

[![](https://downloads.intercomcdn.com/i/o/1043263398/35caf3af32800535f1263b0e/Settings+-+Manage+Users.gif?expires=1784333700&signature=8cc58b266910422a699b52fe0521d1aa0ff56c75ec1c07296fd7a4d073e320a8&req=dSAjFct4noJWUfMW1HO4zdit6uSWgjZDneEkt4P%2BGCvpYqSUKrE9cwCQRmfm%0ALZ7A5XirMv0NeMft4I4%3D%0A)](https://downloads.intercomcdn.com/i/o/1043263398/35caf3af32800535f1263b0e/Settings+-+Manage+Users.gif?expires=1784333700&signature=8cc58b266910422a699b52fe0521d1aa0ff56c75ec1c07296fd7a4d073e320a8&req=dSAjFct4noJWUfMW1HO4zdit6uSWgjZDneEkt4P%2BGCvpYqSUKrE9cwCQRmfm%0ALZ7A5XirMv0NeMft4I4%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1046346456/1a8384898d037a6ce393f9af/Settings+-+Manage+Users+-+Users.png?expires=1784333700&signature=af8618ae36d6d00cc3636b25bd4095a565ec96c165d46de1fec1958a999f2cb5&req=dSAjEMp6m4VaX%2FMW1HO4zVaQCLLGzmyDPnnz3%2BallHVJCw85Q%2BxolRUEVWJT%0AJ91ImWDmRU1RYT5sU50%3D%0A)](https://downloads.intercomcdn.com/i/o/1046346456/1a8384898d037a6ce393f9af/Settings+-+Manage+Users+-+Users.png?expires=1784333700&signature=af8618ae36d6d00cc3636b25bd4095a565ec96c165d46de1fec1958a999f2cb5&req=dSAjEMp6m4VaX%2FMW1HO4zVaQCLLGzmyDPnnz3%2BallHVJCw85Q%2BxolRUEVWJT%0AJ91ImWDmRU1RYT5sU50%3D%0A)

---

# Adding an Internal User

## Step-by-Step Guide

1. Click the **+ New User** button ![](https://downloads.intercomcdn.com/i/o/1044325766/ab0938a52703582ab0eb9ab0/%2B+new+user+button.png?expires=1784430000&signature=35405ae237fdbe2801025ac85864f3118a6d15cb1c24e85ce826dbf8657f30d7&req=dSAjEsp8mIZZX%2FMW3Hu4gQOeXOxvYm%2Ft8s%2BAaufz8BPwKDSTAiY2jG5OYwfP%0AVw%3D%3D%0A) in the top right corner. The new user form will open for you to complete.
2. Select whether you want to add the user **manually** or by **invitation**.   
   ​**Note**: If you don't have the option to select a method to add a user, it's likely because you exclusively use SSO. This is expected behavior, and you can proceed with the steps below.

   * **Manually:** You enter all user details, including name, title, and primary team. You also create a password for the user or allow the system to generate one automatically. Once the user is created, you can copy the password or email it directly to the user.
   * **By Invitation:** The user will be emailed a link to fill in their information, including setting their password.
3. **Email** **Address**: Add the user's email address. This is the email address they will use to log into Element451.

   * If you use SSO for internal user authentication, ensure the email used to create the Element451 account matches the SSO email.
4. **Preferred** **Start** **Page**: Select the user's preferred start page. The preferred start page is the module the user will be automatically redirected to when signing into Element451. Customize it to match their workflow and prioritize the feature that matters most to them. By default, it will be set to the Start page.
5. **Primary Team**: Each user in Element451 must have an assigned [team](https://help.element451.com/en/articles/8346250-teams). Typically, this would be the user's functional department. A user can be a member of as many teams as needed, but they can only have one Primary Team.
6. If you are **manually** adding the user, you will also need to provide the following information:

   * **Title**
   * **First** **Name**
   * **Middle Name** (optional)
   * **Last Name**
   * **Phone Number** (optional; used for )StudentHub Network
   * **Office Building** (optional; used for )StudentHub Network
   * **Office Room** (optional; used for )StudentHub Network
   * **Allow Direct Messages from Network Connections**: When enabled, Network Connections can start private messenger chats in Conversations, automatically assigning them to you. If disabled, conversations must be assigned manually or via rules.
7. Password Options:

   * If **manually** adding a user, you will have two options:

     + **Automatically Generate Password**: Select if you want the password automatically generated. If not, you will be required to add a password.
     + **Ask for Password Change at Next Sign-In**: This will require the user to change their password upon logging in for the first time.
   * If you are using the "invite" method or using SSO **exclusively** for your internal users, you will not see any password options. If you use both SSO **and** Password, be sure to select “yes” for “Automatically generate password” and “no” for “Ask for password change at next sign-in.”
8. **Permissions** **Groups**: Add the user to your chosen permission group(s).  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1045226386/ca9ef79ee21024026d18b002/Settings+-+New+User+-+Perm+Groups.png?expires=1784333700&signature=2fdc97ddc3394fb7fc38e093bb929ae551305786e04934080bdce6e58e26c630&req=dSAjE8t8m4JXX%2FMW1HO4zec56IQ1CBgY%2FkONDcUv1GUr56ZRChTv%2BzweoWHQ%0ApRZQ%0A)](https://downloads.intercomcdn.com/i/o/1045226386/ca9ef79ee21024026d18b002/Settings+-+New+User+-+Perm+Groups.png?expires=1784333700&signature=2fdc97ddc3394fb7fc38e093bb929ae551305786e04934080bdce6e58e26c630&req=dSAjE8t8m4JXX%2FMW1HO4zec56IQ1CBgY%2FkONDcUv1GUr56ZRChTv%2BzweoWHQ%0ApRZQ%0A)
9. **Visibility** **Groups**: Add the user to your chosen visibility group(s). If no visibility groups are chosen, the user will have complete visibility.   
   ​

   [![](https://downloads.intercomcdn.com/i/o/1045226647/121f69da732bcd3b564b2fc5/Settings+-+Add+User+-+Visibility+Groups.png?expires=1784333700&signature=de58245b852dd76d695633113e038789ed9fa10a527018f0fb892bbf4a196b90&req=dSAjE8t8m4dbXvMW1HO4zUEi51QX3vlSaUkF0VnBtJpljNl5FZSHJGkaOMGa%0AZB0q%0A)](https://downloads.intercomcdn.com/i/o/1045226647/121f69da732bcd3b564b2fc5/Settings+-+Add+User+-+Visibility+Groups.png?expires=1784333700&signature=de58245b852dd76d695633113e038789ed9fa10a527018f0fb892bbf4a196b90&req=dSAjE8t8m4dbXvMW1HO4zUEi51QX3vlSaUkF0VnBtJpljNl5FZSHJGkaOMGa%0AZB0q%0A)
10. When finished, click **Save** ![](https://downloads.intercomcdn.com/i/o/1045252268/2d1b11f42755961d054ea138/Save+Button.png?expires=1784430000&signature=3d87b6b3016a896b27b5965f7927a187be74d3a3de3d641ae005615a135d6fef&req=dSAjE8t7n4NZUfMW3Hu4gVTOlbh7WTfctL4eAe89rxxDroWFFzuG%2BWU7ikXM%0Afg%3D%3D%0A) in the top right corner.

    * When you **invite** the user, an email containing a link will be sent to their email address. They will then be prompted to create a password and enter their name, primary team, and title.

      [![](https://downloads.intercomcdn.com/i/o/1045256512/6f031ebe9ddcac562777189c/Screenshot+2024-05-08+at+10_47_09%E2%80%AFAM.png?expires=1784333700&signature=892924fa0106abab3fd1b03dc113547b19cad534574acad1ad7405089c4b102d&req=dSAjE8t7m4ReW%2FMW1HO4zTHaYk5cwSVIdZjxkKNi%2FtuKb%2FkNJ%2FSFz6c1Eq99%0A3YTk%0A)](https://downloads.intercomcdn.com/i/o/1045256512/6f031ebe9ddcac562777189c/Screenshot+2024-05-08+at+10_47_09%E2%80%AFAM.png?expires=1784333700&signature=892924fa0106abab3fd1b03dc113547b19cad534574acad1ad7405089c4b102d&req=dSAjE8t7m4ReW%2FMW1HO4zTHaYk5cwSVIdZjxkKNi%2FtuKb%2FkNJ%2FSFz6c1Eq99%0A3YTk%0A)
    * When you **manually** **add** a user:

      + You receive a confirmation notification that the user has been created.
      + To notify the new user that an account has been created, click the **Email Login Info** button. ![](https://downloads.intercomcdn.com/i/o/1088127814/0f49e11705c142faef8722f3/Note-Orng.png?expires=1784430000&signature=ec29c94be34e8df270aa7dd7ab85be55707a0a4c1da10a9e59a939157c058ff7&req=dSAvHsh8moleXfMW3Hu4gb3Tza7ZHaxi3AJIL8mFylTllWJARbFBXnhWcuMj%0AWA%3D%3D%0A) For security reasons, this email **does not contain the password**. It only contains the URL to the login page of your instance.

        - To share the password, you need to copy it using the "Click to Copy Password" button and then share it privately with the user.

          [![](https://downloads.intercomcdn.com/i/o/1045261141/056f9e151f2e6ee0695f25ae/Settings+-+Add+User+-+Copy+Password.png?expires=1784333700&signature=1e40294813667cb3569998eff67691dba915ddef931ca960003897bcdc138ce7&req=dSAjE8t4nIBbWPMW1HO4zQLvw5MkD%2BwGbUQJeICPb%2F2ohjfVrN0v9wgygzKP%0AG4IX%0A)](https://downloads.intercomcdn.com/i/o/1045261141/056f9e151f2e6ee0695f25ae/Settings+-+Add+User+-+Copy+Password.png?expires=1784333700&signature=1e40294813667cb3569998eff67691dba915ddef931ca960003897bcdc138ce7&req=dSAjE8t4nIBbWPMW1HO4zQLvw5MkD%2BwGbUQJeICPb%2F2ohjfVrN0v9wgygzKP%0AG4IX%0A)

## Adding Users with SSO

If you use SSO for internal user authentication, add users following the same process described while keeping in mind these important notes:

* Ensure the email used to create the Element451 account matches the SSO email.
* If you exclusively use SSO for internal users, the system defaults to the "manual" method of adding a user, and therefore, you should not have the option to select "manual" or "invite" at the beginning of the process.
* If you use SSO **AND** Password as login options, select “yes” for “Automatically generate password” and “no” for “Ask for password change at next sign-in.” For more information on authentication settings, [click here](https://help.element451.com/en/articles/8569773-security-authentication-settings).

[![](https://downloads.intercomcdn.com/i/o/1057431874/8cbfa89414cf7f1bb81d5e57/+Managing+Users+-+SSO.png?expires=1784333700&signature=ae07cd758680d143d585ba76bc8ae319e18bfd59d55fdde5636593508e65bee5&req=dSAiEc19nIlYXfMW1HO4zbOHyOj3ghuwxlcU69KJgrFYUT7q2npTS7UkAxzy%0AvTsHF9ATW17w%2Bp7e42c%3D%0A)](https://downloads.intercomcdn.com/i/o/1057431874/8cbfa89414cf7f1bb81d5e57/+Managing+Users+-+SSO.png?expires=1784333700&signature=ae07cd758680d143d585ba76bc8ae319e18bfd59d55fdde5636593508e65bee5&req=dSAiEc19nIlYXfMW1HO4zbOHyOj3ghuwxlcU69KJgrFYUT7q2npTS7UkAxzy%0AvTsHF9ATW17w%2Bp7e42c%3D%0A)

---

# Viewing + Editing an Internal User

Internal user accounts can be easily viewed or edited after they have been created. This will allow you to change their information, password, or permission and visibility groups. Additionally, you can see their milestones, like when they were last seen and any activity made by them performed in Element451.

1. Click on your profile picture/avatar in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Manage** **Users**. The Users section from the lefthand menu opens by default.
3. Locate the user you wish to view or edit.
4. You can either click on **their name** or click the **three** **vertical** **dots** at the end of the row, followed by the **Edit** button. Both methods will open the user's overview.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1046353106/bd0e414c5560be5e084f2fe1/Settings+-+Manage+Users+-+Users+-+Edit+User.png?expires=1784333700&signature=b2529c43b45d192d5b44fdfe1c7fbe96726b79d492f15daff38903444259bbdb&req=dSAjEMp7noBfX%2FMW1HO4zYkHwEHI9xWyTUStrUMDBLZji7bSWW7Fy0HnH8nN%0AJc3b%0A)](https://downloads.intercomcdn.com/i/o/1046353106/bd0e414c5560be5e084f2fe1/Settings+-+Manage+Users+-+Users+-+Edit+User.png?expires=1784333700&signature=b2529c43b45d192d5b44fdfe1c7fbe96726b79d492f15daff38903444259bbdb&req=dSAjEMp7noBfX%2FMW1HO4zYkHwEHI9xWyTUStrUMDBLZji7bSWW7Fy0HnH8nN%0AJc3b%0A)

[Explore More on Internal User Profiles](https://help.element451.com/en/articles/14727910-managing-internal-user-profiles)

---

# Deleting + Deactivating Internal Users

In Element451, you can delete or deactivate internal users. We recommend deactivation, especially for users with an activity history. Deactivation retains their records, ensuring you won’t see “[deleted user]” in activity logs. This helps with better record retention and tracking.

## Step-by-Step Guide

1. Click on your profile picture/avatar in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Manage** **Users**. The Users section from the lefthand menu opens by default.
3. Locate the user you wish to manage.
4. You can either click on **their name** or click the **three** **vertical** **dots** at the end of the row, followed by the **Edit** button. Both methods will open the user's overview.
5. In the header, click the **silhouette and gear** ![](https://downloads.intercomcdn.com/i/o/1046541187/d157e5946d8e3903dd62a477/silhouette+and+gear+icon.png?expires=1784430000&signature=c4f482815c314cc6a0b1306ac491999587a72b2c48f4c3b9729f8f67796e4e07&req=dSAjEMx6nIBXXvMW3Hu4gWTXjWrB7Slj0QMJ3RlhQPJ0JSOfhUwo1Je12lsq%0ATg%3D%3D%0A) icon.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1046538515/4dd5c55c074e67532f5c78c2/Settings+-+Manage+Users+-+Delete+and+Deactivate+User.png?expires=1784333700&signature=0d3de3d5f17f5b972bc571e3ea2b5d4ee61952f4dd1287c7e8d508bba5e655e6&req=dSAjEMx9lYReXPMW1HO4zQUt2O5CRQVIMwGvI85Xhd6matFZ5w39LdrS7GkX%0ASZid%0A)](https://downloads.intercomcdn.com/i/o/1046538515/4dd5c55c074e67532f5c78c2/Settings+-+Manage+Users+-+Delete+and+Deactivate+User.png?expires=1784333700&signature=0d3de3d5f17f5b972bc571e3ea2b5d4ee61952f4dd1287c7e8d508bba5e655e6&req=dSAjEMx9lYReXPMW1HO4zQUt2O5CRQVIMwGvI85Xhd6matFZ5w39LdrS7GkX%0ASZid%0A)
6. From the menu, select whether you want to **deactivate** or **delete** the user.
7. You will be asked to confirm either option.

---

# Changing + Resetting Internal User Passwords

If you use the password option for internal authentication, you can change a user’s password or email them a reset link. For more information on authentication settings, [click here](https://help.element451.com/en/articles/8569773-security-authentication-settings).

## Step-by-Step Guide

1. Click on your profile picture/avatar in the top right corner of the orange navigation menu.
2. Navigate to **Settings** > **Manage** **Users**. The Users section from the left-hand menu opens by default.
3. Locate the user you wish to manage.
4. You can either click on **their name** or click the **three** **vertical** **dots** at the end of the row, followed by the **Edit** button. Both methods will open the user's overview.
5. In the Profile tab (which opens by default), under Basic Information, you'll see two blue buttons:

   * **Change Password**: Manually change the user's password.
   * **Send Reset Password Link**: Email the user a link to reset their password.

   ---

---

# Next Up

Once you feel confident adding users, check out [Managing Internal User Profiles](https://help.element451.com/en/articles/14727910-managing-internal-user-profiles) for a deep dive into everything available on a user's profile page—including how to review their activity, configure visibility groups, and set up access restrictions.

---