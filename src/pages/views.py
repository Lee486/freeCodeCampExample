from django.http import HttpResponse
from django.shortcuts import render
from flask import request

# Create your views here.
def home_view(request, *args, **kwargs):
    print("args and kwargs:", args, kwargs)
    print("request:", request.user)
    #return HttpResponse("<h1> Home Page </h1?>")
    return render (request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render (request, "contact.html", {})
    
def about_view(request, *args, **kwargs):
    context = {
        "text" : "about me and all these filters",
        "number" : 123,
        "bool" : True,
        "list" : [123, 456, 789, "what", "up", "danger"]
    }
    return render (request, "about.html", context)
    