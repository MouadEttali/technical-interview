import json
import boto3

bedrock_runtime_client = boto3.client(
    'bedrock-runtime',
    region_name="us-east-1"
)
model_id : str ="anthropic.claude-3-haiku-20240307-v1:0"

def construct_payload(prompt:str, max_tokens:int=400):
    return {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        "max_tokens": max_tokens,
        "anthropic_version": "bedrock-2023-05-31"
    }


def generate_response(prompt, max_tokens=300):
    response = bedrock_runtime_client.invoke_model(
    modelId=model_id,
    contentType="application/json",
    body=json.dumps(construct_payload(prompt=prompt, max_tokens=max_tokens))
        )
    
    body_content = response['body'].read()  # Read the content of the StreamingBody
    body_json = json.loads(body_content) 

    return body_json['content'][0]['text']

