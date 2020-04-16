import os
import boto3
import random
from dotenv import load_dotenv

"""
loads environment variables of .env
"""
load_dotenv()

"""
Storage configurations
"""
bucket_name = os.getenv('bucket_name')
s3 = boto3.client('s3')
path_name = 'images'


def get_contents():
    """
    :return: List with contents of bucket
    """
    return s3.list_objects(Bucket=bucket_name, Prefix=path_name)['Contents']


def get_random_image():
    """
    :return: Random image of storage
    """
    contents = get_contents()
    random_content = random.choice(contents)['Key']
    type_images = ['jpg', 'png', 'jpeg']

    if random_content.split('.')[-1] not in type_images:
        get_random_image()

    return random_content


def open_image():
    """
    :return: File Object
    """
    return open(get_random_image(), 'rb')
