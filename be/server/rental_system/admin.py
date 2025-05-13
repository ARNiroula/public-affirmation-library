import datetime

from django import forms
from django.contrib import admin
from django.db import transaction
from django.db.models import Q, F
from django.utils.translation import gettext_lazy as _
# from django.db.models import F

from .models import Rental
from book_copy.models import BookCopy
from invoice.models import Invoice


class RentalModelForm(forms.ModelForm):
    class Meta:
        model = Rental
        # fields = "__all__"
        exclude = ("actual_date",)


# Register your models here.
class IsLateFilter(admin.SimpleListFilter):
    title = _("Is Late")  # The title for the filter
    parameter_name = "is_late"  # The URL parameter for the filter

    def lookups(self, request, model_admin):
        # This defines the filter options available in the sidebar
        return (
            (True, _("Late")),
            (False, _("On time")),
        )

    def queryset(self, request, queryset):
        # This filters the queryset based on the selected filter
        today = datetime.date.today()
        if self.value() == "True":
            return queryset.filter(
                Q(actual_date__isnull=False, expected_date__lt=F("actual_date"))
                | Q(expected_date__lt=today)
            )
        if self.value() == "False":
            return queryset.filter(
                Q(actual_date__isnull=False, expected_date__gte=F("expected_date"))
                | Q(expected_date__gte=today)
            )  # On time if today is before or same as the expected date


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = (
        # "copy__copy_id",
        # "copy__book__name",
        "rental_id",
        "copy_id",
        "book_name",
        "borrow_date",
        "expected_date",
        "actual_date",
        "is_late",
        "customer",
    )
    search_fields = ("cust__username", "copy__book__name")
    list_filter = ("borrow_date", IsLateFilter)
    readonly_fields = ("is_late",)

    # Custom name for copy__book__name
    def book_name(self, obj):
        return obj.copy.book.name

    book_name.admin_order_field = "copy__book__name"
    book_name.short_description = "Book Name"

    # Custom name for copy__copy_id
    def copy_id(self, obj):
        return obj.copy.copy_id

    copy_id.admin_order_field = "copy__copy_id"
    copy_id.short_description = "Copy ID"

    # Custom name for copy__copy_id
    def customer(self, obj):
        return obj.cust

    copy_id.admin_order_field = "cust"
    copy_id.short_description = "Customer who rented the book"

    # Custom is late lookup
    def is_late(self, obj):
        if not obj.actual_date:
            if not obj.expected_date:
                return
            return "Late" if obj.expected_date < datetime.date.today() else "On Time"
        return "Late" if obj.expected_date < obj.actual_date else "On Time"

    def save_model(self, request, obj, form, change):
        if not obj.actual_date:
            super().save_model(request, obj, form, change)
            return

        with transaction.atomic():
            book_copy = BookCopy.objects.select_for_update().get(pk=obj.copy.copy_id)
            book_copy.status = "available"
            book_copy.save()

            # Generate the Invoice
            invoice_amount = self.calculate_invoice_amount(obj)
            invoice = Invoice.objects.create(
                rental=obj,
                invoice_date=datetime.date.today(),
                total_amount=invoice_amount,
            )  # Create the Invoice
            print(f"Invoice {invoice.invoice_id} Created for {obj.cust.username}")
            super().save_model(request, obj, form, change)

    def calculate_invoice_amount(self, rental):
        inital_diff = float((rental.expected_date - rental.actual_date).days)
        if rental.actual_date > rental.expected_date:
            return (inital_diff * 0.2) + (
                float((rental.actual_date - rental.expected_date).days) * 0.4
            )
        else:
            return inital_diff
