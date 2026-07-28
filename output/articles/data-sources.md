---
title: Data Sources
url: https://help.element451.com/en/articles/2066888-data-sources
collection: Data Management
---

Learn how to add, edit, and manage your school's Data Sources.

# Overview

Data Sources are the backbone of your dropdown, radio, and checkbox fields within Element451. This tool is how you manage the values in each lookup field, which are used on your forms, landing pages, applications, and more.

## Accessing Data Sources

Navigate to **Data + Automations** > **Data** **Sources**.

[![](https://downloads.intercomcdn.com/i/o/1084898719/4a25a0fb61d0d1d0d629bae4/Screenshot+2024-06-17+at+5_05_22%E2%80%AFPM.png?expires=1784333700&signature=419f066164e730bf9942e02a62c634a7e40c8d0f9b1256fbc7ed73e7f8940cc1&req=dSAvEsF3lYZeUPMW1HO4zZE04R5fvkWdFsDhH2%2BRo9CJZnc7AH%2FWO1m%2BNx%2F5%0AQHOmPzcKPdQY8OYm0M8%3D%0A)](https://downloads.intercomcdn.com/i/o/1084898719/4a25a0fb61d0d1d0d629bae4/Screenshot+2024-06-17+at+5_05_22%E2%80%AFPM.png?expires=1784333700&signature=419f066164e730bf9942e02a62c634a7e40c8d0f9b1256fbc7ed73e7f8940cc1&req=dSAvEsF3lYZeUPMW1HO4zZE04R5fvkWdFsDhH2%2BRo9CJZnc7AH%2FWO1m%2BNx%2F5%0AQHOmPzcKPdQY8OYm0M8%3D%0A)

---

# Data Source Types

When you navigate to the Data Sources page in your Element451 instance, you'll see 8 different tabs--each representing a data source type.

[![](https://downloads.intercomcdn.com/i/o/1084899828/ad9b0f54b6cfc989e28b7be5/Screenshot+2024-06-17+at+5_07_05%E2%80%AFPM.png?expires=1784333700&signature=760aa5fbbe9072245d05ef7254a1b239de04b4d2239d3bbeb9bd3e6280c06c65&req=dSAvEsF3lIldUfMW1HO4zbx70p2wxvufCScx1AZSHLYepgFdwy95x8iRhs9Q%0ALbaQD5tQ%2B%2FqL%2FPE21Ew%3D%0A)](https://downloads.intercomcdn.com/i/o/1084899828/ad9b0f54b6cfc989e28b7be5/Screenshot+2024-06-17+at+5_07_05%E2%80%AFPM.png?expires=1784333700&signature=760aa5fbbe9072245d05ef7254a1b239de04b4d2239d3bbeb9bd3e6280c06c65&req=dSAvEsF3lIldUfMW1HO4zbx70p2wxvufCScx1AZSHLYepgFdwy95x8iRhs9Q%0ALbaQD5tQ%2B%2FqL%2FPE21Ew%3D%0A)

* **System Data Sources**: Pre-made data sources that cannot be changed. System data sources correspond to pre-existing system fields, like citizenship, country list, or gender. They are denoted by `[SYS`] in the title. By default, all dropdown, radio, and checkbox fields in Element451 are connected to a system data source.  
  ​

  [![A screenshot of the Element interface, showing the System Data Sources tab. A sample data source is displayed.](https://downloads.intercomcdn.com/i/o/668576428/cf5d202db7cdf58ae8108bc9/Screenshot+2023-02-08+at+10.21.03+AM.png?expires=1784333700&signature=a6efefafa1af4f67332cfd51a8600c71c342930bb352933a9c6fe9461c12c3da&req=ciYvE854mYNXFb4f3HP0gE4gj4a%2FW1zK2Emtm5i7WJqCrB%2FLQKGSSvcEtgCr%0A4e0%3D%0A)](https://downloads.intercomcdn.com/i/o/668576428/cf5d202db7cdf58ae8108bc9/Screenshot+2023-02-08+at+10.21.03+AM.png?expires=1784333700&signature=a6efefafa1af4f67332cfd51a8600c71c342930bb352933a9c6fe9461c12c3da&req=ciYvE854mYNXFb4f3HP0gE4gj4a%2FW1zK2Emtm5i7WJqCrB%2FLQKGSSvcEtgCr%0A4e0%3D%0A)
* **Regular Data Sources:** These data sources are used to build an entirely new and custom data source to fit your institution. If the system data sources do not fit your needs, you can substitute them with a regular data source. Additionally, if there is data you would like to collect that is not offered by a system data source, you can create a regular data source to capture that data.

  + It is common to denote a regular data source with your institution's name, like this `[SCHOOL-NAME]` in the name. Doing so will help regular data sources be distinguished from system data sources.

  Follow the steps in the next section to create a regular data source.
* **Majors, Terms, Degrees, Campuses, Tests, Schools, and Courses:** These are the master lists of all of your institution's majors, terms, degrees, campuses, tests, and schools. [Learn how to individually add or import groups of majors, terms, or campuses.](https://help.element451.com/en/articles/3152502-adding-majors-terms-or-campuses)

---

# Reference Data Source

Reference Data Sources are sub-groupings of your Majors, Terms, Degrees, etc. They are narrowed down by specific properties within those categories (e.g., Fall 2024 Majors).

![](https://downloads.intercomcdn.com/i/o/1084902406/2555beb8c65ca30661c104ee/Pro+Tip+-+Orng.png?expires=1784430000&signature=da6a2afa7cf10b80508159f83f52563735f482658799547c4142719f48be7c9c&req=dSAvEsB%2Bn4VfX%2FMW3Hu4gWEeZEsoMJg36juEyNmjGrITi%2FlkDdHHS5yIy5ac%0Asg%3D%3D%0A) Reference data sources are helpful if you would like to build a form that only looks at majors that are available only in a certain term or only active terms going forward rather than all terms (including past terms).

Follow the steps in the next section to create a reference data source.

---

# Creating New Data Sources

## Creating a Regular Data Source

A Regular Data Source will allow you to build a new data source from the ground up. Read more about them [above](https://help.element451.com/en/articles/2066888-data-sources#h_1b2553a10d).

1. From the **Regular Data Source Tab,** click **Add Data Source** *o*n the bottom left.
2. Configure the settings. You will see three tabs: general, columns, and defaults.

   * **General**

     + Enter a name for your data source.
     + Specify if it is active or inactive.
   * **Columns**

     + Add the number of columns necessary to store all the qualifiers of the data points. **Label** and **Value** are the two most common columns used.   
       ​

       [![](https://downloads.intercomcdn.com/i/o/134762748/d54f9af4179d0dcf28615826/Screen+Shot+2019-07-16+at+4.25.04+PM.png?expires=1784333700&signature=386f96e33b7dfc62ba2b1c6fb00a531d0a1239c0c12657fad2c9fec507780ec2&req=dSMjEc98moVXFb4f3HP0gGejTFjJ3yNvedUvQhNO0ZddE0Xcb4aqZrcfYqPo%0A%2FQo%3D%0A)](https://downloads.intercomcdn.com/i/o/134762748/d54f9af4179d0dcf28615826/Screen+Shot+2019-07-16+at+4.25.04+PM.png?expires=1784333700&signature=386f96e33b7dfc62ba2b1c6fb00a531d0a1239c0c12657fad2c9fec507780ec2&req=dSMjEc98moVXFb4f3HP0gGejTFjJ3yNvedUvQhNO0ZddE0Xcb4aqZrcfYqPo%0A%2FQo%3D%0A)
   * **Defaults**

     + **Use as code:** Select the column you want to be used as a unique identifier.
     + ​**Use as label:** Select the column that you want to display on the student-facing form.   
       ​

       [![](https://downloads.intercomcdn.com/i/o/482729548/26fff251f671950e419865ea/Screen+Shot+2022-03-18+at+2.48.59+PM.png?expires=1784333700&signature=49ab80b174ea8e6ffd831e6de9592b300cf4a812ed0894998c29bfc020b66aac&req=cCglEct3mIVXFb4f3HP0gHyU8j1OvqP4uaRNlRRPTB%2Fa9xFA1zzA0diKMAci%0AK9I%3D%0A)](https://downloads.intercomcdn.com/i/o/482729548/26fff251f671950e419865ea/Screen+Shot+2022-03-18+at+2.48.59+PM.png?expires=1784333700&signature=49ab80b174ea8e6ffd831e6de9592b300cf4a812ed0894998c29bfc020b66aac&req=cCglEct3mIVXFb4f3HP0gHyU8j1OvqP4uaRNlRRPTB%2Fa9xFA1zzA0diKMAci%0AK9I%3D%0A)
3. Lastly, click **Done** to create your regular data source and begin using it with your dropdown, radio, or checkbox fields. Learn more about [Fields](https://help.element451.com/en/articles/9118615-field-management).

## Creating a Reference Data Source

1. Navigate to the corresponding tab of the data source that you want to create (majors, terms, campuses, etc.).
2. [Add your majors individually or import a group of your institution's majors, terms, or campuses.](https://help.element451.com/en/articles/3152502-adding-majors-terms-or-campuses)
3. Click **Add Reference Data Source** on the bottom left.
4. Configure the settings. You will see two tabs: general and data.

   * **General**

     + Enter a name for your data source.
     + Specify if it is active or inactive.   
       ​

       [![](https://downloads.intercomcdn.com/i/o/134758577/bdc8685c4df2a5e86ec0d196/Screen+Shot+2019-07-16+at+4.07.48+PM.png?expires=1784333700&signature=5630a3e7694afa3b19d58d1be5337dde4d3d7a5c2fd8de1052ec825f113ceeec&req=dSMjEcx2mIZYFb4f3HP0gHIICAstymrw0CngvF14BsaOdBQktwUCAgierUyR%0AX9U%3D%0A)](https://downloads.intercomcdn.com/i/o/134758577/bdc8685c4df2a5e86ec0d196/Screen+Shot+2019-07-16+at+4.07.48+PM.png?expires=1784333700&signature=5630a3e7694afa3b19d58d1be5337dde4d3d7a5c2fd8de1052ec825f113ceeec&req=dSMjEcx2mIZYFb4f3HP0gHIICAstymrw0CngvF14BsaOdBQktwUCAgierUyR%0AX9U%3D%0A)
     + **Data**

       - Use the "filter data" section to select the properties that you want to filter down your list of majors, terms, or campuses. In this example, we are making a data source containing all active majors (see screenshot).   
         ​

         [![](https://downloads.intercomcdn.com/i/o/134758985/d4da3918f8df22131bee401f/Screen+Shot+2019-07-16+at+4.08.44+PM.png?expires=1784333700&signature=a15db587731b4d31b4900bae53789edcc57b932296e37bb152a159f93b654254&req=dSMjEcx2lIlaFb4f3HP0gC%2BYuQHNYmL9PTCNRjI6akidaGhs9xC6A964fA9B%0AQo0%3D%0A)](https://downloads.intercomcdn.com/i/o/134758985/d4da3918f8df22131bee401f/Screen+Shot+2019-07-16+at+4.08.44+PM.png?expires=1784333700&signature=a15db587731b4d31b4900bae53789edcc57b932296e37bb152a159f93b654254&req=dSMjEcx2lIlaFb4f3HP0gC%2BYuQHNYmL9PTCNRjI6akidaGhs9xC6A964fA9B%0AQo0%3D%0A)
5. Once you specified your properties, click **Done** to create the data source and begin using it to populate your dropdown, radio, or checkbox fields. Learn more about [Fields](https://help.element451.com/en/articles/9118615-field-management).

---

# Filtering Data Sources: Field Order for Proper Filtering

When setting up filters for data sources, **each source can only be filtered by another source that appears to its right** in the following order:

**Schools → Campuses → Degrees → Majors → Terms → Tests**

This means that the **order of fields in your form or application matters.** If a field appears **before** the field that is supposed to filter it, the filtering will not work. For example:

✅ If **Major** comes first, the Term list can be filtered by Major.

❌ If **Term** comes first, filtering Term by Major will **not** work.

Review the order of fields in your form or application to ensure filters function correctly and align them with the **right-to-left** filtering structure. Additionally, you should review your 'available for' properties. For example, if Accounting is available in Spring 2026, you'll need to add that term within the Accounting Major settings.

##

---