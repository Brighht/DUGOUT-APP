from django.shortcuts import render
from spanish_league import settings
import requests 

# Create your views here.
def home(request):
    url = 'https://api.football-data.org/v4/competitions/PD/standings'
    api_key = settings.API_FOOTBALL_KEY
    headers = { 'X-Auth-Token': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        standings = data['standings'][0]['table']
    return render(request, 'home.html',{'standings':standings})


