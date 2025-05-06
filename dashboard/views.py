from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required
def dashboard_view(request):
    return render(request, "dashboard_app/my_dashboard.html")