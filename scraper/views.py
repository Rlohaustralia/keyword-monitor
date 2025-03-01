from django.shortcuts import render
from db_connection import db

# Create your views here.

def live_monitor_view(request):
    scrap_collection = db['scrapper']
    scraped_data = scrap_collection.find().sort("postdate",-1)
    return render(request, "scraper_app/live_monitor.html", {'scraped_data': scraped_data})
