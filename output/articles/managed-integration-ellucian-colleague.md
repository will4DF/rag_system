---
title: Managed Integration: Ellucian Colleague
url: https://help.element451.com/en/articles/12294737-managed-integration-ellucian-colleague
collection: Integrations
---

Sync application and contact data from Element451 to Colleague with a full service integration from Element451

# Overview

Connect data from Element451 to Colleague via the Ellucian Ethos API. Managed integrations from Element451 are customized to your institution's specific needs and maintained by the Element451 team.

* **Integration Mechanism**: REST API
* **Direction**: Bi-directional
* **Sync** **Delay**: 1-5 minutes
* **Trigger** **Type**: Manual or Automated
* **Data** **Format**: JSON
* **Authentication** **Method**: Bearer Auth Token

---

# Element → Colleague Sync

The sync from Element to Colleague is an independent function within the integration that creates or updates applicant data in Colleague when triggered from Element451.

## Triggering the Sync

The Element → Colleague sync can be triggered manually by default and can also be configured to automatically trigger.

### Manual Sync

Add the "Element451 - Trigger Integration Sync" label to any profile to trigger the sync. The label triggers a "Element451 → Ethos Integration Sync" Rule, which runs an "Execute Webhook" step and initializes the sync.

### Automatic Sync

To automate the sync, consider adding additional triggers to the "Element451 → Ethos Integration Sync" Rule.

* A common example is adding a "Decision Released" trigger that will automatically sync applicants to Colleague when their Decision in Element451 is released.

### Sync Sequence

1. Webhook initializes the sync.
2. Contact data is exported, including contact information, demographic data, applications, previous education, relationships, emergency contacts, and citizenship data.
3. Data is transformed to values compatible with Colleague.
4. A person matching request is made to Colleague to identify if the contact exists in the System.

   1. If the contact does not exist, a new person is created.
   2. If the contact does exist, the person is identified.
5. Additional person data is sent to Colleague.
6. Address data is sent to Colleague.
7. Visa/Citizenship data is sent to Colleague.
8. Relative / Family member data is sent to Colleague.

   1. If a family contact does not exist, a new person is created.
   2. If a family contact does exist, the person is identified.
   3. A relationship is created between the applicant and the family member.
9. Application data is sent to Colleague.
10. External education data is sent to Colleague.
11. Emergency contact data is sent to Colleague.

## Field Mapping

Below, we provide a list of fields exported from Element and their matching field in Colleague.

### View the List

