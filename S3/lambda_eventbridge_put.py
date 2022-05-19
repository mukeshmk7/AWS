import json
import boto3
import datetime
s3 = boto3.client('s3')
event_bus = boto3.client('events')

def lambda_handler(event, context):
    S3_BUCKET = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    data = s3.get_object(Bucket=S3_BUCKET, Key=key)
    contents = data['Body'].read()
    response = event_bus.put_events(
        Entries=[
            {
            'Time': datetime.datetime.now(),
            'Source': 'Lambda Publish',
            'Resources': [
             ],
            'DetailType': 'From S3_BUCKET',
            'Detail': json.dumps(json.loads(contents.decode('utf-8'))),
            'EventBusName': 'eventbusname',
            'TraceHeader': f'filename-{key}'
             },
                ]
             )
    return response
