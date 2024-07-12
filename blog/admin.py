from django.contrib import admin
from .models import Mood, Resource, JournalEntry

# Register your models here.

admin.site.register(Mood)
admin.site.register(Resource)
admin.site.register(JournalEntry)