|  |  |  |
| --- | --- | --- |
| **Element Slug** | **Colleague Field** | **Colleague Mnemonic** |
| user-elementid | PERSON.ALT.IDS | DADD |
| user-first-name | FIRST.NAME | NAE |
| user-last-name | LAST.NAME | NAE |
| user-middle-name | MIDDLE.NAME | NAE |
| user-former-last-name | (name type) NAME.HISTORY.LAST.NAME | BIO |
| user-preferred-name | (name type) PREFERRED.NAME | BIO |
| user-prefix-name | PREFIX | BIO |
| user-suffix-name | SUFFIX | BIO |
| user-email-address | PERSON.EMAIL.ADDRESSES | NAE |
| user-identities-school-email | PERSON.EMAIL.ADDRESSES | NAE |
| user-ssn | SSN | NAE |
| user-dob | BIRTHDATE | NAE |
| user-gender | GENDER | NAE |
| user-citizenship-us-statuses | citizenshipStatus | FPER |
| user-race-hispanic | PERSON.ETHNNICS | BIO |
| user-race-categories | PER.RACES | BIO |
| user-citizenship-country | FPER.BIRTH.COUNTRY | FPER |
| user-citizenship-country-of-birth |  |  |
| user-addresses-type |  | ADR |
| user-addresses-street1 | ADDRESS.LINES<1,1> | ADR |
| user-addresses-street2 | ADDRESS.LINES<1,2> | ADR |
| user-addresses-street3 | ADDRESS.LINES<1,3> | ADR |
| user-addresses-city | CITY | ADR |
| user-addresses-state | STATE | ADR |
| user-addresses-province | STATE | ADR |
| user-addresses-zip | ZIP | ADR |
| user-addresses-country | COUNTRY | ADR |
| user-addresses-home-mailing |  | ADR |
| user-phone-home-country-code |  | NAE |
| user-phone-home-number |  | NAE |
| user-phone-cell-country-code |  | NAE |
| user-phone-cell-number |  | NAE |
| user-family-relationship |  | REL |
| user-family-email | PERSON.EMAIL.ADDRESSES | NAE |
| user-family-first-name | FIRST.NAME | NAE |
| user-family-last-name | LAST.NAME | NAE |
| user-family-middle-name | MIDDLE.NAME | NAE |
| user-family-gender | GENDER | NAE |
| user-family-phone-number |  | NAE |
| user-family-phone-country-code |  | NAE |
| user-family-phone-type |  | NAE |
| user-family-address-street-1 | ADDRESS.LINES<1,1> | ADR |
| user-family-address-street-2 | ADDRESS.LINES<1,2> | ADR |
| user-family-address-city | CITY | ADR |
| user-family-address-state | STATE | ADR |
| user-family-address-zipcode | ZIP | ADR |
| user-family-address-country | COUNTRY | ADR |
| user-family-address-province | STATE | ADR |
| user-applications-status | APPL.STATUS (derived from CDAM) ​ | APPN |
| user-applications-submitted-time |  | APPN |
| user-applications-major | APPL.ACAD.PROGRAM | APPN |
| user-applications-term | APPL.START.TERM | APPN |
| user-applications-degree |  | APPN |
| user-applications-campus |  | APPN |
| user-applications-student-type |  | APPN |
| user-applications-board-status |  |  |
| user-applications-decision-released-at |  |  |
| user-education-academic-load |  |  |
| user-education-schools-ceeb | Used to look up Institution Attended | IASU |
| user-education-schools-gpa | INSTA.EXT.GPA | IASU |
| user-education-schools-start | INSTA.START.DATES | IASU |
| user-education-schools-end | INSTA.END.DATES | IASU |
| user-education-schools-graduate-date | INSTA.INTG.HS.GRAD.DATE | IASU |
| user-citizenship-visa-type | VISA.TYPE | FPER |

📌 **Note**: Managed integrations are configurable. Additional custom fields in Element or additional resources in Ethos may be included in your institution's integration. Contact Element451 support for more information.

# Colleague → Element Sync

The sync from Colleague to Element is an independent function within the integration that creates or updates student and application data within Element451 based on data from Colleague.

## Triggering the Sync

The Colleague → Element sync relies on "change notifications" from Ethos, which denote that a change was made to an applicant's data in Colleague. The managed integration reads these notifications every five minutes and updates the applicant's data in Element accordingly.

Ensure that the Element451 Ethos "application" is subscribed to notifications from the persons, addresses, and admission-applications resources in order for change notifications to be received. Remove the subscriptions to disable the Colleague → Element sync.

## Sync Sequence

1. Change notification is added to the consume resource.
2. The managed integration reads the consume resource every five minutes.
3. Change notification for an applicant is read.
4. Applicant data is requested from Colleague, including person data, application data, aptitude assessments , addresses, and previous education.
5. Data is transformed to values compatible with Element451.
6. Person data is imported to Element.
7. Application data is imported to Element.
8. Address data is imported to Element.
9. Aptitude assessment data (evaluations) is imported into Element.
10. Previous education data (schools) is imported into Element.

---

# Data Source Sync

Translating data values between Element451 and Colleague is essential for the integration. Translations are managed by syncing Colleague validation table values to Data Sources in Element. This sync is an independent function within the integration.

## Sync Schedule

* By default, academic-periods (Terms), academic-programs (Majors), and academic-credentials (Degrees) sync **every** **Saturday**.
* Refreshes of these or other data sources can be requested via Element live support.

## Adding New Data Source Values

* New values for data sources should always be added in Colleague first.
* Update the validation table and then wait for the sync to run.
* Once a data source has synced with Colleague, it should not be edited in Element (exceptions apply; ask Element support when in doubt).

