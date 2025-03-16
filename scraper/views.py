from django.shortcuts import render, redirect
from db_connection import db
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
import pandas
import subprocess

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


def apply_filter(request):
    # Filtering keyword
    platform = request.GET.get("platform", "").strip()
    keyword = request.GET.get("keyword", "").strip()
    start_date = request.GET.get("start_date", "").strip()
    end_date = request.GET.get("end_date", "").strip()

    filter_query = {}

    if platform:
        filter_query["platform"] = platform
    if keyword:
        filter_query["keyword"] = {"$regex": keyword, "$options": "i"}
    if start_date or end_date:
        filter_query["postdate"] = {}
    if start_date:
        try:
            filter_query["postdate"]["$gte"] = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y%m%d")
        except ValueError:
            pass
    if end_date:
        try:
            filter_query["postdate"]["$lte"] = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y%m%d")
        except ValueError:
            pass
    print(filter_query)
    return filter_query, platform, keyword, start_date, end_date


def live_monitor_view(request):

    query, platform, keyword, start_date, end_date = apply_filter(request)
    
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


def export_to_excel_view(request):
    # Get the filter query from the request
    filter_query, platform, keyword, start_date, end_date = apply_filter(request)

    if filter_query:
        data = list(scrap_collection.find(filter_query, {"_id": 0}))
    else:
        data = list(scrap_collection.find({}, {"_id": 0}))

    # Convert the fetched data into a Pandas DataFrame
    df = pandas.DataFrame(data)

    # Adjust index so it starts from 1 instead of 0 (for better user experience in Excel)
    df.index += 1  # Index starts from 1 instead of 0

    # Prepare the HTTP response as an Excel file download
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Set the content disposition header to indicate that this is a downloadable file
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Write the DataFrame to the Excel file and return it as a response
    # Use the openpyxl engine to handle the Excel file creation
    with pandas.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=True)  # Write DataFrame to Excel, including index

    return response
    

def refresh_data_view(request):
    if request.method == "POST":
        keyword_text = request.POST.get("keyword","").strip()
        try:
            subprocess.run(["python", "-m", "scraper.api.main", keyword_text], check=True)
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Error in refresh process: {e}", status=500)
    return redirect("live_monitor")