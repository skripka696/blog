from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView, View
from user_profile import forms


class Login(FormView):
    form_class = forms.UserLoginForm
    success_url = '/home/'
    template_name = 'user_profile/login.html'
    #
    # def form_valid(self, form):
    #     user = form.get_user()
    #     return super(Login, self).form_valid()


class Registration(FormView):
    form_class = forms.UserRegistrForm
    success_url = '/home/'
    template_name = 'user_profile/registration.html'


class LogOut(View):
    success_url = '/regist/'
    template_name = 'notes/base.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')