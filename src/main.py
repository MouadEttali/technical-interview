
from data_understanding.dataset_reader import first_data_insights
from problem_statement_synthesizer.files_metadata_retriever import classify_files_bedrock_fast
import boto3

from problem_statement_synthesizer.insights_report_create import generate_markdown_report
from problem_statement_synthesizer.ps_summerizer import process_problem_statement


PS_FOLDER = "problem_statement_files"
client = boto3.client('bedrock-runtime')

model_id = "amazon.titan-text-v1"
filepath_and_classification = classify_files_bedrock_fast(
                                                  folder_path=PS_FOLDER, 
                                                  client=client, 
                                                  model_id=model_id)

dataset_insights = {}

for file_path, classification in filepath_and_classification.items():
     match classification:
        case "problem_statement":
            ps_insights = process_problem_statement(file_path=file_path)
        case "dataset":
            dataset_insights[file_path] = first_data_insights(file_path=file_path)
        case "other":
            print(f"Other document {file_path}")
        case _:
            print(f"Weird document {file_path}")

generate_markdown_report(ps_insights, dataset_insights, model_id=model_id)
