---
title: Payment Types
url: https://help.element451.com/en/articles/9071731-payment-types
collection: Settings + Permissions
---

Explore Element451's flexible payment types: Fixed, Conditional, Calculated, & User-defined. Tailor your payment process for every need.

# Overview

Element451 offers four distinct payment types: **Fixed**, **Conditional**, **Calculated**, and **User-defined**. Whether establishing a static fee, implementing dynamic pricing based on specific criteria, calculating amounts from user data or form fields, or enabling custom contributions within a particular range, these options are tailored to suit various payment needs.

Let's dive into how each payment type can optimize your processes and provide a tailored experience for every user.

---

# Fixed

The fixed payment type allows you to set a **constant amount every person must pay**.

* **Amount**: Specify the amount to be charged.

[![](https://downloads.intercomcdn.com/i/o/1005453780/6abe0ab8355e0ff8ec6e88f2/Payment+Types+-+Fixed.png?expires=1784333700&signature=63e502f9fc2b4f5fb95955e639a58c4972397dae399e298a643b9d00441406bf&req=dSAnE817noZXWfMW1HO4zf%2F6K5SWk7k43QwmUmyPVw5KomvJgjyPVNGqYx2I%0ASg1gmJYmPtO%2F09a%2BYOc%3D%0A)](https://downloads.intercomcdn.com/i/o/1005453780/6abe0ab8355e0ff8ec6e88f2/Payment+Types+-+Fixed.png?expires=1784333700&signature=63e502f9fc2b4f5fb95955e639a58c4972397dae399e298a643b9d00441406bf&req=dSAnE817noZXWfMW1HO4zf%2F6K5SWk7k43QwmUmyPVw5KomvJgjyPVNGqYx2I%0ASg1gmJYmPtO%2F09a%2BYOc%3D%0A)

---

# Conditional

The conditional payment type enables dynamic pricing through **payment rules based on specific conditions**, like user groups and event dates.

* **Amount**: Specify the amount to be charged.
* **Payment Rules:** Select at least one payment rule. Payment rules are configured in General Settings. To learn more about configuring payment rules, visit our [Payment Rules](https://help.element451.com/en/articles/9071765-payment-rules) article.

[![](https://downloads.intercomcdn.com/i/o/1005715123/e561a106b1a707d2ffef67ae/Payment+Types+-+Conditional.png?expires=1784333700&signature=9e02e9eeb65342e6d2079b66b07b3a85460e491230b01699ed415444be2d0eac&req=dSAnE85%2FmIBdWvMW1HO4zdRXv2Fwu8CimTA44zH2s%2FE53GusgYHqUcuVpcf8%0AGzpV1oo8jH05vlymq2Q%3D%0A)](https://downloads.intercomcdn.com/i/o/1005715123/e561a106b1a707d2ffef67ae/Payment+Types+-+Conditional.png?expires=1784333700&signature=9e02e9eeb65342e6d2079b66b07b3a85460e491230b01699ed415444be2d0eac&req=dSAnE85%2FmIBdWvMW1HO4zdRXv2Fwu8CimTA44zH2s%2FE53GusgYHqUcuVpcf8%0AGzpV1oo8jH05vlymq2Q%3D%0A)

---

# Calculated

The calculated payment type allows the payment amount to be **calculated using a formula**. This formula can utilize data from the person's record and/or fields on the submitted form.

* **Calculated**: In the black box, insert your formula. For a list of formula functions, [click here](https://integrations.element451.com/calculated-fields-37).
* **Test** **Formula**: You can test your formula using the 'test formula' toggle, selecting a user, and clicking **Evaluate**. The result of the test will appear in the Evaluated Formula black box. Note: the user you select to test will need a value in the appropriate field(s).

[![](https://downloads.intercomcdn.com/i/o/1005706389/db44fd0e4a5b9d1c2920cfe0/Payment+Types+-+Calculated.png?expires=1784333700&signature=76a37f7a39b62e947a8d9d28d58d3b400fbad875588568cd400f0246940f7ce1&req=dSAnE85%2Bm4JXUPMW1HO4zeot7JI4ngapC0cwU4SRep42%2B92zD%2Fobs%2FZGr5k4%0APAH1SWzqnJvelxzYBXI%3D%0A)](https://downloads.intercomcdn.com/i/o/1005706389/db44fd0e4a5b9d1c2920cfe0/Payment+Types+-+Calculated.png?expires=1784333700&signature=76a37f7a39b62e947a8d9d28d58d3b400fbad875588568cd400f0246940f7ce1&req=dSAnE85%2Bm4JXUPMW1HO4zeot7JI4ngapC0cwU4SRep42%2B92zD%2Fobs%2FZGr5k4%0APAH1SWzqnJvelxzYBXI%3D%0A)

### *Example*

Imagine you're selling homecoming tailgate tickets via a form. You include a *quantity* field asking buyers how many tickets they wish to purchase. The formula multiplies the quantity by $25, the price per pass.   
​  
Here is how that formula would look `[user-custom-tu-orderquantity] * 25`

Note: To include guest fees in your formula calculation, you can use the `user-events-guest-number` field.

---

# User-defined

This user-defined payment type allows purchasers to input a **custom amount within a specified range**. This type is ideal for donations or other use cases where the purchaser should determine the amount to pay.

* **Default** **Amount**: The default amount is a suggested starting point for the payment amount. The figure appears in the payment field by default, offering a quick option for users but not limiting their generosity. You can adjust this to any amount that makes sense for your use case.
* **Validation (Minimum and Maximum)**: Establish the minimum and maximum limits to ensure the payment is within a specified range that fits your operational requirements and financial goals.
* **Field** **Config (Placeholder and Hint)**: Use the placeholder and hint texts to guide users through their payment input, regardless of the scenario. A placeholder can display a sample amount or the most common contribution. At the same time, the hint offers additional information or clarification—ensuring users feel confident and informed as they complete their transactions.

[![](https://downloads.intercomcdn.com/i/o/1005710406/e7f070514d588001941c3c75/Payment+Type+-+User+Defined.png?expires=1784333700&signature=047aa7ceaaba4084d127fe0970e3f53be8ac1e21a5c5683b05d4b587bf9ba1e2&req=dSAnE85%2FnYVfX%2FMW1HO4za1AjH5aV7p8twD6ANsbEHgbCpnJZi3M8427wj1e%0ASMbRUBhbNvdFsGU%2Bvtw%3D%0A)](https://downloads.intercomcdn.com/i/o/1005710406/e7f070514d588001941c3c75/Payment+Type+-+User+Defined.png?expires=1784333700&signature=047aa7ceaaba4084d127fe0970e3f53be8ac1e21a5c5683b05d4b587bf9ba1e2&req=dSAnE85%2FnYVfX%2FMW1HO4za1AjH5aV7p8twD6ANsbEHgbCpnJZi3M8427wj1e%0ASMbRUBhbNvdFsGU%2Bvtw%3D%0A)

#

---