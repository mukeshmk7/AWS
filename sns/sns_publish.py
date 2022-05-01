import boto3
import env
import json

def main():
    topic_arn = env.topic_arn
    sns = boto3.client('sns', aws_access_key_id=env.access_key, aws_secret_access_key=env.secret_key, region_name='us-east-1')
    publishobject = {'transactionId': 1, 'amount': 500.0}
    response = sns.publish(TopicArn=topic_arn, Message=json.dumps(publishobject), Subject='Purchase', MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}})
    print(response)

main()


# lambda function to display message invoked in sns

import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
    return message

