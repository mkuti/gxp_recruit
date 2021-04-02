from django.shortcuts import render
from .models import Job
from .forms import SearchForm

# Create your views here.
def job_results(request):
    q = ''
    results = []

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Job.objects.all()
    
    return render(request, 'job_results.html', {'form': form, 'q': q, 'results': results})