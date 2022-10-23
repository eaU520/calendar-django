from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("All Events")
    
def detail(request, event_id):
    return HttpResponse("Event Title: %s" % event_id)