## Translation Tables

In addition to updating data sources within Element451, the managed integration also maintains "translation tables" behind the scenes.

* These tables are directly responsible for the translation between Element and Colleague data values.
* If a value is not in the table, it will not be translated properly.
* Translation tables are only accessible to Element451 support and will be updated with the data source sync or upon request.

---

# Additional Info + Troubleshooting

Additional information about configuring Ethos can be found in the Integration Guide: <https://integrations.element451.com/ellucian-ethos-142>

## Troubleshooting Common Errors

### Errors during Element → Colleague

**“Person emergency contacts with ID ... and contact name of ... already exists"**

```
{    
  "type": "<class 'ethos_integration.ethos_api.ethos_api.APIException'>",  
  "status_code": "400",    
  "content": {      
    "errors": [        
      {          
        "id": "00000000-0000-0000-0000-000000000000",  
        "code": "Create.Update.Exception",  
        "description": "Error occurred in the source system that prevented update or creation of the record.",  
        "message": "Person.Emergency.Contacts.Contact.Name - Person emergency contacts with ID 'xxxxxxx' and contact name of name already exists. Duplicate contact name is not allowed."        
      }      
    ]    
  }  
}
```

**Origin**: Colleague / Ethos

**Description:**

This means that the Emergency Contact already exists as a person in Colleague.

**Resolution Steps:**

Review the NAE to verify. Edit or disregard.

**"Person record locked for ID ..."**

```
{    
   "type": "<class 'shared_resources.exceptions.APIException'>",  
   "status_code": "400",  
   "content": {      
      "errors": [        
          {          
             "code": "Validation.Exception",  
             "description": "An error occurred attempting to validate data.",  
             "message": "PersonExternalEducation.Record.Lock: PERSON record locked for ID xxxxxxx"        
          }      
       ]    
    }  
}
```

**Origin**: Colleague / Ethos

**Description:**

This means someone is in the record in Colleague.

**Resolution Steps:**

Close the record in Colleague and re-sync

**"Person with ID ... is already enrolled in the requested program ..."**

```
{      
  "errors": [  
    {  
      "code": "admissionApplication",  
      "description": "Unknown error code.",  
      "message": "Person with ID 'xxxxx' is already enrolled in the requested program 'xxxxx'."          
    }      
  ]  
}
```

**Origin:** Colleague / Ethos

**Description:**

This error occurs when attempting to create a new application for the student when syncing Element451→Ethos. If the student is enrolled for the same program, Ethos throws the error.

**Resolution Steps:**

Close the program for that student in SACP (Colleague) by adding an end date. Ensure that the program end date is before the start of the application term.

**reviewRequired**

```
{    
  "outcomes": [      
    {        
      "type": "initial",        
      "status": "reviewRequired",        
      "date": "2025-01-15T11:27:40"      
    }    
  ],    
  "originator": "ETHOS",    
  "id": "xxx-xxxx-xxxx -xxxx-xxxx"  
}
```

**Origin**: Colleague / Ethos

**Description:**

A potential duplicate was found in the SIS when attempting to sync from Element.

**Resolution Steps:**

1. Review the match on PEMR
2. Resolve the duplicate
3. Resync from Element

**Relative review required**

**Origin**: Colleague / Ethos

**Description:**

A potential duplicate was found when attempting to sync a person’s relatives.

**Resolution Steps:**

1. Review the match on REL
2. Resolve the duplicate
3. Resync from Element

**Skipping Invalid Address**

```
Skipping invalid address: {      
  "ethos_id": "",      
  "type": "home",      
  "street1": "*** Street Name Ave",      
  "street2": "",      
  "street3": "",      
  "city": "Some City",      
  "state": "ST",      
  "province": "",      
  "zip": "12345",      
  "country": "",      
  "is_home_mailing": "",      
  "county": "" //country is missing in this example  
}
```

**Origin**: Element451

**Description:**

The student is missing required data on their Element profile. Ensure the following are present:

* Street 1
* City
* State
* Zip
* Country

**Resolution Steps:**

