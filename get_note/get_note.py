import json
import boto3
import os

ddb = boto3.client("dynamodb")
__TableName__ = os.environ["TABLE_NAME"]


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
