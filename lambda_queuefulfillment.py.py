import boto3
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    sqs = boto3.client('sqs')

    logger.info('@@@@@##',event)
    # TODO implement
    sqsurl = "https://sqs.us-east-1.amazonaws.com/571815438302/fufillmentqueue"
    print(event)
    
    try:
        sqs_return = sqs.send_message(QueueUrl=sqsurl, MessageBody=json.dumps(event))
    except:
        return {
            'statusCode': 501,
            'body': 'error'
        }
    
    a = {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Booking Done"
                }
            }
        }
    return a
    
