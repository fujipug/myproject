from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from myproject.models import Content, Difficulty, Country, CategoryType, Category
from django import forms
from myproject.forms import ContentForm, DifficultyForm, CountryForm, CategoryTypeForm, CategoryForm


def admin_forms(request):
    return render(request, "main/admin_forms.html", {})       


def category_manager(request):
    if request.user.is_authenticated():
        categories = Category.objects.all()
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                #messages.success(request, 'Your changes have been saved.')
                edited_data = form.save()
                return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        elif request.method == 'GET':
            form = CategoryForm()
        else:
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        return render(request, 'main/category_form.html', { 'form': form, 'categories': categories })
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))


def category_type_manager(request):
    if request.user.is_authenticated():
        ctypes = CategoryType.objects.all()
        if request.method == 'POST':
            form = CategoryTypeForm(request.POST)
            if form.is_valid():
                #messages.success(request, 'Your changes have been saved.')
                edited_data = form.save()
                return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        elif request.method == 'GET':
            form = CategoryTypeForm()
        else:
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        return render(request, 'main/category_type_form.html', { 'form': form, 'ctypes': ctypes })
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))


def content_manager(request):
    if request.user.is_authenticated():
        contents = Content.objects.all()
        if request.method == 'POST':
            form = ContentForm(request.POST)
            if form.is_valid():
                #messages.success(request, 'Your changes have been saved.')
                edited_data = form.save()
                return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        elif request.method == 'GET':
            form = ContentForm()
        else:
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        return render(request, 'main/content_form.html', { 'form': form, 'contents': contents })
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))


def difficulty_manager(request):
    if request.user.is_authenticated():
        difficulties = Difficulty.objects.all()
        if request.method == 'POST':
            form = DifficultyForm(request.POST)
            if form.is_valid():
                #messages.success(request, 'Your changes have been saved.')
                edited_data = form.save()
                return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        elif request.method == 'GET':
            form = DifficultyForm()
        else:
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        return render(request, 'main/difficulty_form.html', { 'form': form, 'difficulties': difficulties })
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))


def country_manager(request):
    if request.user.is_authenticated():
        countries = Country.objects.all()
        if request.method == 'POST':
            form = CountryForm(request.POST)
            if form.is_valid():
                #messages.success(request, 'Your changes have been saved.')
                edited_data = form.save()
                return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        elif request.method == 'GET':
            form = CountryForm()
        else:
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
        return render(request, 'main/country_form.html', { 'form': form, 'countries': countries })
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))