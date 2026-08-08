from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "publication_date", "created_by", "created_at")
    list_filter = ("genre",)
    search_fields = ("title", "author", "created_by__username")