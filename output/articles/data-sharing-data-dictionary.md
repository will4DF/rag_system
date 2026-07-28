---
title: Data Sharing - Data Dictionary
url: https://help.element451.com/en/articles/7888528-data-sharing-data-dictionary
collection: Insights
---

An overview of the schema and tables offered by Element451 through Snowflake data sharing.

# Overview

Snowflake is a data platform that Element451 has partnered with to house data for analysis and share that data with our partner schools. If you're interested in accessing Snowflake data sharing, talk to your Customer Success Manager.

You can learn more about the Snowflake data platform [here](https://www.snowflake.com/en/).

---

# Data Dictionary

## Schema

Data share tables are located within the following schema:

`v1_element451_shared`

## Tables

The following are descriptions of each table in the shared schema. Descriptions include the column name, column data type, and column description.

### el\_activities\_raw

Activities are performed by the student or by an Element451 user. Read more about [Activities in Element451.](https://help.element451.com/en/articles/5159877-activity-feed-the-student-s-journey)

This table features one row per unique activity. Activity attributes are stored as JSON in the *src* column.

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| \_id | TEXT | Unique activity identifier |
| subdom | TEXT | Partner school instance identifier |
| app\_id | TEXT | Analytics application identifier |
| action | TEXT | Activity category |
| element\_id | TEXT | Unique student record identifier associated with the Activity |
| src | VARIANT | JSON object of activity properties |
| timestamp | TIMESTAMP\_NTZ | Activity occurrence timestamp |
| updated\_at | TIMESTAMP\_NTZ | Activity update timestamp |
| created\_at | TIMESTAMP\_NTZ | Activity log created timestamp |
| deleted\_at | TIMESTAMP\_NTZ | Activity deleted timestamp |
| etl\_loaded\_at | TIMESTAMP\_NTZ | Activity loaded into Snowflake timestamp |

### el\_metadata\_raw

Metadata refers to items such as system settings, field settings, and data sources.

This table features one row per unique metadata item.

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| \_id | TEXT | Unique identifier of metadata item |
| subdom | TEXT | Partner school instance identifier |
| type | TEXT | Metadata category |
| src | VARIANT | JSON object of metadata properties |
| updated\_at | TIMESTAMP\_NTZ | Metadata last update at timestamp |
| created\_at | TIMESTAMP\_NTZ | Metadata created at timestamp |
| etl\_loaded\_at | TIMESTAMP\_NTZ | Metadata last loaded into Snowflake timestamp |

### el\_people\_applications

This table features one row per student application. Applications are a many-to-one relationship with the student record. This modeled table features each application in its own row.

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| subdom | TEXT | Partner school instance identifier |
| element\_id | TEXT | Unique student record identifier associated with the Application |
| updated\_at | TIMESTAMP\_NTZ | Application last updated at timestamp |
| first\_name | VARIANT | Student first name |
| last\_name | VARIANT | Student last name |
| email | VARIANT | Student email |
| registration\_id | TEXT | Unique Application registration identifier |
| created\_at | TIMESTAMP\_NTZ | Application created at timestamp |
| completed\_at | TIMESTAMP\_NTZ | Application progress completed at timestamp |
| submitted\_at | TIMESTAMP\_NTZ | Application submitted timestamp |
| status | TEXT | Application status |
| progress\_percent | NUMBER | Application progress percentage |
| app\_type\_guid | TEXT | Application type identifier |
| term\_guid | TEXT | Application term identifier |
| program\_guid | TEXT | Application major identifier |
| src | VARIANT | JSON object of Application properties |

### el\_people\_milestones

This table features one row per student milestone. Milestones are a many-to-one relationship with the student record. This modeled table features each milestone in its own row.

Learn more about [Milestones](https://help.element451.com/en/articles/3419189-milestones-an-overview).

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| subdom | TEXT | Partner school instance identifier |
| element\_id | TEXT | Unique student record identifier associated with the Milestone |
| updated\_at | TIMESTAMP\_NTZ | Milestone last updated at timestamp |
| milestone\_id | TEXT | Unique Milestone identifier |
| type | TEXT | Milestone type |
| name | TEXT | Milestone name |
| timestamp | TIMESTAMP\_NTZ | Milestone occurrence timestamp |
| application\_guid | TEXT | Application identifier related to Milestone, if applicable |
| application\_internal | BOOLEAN | Application internal/external flag related to Milestone, if applicable |
| registration\_id | TEXT | Application registration identifier related to Milestone, if applicable |
| term | TEXT | Milestone term |
| major | TEXT | Milestone major |
| student\_type | TEXT | Milestone student type |
| blocked\_email | TEXT | Email address that has been blocked related to Milestone, if applicable |
| blocked\_number | TEXT | Phone number that has been blocked related to Milestone, if applicable |
| withdraw\_reason | TEXT | Withdraw reason related to Milestone, if applicable |
| source | TEXT | Milestone creation source |
| interviewer | TEXT | Interviewer name related to Milestone, if applicable |
| deposit\_status | TEXT | Deposit status related to Milestone, if applicable |
| enrollment\_status | TEXT | Enrollment status related to Milestone, if applicable |
| intended\_term | TEXT | Current student intended term value |
| intended\_major | TEXT | Current student intended major value |
| active\_term | TEXT | Current student active term value |
| active\_major | TEXT | Current student active major value |
| src | VARIANT | JSON object of Milestone  properties |

### el\_people\_sources

This table features one row per student source. Sources have a many-to-one relationship with the student record. This modeled table features each source in its own row. The table also features demographic attributes about each student.

Learn more about [Sources](https://help.element451.com/en/articles/2066892-sources).

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| subdom | TEXT | Partner school instance identifier |
| element\_id | TEXT | Unique student record identifier associated with the Source |
| source\_id | TEXT | Unique Source identifier |
| type | TEXT | Source type |
| name | TEXT | Source name or alias |
| timestamp | TIMESTAMP\_NTZ | Source occurrence timestamp |
| source\_guid | TEXT | Source name or alias identifer |
| segment | TEXT | Source segment name |
| segment\_guid | TEXT | Source segment identifier |
| url | TEXT | Source URL, for WEB type Sources |
| event\_date | TIMESTAMP\_NTZ | Event date related to Source, for EVENT type Sources |
| event\_guid | TEXT | Event identifier related to Source, for EVENT type Sources |
| event\_name | TEXT | Event name related to Source, for EVENT type Sources |
| event\_elements\_guid | TEXT | Event elements related to Source, for EVENT type Sources |
| application\_guid | TEXT | Application identifier related to Source, for APP type Sources |
| application\_name | TEXT | Application name related to Source, for APP type Sources |
| registration\_id | TEXT | Application registration id related to Source, for APP type Sources |
| utm\_campaign | TEXT | URL utm\_campaign value related to Source, for WEB type Sources |
| utm\_medium | TEXT | URL utm\_medium value related to Source, for WEB type Sources |
| utm\_content | TEXT | URL utm\_content value related to Source, for WEB type Sources |
| utm\_source | TEXT | URL utm\_source value related to Source, for WEB type Sources |
| utm\_term | TEXT | URL utm\_term value related to Source, for WEB type Sources |
| source\_major | TEXT | Major related to Source |
| active\_major | TEXT | Student' current active major |
| active\_term | TEXT | Student's current active term |
| active\_student\_type | TEXT | Student's current active student type |
| address\_country | TEXT | Student's home address country |
| address\_state | TEXT | Student's home address state |
| address\_county | TEXT | Student's home address county |
| address\_city | TEXT | Student's home address city |
| address\_zipcode | TEXT | Student's home address zip code |
| citizenship\_status | TEXT | Student's citizenship status |
| territory\_name | TEXT | Student's territory |
| engagement\_score | TEXT | Student's current engagement score |
| labels | TEXT | Student's labels, represented as comma-separated list |
| segments | TEXT | Student's calculated segments, represented as comma-separated list |
| suspect | NUMBER | Flag indicating that student is currently in suspect funnel stage |
| prospect | NUMBER | Flag indicating that student is currently in prospect funnel stage |
| app\_start | NUMBER | Flag indicating that student is currently in app\_start funnel stage |
| app\_complete | NUMBER | Flag indicating that student is currently in app\_complete funnel stage |
| app\_submit | NUMBER | Flag indicating that student is currently in app\_submit funnel stage |
| admit | NUMBER | Flag indicating that student is currently in admit funnel stage |
| admit\_conditional | NUMBER | Flag indicating that student is currently in admit\_conditional funnel stage |
| deposit | NUMBER | Flag indicating that student is currently in deposit funnel stage |
| enroll | NUMBER | Flag indicating that student is currently in enroll funnel stage |
| withdraw | NUMBER | Flag indicating that student is currently in withdraw funnel stage |
| denied | NUMBER | Flag indicating that student is currently in denied funnel stage |
| waitlist | NUMBER | Flag indicating that student is currently in waitlist funnel stage |
| hold | NUMBER | Flag indicating that student is currently in hold funnel stage |

### el\_tasks\_raw

This table features one row per task.

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| \_id | TEXT | Unique task identifier |
| subdom | TEXT | Partner school instance identifier |
| src | VARIANT | JSON object of task properties |
| updated\_at | TIMESTAMP\_NTZ | Task last updated at timestamp |
| created\_at | TIMESTAMP\_NTZ | Task created at timestamp |
| etl\_loaded\_at | TIMESTAMP\_NTZ | Task last loaded into Snowflake timestamp |
| deleted\_at | TIMESTAMP\_NTZ | Task deleted at timestamp |

### el\_users\_raw

This table features one row per Element451 record, both internal users and student records.

|  |  |  |
| --- | --- | --- |
| **Column** | **Data Type** | **Description** |
| \_id | TEXT | Unique user record identifier, the Element ID |
| subdom | TEXT | Partner school instance identifier |
| src | VARIANT | JSON object of record properties |
| updated\_at | TIMESTAMP\_NTZ | Record last updated timestamp |
| created\_at | TIMESTAMP\_NTZ | Record created at timestamp |
| deleted\_at | TIMESTAMP\_NTZ | Record deleted at timestamp |
| etl\_loaded\_at | TIMESTAMP\_NTZ | Record last loaded into Snowflake timestamp |

---

---