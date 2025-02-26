from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def live_monitor_view(request):
    return render(request, "scraper_app/live_monitor.html")