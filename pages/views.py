from django.shortcuts import render
from jobs.models import Job
from jobs.views import search_jobs

def home(request):
    '''A view that displays the home page'''
    return render(request, 'home.html')
