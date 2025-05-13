import uuid

from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

# from django.contrib import admin
from django.conf import settings
from utils.storage import minio_client

# Register your models here.


class EventAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False, label="Upload Image")

    class Meta:
        fields = "__all__"

    def save(self, commit=True):
        instance = super().save(commit=False)

        image = self.files.get("image_file")
        if image and isinstance(image, InMemoryUploadedFile):
            # Generate a unique filename
            ext = image.name.split(".")[-1]
            filename = f"public/book/{uuid.uuid4()}.{ext}"
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME

            # Upload to MinIO
            minio_client.upload_fileobj(
                Fileobj=image,
                Bucket=bucket_name,
                Key=filename,
                ExtraArgs={"ContentType": image.content_type},
            )

            # Construct the full URL
            file_url = f"{minio_client.meta.endpoint_url}/{settings.AWS_STORAGE_BUCKET_NAME}/{filename}"
            instance.image_url = file_url

        instance.save()

        return instance
