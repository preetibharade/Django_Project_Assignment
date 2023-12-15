from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidatedirectory
from .forms import CandidateForm


# Create your views here.
def index(request):
  return render(request, 'index.html')
  # views.py


def candidate_list(request):
    candidates = Candidatedirectory.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'create_candidate.html', {'form': form})

def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidatedirectory, id=candidate_id)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'edit_candidate.html', {'form': form, 'candidate': candidate})

def view_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidatedirectory, id=candidate_id)
    return render(request, 'view_candidate.html', {'candidate': candidate} )

def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidatedirectory, id=candidate_id)
    candidate.delete()
    return redirect('candidate_list')
def index_view(request):
    return render(request, 'index.html')