---
title: Campaign Tokens
url: https://help.element451.com/en/articles/1524113-campaign-tokens
collection: Campaigns
---

Learn how to personalize messages with Tokens and the different tokens available to use.

# Overview

Tokens in Element451 are a powerful feature that allows you to generate personalized, dynamic content for your campaigns. They act as placeholders in your messages, which are replaced with actual data from your contacts’ records when the message is sent.

## What Are Tokens?

Tokens are essentially small bits of code that represent placeholders for personalized content. For example, you might see a token like `[user:intended_major]` in your message. When the recipient receives the message, this token will be replaced with the specific data from their contact record.

## How Tokens Work

When you include a token in your message, Element451 automatically pulls the relevant information from the contact’s record. This means each recipient gets a message tailored to their specific information.

For example, if Alma has an intended major in Biology and Annie has an intended major in Accounting, `[user:intended_major]` would be replaced with Biology in the message for Alma and Accounting in the message for Annie.

---

# Token Anatomy

Tokens in Element451 follow a specific structure:

`[type:method,param=value,param=value,...]`

* **type**: Identifies the token provider (e.g., user, custom, event)
* **method**: Specifies the required method from the provider (e.g., user:{mapping})
* **param**: Name of the parameter recognized by the chosen method
* **value**: Value assigned to the parameter

---

# Parameters: Modifying + Formatting Tokens

Tokens can be customized using parameters to modify their output, format dates, reference past or future dates, and display multiple values in a structured list. Below are the key ways you can enhance your tokens:

* **Global Parameters** – Modify how any token behaves, such as setting a fallback value, adding prefixes or suffixes, or altering capitalization.
* **Formatting Date Outputs** – Control how dates are displayed using PHP date formats, ensuring consistency.
* **Referencing Future or Past Dates** – Use the `offset` parameter to dynamically adjust dates based on when your campaign is sent.
* **Displaying Lists with `content:list`** – Format multi-select and checkbox responses into easy-to-read lists instead of plain text.

Each section below includes examples to show how these parameters work in practice.

## Global Parameters

Global parameters can be used with any token. They modify how the token behaves or displays its value.

* **fallback**

  + **Description**: Defines the default value if the token value cannot be found.
  + **Example**: [user:first\_name,fallback=Friend] => “Alma” or “Student”
* **prefix**

  + **Description**: Adds a prefix if the token value is not empty.
  + **Example**: [user:first\_name,prefix=Dear] => “Dear Alma”
* **suffix**

  + **Description**: Adds a suffix if the token value is not empty.
  + **Example**: [user:first\_name,suffix=.] => “Alma.”
* **alter**

  + **Description**: Transforms the string token value.
  + **Options**:

    - uppercase: Converts to uppercase
    - lowercase: Converts to lowercase
    - ucfirst: Capitalizes the first letter
    - slug: Converts to a slug (replaces non-alphanumeric characters with an underscore \_)
  + **Examples**:

    - [user:first\_name,alter=uppercase] => “ALMA”
    - [user:first\_name,alter=lowercase] => “alma”
    - [user:first\_name,alter=ucfirst] => “Alma”
    - [user:email,alter=slug] => “alma\_example\_com”

## Formatting Date Outputs

When using tokens with dates, you can control how the date is displayed by adding a `format` parameter. The format follows PHP’s date formatting rules. Below are some common formatting options you can use:

### Common Date Formats + Outputs

* `Y` – Full year (4 digits)

  + Example: 2025
* `y` – Short year (2 digits)

  + Example: 25
* `F` – Full month name

  + Example: February
* `M` – Short month name

  + Example: Feb
* `m` – Numeric month (leading zero)

  + Example: 02
* `n` – Numeric month (no leading zero)

  + Example: 2
* `d` – Day of the month (leading zero)

  + Example: 28
* `j` – Day of the month (no leading zero)

  + Example: 28
* `D` – Short weekday name

  + Example: Fri
* `l` – Full weekday name

  + Example: Friday
* `H` – 24-hour format (leading zero)

  + Example: 14
* `h` – 12-hour format (leading zero)

  + Example: 02
* `i` – Minutes (leading zero)

  + Example: 30
* `s` – Seconds (leading zero)

  + Example: 45
* `A` – AM/PM (uppercase)

  + Example: PM
* `a` – AM/PM (lowercase)

  + Example: pm

### Example 1

Let's say you store an enrollment deadline as a custom field. When referencing that field in a token, you can add date format parameters to control the output.

`[user:user-custom-elementu-enrollment-deadline, format="D, d M Y"]`

