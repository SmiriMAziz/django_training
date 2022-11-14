from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SigninForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.models import User


class Signin(TemplateView):
    initial = {'key': 'value'}
    form = SigninForm
    template_name = 'signin.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if (user is not None):
                login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                return HttpResponseRedirect('/artists')

            # return render(request, self.template_name, {'form': form})


class Logout(TemplateView):

    def get(self, request, *args, **kwargst):
        logout(request)
        return HttpResponseRedirect('/artists')
