from django.shortcuts import render, get_object_or_404
from .models import Notes

def allnotes(request):
    notes = Notes.objects
    return render(request, 'notes/allnotes.html',{'notes':notes})

def detail(request, notes_id):
    detailnote = get_object_or_404(Notes, pk=notes_id)  #pk primary
    return render(request, 'notes/detailnote.html',{'note':detailnote})
