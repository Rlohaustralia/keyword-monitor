from django.shortcuts import render
from db_connection import db
from datetime import datetime

# Create your views here.

scrap_collection = db['scrapper']

def live_monitor_view(request):

    # Filtering keyword
    platform = request.GET.get("platform","").strip()
    keyword = request.GET.get("keyword","").strip()
    start_date = request.GET.get("start_date","").strip()
    end_date = request.GET.get("end_date","").strip()
    
    query = {}

    if platform:
        query["platform"] = platform
    if keyword:
        query["keyword"] = {"$regex" : keyword, "$options": "i"}
    if start_date or end_date:
        query["postdate"] = {}
    if start_date:
        query["postdate"]["$gte"] = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y%m%d")
    if end_date:
        query["postdate"]["$lte"] = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y%m%d")
        
    if query:
        scraped_data = scrap_collection.find(query).sort("postdate", -1)
    else:
        scraped_data = scrap_collection.find().sort("postdate", -1)
    


    return render(request, "scraper_app/live_monitor.html", {'scraped_data': scraped_data})

