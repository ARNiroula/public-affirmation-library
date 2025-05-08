import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django import forms
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html

from .models import Room, Booking
from utils.storage import minio_client


# Register your models here.
class RoomAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False, label="Upload Image")

    class Meta:
        model = Room
        fields = ["room_id", "capacity", "descr", "image_url"]

    def save(self, commit=True):
        instance = super().save(commit=False)

        image = self.files.get("image_file")
        if image and isinstance(image, InMemoryUploadedFile):
            # Generate a unique filename
            ext = image.name.split(".")[-1]
            filename = f"public/room/{uuid.uuid4()}.{ext}"
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

        if commit:
            instance.save()
        return instance


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    form = RoomAdminForm
    readonly_fields = ["image_url", "image_preview"]
    fields = [
        "room_id",
        "capacity",
        "descr",
        "image_url",
        "image_file",
        "image_preview",
    ]

    def image_preview(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" style="max-height: 200px;"/>', obj.image_url
            )
        return "No image available"

    image_preview.short_description = "Current Image"  # pyright: ignore


admin.site.register(Booking)
