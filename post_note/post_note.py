import json
import uuid
import boto3
import os

ddb = boto3.client("dynamodb")
__TableName__ = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    # if not event["body"]["content"]:
    #     return {
    #         "statusCode": 400,
    #         "body": json.dumps({"Message": "Invalid request"}),
    #     }
    reqBody = json.loads(event["body"])
    noteId = str(uuid.uuid4())
    noteContent = reqBody["content"]
    item = {
        "UUID": {"S": noteId},
        "UserName": {"S": "User"},
        "NoteContent": {"S": noteContent},
    }
    try:
        ddb.put_item(TableName=__TableName__, Item=item)
    except:
        print("Cannot connect DB")
    return {
        "statusCode": 200,
        "body": json.dumps({"Id": noteId}),
    }