Using the token above with the `format="D, d M Y"` parameter, if the stored date is March 15, 2025, the output would be **Sat, 15 Mar 2025**.

### Example 2

In this example, we are using today's date, adding 7 days to it (so we can reference a deadline 7 days from when the email is sent (we explain using the offset parameter in the next section), and formatting the date.

`[date:now, offset=+7d, format="l, F j, Y"]`

Using the token above with the `format="l, F j, Y"` parameter, if today's date is February 20, 2025, the output would be **Thursday, February 27, 2025**.

## Referencing a Future or Past Date Using Date Tokens

When using date tokens, you can adjust the date dynamically by adding an `offset` parameter. This allows you to reference a future or past date when your campaign is sent.

Example: `[date:now,offset=+7d,format="D, d M Y"]`

In this example:

* now represents the current date/time.
* offset=+7d adds 7 days to the current date.
* format="D, d M Y" ensures the date is displayed correctly (e.g., “Mon, 12 Feb 2025”).

**Adjusting Dates:**

* You can use **+** to reference a future date or **-** to reference a past date.

**Examples:**

• offset=-3d → Displays the date **3 days ago**.

• offset=+1m → Displays the date **one month from today**.

**Available Offset Units:**

* Years: y
* Months: m
* Days: d
* Hours: h
* Minutes: I
* Seconds: s

💡 **Tip:** Always include the format parameter to ensure the date displays as expected. You can explore date formatting parameters in the section above this one.

## Display Multiple Values as a Formatted List (content:list)

When displaying data collected from checkbox/multi-select fields in your Campaigns, use the `content:list` token to create organized, easy-to-read lists.

⚠️ **Important Note Regarding Data with Commas (e.g., 5,000)**

The `content:list` token cannot be used with values that contain commas. For example, if your data includes numbers like "5,000" or "10,000", the token will treat these commas as separators and split the numbers incorrectly on separate lines. If your data contains commas, you must modify the data to remove them before using this token.

## About the `content:list` Token

The `content:list` token helps you display multiple answers from checkboxes or multi-select fields in a nice-looking list format in your emails. For example, if students select multiple courses they're interested in, this token can display them as a neat bulleted list instead of a string of text with commas.

**This token requires four pieces, with options for additional parameters based on your specific needs:**

1. `source` - Can be a custom field mapping slug, a token, or a custom field containing tokens (see detailed options below)
2. `template` - Must be set to `"<li>%1$s</li>"` (this formats each item as a list entry)
3. `container` - The type of list you want: `ul` creates bullet points, `ol` creates numbered items (1, 2, 3...)
4. `delimiter` - Default is comma (`,`), but can be customized based on your data format

## Ways to Use the `content:list` Token

1. **`Source` = Another Token**  
   When using a token as the source, the output of that token will be split by the "delimiter" parameter and turned into list items.

   1. Custom field tokens automatically return the names from the data source, not the raw value.
   2. If the field contains an array, the output will be a comma-separated string of those names.
   3. You could point to a string field. For example, if the token pointed to a custom field that shows the string "AL|AK|AZ|AR," you could pass `delimiter="|"` it to split those values.  
      ​

      ```
      [content:list,source="[user:user-custom-field-name]",template="<li>%1$s</li>",container="ul",delimiter=","]
      ```
2. **`Source` = A Custom Field Slug**  
   When using a custom field slug directly, by default, the raw value of the custom field will be turned into a list of items.

   1. If the raw value of the custom field is a string, it will be split by the "delimiter" parameter first.
   2. If you want to display the names from the data source instead of the raw values, you should add an `output=name` parameter.
   3. If the raw value contains tokens, those tokens will be replaced before building the list.  
      ​

      ```
      [content:list,source="user-selected-courses",template="<li>%1$s</li>",container="ul",delimiter=",",output=name]
      ```

---

# Using Tokens in a Campaign

Including a token in your campaign is simple. You can insert a token using the **formatting toolbar** within the campaign editor or **manually type** your token text enclosed in brackets [ ] in the message content.

