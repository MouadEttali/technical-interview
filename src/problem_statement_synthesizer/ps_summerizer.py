from PyPDF2 import PdfReader
from docx import Document
from model.models import generate_response

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
    
    # Summarize the problem statement
    summary_prompt = f"Summarize the following problem statement in 2-3 concise sentences: {text}"
    summary = generate_response(prompt=summary_prompt, max_tokens=700)
    
    # Determine ML problem type and target variable
    ml_prompt = f"Analyze the following problem statement to determine the ML problem type (classification, regression, clustering, or other) and the target variable {text}"
    ml_insights = generate_response(prompt=ml_prompt, max_tokens=300)
    
    # Suggest important features
    feature_prompt = f"Identify potentially important features or variables from the problem statement if features are explicitly mentioned: {text}"
    features = generate_response(prompt=feature_prompt, max_tokens=400)
    
    return {
        "summary": summary.strip(),
        "ml_problem_type": ml_insights.strip(),
        "suggested_features": features.strip()
    }

# Main function
def process_problem_statement(file_path):
    text = extract_full_ps_text(file_path)
    return analyze_problem_statement(text)
