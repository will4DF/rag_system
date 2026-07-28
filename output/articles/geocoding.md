---
title: Geocoding
url: https://help.element451.com/en/articles/8834728-geocoding
collection: People
---

Learn about Geocoding, a filtering feature that allows you to use the distance from a specific address to segment users.

# Overview

Element451 offers a geocoding service that makes it easy to use a filter to segment users based on their distance from a specific address.

Geocoding is the process of converting addresses (like "1 Glenwood Ave, Raleigh, NC") into geographic coordinates (like 35.7779° N, -78.6420° W).

Harnessing the power of geocoding in your user segmentation means your communication is not just targeted; it's location-smart. It's about reaching the right students in the right place at the right time.

## Important Considerations

* Only United States and Canada addresses can be geocoded.
* `Street_1` is a required field for geocoding.

---

# Add a Geo Filter

[![](https://downloads.intercomcdn.com/i/o/989213047/29b54969c19b8e8163dff457/Note-Orng.png?expires=1784333700&signature=8582991d61217684351b799405dcec13830ae60936cc48cf7e24c1e8d0872f0e&req=fSguFMh9nYVYFb4f3HP0gDpzDL%2BCGLr3BCaYqk72KWTKQMBmmv%2BhX5kADE6i%0AqVz7yJAZFYQ2sP9JQQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/989213047/29b54969c19b8e8163dff457/Note-Orng.png?expires=1784333700&signature=8582991d61217684351b799405dcec13830ae60936cc48cf7e24c1e8d0872f0e&req=fSguFMh9nYVYFb4f3HP0gDpzDL%2BCGLr3BCaYqk72KWTKQMBmmv%2BhX5kADE6i%0AqVz7yJAZFYQ2sP9JQQ%3D%3D%0A)

Before starting this process, we recommend having a good understanding of [Filters + Segments](https://help.element451.com/en/collections/124543-filters-segments).

Geocoding is used when you apply the **Address Location** filter in the People Module (**Contacts** > **People**).

[![](https://downloads.intercomcdn.com/i/o/936315285/f2c4621fdbc830c9251d7e22/Screenshot+2024-01-17+at+1.14.56%E2%80%AFPM.png?expires=1784333700&signature=a8bc959d2d078f8c1a67f93f3fb36eca708aa19b6d9734e45293923096ac0d4a&req=fSMhFch7n4laFb4f3HP0gM5PFH6j0G70jcjUxBDjZ8DfqWjKq7TMTGsanthj%0A8qjl%2FHjtphgtvEL4Kg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/936315285/f2c4621fdbc830c9251d7e22/Screenshot+2024-01-17+at+1.14.56%E2%80%AFPM.png?expires=1784333700&signature=a8bc959d2d078f8c1a67f93f3fb36eca708aa19b6d9734e45293923096ac0d4a&req=fSMhFch7n4laFb4f3HP0gM5PFH6j0G70jcjUxBDjZ8DfqWjKq7TMTGsanthj%0A8qjl%2FHjtphgtvEL4Kg%3D%3D%0A)

Once you select the **Address** **Location** filter, you will configure the constraints:

* **Operator**: Distance From
* **Address**: The address from which to measure. Beginning to type here will bring up an auto-complete using Google Maps to assist you in finding the exact address.
* **Count**: Select one:

  + ***At most*** *(*will include all users whose location is within that distance)
  + ***At least*** *(*will include all users whose location is beyond that distance)
* **Distance**: The number of miles/kilometers you would like to set as a maximum distance from the chosen address
* **Unit**: Choose to measure in miles or kilometers

[![](https://downloads.intercomcdn.com/i/o/936313842/f0837a5b720c7f3284adcfc8/Screenshot+2024-01-17+at+1.14.30%E2%80%AFPM.png?expires=1784333700&signature=eca3147b9babef44ff58e7f7b37832d811fc1693a3bd10990b98973e021b2a0b&req=fSMhFch9lYVdFb4f3HP0gAZBylMdFUcUVClzVeo101jRQNfUlN3Bowt8%2Bgbx%0A68frJyhzx47ozLBvqw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/936313842/f0837a5b720c7f3284adcfc8/Screenshot+2024-01-17+at+1.14.30%E2%80%AFPM.png?expires=1784333700&signature=eca3147b9babef44ff58e7f7b37832d811fc1693a3bd10990b98973e021b2a0b&req=fSMhFch9lYVdFb4f3HP0gAZBylMdFUcUVClzVeo101jRQNfUlN3Bowt8%2Bgbx%0A68frJyhzx47ozLBvqw%3D%3D%0A)

---

# Use Case

Combine the power of location with other filters, like survey responses, to create ultra-focused segments.

For example, you can easily craft a segment of '**Local Students Who Answered a Survey,**' pinpointing students within a certain distance from your campus who engaged with your survey. This allows for incredibly targeted communication and analysis, ensuring your messages are as relevant and personalized as possible.

---