from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import RegisterUserForm


# Create your views here.
class Login(LoginView):
    template_name = "users/login/index.html"


class Logout(LogoutView):
    next_page = "/"


class Register(FormView):
    template_name = "users/register/index.html"
    form_class = RegisterUserForm
    success_url = "/users/login/"

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
