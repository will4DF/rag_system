---
title: Assignment Behavior
url: https://help.element451.com/en/articles/8857504-assignment-behavior
collection: Workflows + Rules
---

Learn about the assignment behavior settings (Selected, Rotational, Balanced) in Workflows + Rules when adding or changing an assignee.

# Overview

The ***Change Assignee*** action in Workflows + Rules offers three distinct assignment behaviors. Each option caters to specific organizational preferences and workload distribution strategies. Whether you aim for consistent involvement, orderly rotation, or a balanced workload among your team, this setting ensures that person records are efficiently managed and assigned.

---

# Assignment Types + Explanations

## Selected

* Assigns person records to all user(s) listed in the *Assigned To* field

## Rotational

* Assigns person records to a single user listed in the *Assigned To* field on a rotational basis

When each person on the list has received an assigned user, the rotation will start back at the beginning.

The rotation history automatically resets every month, regardless of whether it has reached all users in the cycle or not. After this reset, the workflow begins anew, starting with the first user in the rotation rather than continuing from the last point.

* Tip: If you often have just a few assignments each month, consider opting for a balanced assignment method instead. This approach considers the total workload for each user on the list, ensuring tasks are distributed more evenly.

## Balanced Assignment

* Assigns users to a single user listed in the *Assigned To* field on a balanced basis
* Balanced Assignment evaluates the workload of each user listed in the "Assigned To" field and assigns the record to the user with the least number of assignments.
* If only one user or team is listed in the "Assigned To" field, all records are assigned to them, and Balanced Assignment does not apply.

Balanced means that the Workflow or Rule will give the assignment to the user with the lowest number of assigned person records. Thus, this feature balances out the assignments for all individuals in that particular *Assigned To* field. For example, if three team members (A, B, and C) are listed in the "Assigned To" field, and their current assignments are 5, 3, and 7 respectively, a new record will be assigned to Team Member B, as they have the lowest number of assignments. However, if only Team Member A is listed, all new records will be assigned to them regardless of their workload.

---