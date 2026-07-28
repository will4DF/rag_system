---
title: Importing Record Bio-Demographic Data
url: https://help.element451.com/en/articles/10771204-importing-record-bio-demographic-data
collection: Data Management
---

Learn how to import bio-demographic data of a record.

Direct attributes on a record are fields that can only have one value, and typically this tends to be bio-demographic data. Fields like citizenship status, gender, but also contact data like cell phone number, home address, and more are direct attributes. This is a good place to start when importing historic data as the mapping will be pretty standard and you won't have to worry about application, funnel, school, or test score data.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481808352/5d3eebe1ad5c42b44a6e354cb097/Screenshot+2025-04-17+at+4_05_02%E2%80%AFPM.png?expires=1784333700&signature=053699184f147102525c788a632e825ef728c803b406a2cae2f3f87473dd8265&req=dSQvF8F%2BlYJaW%2FMW1HO4zQrW3oynWjduOvEC3gWUMvZyqMd60C%2BHK0SMdKf6%0AWRbeV%2BuaRfiQF8mE8pQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481808352/5d3eebe1ad5c42b44a6e354cb097/Screenshot+2025-04-17+at+4_05_02%E2%80%AFPM.png?expires=1784333700&signature=053699184f147102525c788a632e825ef728c803b406a2cae2f3f87473dd8265&req=dSQvF8F%2BlYJaW%2FMW1HO4zQrW3oynWjduOvEC3gWUMvZyqMd60C%2BHK0SMdKf6%0AWRbeV%2BuaRfiQF8mE8pQ%3D%0A)

## Creating a Bio-Demographic File

As a reminder, the file needs to be either .csv or .txt, contain a unique identifier (or a few!), and only have one row per record. The bio-demographic file is a great opportunity to add unique identifiers that may be helpful for future imports like your application and funnel information.

Any direct attributes or properties can be added to the file you are creating. There is a Historic Bio-Demographic Import template in your instance, but you are not required to follow that exact layout if you need additional unique identifiers or need to put the fields in a different order, the template is a starting point if you need direction.

## Fields to Include in the File

Listed below are fields that you can include on your bio-demographic file.

* Contact Identifiers (Student ID, Historic ID, and/or Email)
* Name
* Birthdate
* Gender
* Ethnicity
* Citizenship
* Phone Numbers
* Addresses
* Intended Major, Term, Student Type, Degree

  + Intended fields are simply what the student might be interested in or expressed interest in through a form. This is not related to the application.

## Mapping Bio-Demographic Data

You will have one import task for bio-demographic data with some of the following fields.

## Mapping

* **Contact Identifiers:** This can be a historic ID from a previous CRM, student ID, email, or other identifier. Not all are necessary, but the more the better!

  + user-identities-historicid
  + user-identities-schoolid
  + user-email-address

    - Note, this is the record's **personal email**
  + user-identities-school-email
* **Personal**

  + user-ssn
  + user-preferred-name

  + user-first-name
  + user-middle-name
  + user-last-name
  + user-former-last-name
  + user-dob
  + user-gender
  + user-gender-pronouns
* **Contact**

  + user-phone-cell-country-code
  + user-phone-cell-number
  + user-phone-home-country-code
  + user-phone-home-number
  + user-sms-updates
  + user-addresses-home-street1
  + user-addresses-home-street2
  + user-addresses-home-city
  + user-addresses-home-state
  + user-addresses-home-province
  + user-addresses-home-country
  + user-addresses-home-zip
  + user-addresses-mailing-street1
  + user-addresses-mailing-street2
  + user-addresses-mailing-city
  + user-addresses-mailing-state
  + user-addresses-mailing-province
  + user-addresses-mailing-country
  + user-addresses-mailing-zip
* **Race**

  + user-race-hispanic
  + user-race-categories
* **Citizenship**

  + user-citizenship-country
  + user-citizenship-country-of-birth
  + user-citizenship-us-status
  + user-citizenship-visa-type

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1428499512/bb02536a5189407b044c3ddd182e/Screenshot+2025-03-18+at+10_14_13%E2%80%AFAM.png?expires=1784333700&signature=e82dd8dbe103a5fa135f1ad04a6e06401cbe560042a0f3282463678686b78773&req=dSQlHs13lIReW%2FMW1HO4zW9NTRCYIuJF7ZgSTUuYQ6HuhyhuIHVv9ZDDCLiL%0AjxAIJ8%2FD%2BokqWgA%2FHz4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1428499512/bb02536a5189407b044c3ddd182e/Screenshot+2025-03-18+at+10_14_13%E2%80%AFAM.png?expires=1784333700&signature=e82dd8dbe103a5fa135f1ad04a6e06401cbe560042a0f3282463678686b78773&req=dSQlHs13lIReW%2FMW1HO4zW9NTRCYIuJF7ZgSTUuYQ6HuhyhuIHVv9ZDDCLiL%0AjxAIJ8%2FD%2BokqWgA%2FHz4%3D%0A)

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481750419/b811f15c571c1484b304e6a5735e/Important+-+Orng.png?expires=1784430000&signature=0ecae1fbfb70a6c771be153e5f66aec28bbd5b220a2a734684449fdd17ce5d32&req=dSQvF857nYVeUPMW3Hu4ge07VJ153g11VXdcuFN3mY1TLRW5ERcXh6S%2FgDmf%0AsA%3D%3D%0A) Pay special attention to any fields that have a blue box next to their Field and Slug name. Blue = Do! There are additional transformation settings to consider before running the import. Review our [Column Setting Options](https://help.element451.com/en/articles/9006325-column-setting-options-for-imports) article for an explanation on Transformations.

## Next Steps

After you complete mapping the import, you are almost ready to run it. Follow the rest of our [Creating Imports](https://help.element451.com/en/articles/9001231-creating-imports#h_197a97ad23) help article for setting up Configuration Settings, Previewing, and Running your import.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1486305366/59d71e18be23298ca39aad16ed34/Pro+Tip+-+Orng.png?expires=1784430000&signature=539d1aca7dd294988e07f433faa043c313c8e4fc1162c232abcf42724e2475b6&req=dSQvEMp%2BmIJZX%2FMW3Hu4gePpw8acGwSwVkd8YWbwg6CRW4NXOt7WVndeZDgB%0ANQ%3D%3D%0A)![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1481773211/3aac945129121b1dedb050b14dc3/Pro+Tip+-+Orng.png?expires=1784430000&signature=1f5216c7f520ff2b4e0faf96e0bba7fdc76ed98b9458e8209e7da0929ea42eea&req=dSQvF855noNeWPMW3Hu4gQPB%2F7hveCrq0Ap9LUnl468Fqh7GUo37%2FitwjDq5%0AOw%3D%3D%0A) Importing a large file? Copy the first couple rows of your file into a separate file and import that subset in. That will give you a chance to see what the results look like, without causing too much trouble if something was mapped incorrectly.

#

---