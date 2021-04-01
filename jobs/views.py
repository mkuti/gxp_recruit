from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Job
from .filters import JobFilter

# Create your views here.
class search_jobs(ListView):
    model = Job
    template_name = 'job_results.html'