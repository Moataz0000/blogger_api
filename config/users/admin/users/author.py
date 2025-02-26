from django.contrib import admin
from ...models.author import Author

@admin.register(Author)
class AuthorUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'email', 'phone_number']
    list_filter = ['date_joined']
    search_fields = ['username']
    search_help_text = 'Search by username'