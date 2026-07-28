---
title: The Element451 Data Model
url: https://help.element451.com/en/articles/9824701-the-element451-data-model
collection: Data Management
---

Understand how Element451 structures data in its database.

# What is a Data Model?

A data model refers to how data is structures in a database and how different types of data relate to each other.

Even if you never see this data structure, you'll interact with it every time you use Element451. Understanding the data model can help you better anticipate how your actions in Element451 will access, change, and use this data.

# The Contact-centric Data Model

Element451 is a ***contact-centric*** platform, meaning the "contact" or student record, is the primary data object. All other data objects, (applications, events, milestones, evaluations) are stored as "properties" of the contact. Contrast this to other systems that might store applications in a separate database from contacts.

## Example Contact Record

A contact record in Element451's database looks something like this:

```
{  
   first_name: "Jessica",  
   last_name: "Student",  
   email: "jessica.student@element451.com",  
   element_id: "382075100334",  
   applications: [  
      {  
        registration_id: "849F3PO",  
        app_type: "Incoming Freshman"  
        major: "Dancing",  
        term: "Fall",  
        student_type: "Freshman",  
        index_weight: 1  
      },  
      {  
        registration_id: "R2D29F1",  
        app_type: "Graduate & Doctorate"  
        major: "Underwater Basket Weaving",  
        term: "Summer",  
        student_type: "Graduate"  
        index_weight: 2  
      },  
   ],  
   evaluations: [  
      {  
        type: "SAT",  
        math_score: "500",  
        reading_writing_score: "510",  
        test_date: "2020-05-01",  
        index_weight: 1  
       }  
   ],  
   ...  
}
```

Everything between the top and bottom curly brace, "{", is the contact record.

Each property of the user has a name (i.e., "email") and a value ("[test@element451.com](mailto:test@element451.com)").

## Direct Attributes vs Repeaters

Note that some properties only have one value, such as *name* and *email*. These are **"direct" properties** of the contact. They can only have one value at a time.

Other properties, such as *applications* and *evaluations* are opened by a bracket, "[".

This indicates that the property will have more than one value. These are called arrays which contain "**repeaters**". The *applications* array above has two "repeaters" within, each representing a unique application that the contact created. Repeaters have a **many-to-one relationship** with the contact.

