import boto3

# Create a session with the udacity profile
session = boto3.Session(profile_name='udacity')

# Create a bedrock client from that session
bedrock = session.client('bedrock')

# Now call the method on the bedrock client
response = bedrock.list_foundation_models()

for model in response['modelSummaries']:
    print(f"Model ID: {model['modelId']}")
    print(f"Model Name: {model['modelName']}")
    print(f"Provider: {model['providerName']}")
    print("---")