import json
import boto3
import os

ddb = boto3.client("dynamodb")
__TableName__ = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    print(ddb)
    print(__TableName__)
    try:
        res = ddb.get_item(
            TableName=__TableName__,
            Key={"Email": {"S": "Note"}, "Name": {"S": "User"}},
            AttributesToGet=[
                "NoteContent",
            ],
        )
        print(res)
    except:
        print("Cannot get item")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world"}),
    }
