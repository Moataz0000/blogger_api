from django.contrib import admin
from ..models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at', 'is_active']
    search_fields = ['title']
    search_help_text = 'Search by post title...'
    readonly_fields = ['slug', 'created_at']
    list_filter = ['is_active', 'created_at']
