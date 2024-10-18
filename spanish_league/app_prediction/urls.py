from django.urls import path
from . import views

urlpatterns = [
    path('',views.signUp, name='signup'),
    path('',views.home, name='home'),
    path('matches',views.upcoming_matches, name='matches')
]