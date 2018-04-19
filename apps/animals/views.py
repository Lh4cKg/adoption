from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.generic import (View, ListView, DetailView, UpdateView, DeleteView, TemplateView, CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AnimalCreateForm
from .models import Animals, Comment
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm
from ..accounts.models import UserModel
from django.contrib import messages

User = get_user_model()


def add_comment_to_post(request, slug):
    template_name = "comment.html"
    post = get_object_or_404(Animals, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.autor = request.user
            comment.save()
            messages.success(request, 'Comment succesufuly added!')
            return redirect("/home/")
    else:
        form = CommentForm()
    return render(request, template_name, {'form': form})


class AnimalCreateView(SuccessMessageMixin, FormView, LoginRequiredMixin, CreateView):
    form_class = AnimalCreateForm
    template_name = 'animals/form.html'
    success_message = 'You succesufuly added animal for adoption!'
    model = Animals

    # def get_succes_message(self, cleaned_data):
    #     print(cleaned_data)
    #     return ("You added animal succesufuly!")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.autor = self.request.user
        return super(AnimalCreateView, self).form_valid(form)

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.user = self.request.user
    #     return super(AnimalCreateView, self).form_valid(form)


class AnimalListView(LoginRequiredMixin, ListView):
    template_name = "animals/animal_list.html"

    def get_queryset(self):
        return Animals.objects.all()


class MyAnimalsListView(LoginRequiredMixin, ListView):
    context_object_name = "animal_list"
    template_name = "animals/my_animal_list.html"

    # queryset = Animals.objects.filter(autor = request.User)
    def get_queryset(self):
        return Animals.objects.filter(autor=self.request.user)


class AnimalDetailView(LoginRequiredMixin, DetailView):
    template_name = "animals/animals_detail.html"
    model = Animals

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['object'] = UserModel.objects.all(nickname = nickname)
        return context


class AnimalUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = AnimalCreateForm
    login_url = '/accounts/login/'
    template_name = 'animals/animals_update.html'
    success_message = 'You succesufuly updated your pet!'
    success_url = "/animals/mylist/"

    # success_url = "/restaurants/"

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update animal: {name}'
        return context

    def get_queryset(self):
        return Animals.objects.filter(autor=self.request.user)


class AnimalDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "animals/author_check_delete.html"
    model = Animals
    success_message = "You succesufuly removed animal"
    success_url = reverse_lazy("animals:list_animals")
