import boto3
import base64
from botocore.exceptions import ClientError
import json
import yaml

yml_configs = {}
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)
    

def get_secrets():
    secret_name = yml_configs['secrets']['secret_name']
    region_name = yml_configs['secrets']['region_name']

    print("in get secrets")
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    print("after session call in secrets")

    try:
        print("before try in secrets")
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        print("in secrets")
        print(get_secret_value_response)
    except ClientError as e:
        print("in error in secrets")
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    print("returning in secrets")
    return json.loads(get_secret_value_response['SecretString'])
