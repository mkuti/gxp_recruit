from django.contrib import admin
from .models import Job, Contract, Schedule, Location

# Register your models here.
admin.site.register(Job)
admin.site.register(Contract)
admin.site.register(Schedule)
admin.site.register(Location)