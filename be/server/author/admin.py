from django.contrib import admin

from .models import Author, AuthorBookRelationship
# Register your models here.

admin.site.register(AuthorBookRelationship)


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "total_books",
    )
    search_fields = (
        "fname",
        "mname",
        "lname",
    )

    readonly_fields = (
        "name",
        "total_books",
    )

    def name(self, obj):
        return str(obj)

    name.short_description = "Name of author"  # pyright: ignore

    def total_books(self, obj):
        return obj.book.count()

    total_books.short_description = "Books in Library"  # pyright: ignore


admin.site.register(Author, AuthorModelAdmin)
