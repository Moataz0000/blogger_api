from rest_framework import permissions
from users.models.author import Author


class IsAuthorUser(permissions.BasePermission):
    message = "You do not have permission to perform this action. only the authors user can do this action."
    author_allow_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, Author) and request.method in self.author_allow_methods:
            return True
        return False
