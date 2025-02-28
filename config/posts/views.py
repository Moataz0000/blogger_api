from rest_framework import generics, permissions

from .models.post import Post
from .permissions import IsAuthorUser
from .serializers import PostCreateSerializer, PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorUser]
    lookup_field = "slug"
    lookup_url_kwarg = "post_slug"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class PostCreateView(generics.CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthorUser]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
