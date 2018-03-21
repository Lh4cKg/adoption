from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AnimalCreateForm, AnimalCreate



class Index(TemplateView):
	login_url = "/login/"
	redirect_field_name = '/about/'
	template_name ="index.html "
	

class Home(LoginRequiredMixin, TemplateView):
	template_name= "home.html"


class AnimalCreateView(LoginRequiredMixin, CreateView):
    form_class = AnimalCreateForm
    login_url = '/login/'
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)