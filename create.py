import json
import os
import boto3
from datetime import datetime

table = os.environ['CANDIDATE_SEARCH_TABLE_NAME']
db = boto3.client('dynamodb')


def handle(event, context):
    request_body = __extract_body_as_json(event)

    parameters = request_body['parameters']

    user_id = 'user1234'
    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    search_id = f"{user_id}_{current_time}"

    db_response = db.put_item(
        TableName=table,
        Item={
            'id': {
              'S': search_id
            },
            'parameters': {
                'S': json.dumps(parameters)
            },
            'user': {
                'S': user_id
            },
            'date_created': {
                'S': current_time
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
