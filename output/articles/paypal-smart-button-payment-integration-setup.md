---
title: Paypal Smart Button Payment Integration Setup
url: https://help.element451.com/en/articles/9083465-paypal-smart-button-payment-integration-setup
collection: Settings + Permissions
---

# Overview

This process is exactly the same for creating Sandbox and Live applications.  
It is recommended to use meaningful names for the Application so later they are not confused with other Applications.

First, you'll need to get setup in Paypal (explained below in this article) and then use the credentials created there to configure the payment gateway in Element451 (explained in the *[Getting Started with Payments + How to Add and Connect Payment Providers](https://help.element451.com/en/articles/3136121-getting-started-with-payments-how-to-add-and-connect-payment-providers)* article).

---

# How to Get Paypal Client ID and Secret Key

## Requirements

The only requirement is to have a PayPal account; if you don’t have one, create one first.

## Steps-by-Step Process

1. Navigate to the Paypal website: [https://www.paypal.com](https://www.paypal.com/us/home)
2. Navigate to the Login screen by clicking on any “**Log In**” button.
3. Entering your credentials will get you into the Dashboard.
4. Click on your profile name/photo, on the right side top corner.
5. From the dropdown menu click on “**Account Settings.**”  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028311647/96b6dea3de2010155f5b3e18ee61/Step5.png?expires=1784333700&signature=e4fe9310d94849bcf3a8e387df5a50625b22d6b9d2efeee225b20280e5bd9369&req=diAlHsp%2FnIdbXvMW1HO4zRzFA8REbqv48MzfWcRBAgU7I%2FKIgLtx5WANMjqG%0At785%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028311647/96b6dea3de2010155f5b3e18ee61/Step5.png?expires=1784333700&signature=e4fe9310d94849bcf3a8e387df5a50625b22d6b9d2efeee225b20280e5bd9369&req=diAlHsp%2FnIdbXvMW1HO4zRzFA8REbqv48MzfWcRBAgU7I%2FKIgLtx5WANMjqG%0At785%0A)
6. On the new screen, on the tab “Account access,” click “**Update**” on the item “API access.”  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028311930/ef9dadd47fcd1690cd7c0a624682/Step6.png?expires=1784333700&signature=cce7f964661342c5d460ac4983fda52aaa087770f06f8ef321fd6267a4527ec4&req=diAlHsp%2FnIhcWfMW1HO4zR8LG1zMrlkuFf9lSj%2BJSllNnXCNSyv3P6RCnlwV%0AeRLF%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028311930/ef9dadd47fcd1690cd7c0a624682/Step6.png?expires=1784333700&signature=cce7f964661342c5d460ac4983fda52aaa087770f06f8ef321fd6267a4527ec4&req=diAlHsp%2FnIhcWfMW1HO4zR8LG1zMrlkuFf9lSj%2BJSllNnXCNSyv3P6RCnlwV%0AeRLF%0A)
7. On the new screen, on the question “How is Paypal set up on your website?,” click “**Manage REST API apps and credentials**” under the “REST API Integration” option.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028312465/0f2116dcf2249587e1f852b69c3c/Step7.png?expires=1784333700&signature=f7215721ff88a1e3b0ffc2601df1f3bd53ed726687113a402655077557885c12&req=diAlHsp%2Fn4VZXPMW1HO4zTs89hVnqGC51ExPUjrRYcSz0cKoM3Zs9JbIFwXY%0A%2BW%2FW%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028312465/0f2116dcf2249587e1f852b69c3c/Step7.png?expires=1784333700&signature=f7215721ff88a1e3b0ffc2601df1f3bd53ed726687113a402655077557885c12&req=diAlHsp%2Fn4VZXPMW1HO4zTs89hVnqGC51ExPUjrRYcSz0cKoM3Zs9JbIFwXY%0A%2BW%2FW%0A)
8. On the new screen, click on “**Paypal Developer experience.**” This will take you to the Paypal Developer Dashboard where you can manage your integrations.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028312750/ff75c46d15b97bf3b4ad27796668/Step8.png?expires=1784333700&signature=148e39b902c613cd9e2b44d0d5b101ff9499f9bb5b8c531777a6a292d2509f78&req=diAlHsp%2Fn4ZaWfMW1HO4za2QZKOdMwPyCUBjlZ0KlgOpjScxNOgsbj6CnqsQ%0A00j5%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028312750/ff75c46d15b97bf3b4ad27796668/Step8.png?expires=1784333700&signature=148e39b902c613cd9e2b44d0d5b101ff9499f9bb5b8c531777a6a292d2509f78&req=diAlHsp%2Fn4ZaWfMW1HO4za2QZKOdMwPyCUBjlZ0KlgOpjScxNOgsbj6CnqsQ%0A00j5%0A)
9. On the Developer Dashboard, under the “My Apps & Credentials” tab, you can see existing Sandbox and Live applications, or create new ones. Let’s create a Sandbox one to test the integration.  
   ​  
   Click “**Sandbox**” and then click “**Create App.**”  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028312948/6bfd5e771a664099dc25360b49d1/Step9.png?expires=1784333700&signature=42febd22cf58a8db5d088db3128381423543290d6870cf76edaf00925701c9da&req=diAlHsp%2Fn4hbUfMW1HO4zRrerOh2sPUqrLw0YyyXT0j5Q9t7aimV0yZrt6cl%0AtLlK%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028312948/6bfd5e771a664099dc25360b49d1/Step9.png?expires=1784333700&signature=42febd22cf58a8db5d088db3128381423543290d6870cf76edaf00925701c9da&req=diAlHsp%2Fn4hbUfMW1HO4zRrerOh2sPUqrLw0YyyXT0j5Q9t7aimV0yZrt6cl%0AtLlK%0A)
