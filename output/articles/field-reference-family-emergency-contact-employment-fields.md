---
title: Field Reference: Family, Emergency Contact + Employment Fields
url: https://help.element451.com/en/articles/15902065-field-reference-family-emergency-contact-employment-fields
collection: Data Management
---

Every standard family member, emergency contact, and employment field with its slug, type, purpose, and an example value.

# Family Members (36 fields)

Page includes a Root Family Repeater Example (code sample). All fields are repeater (per-family-member) slugs ending in -\*.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **What It Does** | **Example** |
| Family - Phone Country Code \* | `user-family-phone-country-code-*` | string | Family - Phone Country Code. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 1 |
| Family - Phone Number \* | `user-family-phone-number-*` | string | Family - Phone Number. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Family - Phone Type \* | `user-family-phone-type-*` | string | Family - Phone Type. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Family Address City \* | `user-family-address-city-*` | string | Family Address City. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Raleigh |
| Family Address Country \* | `user-family-address-country-*` | string | Family Address Country. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | US |
| Family Address Location Latitude \* | `user-family-address-loc-lat-*` | float | Family Address Location Latitude. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 3.75 |
| Family Address Location Longitude \* | `user-family-address-loc-lng-*` | float | Family Address Location Longitude. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 3.75 |
| Family Address Province \* | `user-family-address-province-*` | string | Family Address Province. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Family Address State \* | `user-family-address-state-*` | string | Family Address State. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | NC |
| Family Address Street line 1 \* | `user-family-address-street-1-*` | string | Family Address Street line 1. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Family Address Street line 2 \* | `user-family-address-street-2-*` | string | Family Address Street line 2. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Family Address Street line 3 \* | `user-family-address-street-3-*` | string | Family Address Street line 3. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Family Address Type \* | `user-family-address-type-*` | string | Family Address Type. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Family Address Zipcode \* | `user-family-address-zipcode-*` | string | Family Address Zipcode. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 27601 |
| Family Address Zipcode4 \* | `user-family-address-zipcode4-*` | string | Family Address Zipcode4. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 27601 |
| Family Email \* | `user-family-email-*` | string | Family Email. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Family Employee \* | `user-family-employee-*` | boolean | Family Employee. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Family Employer \* | `user-family-employer-*` | string | Family Employer. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Family First Name \* | `user-family-first-name-*` | string | Family First Name. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Alma |
| Family Gender \* | `user-family-gender-*` | string | Family Gender. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Female |
| Family Graduated of School \* | `user-family-graduated-of-school-*` | string | Family Graduated of School. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Family Highest Degree \* | `user-family-degree-*` | string | Family Highest Degree. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Bachelor of Science |
| Family Index Weight \* | `user-family-index_weight-*` | integer | Family Index Weight. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 2 |
| Family is alive \* | `user-family-living-*` | boolean | Family is alive. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Family Is University Employee? \* | `user-family-university-employee-*` | boolean | Family Is University Employee?. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Family Job Ocupation \* | `user-family-ocupation-*` | string | Family Job Ocupation. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Family Job Title \* | `user-family-title-*` | string | Family Job Title. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Registered Nurse |
| Family Last Name \* | `user-family-last-name-*` | string | Family Last Name. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Mater |
| Family Marital Status \* | `user-family-marital_status-*` | string | Family Marital Status. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |
| Family Member - Relationship Type \* | `user-family-relationship-*` | string | Family Member - Relationship Type. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Mother |
| Family Member Element Id \* | `user-family-user_id-*` | mongoid | Family Member Element Id. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 5f8a9b2c1d3e4f5a6b7c8d9e |
| Family Middle Name \* | `user-family-middle-name-*` | string | Family Middle Name. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | J |
| Family Prefix \* | `user-family-prefix-*` | string | Family Prefix. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Ms. |
| Family Same Address? \* | `user-family-same_address-*` | boolean | Family Same Address?. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Family Suffix \* | `user-family-suffix-*` | string | Family Suffix. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Jr. |
| Family type \* | `user-family-type-*` | string | Family type. Part of a family member entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Text value |

# Emergency Contacts (44 fields)

