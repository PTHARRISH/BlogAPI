from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


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

# Slug:
# A SlugField is essentially a CharField
# that's specifically designed to store URL-friendly strings containing
# only letters, numbers, underscores, or hyphens.
# It's commonly used for creating clean, readable URLs.

# Common Usage Pattern
# This field configuration is typically used when:
# You want to auto-generate slugs from other fields (like a title)
# You don't want to require manual slug entry in forms
# You need each slug to be unique for URL routing
# You want to allow the slug to be empty initially
# and populate it programmatically
# For example, in a typical blog entry URL:
# https://www.geeksforgeeks.org/python/add-the-slug-field-inside-django-model/


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
    featured_image = models.ImageField(upload_to="blog_img", blank=True, null=True)

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        self.slug = slug

        if not self.is_draft and self.published_time is None:
            self.published_time = timezone.now()

        super().save(*args, **kwargs)


# class Meta:
#     ordering = ['-published_time', 'title']  # Newest first, then alphabetically by title

# The class Meta:
# with ordering = ["-published_time"] is a Django model metadata configuration
# that defines the default ordering behavior for database queries on this model.

# super().save(*args, **kwargs):
# The super().save(*args, **kwargs) is a critical call in Django
# when overriding the model's save() method.
# This line calls the parent class's (Model) original save method,
# which performs the actual database operation.
# Without this call, your data won't be saved to the database


# Your approach (works but not recommended):

# from django.contrib.auth import get_user_model
# User = get_user_model()
# author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# In short, use settings.AUTH_USER_MODEL for ForeignKey fields in models
# because it avoids timing issues, migration problems,
# and works safely with custom user models
