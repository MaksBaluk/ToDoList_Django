from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import *


# Create your views here.


class HomeTemplate(TemplateView):
    template_name = 'ToDoList/home.html'

    def get_queryset(self):
        return CustomUser.objects.values('slug')


class UserLogin(LoginView):
    template_name = 'ToDoList/login_view.html'
    authentication_form = CustomUserLoginForm

    def get_success_url(self):
        return reverse_lazy('main')


class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'ToDoList/reqister_view.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class UserLogout(LoginRequiredMixin, LogoutView):
    redirect_field_name = 'main'
