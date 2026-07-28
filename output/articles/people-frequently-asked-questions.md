---
title: 📌 People: Frequently Asked Questions
url: https://help.element451.com/en/articles/10602482-people-frequently-asked-questions
collection: People
---

This article answers commonly asked questions about People, providing quick solutions and key insights.

[![Pardon our progress as we actively develop this article.](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389330653/adbe7f86fd2e277f11859470ec82/Pardon+our+Progress.png?expires=1784333700&signature=9cd8e06d3ae721f530493e6e644777ae82a67f7794baf4cc8f474ffc2fa427ef&req=dSMvH8p9nYdaWvMW1HO4zWzvosLKqgnHFCrvyxQd4zSITSrzDhSPLg2%2BP6pC%0AwP%2F%2F1EwUB5fWSTFi4hI%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1389330653/adbe7f86fd2e277f11859470ec82/Pardon+our+Progress.png?expires=1784333700&signature=9cd8e06d3ae721f530493e6e644777ae82a67f7794baf4cc8f474ffc2fa427ef&req=dSMvH8p9nYdaWvMW1HO4zWzvosLKqgnHFCrvyxQd4zSITSrzDhSPLg2%2BP6pC%0AwP%2F%2F1EwUB5fWSTFi4hI%3D%0A)

# General | Contact Management

#### What’s the difference between deactivating and deleting a contact? And when should I delete a contact?

* **Deactivating:** Keeps all historical data intact. The contact can’t log in or be added to workflows, campaigns, and other modules, but their record remains in the system.
* **Deleting:** Permanently removes the contact and all related data.

We recommend deleting a contact when:

* You’re certain that **all related data is no longer needed**.
* To permanently remove test or duplicate records that have no historical value.

#### Why doesn't the main search bar (in the top navigation) return all students that match my search?

The main search bar does a text search across a specific set of fields:

* Name components (first, last, middle, preferred)
* Email address
* Identities (exact match)
* SSN (exact match), and
* Phone number (exact match)

The search dropdown only displays a limited number of results, so if you're searching a common name like "Smith," the student you're looking for may not appear in that short list.

To improve your results:

* Try narrowing your search by adding another part of their name (e.g., "Jordan Smith") or searching by their email address instead.
* If you're looking for a contact, we also recommend using the search feature within the **People** module, which displays results in a table format and provides a more complete view of matching records.

---

# Profile Cards

#### Why are my data sources showing in alphabetical order on profile cards?

All options on profile cards are automatically sorted alphabetically. This is system-defined behavior and may differ from the custom order you see in your data sources list. Index weights only apply to student-facing items, such as forms and applications.

---

# Deduplication

#### How can I merge records that aren’t automatically flagged as duplicates?

If Element451 doesn’t flag a duplicate record, you can manually search for and merge it. Use the **“See Possible Duplicates”** icon in the record header to compare it against your contact list and merge any identified duplicates. If you don’t see this icon, it may need to be added to your **profile template**.

For detailed steps, check out our help article: [Merging Duplicate Records](https://help.element451.com/en/articles/9472960-merging-duplicate-records#h_6b3bfc47d6).

#### Does E451 treat SSNs with dashes and SSNs without dashes as the same value?

No. In Element451, an SSN with dashes (e.g., 11-22-3333) is considered different from the same SSN without dashes (11122333). Use the validation option **“Save Value as Masked Format”** on the SSN field to standardize the format during entry.

---

# Filters + Segments

#### How can I create a segment to find records with no custom activities?

Because custom fields can either **exist with a value, exist but be empty, or not exist at all**, filtering for records with **no custom activities** requires a combination of operators. Using only **“Not In”** may exclude records where the field doesn’t exist in the database.

To ensure accurate results, you’ll need to combine **“Not In”** with **“Does Not Exist”** when building your segment. This approach accounts for both empty and missing values.

For a full breakdown of custom field behavior and step-by-step guidance, visit our help article: [Filtering Custom Fields in Segments](https://help.element451.com/en/articles/10167508-filtering-with-custom-fields-in-segments).

#### How can I create a segment of contacts who haven’t received a specific email?

Element451 does not currently support direct filtering for activity that did not occur (such as an email not being received). However, you can achieve this through a simple workaround: you’ll need to label those contacts who **did** receive the email and then filter them out using that label.

1. **Create a Segment of Those Who Received the Email:**

   * Go to Contacts > People.
   * Click Add Filter.
   * Choose the Received Email filter and specify the email you want to track.
   * Save this segment (e.g., “Received FAFSA 2025 Email”).
2. **Create a New Label:**

   * Go to Contacts > Categories > Labels.
   * Add a new label and give it a name that identifies it with the email (e.g., “FAFSA 2025 Email").
3. **Apply the Label to the Segment:**

   * Go to Contacts > Segments.
   * Locate your new Segment.
   * Click the more icon (three vertical dots) at the end of the row.
   * Select "Add Labels" from the menu.
   * This will bulk-apply the label to each student’s profile within the segment.
4. **Create a New Segment to Exclude Those Contacts:**

   * Go back to Contacts > People.
   * Click Add Filter.
   * Use the `User: Labels` filter to exclude the list you created.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1514179466/143308caa7599a6944b67f4c233e/CleanShot+2025-05-08+at+08_16_22.png?expires=1784333700&signature=b681267946670acd3a5e172c18aad6d3101bdb0c18a1dd8cb38523f236d074d2&req=dSUmEsh5lIVZX%2FMW1HO4zWuEIl2aPb21hNdJAp40OE4808HvAEeBzCnsI18E%0A5a3R%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1514179466/143308caa7599a6944b67f4c233e/CleanShot+2025-05-08+at+08_16_22.png?expires=1784333700&signature=b681267946670acd3a5e172c18aad6d3101bdb0c18a1dd8cb38523f236d074d2&req=dSUmEsh5lIVZX%2FMW1HO4zWuEIl2aPb21hNdJAp40OE4808HvAEeBzCnsI18E%0A5a3R%0A)
   * If you want to filter this list further (e.g., only transfer students, a specific enrollment year, or academic program), be sure to add those filters now. This ensures you’re only capturing those who didn’t receive the email and also meet your specified criteria.
5. **Save This as Your “Not Received” Segment:**

   * Save this segment as “Not Received Specific Email,” which will now contain only those contacts who did not receive the email.
   * The segment will now contain only those contacts who did not receive the specified email and match any additional criteria you applied.  
     ​

#### How can I create a segment of contacts by conversation tags?

The People module does not have a filter for segmenting contacts by conversation tags. However, you can use the conversation tag filter in the Conversations module to refine your inbox view.

#### How can I create a segment of contacts based on issues with name format?

You can use regular expressions (regex) in segment filters to identify name formatting issues in student records.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1514475612/78f44afc0fe21dd980e5ef2e7388/CleanShot%2B2025-02-20%2Bat%2B15_44_02.png?expires=1784333700&signature=93e931184ddb757bdeae5cce76002a8b4338fd89051cd959a748fe0daa24e102&req=dSUmEs15mIdeW%2FMW1HO4zSpz8UpfMWcBEoE8ruBY2lktCofAruYvPMsw7aqm%0AT2jnMSYqFlGXTFAO3k0%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1514475612/78f44afc0fe21dd980e5ef2e7388/CleanShot%2B2025-02-20%2Bat%2B15_44_02.png?expires=1784333700&signature=93e931184ddb757bdeae5cce76002a8b4338fd89051cd959a748fe0daa24e102&req=dSUmEs15mIdeW%2FMW1HO4zSpz8UpfMWcBEoE8ruBY2lktCofAruYvPMsw7aqm%0AT2jnMSYqFlGXTFAO3k0%3D%0A)

When adding a First Name or Last Name filter in Element451, select the REGEXP operator and enter a regex pattern to match specific issues.

Here are some common patterns you can use:

* **All caps names:** `^[A-Z\s]+$`

  + Example Match: "JOHN DOE"
* **Names with numbers:** `[0-9]`

  + Example Match: "J0hn"
* **Names with special characters:** `[^a-zA-Z'\-\s]`

  + Example Match: "J@hn" or "Doe#"
* **Names with leading or trailing spaces:** `^\s+|\s+$`

  + Example Match: " John" or "Doe "
* **Names with double spaces between words:** `\s{2,}`

  + Example Match: "John Doe"
* **Mixed capitalization (e.g., “jOHN dOE”)**: `\b[a-zA-Z]*[A-Z][a-z]*\b`

  + Example Match: "jOHN" or "doE"
* **Names missing vowels (possible typos):** `\b[b-df-hj-np-tv-z]{3,}\b`

  + Example Match: "Jhn" or "Brt"
* **First letter not capitalized:** `\b[a-z]`

  + Example Match: "john" or "doe"

#### How can I create a segment based on multiple area codes?

To create a segment for multiple area codes, follow these steps:

1. Use the **Phone (All Properties)** filter.
2. Select **Has → Number → Starts With**.
3. Enter the area code (e.g., 212).
4. Add additional area codes by clicking **Add Filter**, repeating the same steps, and grouping them with the **Any** operator.

#### How do I add a person to a segment?

Segments are built using **filters**, so you cannot manually add individuals. A person will appear in a segment only if they meet the defined segment criteria.

If the segment is non-calculated (meaning it doesn’t update dynamically as student data changes), you can refresh it by:

1. Open the segment.
2. Click the "Apply" button to **reapply** the filters and update the data.
3. Saving your changes by selecting either:

   * "**Save**" to overwrite the existing segment.
   * **"Save as New Segment"** to create a new version without overwriting the original.

#### Why are no records found when I filter by source code (alias)?

When filtering by source code, you should always use the `Alias List` filter.

#### Why can't I filter by (or find) a specific custom field?

If your custom field is a **text area** field, it won’t appear in the filter list because text area fields are not supported for filtering.

#### I’m using the Date of Inquiry filter, and a student doesn’t appear in my segment even though their date matches. Why?

Date filters in segments use 12:00 PM UTC as the cutoff time—so it’s not just the date that matters, but also the timestamp behind it.

For example, if you’re filtering for “Date of Inquiry on or after 5/2,” and a student’s Date of Inquiry is 5/2 at 9:15 AM UTC, they won’t be included. That’s because their timestamp is before the 12:00 PM UTC threshold applied to the filter.

Try adjusting the filter to “on or after 5/1” to catch records like this.

We know this can be confusing, and we’re exploring ways to improve it.

---