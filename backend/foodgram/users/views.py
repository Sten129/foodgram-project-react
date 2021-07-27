from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    # template_name = "signup.html"

def profile(request, username):
    pass

def my_profile(request, username):
    pass
# Create your views here.
