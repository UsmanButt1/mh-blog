from django.views import generic, View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from .forms import JournalEntryForm
from django.views.generic import TemplateView, View

# Create your views here.

'''
Index View for Homepage
'''
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

'''
Add Journal Entry View
'''
@login_required
def AddJournalEntry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, f"Your journal entry '{instance.title}' has been saved.")
                return redirect('journalentries')
            else:
                messages.error(request, "You must be logged in to add an entry.")
    else:
        form = JournalEntryForm()
    return render(request, 'add_journal.html', {'form': form})

'''
Edit Journal Entry View
'''
@login_required
def EditJournalEntry(request, pk):
    entry = get_object_or_404(JournalEntry.objects.get(pk=pk))
    
    if request.user != entry.User:
        messages.error
        (request, "You do not have permission to edit this entry")
        return redirect('edit_journal.html', {'form': form})
    
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your journal entry '{entry.title}' has been updated.")
            return redirect('journalentries')
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'edit_journal.html', {'form': form})

'''
Delete Journal Entry
'''
@login_required
def DeleteJournalEntry(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)

    if request.user != entry.User:
        messages.error
        (request, "You do not have permission to edit this entry")
        return redirect('edit_journal_entry.html', {'form': form})

    if request.method == 'POST':
        entry.delete()
        messages.success(request, f"Your journal entry '{entry.title}' has been deleted.")
        return redirect('journalentries')

'''
View Journal Entries
'''
class JournalEntryView(LoginRequiredMixin, generic.ListView):
    model = JournalEntry
    template_name = "journal_entries.html"
    paginate_by = 6

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JournalEntryForm()
        return context
