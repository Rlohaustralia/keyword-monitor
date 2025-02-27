from django.shortcuts import render
from db_connection import db

# Create your views here.

def live_monitor_view(request):
    scrap_collection = db['scrapper']
    naver_blogs = scrap_collection.find()
    return render(request, "scraper_app/live_monitor.html", {'naver_blogs': naver_blogs})
