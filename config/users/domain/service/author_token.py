from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from users.models.author import Author


class AuthorTokenService:

    @staticmethod
    def create_author_token(user: Author):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
