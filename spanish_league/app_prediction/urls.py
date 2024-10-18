from django.urls import path
from . import views

urlpatterns = [
    path('',views.signUp, name='signup.html'),
    path('home/',views.home, name='home'),
    path('matches/',views.upcoming_matches, name='matches')
]