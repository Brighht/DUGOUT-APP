from django.urls import path
from . import views

url_patterns = [
    path('',views.home, name='epl_home')
]