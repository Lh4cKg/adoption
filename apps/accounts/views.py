from django.contrib.auth import login, authenticate
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, DetailView, FormView, UpdateView, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateProfile
from .models import UserModel
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import logout, login
from ..animals.models import Animals



class Profile(SingleObjectMixin):
    model = UserModel

    def get_object(self):
        try:
            return self.request.user.get_profile()
        except Profile.DoesNotExist:
            raise NotImplemented(" note implemented user")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password,)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_profile(request, nickname):
    template_name = "profile.html"

    user = UserModel.objects.get(nickname=nickname)
    animals = Animals.objects.filter(autor=user)
    context = {"user": user, "animals": animals}
    return render(request, template_name, context)


class UserList(ListView):
    def get_queryset(self):
        return UserModel.objects.all()


class ProfileDetail(DetailView):
    template_name = "accounts/profile.html"

    model = UserModel

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetail, self).get_context_data(*args, **kwargs)
        print(context)

        return context


class ProfileUpdate(SuccessMessageMixin, FormView, LoginRequiredMixin, UpdateView):
    template_name = "accounts/profile_update.html"
    model = UserModel
    succes_message = "Profile Updated!"
    form_class = UpdateProfile

    # fields = ["nickname", "first_name", "last_name"]

    def get_object(self, queryset=None):
        user = UserModel.objects.get(nickname=self.kwargs["nickname"])
        return user

    def get_success_url(self):
        # succes_url = "/accounts/<nickname>"
        return reverse_lazy("home")


class ProfileDetailView(DetailView):
    template_name = "accounts/profile.html"

    def get_object(self):
        nickname = self.kwargs.get("nickname")
        if nickname is None:
            raise Http404
        return get_object_or_404(UserModel, nickname__iexact=nickname, is_active=True)
