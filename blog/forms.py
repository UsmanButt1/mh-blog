from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mood, Resource, JournalEntry

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood', 'reason']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'url', 'resource_type']
    
class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        exclude = ['published_on', 'user']

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
        error_messages={'unique': 'A user with that username already exists. Please choose another username'}
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'Email'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'})
    )