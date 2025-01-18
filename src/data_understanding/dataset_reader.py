import pandas as pd


def read_dataset(file_path):
    # Check the file extension and read the corresponding dataset format
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.parquet'):
        return pd.read_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path.split('.')[-1]}")

def first_data_insights(file_path):
    df = read_dataset(file_path)
    
    # 1. Dataset Dimensions & Columns
    dataset_info = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "data_types": df.dtypes.to_dict()
    }

    # 2. Missing Data
    missing_data = df.isnull().sum()
    missing_percentage = (missing_data / df.shape[0]) * 100
    dataset_info["missing_data"] = {
        "missing_count": missing_data.to_dict(),
        "missing_percentage": missing_percentage.to_dict()
    }

    # 3. Summary Statistics (numerical columns)
    summary_stats = df.describe().to_dict()
    dataset_info["summary_statistics"] = summary_stats

    # 4. Duplicate Rows
    dataset_info["duplicate_rows"] = df.duplicated().sum()

    # 5. Outliers (for numeric columns)
    outliers = {}
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        # Calculate outliers using IQR
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers[col] = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]

    dataset_info["outliers"] = outliers

    # 6. Check Categorical Column Distributions (if any)
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns
    categorical_distributions = {col: df[col].value_counts().to_dict() for col in categorical_columns}
    dataset_info["categorical_distributions"] = categorical_distributions

    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()  # Includes int and float columns
    dataset_info["categorical_columns"] = categorical_columns
    dataset_info["numerical_columns"] = numerical_columns

    return dataset_info
