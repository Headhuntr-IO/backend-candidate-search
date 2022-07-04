import json
import os


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "app": os.environ['APP_NAME']
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
