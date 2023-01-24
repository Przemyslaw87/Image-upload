import os

import pytest
from decouple import config
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import Images


class SettingsTest(TestCase):
    def test_setting_aws_key(self):
        assert hasattr(settings, "AWS_ACCESS_KEY_ID")
        assert settings.AWS_ACCESS_KEY_ID == config("AWS_ACCESS_KEY_ID")

    def test_setting_aws_access_key(self):
        assert hasattr(settings, "AWS_SECRET_ACCESS_KEY")
        assert settings.AWS_SECRET_ACCESS_KEY == config("AWS_SECRET_ACCESS_KEY")

    def test_setting_aws_bucket(self):
        assert hasattr(settings, "AWS_STORAGE_BUCKET_NAME")
        assert settings.AWS_STORAGE_BUCKET_NAME == config("AWS_STORAGE_BUCKET_NAME")

    def test_setting_default_storage(self):
        assert hasattr(settings, "DEFAULT_FILE_STORAGE")
        assert (
            settings.DEFAULT_FILE_STORAGE == "storages.backends.s3boto3.S3Boto3Storage"
        )


class ImagesModelsTests(TestCase):

    @pytest.mark.usefixtures("minio_settings", "delete_image_from_minio")
    def test_create_image_success(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_directory, "foto.jpg")
        with open(image_path, "rb") as f:
            image_file = SimpleUploadedFile(f.name, f.read())
            image_instance = Images.objects.create(
                title="Title", width=300, height=200, image_url=image_file
            )
            image_instance.save()
        assert Images.objects.count() == 1

    @pytest.mark.usefixtures("minio_settings","delete_image_from_minio")
    def test_create_image_success_ok_fields(self):
        """
            Test that creating an image with valid fields and saving it to minio
            results in a successful creation and the image's fields match the expected values.
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_directory, "foto.jpg")
        with open(image_path, "rb") as f:
            image_file = SimpleUploadedFile(f.name, f.read())
            image_instance = Images.objects.create(
                title="Title", width=300, height=200, image_url=image_file
            )
            image_instance.save_and_upload()
        assert image_instance.height == 200
        assert image_instance.width == 200
        assert image_instance.original_name_file == "foto.jpg"
        assert image_instance.title == "Title"
