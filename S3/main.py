import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
import requests

bucket_name = 'myfiles07'

def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
# upload_file("./data.json", bucket_name, "data.json")

def delete_non_empty_bucket(bucket):
    s3_client = s3 = boto3.resource('s3') 
    bucketClient = s3_client.Bucket(bucket)
    bucketClient.objects.all().delete()
    bucketClient.meta.client.delete_bucket(Bucket=bucket)
#delete_non_empty_bucket(bucket_name)

def delete_object(bucket,object_name):
    s3_client = boto3.client('s3')
    response = s3_client.delete_object(Bucket=bucket,Key=object_name)
    print(response)
delete_object(bucket_name, "data.json")

import json
import boto3


s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    target_bucket = 'myfiles08'
    copy_source = {'Bucket': source_bucket, 'Key': object_key}
    print ("Source bucket : ", source_bucket)
    print ("Target bucket : ", target_bucket)
    try:
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=object_key)
        s3.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
        return {
        'statusCode': 200,
        'body': json.dumps('File has been Successfully Copied')
        }
    except Exception as err:
        print ("Error -"+str(err))
        return err