from django.views import generic


# Create your views here.

class indexView(generic.TemplateView):
    template_name  = "index.html"

class aboutView(generic.TemplateView):
    template_name = "about.html"

class contactView(generic.TemplateView):
    template_name = "contact.html"