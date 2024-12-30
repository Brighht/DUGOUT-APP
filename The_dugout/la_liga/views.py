from django.shortcuts import render,redirect
from tunnel_vision import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages,auth
import requests

# # Create your views here.    

def home(request):                    
    url = 'https://api.football-data.org/v4/competitions/PD/standings'                  #this makes a request to the uri server
    api_key = settings.API_FOOTBALL_KEY                                                 #informing header where to find API_KEY
    headers = { 'X-Auth-Token': api_key}                                                #header of request

    response = requests.get(url, headers=headers)                                       #retreiving response from the api 

    if response.status_code == 200:                                                     #checking for success or successful retreival
        data = response.json()                                                          #assigning retreived respose to data variable
        standings = data['standings'][0]['table']                                       #standings retrieves the value from the table key in the standing dict
    return render(request, 'index.html',{'standings':standings})
