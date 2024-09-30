from django.shortcuts import render
from spanish_league import settings
import requests 
import json

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


def live_matches(request):
    url = 'http://api.football-data.org/v4/competitions/2014/matches?matchday=8'
    api_key = settings.API_FOOTBALL_KEY
    headers = { 'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)

    #checking to see if we really have received the expected data from the data
    if response.status_code == 200:
        data_II = response.json()
        liveMatches = data_II["matches"][0]                                    #retrieves matches diction from the json file             
        homeTeam = data_II["matches"][0]                                     
        awayTeam = data_II["matches"][0]
    return render(request, 'live.html', {"liveMatches": liveMatches,"homeTeam":homeTeam, "awayTeam":awayTeam})