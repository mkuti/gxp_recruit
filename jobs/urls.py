from django.urls import path
from .views import job_results

urlpatterns = [
    path('', job_results, name='jobs'),
]