Page includes a Root Emergency Contacts Repeater Example (code sample). Titles ending in \* are repeater (per-contact) variants.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **Data Source** | **What It Does** | **Example** |
| Emergency Contact - Address City | `user-emergency-contacts-address-city` | string |  | Emergency Contact - Address City. Part of an emergency contact entry on the contact record. | Raleigh |
| Emergency Contact - Address City \* | `user-emergency-contacts-address-city-*` | string |  | Emergency Contact - Address City. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Raleigh |
| Emergency Contact - Address Country | `user-emergency-contacts-address-country` | string | Values for [SYS] Country List (ISO 3166) | Emergency Contact - Address Country. Part of an emergency contact entry on the contact record. Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Emergency Contact - Address Country \* | `user-emergency-contacts-address-country-*` | string | Values for [SYS] Country List (ISO 3166) | Emergency Contact - Address Country. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Values for [SYS] Country List (ISO 3166). | US |
| Emergency Contact - Address County | `user-emergency-contacts-address-county` | string |  | Emergency Contact - Address County. Part of an emergency contact entry on the contact record. | 28 |
| Emergency Contact - Address County \* | `user-emergency-contacts-address-county-*` | string |  | Emergency Contact - Address County. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 28 |
| Emergency Contact - Address Province | `user-emergency-contacts-address-province` | string |  | Emergency Contact - Address Province. Part of an emergency contact entry on the contact record. | 28 |
| Emergency Contact - Address Province \* | `user-emergency-contacts-address-province-*` | string |  | Emergency Contact - Address Province. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 28 |
| Emergency Contact - Address State | `user-emergency-contacts-address-state` | string | Values for [SYS] USA State List (ISO) | Emergency Contact - Address State. Part of an emergency contact entry on the contact record. Options come from: Values for [SYS] USA State List (ISO). | NC |
| Emergency Contact - Address State \* | `user-emergency-contacts-address-state-*` | string | Values for [SYS] USA State List (ISO) | Emergency Contact - Address State. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). Options come from: Values for [SYS] USA State List (ISO). | NC |
| Emergency Contact - Address Street 1 | `user-emergency-contacts-address-street-1` | string |  | Emergency Contact - Address Street 1. Part of an emergency contact entry on the contact record. | 123 Oak Street |
| Emergency Contact - Address Street 1 \* | `user-emergency-contacts-address-street-1-*` | string |  | Emergency Contact - Address Street 1. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Emergency Contact - Address Street 2 | `user-emergency-contacts-address-street-2` | string |  | Emergency Contact - Address Street 2. Part of an emergency contact entry on the contact record. | 123 Oak Street |
| Emergency Contact - Address Street 2 \* | `user-emergency-contacts-address-street-2-*` | string |  | Emergency Contact - Address Street 2. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 123 Oak Street |
| Emergency Contact - Address Type | `user-emergency-contacts-address-type` | string |  | Emergency Contact - Address Type. Part of an emergency contact entry on the contact record. | 28 |
| Emergency Contact - Address Type \* | `user-emergency-contacts-address-type-*` | string |  | Emergency Contact - Address Type. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 28 |
| Emergency Contact - Address Zip Code | `user-emergency-contacts-address-zipcode` | string |  | Emergency Contact - Address Zip Code. Part of an emergency contact entry on the contact record. | 27601 |
| Emergency Contact - Address Zip Code \* | `user-emergency-contacts-address-zipcode-*` | string |  | Emergency Contact - Address Zip Code. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 27601 |
| Emergency Contact - Cell Phone Country Code | `user-emergency-contacts-cell-phone-country-code` | string |  | Emergency Contact - Cell Phone Country Code. Part of an emergency contact entry on the contact record. | 1 |
| Emergency Contact - Cell Phone Country Code \* | `user-emergency-contacts-cell-phone-country-code-*` | string |  | Emergency Contact - Cell Phone Country Code. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 1 |
| Emergency Contact - Cell Phone Country Code Alpha 2 | `user-emergency-contacts-cell-phone-country-alpha-2` | string |  | Emergency Contact - Cell Phone Country Code Alpha 2. Part of an emergency contact entry on the contact record. | 1 |
| Emergency Contact - Cell Phone Country Code Alpha 2 \* | `user-emergency-contacts-cell-phone-country-alpha-2-*` | string |  | Emergency Contact - Cell Phone Country Code Alpha 2. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 1 |
| Emergency Contact - Cell Phone Number | `user-emergency-contacts-cell-phone-number` | string |  | Emergency Contact - Cell Phone Number. Part of an emergency contact entry on the contact record. | (919) 555-0123 |
| Emergency Contact - Cell Phone Number \* | `user-emergency-contacts-cell-phone-number-*` | string |  | Emergency Contact - Cell Phone Number. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Emergency Contact - Cell Phone Number International | `user-emergency-contacts-cell-phone-international` | string |  | Emergency Contact - Cell Phone Number International. Part of an emergency contact entry on the contact record. | (919) 555-0123 |
| Emergency Contact - Cell Phone Number International \* | `user-emergency-contacts-cell-phone-international-*` | string |  | Emergency Contact - Cell Phone Number International. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Emergency Contact - Email | `user-emergency-contacts-email` | string |  | Emergency Contact - Email. Part of an emergency contact entry on the contact record. | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Emergency Contact - Email \* | `user-emergency-contacts-email-*` | string |  | Emergency Contact - Email. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | [alma.mater@example.com](mailto:alma.mater@example.com) |
| Emergency Contact - First Name | `user-emergency-contacts-first-name` | string |  | Emergency Contact - First Name. Part of an emergency contact entry on the contact record. | Alma |
| Emergency Contact - First Name \* | `user-emergency-contacts-first-name-*` | string |  | Emergency Contact - First Name. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Alma |
| Emergency Contact - Home Phone Country Code | `user-emergency-contacts-home-phone-country-code` | string |  | Emergency Contact - Home Phone Country Code. Part of an emergency contact entry on the contact record. | 1 |
| Emergency Contact - Home Phone Country Code \* | `user-emergency-contacts-home-phone-country-code-*` | string |  | Emergency Contact - Home Phone Country Code. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 1 |
| Emergency Contact - Home Phone Country Code Alpha 2 | `user-emergency-contacts-home-phone-country-alpha-2` | string |  | Emergency Contact - Home Phone Country Code Alpha 2. Part of an emergency contact entry on the contact record. | 1 |
| Emergency Contact - Home Phone Country Code Alpha 2 \* | `user-emergency-contacts-home-phone-country-alpha-2-*` | string |  | Emergency Contact - Home Phone Country Code Alpha 2. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | 1 |
| Emergency Contact - Home Phone Number | `user-emergency-contacts-home-phone-number` | string |  | Emergency Contact - Home Phone Number. Part of an emergency contact entry on the contact record. | (919) 555-0123 |
| Emergency Contact - Home Phone Number \* | `user-emergency-contacts-home-phone-number-*` | string |  | Emergency Contact - Home Phone Number. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Emergency Contact - Home Phone Number International | `user-emergency-contacts-home-phone-international` | string |  | Emergency Contact - Home Phone Number International. Part of an emergency contact entry on the contact record. | (919) 555-0123 |
| Emergency Contact - Home Phone Number International \* | `user-emergency-contacts-home-phone-international-*` | string |  | Emergency Contact - Home Phone Number International. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | (919) 555-0123 |
| Emergency Contact - Is Primary | `user-emergency-contacts-is-primary` | boolean |  | Emergency Contact - Is Primary. Part of an emergency contact entry on the contact record. | true / false |
| Emergency Contact - Is Primary \* | `user-emergency-contacts-is-primary-*` | boolean |  | Emergency Contact - Is Primary. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | true / false |
| Emergency Contact - Last Name | `user-emergency-contacts-last-name` | string |  | Emergency Contact - Last Name. Part of an emergency contact entry on the contact record. | Mater |
| Emergency Contact - Last Name \* | `user-emergency-contacts-last-name-*` | string |  | Emergency Contact - Last Name. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Mater |
| Emergency Contact - Relationship | `user-emergency-contacts-relationship` | string |  | Emergency Contact - Relationship. Part of an emergency contact entry on the contact record. | Mother |
| Emergency Contact - Relationship \* | `user-emergency-contacts-relationship-*` | string |  | Emergency Contact - Relationship. Part of an emergency contact entry on the contact record. Repeater variant: \* targets a specific or any position in the list (1, 2, 3...). | Mother |

