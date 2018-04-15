from django.shortcuts import render
from django.template import loader
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



class Index(TemplateView):
	login_url = "/login/"
	redirect_field_name = '/about/'
	template_name ="index.html "

