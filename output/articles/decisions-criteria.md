---
title: Decisions: Criteria
url: https://help.element451.com/en/articles/9210619-decisions-criteria
collection: Decisions
---

Discover how to customize your review metrics in Decisions, enhancing the precision of applicant assessments with criteria settings.

# Overview

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1336474930/adc3a49e12f9e3c553fedb5078b1/Important.png?expires=1784430000&signature=2e63d938483ddb211d5d6b291fac9b087d979841c3af36f660cfba5c9f94545f&req=dSMkEM15mYhcWfMW3Hu4gWTfRNRktLSyHo7ovEiL4cuPkh9s88I2ciESqAnI%0Ayg%3D%3D%0A) When you change the settings or conditions for a criterion, those updates only affect new decisions submitted after the change. Any existing decisions keep the original criteria that were in place when the application was submitted.

Student data is also only checked once, at the time of submission. If the data doesn’t meet the conditions then, the criterion won’t appear later—even if the student’s information changes and would meet the conditions afterward.

The **Criteria** feature within the **Decisions Module** allows you to build and customize evaluation metrics for applicants, such as class rank, GPA, essays, and more. With configurable options for each criterion, including conditional logic, this functionality is especially valuable for programs with limited access or seating, where accurate student ranking is essential. Each criterion you configure appears during the application review process, displaying only for relevant applicants, enabling reviewers to input their scores directly into the decision interface for a streamlined evaluation experience.

## Accessing Criteria

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Criteria** tab.

