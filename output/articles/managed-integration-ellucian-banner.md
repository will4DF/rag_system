---
title: Managed Integration: Ellucian Banner
url: https://help.element451.com/en/articles/12305739-managed-integration-ellucian-banner
collection: Integrations
---

Sync application and contact data from Element451 to Banner with a full service integration from Element451

# Overview

Connect data from Element451 to Banner via the Ellucian Ethos API. Managed integrations from Element451 are customized to your institution's specific needs and maintained by the Element451 team.

* **Integration Mechanism**: REST API
* **Direction**: Bi-directional
* **Sync Delay**: 1-5 minutes
* **Trigger Type**: Manual or Automated
* **Data Format**: JSON
* **Authentication Method**: Bearer Auth Token

---

# Element → Banner Sync

The sync from Element to Banner is an independent function within the integration that creates or updates applicant data in Banner when triggered from Element451.

## Triggering the Sync

The Element → Banner sync can be triggered manually by default and can also be configured to automatically trigger.

### Manual Sync

Add the "Element451 - Trigger Integration Sync" label to any profile to trigger the sync. The label triggers a "Element451 → Ethos Integration Sync" Rule, which runs an "Execute Webhook" step and initializes the sync.

### Automatic Sync

To automate the sync, consider adding additional triggers to the "Element451 → Ethos Integration Sync" Rule.

* A common example is adding a "Decision Released" trigger that will automatically sync applicants to Banner when their Decision in Element451 is released.

### Sync Sequence

1. Webhook initializes the sync
2. Contact data is exported, including contact information, demographic data, applications, previous education, relationships, emergency contacts, and citizenship data.
3. Data is transformed to values compatible with Banner.
4. A person matching request is made to Banner to identify if the contact exists in the System.

   1. If the contact does not exist, a new person is created.
   2. If the contact does exist, the person is identified.
5. Additional person data is sent to Banner.
6. Address data is sent to Banner.
7. Visa/Citizenship data is sent to Banner.
8. Relative / Family member data is sent to Banner.

   1. If a family contact does not exist, a new person is created.
   2. If a family contact does exist, the person is identified.
   3. A relationship is created between the applicant and the family member.
9. Application data is sent to Banner.
10. External education data is sent to Banner.
11. Emergency contact data is sent to Banner.

## Field Mapping

Below, we provide a list of fields exported from Element and their matching field in Banner.

### View the List

