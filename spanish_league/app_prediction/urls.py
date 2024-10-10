from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('matches',views.live_matches, name='matches'),
    path('tactics',views.matchTactics, name='matchTactics')
]