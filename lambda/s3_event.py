import json
import boto3
import pandas as pd

def lambda_handler(event, context):
    # TODO implement
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    s3_object_response = get_object(bucket_name, key)
    if s3_object_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        result = s3_object_response['Body'].read().decode('utf-8')
        json_content = json.loads(result)
        result_df = pd.read_json(json_content)
    return result_df
    
def get_object(bucket, key):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket, Key=key)
    return response