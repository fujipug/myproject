from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from myproject.forms import SigninForm


def signin_manager(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                #messages.error(request, 'Incorrect username or password')
                return HttpResponseRedirect('/signin/')
    elif request.method == 'GET':
        form = SigninForm()
    else:
        return HttpResponseRedirect('/signin/')
    return render(request, "main/sign_in.html", {"form": form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')