---
title: Element451 Field Reference (Data Dictionary)
url: https://help.element451.com/en/articles/15902105-element451-field-reference-data-dictionary
collection: Data Management
---

A complete reference of every standard field in Element451: names, slugs, data types, what each field does, and example values, organized by section.

This reference documents every standard field in Element451: what it is called, its slug, its data type, what it does, and an example value. Use it when you are building forms and applications, mapping imports and exports, building segments, or personalizing campaigns and you need to know exactly which field to use.

# How Fields Are Identified: Slugs

Every field in Element451 has a **slug**, a unique backend identifier. You will see slugs in Field Management, import/export mappings, tokens, and the API. A few rules make them easy to read:

* Standard contact fields start with `user-`, for example `user-first-name`. The segment of the slug after `user-` tells you which part of the record it belongs to: `user-addresses-`, `user-education-`, `user-applications-`, `user-evaluations-`, and so on.
* Custom fields follow the pattern `user-custom-[school]-[name]` and are created in Data + Automations > Field Management > Custom Fields.
* A trailing `*` (star mapping) means the field lives in a list and the star targets a position: any address, the second family member, a specific test attempt. Replace the star with a position number or leave it to match any entry.
* To use any field as a campaign token, wrap it as `[user:slug]` in lowercase, for example `[user:user-custom-demo1-dietary-restrictions]`. See the Campaign Tokens article for parameters like fallbacks and date formatting.

---

# The Field Reference, by Section

Standard fields are documented across the following articles. Each table lists the field name, slug, data type, data source (where the options come from, when applicable), what the field does, and an example value.

