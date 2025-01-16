import os
from PyPDF2 import PdfReader
from docx import Document

from model.models import generate_response # type:ignore

def extract_preview(file_path, num_lines=5):
    """
    Extract a preview of the file content (first `num_lines` lines) or metadata.

    Args:
        file_path (str): Path to the file.
        num_lines (int): Number of lines to extract as a preview.

    Returns:
        str: Preview text extracted from the file.
    """
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.txt':
        with open(file_path, 'r') as f:
            return "\n".join([next(f, '').strip() for _ in range(num_lines)])
    elif ext == '.pdf':
        reader = PdfReader(file_path)
        preview = []
        for page in reader.pages[:1]:  # Limit to the first page
            preview += page.extract_text().splitlines()[:num_lines]
        return "\n".join(preview)
    elif ext == '.docx':
        doc = Document(file_path)
        preview = [para.text for para in doc.paragraphs[:num_lines]]
        return "\n".join(preview)
    elif ext in ['.csv', '.json', "parquet"]:
        return f"This file is a structured dataset with the extension {ext}."
    else:
        return f"Unsupported file format: {ext}"

def classify_files_bedrock_fast(folder_path="problem_statement_files", num_lines=5):
    """
    Classify files using AWS Bedrock with limited content preview.

    Args:
        folder_path (str): Path to the folder containing files.
        client: AWS Bedrock boto3 client.
        model_id (str): ID of the Bedrock LLM to use.
        num_lines (int): Number of lines to extract for preview.

    Returns:
        dict: Dictionary with file names as keys and classifications as values.
    """
    file_classification = {}
    
    # Iterate through files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue  # Skip directories
        
        # Extract a limited preview from the file
        preview = extract_preview(file_path, num_lines=num_lines)
        
        # Prompt for classification
        prompt = (
            f"The file is named: {file_name}\n\n"
            f"Here is a preview of the content:\n{preview}\n\n"
            f"Based on this information, classify this file into one of the following categories:\n"
            f"- problem_statement: Describes the business problem or ML task.\n"
            f"- dataset: Contains structured or tabular data for ML training.\n"
            f"- other: Any other type of file.\n\n"
            f"Only provide the category and nothing else!"
        )
        
        # Call Bedrock
        result = generate_response(prompt=prompt, max_tokens=200)
        
        print(result)
        # Parse response and add to classification
        file_classification[file_path] = result.strip()
    
    return file_classification


