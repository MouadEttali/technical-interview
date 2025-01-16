# Machine Learning Problem Report

## Problem Statement Insights

**Summary**: This is a problem statement that requires classification.

**ML Problem Type**: Classification

**Suggested Features**: Age, Income, Education

## Dataset Insights

### dataset.csv

**Number of Rows**: 1000

**Number of Columns**: 10

**Column Names**: Age, Income, Gender, Education, Location

**Data Types**: 
- Age: int64
- Income: float64
- Gender: object
- Education: object
- Location: object

### Missing Data

- **Age**: 50 missing values (5% missing)
- **Income**: 20 missing values (2% missing)

### Summary Statistics (Numerical Columns)

- **Age**: 
  - Min: 18
  - Max: 60
  - Mean: 35
  - Std: 10
- **Income**:
  - Min: 1500
  - Max: 10000
  - Mean: 4500
  - Std: 1500

### Duplicate Rows: 10

### Outliers (Numerical Columns)

- **Age**: 5 outliers detected
- **Income**: 2 outliers detected

### Categorical Column Distributions

- **Gender**: 
  - Male: 500
  - Female: 500
- **Location**:
  - Urban: 600
  - Rural: 400

**Categorical Columns**: Gender, Education, Location

**Numerical Columns**: Age, Income