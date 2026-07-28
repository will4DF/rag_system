---
title: Bolt App Fraud Detector Agent
url: https://help.element451.com/en/articles/9927313-bolt-app-fraud-detector-agent
collection: Bolt AI
---

# Overview

The Bolt App Fraud Detector Agent, powered by Bolt AI, identifies and flags potentially fraudulent applications by analyzing multiple risk factors. Using an advanced AI engine, the agent evaluates indicators such as submission timing, email validity, IP address behavior, and other factors to assign an overall risk assessment to each application.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1503336117/20ec6685c47ff8d6f474b2979f3a/Bolt+App+Reader+Agent+-+HC+Graphic+%281%29.png?expires=1784333700&signature=b6fda7e4c501932d6ea850a7fd45eaac6295a3d7144e5de2725b430113776ea4&req=dSUnFcp9m4BeXvMW1HO4zdrgC0lqqAKUr%2BboyAl4JAc8xbo4eD40Kz7wgSDY%0AMU9BwJg%2B3jgHG%2BP%2F5MM%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1503336117/20ec6685c47ff8d6f474b2979f3a/Bolt+App+Reader+Agent+-+HC+Graphic+%281%29.png?expires=1784333700&signature=b6fda7e4c501932d6ea850a7fd45eaac6295a3d7144e5de2725b430113776ea4&req=dSUnFcp9m4BeXvMW1HO4zdrgC0lqqAKUr%2BboyAl4JAc8xbo4eD40Kz7wgSDY%0AMU9BwJg%2B3jgHG%2BP%2F5MM%3D%0A)

## Key Features + Considerations:

