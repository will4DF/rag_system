---
title: Field Reference: User Profile Fields
url: https://help.element451.com/en/articles/15901962-field-reference-user-profile-fields
collection: Data Management
---

Every standard user profile field in Element451 with its slug, type, purpose, and an example value.

# User Profile (168 fields)

Note: Does not requires a root item when using an inline template. Titles ending in \* are repeater fields (per-item slugs, e.g. user-addresses-\*).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **Data Source** | **What It Does** | **Example** |
| ACT ID | `user-identities-actid` | string |  | ACT ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Address - City \* | `user-addresses-city-*` | string |  | Address - City. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Raleigh |
| Address - Coordinates (object) \* | `user-addresses-location-*` | object |  | Address - Coordinates (object). Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Nested object (JSON) |
| Address - Coordinates Point (object) \* | `user-addresses-point-*` | object |  | Address - Coordinates Point (object). Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Nested object (JSON) |
| Address - Country \* | `user-addresses-country-*` | string |  | Address - Country. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | US |
| Address - County \* | `user-addresses-county-*` | string |  | Address - County. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Address - County Code \* | `user-county-code-*` | float |  | Address - County Code. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 3.75 |
| Address - EPS code (CollegeBoard) \* | `user-addresses-eps-*` | string |  | Address - EPS code (CollegeBoard). Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Address - Latitude \* | `user-addresses-lat-*` | float |  | Address - Latitude. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 3.75 |
| Address - Longitude \* | `user-addresses-lng-*` | float |  | Address - Longitude. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 3.75 |
| Address - Miles from Campus \* | `user-distance-campus-miles-*` | float |  | Address - Miles from Campus. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Main Campus |
| Address - Minutes from Campus \* | `user-distance-campus-minutes-*` | float |  | Address - Minutes from Campus. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Main Campus |
| Address - province \* | `user-addresses-province-*` | string |  | Address - province. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Address - Source \* | `user-addresses-source-*` | string |  | Address - Source. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Address - State \* | `user-addresses-state-*` | string |  | Address - State. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | NC |
| Address - Street 1 \* | `user-addresses-street1-*` | string |  | Address - Street 1. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Address - Street 2 \* | `user-addresses-street2-*` | string |  | Address - Street 2. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Address - Street 3 \* | `user-addresses-street3-*` | string |  | Address - Street 3. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Address - Type \* | `user-addresses-type-*` | string |  | Address - Type. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Address - Zipcode \* | `user-addresses-zip-*` | string |  | Address - Zipcode. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 27601 |
| Address - Zipcode + 4 \* | `user-addresses-zipfour-*` | string |  | Address - Zipcode + 4. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 27601 |
| ANTHOLOGY ID | `user-identities-anthologyid` | string |  | ANTHOLOGY ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Applying for Student Visa (F1)? | `user-citizenship-visa-f1` | boolean | Values for [SYS] Yes/No | Applying for Student Visa (F1)?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| Birth Place | `user-citizenship-birth-place` | string |  | Birth Place. Stored on the contact record. | Text value |
| Campus | `user-education-campus` | string | Transformations for campuses | Campus. Stored on the contact record. Options come from: Transformations for campuses. | Main Campus |
| Campus Nexus ID | `user-identities-campusnexusid` | string |  | Campus Nexus ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Cas ID | `user-identities-casid` | string |  | Cas ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| CFNC ID | `user-identities-cfncid` | string |  | CFNC ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Citizenship Status | `user-citizenship-us-status` | string | Values for [SYS] Citizenship Status List | Citizenship Status. Stored on the contact record. Options come from: Values for [SYS] Citizenship Status List. | Text value |
| Coalition ID | `user-identities-coalitionid` | string |  | Coalition ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| College Board ID | `user-identities-collegeboardid` | string |  | College Board ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Common App ID | `user-identities-commonappid` | string |  | Common App ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Common App Transfer ID | `user-identities-commonapptransferid` | string |  | Common App Transfer ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Country of Birth | `user-citizenship-country-of-birth` | string | Values for [SYS] Country List (ISO 3166) | Country of Birth. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Country of Citizenship | `user-citizenship-country` | string | Values for [SYS] Country List (ISO 3166) | Country of Citizenship. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Date of Birth | `user-dob` | date |  | The contact's date of birth. | 2026-08-15 |
| EAB ID | `user-identities-eabid` | string |  | EAB ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Element ID | `user-elementid` | mongoid |  | Element ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Email address | `user-email-address` | string |  | The contact's primary email address. Used for identification, matching, and email campaigns. | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Encoura ID | `user-identities-encouraid` | string |  | Encoura ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| English Native Language? | `user-citizenship-english-native-language` | boolean | Values for [SYS] Yes/No | English Native Language?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| Ethos ID | `user-identities-ethosid` | string |  | Ethos ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Family - Guardian 1 Address City | `user-family-guardian-1-address-city` | string |  | Family - Guardian 1 Address City. Stored on the contact record. | Raleigh |
| Family - Guardian 1 Address Country | `user-family-guardian-1-address-country` | string | Values for [SYS] Country List (ISO 3166) | Family - Guardian 1 Address Country. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Family - Guardian 1 Address Province | `user-family-guardian-1-address-province` | string |  | Family - Guardian 1 Address Province. Stored on the contact record. | Text value |
| Family - Guardian 1 Address State | `user-family-guardian-1-address-state` | string | Values for [SYS] USA State List (ISO) | Family - Guardian 1 Address State. Stored on the contact record. Options come from: Values for [SYS] USA State List (ISO). | NC |
| Family - Guardian 1 Address Street line 1 | `user-family-guardian-1-address-street-1` | string |  | Family - Guardian 1 Address Street line 1. Stored on the contact record. | 123 Oak Street |
| Family - Guardian 1 Address Street line 2 | `user-family-guardian-1-address-street-2` | string |  | Family - Guardian 1 Address Street line 2. Stored on the contact record. | 123 Oak Street |
| Family - Guardian 1 Address Zipcode | `user-family-guardian-1-address-zipcode` | string |  | Family - Guardian 1 Address Zipcode. Stored on the contact record. | 27601 |
| Family - Guardian 1 college | `user-family-guardian-1-college` | string |  | Family - Guardian 1 college. Stored on the contact record. | Text value |
| Family - Guardian 1 Degree | `user-family-guardian-1-degree` | string |  | Family - Guardian 1 Degree. Stored on the contact record. | Bachelor of Science |
| Family - Guardian 1 Employee | `user-family-guardian-1-employee` | boolean |  | Family - Guardian 1 Employee. Stored on the contact record. | true / false |
| Family - Guardian 1 employer | `user-family-guardian-1-employer` | string |  | Family - Guardian 1 employer. Stored on the contact record. | Text value |
| Family - Guardian 1 First Name | `user-family-guardian-1-first-name` | string |  | Family - Guardian 1 First Name. Stored on the contact record. | Alma |
| Family - Guardian 1 is living or deceased | `user-family-guardian-1-living` | boolean |  | Family - Guardian 1 is living or deceased. Stored on the contact record. | true / false |
| Family - Guardian 1 is same\_address | `user-family-guardian-1-same_address` | boolean |  | Family - Guardian 1 is same\_address. Stored on the contact record. | true / false |
| Family - Guardian 1 Last Name | `user-family-guardian-1-last-name` | string |  | Family - Guardian 1 Last Name. Stored on the contact record. | Mater |
| Family - Guardian 1 marital status | `user-family-guardian-1-marital-status` | string |  | Family - Guardian 1 marital status. Stored on the contact record. | Text value |
| Family - Guardian 1 occupation | `user-family-guardian-1-occupation` | string |  | Family - Guardian 1 occupation. Stored on the contact record. | Registered Nurse |
| Family - Guardian 1 Phone Number | `user-family-guardian-phone-1-number` | string |  | Family - Guardian 1 Phone Number. Stored on the contact record. | (919) 555-0123 |
| Family - Guardian 1 Prefix Name | `user-family-guardian-1-prefix-name` | string |  | Family - Guardian 1 Prefix Name. Stored on the contact record. | Ms. |
| Family - Guardian 1 Relationship Type | `user-family-guardian-1-relationship` | string | Values for [SYS] Family Relationship | Family - Guardian 1 Relationship Type. Stored on the contact record. Options come from: Values for [SYS] Family Relationship. | Mother |
| Family - Guardian 1 Title | `user-family-guardian-1-title` | string |  | Family - Guardian 1 Title. Stored on the contact record. | Registered Nurse |
| Family - Guardian 2 Address City | `user-family-guardian-2-address-city` | string |  | Family - Guardian 2 Address City. Stored on the contact record. | Raleigh |
| Family - Guardian 2 Address Country | `user-family-guardian-2-address-country` | string | Values for [SYS] Country List (ISO 3166) | Family - Guardian 2 Address Country. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Family - Guardian 2 Address Province | `user-family-guardian-2-address-province` | string |  | Family - Guardian 2 Address Province. Stored on the contact record. | Text value |
| Family - Guardian 2 Address Same as Student | `user-family-guardian-2-same_address` | boolean |  | Family - Guardian 2 Address Same as Student. Stored on the contact record. | true / false |
| Family - Guardian 2 Address State | `user-family-guardian-2-address-state` | string | Values for [SYS] USA State List (ISO) | Family - Guardian 2 Address State. Stored on the contact record. Options come from: Values for [SYS] USA State List (ISO). | NC |
| Family - Guardian 2 Address Street line 1 | `user-family-guardian-2-address-street-1` | string |  | Family - Guardian 2 Address Street line 1. Stored on the contact record. | 123 Oak Street |
| Family - Guardian 2 Address Street line 2 | `user-family-guardian-2-address-street-2` | string |  | Family - Guardian 2 Address Street line 2. Stored on the contact record. | 123 Oak Street |
| Family - Guardian 2 Address Zipcode | `user-family-guardian-2-address-zipcode` | string |  | Family - Guardian 2 Address Zipcode. Stored on the contact record. | 27601 |
| Family - Guardian 2 College | `user-family-guardian-2-college` | string |  | Family - Guardian 2 College. Stored on the contact record. | Text value |
| Family - Guardian 2 Degree | `user-family-guardian-2-degree` | string |  | Family - Guardian 2 Degree. Stored on the contact record. | Bachelor of Science |
| Family - Guardian 2 Employee | `user-family-guardian-2-employee` | boolean |  | Family - Guardian 2 Employee. Stored on the contact record. | true / false |
| Family - Guardian 2 Employer | `user-family-guardian-2-employer` | string |  | Family - Guardian 2 Employer. Stored on the contact record. | Text value |
| Family - Guardian 2 First Name | `user-family-guardian-2-first-name` | string |  | Family - Guardian 2 First Name. Stored on the contact record. | Alma |
| Family - Guardian 2 Last Name | `user-family-guardian-2-last-name` | string |  | Family - Guardian 2 Last Name. Stored on the contact record. | Mater |
| Family - Guardian 2 Living | `user-family-guardian-2-living` | boolean |  | Family - Guardian 2 Living. Stored on the contact record. | true / false |
| Family - Guardian 2 Marital Status | `user-family-guardian-2-marital-status` | string | Values for [SYS] Marital Status List | Family - Guardian 2 Marital Status. Stored on the contact record. Options come from: Values for [SYS] Marital Status List. | Text value |
| Family - Guardian 2 Occupation | `user-family-guardian-2-occupation` | string |  | Family - Guardian 2 Occupation. Stored on the contact record. | Registered Nurse |
| Family - Guardian 2 Phone Number | `user-family-guardian-phone-2-number` | string |  | Family - Guardian 2 Phone Number. Stored on the contact record. | (919) 555-0123 |
| Family - Guardian 2 Phone Type | `user-family-guardian-2-phone-type` | string |  | Family - Guardian 2 Phone Type. Stored on the contact record. | (919) 555-0123 |
| Family - Guardian 2 Relationship Type | `user-family-guardian-2-relationship` | string | Values for [SYS] Family Relationship | Family - Guardian 2 Relationship Type. Stored on the contact record. Options come from: Values for [SYS] Family Relationship. | Mother |
| Family - Guardian 2 Title | `user-family-guardian-2-title` | string |  | Family - Guardian 2 Title. Stored on the contact record. | Registered Nurse |
| Family - Guardian Email 1 | `user-family-guardian-email-1` | string |  | Family - Guardian Email 1. Stored on the contact record. | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Family - Guardian Email 2 | `user-family-guardian-email-2` | string |  | Family - Guardian Email 2. Stored on the contact record. | [alma.mater@example.com](mailto:alma.mater@example.com) |
| First Name | `user-first-name` | string |  | The contact's legal first (given) name. | Alma |
| First Source Description - Calculated | `user-calculated-first_source_description` | string |  | First Source Description. Calculated automatically by Element451 and read only. | Text value |
| First Source Type - Calculated | `user-calculated-first_source_type` | string |  | First Source Type. Calculated automatically by Element451 and read only. | Text value |
| Former Last Name | `user-former-last-name` | string |  | A previous last name (for example, prior to a legal name change). | Mater |
| Furthest Funnel Stage - Calculated | `user-calculated-furthest_funnel_stage` | string |  | Furthest Funnel Stage. Calculated automatically by Element451 and read only. | Text value |
| Gender | `user-gender` | string | Values for [SYS] Gender List | The contact's gender selection, powered by the Gender List data source. | Female |
| Gender Pronouns | `user-gender-pronouns` | string | Values for [SYS] Gender Pronouns | The contact's pronouns (for example she/her, he/him, they/them). | Female |
| High School Counselor Marketing ID | `user-identities-hscmid` | string |  | High School Counselor Marketing ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Historic ID | `user-identities-historicid` | string |  | Historic ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Home Address - City | `user-addresses-home-city` | string |  | Home Address - City. Stored on the contact record. | Raleigh |
| Home Address - Coordinates (object) | `user-addresses-home-location` | object |  | Home Address - Coordinates (object). Stored on the contact record. | Nested object (JSON) |
| Home Address - Country | `user-addresses-home-country` | string | Values for [SYS] Country List (ISO 3166) | Home Address - Country. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Home Address - County | `user-addresses-home-county` | string |  | Home Address - County. Stored on the contact record. | Text value |
| Home Address - Mailing? | `user-addresses-home-mailing` | boolean | Values for [SYS] Yes/No | Home Address - Mailing?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| Home Address - province | `user-addresses-home-province` | string |  | Home Address - province. Stored on the contact record. | Text value |
| Home Address - State | `user-addresses-home-state` | string | Values for [SYS] USA State List (ISO) | Home Address - State. Stored on the contact record. Options come from: Values for [SYS] USA State List (ISO). | NC |
| Home Address - Street 1 | `user-addresses-home-street1` | string |  | Home Address - Street 1. Stored on the contact record. | 123 Oak Street |
| Home Address - Street 2 | `user-addresses-home-street2` | string |  | Home Address - Street 2. Stored on the contact record. | 123 Oak Street |
| Home Address - Street 3 | `user-addresses-home-street3` | string |  | Home Address - Street 3. Stored on the contact record. | 123 Oak Street |
| Home Address - Zip Code | `user-addresses-home-zip` | string |  | Home Address - Zip Code. Stored on the contact record. | 27601 |
| Home Address - Zipcode + 4 | `user-addresses-home-zipfour` | string |  | Home Address - Zipcode + 4. Stored on the contact record. | 27601 |
| How did you hear about us? | `user-how-did-you-hear-about-us` | string |  | Self-reported answer for how the contact heard about the institution. | Text value |
| Intended Degree | `user-education-degree` | string | Transformations for degrees | Intended Degree. Stored on the contact record. Options come from: Transformations for degrees. | Bachelor of Science |
| Intended Major | `user-education-prefered-major` | string | Transformations for Majors | Intended Major. Stored on the contact record. Options come from: Transformations for Majors. | Biology |
| Intended Term | `user-education-term` | string | Transformations for Term | Intended Term. Stored on the contact record. Options come from: Transformations for Term. | Fall 2026 |
| Last Name | `user-last-name` | string |  | The contact's last (family) name. | Mater |
| Mailing Address - City | `user-addresses-mailing-city` | string |  | Mailing Address - City. Stored on the contact record. | Raleigh |
| Mailing Address - Coordinates (object) | `user-addresses-mailing-location` | object |  | Mailing Address - Coordinates (object). Stored on the contact record. | Nested object (JSON) |
| Mailing Address - Country | `user-addresses-mailing-country` | string | Values for [SYS] Country List (ISO 3166) | Mailing Address - Country. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Mailing Address - County | `user-addresses-mailing-county` | string |  | Mailing Address - County. Stored on the contact record. | Text value |
| Mailing Address - province | `user-addresses-mailing-province` | string |  | Mailing Address - province. Stored on the contact record. | Text value |
| Mailing Address - State | `user-addresses-mailing-state` | string | Values for [SYS] USA State List (ISO) | Mailing Address - State. Stored on the contact record. Options come from: Values for [SYS] USA State List (ISO). | NC |
| Mailing Address - Street 1 | `user-addresses-mailing-street1` | string |  | Mailing Address - Street 1. Stored on the contact record. | 123 Oak Street |
| Mailing Address - Street 2 | `user-addresses-mailing-street2` | string |  | Mailing Address - Street 2. Stored on the contact record. | 123 Oak Street |
| Mailing Address - Street 3 | `user-addresses-mailing-street3` | string |  | Mailing Address - Street 3. Stored on the contact record. | 123 Oak Street |
| Mailing Address - Zip Code | `user-addresses-mailing-zip` | string |  | Mailing Address - Zip Code. Stored on the contact record. | 27601 |
| Mailing Address - Zipcode + 4 | `user-addresses-mailing-zipfour` | string |  | Mailing Address - Zipcode + 4. Stored on the contact record. | 27601 |
| Middle Name | `user-middle-name` | string |  | The contact's middle name. | J |
| Name Prefix | `user-prefix-name` | string | Values for [SYS] Prefix List | Name prefix such as Mr., Ms., or Dr. | Ms. |
| Name Suffix | `user-suffix-name` | string | Values for [SYS] Suffix List | Name suffix such as Jr., Sr., II, or III. | Jr. |
| Native Language | `user-citizenship-native-language` | string | Values for [SYS] Languages ISO 639-2 | Native Language. Stored on the contact record. Options come from: Values for [SYS] Languages ISO 639-2. | Text value |
| NC Student Number ID | `user-identities-ncstudentnumberid` | string |  | NC Student Number ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Niche ID | `user-identities-nicheid` | string |  | Niche ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Opt in for SMS | `user-sms-updates` | boolean |  | Opt in for SMS. Stored on the contact record. | true / false |
| Opt in for WhatsApp | `user-whatsapp-updates` | boolean |  | Opt in for WhatsApp. Stored on the contact record. | true / false |
| Permanent Resident Number | `user-citizenship-permanent-resident-number` | string |  | Permanent Resident Number. Stored on the contact record. | Text value |
| Phone Cell - Country Code | `user-phone-cell-country-code` | string |  | Phone Cell - Country Code. Stored on the contact record. | 1 |
| Phone Cell - Number | `user-phone-cell-number` | string |  | Phone Cell - Number. Stored on the contact record. | (919) 555-0123 |
| Phone Home - Country Code | `user-phone-home-country-code` | string |  | Phone Home - Country Code. Stored on the contact record. | 1 |
| Phone Home - Number | `user-phone-home-number` | string |  | Phone Home - Number. Stored on the contact record. | (919) 555-0123 |
| Phone Number \* | `user-phone-number-*` | string |  | Phone Number. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Phone Type \* | `user-phone-type-*` | string |  | Phone Type. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Populi ID | `user-identities-populiid` | string |  | Populi ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Preferred Name | `user-preferred-name` | string |  | The name the contact prefers to be called; used by staff and in personalization when set. | Alma |
| Previously Applied? | `user-education-university-applied-before` | boolean | Values for [SYS] Yes/No | Previously Applied?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| Race - Categories | `user-race-categories` | array | Values for [SYS] Racial List | Race - Categories. Stored on the contact record. Options come from: Values for [SYS] Racial List. | multiple values (list) |
| Race - Hispanic/Latino | `user-race-hispanic` | boolean | Values for [SYS] Yes/No | Race - Hispanic/Latino. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| RCN ID | `user-identities-rcnid` | string |  | RCN ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Religious Affiliation | `user-religion-name` | string | Values for [SYS] Religion List | Religious Affiliation. Stored on the contact record. Options come from: Values for [SYS] Religion List. | Text value |
| School Email | `user-identities-school-email` | string |  | School Email: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| School ID | `user-identities-schoolid` | string |  | School ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Scoir ID | `user-identities-scoirid` | string |  | Scoir ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Search ID | `user-identities-searchid` | string |  | Search ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Second Country of Citizenship | `user-citizenship-country-second` | string | Values for [SYS] Country List (ISO 3166) | Second Country of Citizenship. Stored on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| SMS Enabled \* | `user-phone-sms-enabled-*` | boolean |  | SMS Enabled. Stored on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Social Security # | `user-ssn` | string |  | Social Security #. Stored on the contact record. | Text value |
| Sources - Source Code (Alias) - Custom | `user-sources-source-code` | string | Transformation for Source Code (Alias) | Sources - Source Code (Alias) - Custom. Stored on the contact record. Options come from: Transformation for Source Code (Alias). | Text value |
| Spark ID | `user-identities-sparkid` | string |  | Spark ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| State ID | `user-identities-stateid` | string |  | State ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| State Residency Status | `user-citizenship-state-residency` | string |  | State Residency Status. Stored on the contact record. | NC |
| U.S. Residency? | `user-citizenship-currently-us` | boolean | Values for [SYS] Yes/No | U.S. Residency?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| U.S. Visa Holder? | `user-citizenship-hold-visa` | boolean | Values for [SYS] Yes/No | U.S. Visa Holder?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| User - Last Updated Date | `user-updated-at` | date |  | User - Last Updated Date. Stored on the contact record. | 2026-08-15 |
| User - Optional Last Updated Date | `user-opt-updated-at` | date |  | User - Optional Last Updated Date. Stored on the contact record. | 2026-08-15 |
| User Academic Load - Full Time, Part Time | `user-education-academic-load` | string | Values for Academic Load Options | User Academic Load - Full Time, Part Time. Stored on the contact record. Options come from: Values for Academic Load Options. | Text value |
| User Require Visa? | `user-citizenship-require-visa` | boolean | Values for [SYS] Yes/No | User Require Visa?. Stored on the contact record. Options come from: Values for [SYS] Yes/No. | Yes / No |
| User Visa Type | `user-citizenship-hold-visa-type` | string | Values for [SYS] Visa types | User Visa Type. Stored on the contact record. Options come from: Values for [SYS] Visa types. | Text value |
| User's assigned territory | `user-territory` | string |  | User's assigned territory. Stored on the contact record. | Text value |
| Visa Type | `user-citizenship-visa-type` | string | Values for [SYS] Visa types | Visa Type. Stored on the contact record. Options come from: Values for [SYS] Visa types. | Text value |
| Workday ID | `user-identities-workdayid` | string |  | Workday ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Years Lived in USA | `user-citizenship-us-years` | string |  | Years Lived in USA. Stored on the contact record. | 2026 |
| Zee Mee ID | `user-identities-zeemeeid` | string |  | Zee Mee ID: external system identifier used for record matching and integrations. | 5f8a9b2c1d3e4f5a6b7c8d9e |

---