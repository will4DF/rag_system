---
title: Authorize.net Setup (Payment Integration)
url: https://help.element451.com/en/articles/12884655-authorize-net-setup-payment-integration
collection: Settings + Permissions
---

# Overview

This guide walks you through setting up Authorize.net as a payment gateway to accept payments in Element451.   
​

First, you'll need to get setup in Authorize.net (explained below in this article) and then use the credentials created there to configure the payment gateway in Element451 (explained in the *[Getting Started with Payments + How to Add and Connect Payment Providers](https://help.element451.com/en/articles/3136121-getting-started-with-payments-how-to-add-and-connect-payment-providers)* article).

📌 **Note:** You will follow the same process outlined below for creating Live and Test (Sandbox) applications.

---

# Setup in Authorize.net

1. Navigate to the [Authorize.net website](https://login.authorize.net/) and login using your credentials.
2. From the dashboard, click on “**Account**” and then “**Account and API Settings**” on the left hand menu.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839438901/271c31813ac8ff0a2725f5934a13/4450ad33-6353-48f2-8fcf-e94d47d69d8f?expires=1784333700&signature=03f70f122e4e3cbe8f208d59fbc5096dab905297d65199a47b60f5a46be5e4b5&req=dSgkH819lYhfWPMW1HO4zdIpT5%2Bn00MiXuWV%2FHSbn25IUPUvhdixXMdqzJ7n%0A%2BhdY%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839438901/271c31813ac8ff0a2725f5934a13/4450ad33-6353-48f2-8fcf-e94d47d69d8f?expires=1784333700&signature=03f70f122e4e3cbe8f208d59fbc5096dab905297d65199a47b60f5a46be5e4b5&req=dSgkH819lYhfWPMW1HO4zdIpT5%2Bn00MiXuWV%2FHSbn25IUPUvhdixXMdqzJ7n%0A%2BhdY%0A)
3. From the Security Settings menu, click the “**API Credentials and Keys**."  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839439343/52723a5d18ebf8e0723faccad5b4/2de77e5c-d42e-4843-be7e-583043fd7b74?expires=1784333700&signature=2ea4f73d5b9c0e6bcc82a792281584777177eab85b5604529a00477ec1270dfd&req=dSgkH819lIJbWvMW1HO4zYz7vqSWO46uRS4EMWug3xW1lA3MmXV3fY6P%2BTT9%0AyuaO%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839439343/52723a5d18ebf8e0723faccad5b4/2de77e5c-d42e-4843-be7e-583043fd7b74?expires=1784333700&signature=2ea4f73d5b9c0e6bcc82a792281584777177eab85b5604529a00477ec1270dfd&req=dSgkH819lIJbWvMW1HO4zYz7vqSWO46uRS4EMWug3xW1lA3MmXV3fY6P%2BTT9%0AyuaO%0A)
4. On the **API Credentials and Keys** page, you'll see your “**API Login ID.**” You'll enter this ID in Element451.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839440479/0439740e7bdd0df395c21b4bdebb/bf2fa107-e91b-4e64-802c-42c7b2c53cad?expires=1784333700&signature=4c9081477548ccbc3c01e667f16fa2ac7c43db17a0f57bf00e2a4b4ca098681c&req=dSgkH816nYVYUPMW1HO4zc7NX1v8Vf9uH7YsgULXw6l0%2Fgzk5jhsKwFNTjpj%0AdYF%2B%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839440479/0439740e7bdd0df395c21b4bdebb/bf2fa107-e91b-4e64-802c-42c7b2c53cad?expires=1784333700&signature=4c9081477548ccbc3c01e667f16fa2ac7c43db17a0f57bf00e2a4b4ca098681c&req=dSgkH816nYVYUPMW1HO4zc7NX1v8Vf9uH7YsgULXw6l0%2Fgzk5jhsKwFNTjpj%0AdYF%2B%0A)
5. Scroll down to find the “**Transaction Key**” section. Click on “**GENERATE NEW TRANSACTION KEY**” button.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839443350/4dd785fc40fac35c721c5f7def9e/6c7f235b-829c-472c-9b19-4976fe75b8d9?expires=1784333700&signature=2f8442e17bdd8a5824791de60160221ac0a6e5b610ceb9d6a5432869249e590b&req=dSgkH816noJaWfMW1HO4zY3opWORffGsLXMT7TsonpJyKTt2%2B8aRSZXGqDn0%0AEyHv%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839443350/4dd785fc40fac35c721c5f7def9e/6c7f235b-829c-472c-9b19-4976fe75b8d9?expires=1784333700&signature=2f8442e17bdd8a5824791de60160221ac0a6e5b610ceb9d6a5432869249e590b&req=dSgkH816noJaWfMW1HO4zY3opWORffGsLXMT7TsonpJyKTt2%2B8aRSZXGqDn0%0AEyHv%0A)
6. A popup will appear, providing you with a **Transaction Key**. Use the **copy** **icon** to copy the key. Once you've copied the key and saved it, click on “Done.”

   * 📌 Note: Be sure to immediately copy and save it in a secure location because it cannot be revealed again.   
     ​

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839443721/52b36202df05508fa1368f2a5507/27a0b8a0-1f0c-456f-8033-55d756947bab?expires=1784333700&signature=20243c8bf5e6acf40af4698501bf1877c7ba65362cc5adcd101e29bdf3d352a1&req=dSgkH816noZdWPMW1HO4zZ%2B5ONVCG3daYBK75%2BcNnalKo89zmzbMzwbEgozI%0ACN4Y%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839443721/52b36202df05508fa1368f2a5507/27a0b8a0-1f0c-456f-8033-55d756947bab?expires=1784333700&signature=20243c8bf5e6acf40af4698501bf1877c7ba65362cc5adcd101e29bdf3d352a1&req=dSgkH816noZdWPMW1HO4zZ%2B5ONVCG3daYBK75%2BcNnalKo89zmzbMzwbEgozI%0ACN4Y%0A)
7. Scroll down to the “**Signature Key**” section and click on “**GENERATE NEW SIGNATURE KEY.**”  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839446704/d7d7182ccaf0de7fd4bc77e6c2f3/0dc6f38e-cf5a-4da5-bc54-ad3983611ed0?expires=1784333700&signature=7606ec74227d997520a4735449d30411fe02923f0268053a6b554557a6c59269&req=dSgkH816m4ZfXfMW1HO4zVy0FqIsxrzGPgKPUEHKwbznEF2OksGYN5XUTOXX%0AEqI6%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839446704/d7d7182ccaf0de7fd4bc77e6c2f3/0dc6f38e-cf5a-4da5-bc54-ad3983611ed0?expires=1784333700&signature=7606ec74227d997520a4735449d30411fe02923f0268053a6b554557a6c59269&req=dSgkH816m4ZfXfMW1HO4zVy0FqIsxrzGPgKPUEHKwbznEF2OksGYN5XUTOXX%0AEqI6%0A)
8. A popup will appear, providing you with a **Signature Key**. Use the **copy** **icon** to copy the key. Once you've copied the key and saved it, click on “Done.”

   * 📌 Note: Be sure to immediately copy and save it in a secure location because it cannot be revealed again.   
     ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839447022/9dbb1071470dced70e5d90e1fcc2/a4ef921a-339e-4f4b-a74c-19d5c402ee9e?expires=1784333700&signature=1a491cf291a48cae3441b7c8bf1a2137f8fdd449244bec26fa4411c19bd449c6&req=dSgkH816moFdW%2FMW1HO4zX4NWGVXnUp5okC%2BWc7faJZbqeW%2FKbNw%2BiDP6GRz%0AxUFL%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839447022/9dbb1071470dced70e5d90e1fcc2/a4ef921a-339e-4f4b-a74c-19d5c402ee9e?expires=1784333700&signature=1a491cf291a48cae3441b7c8bf1a2137f8fdd449244bec26fa4411c19bd449c6&req=dSgkH816moFdW%2FMW1HO4zX4NWGVXnUp5okC%2BWc7faJZbqeW%2FKbNw%2BiDP6GRz%0AxUFL%0A)
