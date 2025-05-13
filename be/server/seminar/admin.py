import uuid

from django import forms
from django.db.models import Sum
from django.conf import settings
from django.contrib import admin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.html import format_html

from .models import Seminar
from sponser.models import SponserSeminarRelationship
from utils.storage import minio_client
# Register your models here.


class SponserSeminarInline(admin.TabularInline):
    model = SponserSeminarRelationship
    extra = 1


class SeminarAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False, label="Upload Image")

    class Meta:
        model = Seminar
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


class SeminarModelAdmin(admin.ModelAdmin):
    form = SeminarAdminForm
    inlines = [SponserSeminarInline]
    filter_tags = ("event_type",)
    list_display = (
        "event_name",
        "start_date_time",
        "end_date_time",
        "event_topic",
        "keynote_speaker",
        "seminar_type",
        "total_sponsors",
        "total_amount",
    )
    readonly_fields = [
        "image_preview",
        "total_sponsors",
        "total_amount",
    ]

    search_fields = (
        "event_name",
        "keynote_speaker",
    )

    list_filter = (
        "start_date_time",
        "event_topic",
    )

    def image_preview(self, obj):
        if obj.cover_url:
            return format_html(
                '<img src="{}" style="max-height: 200px;"/>', obj.cover_url
            )
        return "No image available"

    image_preview.short_description = "Current Image"  # pyright: ignore

    def total_sponsors(self, obj):
        return obj.sponser.count()

    total_sponsors.short_description = "Total Sponsors"  # pyright: ignore

    def total_amount(self, obj):
        total = obj.sponserseminarrelationship_set.aggregate(
            total_amount=Sum("amount")
        )["total_amount"]
        return total if total is not None else 0

    total_amount.short_description = "Total Amount"  # pyright: ignore


admin.site.register(Seminar, SeminarModelAdmin)
