from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import keyword_collection, scrap_collection, add_keyword, get_all_keywords, update_keyword, delete_keyword
from django.http import HttpResponse, request
from django.contrib import messages
from django.http import HttpResponseBadRequest
import subprocess
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

@login_required
def keyword_view(request):
    if request.method == "POST":
        keyword_text = request.POST.get("keyword","").strip()
        user = str(request.user.id)

        # Not allow duplicated keyword
        if keyword_collection.find_one({"user" : user, "keyword": keyword_text}):
            return redirect('mykeyword')
        
        if keyword_text:
            add_keyword(user, keyword_text)
            try:
                subprocess.run(["python", "-m", "scraper.api.main", user, keyword_text], check=True)
            except subprocess.CalledProcessError as e:
                return HttpResponse(f"Error in scraping process: {e}", status=500)
        return redirect("mykeyword")
    
    user = str(request.user.id)
    keywords = get_all_keywords(user)
    return render(request, "keyword_app/my_keyword.html", {"keywords" : keywords})


@login_required
def update_keyword_view(request, keyword_text):
    if request.method == "POST":
        new_keyword = request.POST.get("new_keyword", "").strip()
        user = str(request.user.id)

        if new_keyword:
            # Update keyword
            update_keyword(user, keyword_text, new_keyword)
            
            # Delete all data related to old keyword from scrap_collection
            scrap_collection.delete_many({"user" : user, "keyword": keyword_text})

            # Do scrapping with new keyword
            try:
                subprocess.run(["python", "-m", "scraper.api.main", user, new_keyword], check=True)
            except subprocess.CalledProcessError as e:
                return HttpResponse(f"Error in scraping process: {e}", status=500)
            return redirect("mykeyword")
        else:
            return HttpResponseBadRequest("Invalid keyword")
    return HttpResponseBadRequest("Invalid request method")


@login_required
def delete_keyword_view(request, keyword_text):
    if request.method == "POST":
        user = str(request.user.id)

        delete_keyword(user, keyword_text)
        scrap_collection.delete_many({"user" : user, "keyword" : keyword_text})
        return redirect("mykeyword")
    return HttpResponseBadRequest("Invalid request method")

