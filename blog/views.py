from django.views import generic, View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
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
            JournalEntry.slug = slugify(JournalEntry.title)
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
def EditJournalEntry(request, journalentry_id):
    journalentry = get_object_or_404(JournalEntry, id=journalentry_id)

    if request.method == 'POST':
        journalentryform = JournalEntryForm(data=request.POST, instance=journalentry)

        if journalentryform.is_valid() and journalentry.user == request.user:
            journalentry = journalentryform.save(commit=False)
            journalentry.save()
            messages.add_message(request, messages.SUCCESS, 'Journal Entry Updated!')
            return HttpResponseRedirect(reverse('journalentries'))
        else:
            messages.add_message(request, messages.ERROR, 'Error Updating Journal Entry!')
    else:
        journalentryform = JournalEntryForm(instance=journalentry)

    context = {'form': journalentryform, 'journalentry': journalentry}
    return render(request, 'edit_journal_entry.html', context)

'''
Delete Journal Entry
'''
@login_required
def DeleteJournalEntry(request, journalentry_id):
    journalentry = get_object_or_404(JournalEntry, id=journalentry_id)

    if request.method == 'POST':
        if journalentry.user == request.user:
            journalentry.delete() 
            messages.add_message(request, messages.SUCCESS, 'Journal entry deleted!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only delete your own journal entries!')
        return redirect('journalentries')
    
    context = {'journalentry': journalentry}
    return render(request, 'confirm_delete_journal_entry.html', context)
    
'''
View Journal Entries
'''
class JournalEntryView(LoginRequiredMixin, generic.ListView):
    model = JournalEntry
    template_name = "journal_entries.html"
    paginate_by = 6

    def get_queryset(self):
        return JournalEntry.objects.all().order_by('-published_on')

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JournalEntryForm()
        return context