[![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256800898/484d336065ee696463d73c8903ee/Conditional+Decision+Criteria.png?expires=1784333700&signature=ce6a632a2e7fbd664fe95b63eaa5c43b7a5cf1891c89daa95b31633548d130c5&req=dSIiEMF%2BnYlWUfMW1HO4zTofOWA8nMBgLLwB9Ah6uNaMgo7AO%2FuF9H04YTZG%0ADVIf58Y7zuoZYSCq9ok%3D%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256800898/484d336065ee696463d73c8903ee/Conditional+Decision+Criteria.png?expires=1784333700&signature=ce6a632a2e7fbd664fe95b63eaa5c43b7a5cf1891c89daa95b31633548d130c5&req=dSIiEMF%2BnYlWUfMW1HO4zTofOWA8nMBgLLwB9Ah6uNaMgo7AO%2FuF9H04YTZG%0ADVIf58Y7zuoZYSCq9ok%3D%0A)

---

# Criteria Configurations

## Types

* **Global**: Applies one score per application, regardless of the number of reviewers.
* **Per** **Reviewer**: Enables multiple scores per application, useful when different individuals evaluate the same application.

## Weight

* Sets the relative importance of each criterion on a scale from 1 to 10, with 1 being least important and 10 being most important. The default setting is 5.

## Aggregate Score Type

* Choose how to aggregate scores from each criteria item (**only applies to Per Reviewer criteria type**):

  + **Average**: Calculates the mean score.
  + **Sum**: Adds up all the scores.
  + **Max**: Uses the highest score given.
  + **Min**: Uses the lowest score given.

## Score Types

* **Categorical**: Establishes a ranking system with a defined number of levels from low to high. For example, categories might be labeled Very Low, Low, Average, and High.
* **Numerical**: This option assigns scores as simple numerical values. You can set a maximum score, such as 10, and reviewers can select any number from 1 to 10.
* **Boolean**: Offers a binary scoring option, typically labeled Yes or No. Labels are customizable, provided one equates to true and the other to false.

## Understanding Weighted Scoring in Applicant Evaluation

To provide a clear understanding of how weighted scoring impacts applicant evaluations, let’s explore an example scenario with four criteria: Class Rank, GPA, Essay, and Letters of Recommendation.

## **Scenario:**

An applicant has the following scores for each criterion:

* **Class Rank**: 2 out of a maximum of 4
* **GPA**: 1 out of a maximum of 4
* **Essay**: 3 out of a maximum of 4
* **Letters of Recommendation**: 1 out of a maximum of 1

## **Criteria Weights:**

The importance of each criterion in the overall evaluation process is defined by its weight:

* **Class Rank**: Weight = 5
* **GPA**: Weight = 8
* **Essay**: Weight = 4
* **Letters of Recommendation**: Weight = 2

Weights indicate the relative importance of each criterion in the final score, allowing evaluators to prioritize certain aspects of an applicant's application.

## **Calculation Method:**

1. **Proportionate Score Calculation**: Each score is first converted into a proportion of the maximum possible score for that criterion:

   * **Class Rank**: 2/4 = 0.5
   * **GPA**: 1/4 ​= 0.25
   * **Essay**: 3/4 = 0.75
   * **Letters of Recommendation**: 1/1 = 1.0

   These proportions are then **multiplied** **by their respective weights** to reflect their importance:

   * **Class Rank**: 0.5 × 5 = 2.5
   * **GPA**: 0.25 × 8 = 2.0
   * **Essay**: 0.75 × 4 = 3.0
   * **Letters of Recommendation**: 1.0 × 2 = 2.0
2. **Weighted Sum and Normalization**: The weighted scores are summed:

   * **Total Weighted Score**: 2.5 + 2.0 + 3.0 + 2.0 = 9.5

   To ensure the final score fits within the standardized maximum of 10, we normalize this sum based on the total of the weights:

   * **Sum of Weights**: 5 + 8 + 4 +2 = 19
   * **Normalized Score**: 9.5 ÷ 19 × 10 = 5.0

## **Conclusion:**

![](https://downloads.intercomcdn.com/i/o/1036466017/49c3a7788736e092eb17eae7/Decisions+-+Score+of+5.png?expires=1784430000&signature=c93922cb4624d20f3fee69f9b7d9483a5b95cbee5dbe558cb779abc67a3cbbcd&req=dSAkEM14m4FeXvMW3Hu4gR9EHkZx96Le7x0q0XvhEoaEw0pp2zZEQFBmCkqh%0AJA%3D%3D%0A)The final score is 5 out of 10.

This score indicates how well the applicant performed across all weighted criteria, scaled to a maximum score of 10. This method ensures that each criterion's influence on the overall score is proportional to its assigned weight, providing a fair and balanced assessment of the applicant’s qualifications.

---

# Adding Criteria

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on the **Criteria** tab.
3. Click the **blue plus sign** ![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256801962/ff087c56e6d43ca56311a7eac981/%2B+Plus+Button+Transparent.png?expires=1784430000&signature=05d6f39c3e971756b6cadf302c82fc4a2f91defe7c740b15de21291976a2b263&req=dSIiEMF%2BnIhZW%2FMW3Hu4gTKQdYrQup4sqTxFimgjmEmnIH%2FJ4z7nK06MAeZr%0ATQ%3D%3D%0A) in the bottom right corner of the page.
4. Configure the three tabs of the new criteria:

   * **General**

     + Provide a name, a short name (this will be visible if the full name is too long to display), and a brief description.
   * **Works For**

     + Select the application(s) you wish this criterion to work with.
   * **Conditions**

     + Add **conditional logic** to control when this criterion will be displayed. By setting conditions, you can ensure that this criterion only appears for applicants who meet specific requirements, helping reviewers focus on relevant evaluation items.

       - Click **Add Condition** to begin setting up criteria visibility rules.
       - Select from two condition types:

         * **Segment Reference:** Create a custom segment of Contacts based on specific properties, such as **demographics** or **interaction history** from their Contact record. This option is ideal if you want to tailor criteria for certain applicant groups based on customized characteristics.
         * **User Segment:** Use a **pre-existing segment** that you’ve already created. This option provides a faster setup if the relevant segment has been previously defined.
       - Once conditions are set, this criterion will only be visible for applicants who match the defined segment criteria.
5. Click **Create**. Your criteria item will be added to the criteria list and open for you to configure.
6. Configure the settings of the criteria item. Refer to the [Criteria Configuration](#h_86017b711f) section above for a comprehensive explanation of each setting.

---

# Editing, Reordering, + Deleting Criteria

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1336474930/adc3a49e12f9e3c553fedb5078b1/Important.png?expires=1784430000&signature=2e63d938483ddb211d5d6b291fac9b087d979841c3af36f660cfba5c9f94545f&req=dSMkEM15mYhcWfMW3Hu4gWTfRNRktLSyHo7ovEiL4cuPkh9s88I2ciESqAnI%0Ayg%3D%3D%0A) When criteria are updated or conditions are changed, **the updates only apply to new decisions** **submitted** **after the update has taken effect**. Previous decisions will retain the criteria list that was present at the time of application submission.

1. Navigate to **Applications** > **Decisions** > **Decision** **Settings.**
2. Click on either the **Criteria** tab.
3. In the lefthand menu, locate the criteria item you wish to edit, reorder, or delete.
4. Click on the criteria item name.
5. Follow the instructions below:

## Editing

* **Criteria Settings (Type, Weight, etc.)**

  1. Click on the **cog/gear** icon next to the criteria item.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256816373/898a42f4db8cd0602aeef97af914/Conditional+Decision+Criteria.png?expires=1784333700&signature=0fb8b7c186451a3860cce2c9051c0e03a83e3f6a80f7bafa97a9cba7fddf8005&req=dSIiEMF%2Fm4JYWvMW1HO4zcqLjsK1ctawQhGrlLnYjP4wstzUyJl3zKSAxMDN%0AO0em%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256816373/898a42f4db8cd0602aeef97af914/Conditional+Decision+Criteria.png?expires=1784333700&signature=0fb8b7c186451a3860cce2c9051c0e03a83e3f6a80f7bafa97a9cba7fddf8005&req=dSIiEMF%2Fm4JYWvMW1HO4zcqLjsK1ctawQhGrlLnYjP4wstzUyJl3zKSAxMDN%0AO0em%0A)
  2. Make your changes.
  3. Click **Save** when you have finished.
* **Name, Short Name, Description, or Conditions**

  1. Click on the **pencil** **icon** next to the criteria item.

     [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256816718/53925bea82b995d436fd76460223/Conditional+Decision+Criteria.png?expires=1784333700&signature=4b41bf522cd25a1e83483fb562a31796cc560319c07825e0c85f079c2da412af&req=dSIiEMF%2Fm4ZeUfMW1HO4zeb0DIMEA0FlYvXG%2FhlHxMS1GJGT9a0Rz2UvIsoc%0Ad8ls%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256816718/53925bea82b995d436fd76460223/Conditional+Decision+Criteria.png?expires=1784333700&signature=4b41bf522cd25a1e83483fb562a31796cc560319c07825e0c85f079c2da412af&req=dSIiEMF%2Fm4ZeUfMW1HO4zeb0DIMEA0FlYvXG%2FhlHxMS1GJGT9a0Rz2UvIsoc%0Ad8ls%0A)
  2. Navigate through the three tabs: general, works for, and conditions to make your changes.
  3. Click **Update** when you have finished.

## Reordering

* To reorder criteria items, use the double-sided arrow to the left of the criteria name and drag and drop the item to the desired location.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256817393/6995ce63894bb9831fc939b5143e/Cond+criteria.png?expires=1784333700&signature=be0542b486886931ee91dec0315cfded080ffdc3b6a8993ff9db91953c169dbd&req=dSIiEMF%2FmoJWWvMW1HO4zZK9LCBsoTgbnvTu3KTAdWWlk4EzJ3M95CrABmjS%0ARwAC%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256817393/6995ce63894bb9831fc939b5143e/Cond+criteria.png?expires=1784333700&signature=be0542b486886931ee91dec0315cfded080ffdc3b6a8993ff9db91953c169dbd&req=dSIiEMF%2FmoJWWvMW1HO4zZK9LCBsoTgbnvTu3KTAdWWlk4EzJ3M95CrABmjS%0ARwAC%0A)