This concept or repeaters powers the ["Repeat fields based on:"](https://help.element451.com/en/articles/9007317-creating-exports#h_32db4b2e5b) of the Exports module, the [Star Mappings](https://help.element451.com/en/articles/9824701-the-element451-data-model) available to Import and Export tasks, and [repeatable sections](https://help.element451.com/en/articles/9040630-creating-managing-applications#h_9b16931a43) of an application.

# Other Data Objects

While the contact is the primary object in the model, other objects exist independently. Though they exist separately, they reference a single contact directly. These three examples are commonly used but several more exist.

## The Activity Object

Key to student engagement, [activities](https://help.element451.com/en/articles/5159877-activity-feed-overview) log when contacts or internal users complete an action. Here is an abridged example:

### Activity Example Data

```
{    
  "_id": "64d378b7bb3abf8046415",    
  "action": "emailOpened",  
  "campaign_guid": "instance.communications.79243",  
  "campaign_title": "New Student Welcome Night",   
  "element_id": "64d247c9cb8110ff958",  
  "email_subject": "[user:first_name], you're invited!",  
  "from_email": "admissions@instance.edu",  
  "timestamp": "2023-08-09T11:29:59.086000",  
  "to_email": "jessica.student@element451.com",  
  "variant_id": "default"  
}
```

Note that this example is an email open, found in the "action" property. The action also references the contact in the "element\_id" property. **Each activity references a single contact.** If the email was opened by 150 contacts, each contact would have an emailOpened activity.

## The Decision Object

As shown above, when a contact creates an application it is saved to the contact record. However, when the application is submitted it is simultaneously registered as a decision. Decisions log the contact's application information and their status in the decision process that you configure in [Decisions Settings](https://help.element451.com/en/collections/9390605-decisions-settings). It looks a bit like this:

### Decision Example Data

```
{  
  "_id": "66dac1990c5f6d02fc1",  
  "application": "Incoming Freshman",  
  "assigned_to": "Sarah Staff",  
  "board": {  
    "stage": "In Review",  
    "status": "Awaiting Transcript"  
  },  
  "checklist": [  
    {  
      "item_key": "test_score",  
      "status": "uncompleted",  
      "type": "one_off",  
      "updated_by": "checklist_condition_evaluator",  
      "visible": false  
    },  
    {  
      "item": "transcript",  
      "status": "uncompleted",  
      "type": "one_off",  
      "updated_by": "checklist_condition_evaluator",  
      "visible": true  
    },  
  "cohorts": [  
    "FTEQMYFY",  
    "DTW0DUS1"  
  ],  
  "created_at": "2024-09-06T08:47:21.569000",  
  "element_id": "66da49b015abd008bff",  
  "registration_id": "RQMSDORB",  
  "score": 70,  
  "visibility_groups": [  
    "all"  
  ]  
}
```

Note that the Decisions stores checklist, cohort and board information, as well as items like score, criteria and more. Each decision is assigned to one student.

## The Task Object

The task object stores the status of the task, the student it is related to and the staff member it is assigned to.

### Task Example Data

```
{  
  "_id": "64ba9084f21bb2b7050a5dd5",  
  "assigned_to": [  
    "Sarah Staff"  
  ],  
  "created_at": "2024-07-21T14:04:52.953000",  
  "description": "Contact the student.",  
  "done_at": "2023-07-21T18:56:07.946000",  
  "due_datetime": "2023-07-21T14:02:00",  
  "name": "Initial Outreach Call",  
  "notes": [  
    {  
      "author_id": "Sarah Staff",  
      "body": "Reached out to student, had productive discussion.",  
      "created_at": "2024-07-21T18:56:04",  
      "updated_at": "2024-07-21T18:56:04"  
    }  
  ],  
  "queue_references": [  
    "Staff Tasks"  
    ],  
  "related_to": "Jessica Student",  
  "status": "done",  
  "type": "Outreach Call"  
}
```

# The Data Model in Action

Now that we've seen how Element451 structures the data at the core of the CRM, let's see that data in action throughout the platform.

## Person Profile Cards

The Person Profile can be configured with a to display a set of [Cards](https://help.element451.com/en/articles/1475735-the-person-profile#h_8456eb5949) in the Main display area. Many of these cards correspond directly to the sections or repeaters of data on the contact record. For example, the Applications card displays the data in the applications repeater.

```
applications: [  
      {  
        registration_id: "849F3PO",  
        app_type: "Incoming Freshman"  
        major: "Dancing",  
        term: "Fall",  
        student_type: "Freshman",  
        index_weight: 1  
      },  
      {  
        registration_id: "R2D29F1",  
        app_type: "Graduate & Doctorate"  
        major: "Underwater Basket Weaving",  
        term: "Summer",  
        student_type: "Graduate"  
        index_weight: 2  
      },  
   ],
```

[![](https://downloads.intercomcdn.com/i/o/1185864681/0f3bcdbea844852dfaf951b0/Screenshot%2B2024-09-16%2Bat%2B11_45_08-E2-80-AFAM.png?expires=1784333700&signature=7518b589061a1118643bd338933cdc7102ed73cbe8d434c4ee6410b7f1ea0c24&req=dSEvE8F4mYdXWPMW1HO4zfQ%2FIOhV%2FVzqfAq79QnSTQvTBujG%2Bw1W9PcvPtlq%0ABagLHpxsM%2BxTu3Z6SO0%3D%0A)](https://downloads.intercomcdn.com/i/o/1185864681/0f3bcdbea844852dfaf951b0/Screenshot%2B2024-09-16%2Bat%2B11_45_08-E2-80-AFAM.png?expires=1784333700&signature=7518b589061a1118643bd338933cdc7102ed73cbe8d434c4ee6410b7f1ea0c24&req=dSEvE8F4mYdXWPMW1HO4zfQ%2FIOhV%2FVzqfAq79QnSTQvTBujG%2Bw1W9PcvPtlq%0ABagLHpxsM%2BxTu3Z6SO0%3D%0A)

## Understanding Import + Export Mappings

Seeing how the contact record is constructed, we can notice that [Import + Export mappings](https://help.element451.com/en/articles/9001231-creating-imports#h_d4d5c816b1) act as "paths" to locations on the contact record.

For example, `user-first-name`

1. "user" denotes that this mapping accessed the contact, or "user", record.
2. "first-name" then points to the first\_name attribute that we see above.

Another example, `user-applications-major`

1. "applications" points to the applications array
2. "major" points to the major attribute of an application object.

## Segment Filter Colors for Property Types

Element451 offers many different Filters to help you narrow down groups of people based on conditions. Those Filters are categorized by Type. Read more [here](https://help.element451.com/en/articles/8800347-filters-property-types).

[![](https://downloads.intercomcdn.com/i/o/1185863346/1aa26f7ed140928f5b1dd0a9/Screenshot%2B2024-09-09%2Bat%2B1_20_13-E2-80-AFPM.png?expires=1784333700&signature=900dc7d3b98426883aa122b085277a87a045f92442283ac213e87f8fc4f5f749&req=dSEvE8F4noJbX%2FMW1HO4zRJCN8ySXUyVrUYvsWQOASELOOG%2FVDcpP78vjD0f%0AVz6JPp1QE5mntabShTw%3D%0A)](https://downloads.intercomcdn.com/i/o/1185863346/1aa26f7ed140928f5b1dd0a9/Screenshot%2B2024-09-09%2Bat%2B1_20_13-E2-80-AFPM.png?expires=1784333700&signature=900dc7d3b98426883aa122b085277a87a045f92442283ac213e87f8fc4f5f749&req=dSEvE8F4noJbX%2FMW1HO4zRJCN8ySXUyVrUYvsWQOASELOOG%2FVDcpP78vjD0f%0AVz6JPp1QE5mntabShTw%3D%0A)

Notice that different filter property types correspond to different data objects. Light blue corresponds to the contact object, purple to Decisions, and brown to Tasks. For a complete list of categories, visit our [Property Types](https://intercom.help/element451/en/articles/8800347-filters-property-types) help article.

---