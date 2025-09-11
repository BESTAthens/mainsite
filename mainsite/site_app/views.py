from django.shortcuts import render
from django.http import HttpResponse


#εδώ τα views
def home(request):
    return render(request, "site_app/home.html") #αυτά ψάχνουν στο templates/site_app

def about(request):
    return render(request, "site_app/about.html")

def events(request):
    return render(request, "site_app/events.html")

def team(request):
    return render(request, "site_app/team.html")

def sponsors(request):
    return render(request, "site_app/sponsors.html")

def contact(request):
    return render(request, "site_app/contact.html")
