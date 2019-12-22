from django.urls import path
from . import views

urlpatterns = [
    path('', views.allnotes, name='allnotes'),
    path('<int:notes_id>/', views.detail, name='detail'), #to access request like "localhost/notes/2"  2 is notes id
]
