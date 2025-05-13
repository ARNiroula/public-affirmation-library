from django.contrib import admin
from django.utils.html import format_html

from .models import Exhibition
from event.admin import EventAdminForm


class ExhibitionAdminForm(EventAdminForm):
    class Meta:  # pyright: ignore
        model = Exhibition
        fields = "__all__"


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    form = ExhibitionAdminForm
    list_display = (
        "event_name",
        "start_date_time",
        "end_date_time",
        "expenses",
        "total_signed",
        "event_topic",
    )
    readonly_fields = [
        "image_preview",
        "total_signed",
        "image_url",
    ]
    list_filter = (
        "start_date_time",
        "event_topic",
        "expenses",
    )
    search_fields = ("event_name",)

    def image_preview(self, obj):
        if obj.cover_url:
            return format_html(
                '<img src="{}" style="max-height: 200px;"/>', obj.cover_url
            )
        return "No image available"

    image_preview.short_description = "Current Image"  # pyright: ignore

    def total_signed(self, obj):
        return obj.users.count()

    total_signed.short_description = "People Signed"  # pyright: ignore
