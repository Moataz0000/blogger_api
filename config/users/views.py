from rest_framework import generics
from rest_framework.response import Response

from .models.author import Author
from .serializer import AuthorCreateSerializer


class AuthorRegisterView(generics.CreateAPIView):
    model = Author
    serializer_class = AuthorCreateSerializer
