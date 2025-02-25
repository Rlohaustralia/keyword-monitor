from django.shortcuts import render, redirect
from .models import keyword_collection, add_keyword, get_all_keywords, update_keyword, delete_keyword
from django.http import HttpResponse, request
from django.contrib import messages
from django.http import HttpResponseBadRequest


# Create your views here.

def keyword_view(request):
    if request.method == "POST":
        keyword_text = request.POST.get("keyword","").strip()

        # Not allow duplicated keyword
        if keyword_collection.find_one({"keyword": keyword_text}):
            return redirect('mykeyword')
        
        if keyword_text:
            add_keyword(keyword_text)
        return redirect("mykeyword")
    
    keywords = get_all_keywords()
    return render(request, "keyword_app/my_keyword.html", {"keywords" : keywords})


def update_keyword_view(request, keyword_text):
    if request.method == "POST":
        new_keyword = request.POST.get("new_keyword", "").strip()
        if new_keyword:
            update_keyword(keyword_text, new_keyword)
            return redirect("mykeyword")
        else:
            return HttpResponseBadRequest("Invalid keyword")
    return HttpResponseBadRequest("Invalid request method")


def delete_keyword_view(request, keyword_text):
    if request.method == "POST":
        delete_keyword(keyword_text)
        return redirect("mykeyword")
    return HttpResponseBadRequest("Invalid request method")
