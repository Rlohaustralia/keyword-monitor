from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views import generic

class aboutView(generic.TemplateView):
    template_name = "about.html"
    

    def get(self, request, *args, **kwargs):
        
        if request.GET.get('error') == '404':
            # 404 ERROR
            return JsonResponse({'message': 'Page not found.'}, status=404)
        elif request.GET.get('error') == '500':
            # 500 ERROR
            return JsonResponse({'message': 'Internal server error occurred.'}, status=500)
        else:
            # 200 SUCCESS
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)


# Create your views here.

class indexView(generic.TemplateView):
    template_name  = "index.html"

    def get(self, request, *args, **kwargs):
        
        if request.GET.get('error') == '404':
            # 404 ERROR
            return JsonResponse({'message': 'Page not found.'}, status=404)
        elif request.GET.get('error') == '500':
            # 500 ERROR
            return JsonResponse({'message': 'Internal server error occurred.'}, status=500)
        else:
            # 200 SUCCESS
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
    


class contactView(generic.TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        
        if request.GET.get('error') == '404':
            # 404 ERROR
            return JsonResponse({'message': 'Page not found.'}, status=404)
        elif request.GET.get('error') == '500':
            # 500 ERROR
            return JsonResponse({'message': 'Internal server error occurred.'}, status=500)
        else:
            # 200 SUCCESS
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
