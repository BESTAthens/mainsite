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

def joinus(request):
    return render(request, "site_app/joinus.html")

def clue1(request):
    return render(request, "site_app/clue1.html")

def clue2(request):
    return render(request, "site_app/clue2.html")

def clue3(request):
    return render(request, "site_app/clue3.html")

def clue4(request):
    return render(request, "site_app/clue4.html")

def IT(request):
    return render(request, "site_app/IT.html")