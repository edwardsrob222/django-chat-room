
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class LoginView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('chat_list')


class ProfileCreateView(generic.CreateView):
    model = Profile
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('chat:chat_list')
    fields = ('bio', 'location', 'avatar',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def profile_detail(request):
    profile_list = Profile.objects.all()

    context = {
        'profile_list': profile_list,
    }

    return render(request, 'registration/profile_detail.html', context)

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile_detail.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