* [User Profile Fields (168 fields)](https://help.element451.com/en/articles/15901962-field-reference-user-profile-fields)
* [Application, Decision + Checklist Fields (119 fields)](https://help.element451.com/en/articles/15901975-field-reference-application-decision-checklist-fields)
* [Education Fields (124 fields)](https://help.element451.com/en/articles/15902012-field-reference-education-fields)
* [Test Score (Evaluation) Fields, Part 1 (124 fields)](https://help.element451.com/en/articles/15902029-field-reference-test-score-evaluation-fields-part-1)
* [Test Score (Evaluation) Fields, Part 2 (124 fields)](https://help.element451.com/en/articles/15902042-field-reference-test-score-evaluation-fields-part-2)
* [Family, Emergency Contact + Employment Fields (94 fields)](https://help.element451.com/en/articles/15902065-field-reference-family-emergency-contact-employment-fields)
* [Event, Milestone, Source + Note Fields (131 fields)](https://help.element451.com/en/articles/15902096-field-reference-event-milestone-source-note-fields)

A combined, spreadsheet-friendly version of all 884 standard fields is maintained by the Product team alongside this article set.

---

# Field Types

Every field has a type that controls how it displays on forms and what data it accepts.

|  |  |  |
| --- | --- | --- |
| **Type** | **What it is** | **Notes / Example** |
| Audio/Video | Upload of an audio or video file. | .mp4, .mov, .wmv, .avi, .mp3, .aac, .ogg, .wav, .webm and similar |
| Boolean | A yes/no, true/false value shown as a single checkbox. | true / false |
| Checkbox | A list shown all at once; multiple selections allowed. | Requires a data source |
| Date | Calendar date picker. | 2026-08-15 |
| DateTime | Calendar date and time picker. | 2026-08-15 14:30 |
| Dropdown (select) | A click-to-open list; one selection allowed. | Requires a data source |
| Radio Button | A list shown all at once; one selection allowed. | Requires a regular yes/no data source |
| Text (string) | A single line of text. | Alma |
| Text Area | Multiple lines of text. Not supported in filters and segments. | Longer written responses |
| Upload | Single file upload. | .pdf, .docx, .png, .csv and similar |
| Multiple Upload | Several files at once; same supported types as Upload. |  |
| Float / Integer | Numeric values, with or without decimals. | 3.75 / 2 |
| Array / Object | Structured lists or nested data, seen in exports and the API. | Multiple values (JSON) |

---

# Repeaters + Root Mappings

Some parts of the record hold lists (multiple applications, schools, test scores, family members). When exporting or using the API with inline templates, use the section root slug to repeat through all entries instead of only the first one.

|  |  |  |
| --- | --- | --- |
| **Section** | **Root Slug** | **Notes** |
| User Profile, Employment, Events, Education | None required | Education can optionally use user-education-schools-root to repeat all school records. |
| Applications | `user-applications-root` | Use the root or unwinding to get every application, not just the first. |
| Evaluations (Test Scores) | `user-evaluations-root` | Required for repeating. Some scores automatically return the super score for the requested test type. |
| Milestones | `user-milestones-root` | Required if you want more than the first matching milestone. |
| Sources | `user-sources-root` | May be required for more than the first matching source. |
| User Notes | `user-notes-root` | Required when using an inline template. |
| Family Members + Emergency Contacts | `user-family-root` | Or set a position scope (1, 2, 3...) for a specific entry. |
| Decisions Checklist | `decisions-checklist-root` | Requires unwinding when exporting. |
| Decisions | Not exportable via API | Use the Applications section to export decision data. |

---

# Fields with Editable Data Sources

These pre-defined fields appear in Data + Automations > Field Management > Fields. Each is powered by a data source you can swap for your own. The data source controls the options students see on forms and applications.

|  |  |  |  |
| --- | --- | --- | --- |
| **Field** | **Slug** | **Type** | **Default Data Source** |
| Academic Load | `user-education-academic-load` | select | Academic Load Options |
| Application Campus | `user-applications-campus` | select | [SYS] Campuses Reference Type |
| Application Concentration | `user-applications-concentration` | select | Major List |
| Application - Housing Interest | `user-applications-housing` | select | Housing List |
| Application Major | `user-applications-major` | select | Major List |
| Application Minor | `user-applications-minor` | select | Major List |
| Application Second Major | `user-applications-major-second` | select | Major List |
| Application Student Type | `user-applications-student-type` | select | [SYS] Student Types |
| Application Term | `user-applications-term` | select | Term List |
| Application Third Major | `user-applications-major-third` | select | Major List |
| Asian Background | `user-race-ethnicity-asian` | checkbox | [SYS] Race/Ethnicity - Asian |
| Black or African American Background | `user-race-ethnicity-black` | checkbox | [SYS] Race/Ethnicity - Black or African American |
| Citizenship Status | `user-citizenship-us-status` | select | [SYS] Citizenship Status List |
| Country of Birth | `user-citizenship-country-of-birth` | select | [SYS] Country List (ISO 3166) |
| Country of Citizenship | `user-citizenship-country` | select | [SYS] Country List (ISO 3166) |
| Gender | `user-gender` | radio | [SYS] Gender List |
| Gender Pronouns | `user-gender-pronouns` | select | [SYS] Gender Pronouns |
| Hispanic or Latino Background | `user-race-ethnicity-hispanic` | checkbox | [SYS] Race/Ethnicity - Hispanic or Latino |
| Housing Preference | `user-education-housing` | radio | [SYS] Housing List |
| How did you hear about us? | `user-how-did-you-hear-about-us` | select | [SYS] How did you hear about us List |
| Intended Campus | `user-education-campus` | select | [SYS] Campuses Reference Type |
| Intended Major | `user-education-prefered-major` | select | Major List |
| Intended Student Type | `user-education-student-type` | select | [SYS] Student Types |
| Intended Term | `user-education-term` | select | Term List |
| Middle Eastern or North African Background | `user-race-ethnicity-mena` | checkbox | [SYS] Race/Ethnicity - Middle Eastern or North African |
| Name Prefix | `user-prefix-name` | select | [SYS] Prefix List |
| Name Suffix | `user-suffix-name` | select | [SYS] Suffix List |
| Native Hawaiian or Pacific Islander Background | `user-race-ethnicity-hpi` | checkbox | [SYS] Race/Ethnicity - Native Hawaiian or Pacific Islander |
| Native Language | `user-citizenship-native-language` | select | [SYS] Languages ISO 639-2 |
| Race/Ethnicity Categories | `user-race-ethnicity-categories` | checkbox | [SYS] Race/Ethnicity Categories (2026 Federal Standards) |
| Religious Affilliation | `user-religion-name` | select | [SYS] Religion List |
| Second Country of Citizenship | `user-citizenship-country-second` | select | [SYS] Country List (ISO 3166) |
| State Residency Status | `user-citizenship-state-residency` | select | [SYS] State Residency Status |
| Tribal Affiliation | `user-race-ethnicity-tribe` | checkbox | [SYS] Race/Ethnicity - Tribes |
| Visa Type | `user-citizenship-visa-type` | select | [SYS] Visa types |
| Visa Type (Hold) | `user-citizenship-hold-visa-type` | select | [SYS] Visa types |
| White Background | `user-race-ethnicity-white` | checkbox | [SYS] Race/Ethnicity - White |
| Your Race | `user-race-categories` | checkbox | [SYS] Racial List |

---

# Field Groupings

Groupings bundle several related fields into one reusable block you can drop onto applications and forms. Manage their data sources in Data + Automations > Field Management > Groupings.

|  |  |  |
| --- | --- | --- |
| **Grouping** | **Slug** | **What it contains** |
| College Information | `user-education-schools-colleges` | College name, CEEB, dates attended, degree earned, and related college history fields. |
| Emergency Contact | `user-emergency-contacts-root` | Emergency contact name, relationship, phone, email, and address fields. |
| GPA | `user-gpa-root` | GPA value, scale, and weighting fields. |
| High School Information | `user-education-schools-highschools` | High school name, CEEB, dates attended, and graduation fields. |
| Holds | `user-holds-root` | Hold or restriction entries on the record. |
| Home Address | `user-addresses-home` | Street lines, city, state, zip, and country for the home address. |
| Mailing Address | `user-addresses-mailing` | Street lines, city, state, zip, and country for the mailing address. |
| Parent / Legal Guardian | `user-family-root` | Parent or guardian name, relationship, contact, education, and employment fields. |
| Parent/Legal Guardian (Alumnus) | `user-family-alumnis` | Alumni parent or guardian entries. |
| Race/Ethnicity | `user-race-ethnicity-root` | The complete race and ethnicity question set. |
| School Information | `user-education-schools-root` | Generic school entry covering both high schools and colleges. |
| Test Score | `user-evaluations-unofficial-root` | Self-reported (unofficial) test score entry with test type, date, and scores. |
| User Athletics | `user-athletics-root` | Sport, level of interest, and athletic recruitment fields. |
| User Employments | `user-employment-employees` | Employer, title, and employment date fields. |

---