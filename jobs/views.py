from django.shortcuts import render
from .models import Job

def job(request):
    jobs = Job.objects
    return render(request, 'jobs/job.html',{'jobs':jobs})
