from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.

class Mood(models.Model):
    """
    Mood model
    """
    MOOD_TYPES = [
        ('H', 'Happy'),
        ('N', 'Neutral'),
        ('S', 'Sad'),
    ]
    mood = models.CharField(max_length=1, choices=MOOD_TYPES)
    reason = models.CharField(max_length=200, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"REASON: {self.reason}"

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"TITLE: {self.title}"

class JournalEntry(models.Model):
    """
    Journal entry model
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    entry_text = models.TextField()
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"TITLE: {self.title}, ENTRY TEXT: {self.entry_text}"