9. Click on “**Account**” and then “**Account and API Settings**” on the left hand menu.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839447563/0c9306345a89f7400b8f28cf8aa0/453465c9-579d-4f58-838a-03dab509a606?expires=1784333700&signature=45ed1c712c575c5a9e212039e24e4ed47079ce4bce3fc34d4031fb79fed27ed3&req=dSgkH816moRZWvMW1HO4zTxf5HL2EABFZ%2FmPYFsuWIDzCOUqvt1BA6D%2BHJxL%0AeT23%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839447563/0c9306345a89f7400b8f28cf8aa0/453465c9-579d-4f58-838a-03dab509a606?expires=1784333700&signature=45ed1c712c575c5a9e212039e24e4ed47079ce4bce3fc34d4031fb79fed27ed3&req=dSgkH816moRZWvMW1HO4zTxf5HL2EABFZ%2FmPYFsuWIDzCOUqvt1BA6D%2BHJxL%0AeT23%0A)
10. Scroll down to the “**Webhook Notifications**” section and click on “**Webhooks.**”  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839447963/4ee834cd8ad10536358898ad4d20/2d3a20bf-6e84-49db-8a2a-5ac810f2314f?expires=1784333700&signature=3d7b4d8e6ff78025b96a674ef864f767666d2b71eea4da102f9446518f00dd17&req=dSgkH816mohZWvMW1HO4zaplY2xP%2BYBM4lOsYSdp93pHL0AEofymZWDQIrRN%0A9vws%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839447963/4ee834cd8ad10536358898ad4d20/2d3a20bf-6e84-49db-8a2a-5ac810f2314f?expires=1784333700&signature=3d7b4d8e6ff78025b96a674ef864f767666d2b71eea4da102f9446518f00dd17&req=dSgkH816mohZWvMW1HO4zaplY2xP%2BYBM4lOsYSdp93pHL0AEofymZWDQIrRN%0A9vws%0A)

    ​
