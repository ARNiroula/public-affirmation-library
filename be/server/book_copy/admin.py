from django.contrib import admin

from .models import BookCopy


# Register your models here.
@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ("copy_id", "book__name", "status", "last_booked", "when_returned")
    readonly_fields = (
        "last_booked",
        "when_returned",
    )
    list_filter = ("status",)

    def last_booked(self, obj):
        query = obj.rentals.order_by("-borrow_date").first()
        if not query:
            return ""
        return query.borrow_date

    def when_returned(self, obj):
        query = obj.rentals.order_by("-borrow_date").first()
        if not query:
            return ""
        return "Not Returned" if not query.actual_date else query.actual_date


# admin.site.register(BookCopy)
