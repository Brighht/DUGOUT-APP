from django.shortcuts import render
from spanish_league import settings
import requests 

# Create your views here.
def home(request):                                      
    url = 'https://api.football-data.org/v4/competitions/PD/standings'                  #this makes a request to the uri server
    api_key = settings.API_FOOTBALL_KEY                                                 #informing header where to find API_KEY
    headers = { 'X-Auth-Token': api_key}                                                #header of request

    response = requests.get(url, headers=headers)                                       #retreiving response from the api 

    if response.status_code == 200:                                                     #checking for success or successful retreival
        data = response.json()                                                          #assigning retreived respose to data variable
        standings = data['standings'][0]['table']                                       #standings retrieves the value from the table key in the standing dict
    return render(request, 'home.html',{'standings':standings})


def live_matches(request):
    url = 'http://api.football-data.org/v4/competitions/2014/matches?matchday=8'
    api_key = settings.API_FOOTBALL_KEY
    headers = { 'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)


    #checking to see if we really have received the expected data from the data
    if response.status_code == 200:
        liveMatches = []
        data_II = response.json()
        for match in data_II['matches']:                                  #This iterates throught the json file and locates the values contained by the key "matches"
            liveMatches.append(match)                                                                     
    return render(request, 'live.html', {"liveMatches": liveMatches})