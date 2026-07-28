---
title: Scheduling Import + Export
url: https://help.element451.com/en/articles/9007716-scheduling-import-export
collection: Data Management
---

Learn about regularly importing or exporting files.

# Overview

Scheduling import tasks and export tasks can be an integral part of an integration between your Student Information System or other systems. Rather than manually running these tasks every morning, week, or month, set up schedules with custom repeat settings.

---

# Scheduling Imports

## Access the Import Schedule

To access the Schedule feature:

1. Navigate to **Data + Automations > Import + Export > Imports.**
2. Edit the import you want to set the schedule up for by clicking the **Import Name**.
3. Click the **Schedule** button in the top right corner.

[![](https://downloads.intercomcdn.com/i/o/977868377/5abfee0a24ddff48fed8d4b6/Screenshot+2024-02-29+at+9_21_28%E2%80%AFAM.png?expires=1784333700&signature=22370cb1a5385a6c321c9d674e6f739d202fa7b21043330f4f64a1aa736c746c&req=fScgHs92noZYFb4f3HP0gP1UdsG1S98Ef79Sru1EsuVDILrS1XWOo70sOL8s%0A3vOTYcv9TfVKws9igA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977868377/5abfee0a24ddff48fed8d4b6/Screenshot+2024-02-29+at+9_21_28%E2%80%AFAM.png?expires=1784333700&signature=22370cb1a5385a6c321c9d674e6f739d202fa7b21043330f4f64a1aa736c746c&req=fScgHs92noZYFb4f3HP0gP1UdsG1S98Ef79Sru1EsuVDILrS1XWOo70sOL8s%0A3vOTYcv9TfVKws9igA%3D%3D%0A)

## Creating the Import Schedule

When you create an Import Schedule, you can set up a one-time import to run once in the future, or you can set up a repeated schedule.

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1369023294/0bf06f431372c62ecfc8f82c5247/Important.png?expires=1784430000&signature=c366eb91673df725d0d3668b9cd0ab6d70ece9d2e41147243ee164c2fe74c35d&req=dSMhH8l8noNWXfMW3Hu4gZtQQ75dlh0be0E9j%2BH4h0%2Bm0v%2F4bZUI%2BDp0U9Xs%0Azw%3D%3D%0A) Be mindful that the time you select for your import to run on a schedule should closely align with when the file appears in the SFTP. It may take a few minutes for the file to appear in the SFTP, so we recommend scheduling the import 15-30 minutes after you expect the file to be delivered.

1. Select a starting **Date.**
2. Toggle the **Repeat** on if you want the import to be imported regularly.
3. Select the **Period of time** of how often it will be imported.
4. Select a **Time** (Note: This is in your instance's time zone.).
5. Toggle **When no matching files are available, execute the next scheduled task run** if you want the import to continue trying to run on the next scheduled run rather than fail and stop running in the future.
6. Click **Schedule Task.**

[![](https://downloads.intercomcdn.com/i/o/976113094/c4af1aed1d2d5aeb60d19df9/Screenshot+2024-02-27+at+9_08_57%E2%80%AFPM.png?expires=1784333700&signature=ab5001f1c415cdf9265f4bede8a079c52ad39979bce9262560c93242abe7e788&req=fSchF8h9nYhbFb4f3HP0gLLnQDZ7vCWvX3zpr6qxpEM3GSlk5j%2BaSjxQyD3a%0AVSPkZ7GUjpWv26IkFw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976113094/c4af1aed1d2d5aeb60d19df9/Screenshot+2024-02-27+at+9_08_57%E2%80%AFPM.png?expires=1784333700&signature=ab5001f1c415cdf9265f4bede8a079c52ad39979bce9262560c93242abe7e788&req=fSchF8h9nYhbFb4f3HP0gLLnQDZ7vCWvX3zpr6qxpEM3GSlk5j%2BaSjxQyD3a%0AVSPkZ7GUjpWv26IkFw%3D%3D%0A)

---

# Scheduling Exports

## Access the Export Schedule

To access the Schedule feature:

1. Navigate to **Data + Automations > Import + Export > Exports.**
2. Edit the export you want to set the schedule up for by clicking the **Export Name**.
3. Click the **Schedule** button in the top right corner.

[![](https://downloads.intercomcdn.com/i/o/977869135/01e912fa51e38517089c6b93/Screenshot+2024-02-29+at+9_22_19%E2%80%AFAM.png?expires=1784333700&signature=1e998851a380cca34e9d30fadf8433423367bdda0f3b51792e6b9db774404f08&req=fScgHs93nIJaFb4f3HP0gK9xjxdSuohUlr8X6G5fCJZhC4m0E%2FyIktkbK87f%0AYiTPX2el6yt%2FTvjBwQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/977869135/01e912fa51e38517089c6b93/Screenshot+2024-02-29+at+9_22_19%E2%80%AFAM.png?expires=1784333700&signature=1e998851a380cca34e9d30fadf8433423367bdda0f3b51792e6b9db774404f08&req=fScgHs93nIJaFb4f3HP0gK9xjxdSuohUlr8X6G5fCJZhC4m0E%2FyIktkbK87f%0AYiTPX2el6yt%2FTvjBwQ%3D%3D%0A)

## Creating the Export Schedule

When you create an Export Schedule, you can set up a one-time export to run once in the future, or you can set up a repeated schedule.

1. Select a starting **Date**.
2. Toggle the **Repeat** on if you want the export to be exported regularly.
3. Select the **Period of time** of how often it will be exported.
4. Select a **Time. Note**: This is in your instance's time zone.
5. Click **Schedule Task.**

[![](https://downloads.intercomcdn.com/i/o/976119011/47ed22b9ee5b2b44fe008ee0/Screenshot+2024-02-27+at+9_22_33%E2%80%AFPM.png?expires=1784333700&signature=32eb6ac052f192b4bc24fd5f299ce786c73e6f501f827bcd05658dd6e28e6adf&req=fSchF8h3nYBeFb4f3HP0gJrhEkzJAopuJ5o%2B%2BSTTpVpVRxPTOLL9rJua7dCh%0A8vZdWwKKzPa%2B1qBhXQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/976119011/47ed22b9ee5b2b44fe008ee0/Screenshot+2024-02-27+at+9_22_33%E2%80%AFPM.png?expires=1784333700&signature=32eb6ac052f192b4bc24fd5f299ce786c73e6f501f827bcd05658dd6e28e6adf&req=fSchF8h3nYBeFb4f3HP0gJrhEkzJAopuJ5o%2B%2BSTTpVpVRxPTOLL9rJua7dCh%0A8vZdWwKKzPa%2B1qBhXQ%3D%3D%0A)

---