|  |  |  |
| --- | --- | --- |
| **Element Slug** | **Banner Field** | **Banner Form** |
| user-elementid | GORADID\_ADDITIONAL\_ID | SPAIDEN |
| user-first-name | SPRIDEN\_FIRST\_NAME | SPAIDEN |
| user-last-name | SPRIDEN\_LAST\_NAME | SPAIDEN |
| user-middle-name | SPRIDEN\_MI | SPAIDEN |
| user-former-last-name | (name type = BIRTH) | SPAIDEN |
| user-preferred-name | (name type = PREFERRED/CHOSEN) | SPAIDEN |
| user-prefix-name | SPRIDEN\_SURNAME\_PREFIX | SPAIDEN |
| user-suffix-name | SPBPERS\_NAME\_SUFFIX | SPAIDEN |
| user-email-address | GOREMAL\_EMAIL\_ADDRESS | GOAEMAL |
| user-identities-school-email | GOREMAL\_EMAIL\_ADDRESS | GOAEMAL |
| user-ssn | SPBPERS\_SSN | SPBPERS |
| user-dob | SPBPERS\_BIRTH\_DATE | SPRIDEN |
| user-gender | SPBPERS\_GNDR\_CODE | SPBPERS |
| user-citizenship-us-statuses | SPBPERS\_CITZ\_CODE | SPRBPERS |
| user-race-hispanic | SPBPERS\_ETHN\_CODE | SPRBPERS |
| user-race-categories | GORPRAC\_RACE\_CDE | GORPRAC |
| user-citizenship-country | GOBINTL\_NATN\_CODE\_LEGAL | SPAIDEN |
| user-citizenship-country-of-birth | GOBINTL\_NATN\_CODE\_BIRTH | SPAIDEN |
| user-addresses-street1 | SPRADDR\_STREET\_LINE1 | SPAIDEN |
| user-addresses-street2 | SPRADDR\_STREET\_LINE2 | SPAIDEN |
| user-addresses-street3 | SPRADDR\_STREET\_LINE3 | SPAIDEN |
| user-addresses-city | SPRADDR\_CITY | SPAIDEN |
| user-addresses-state | SPRADDR\_STAT\_CODE | SPAIDEN |
| user-addresses-province | SPRADDR\_STAT\_CODE | SPAIDEN |
| user-addresses-zip | SPRADDR\_ZIP | SPAIDEN |
| user-addresses-country | SPRADDR\_NATN\_CODE | SPAIDEN |
| user-phone-home-country-code | SPRTELE\_PHONE\_AREA | SPATELE |
| user-phone-home-number | SPRTELE\_PHONE\_NUMBER | SPATELE |
| user-phone-cell-country-code | SPRTELE\_PHONE\_AREA | SPATELE |
| user-phone-cell-number | SPRTELE\_PHONE\_NUMBER | NAE |
| user-family-relationship | SORFOLK\_DIR\_RELT\_ID / SORFOLK\_RELT\_CODE | SOAFOLK |
| user-family-email | GOREMAL\_EMAIL\_ADDRESS | SOAFOLK / SPAIDEN |
| user-family-first-name | SPRIDEN\_FIRST\_NAME | SOAFOLK / SPAIDEN |
| user-family-last-name | SPRIDEN\_LAST\_NAME | SOAFOLK / SPAIDEN |
| user-family-middle-name | SPRIDEN\_MI | SOAFOLK / SPAIDEN |
| user-family-gender | SPBPERS\_GNDR\_CODE | SPBPERS |
| user-family-phone-number | SPRTELE\_PHONE\_NUMBER | SPATELE |
| user-family-phone-country-code | SPRTELE\_PHONE\_AREA | SPATELE |
| user-family-address-street-1 | SPRADDR\_STREET\_LINE1 | SPAIDEN |
| user-family-address-street-2 | SPRADDR\_STREET\_LINE2 | SPAIDEN |
| user-family-address-city | SPRADDR\_CITY | SPAIDEN |
| user-family-address-state | SPRADDR\_STAT\_CODE | SPAIDEN |
| user-family-address-zipcode | SPRADDR\_ZIP | SPAIDEN |
| user-family-address-country | SPRADDR\_NATN\_CODE | SPAIDEN |
| user-family-address-province | SPRADDR\_STAT\_CODE | SPAIDEN |
| user-applications-status | SARAPPD\_APDC\_CODE | SAADCRV |
| user-applications-submitted-time | SARADAP\_APPL\_DATE | SAAADMS |
| user-applications-major | SARADAP\_MAJR\_CODE\_1 | SAAADMS |
| user-applications-term | SARADAP\_TERM\_CODE\_ENTRY | SAAADMS |
| user-applications-degree | SARADAP\_DEGC\_CODE | SAAADMS |
| user-applications-campus | SORLCUR\_CAMP\_CODE | SAAADMS |
| user-applications-student-type | SARADAP\_STYP\_CODE | SAAADMS |
| user-applications-board-status | SARADAP\_ADMT\_CODE | SAAADMS |
| user-applications-decision-released-at | SARAPPD\_APDC\_DATE | SAAADMS |
| user-education-academic-load | (SARADAP\_FULL\_PART\_IND or SARADAP\_FULL\_PART\_IND) | SAAADMS |
| user-education-schools-gpa | SORHSCH\_GPA | SORHSCH |
| user-education-schools-start | SORDEGR\_ATTEND\_FROM | SOAPCOL |
| user-education-schools-end | SORDEGR\_ATTEND\_TO | SOAPCOL |
| user-education-schools-graduate-date | SORHSCH\_GRADUATION\_DATE | SOAHSCH |
| user-citizenship-visa-type | GORVISA\_VTYP\_CODE | GOAINTL |

