import boto3
import json

session = boto3.Session(profile_name='udacity')

# Try us-east-1 (Virginia) - commonly has Bedrock
bedrock = session.client('bedrock-runtime', region_name='us-east-1')

prompt = "Human: Write a short story about a robot learning to paint.\n\nAssistant:"

body = json.dumps({
    "prompt": prompt,
    "max_tokens_to_sample": 500,
    "temperature": 0.7,
    "top_p": 1,
    "stop_sequences": ["\n\nHuman:"]
})

response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0",
    body=body
)

response_body = json.loads(response['body'].read())
print(response_body['completion'])