# Employment (14 fields)

Note: Does not require a root item when using an inline template.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field Name** | **Slug** | **Type** | **What It Does** | **Example** |
| Employee business 1 | `user-employment-employees-1-business` | string | Employee business 1. Part of an employment entry on the contact record. | Registered Nurse |
| Employee business 2 | `user-employment-employees-2-business` | string | Employee business 2. Part of an employment entry on the contact record. | Registered Nurse |
| Employee company name 1 | `user-employment-employees-1-companyname` | string | Employee company name 1. Part of an employment entry on the contact record. | Text value |
| Employee company name 2 | `user-employment-employees-2-companyname` | string | Employee company name 2. Part of an employment entry on the contact record. | Text value |
| Employee Employment Status 1 | `user-employment-employees-1-status` | string | Employee Employment Status 1. Part of an employment entry on the contact record. | Text value |
| Employee Employment Status 2 | `user-employment-employees-2-status` | string | Employee Employment Status 2. Part of an employment entry on the contact record. | Text value |
| Employee End Date 1 | `user-employment-employees-1-end_date` | date | Employee End Date 1. Part of an employment entry on the contact record. | 2026-08-15 |
| Employee End Date 2 | `user-employment-employees-2-end_date` | date | Employee End Date 2. Part of an employment entry on the contact record. | 2026-08-15 |
| Employee position 1 | `user-employment-employees-1-position` | string | Employee position 1. Part of an employment entry on the contact record. | Text value |
| Employee position 2 | `user-employment-employees-2-position` | string | Employee position 2. Part of an employment entry on the contact record. | Text value |
| Employee reimbursement 1 | `user-employment-employees-1-reimbursement` | string | Employee reimbursement 1. Part of an employment entry on the contact record. | Text value |
| Employee reimbursement 2 | `user-employment-employees-2-reimbursement` | string | Employee reimbursement 2. Part of an employment entry on the contact record. | Text value |
| Employee Start Date 1 | `user-employment-employees-1-start_date` | date | Employee Start Date 1. Part of an employment entry on the contact record. | 2026-08-15 |
| Employee Start Date 2 | `user-employment-employees-2-start_date` | date | Employee Start Date 2. Part of an employment entry on the contact record. | 2026-08-15 |

---