1. Navigate to student’s Element profile.
2. Edit Address, ensure all data items are present, save
3. Resync from Element

**'{State Name}' is not defined as a state or province.**

```
{    
  "type": "<class 'shared_resources.exceptions.APIException'>",    
  "status_code": 400,    
  "content": {      
    "errors": [        
      {          
        "id": "176684ff-6cce-4473-ac9b-caa912220a9e", //address identifier          
        "sourceId": "0862595",          
        "code": "persons.addresses",          
        "description": "Unknown error code.",          
        "message": "'North Carolina' is not defined as a state or province.  (Parameter 'addressDto.place.region')" //North Carolina example shown, but State Name may vary        
      }      
    ]    
  },    
  "args": [      
    "Status code: 400\nContent:\n{\n    \"errors\": [\n        {\n            \"id\": \"176684ff-6cce-4473-ac9b-caa912220a9e\",\n            \"sourceId\": \"0862595\",\n            \"code\": \"persons.addresses\",\n            \"description\": \"Unknown error code.\",\n            \"message\": \"'North Carolina' is not defined as a state or province.  (Parameter 'addressDto.place.region')\"\n        }\n    ]\n}"    
  ]  
}
```

**Origin**: Colleague / Ethos

**Description:**

The student has bad data on their Element profile. Address has State *name* instead of State *abbreviation.* In the case of North Carolina, State should be “NC”.

**Resolution Steps:**

1. Navigate to student’s Element profile.
2. Edit Address, select correct State from dropdown menu, save
3. Resync from Element

**"Student program not found for: {student\_id}\*{program\_code} "**

```
Method: GET Endpoint: /api/admission-applications?criteria={"applicant":{"id":"{ethos_id}"}}   
Response:    
  {       
    "errors": [  
      {  
        "code": "Data.Access",  
        "description": "Unknown error code.",  
        "message": "Student program not found for: {student_id}*.{program_code}"  
      }       
    ]   
}
```

**Origin:** Colleague / Ethos

**Description:**   
An invalid pointer exists for the student program.

**Resolution Steps:**

Varies. Consult Institutional IT or Ellucian Support.

**There is no CEEB for the institution**

```
Summary 1: There is no ceeb for the institution. Ensure an institution with CEEB code 1234 is listed on INST in Colleague. If no institution, please create one and notify Element451 support to resync with Colleague.  
Full Error 1:   
{    
  "institution_id": "",   
  "ceeb": "1234"   
  "type": "highschool",    
  "entry_type": "highschool",    
  "gpa": "",    
  "start": "",    
  "end": "",    
  "graduate_date": "2017-04-17",    
  "institution_country": ""  
}
```

**Origin**: Colleague / Ethos

**Description:**

The student selected a prior education institution in Element451 that does not have a match on INST in Colleague.

**Resolution Steps:**

1. Create an entry for the institution on INST
2. Notify the Element451 team via live support to resync with the SIS to pick up new institutions.

### Error during Colleague → Element

**"code": "GUID.Not.Found", "description": "An error occurred translating the GUID to an ID.", "message": "No Guid found, Entity:'OTHER.CCDS', Record ID:'??"**

```
Method: GET  
Endpoint: /api/student-academic-programs/aea41913-f795-42d1-80c0-557a0fc25281  
Response: {      
  "errors": [          
    {              
      "id": "aea913-f75-42d1-80c00-557a0f5281",              
      "sourceId": "1396903*",              
      "code": "GUID.Not.Found",              
      "description": "An error occurred translating the GUID to an ID.",              
      "message": "No Guid found, Entity:'OTHER.CCDS',   
       Record ID:''"          
    }      
  ]  
}
```

**Origin:** Colleague / Ethos

**Description**

When syncing to Ethos, the managed integration attempts to extract data about the academic program the student has applied to. This error indicates that program data found in the OTHER.CCDS table cannot be found by that GUID.

This error only applies to application data. Other data, such as person, address and emergency contact, should still sync.

**Resolution Steps:**

Run GNGU on OTHER.CCDS. This will create the GUID association and allow the request to the student-academic-programs resource to return data without error.

---