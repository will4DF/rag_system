---
title: Understanding Score Calculations + Weighted Criteria
url: https://help.element451.com/en/articles/9261175-understanding-score-calculations-weighted-criteria
collection: Decisions
---

Gain a deeper understanding of how Decision scores are calculated using weighted criteria.

# Overview

To provide a clear understanding of how weighted scoring impacts applicant evaluations, we’ll explore two scenarios: one using the Global (single reviewer) criteria and another with the Per Reviewer (multiple reviewers) criteria.

Before you proceed, it's crucial to familiarize yourself with our **[Decisions Criteria](https://help.element451.com/en/articles/9210619-decisions-criteria)** article. This will significantly enhance your understanding of the examples we're about to explore.

Remember, each criterion's importance in the overall evaluation process is defined by its weight. The weights indicate the relative importance of each criterion in the final score, allowing evaluators to prioritize certain aspects of an applicant's application.

---

# Scenario 1 (Global)

[![](https://downloads.intercomcdn.com/i/o/1036526953/81ea73dfea5e6e50b1492b5b/Decisions+-+Scenario+one.png?expires=1784333700&signature=4ef2dcc53c03ef9ab653e3efd772a9853eb339903bcb36abcf1861647f9a628b&req=dSAkEMx8m4haWvMW1HO4zZ07aQTE6sTAw0drWAUVOnV2W0xLtDZB2XYbG4b7%0A6rJ5yKCTc8row62im0s%3D%0A)](https://downloads.intercomcdn.com/i/o/1036526953/81ea73dfea5e6e50b1492b5b/Decisions+-+Scenario+one.png?expires=1784333700&signature=4ef2dcc53c03ef9ab653e3efd772a9853eb339903bcb36abcf1861647f9a628b&req=dSAkEMx8m4haWvMW1HO4zZ07aQTE6sTAw0drWAUVOnV2W0xLtDZB2XYbG4b7%0A6rJ5yKCTc8row62im0s%3D%0A)

In this scenario, an applicant has a score of **5** based on the following scores for each criterion.

|  |  |  |
| --- | --- | --- |
| **Criterion** | **Score** | **Weight** |
| Class Rank | 2 out of 4 | 5 |
| GPA | 1 out of 4 | 8 |
| Essay | 3 out of 4 | 4 |
| Letters of Rec | 1 out of 1 | 2 |

## How was the score calculated?

1. **Convert Scores to Proportions**

   First, each criterion score is turned into a proportion to standardize the scores across different criteria. Divide the score the student received by the highest possible score:

   * **Class Rank**: 2 ÷ 4 = 0.5
   * **GPA**: 1 ÷ 4 ​= 0.25
   * **Essay**: 3 ÷ 4 = 0.75
   * **Letters of Recommendation**: 1 ÷ 1 = 1.0
2. **Apply Weights**

   You assigned each criterion a different "weight," which shows how important it is in the overall evaluation. Multiply each proportion by its weight to get a weighted score:

   * **Class Rank**: 0.5 × 5 = 2.5
   * **GPA**: 0.25 × 8 = 2.0
   * **Essay**: 0.75 × 4 = 3.0
   * **Letters of Recommendation**: 1.0 × 2 = 2.0
3. **Sum Up Weighted Scores**

   Add all the weighted scores together to get a total scorethat reflects the overall performance of a student across all evaluated criteria.  
   ​

   * **Total Weighted Score**: 2.5 + 2.0 + 3.0 + 2.0 = 9.5
4. **Normalize the Score**

   To ensure the final score fits the scale of 0-10, we normalize it. Divide the total weighted score by the sum of all the weights and then multiply by the maximum score.

   * **Sum of Weights**: 5 + 8 + 4 + 2 = 19
   * **Normalized Score**: 9.5 ÷ 19 × 10 = 5.0

##

---

# Scenario 2 (Per Reviewer)

[![](https://downloads.intercomcdn.com/i/o/1036559880/84d54153ca49ff39a2ae3450/Screenshot+2024-04-29+at+4_43_10%E2%80%AFPM.png?expires=1784333700&signature=eff34cea1d165b93870bd925f97e4b3005c4f2a47d18aaf7d1c9194b9f0437d1&req=dSAkEMx7lIlXWfMW1HO4zQfrp9Zv%2F09sIjJ%2BNyS6Su4jVklUShOBUzRUfjXs%0Ae70bvKz5vI0EX%2Fgk9KQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1036559880/84d54153ca49ff39a2ae3450/Screenshot+2024-04-29+at+4_43_10%E2%80%AFPM.png?expires=1784333700&signature=eff34cea1d165b93870bd925f97e4b3005c4f2a47d18aaf7d1c9194b9f0437d1&req=dSAkEMx7lIlXWfMW1HO4zQfrp9Zv%2F09sIjJ%2BNyS6Su4jVklUShOBUzRUfjXs%0Ae70bvKz5vI0EX%2Fgk9KQ%3D%0A)

In this scenario, an applicant has a score of **8** based on the following scores for each criterion.

|  |  |  |  |
| --- | --- | --- | --- |
| **Criterion** | **Score (Reviewer 1)** | **Score (Reviewer 2)** | **Weight** |
| Class Rank | 3 out of 4 | 2 out of 4 | 5 |
| GPA | 3 out of 4 | 4 out of 4 | 8 |
| Essay | 3 out of 4 | 2 out of 4 | 4 |
| Letters of Rec | 1 out of 1 | 1 out of 1 | 2 |

## How was the score calculated?

1. **Convert Scores to Proportions**

   First, each criterion score is turned into a proportion to standardize the scores across different criteria. Divide the score the student received by the highest possible score:

   ​**Reviewer 1:**

   * Class Rank: 3 ÷ 4 = 0.75
   * GPA: 3 ÷ 4 = 0.75
   * Essay: 3 ÷ 4 = 0.75
   * Letter of Recommendation: 1 ÷ 1 = 1.0

   ​**Reviewer 2:**

   * Class Rank: 2 ÷ 4 = 0.5
   * GPA: 4 ÷ 4 = 1.0
   * Essay: 2 ÷ 4 = 0.5
   * Letter of Recommendation: 1 ÷ 1 = 1.0
2. **Aggregate Scores Based on Criterion Setting**

   For each criterion, combine the scores from the two reviewers using the specified aggregation method (average, sum, max, or min).

   * **Class Rank**: Average (0.75 + 0.5) ÷ 2 = 0.625
   * **GPA**: Average (0.75 + 1.0) ÷ 2 = 0.875
   * **Essay**: Average (0.75 + 0.5) ÷ 2 = 0.625
   * **Letter of Recommendation**: Max (1.0, 1.0) = 1.0
3. **Apply Weights**

   You assigned each criterion a different "weight," which shows how important it is in the overall evaluation. Multiply each proportion by its weight to get a weighted score:

   * **Class Rank**: 0.625 × 5 = 3.125
   * **GPA**: 0.875 × 8 = 7.0
   * **Essay**: 0.625 × 4 = 2.5
   * **Letters of Recommendation**: 1.0 × 2 = 2.0
4. **Sum Up Weighted Scores**

   Add all the weighted scores together to get a total scorethat reflects the overall performance of a student across all evaluated criteria.  
   ​

   * **Total Weighted Score**: 3.125 + 7.0 + 2.5 + 2.0 = 14.625
5. **Normalize the Score**

   To ensure the final score fits the scale of 0-10, we normalize it. Divide the total weighted score by the sum of all the weights and then multiply by the maximum score.

   * **Sum of Weights**: 5 + 8 + 4 + 2 = 19
   * **Normalized Score**: 14.625 ÷ 19 × 10 = 7.697

---