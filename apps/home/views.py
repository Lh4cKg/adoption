from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ..animals.models import Animals


class Index(TemplateView):
    login_url = "/login/"
<<<<<<< HEAD
=======
    redirect_field_name = '/about/'
>>>>>>> ea296892d6d5536b4b897083c96961efaac78d96
    template_name = "index.html"


class Home(LoginRequiredMixin, ListView):
    template_name = "home.html"
    queryset = Animals.objects.all()
