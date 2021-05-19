from django.conf import settings
from storages.backends.s3boto3 import S3BBoto3Storage


class StaticStorage(S3BBoto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BBoto3Storage):
    location = settings.MEDIAFILES_LOCATION