However, **we recommend inserting the token using the toolbar** instead of typing it manually. Once you’ve added the token to the campaign, you can modify it using [parameters](#h_8b1d74e48c) if needed.

## Where + How to Use Tokens in Campaigns

### Email

* Subject Line

  [![](https://downloads.intercomcdn.com/i/o/876561078/4bb57629244791c09b0023dd/Campaigns+-+Tokens+-+Email+Subject+Line.png?expires=1784333700&signature=9e4ee0eefba5be89a6080723ba2b01c52027fb939524f3839df7da1b72f2d5b8&req=fCchE89%2FnYZXFb4f3HP0gDxNBPOCivzS%2FGQqFimoZnrhKJ0yLo%2FThGqdLz50%0ArdU%3D%0A)](https://downloads.intercomcdn.com/i/o/876561078/4bb57629244791c09b0023dd/Campaigns+-+Tokens+-+Email+Subject+Line.png?expires=1784333700&signature=9e4ee0eefba5be89a6080723ba2b01c52027fb939524f3839df7da1b72f2d5b8&req=fCchE89%2FnYZXFb4f3HP0gDxNBPOCivzS%2FGQqFimoZnrhKJ0yLo%2FThGqdLz50%0ArdU%3D%0A)
* Preview Text

  [![](https://downloads.intercomcdn.com/i/o/1195823763/145841e08cb6294effb39b33/Campaigns%2B-%2BTokens%2B-%2BEmail%2B-%2BPreview%2BText.png?expires=1784333700&signature=53904865e25bcb87b9a8f797ea13dadcff4f05a2afa7908ca3a18ba8ef1143a4&req=dSEuE8F8noZZWvMW1HO4zbGx4XKgIjD%2BdXf6PmNPEAntniIZaCav5SoQRN80%0AYX8n%0A)](https://downloads.intercomcdn.com/i/o/1195823763/145841e08cb6294effb39b33/Campaigns%2B-%2BTokens%2B-%2BEmail%2B-%2BPreview%2BText.png?expires=1784333700&signature=53904865e25bcb87b9a8f797ea13dadcff4f05a2afa7908ca3a18ba8ef1143a4&req=dSEuE8F8noZZWvMW1HO4zbGx4XKgIjD%2BdXf6PmNPEAntniIZaCav5SoQRN80%0AYX8n%0A)
* Body (highlight the text and click the **Insert** **Token** icon)

  [![](https://downloads.intercomcdn.com/i/o/1195825003/79aff08ff55fc0ff2ef9e9d9/Campaigns%2B-%2BTokens%2B-%2BEmail%2B-%2BBody.png?expires=1784333700&signature=4713f3606e76ba34b5dbbc2a98ba98049a7a3d5ec6f61ba6b62661d3dc8b8e16&req=dSEuE8F8mIFfWvMW1HO4zSgZezJ3rdYuN6X%2B6t62xRjogIRD%2B6PiMXbUUcP%2F%0AQF08%0A)](https://downloads.intercomcdn.com/i/o/1195825003/79aff08ff55fc0ff2ef9e9d9/Campaigns%2B-%2BTokens%2B-%2BEmail%2B-%2BBody.png?expires=1784333700&signature=4713f3606e76ba34b5dbbc2a98ba98049a7a3d5ec6f61ba6b62661d3dc8b8e16&req=dSEuE8F8mIFfWvMW1HO4zSgZezJ3rdYuN6X%2B6t62xRjogIRD%2B6PiMXbUUcP%2F%0AQF08%0A)

  [![](https://downloads.intercomcdn.com/i/o/1195825230/47148bc5c169158daa1041a4/Campaigns%2B-%2BTokens%2B-%2BEmail%2BBody.png?expires=1784333700&signature=6ca49d76306338251aebf047723dd01c9d0250392ba95eb3c889755245a15902&req=dSEuE8F8mINcWfMW1HO4zUAgSnzMWYB%2FBXv4uTblm0GEqw1XnEVraIWWXRAN%0ASKS0%0A)](https://downloads.intercomcdn.com/i/o/1195825230/47148bc5c169158daa1041a4/Campaigns%2B-%2BTokens%2B-%2BEmail%2BBody.png?expires=1784333700&signature=6ca49d76306338251aebf047723dd01c9d0250392ba95eb3c889755245a15902&req=dSEuE8F8mINcWfMW1HO4zUAgSnzMWYB%2FBXv4uTblm0GEqw1XnEVraIWWXRAN%0ASKS0%0A)

### SMS

* Body

  [![](https://downloads.intercomcdn.com/i/o/1195826005/b54d4ee18b82f522becf7a90/Campaigns%2B-%2BTokens%2B-%2BSMS.png?expires=1784333700&signature=5caffbb26196413e52a90fb43a9ae2d1be5d485fe8ebbc951f3db64eed9842e3&req=dSEuE8F8m4FfXPMW1HO4zYp6e7g%2FfrmsqfW86yC5QdA9ZG5PY77Y00qIxvW%2B%0AevaE%0A)](https://downloads.intercomcdn.com/i/o/1195826005/b54d4ee18b82f522becf7a90/Campaigns%2B-%2BTokens%2B-%2BSMS.png?expires=1784333700&signature=5caffbb26196413e52a90fb43a9ae2d1be5d485fe8ebbc951f3db64eed9842e3&req=dSEuE8F8m4FfXPMW1HO4zYp6e7g%2FfrmsqfW86yC5QdA9ZG5PY77Y00qIxvW%2B%0AevaE%0A)

### Push Notification

* Title
* Content
* Link  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1195826598/28c2e7c518612e6dd7c862e6/Campaigns%2B%2BTokens%2B%2BPush-402x.png?expires=1784333700&signature=25ed4d60ab8e5e9edd2c4fe9eccb317a674075cb36e2dcc19d390c91bb5b30a0&req=dSEuE8F8m4RWUfMW1HO4zZ1fgqnEfiDNqbvu1KH6r2cO5wLGrYvyCraQ7P%2Fm%0Aw%2FvK%0A)](https://downloads.intercomcdn.com/i/o/1195826598/28c2e7c518612e6dd7c862e6/Campaigns%2B%2BTokens%2B%2BPush-402x.png?expires=1784333700&signature=25ed4d60ab8e5e9edd2c4fe9eccb317a674075cb36e2dcc19d390c91bb5b30a0&req=dSEuE8F8m4RWUfMW1HO4zZ1fgqnEfiDNqbvu1KH6r2cO5wLGrYvyCraQ7P%2Fm%0Aw%2FvK%0A)

For more information on push notifications, [click here](https://help.element451.com/en/articles/9888911-studenthub-push-notifications).

---

# List of Available Tokens

## System Field Tokens

### Address

|  |  |
| --- | --- |
| Home City | [address:addresses\_home\_city] |
| Home Country | [address:addresses\_home\_country] |
| Home Addresses | [address:addresses\_home\_full] |
| Home State | [address:addresses\_home\_state] |
| Home Street1 | [address:addresses\_home\_street1] |
| Home Street2 | [address:addresses\_home\_street2] |
| Home Street3 | [address:addresses\_home\_street3] |
| Home ZipCode | [address:addresses\_home\_zipcode] |
| Mailing City | [address:addresses\_mailing\_city] |
| Mailing Country | [address:addresses\_mailing\_country] |
| Mailing | [address:addresses\_mailing\_full] |
| Mailing State | [address:addresses\_mailing\_state] |
| Mailing Street1 | [address:addresses\_mailing\_street1] |
| Mailing Street2 | [address:addresses\_mailing\_street2] |
| Mailing Street3 | [address:addresses\_mailing\_street3] |
| Mailing ZipCode | [address:addresses\_mailing\_zipcode] |

Home City [address:addresses\_home\_city]

Home Country [address:addresses\_home\_country]

Home Addresses [address:addresses\_home\_full]

Home State [address:addresses\_home\_state]

Home Street1 [address:addresses\_home\_street1]

Home Street2 [address:addresses\_home\_street2]

Home Street3 [address:addresses\_home\_street3]

Home ZipCode [address:addresses\_home\_zipcode]

Mailing City [address:addresses\_mailing\_city]

Mailing Country [address:addresses\_mailing\_country]

Mailing [address:addresses\_mailing\_full]

Mailing State [address:addresses\_mailing\_state]

Mailing Street1 [address:addresses\_mailing\_street1]

Mailing Street2 [address:addresses\_mailing\_street2]

Mailing Street3 [address:addresses\_mailing\_street3]

Mailing ZipCode [address:addresses\_mailing\_zipcode]

### Application

|  |  |
| --- | --- |
| Application Portal URL | [application:base\_url] |
| Application Login Token | [application:login\_token] |
| Application Login URL | [application:login\_url] |
| Application Name | [application:name] |
| Application Fee | [application:payment\_amount] |
| Application Fee Currency | [application:payment\_currency] |

### Appointment

|  |  |
| --- | --- |
| Next Appointment Assignee | [appointment:next\_appointment\_assignee] |
| Next Appointment Date/Time | [appointment:next\_appointment\_datetime] |
| Next Appointment Type | [appointment:next\_appointment\_type] |
| Next Appointment Url | [appointment:next\_appointment\_url] |
| Next Appointment Avail Title | [appointment:next\_appointment\_availability\_title] |

### Client (Institution)

|  |  |
| --- | --- |
| Institution Primary Color | [client:color\_primary] |
| Institution Secondary Color | [client:color\_secondary] |
| Institution Contact Information | [client:contact] |
| Institution Logo | [client:email\_logo] |
| Institution Name | [client:name] |
| Institution Signatures | [client:signatures] |

### Content

|  |  |
| --- | --- |
| Formula | [content:formula] |
| List\* | [content:list] |

### Course

When inserting a course token, you'll be prompted to select the specific course and section the token should reference. Section lists are filtered to the selected course so you can quickly find the right one.

|  |  |  |
| --- | --- | --- |
| Course Name | Course | [course:name] |
| Course Code | Course | [course:code] |
| Course Credits | Course | [course:credits] |
| Course Department | Course | [course:department] |
| Section Code | Section | [course:section\_code] |
| Section Term | Section | [course:section\_term] |
| Section Instructor | Section | [course:section\_instructor] |
| Section Instructor Email | Section | [course:section\_instructor\_email] |
| Section Times | Section | [course:section\_times]  *Renders as a table of all scheduled day and time entries for that section* |
| Enrollment Status | Enrollment | [course:enrollment\_status] |
| Grade Risk | Enrollment | [course:enrollment\_grade\_risk] |
| Current Grade (Text) | Enrollment | [course:enrollment\_current\_grade\_text] |
| Current Grade (Number) | Enrollment | ([course:enrollment\_current\_grade\_number]) |
| Final Grade (Text) | Enrollment | [course:enrollment\_final\_grade\_text] |
| Final Grade (Number) | Enrollment | [course:enrollment\_final\_grade\_number] |
| Last LMS Activity | Enrollment | [course:enrollment\_last\_lms\_activity] |
| Last Attended Date | Enrollment | [course:enrollment\_last\_attended\_date] |

### Custom

|  |  |
| --- | --- |
| Email View in Browser URL | [custom:online-view] |
| Unsubscribe URL | [custom:unsubscribe] |

### Date

|  |  |
| --- | --- |
| Current day | [date:day] |
| Current hour | [date:hour] |
| Current minute | [date:minute] |
| Current month | [date:month] |
| Current date and time | [date:now] |
| Current second | [date:second] |
| Current year | [date:year] |

### Document

|  |  |
| --- | --- |
| Related folder | [document:folder] |
| Original filename | [document:original\_file] |
| Document type | [document:type] |

### Event

Note: When emailing event **registrants**, we recommend using the [messaging feature within the Events module](https://help.element451.com/en/articles/6067308-tokens-for-events-messages) and using the event tokens specific to that feature.

|  |  |
| --- | --- |
| Event Categories | [event:categories] |
| Event Description | [event:description] |
| Event End Date | [event:end\_date] |
| Event End Time | [event:end\_time] |
| Event Link | [event:event\_link] |
| Event Image | [event:image] |
| Event Location | [event:location] |
| Event Name | [event:name] |
| Event Portal URL | [event:site\_url] |
| Event Start Date | [event:start\_date] |
| Event Start Time | [event:start\_time] |
| Event Timezone | [event:timezone] |
| Event Type | [event:type] |
| Event URL | [event:url] |
| Venue Address | [event:venue\_address] |
| Venue Address 2 | [event:venue\_address2] |
| Venue Building | [event:venue\_building] |
| Venue City | [event:venue\_city] |
| Venue Country | [event:venue\_country] |
| Venue Name | [event:venue\_name] |
| Venue Room | [event:venue\_room] |
| Venue State | [event:venue\_state] |
| Venue Zip | [event:venue\_zip] |

### File

|  |  |
| --- | --- |
| File extension | [file:extension] |
| File guid | [file:guid] |
| File guid (short) | [file:guidShort] |
| File name | [file:name] |
| File size (in bytes) | [file:size] |

### Form

|  |  |
| --- | --- |
| Form Login Token | [form:login\_token] |
| Form Login URL | [form:login\_url] |

### Identity

|  |  |
| --- | --- |
| School ID | [identity:school] |

### Import + Export

|  |  |
| --- | --- |
| ImportExport task name | [ie\_task:name] |
| ImportExport task result error | [ie\_task:result\_error] |
| ImportExport task result stats count | [ie\_task:result\_stats\_count] |
| ImportExport task result stats created | [ie\_task:result\_stats\_created] |
| ImportExport task result stats exported | [ie\_task:result\_stats\_exported] |
| ImportExport task result stats failed | [ie\_task:result\_stats\_failed] |
| ImportExport task result stats skipped | [ie\_task:result\_stats\_skipped] |
| ImportExport task result stats unchanged | [ie\_task:result\_stats\_unchanged] |
| ImportExport task result stats updated | [ie\_task:result\_stats\_updated] |
| ImportExport task result stats worker | [ie\_task:result\_stats\_worker] |
| ImportExport task result stats worker\_done | [ie\_task:result\_stats\_worker\_done] |
| ImportExport task result warnings | [ie\_task:result\_warnings] |

### Info Request

|  |  |
| --- | --- |
| Recommender First Name | [inforequest:first\_name] |
| Recommender Last Name | [inforequest:last\_name] |

### Landing Page

|  |  |
| --- | --- |
| Landing Page Token | [landingpage:login\_token] |

### Link

|  |  |
| --- | --- |
| Link - Email | [link:email] |
| Link - URL | [link:link] |

### Microsite

|  |  |
| --- | --- |
| Site451 Login Token | [microsite:login\_token] |
| Site451 Login URL | [microsite:login\_url] |

### Survey

|  |  |
| --- | --- |
| Survey Description | [survey:description] |
| Survey End Date | [survey:end] |
| Survey Name | [survey:name] |
| Survey Start Date | [survey:start] |
| Survey Magic Link | [survey:user\_magic\_link] |

### Task

|  |  |
| --- | --- |
| Next Task Assignee | [task:next\_task\_assigned\_to] |
| Next Task Description | [task:next\_task\_description] |
| Next Task Name | [task:next\_task\_name] |
| Next Task Type | [task:next\_task\_type] |

### User

|  |  |
| --- | --- |
| Act ID | [user:actid] |
| Active Campus | [user:active\_campus] |
| Active Campus - Address | [user:active\_campus\_address] |
| Active Campus - City | [user:active\_campus\_city] |
| Active Campus - Country | [user:active\_campus\_country] |
| Active Campus - State | [user:active\_campus\_state] |
| Active Campus - Zip | [user:active\_campus\_zip] |
| Active Degree | [user:active\_degree] |
| Active Major | [user:active\_major] |
| Active Student Type | [user:active\_student\_type] |
| Active Term | [user:active\_term] |
| Anthology ID | [user:anthologyid] |
| Campus | [user\_application:campus] |
| Decision Release Date | [user\_application:decision\_released\_at] |
| Degree | [user\_application:degree] |
| Major | [user\_application:major] |
| Registration Id | [user\_application:registration\_id] |
| Status | [user\_application:status] |
| Submitted Date | [user\_application:submitted\_time] |
| Term | [user\_application:term] |
| Assignee Email | [user:assignee\_email] |
| Assignee First Name | [user:assignee\_first\_name] |
| Assignee Last Name | [user:assignee\_last\_name] |
| Assignee Title | [user:assignee\_title] |
| Campus Nexus ID | [user:campusnexusid] |
| Cas ID | [user:casid] |
| CFNC ID | [user:cfncid] |
| COALITION ID | [user:coalitionid] |
| College Area of Study | [user:college\_area\_of\_study] |
| College Board ID | [user:collegeboardid] |
| COMMON APP ID | [user:commonappid] |
| COMMON APP TRANSFER ID | [user:commonapptransferid] |
| Checklist | [user\_decision:checklist] |
| Date of Birth | [user:dob] |
| EAB ID | [user:eabid] |
| Email Address | [user:email\_address] |
| EMAIL ID | [user:emailid] |
| Encoura ID | [user:encouraid] |
| Ethos ID | [user:ethosid] |
| First Name | [user:first\_name] |
| Former Last Name | [user:former\_last\_name] |
| Pronoun (ex. his, her, their ...) | [user:gender\_pronoun] |
| Guardian Emails | [user:guardian\_emails] |
| Historic ID | [user:historicid] |
| High School Counselor Emails | [user:hs\_counselor\_emails] |
| High School Counselor Marketing ID | [user:hscmid] |
| User ID | [user:id] |
| Identity Emails | [user:identity\_emails] |
| Intended Major | [user:intended\_major] |
| Intended Term | [user:intended\_term] |
| Last Login Date | [user:last\_login] |
| Last Name | [user:last\_name] |
| Middle name | [user:middle\_name] |
| NC Student Number ID | [user:ncstudentnumberid] |
| Niche ID | [user:nicheid] |
| PARCHMENT ID | [user:parchmentid] |
| Phone Cell International | [user:phone\_cell\_international] |
| Phone Cell Number | [user:phone\_cell\_number] |
| Populi ID | [user:populiid] |
| Preferred Name | [user:preferred\_name] |
| Name Prefix | [user:prefix\_name] |
| RCN ID | [user:rcnid] |
| Relationship Emails | [user\_related:emails] |
| Salesforce ID | [user:salesforceid] |
| School Email | [user:schoolemail] |
| SCHOOL ID | [user:schoolid] |
| SCOIR ID | [user:scoirid] |
| SPARK ID | [user:sparkid] |
| STATE ID | [user:stateid] |
| Name Suffix | [user:suffix\_name] |
| Zee Mee ID | [user:zeemeeid] |

\*Denotes a token that has additional details above in the Parameters: Modifying + Formatting Tokens section.

## Custom Field Tokens

You can manually create tokens for any of your custom data fields. Follow the process outlined below to create one:

## How to Create a Custom Field Token

1. Navigate to Data + Automations > Field Management
2. Click on Custom Fields in the left-hand menu
3. Locate your custom field and the **slug** for that field. You will use the slug to create the token.
4. Take the token, add "**user:**" to the front of it, and put it in brackets. ***Be sure that the entire token is in lowercase.***

   * Example 1:

     + Slug: user-custom-demo1-dietary-restrictions
     + Token: [user:user-custom-demo1-dietary-restrictions]
   * Example 2:

     + Slug: user-custom-demo1-dietary-explain
     + Token: [user:user-custom-demo1-dietary-explain]

[![](https://downloads.intercomcdn.com/i/o/327859738/fa29068831e4267661edb93c/Screen+Shot+2021-04-22+at+4.35.34+PM.png?expires=1784333700&signature=e97dd5508c3d31819ec0cc95de22bc09e94c55662cbdc4bcd7d73f12ba93f51b&req=dyIgHsx3moJXFb4f3HP0gEbPQaPrWTtVsXm1nS0YOv65Zyka2W1VCSxJdhp5%0A5fQOcs%2FMePsVIw17fQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/327859738/fa29068831e4267661edb93c/Screen+Shot+2021-04-22+at+4.35.34+PM.png?expires=1784333700&signature=e97dd5508c3d31819ec0cc95de22bc09e94c55662cbdc4bcd7d73f12ba93f51b&req=dyIgHsx3moJXFb4f3HP0gEbPQaPrWTtVsXm1nS0YOv65Zyka2W1VCSxJdhp5%0A5fQOcs%2FMePsVIw17fQ%3D%3D%0A)

#

---

# Testing Token Content in Campaigns

![](https://downloads.intercomcdn.com/i/o/1065473500/ae2a87605d3d50fc22d8c3e4/Important+-+Orng.png?expires=1784430000&signature=48ffd941808260f1a4472e0afb80529268dfedcb417050b0012c15c0d14514aa&req=dSAhE815noRfWfMW3Hu4gYcsgJ29qaJ8RupzkDmsGpObFfdfVUAbvYc6sOej%0A%2FA%3D%3D%0A) To properly test token content in a campaign, you must use the “send to segment” option. If you don’t have a segment comprised of test users, you should create one. This approach is necessary because tokens (and the data they represent) are linked to specific individual records. Therefore, if you test your message by manually entering an email address or phone number, the tokens will not be replaced with actual data.

[Explore More: Testing Campaigns →](https://help.element451.com/en/articles/8901250-testing-previewing-campaigns)

---

# Link Tokens with Tracking Information

You can generate links using a token with various customizable properties, making it perfect for tracking user interactions and tailoring link behavior. Here are the key parameters you can configure:

## Parameter Options + Examples

* **url**: The web address you want the link to go to. (Required)
* **tracking**: Whether to track link clicks or not. (Required)
* **eid**: Option to add eid to tracked links. (Optional)
* **display\_text**: Custom text to display for the link. (Optional)
* **sms\_tracking:** Shorten and track link, only for SMS (Optional)

  + When sending SMS messages, you can choose whether to shorten and track links by selecting “Yes” or “No” for this setting. Use “No” if you’re including links with unique formatting or characters that could be altered by the shortening process. This ensures your recipients can access the intended URL without issues. A common example is Microsoft Bookings links, which often include special characters like “@” that may break when shortened.

Example 1: Redirects to: [www.google.com/?eid=Kduwsq234](http://www.google.com/?eid=Kduwsq234)

```
[link:link,url=www.google.com,tracking=true]=> "<ahref='element.tracking/Wsdweaqw'>click here</a>"
```

Example 2: Redirects to: [www.google.com](http://www.google.com)

```
[link:link,url=www.google.com,tracking=true,eid=false]  
=> "<ahref='element.tracking/Wsdweaqw'>click here</a>"
```

Example 3: Redirects to: [www.google.com/?eid=Kduwsq234](http://www.google.com/?eid=Kduwsq234)

```
[link:link,url=www.google.com,tracking=true,display_text=click here] => "<a href='element.tracking/Wsdweaqw'>click here</a>"
```

Example 4: SMS tracking

```
[link:link,url=https://www.google.com,sms_tracking=true] =>  
https://elmt.link/abcdefg
```

## **Tracking with UTM Parameters**

UTM parameters can be added to token URLs in two ways.

### Adding UTMs via Communication Settings

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308087385/cef0ec7c61d8339b70d76c6cb0ad/Screenshot%2B2026-04-22%2Bat%2B2_24_21-E2-80-AFPM.png?expires=1784333700&signature=ec7318775fe5a48d3341709ddbc8ed07ad2940ca7cb09204d6ba264eb685a11f&req=diMnHsl2moJXXPMW1HO4zUIP8R%2FLeT2tmX6fHBsj3nwSXYpwDT1%2FkEz1na6v%0AD%2B4wJEVQiY7kK7L49pg%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/2308087385/cef0ec7c61d8339b70d76c6cb0ad/Screenshot%2B2026-04-22%2Bat%2B2_24_21-E2-80-AFPM.png?expires=1784333700&signature=ec7318775fe5a48d3341709ddbc8ed07ad2940ca7cb09204d6ba264eb685a11f&req=diMnHsl2moJXXPMW1HO4zUIP8R%2FLeT2tmX6fHBsj3nwSXYpwDT1%2FkEz1na6v%0AD%2B4wJEVQiY7kK7L49pg%3D%0A)

UTM values added to the "UTM Settings" section of a Campaign's Communication Settings will be applied to all links for each medium, including SMS shortlinks.

A Campaign with UTMs of utm\_source=element451, utm\_medium=email and utm\_campaign=apply\_push would

**Email Example:**

```
[link:link,url=www.google.com,tracking=true,display_text=click here]  
=> becomes this link:  
https://www.google.com?utm_source=element451&utm_medium=email&utm_campaign=apply_push  
=> which is added to the email HTML as:
```

**SMS Example:**

```
[link:link,url=https://www.google.com,sms_tracking=true]  
=> becomes this link:  
https://www.google.com?utm_source=element451&utm_medium=email&utm_campaign=apply_push  
=> which is added to the SMS message as:  
https://elmt.link/abcdefg
```

### Hard-coding UTMs

UTM parameters can be "hard-coded" into the url of the token:

```
[link:link,url=https://www.google.com?utm_source=element451,sms_tracking=true]
```

🚨 **Important:**

**Do Not Hard-code UTMs if Communication Settings UTMs are Set**

This with cause the link to have both sets of UTMs. The link will still be valid but reporting could be compromised.

---

# Login URL vs. Login Token (Magic Links)

When adding a token to a Campaign, you will see several different “login” tokens. Login tokens generate **Magic Links**, which are unique short-term identifiers that help Element451 identify a student and relate them to an existing record. This allows them to either bypass the authentication process (they won’t have to log in) or pre-populate known information on forms. These features are designed to expedite and improve the student experience. Click the button below to learn more about Magic Links.

[Explore More: Magic Links →](https://help.element451.com/en/articles/8106669-magic-links)

---

# Frequently Asked Questions + Troubleshooting

#### **Q: What happens if there is no data for the token to pull?**

A: Let's say you have a token for a middle name, **[user:middle\_name]**, but the student didn't enter a middle name. The space will be empty because there is no data to replace the token. Therefore, we advise that you mindfully include tokens that have data to be included in the campaigns. Alternatively, you could alter the token to use a fallback parameter to insert a value instead of the token when data is missing. To learn more, see the [Parameters section above](#h_8b1d74e48c).

#### **Q: Why aren't my tokens populating?**

A: When you send a message (or test to a segment of test users) and one or more of the tokens used in your email don't populate, follow these troubleshooting steps.

Confirm that the contact has data in the field that is associated with that token.

* If the field is empty, the token may have worked as intended.
* If there is data present, delete the token and add it back to your campaign. When adding system tokens, you should add them from the token menu. For custom tokens, you should carefully type the whole token.

In some cases, a broken token will simply not populate. In others, a broken token may prevent a campaign message from being sent at all. So it is important to ensure you are correctly inserting your tokens.

🚨 **Important: Avoid copying and pasting tokens** or parts of tokens from various sources like other Element451 screens, webpages, documents, or email editors. WYSIWYG editors, like the one used in Element451, can hide HTML code within the copied text. Although this code is harmless and may not otherwise impact the message, it will disrupt the functionality of tokens if included inside the token string.

---