import json
import os
import boto3

table = os.environ['CANDIDATE_SEARCH_TABLE_NAME']
db = boto3.client('dynamodb')


def handle(event, context):
    request_body = __extract_body_as_json(event)

    parameters = request_body['parameters']

    db_response = db.put_item(
        TableName=table,
        Item={
            'parameters': {
                'S': json.dumps(parameters)
            },
            'user': {
                'S': 'user123'
            }
        },
        ReturnValues='ALL_OLD'
    )

    response_body = {
        "table": table,
        "parameters": parameters,
        "insertResponse": db_response
    }

    return __assemble_response(200, response_body)


def __extract_body_as_json(event):
    if event['body']:
        try:
            return json.loads(event['body'])
        except ValueError:
            return {}
    else:
        return {}


def __assemble_response(http_code, body):
    return {
        "statusCode": http_code,
        "body": json.dumps(body)
    }
