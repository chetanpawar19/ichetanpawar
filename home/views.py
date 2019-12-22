from django.shortcuts import render
from .models import Highlights

def home(request):
    highlights = Highlights.objects
    return render(request, 'home/index.html',{'highlights':highlights})
