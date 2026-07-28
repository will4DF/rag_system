---
title: Understanding Fraud Detector Agent Reasoning Terminology
url: https://help.element451.com/en/articles/15032569-understanding-fraud-detector-agent-reasoning-terminology
collection: Bolt AI
---

A reference for interpreting the language and signals in Fraud Detector Agent reasoning when reviewing applications.

# Overview

The **Fraud Detector Agent** generates plain-language reasoning to explain why an application received a particular fraud recommendation. Because the reasoning is written in natural language, the same underlying signal can be expressed in different ways across applications. An "exact identity match" in one decision may appear as a "100 identity match score" in another.

This article is a reference for admissions, enrollment, and CRM operations teams reviewing Fraud Detector Agent decisions. Use it to interpret the most common terminology used in reasoning: phone identity match scores, IP and location distance phrases, and contextual phrases like "aligns with."

📌 **Note:** Fraud Detector Agent reasoning supports human review; it does not replace it. Always consider reasoning alongside the full application record and your institution's review policies.

## Where This Applies

This guidance applies to:

* [Decisions](https://help.element451.com/en/articles/9200421-getting-started-with-decisions) and application review workflows
* [Fraud Detector Agent](https://help.element451.com/en/articles/9927313-bolt-app-fraud-detector-agent)
* Admissions, enrollment, and CRM operations teams

For background on what the Agent does and how it fits into the review process, see [Bolt App Fraud Detector Agent](https://help.element451.com/en/articles/9927313-bolt-app-fraud-detector-agent).

## Key Concepts at a Glance

* Phone identity match scores are **structured values** from an external phone intelligence service.
* The phone identity match score can be **0**, **40**, **80**, or **100**. A score of **100** indicates an exact match.
* IP and location distance wording is **approximate**.
* Terms like **close**, **very close**, **modest**, and **relatively small** are qualitative descriptors, not fixed product thresholds.
* Reasoning supports human review; it does not replace your institution's review process.

---

# Phone Identity Match Terminology

The Fraud Detector Agent references phone identity match results when the applicant's phone number can be compared against known identity information for that number.

The underlying field is commonly referred to as **identity\_match\_score**. The score reflects the overall level of match between applicant information (first name, last name, address) and known properties for the phone number, on a scale from **0** to **100**.

## How to Read the Score

|  |  |  |
| --- | --- | --- |
| **Score** | **General interpretation** | **How to read it during review** |
| **100** | Exact match | The applicant information strongly matches known identity information for the phone number. |
| **80** | Strong match | Most identity information matches the phone number record. |
| **40** | Partial or limited match | Some identity information matches, but the signal isn't strong enough to treat as exact. |
| **0** | No match | The applicant information does not match known identity information for the phone number. |

🧠 **Good to Know:** The match score reflects whether the applicant's first name, last name, and address match the known properties for that phone number. It does not factor in IP, email, or activity signals.

---

# What "Exact" Means for Phone Reasoning

When phone reasoning says **exact identity matches**, the phone identity match is at the strongest available level. Interpret it the same way as a **100** identity match score.

You may see slightly different wording across applications. One decision might say "the phone identity match score is 100," while another might say "the phone has exact identity matches." These are plain-language descriptions of the same signal.

---

# Why Reasoning Sometimes Shows a Percentage and Sometimes Uses Words

The Fraud Detector Agent generates a plain-language explanation from the data available at the time of evaluation. Some decisions include the numeric value directly. Others summarize the result in natural language.

Wording can vary even when the underlying signal is similar. Read a phrase like "exact identity matches" as a descriptive explanation, not a separate scoring system.

✨ **Pro Tip:** Train reviewers to focus on the *type* of signal being described (identity match strength, IP proximity, address consistency) rather than the specific phrasing. The phrasing varies; the signal type does not.

---

# IP and Location Distance Terminology

The Fraud Detector Agent compares the approximate location of the applicant's IP address against their home address or the institution's location.

## Common Phrases

|  |  |  |
| --- | --- | --- |
| **Term** | **General interpretation** | **How to use it** |
| **Very close** | The IP location appears very near the comparison location. | Treat as a lower-risk location signal, unless other signals conflict. |
| **Close** | The IP location appears near the comparison location. | Treat as directionally consistent, but still approximate. |
| **Modest distance** | The IP location is not immediately nearby, but is within a reasonable range. | Don't treat as exact distance guidance, or as a concern by itself. |
| **Relatively small distance** | The distance isn't large enough on its own to create strong concern. | Review alongside other phone, email, address, and activity signals. |
| **Aligns with** | The signal is directionally consistent with the applicant's provided information. | Use as one supporting signal, not as proof that the application is legitimate. |

These terms are approximate. They are not fixed product thresholds.

## Reference Distances From Reviewed Examples

|  |  |  |  |
| --- | --- | --- | --- |
| **Reasoning term** | **Example distance (internal calc)** | **Example distance (external service)** | **Recommended interpretation** |
| **Close** | About 5,688 meters | About 10 km | The IP location appeared reasonably near the applicant's home address. |
| **Modest** | About 26,693 meters | About 28 km | The IP location wasn't immediately nearby, but wasn't obviously inconsistent on its own. |

🚨 **Important:** Use these as reference points, not permanent thresholds. IP location is approximate and varies depending on the internet service provider, network routing, device connection, VPN status, and available location data.

---

# Location Fields Used in Reasoning

The Fraud Detector Agent uses several location-based fields when evaluating IP and address consistency.

|  |  |
| --- | --- |
| **Field** | **Description** |
| **activity\_distance\_from\_home** | Distance in meters between the approximate location of the applicant's IP address and the applicant's home address. |
| **activity\_distance\_from\_client** | Distance in meters between the approximate location of the applicant's IP address and the institution's location. |
| **home\_distance\_from\_client** | Distance in meters between the applicant's home address and the institution's location. |
| **home\_address\_distance\_to\_ip\_km** | Distance in kilometers between the applicant's IP address and home address, calculated by an external service. |

📌 **Note:** Some fields aren't available for every institution or every application. For example, if an institution hasn't configured a physical address in its settings, the Fraud Detector Agent can't calculate distance from the applicant's activity or home address to the institution.

---

# How to Interpret "Aligns With"

When the reasoning says a signal **aligns with** the application, the signal is consistent with the applicant information or with other lower-risk indicators.

Examples include:

* The IP address is in the same country as the home address.
* The IP address is near the home address.
* The phone identity information matches the applicant's name or address.
* The signal does not conflict with other information on the application.

**Aligns with** doesn't mean the application is legitimate. It means this specific signal isn't creating a major contradiction.

---

# How to Review Fraud Detector Agent Reasoning

When reviewing reasoning, use the explanation as a guide to the signals the Agent considered.

Recommended review process:

1. Start with the overall fraud recommendation and risk level.
2. Review each reasoning section separately: phone, IP, address, email, and activity signals when available.
3. Treat phone identity match scores as **structured** values.
4. Treat IP distance wording as **approximate** guidance.
5. Look for patterns across multiple signals rather than relying on a single word.
6. Use the full application record and your institution's review process before taking action.

💡 **Use Case:** An admissions reviewer opens an application flagged as high risk. The reasoning notes "exact identity matches" on the phone and an IP "close" to the home address; both are lower-risk signals. However, the email signal flags a recently created throwaway address, and the activity log shows submissions from multiple unrelated devices. Looking at the *pattern* across signals rather than the favorable phone result alone, the reviewer escalates the application.

---

# Examples

## Phone reasoning says "exact identity matches"

If the Agent says the phone has **exact identity matches**, treat it as the strongest phone identity match signal. This is equivalent to a **100** identity match score.

## IP is described as "close" to the home address

If the Agent says the IP is **close** to the home address, treat it as a lower-risk location signal. The IP location appears reasonably near the applicant's home address.

Because IP location is approximate, don't treat **close** as a precise distance band.

## IP distance is described as "modest"

If the Agent says the IP-to-home distance is **modest**, treat it as a distance that isn't extremely close, but also isn't obviously inconsistent on its own.

In one reviewed case, **modest** described a distance of approximately 27 to 28 km. Use this as a reference example, not a fixed threshold.

## IP country "aligns with" the home address

If the Agent says the IP is in the same country as the home address, that signal is lower risk than an IP from a different country or region that doesn't match the applicant's expected location.

---

# Important Caveats

The Fraud Detector Agent reasoning supports human review. It does not replace your institution's review policies.

Keep the following in mind:

* IP geolocation is approximate.
* Internet service providers may route traffic through nearby or regional locations that differ from the applicant's actual city.
* A nearby IP address doesn't prove an application is legitimate.
* A distant IP address doesn't always prove an application is fraudulent.
* Qualitative terms vary because the Agent writes reasoning in natural language.
* Distance terms are not currently strict thresholds.
* The Fraud Detector Agent uses the application and signal data available at the time of evaluation.

🚨 **Important:** Marking an application as legitimate or fraud serves as data collection and as a UI indicator that a reviewer confirmed or overrode the Agent's opinion. It does not retrain the underlying model.

---

# Frequently Asked Questions

### Does "exact" mean 100 for phone identity match?

In practice, yes. If phone reasoning says **exact identity matches**, treat it as the strongest available phone identity match signal, equivalent to a **100** identity match score.

### Are "close," "very close," and "modest" fixed distance ranges?

No. These are qualitative descriptions generated from the available location data. Treat them as approximate guidance, not fixed product thresholds.

### Why did one application show 100 while another said "exact"?

The Agent chooses different wording when explaining the same type of signal. One explanation might include the numeric score; another might summarize the result in words.

### Does marking an application as legitimate or fraud train the Agent?

No. Today, marking an application as legitimate or fraud serves as data collection and as a UI indicator that a reviewer changed or confirmed the Agent's opinion. It does not train the underlying LLM.

### What should staff do if the wording is unclear?

Review the full reasoning, the underlying application details, and any available signal data. If you still can't interpret the decision confidently, follow your institution's escalation process.

---