## Deleting

* Click on the **trash can** icon next to the criteria item. You will be prompted to confirm your action.

  [![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256818005/e30f015f5fca243459d7d20ded28/Conditional+Decision+Criteria.png?expires=1784333700&signature=5781648d47d25699eb6b8af49313ab7719b95f39cc45396da47e5460a00899ec&req=dSIiEMF%2FlYFfXPMW1HO4zdNa8xd%2FwLpdytHqjtgAlB6BL%2B1aUt%2FXte9e5XQ%2F%0ALNwS%0A)](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1256818005/e30f015f5fca243459d7d20ded28/Conditional+Decision+Criteria.png?expires=1784333700&signature=5781648d47d25699eb6b8af49313ab7719b95f39cc45396da47e5460a00899ec&req=dSIiEMF%2FlYFfXPMW1HO4zdNa8xd%2FwLpdytHqjtgAlB6BL%2B1aUt%2FXte9e5XQ%2F%0ALNwS%0A)

  ​

---

# Utilizing Criteria for Application Reviews

The criteria you set up in Decision Settings are visible in each application decision, allowing you to score each item and include relevant notes. For further details, check out our article on [Reviewing and Processing Application Decisions](https://help.element451.com/en/articles/9241630-reviewing-processing-application-decisions).

![](https://downloads.intercomcdn.com/i/o/h9r2yo9x/1265484218/12bfd07767d47590c3850608fb8c/Note.png?expires=1784430000&signature=41bd5460adb7c8704bf081990830cfa914aa8eb8aac4a4bc501464a35278caac&req=dSIhE812mYNeUfMW3Hu4gY%2FwPNnUI0iA2Iuk6sQjysg2spkeLIGwxg1JdDTI%0AbA%3D%3D%0A) **Criteria Behavior:** When you change the settings or conditions for a criterion, those updates only affect new decisions submitted after the change has taken effect. Any existing decisions keep the original criteria that were in place when the application was submitted.

Student data is also only checked once, at the time of submission. If the data doesn’t meet the conditions then, the criterion won’t appear later—even if the student’s information changes and would meet the conditions afterward.

---