11. On the screen, click on the “**+ Create a webhook notification**” button in the top right corner of the screen.  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839448186/7a9f0a33f12bbfd514269622044c/3729c191-2f0e-4353-a0e7-55e466998e91?expires=1784333700&signature=b7bb667b183ad5cb31a085eef7b64a9d1524279194dc93b026808fe906c301a7&req=dSgkH816lYBXX%2FMW1HO4zfxb3x%2F01vqx%2F93uNnrV%2FoPCr72nYbPe02lk%2FprV%0AuFqO%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839448186/7a9f0a33f12bbfd514269622044c/3729c191-2f0e-4353-a0e7-55e466998e91?expires=1784333700&signature=b7bb667b183ad5cb31a085eef7b64a9d1524279194dc93b026808fe906c301a7&req=dSgkH816lYBXX%2FMW1HO4zfxb3x%2F01vqx%2F93uNnrV%2FoPCr72nYbPe02lk%2FprV%0AuFqO%0A)

    ​
12. Complete the details for the webhook notification:

    * **Webhook notification name**: “Element451 Payments”
    * **Endpoint URL**: “https://`<SUBDOMAIN>`.integration.451.io/clients/integrations/authorizenet/webhook”

      + 🚨 **Important:** Please replace <SUBDOMAIN> with your assigned subdomain).
    * **Status**: “Active”  
      ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839448812/5d53051fb8daa759c8d7bf0d33f1/d59d9068-e2a0-4fb8-a5f0-88fb1737171e?expires=1784333700&signature=ac1f637085bdf408a741284738c8dc91bc2191770df34e8fb09853e19f53a67d&req=dSgkH816lYleW%2FMW1HO4zSHgNcK7IIBuXqJh4LEj%2Ba0lteju9zkjY%2F%2BCVo36%0ARw2n%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839448812/5d53051fb8daa759c8d7bf0d33f1/d59d9068-e2a0-4fb8-a5f0-88fb1737171e?expires=1784333700&signature=ac1f637085bdf408a741284738c8dc91bc2191770df34e8fb09853e19f53a67d&req=dSgkH816lYleW%2FMW1HO4zSHgNcK7IIBuXqJh4LEj%2Ba0lteju9zkjY%2F%2BCVo36%0ARw2n%0A)
13. From the **Select Events** menu, use the checkboxes to select all the events from the “**Payment** **Events**” section and click “**Save**.”  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839449072/1d78dd6ddc1c2ed56c8057c108d6/def07227-833f-4d48-9561-106a4266d7cf?expires=1784333700&signature=42ee0e23a76bb463253c9376be493c58661ff584f7ed37e412761ea443b9da9c&req=dSgkH816lIFYW%2FMW1HO4zVH3oQ%2BVOeJLnWuZvBcLfzbkU5k1zJfkK18evgub%0AArCg%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839449072/1d78dd6ddc1c2ed56c8057c108d6/def07227-833f-4d48-9561-106a4266d7cf?expires=1784333700&signature=42ee0e23a76bb463253c9376be493c58661ff584f7ed37e412761ea443b9da9c&req=dSgkH816lIFYW%2FMW1HO4zVH3oQ%2BVOeJLnWuZvBcLfzbkU5k1zJfkK18evgub%0AArCg%0A)
14. You should see the resulting webhook notification listed:  
    ​

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839449249/ab52fb93b39a3d42be7deb82ddb9/05f249c7-a938-416c-87c6-193511b7fef5?expires=1784333700&signature=336c7d2583d9e56fd596ade126762939b698af374dff6b2ca2c7bb58dcd2dc4a&req=dSgkH816lINbUPMW1HO4zTmUb39hycw%2FacnxmowCGLLChYJ5OXKenYs1b9ZN%0AkmWe%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1839449249/ab52fb93b39a3d42be7deb82ddb9/05f249c7-a938-416c-87c6-193511b7fef5?expires=1784333700&signature=336c7d2583d9e56fd596ade126762939b698af374dff6b2ca2c7bb58dcd2dc4a&req=dSgkH816lINbUPMW1HO4zTmUb39hycw%2FacnxmowCGLLChYJ5OXKenYs1b9ZN%0AkmWe%0A)
15. Now, you can navigate to Element451 and configure your integration with the values obtained using this guide:

    * API Login Id
    * Transaction Key
    * Signature Key

*For a step-by-step guide to configure the payment gate in Element451, review out [Getting Started with Payments + How to Add and Connect Payment Providers](https://help.element451.com/en/articles/3136121-getting-started-with-payments-how-to-add-and-connect-payment-providers)*help article.

---