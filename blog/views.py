from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from .forms import JournalEntryForm, MoodForm, ResourceForm, SignUpForm
from django.views.generic import TemplateView, View

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class SignUpView(View):
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, f"Your account '{instance.user.username}' has been created")
                return redirect('index.html')
        else:
            form = SignUpForm()
        return render(request, self.template_name, {'form': form})

@login_required
def add_journal_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f"Your journal entry '{instance.title}' has been saved.")
            return redirect('journal_entries.html')
    else:
        form = JournalEntryForm()
    return render(request, 'add_journal.html', {'form': form})

@login_required
def edit_journal_entry(request, pk):
    entry = JournalEntry.objects.get(pk=pk)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your journal entry '{entry.title}' has been updated.")
            return redirect('journal_entries.html')
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'edit_journal.html', {'form': form})

@login_required
def delete_journal_entry(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, f"Your journal entry '{entry.title}' has been deleted.")
        return redirect('journal_entries.html')

@login_required
def journal_entries(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-published_on')
    return render(request, 'journal_entries.html', {'entries': entries})