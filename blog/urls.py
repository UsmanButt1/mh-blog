from . import views
from blog.views import IndexView, JournalEntryView, AddJournalEntry, EditJournalEntry, DeleteJournalEntry
from django.urls import path

urlpatterns = [
    path('journalentries/', views.JournalEntryView.as_view(), name='journalentries'),
    path('new/', AddJournalEntry, name='addjournalentry'),
    path('editjournalentry/<int:journalentry_id>', views.EditJournalEntry, name='editjournalentry'), # noqa
    path('delete/<int:journalentry_id>/', views.DeleteJournalEntry, name='deletejournalentry'), # noqa
]
