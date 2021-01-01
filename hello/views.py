from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
   
def rayyan(request):
    return HttpResponse("Hello Rayyan")


def ibrahim(request):
    return HttpResponse("Hello Ibrahim") 

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })