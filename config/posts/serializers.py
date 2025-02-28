from rest_framework import serializers
from taggit.serializers import TagListSerializerField

from .models.post import Post


class PostSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d-%H:%M:%S")
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "slug",
            "content",
            "tags",
            "is_active",
            "created_at",
            "image",
        ]

    def get_author(self, author: Post):
        return author.author.username


class PostCreateSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ["title", "content", "tags", "image"]
