import boto3

def generate_markdown_report(ps_insights, dataset_insights, model_id="YOUR_BEDROCK_MODEL_ID"):
    # Initialize AWS Bedrock client
    client = boto3.client('bedrock')

    # Markdown Header
    report = "# Machine Learning Problem Report\n\n"

    # Add problem statement insights to the report
    report += "## Problem Statement Insights\n"
    report += f"**Summary**: {ps_insights.get('summary', 'No summary provided')}\n"
    report += f"**ML Problem Type**: {ps_insights.get('ml_problem_type', 'Not detected')}\n"
    report += f"**Suggested Features**: {ps_insights.get('suggested_features', 'No features suggested')}\n\n"

    # Add dataset insights to the report
    report += "## Dataset Insights\n"
    for file_path, insights in dataset_insights.items():
        report += f"### {file_path}\n"
        # Dataset dimensions and columns
        report += f"**Number of Rows**: {insights.get('rows', 'Unknown')}\n"
        report += f"**Number of Columns**: {insights.get('columns', 'Unknown')}\n"
        report += f"**Column Names**: {', '.join(insights.get('column_names', []))}\n"
        report += f"**Data Types**: {', '.join([f'{col}: {dtype}' for col, dtype in insights.get('data_types', {}).items()])}\n\n"

        # Missing data
        missing_data = insights.get('missing_data', {})
        report += "### Missing Data\n"
        for col, count in missing_data.get('missing_count', {}).items():
            report += f"- **{col}**: {count} missing values ({missing_data['missing_percentage'].get(col, '0')}% missing)\n"
        
        # Summary statistics
        report += "### Summary Statistics (Numerical Columns)\n"
        summary_stats = insights.get('summary_statistics', {})
        for col, stats in summary_stats.items():
            if isinstance(stats, dict):  # Only for numerical columns
                report += f"- **{col}**: Min: {stats.get('min')}, Max: {stats.get('max')}, Mean: {stats.get('mean')}, Std: {stats.get('std')}\n"
        
        # Duplicate Rows
        report += f"### Duplicate Rows: {insights.get('duplicate_rows', 'Unknown')}\n"

        # Outliers
        outliers = insights.get('outliers', {})
        report += "### Outliers (Numerical Columns)\n"
        for col, outlier_count in outliers.items():
            report += f"- **{col}**: {outlier_count} outliers detected\n"
        
        # Categorical Column Distributions
        categorical_distributions = insights.get('categorical_distributions', {})
        if categorical_distributions:
            report += "### Categorical Column Distributions\n"
            for col, distribution in categorical_distributions.items():
                report += f"- **{col}**: {', '.join([f'{k}: {v}' for k, v in distribution.items()])}\n"
        
        # Categorical and Numerical Columns
        report += f"**Categorical Columns**: {', '.join(insights.get('categorical_columns', []))}\n"
        report += f"**Numerical Columns**: {', '.join(insights.get('numerical_columns', []))}\n\n"

    # Optionally use Bedrock to enhance the markdown report by summarizing or adding suggestions
    bedrock_prompt = f"Enhance the following report for clarity and detail:\n\n{report}"
    response = client.invoke_model(prompt=bedrock_prompt, modelId=model_id)
    enhanced_report = response['output']
    with open("first_insights.md", "r") as f:
        f.write(enhanced_report)
    print("enhanced report created successfully")

# Example usage:
ps_insights = {
    "summary": "This is a problem statement that requires classification.",
    "ml_problem_type": "Classification",
    "suggested_features": "Age, Income, Education"
}

dataset_insights = {
    "dataset.csv": {
        "rows": 1000,
        "columns": 10,
        "column_names": ["Age", "Income", "Gender", "Education", "Location"],
        "data_types": {"Age": "int64", "Income": "float64", "Gender": "object", "Education": "object", "Location": "object"},
        "missing_data": {
            "missing_count": {"Age": 50, "Income": 20},
            "missing_percentage": {"Age": 5, "Income": 2}
        },
        "summary_statistics": {"Age": {"min": 18, "max": 60, "mean": 35, "std": 10}, "Income": {"min": 1500, "max": 10000, "mean": 4500, "std": 1500}},
        "duplicate_rows": 10,
        "outliers": {"Age": 5, "Income": 2},
        "categorical_distributions": {"Gender": {"Male": 500, "Female": 500}, "Location": {"Urban": 600, "Rural": 400}},
        "categorical_columns": ["Gender", "Education", "Location"],
        "numerical_columns": ["Age", "Income"]
    }
}

markdown_report = generate_markdown_report(ps_insights, dataset_insights)
print(markdown_report)
