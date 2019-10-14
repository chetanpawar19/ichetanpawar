from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'), #to access request like "localhost/blog/2"  2 is blog id
]
