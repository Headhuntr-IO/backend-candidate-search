import json
import os
import boto3

table = os.environ['CANDIDATE_SEARCH_TABLE_NAME']
db = boto3.client('dynamodb')


def handle(event, context):
    request_body = __extract_body_as_json(event)

    parameters = request_body['parameters']
    print(table)

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "table": table,
            "parameters": parameters
        })
    }

    return response


def __extract_body_as_json(event):
    if event['body']:
        try:
            return json.loads(event['body'])
        except ValueError:
            return {}
    else:
        return {}
