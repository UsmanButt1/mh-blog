from django.urls import path
from .views import IndexView, journal_entries, add_journal_entry, edit_journal_entry, delete_journal_entry

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('journal_entries/', journal_entries, name='journal_entries'),
    path('new/', add_journal_entry, name='add_journal_entry'),
    path('edit_journal_entry/<int:pk>/', edit_journal_entry, name='edit_journal_entry'),
    path('delete/<int:pk>/', delete_journal_entry, name='delete_journal_entry'),
]