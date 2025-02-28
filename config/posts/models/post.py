from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from users.models.author import Author


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="posts")
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/images", blank=True, null=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author.username} | Write | {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
        ]
