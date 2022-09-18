import boto3
import json


def lambda_handler(event, context):
    topic_arn = "your topic arn"
    sns = boto3.client('sns', region_name='us-east-1')
    publishobject = {'transactionId': 3, 'amount': 9000.0}
    response = sns.publish(TopicArn=topic_arn, Message=json.dumps(publishobject), Subject='Purchase', MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}})
    return response['ResponseMetadata']['HTTPStatusCode']