from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ..animals.models import Animals


class Index(TemplateView):
    login_url = "/login/"
<<<<<<< HEAD
    redirect_field_name = '/about/'
=======
>>>>>>> 7ee03d8301d5bb5a548113273c33f6bd5829feaf
    template_name = "index.html"


class Home(LoginRequiredMixin, ListView):
    template_name = "animals/home.html"
    queryset = Animals.objects.all()
