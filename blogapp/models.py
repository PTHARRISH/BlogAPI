from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_image", blank=True, null=True
    )
    facebook = models.URLField(max_length=255, blank=True, null=True)
    yotube = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.username)


# A URLField is a specialized CharField that's designed to store URLs
# and is validated by Django's URLValidator.
# It ensures that the entered value is a valid URL format
# before saving to the database.

# A SlugField is essentially a CharField
# that's specifically designed to store URL-friendly strings containing
# only letters, numbers, underscores, or hyphens.
# It's commonly used for creating clean, readable URLs.


class Blog(models.Model):
    CATEGORY = (
        ("Technology", "Technology"),
        ("Economy", "Economy"),
        ("Business", "Business"),
        ("Sports", "Sports"),
        ("Lifestyle", "Lifestyle"),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="blogs",
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    published_time = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=255, choices=CATEGORY, blank=True, null=True)
    featured_image=models.ImageField(upload_to="blog_img",blank=True,null=True)



# Your approach (works but not recommended):

# from django.contrib.auth import get_user_model
# User = get_user_model()
# author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# In short, use settings.AUTH_USER_MODEL for ForeignKey fields in models
# because it avoids timing issues, migration problems,
# and works safely with custom user models
