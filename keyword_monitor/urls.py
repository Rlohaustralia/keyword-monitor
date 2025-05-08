"""
URL configuration for keyword_monitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from users.views import *
from keywords.views import *
from scraper.views import *
from dashboard.views import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main
    path('', indexView.as_view(), name='index'),
    path('about/', aboutView.as_view(), name='about'),
    path('contact/', contactView.as_view(), name='contact'),
    path('signup/', signUpView.as_view(), name='signup'),
    path('signin/', signInView.as_view(), name='signin'),
    path('signout/',signOutView.as_view(), name='signout'),

    # Keyword
    path('my_keyword/', keyword_view, name='mykeyword'),
    path('my_keyword/delete/<str:keyword_text>/', delete_keyword_view, name='delete_keyword'),
    path('my_keyword/update/<str:keyword_text>/', update_keyword_view, name='update_keyword'),
    
    # Scraper
    path('live_monitor/', live_monitor_view, name='live_monitor'),
    path('download/', export_to_excel_view, name='export_excel'),
    path('refresh_data/', refresh_data_view, name='refresh_data'),

    # Dashboard
    path('dashboard/', dashboard_view, name='dashboard'),

    # Postman API (For TEST only)
    path('api/reference_keyword/', add_reference_keywords, name='add_reference_keywords')
]
