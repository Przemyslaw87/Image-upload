import boto3
import pytest
from decouple import config
from django.test import override_settings


@pytest.fixture
def delete_image_from_minio():
    yield
    # Create an S3 client
    s3 = boto3.client(
        "s3",
        aws_access_key_id=config("MINIO_ACCESS_KEY"),
        aws_secret_access_key=config("MINIO_SECRET_KEY"),
        endpoint_url="http://minio:9000",
    )
    # Get a list of all objects in the bucket
    objects = s3.list_objects(Bucket="my-local-bucket")
    # Iterate through the list and delete each object
    for obj in objects['Contents']:
        s3.delete_object(Bucket="my-local-bucket", Key=obj['Key'])

@pytest.fixture
def minio_settings():
    with override_settings(
        DEFAULT_FILE_STORAGE="storages.backends.s3boto3.S3Boto3Storage",
        AWS_STORAGE_BUCKET_NAME="my-local-bucket",
        AWS_S3_ENDPOINT_URL="http://minio:9000",
        AWS_ACCESS_KEY_ID=config("MINIO_ACCESS_KEY"),
        AWS_SECRET_ACCESS_KEY=config("MINIO_SECRET_KEY"),
        MINIO_STORAGE_USE_HTTPS=False,
    ):
        yield