📌 **Note**: Managed integrations are configurable. Additional custom fields in Element or additional resources in Ethos may be included in your institution's integration. Contact Element451 support for more information.

---

# Banner → Element Sync

The sync from Banner to Element is an independent function within the integration that creates or updates student and application data within Element451 based on data from Banner.

## Triggering the Sync

The Banner → Element sync relies on "change notifications" from Ethos, which denote that a change was made to an applicant's data in Banner. The managed integration reads these notifications every five minutes and updates the applicant's data in Element accordingly.

Ensure that the Element451 Ethos "application" is subscribed to notifications from the persons, addresses, and admission-applications resources in order for change notifications to be received. Remove the subscriptions to disable the Banner->Element sync.

## Sync Sequence

1. Change notification is added to the consume resource.
2. The managed integration reads the consume resource every five minutes.
3. Change notification for an applicant is read.
4. Applicant data is requested from Banner, including person data, application data, aptitude assessments, addresses, and previous education.
5. Data is transformed to values compatible with Element451.
6. Person data is imported to Element.
7. Application data is imported to Element.
8. Address data is imported to Element.
9. Aptitude assessment data (evaluations) is imported into Element.
10. Previous education data (schools) is imported into Element.

---

# Data Source Sync

Translating data values between Element451 and Banner is essential for the integration. Translations are managed by syncing Banner validation table values to Data Sources in Element. This sync is an independent function within the integration.

## Sync Schedule

* By default, academic-periods (Terms), academic-programs (Majors), and academic-credentials (Degrees) sync **every Saturday**.
* Refreshes of these or other data sources can be requested via Element live support.

## Adding New Data Source Values

* New values for data sources **should always be added in Banner first**.
* Update the validation table and then wait for the sync to run.
* Once a data source has synced with Banner, it should not be edited in Element (exceptions apply; ask Element support when in doubt).

## Translation Tables

In addition to updating data sources within Element451, the managed integration also maintains "translation tables" behind the scenes.

* These tables are directly responsible for the translation between Element and Banner data values.
* If a value is not in the table, it will not be translated properly.
* Translation tables are only accessible to Element451 support and will be updated with the data source sync or upon request.

# Additional Information

Additional information about configuring Ethos can be found in the Integration Guide: <https://integrations.element451.com/ellucian-ethos-142>

## Troubleshooting Common Errors

### Errors during Element->Banner

#### PERSON record locked for ID ...

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

**Origin**: Banner / Ethos

**Description:**

This means someone is in the record in Banner.

**Resolution Steps:**

Close the record in Banner and re-sync

#### reviewRequired

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

**Origin**: Banner / Ethos

**Description:**

A potential duplicate was found in the SIS when attempting to sync from Element.

**Resolution Steps:**

1. Review the match on GOAMTCH
2. Resolve the duplicate
3. Resync from Element

#### Relative review required

**Origin**: Banner / Ethos

**Description:**

A potential duplicate was found when attempting to sync a person’s relatives.

**Resolution Steps:**

1. Review the match on SOAFOLK
2. Resolve the duplicate
3. Resync from Element

#### **Skipping Invalid Address**

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

#### '{State Name}' is not defined as a state or province.

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

**Origin**: Banner / Ethos

**Description:**

The student has bad data on their Element profile. Address has State *name* instead of State *abbreviation.* In the case of North Carolina, State should be “NC”.

**Resolution Steps:**

1. Navigate to student’s Element profile.
2. Edit Address, select correct State from dropdown menu, save
3. Resync from Element

#### There is no ceeb for the institution

```
Summary 1: There is no ceeb for the institution. Ensure an institution with CEEB code 1234 is listed on STVSBGI in Banner. If no institution, please create one and notify Element451 support to resync with Banner.  
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

**Origin**: Banner / Ethos

**Description:**

The student selected a prior education institution in Element451 that does not have a match on STVSBGI in Banner.

**Resolution Steps:**

1. Create an entry for the institution on STVSBGI
2. Notify the Element451 team via live support to resync with the SIS to pick up new institutions.

---