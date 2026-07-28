---
title: Getting Started with Profile Templates
url: https://help.element451.com/en/articles/6449965-getting-started-with-profile-templates
collection: Settings + Permissions
---

Getting started with Profile Templates

# Overview

Profile Templates in Element451 allow you to define what information appears on a user's profile. You can start with our versatile **system templates** or craft **custom** **templates** tailored to your needs.

Profile templates are dynamic, meaning they can display content based on various factors such as profile data, user characteristics, and visibility groups. Given the high customizability of these profiles, the display and accessibility of certain information may vary. This article guides you through effectively managing your profile templates.

[![](https://downloads.intercomcdn.com/i/o/1046609977/d785813ac9b17dd9a56584a0/Important+-+Orng.png?expires=1784333700&signature=cd9794b015217fe38383e6749fccdefd2ec110be63e1e86d33eef58f0cb0f229&req=dSAjEM9%2BlIhYXvMW1HO4zd4XMKYk3KF8vR1qSmJJ5MyLG5ZTq2ZgAd0DWG04%0AwRQakTPUjp0zhNMByb0%3D%0A)](https://downloads.intercomcdn.com/i/o/1046609977/d785813ac9b17dd9a56584a0/Important+-+Orng.png?expires=1784333700&signature=cd9794b015217fe38383e6749fccdefd2ec110be63e1e86d33eef58f0cb0f229&req=dSAjEM9%2BlIhYXvMW1HO4zd4XMKYk3KF8vR1qSmJJ5MyLG5ZTq2ZgAd0DWG04%0AwRQakTPUjp0zhNMByb0%3D%0A)

To edit or create Custom Templates, you must have the '***Administer Profile Templates'*** permission.

## Accessing Bolt Profile Templates

1. Click on your avatar in the top right corner of the main navigation menu.
2. Navigate to **Settings** > **Profile Templates**.

---

# Profile Template List View (System + Custom)

The Profile Templates list view shows all profile template names, descriptions, and statuses. Profile Templates are displayed in two groups:

* **Custom People Templates:** Templates created by your institution
* **System People Templates:** Templates are built and delivered by Element451

  + They can be used as the foundation for a custom template by being duplicated and customized.
  + They rank **after** Custom People Templates in order of precedence.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353460638/c7a93ef779802e55f5e3825bd60d/Profile+Templates.png?expires=1784333700&signature=c33a43d9f38d629e332a0688b44ae20dd6efe65e064931bd058e07b93cc293ef&req=dSMiFc14nYdcUfMW1HO4zZ3VArkWLBMCB9a7puczyMszv6dyo%2BNDSdDrxxSJ%0AaMIZZcOzqQektJfVEt4%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353460638/c7a93ef779802e55f5e3825bd60d/Profile+Templates.png?expires=1784333700&signature=c33a43d9f38d629e332a0688b44ae20dd6efe65e064931bd058e07b93cc293ef&req=dSMiFc14nYdcUfMW1HO4zZ3VArkWLBMCB9a7puczyMszv6dyo%2BNDSdDrxxSJ%0AaMIZZcOzqQektJfVEt4%3D%0A)

From the list view, you can take several actions:

* Activate or deactivate profile templates.
* Drag and drop reorder the list (grab the = to begin).
* Open, edit, delete, or duplicate a profile template.
* Create a new custom template.
* Duplicate a system template to use as a foundation of a custom template.

## Video Guide: Profile Template List View

---

# Order of Precedence

Filters configured in the [Profile Template settings](#h_2e5c6dfca7) determine when a particular profile template should be displayed to a user. Since it is possible for there to be more than one qualifying template, Element451 uses the order of precedence to determine which should be shown in those cases. Working from the top down, the first qualifying template will be displayed.

Custom Templates are evaluated first, then System Templates.

Generally, place the narrowest use profile at the top of the list and work down to the broadest. For example:

1. Agent Profiles
2. Family Profiles
3. Graduate Student Profiles
4. Admitted Undergraduate Student Profiles
5. International Undergraduate Student Profiles
6. Domestic Undergraduate Student Profiles
7. Default Profile

[![](https://downloads.intercomcdn.com/i/o/1046613574/22fb8ced3be57e4ced3c007a/Pro+Tip+-+Orng.png?expires=1784333700&signature=d0e29237b2de601de56870ef4b8b83c9f05e39c1aed8e41f5f189059e486929c&req=dSAjEM9%2FnoRYXfMW1HO4zT9hT6%2BAFxzbqkr1DcO9L4VZ3pGJAXhY0vhYY9bF%0AArTbRvhGql7Pjy3xCS4%3D%0A)](https://downloads.intercomcdn.com/i/o/1046613574/22fb8ced3be57e4ced3c007a/Pro+Tip+-+Orng.png?expires=1784333700&signature=d0e29237b2de601de56870ef4b8b83c9f05e39c1aed8e41f5f189059e486929c&req=dSAjEM9%2FnoRYXfMW1HO4zT9hT6%2BAFxzbqkr1DcO9L4VZ3pGJAXhY0vhYY9bF%0AArTbRvhGql7Pjy3xCS4%3D%0A)

Create a custom "default" template without filters and put it at the bottom of your custom profiles list. This will prevent system templates from being displayed.

---

# Creating or Editing a Custom Profile Template

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353819701/1fb72395100dac48679762e66e73/Templates-Editing.png?expires=1784333700&signature=6468684d68046695dfa2d6b822e35294551ba01df89bcffeb06d41281d98857c&req=dSMiFcF%2FlIZfWPMW1HO4zRnVRsiFCaT8CBVM%2BMAemJ4flRlUEAvSMRKsvDtP%0AdVxCVE2MxRCpXdqIPYQ%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1353819701/1fb72395100dac48679762e66e73/Templates-Editing.png?expires=1784333700&signature=6468684d68046695dfa2d6b822e35294551ba01df89bcffeb06d41281d98857c&req=dSMiFcF%2FlIZfWPMW1HO4zRnVRsiFCaT8CBVM%2BMAemJ4flRlUEAvSMRKsvDtP%0AdVxCVE2MxRCpXdqIPYQ%3D%0A)

## Creating New Templates

* Navigate to **Settings** > **Profile Templates**.
* Click on the **+ Create Template**button.

  + [![](https://downloads.intercomcdn.com/i/o/1046615374/15c78082f61413a68e8d8214/Pro+Tip+-+Orng.png?expires=1784333700&signature=7c5dc55979aebe7a166b5359a051ad501b41014c415e741a1ebe8d3503f73696&req=dSAjEM9%2FmIJYXfMW1HO4zdnqGHpsTbwZ7AFuBqijOb8T1sK8ieA%2F4ci2FQqL%0AXMOG%0A)](https://downloads.intercomcdn.com/i/o/1046615374/15c78082f61413a68e8d8214/Pro+Tip+-+Orng.png?expires=1784333700&signature=7c5dc55979aebe7a166b5359a051ad501b41014c415e741a1ebe8d3503f73696&req=dSAjEM9%2FmIJYXfMW1HO4zdnqGHpsTbwZ7AFuBqijOb8T1sK8ieA%2F4ci2FQqL%0AXMOG%0A)

    You can also create a new custom profile template by **duplicating** an existing template (system or custom).
* Configure the settings using the four tabs: settings, header, sidebar, and main. We explain these settings in detail in the next article, [Configuring Profile Templates](https://intercom.help/element451/en/articles/10471008-configuring-profile-templates-in-element451).

## Editing + Managing Existing Templates

* Navigate to **Settings** > **Profile Templates**.
* Locate the template you wish to edit or manage.
* Click on the vertical ellipsis **⋮** next to it.
* From there, you can select to open, edit, delete, or duplicate.

## Profile Template Configurations

When editing or creating a profile template, you’ll find four tabs at the top of the side sheet. Each tab lets you customize the template to fit your needs. We go into detail on each one in our [Configuring Profile Templates](https://intercom.help/element451/en/articles/10471008-configuring-profile-templates-in-element451) article.

[Explore More: Profile Template Configurations](https://help.element451.com/en/articles/10471008-configuring-profile-templates-in-element451)

---