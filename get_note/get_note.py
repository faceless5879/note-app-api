import json
import boto3
import os

ddb = boto3.client("dynamodb")
__TableName__ = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    try:
        allRecord = ddb.scan(
            TableName=__TableName__,
            AttributesToGet=["NoteContent", "UUID"],
        )
    except:
        print("Cannot connect to DB")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(allRecord["Items"]),
    }
