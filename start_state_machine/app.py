import json
import os
import sys
import jsonschema
from jsonschema import validate

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e


    # Assume an event payload of two numbers
    e = json.loads(json.dumps(event))
    environment = e['environment']
    number_of_hellos = e['number_of_hellos']
    times = number_of_hellos

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "starting state machine, times " + str(times),
            "environment": environment,
            "number_of_hellos": number_of_hellos
            # "location": ip.text.replace("\n", "")
        }),
    }


