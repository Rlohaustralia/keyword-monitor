from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from dashboard.services.keyword_content_counts_analysis import *
from dashboard.utils.charts import generate_pie_chart



@login_required
def dashboard_view(request):
    
    user = str(request.user.id)
    keyword_counts = get_keyword_counts_by_user(user)

    labels = list(keyword_counts.keys())
    values = list(keyword_counts.values())
    pie_chart = generate_pie_chart(labels, values)

    return render(request, "dashboard_app/my_dashboard.html", {'pie_chart': pie_chart})