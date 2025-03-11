from django.shortcuts import render
from db_connection import db
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.

scrap_collection = db['scrapper']


def paginate(query, page_number):
    ITEMS_PER_PAGE = 10
    total_items = scrap_collection.count_documents(query)
    total_pages = (total_items // ITEMS_PER_PAGE) + (1 if total_items % ITEMS_PER_PAGE > 0 else 0)
    page_number = max(1, min(page_number, total_pages))
    skip_count = (page_number - 1) * ITEMS_PER_PAGE
    scraped_data = scrap_collection.find(query).sort("postdate", -1).skip(skip_count).limit(ITEMS_PER_PAGE)
    return scraped_data, total_pages, page_number


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
        try:
            query["postdate"]["$gte"] = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y%m%d")
        except ValueError:
            pass
    if end_date:
        try:
            query["postdate"]["$lte"] = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y%m%d")
        except:
            pass
    
    page_number = int(request.GET.get('page',1))
    scraped_data, total_pages, page_number = paginate(query, page_number)

    return render(request, "scraper_app/live_monitor.html", {
        'scraped_data': scraped_data,
        'page_number': page_number,
        'total_pages': total_pages,
        'platform': platform,
        'keyword': keyword,
        'start_date': start_date,
        'end_date': end_date,
    })


