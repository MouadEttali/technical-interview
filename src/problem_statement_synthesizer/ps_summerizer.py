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

def analyze_problem_statement_with_headers(text):
    # Define the combined prompt with headers
    combined_prompt = f"""
    Analyze the following problem statement and do the following tasks:

    1. Summarize the problem statement in 2-3 concise sentences.
    2. Determine the ML problem type (classification, regression, clustering, or other) and the target variable.
    3. Identify any special requests, constraints, or criteria that must be followed to address this problem.

    For each of these 3 tasks, start your response with one of these headers:

    # Problem Statement Summary 
    # ML Problem Type
    # Special Requests

    Problem Statement: {text}
    """
    
    # Generate a single response covering all points
    response = generate_response(prompt=combined_prompt, max_tokens=1000)
    
    # Parse the response based on headers
    summary = ""
    ml_problem_type = ""
    special_requests = ""
    
    # Split the response into sections
    for section in response.split("\n#"):
        if "Problem Statement Summary" in section:
            summary = section.replace("Problem Statement Summary", "").strip()
        elif "ML Problem Type" in section:
            ml_problem_type = section.replace("ML Problem Type", "").strip()
        elif "Special Requests" in section:
            special_requests = section.replace("Special Requests", "").strip()
    
    # Return structured output
    return {
        "summary": summary,
        "ml_problem_type": ml_problem_type,
        "special_requests": special_requests
    }



# Main function
def process_problem_statement(file_path):
    text = extract_full_ps_text(file_path)
    return analyze_problem_statement_with_headers(text)
