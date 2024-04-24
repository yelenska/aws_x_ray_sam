import json

from aws_lambda_powertools import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
import requests

MODULES = ["requests"]
tracer = Tracer(patch_modules=MODULES)


@tracer.capture_method
def update_event(event: dict) -> dict:
    event['updated'] = True
    return event


@tracer.capture_method
def get_ip() -> str:
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext):
    tracer.put_metadata(key='request_id', value=context.aws_request_id)
    tracer.put_annotation(key='lambda_ip', value=get_ip())

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'hello world',
            'event': update_event(event),
        }),
    }
