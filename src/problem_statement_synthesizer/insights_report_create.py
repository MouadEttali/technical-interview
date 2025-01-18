
from model.models import generate_response

def generate_markdown_report(ps_insights, dataset_insights):

    # Markdown Header
    report = "# Machine Learning Problem Report\n\n"

    # Add problem statement insights to the report
    report += "## Problem Statement Insights\n"
    report += f"**Summary**: \n{ps_insights.get('summary', 'No summary provided')}\n"
    report += f"**ML Problem Type**: \n {ps_insights.get('ml_problem_type', 'Not detected')}\n"
    report += f"**Suggested Features**: \n {ps_insights.get('suggested_features', 'No features suggested')}\n\n"

    # Add dataset insights to the report
    report += "## Dataset Insights\n"
    for file_path, insights in dataset_insights.items():
        report += f"### {file_path}\n"
        # Dataset dimensions and columns
        report += f"**Number of Rows**: {insights.get('rows', 'Unknown')}\n"
        report += f"**Number of Columns**: {insights.get('columns', 'Unknown')}\n"
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
    report_prompt = f"Enhance the following report for clarity and detail :\n\n{report}  End of Report\
        # Requirements for enhancements :\n * make sure there aren't many information stacked in one line so use breaklines for new information \
        * if a certain information can be written in tabular format do it \
        * Do not repeate the same information"
    response = generate_response(prompt=report_prompt, max_tokens=3000)

    with open("first_insights.md", "w") as f:
        f.write(response)
    print("enhanced report created successfully")
