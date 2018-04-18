from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ..animals.models import Animals


class Index(TemplateView):
    login_url = "/login/"
    template_name = "index.html"


class Home(LoginRequiredMixin, ListView):
    template_name = "animals/home.html"
    queryset = Animals.objects.all()
