from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
#from django.core.context_processors import csrf
from accounts.forms import (LoginForm, RegisterForm)

# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    form = LoginForm()
    regFrom = RegisterForm()

    args = {
        'form': form,
        'reg' : regFrom,
    }
    return render(request, "login.html", args)

def auth_user(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")  # Redirect to a success page.
    regFrom = RegisterForm()
    args = {
        'form': form,
        'reg': regFrom,
    }
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def register(request):
    reg = RegisterForm(request.POST)
    if request.POST and reg.is_valid():
        reg.save()
        return HttpResponseRedirect("/")
    form = LoginForm()
    args = {
        'form': form,
        'reg': reg,
    }
    return render(request, 'login.html', args)