---
title: Deduplication Logic
url: https://help.element451.com/en/articles/4935488-deduplication-logic
collection: People
---

How Element451 determines duplicates by comparing and scoring fields.

# Overview

Element451 automatically searches for and scores possible duplicate records to help you maintain clean, accurate student data. This article outlines how the duplicate detection logic works—from the fields that trigger a check to how matches are scored and presented in the Deduplication Module.

If you're looking for a more foundational overview of how to use the Deduplication Module, check out our [Getting Started with Deduplication](https://help.element451.com/en/articles/2511116-getting-started-with-the-deduplication-module) article.

---

# When Does Element451 Search for Duplicates?

A duplicate search is automatically triggered when any of the following fields on a student's record are updated:

* First Name
* Last Name
* Email
* Phone
* Addresses
* Identities
* Date of Birth

---

# How Duplicate Match Scores Are Calculated

When a potential match is found, Element451 assigns it a **duplicate probability score**. This score determines the likelihood that the two records belong to the same person.

## Scoring Logic + Thresholds

* Matching first and last names alone will not flag duplicates. An additional field is required for a score to be generated. At least one of these fields must match:*email*, *phone*, *address*, *date of birth*, or *social security number*.
* Each field contributes differently to the score—some fields carry more weight than others.
* A minimum score of **70%** is required to flag a duplicate. The more valuable fields that match, the higher the duplicate score. For a list of common matching field combinations and the calculated score, see the *[Matching Field Combinations and Their Scores](#h_30a5703e5e)* section below.

## Special Cases + Considerations

* **Person Name**

  + All names are made lowercase.
  + Leading and trailing spaces are removed.
  + Hyphenated and space-separated names (like “Mary-Jane” or “Mary Jane”) are split into parts and compared individually.
  + First and last names are compared separately. If any of the first name parts from one record exist in the other record's first name parts, it is a match. If both conditions are positive, the name is considered a match.
  + Element451 uses a comprehensive nickname database with over 1,300 variations to catch common name substitutions (e.g., "Bill" for "William").
  + Former last names on the contact (if present) are also considered when matching, so a record's prior surname can still surface a duplicate.
* **Email**

  + Emails from both records are stripped, so just the prefix before “@” is compared. Since these records have already passed the initial search, we are just searching for an exact match in this round.
  + When a record only includes name and email, the email must be an exact match. This prevents false positives when limited data is available.
  + Empty or missing emails are ignored—they never count as a match, even if both records happen to have a blank email field.
* **Identity**

  + If either record has an “EMAIL” identity, Element compares it against the other record's primary email address.
  + If either record has an ALTERNATE\_ID identity, Element451 compares it against the other record's Alternate ID values. An exact match on Alternate ID is treated the same as other identity matches in the scoring logic.
  + Identity matches respect **identity type namespaces**—a "Banner ID" of `12345` on one record only matches a "Banner ID" of `12345` on the other, not a different identity type that happens to share the value.
* **Date of Birth**

  + The day, month, and year of the records' dates of birth are compared for an exact match.
* **Addresses**

  + Element uses a third-party API to normalize each address's “Street 1” field.
  + If there are multiple addresses, Element checks if any of the first record's normalized addresses match any of the second record's normalized addresses exactly.
* **Phone**

  + Using the clean 7-digit number only, if any of the first record's phone numbers match any of the second record's phone numbers exactly, it is a positive match.
* **Social Security Numbers**

  + SSNs are considered highly reliable. If included in either record, a matching SSN significantly boosts the duplicate score.
  + SSNs must contain exactly 9 digits to be used in duplicate detection.
  + When comparing records, Element451 automatically ignores any dashes, spaces, or formatting characters, so 123-45-6789, 123 45 6789, and 123456789 are all treated as the same SSN.
  + Element451 automatically rejects invalid or placeholder SSNs—common test values like `000-00-0000`, `111-11-1111`, or `123-45-6789` will not be used for matching.
  + **Important:** If two records have the same SSN with different formatting, you'll need to decide which format to keep when merging, based on your data preferences.
* **Contradiction Detection**

  + Even when high-value fields (like email or identity) match exactly, Element451 will **cap or reject the score** if the records also show strong contradictions—for example, conflicting dates of birth or conflicting SSNs. This prevents two genuinely different people who happen to share an email from being scored as a confident duplicate.
* **Relationships**

  + If two records are connected in Element451 (e.g., siblings or parents), they will not be flagged as duplicates, even if other fields match.
* **Ambiguous Duplicates**

  + When more than one record qualifies as a potential duplicate, Element451 flags the result as **ambiguous** and includes **match explanation metadata** showing which fields drove each candidate's score. This makes it easier for staff to review the candidates side-by-side and choose the correct master record.

## Matching Field Combinations and Their Scores

The table below shows how different combinations of matching fields contribute to the duplicate probability score. A score of **70% or higher** is required for records to be flagged as potential duplicates.

|  |  |
| --- | --- |
| **Matching Fields** | **Score** |
| Name + Email | 70% |
| Name + DOB | 75% |
| Name + Address | 75% |
| Name + Phone | 75% |
| Name + Email + DOB | 85% |
| Name + Email + Address | 85% |
| Name + Email + Phone | 85% |
| Name + SSN | 95% |
| Name + Email + SSN | 95% |
| Name + Phone + SSN | 95% |
| Name + Address + SSN | 95% |
| Name + DOB + SSN | 100% |
| Name + Email + DOB + SSN | 100% |
| Name + DOB + Address + SSN | 100% |
| Name + Address + Phone + SSN | 100% |
| Name + DOB + Address | 100% |
| Name + DOB + Phone | 100% |
| Name + Address + Phone | 100% |
| All fields except SSN | 100% |
| All fields including SSN | 100% |

***Note:*** *These combinations reflect how the deduplication algorithm scores matches behind the scenes. Element451 does not require every field to be present, only enough matching data to reach the 70% threshold.*

---

# Selection of a Master Record

When Element451 finds a possible duplicate, it performs a *"smart"* selection to determine which record should be a new "master" record*.* First, Element looks for a recent activity such as:

* Logging in
* Opening an email
* Filling out a form
* Registered for an event

Then, Element will prioritize the record without hard email bounces or unsubscribe milestones.

---