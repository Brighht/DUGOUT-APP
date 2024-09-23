from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('',views.live_matches, name='home'),
]