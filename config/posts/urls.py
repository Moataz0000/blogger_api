from django.urls import path

from .views import PostCreateView, PostDetailView, PostListView

app_name = "posts"


urlpatterns = [
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:post_slug>/", PostDetailView.as_view(), name="post_detail"),
]
