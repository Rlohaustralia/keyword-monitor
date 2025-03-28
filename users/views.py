from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# class registrationView(generic.CreateView):
#     template_name = "registration/register.html"
#     form_class = customizedUserCreationForm
#     def get_success_url(self):
#         return reverse("login")

class signUpView(generic.CreateView):
    template_name = "registration_app/signUp.html"
    form_class = SignUpForm
    success_url = '/signin'

class signInView(LoginView):
    template_name = "registration_app/signIn.html"
    success_url = '/'

class signOutView(LogoutView):
    next_page = '/'