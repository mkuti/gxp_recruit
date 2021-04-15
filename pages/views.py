from django.shortcuts import render
from jobs.models import Job
from jobs.filters import JobFilter

def home(request):
    '''A view that displays the home page with a search bar'''
    jobs = Job.objects.all()
    for job in jobs:
        print(job.description)
    filtered_jobs = JobFilter(request.GET, queryset=jobs)

    return render(request, 'home.html', {'filter': filtered_jobs})