* **Powered by Bolt AI**: Utilizes an LLM-based reasoning engine that analyzes behaviors, patterns, and data points to flag applications and provides in-depth reasoning.
* **Flagging System**: Each application meeting fraud detection criteria ([detailed below](#h_a578b8faa5)) is flagged at least as “low risk.” These flags are available for human review, allowing you to confirm or dismiss the flag manually.
* **Three Risk Categories**: Risk is classified into three levels—low, medium, and high.
* **Permissions for Access**:

  + *View Application Fraud Status*: Allows users to see the flag and its reasoning.
  + *Update Application Fraud Status*: Allows users to mark applications as fraudulent or legitimate.
* **Segment and Filter Capabilities**: Filter flagged applications in the Decisions and People modules for focused review.

---

# Which Applications Are Evaluated for Fraud?

* **Element451 Applications**: If you're using Element451's Applications module, fraud detection runs immediately after an application is submitted/decision is created.
* **Imported Applications**: If you're importing application data from another solution into Element451, fraud detection applies in these cases:

  + *[Submission via Workflows + Rules](https://help.element451.com/en/articles/9007767-importing-application-data?q=app+reader#h_04259716ff)*: If a decision is created using the “Register Application in Decisions” action and the "Run Application Fraud Detection" toggle is turned on. The fraud detection agent is triggered upon creation of the decision.
  + *Login and Submit*: If an applicant logs into the application site to submit.

If data, such as an IP address or submission time, is missing from an imported application, those items cannot be evaluated for fraud. For example, submission timing won’t be assessed without submission time data.

---

# Fraud Detection Factors

The agent evaluates fraud risk by analyzing multiple indicators, ensuring no single factor disproportionately affects the fraud score. Here are the key factors assessed:

Expand each section to read more about the specific factors within each category.

## Timing

* **Time to Submit**: A very short time to complete the application might indicate the use of automated tools or bots.
* **Local Submission Time**: Submitting an application in the middle of the night, based on the applicant’s local time, could signal unusual behavior.

📌 **Note:** For applicants with previous application history, timing indicators, such as time to submit, are given less weight or may be excluded entirely from evaluation, especially when prior applications have already been reviewed and resolved as valid.

## Duplicate Applications

* **Number of Duplicate Users**: Multiple similar accounts suggest that someone may be trying to bypass the system.
* **Applications from Duplicates**: If duplicate users submit many applications, it can indicate coordinated fraudulent activity.

## Email Address Analysis

* **Validity Score**: A scoring system rates how likely the email address is to be invalid, from 0 (low risk) to 100 (high risk).
* **Email Status**: We classify emails as valid, risky, or invalid.
* **Disposable Emails**: Temporary or throwaway emails are often used for fraudulent purposes.
* **Bounces**: We verify whether emails to this address have bounced in the past, signaling a fake or inactive email.
* **Blocked Access**: If the email address is linked to suspicious activity, it will be flagged here.

## IP Address Analysis

* **Other IP Addresses Used**: We track multiple IPs associated with the same user, which can suggest location masking.
* **Shared IPs**: Multiple users applying from the same IP can indicate coordinated activity.
* **IP Risk Score**: An external service assigns a risk score from 0.01 (low risk) to 99 (high risk) to assess the IP’s credibility.
* **VPN Detection**: We check whether the applicant is using a VPN, which can mask their true location.
* **Location Consistency**: We compare the IP address to the applicant’s provided home address. A large discrepancy could indicate fraud.

## Location Analysis

* **Distance from Home**: We analyze the distance between the applicant’s IP address and their stated home address.
* **Distance from School**: We also compare the distance between the IP address and the location of the school they’re applying to. Large distances or mismatches could signal fraudulent intent.

## Phone Number Analysis

* **Phone Validity**: We check if the provided phone number is valid and active.
* **Line Type**: Identifies whether the phone is a mobile, landline, or VoIP. Internet-based numbers are sometimes used for fraudulent activities.
* **Carrier and Risk Assessment**: The phone’s carrier is assessed for risk levels, as some carriers are more prone to fraudulent activity.
* **Identity Match**: We compare the phone number with the applicant’s name and address. A low match score can suggest the number doesn’t belong to the applicant.

---

# Reviewing + Resolving Fraud Flags

All evaluated applications include a fraud flag category: low risk (green), medium risk (yellow), and high risk (red). These flags require human review, allowing you to confirm or dismiss the flag manually. Use the resolution feature to record whether an application is legitimate or fraudulent. This supports the review workflow and reporting; it does not retrain the underlying model. Incorporating filters for low and medium-risk applications into your fraud prevention rules can enhance the breadth of oversight. Excluding high-risk classifications from additional rules prevents unnecessary overlaps and ensures optimized specificity in rule applications.

## Accessing the Flag

* **All Decisions List (Medium + High Risk):** On the All Decisions page/list, an icon to the right of the applicant's name denotes if the application was flagged with medium or high risk. Low-risk applications are **not** denoted in this view.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243173017/237e5227bccdb41bf9e53bde625b/App+Fraud+Detection+-+Medium+Risk+-+Decision+List.png?expires=1784333700&signature=6fe41a2bf4cd07ca0e166c3d63c565649f8384260b87e7c0a2cd1a763f5429fc&req=dSIjFch5noFeXvMW1HO4zfKL%2FWx2TiEuSjuuepVCH9hQ9UylygFEmDu9tiJ6%0Atu7k%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243173017/237e5227bccdb41bf9e53bde625b/App+Fraud+Detection+-+Medium+Risk+-+Decision+List.png?expires=1784333700&signature=6fe41a2bf4cd07ca0e166c3d63c565649f8384260b87e7c0a2cd1a763f5429fc&req=dSIjFch5noFeXvMW1HO4zfKL%2FWx2TiEuSjuuepVCH9hQ9UylygFEmDu9tiJ6%0Atu7k%0A)
* **Decision Header:**

  + **Chip (All Risks)**: When viewing an individual decision, a color-coded chip is under the score, indicating whether the application fraud risk is low (gray), medium (orange), or high (red).

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243170323/52640b6b99cc8279ceb7a77655c7/App+Fraud+Detection+-+Medium+Risk+-+Flag+Chip.png?expires=1784333700&signature=9c2ebce0fca475a45d86236d1c37bd304da3293fbc83d67f4e4d97e820c64c6a&req=dSIjFch5nYJdWvMW1HO4zVB9WXyta1YzJKOh3jC46ChdOszc26hn1uSJcaQD%0AcqrV%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243170323/52640b6b99cc8279ceb7a77655c7/App+Fraud+Detection+-+Medium+Risk+-+Flag+Chip.png?expires=1784333700&signature=9c2ebce0fca475a45d86236d1c37bd304da3293fbc83d67f4e4d97e820c64c6a&req=dSIjFch5nYJdWvMW1HO4zVB9WXyta1YzJKOh3jC46ChdOszc26hn1uSJcaQD%0AcqrV%0A)
  + **Banner (Medium + High Risk):** In addition to the chip, a banner is displayed under the header for medium and high-risk flags to increase visibility.

    [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243174937/881037c220b853ce60506cb03ad8/App+Fraud+Detection+-+Medium+Risk+-+Banner.png?expires=1784333700&signature=ce4006f85dd7da662a7168eba7f1a24f34fd71b7886b7e136d793c38e7680758&req=dSIjFch5mYhcXvMW1HO4zVUGW4PWWj1aUbIBRquDRKGTxD%2BpcvyRUA2K3%2FLR%0ASUAq%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243174937/881037c220b853ce60506cb03ad8/App+Fraud+Detection+-+Medium+Risk+-+Banner.png?expires=1784333700&signature=ce4006f85dd7da662a7168eba7f1a24f34fd71b7886b7e136d793c38e7680758&req=dSIjFch5mYhcXvMW1HO4zVUGW4PWWj1aUbIBRquDRKGTxD%2BpcvyRUA2K3%2FLR%0ASUAq%0A)

## Reviewing Flag Reasoning + Resolving Flags

Each flag contains a detailed reasoning for the category that was assigned to it. This reasoning breaks down the factors contributing to the risk, helping you understand why the application was flagged and whether it warrants further investigation.

To review and resolve flags:

1. Click on the chip in the header (or the banner if it's a medium or high-risk flag).
2. The Fraud Detection side sheet will open, where you can review the reasoning.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243186276/51618f682af052166bc874db9236/App+Fraud+Detection+-+Reasoning+-+w+bkgd.png?expires=1784333700&signature=e9df65db547b00cef74400fbef599086a0ac843c95c18b50352ea5efc00e3333&req=dSIjFch2m4NYX%2FMW1HO4zQjJpLGQh%2FM1MS0FGbIT5aDu3udh16Lt48ZxS1DM%0AG8f8%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243186276/51618f682af052166bc874db9236/App+Fraud+Detection+-+Reasoning+-+w+bkgd.png?expires=1784333700&signature=e9df65db547b00cef74400fbef599086a0ac843c95c18b50352ea5efc00e3333&req=dSIjFch2m4NYX%2FMW1HO4zQjJpLGQh%2FM1MS0FGbIT5aDu3udh16Lt48ZxS1DM%0AG8f8%0A)
3. After your review, if you determine:

   * the application is fraudulent, select "Mark as Fraudulent."
   * the application is legitimate, select "Mark as Legitimate."   
     ​

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243187275/c26cb10c85520ee3dad233d8d086/Fraud+-+Reasoning.png?expires=1784333700&signature=cd39670efec94c2ecdbd9e7ae45c179acebe727e57ce2d0800c59c2f50687270&req=dSIjFch2moNYXPMW1HO4zZhNWl0zQQm9bt2y0MFI7udf4bufsxanghyc4s5N%0AOyFf%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1243187275/c26cb10c85520ee3dad233d8d086/Fraud+-+Reasoning.png?expires=1784333700&signature=cd39670efec94c2ecdbd9e7ae45c179acebe727e57ce2d0800c59c2f50687270&req=dSIjFch2moNYXPMW1HO4zZhNWl0zQQm9bt2y0MFI7udf4bufsxanghyc4s5N%0AOyFf%0A)

---

# Filtering + Segmenting by Fraud Flags

To make reviewing flagged applications easier, you can use filtering:

* **Decisions Module**: In the Decisions module (Applications > Decisions > All Decisions), you can filter applications based on the fraud flag to quickly see which ones may require attention.
* **People Module**: In the People module, you can use Decision Filters to isolate applicants with certain fraud risk levels, helping you focus on specific subsets of applicants. You can also use filters or conditions effectively to ensure that rules incorporate the appropriate risk classifications without overlaps. Regularly assess your configurations to verify completeness and accuracy in fraud detection management.

---

# Exporting Fraud Detection Data

You can leverage the [Import + Export](https://help.element451.com/en/articles/9006515-getting-started-with-exports) module to export the fraud flag category, along with the reasoning behind the flag. This allows you to review the data offline or share it with your team for further analysis.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1611866476/6e35dca3cacabf75c620f38953de/CleanShot+2025-07-09+at+15_00_48%402x.png?expires=1784333700&signature=79bbf22f6f612ad68e76f103d676bf184a1cda692cf6a8c43f595ec9674041e0&req=dSYmF8F4m4VYX%2FMW1HO4zXnHlhNczKM7sE40zEd5QO8mH12iZT5oSfG9DK32%0AHkELZx4S5gjPvz5tnBI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1611866476/6e35dca3cacabf75c620f38953de/CleanShot+2025-07-09+at+15_00_48%402x.png?expires=1784333700&signature=79bbf22f6f612ad68e76f103d676bf184a1cda692cf6a8c43f595ec9674041e0&req=dSYmF8F4m4VYX%2FMW1HO4zXnHlhNczKM7sE40zEd5QO8mH12iZT5oSfG9DK32%0AHkELZx4S5gjPvz5tnBI%3D%0A)

---