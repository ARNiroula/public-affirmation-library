import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django import forms
from django.conf import settings
from django.utils.html import format_html
from django.contrib import admin, messages

from .models import Book
from book_copy.models import BookCopy
from utils.storage import minio_client

# Register your models here.


class BookAdminForm(forms.ModelForm):
    image_file = forms.FileField(required=False, label="Upload Image")
    pub_date = forms.DateField(widget=forms.TextInput(attrs={"type": "text"}))

    number_of_copies = forms.IntegerField(
        required=False, min_value=0, initial=0, label="Number of Copies"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Pre-fill number_of_copies for existing objects
        self.request = kwargs.get("request", None)
        if self.instance and self.instance.pk:
            self.fields["number_of_copies"].initial = self.instance.copies.count()

    class Meta:
        model = Book
        fields = [
            "isbn",
            "name",
            "topic",
            "summary",
            "pub_date",
            "cover_url",
        ]

    class Media:
        css = {"all": ["https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css"]}
        js = [
            "https://cdn.jsdelivr.net/npm/flatpickr",
            "/static/js/init_flatpickr.js",
        ]

    def save(self, commit=True):
        print(commit)
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
            instance.cover_url = file_url

        # Handle Book Copies
        desired_count = self.cleaned_data.get("number_of_copies", 0)
        current_copies_qs = instance.copies.all()
        current_count = current_copies_qs.count()

        if desired_count > current_count:
            instance.save()
            BookCopy.objects.bulk_create(  # pyright: ignore
                [BookCopy(book=instance) for _ in range(desired_count - current_count)]
            )
        elif desired_count < current_count:
            instance.save()
            excess_needed = current_count - desired_count
            removable_copies = current_copies_qs.filter(status="available")[
                :excess_needed
            ]
            actually_removed = removable_copies.count()

            # Delete only available copies
            removable_copies.delete()

            # Inform admin of partial deletion if needed
            if hasattr(self, "request") and actually_removed < excess_needed:
                messages.warning(
                    self.request,
                    f"Only {actually_removed} of {excess_needed} copies were deleted. "
                    f"Some are in use (on loan/reserved).",
                )

        return instance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    readonly_fields = ["cover_url", "image_preview", "total_copies"]
    fields = [
        "isbn",
        "name",
        "topic",
        "summary",
        "pub_date",
        "cover_url",
        "image_file",
        "image_preview",
        "number_of_copies",
        "total_copies",
    ]

    def image_preview(self, obj):
        if obj.cover_url:
            return format_html(
                '<img src="{}" style="max-height: 200px;"/>', obj.cover_url
            )
        return "No image available"

    image_preview.short_description = "Current Image"  # pyright: ignore

    def total_copies(self, obj):
        return obj.copies.count()

    total_copies.short_description = "Total Copies"  # pyright: ignore
