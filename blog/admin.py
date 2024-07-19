from django.contrib import admin
from .models import Resource, JournalEntry

# Register your models here.


@admin.register(Resource)
# Custom admin class for the Resource model
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type')
    search_fields = ['title', 'resource_type']
    list_filter = ('title', 'resource_type')


@admin.register(JournalEntry)
# Custom admin class for the Journal Entry model
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'mood')
    search_fields = ['title', 'user', 'mood', 'resource_type']
    list_filter = ('title', 'user', 'mood')
