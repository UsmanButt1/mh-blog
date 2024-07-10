from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.
class JournalEntry(models.Model):
    """
    Journal Entry model
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    published_on = models.DateTimeField(auto_now_add=True)
    entry_text = models.TextField()
    mood_id = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    resource_id = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s Entry - {self.date}"

class Mood(models.Model):
    """
    Mood model
    """
    mood = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    """
    Resource model
    """
    RESOURCE_TYPES = [
        ('A', 'Article'),
        ('V', 'Video'),
        ('P', 'Podcast'),
    ]
    title = models.CharField(max_length=200)
    url = models.URLField()
    resource_type = models.CharField(max_length=1, choices=RESOURCE_TYPES)
    creation_date = models.DateTimeField(auto_now_add=True)