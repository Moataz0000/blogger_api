import bleach
from rest_framework import serializers

from .domain.service.author_token import AuthorTokenService
from .models.author import Author


class AuthorCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Author
        fields = ["email", "username", "phone_number", "full_name", "password"]

    def validate(self, attrs):
        attrs["full_name"] = bleach.clean(attrs["full_name"], strip=True)
        return attrs

    def create(self, validated_data):
        email = validated_data["email"]
        username = email.split("@")[0]
        validated_data["username"] = username

        user = Author.objects.create(**validated_data)
        self.tokens = AuthorTokenService.create_author_token(user)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["tokens"] = self.tokens
        return data
