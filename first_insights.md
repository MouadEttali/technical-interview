# Machine Learning Problem Report

## Problem Statement Insights
**Summary**:
The problem statement describes a challenge faced by Modjo, a company that gathers and processes audio and video meetings between their sales/customer success teams and their prospects/clients. The goal is to build a model that can predict the type of call (tags such as Cold Call, 1st Call, Demo, etc.) based on various characteristics of the call, such as duration, date, users involved, media type, and other call-related features.

**ML Problem Type**:
The problem is a classification problem, where the target variable is the call "tag" or type. The goal is to predict the appropriate tag for a given call based on the provided features.

**Suggested Features**:
No features suggested

## Dataset Insights
### problem_statement_files/DS-challenge-dataset.csv
**Number of Rows**: 3786
**Number of Columns**: 17

**Data Types**:
- id: int64
- duration: float64
- date: object
- userId: int64
- modifiedById: float64
- phoneProvider: object
- direction: object
- mediaType: object
- dealId: float64
- userTalkRatio: float64
- longestContactMonologue: float64
- patience: float64
- interactionSpeed: float64
- role: object
- teams: object
- contacts: float64
- tag: object

### Missing Data
| Column | Missing Values | Percentage Missing |
| --- | --- | --- |
| id | 0 | 0.0% |
| duration | 0 | 0.0% |
| date | 0 | 0.0% |
| userId | 0 | 0.0% |
| modifiedById | 3006 | 79.40% |
| phoneProvider | 0 | 0.0% |
| direction | 0 | 0.0% |
| mediaType | 0 | 0.0% |
| dealId | 2182 | 57.63% |
| userTalkRatio | 0 | 0.0% |
| longestContactMonologue | 0 | 0.0% |
| patience | 0 | 0.0% |
| interactionSpeed | 0 | 0.0% |
| role | 0 | 0.0% |
| teams | 58 | 1.53% |
| contacts | 1 | 0.03% |
| tag | 0 | 0.0% |

### Summary Statistics (Numerical Columns)
| Column | Min | Max | Mean | Std. Dev. |
| --- | --- | --- | --- | --- |
| id | 1.0 | 5288.0 | 2512.8495 | 1633.8540 |
| duration | 0.0 | 10127.0 | 1539.6029 | 1093.1679 |
| userId | 1.0 | 63.0 | 12.1041 | 9.1407 |
| modifiedById | 1.0 | 67.0 | 13.3718 | 10.3434 |
| dealId | 1.0 | 645.0 | 275.25 | 172.5470 |
| userTalkRatio | 0.0 | 1.3181 | 0.4122 | 0.1983 |
| longestContactMonologue | 0.0 | 3040.52 | 119.3517 | 208.2113 |
| patience | 0.0 | 470.645 | 1.4116 | 11.9073 |
| interactionSpeed | 0.0 | 10.4679 | 2.8421 | 1.6212 |
| contacts | 1.0 | 44.0 | 1.6127 | 1.7333 |

### Duplicate Rows
There are no duplicate rows in the dataset.

### Outliers (Numerical Columns)
| Column | Outliers Detected |
| --- | --- |
| id | 0 |
| duration | 21 |
| userId | 54 |
| modifiedById | 31 |
| dealId | 0 |
| userTalkRatio | 8 |
| longestContactMonologue | 245 |
| patience | 313 |
| interactionSpeed | 81 |
| contacts | 242 |

### Categorical Column Distributions
**date**:
The `date` column has a wide range of unique values, with some dates having more than one occurrence.

**phoneProvider**:
- zoom: 2734
- aircall: 870
- google: 87
- manual: 87
- ringover: 5
- zoom_phone: 1
- microsoft: 1
- salesloft: 1

**direction**:
- outbound: 3545
- inbound: 241

**mediaType**:
- video: 2713
- audio: 1073

**role**:
- admin: 3786

**teams**:
- {Sales}: 3246
- {Account Manager}: 314
- {Account Manager,Product}: 82
- {Product,Account Manager}: 70
- {Tech}: 15
- {Marketing}: 1

**tag**:
- Client Follow Up: 621
- Demo: 611
- 1st Call: 532
- Unscheduled Follow up: 468
- Prospect Follow up: 382
- Cold Call: 371
- Other: 287
- Onboarding Team: 197
- Onboarding Managers: 177
- Set up: 140

## Summary
The dataset contains information about calls made by Modjo's sales and customer success teams. The data includes various call-related features, such as duration, date, users involved, media type, and call tags. The problem is a classification problem, where the goal is to predict the appropriate call tag based on the provided features.

The dataset has a few challenges:
- There are a significant number of missing values in the `modifiedById` and `dealId` columns.
- There are several outliers in the numerical columns, which may need to be addressed during the modeling process.
- The `date` column has a wide range of unique values, which may require some feature engineering to make it more useful for the model.

Overall, the dataset provides a good starting point for the given machine learning problem.