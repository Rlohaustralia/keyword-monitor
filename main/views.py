from django.shortcuts import render
from django.views import generic

# 사용자의 요청을 처리하는 로직을 작성하는 파일
# 여기서 데이터베이스에서 데이터를 가져오거나, 다른 로직을 수행한 후 사용자에게 응답을 반환

# Create your views here.

class indexView(generic.TemplateView):
    template_name  = "index.html"