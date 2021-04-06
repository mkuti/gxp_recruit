from django.shortcuts import render
from .models import Job
from .forms import SearchForm

# Create your views here.
def job_results(request):
    """
    A view to show all jobs
    """
    jobs = Job.objects.filter(is_active=True)
    
    return render(request, 'job_results.html', {'jobs': jobs})