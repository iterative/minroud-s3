from base64 import b64decode
from boto3 import client
from hashlib import sha256
from os import environ


BUCKET = environ["BUCKET"]
REGION = environ["REGION"]


def handler(event, context):
    body = b64decode(event["body"]) if event["isBase64Encoded"] else event["body"]
    mime = event["headers"].get("content-type", "application/octet-stream")
    seed = event["headers"].get("content-seed", event["body"])
    name = sha256(seed.encode()).hexdigest()

    client("s3").put_object(
        ACL="public-read", Body=body, Bucket=BUCKET, ContentType=mime, Key=name
    )

    return {
        "statusCode": 200,
        "body": f"https://{BUCKET}.s3.{REGION}.amazonaws.com/{name}",
    }