10. On the creation screen, add a meaningful “App Name,” perhaps “Element451—Sandbox” for the sandbox App and “Element451—Live” for the Live App; choose “Merchant” as the “App Type” and select the default “Sandbox Business Account,” then click “Create App.”  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313160/bd22f54f699c76eb0505cb7c3d83/Step10.png?expires=1784333700&signature=65337eff1de364d34a32593366776f48b2de5ff6cf021f9d51e9ba58197aa146&req=diAlHsp%2FnoBZWfMW1HO4zVa5p7mNdOhV9z7aslhe%2BTbWLU4Wutpk5K%2BMVvTb%0ANwfU%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313160/bd22f54f699c76eb0505cb7c3d83/Step10.png?expires=1784333700&signature=65337eff1de364d34a32593366776f48b2de5ff6cf021f9d51e9ba58197aa146&req=diAlHsp%2FnoBZWfMW1HO4zVa5p7mNdOhV9z7aslhe%2BTbWLU4Wutpk5K%2BMVvTb%0ANwfU%0A)
11. On the resulting screen, you can see the App you just created.  
    Where the “**Client ID**” and “**Secret**” keys reside, which are the Keys required for the Element451 integration.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313371/414cef85121cbe82af7bfd771b38/Step11.png?expires=1784333700&signature=010b6322d95a0e535b68f6acd3c0f892c85dabdc8db5f0cf4179bfcde3c3396a&req=diAlHsp%2FnoJYWPMW1HO4zefxAHaXCx1a51QToff7LLkEIxDuSGkDczbC4o9o%0A1sWW%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313371/414cef85121cbe82af7bfd771b38/Step11.png?expires=1784333700&signature=010b6322d95a0e535b68f6acd3c0f892c85dabdc8db5f0cf4179bfcde3c3396a&req=diAlHsp%2FnoJYWPMW1HO4zefxAHaXCx1a51QToff7LLkEIxDuSGkDczbC4o9o%0A1sWW%0A)
12. By clicking on “**Show**” under “Secret” you can manage your secret keys for this Application.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313631/4b6b5c8a3ce9b122c1c6bb97b5d7/Step12.png?expires=1784333700&signature=1f659c00e23a2ffc724bab76c58c7b9c7b22092e2afdc301bf92b4f3ac258840&req=diAlHsp%2FnodcWPMW1HO4zXN1wg2kqhO%2BrXUQMwrk0lFJ%2BrCCX%2B2P%2B1%2B7JmlX%0ANcY0%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313631/4b6b5c8a3ce9b122c1c6bb97b5d7/Step12.png?expires=1784333700&signature=1f659c00e23a2ffc724bab76c58c7b9c7b22092e2afdc301bf92b4f3ac258840&req=diAlHsp%2FnodcWPMW1HO4zXN1wg2kqhO%2BrXUQMwrk0lFJ%2BrCCX%2B2P%2B1%2B7JmlX%0ANcY0%0A)
13. Down below in that screen, you can configure the settings for the Application; we only need “Accept Payments” for this integration, so you can select only that option and then click “**Save.**”  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313892/138a4a95fd4fcbb9c28c85072d5c/Step13.png?expires=1784333700&signature=d7b2324394f6eea41e9d6bf53b04de15e52a31094ffc043708b85cde56cf3748&req=diAlHsp%2FnolWW%2FMW1HO4zSpkD4C3fxWiBt%2FGbA%2BnuzRYOSBWjaiSoyYs8ThW%0AbX85%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028313892/138a4a95fd4fcbb9c28c85072d5c/Step13.png?expires=1784333700&signature=d7b2324394f6eea41e9d6bf53b04de15e52a31094ffc043708b85cde56cf3748&req=diAlHsp%2FnolWW%2FMW1HO4zSpkD4C3fxWiBt%2FGbA%2BnuzRYOSBWjaiSoyYs8ThW%0AbX85%0A)

    A warning might appear; just click “**Continue**.”  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028314389/cb1919ec8d6e4bdf02cc8409595f/Step13b.png?expires=1784333700&signature=bd9fa61b07ca8cde09d5a4bb2565453e3212ee68804867e8f3c3edd9ae792533&req=diAlHsp%2FmYJXUPMW1HO4zd3XswC%2B%2FiWjdbY9Rr5Zmt%2BnwNg5WjVIS4CnotPc%0Aj9zi%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028314389/cb1919ec8d6e4bdf02cc8409595f/Step13b.png?expires=1784333700&signature=bd9fa61b07ca8cde09d5a4bb2565453e3212ee68804867e8f3c3edd9ae792533&req=diAlHsp%2FmYJXUPMW1HO4zd3XswC%2B%2FiWjdbY9Rr5Zmt%2BnwNg5WjVIS4CnotPc%0Aj9zi%0A)
