from django.shortcuts import render
from jobs.models import Job
from jobs.forms import SearchForm

def home(request):
    '''A view that displays the home page with search bar'''
    print(Job.objects.all())
    form = SearchForm()
    q = ''
    return render(request, 'home.html', {'form': form})
