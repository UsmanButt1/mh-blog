from django import forms
from .models import Resource, JournalEntry


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        exclude = ['published_on', 'user', 'slug', ]
        resource = Resource.title
        labels = {
            "entry_text": "Enter your journal entry",
            "resource": "Resource Type",
            "resourcetitle": "Resource Title",
            "resourceurl": "Resource URL",
            }