14. Scroll down to the “**Webhooks**” section and click on the “**Add** **Webhook**” button.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028314607/ee4d4512f9464d98c2063f62c54c/Step14.png?expires=1784333700&signature=d12e5b494ef9fc1eade5e7ea59ed3ff4cd28a1719f2ebc97d7bcb25c7b1fec9d&req=diAlHsp%2FmYdfXvMW1HO4zR%2BZepeTwCCLts2FfPcyT9WMcsook9ThYtXz26Pv%0AX1zz%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028314607/ee4d4512f9464d98c2063f62c54c/Step14.png?expires=1784333700&signature=d12e5b494ef9fc1eade5e7ea59ed3ff4cd28a1719f2ebc97d7bcb25c7b1fec9d&req=diAlHsp%2FmYdfXvMW1HO4zR%2BZepeTwCCLts2FfPcyT9WMcsook9ThYtXz26Pv%0AX1zz%0A)
15. On the creation form provide the “Webhook URL” as “[`https://<SUBDOMAIN>.integration.451.io/clients/integrations/paypal/webhook`](https://<SUBDOMAIN>.integrations.451.io/clients/integrations/paypal/webhook)”

    * 🚨 Important: Please notice that the placeholder “<SUBDOMAIN>” must be replaced with your assigned Element subdomain.

    For “Event types” select all event types under the “Payments and Payouts” option.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028314882/5df5b879a09c73c4e9e0c82581d0/Step15.png?expires=1784333700&signature=f3e3d22a05c23effea462d81032669a8aba370a83a1d8c93dc4390944514a103&req=diAlHsp%2FmYlXW%2FMW1HO4zRZmwEsyGzxTs9UPMRQUW6YDiFHyNYEyCVOZlYoe%0AjnXa%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028314882/5df5b879a09c73c4e9e0c82581d0/Step15.png?expires=1784333700&signature=f3e3d22a05c23effea462d81032669a8aba370a83a1d8c93dc4390944514a103&req=diAlHsp%2FmYlXW%2FMW1HO4zRZmwEsyGzxTs9UPMRQUW6YDiFHyNYEyCVOZlYoe%0AjnXa%0A)
16. Once the webhook is created you will see it listed, and it will show the Webhook ID that we need for that setup:  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028315256/9b4ae73d17788efeebe3ed25549c/Step16.png?expires=1784333700&signature=7abdad0fb8e0813346187ee271fa617774127d95c8e72346fb7a77667512267b&req=diAlHsp%2FmINaX%2FMW1HO4zdK3b70YS7zpd3Cbop%2BJA%2FjywM07qvXL5Uajw2Hp%0ADqHj%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2028315256/9b4ae73d17788efeebe3ed25549c/Step16.png?expires=1784333700&signature=7abdad0fb8e0813346187ee271fa617774127d95c8e72346fb7a77667512267b&req=diAlHsp%2FmINaX%2FMW1HO4zdK3b70YS7zpd3Cbop%2BJA%2FjywM07qvXL5Uajw2Hp%0ADqHj%0A)

## That's it!

Just like that your Application was created and is ready to be used and the webhook will be able to communicate updates to Element.

Make sure you copy and safely share the “**Client ID**”, “**Secret**” and “Webhook ID” keys with the Element451 team.

## Notes

* This process is exactly the same for creating Sandbox and Live applications.
* It is recommended to use meaningful names to the Application so later they are not confused with other Applications.
* You should only share keys with the Element451 team.

---