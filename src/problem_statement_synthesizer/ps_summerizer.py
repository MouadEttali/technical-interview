import boto3
from PyPDF2 import PdfReader
from docx import Document  # type:ignore

def extract_full_ps_text(file_path):
    if file_path.endswith('.txt') or file_path.endswith('.md'):
        with open(file_path, 'r') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        return " ".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return " ".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format. Use .txt, .pdf, or .docx")

def analyze_problem_statement(text):
    # Initialize AWS Bedrock client
    client = boto3.client('bedrock')
    
    # Summarize the problem statement
    summary_prompt = f"Summarize the following problem statement in 2-3 concise sentences: {text}"
    summary = client.invoke_model(prompt=summary_prompt, modelId='YOUR_BEDROCK_MODEL_ID')['output']
    
    # Determine ML problem type and target variable
    ml_prompt = f"Analyze the following problem statement to determine the ML problem type (classification, regression, clustering, or other) and the target variable {text}"
    ml_insights = client.invoke_model(prompt=ml_prompt, modelId='YOUR_BEDROCK_MODEL_ID')['output']
    
    # Suggest important features
    feature_prompt = f"Identify potentially important features or variables from the problem statement if features are explicitly mentioned: {text}"
    features = client.invoke_model(prompt=feature_prompt, modelId='YOUR_BEDROCK_MODEL_ID')['output']
    
    return {
        "summary": summary.strip(),
        "ml_problem_type": ml_insights.strip(),
        "suggested_features": features.strip()
    }

# Main function
def process_problem_statement(file_path):
    text = extract_full_ps_text(file_path)
    insights = analyze_problem_statement(text)
    return insights
