
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class LoginView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'login.html'
    success_url = reverse_lazy('chat_list')


class ProfileCreateView(generic.CreateView):
    model = Profile
    template_name = 'profile_create.html'
    success_url = reverse_lazy('chat:chat_list')
    fields = ('bio', 'location', 'avatar',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'
