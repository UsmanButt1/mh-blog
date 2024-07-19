from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

MOOD_TYPES = ((1, "happy"), (2, "neutral"), (3, "sad"))

# Create your models here.


class Resource(models.Model):
    """
    Resource model
    """
    title = models.CharField(max_length=100, null=True)
    resource_type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"


class JournalEntry(models.Model):
    """
    Journal entry model
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    entry_text = models.TextField(blank=False, null=False)
    mood = models.IntegerField(choices=MOOD_TYPES, default=2)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True)
    resourcetitle = models.CharField(max_length=200, blank=True, null=True)
    resourceurl = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"TITLE: {self.title}, ENTRY TEXT: {self.entry_text}"
