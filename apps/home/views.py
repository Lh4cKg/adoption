from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ..animals.models import Animals


class Index(TemplateView):
    login_url = "/login/"
    redirect_field_name = '/about/'
    template_name = "temp/index.html"


class Home(LoginRequiredMixin, ListView):
    template_name = "home.html"
    queryset = Animals.objects.all()