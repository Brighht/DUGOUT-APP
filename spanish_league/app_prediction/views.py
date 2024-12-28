from django.shortcuts import render,redirect
from spanish_league import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
import requests

# # Create your views here.
# def signUp(request):
#     if request.method == 'POST':
#         username =request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(username = username).exist():
#                 messages.info(request, "Username Exists")
#                 return redirect('signup')
        
#             elif User.objects.filter(email = email).exits():
#                 messages.info(request, "Email ALready Used")
#                 return redirect('signup')

#             else:
#                 return redirect('login')
#         else:
#             return render(request, 'signup.html')

#     return render(request, 'signup.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

    
#         user = User.auth.authenticate(username=username, password = password1)
#         user.save()

#         if User is not None:
#             auth.login(request, User)
#             return redirect('home')
#         else:
#             return redirect('login')
#     return render(request, 'home.html')
    

def home(request):                    
    url = 'https://api.football-data.org/v4/competitions/PD/standings'                  #this makes a request to the uri server
    api_key = settings.API_FOOTBALL_KEY                                                 #informing header where to find API_KEY
    headers = { 'X-Auth-Token': api_key}                                                #header of request

    response = requests.get(url, headers=headers)                                       #retreiving response from the api 

    if response.status_code == 200:                                                     #checking for success or successful retreival
        data = response.json()                                                          #assigning retreived respose to data variable
        standings = data['standings'][0]['table']                                       #standings retrieves the value from the table key in the standing dict
    return render(request, 'index.html',{'standings':standings})

# def upcoming_matches(request):
    
#     url = 'http://api.football-data.org/v4/competitions/2014/matches?matchday=8'
#     api_key = settings.API_FOOTBALL_KEY
#     headers = { 'X-Auth-Token': api_key}
#     response = requests.get(url, headers=headers)


#     #checking to see if we really have received the expected data from the data
#     if response.status_code == 200:
#         upcomingMatches = []
#         data_II = response.json()
#         for match in data_II['matches']:                                  #This iterates throught the json file and locates the values contained by the key "matches"
#             upcomingMatches.append(match)                                                                     
#     return render(request, 'live.html', {"upcomingMatches": upcomingMatches})

#     def matchTactics(request):
#         pass