from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    created_by_username = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Book
        fields = [
            "id", "title", "author", "publication_date", "genre",
            "description", "created_by", "created_by_username",
            "created_at", "updated_at",
        ]
        read_only_fields = ["created_by"]
