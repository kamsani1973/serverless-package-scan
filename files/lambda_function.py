import json
import boto3

print('Loading function')

def lambda_handler(event, context):
    print("Hello Kamsani!")
    return {
        'statusCode': 200,
        'body': 'Hello Kamsani!'
    }
