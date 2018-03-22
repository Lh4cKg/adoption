from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import( View, ListView, DetailView, UpdateView, DeleteView, TemplateView, CreateView) 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  AnimalCreateForm
from .models import Animals
from django.urls import reverse_lazy
from django.db.models import Q



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
    # success_url= "/animal/update/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(AnimalCreateView, self).form_valid(form)


# class AnimalListView(LoginRequiredMixin, ListView):
#     template_name=" animal_list.html"
#     def get_queryset(self):
#         # original qs
#         qs = Animal.objects.all()


def animals_listview(request):
    template_name= "animal_list.html"
    queryset = Animals.objects.all()
    context = {"object_list": queryset
    }
    return render(request, template_name, context)

class AnimalListView(LoginRequiredMixin, ListView):
    template_name= "animal_list.html"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Animals.objects.filter(
                Q(category__contains=slug)
                )

        else:
            queryset = Animals.objects.none()
        return slug


class AnimalDetailView(LoginRequiredMixin, DetailView):
    template_name= "animals_detail.html"

    queryset = Animals.objects.all()

    def get_context_data(self, *args, **kwargs):
        context=super(AnimalDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    









# class AnimalUpdateView(LoginRequiredMixin, UpdateView):
#     model = Animals
#     fields =[
#         "category", 
#         "name", 
#         "age",
#         "gender",
#         "description",
#         "photo",
#         ]

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animals
    success_url = reverse_lazy("mysite:home")