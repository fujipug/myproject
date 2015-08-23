from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from myproject.models import Content, Difficulty, Country, CategoryType, Category
from django import forms
from myproject.forms import ContentForm, DifficultyForm, CountryForm, CategoryTypeForm, CategoryForm, SigninForm
from django.core import serializers
from myproject.serializers import ContentSerializer, DifficultySerializer, CountrySerializer, CategoryTypeSerializer, CategorySerializer
from rest_framework import filters
from rest_framework import generics

#Serializer Stuff
class ContentList(generics.ListCreateAPIView):
    model = Content
    serializer_class = ContentSerializer
    def string_contains_substring(self, string, substring):
        if substring is not None:
            if substring in string:
                return True
            else:
                return False
        return True

    def any_element_in_both_lists(self, first, second):
        if len(first) == 0 or len(second) == 0:
            return False
        for element in first:
            if element in second:
                return True
        return False

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a 'title' query parameter in the URL.
        """
        queryset = []

        
        # url variables
        first_name_substring= self.request.query_params.get('first_name', "").decode('utf8')
        last_name_substring = self.request.query_params.get('last_name', "").decode('utf8')
        difficulty_substring = self.request.query_params.get('difficulty', "").decode('utf8')
        country_substring = self.request.query_params.get('country', "").decode('utf8')
        title_substring = self.request.query_params.get('title', "")
        category_substring_list = self.request.query_params.get('categories', "")

        #get categories based off category substring list
        category_filters = []
        if category_substring_list:
            category_substrings = category_substring_list.split(',')#[x for x in category_substring_list.split(',')]
            categories = Category.objects.all()
            for category in categories:
                for category_substring in category_substrings:
                    if self.string_contains_substring(category.slug, category_substring):
                        category_filters.append(category)
                        break

        order_by = self.request.query_params.get('order_by', '')
        if order_by:
            contents = Content.objects.all().order_by(order_by)
        else:
            contents = Content.objects.all()

        #filter
        for content in contents:
            if not self.string_contains_substring(slugify(content.first_name), first_name_substring):
                continue
            if not self.string_contains_substring(content.last_name, last_name_substring):
                continue
            if not self.string_contains_substring(content.country.slug, country_substring):
                continue
            if not self.string_contains_substring(content.difficulty.slug, difficulty_substring):
                continue
            if not self.string_contains_substring(content.title, title_substring):
                continue
            if category_substring_list and not self.any_element_in_both_lists(category_filters, content.categories.all()):
                continue
            queryset.append(content)

        return queryset


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class DifficultyList(generics.ListCreateAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class DifficultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CategoryTypeList(generics.ListCreateAPIView):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class CategoryTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a 'category_type' query parameter in the URL.
            """
            queryset = Category.objects.all()
            category_type_id = self.request.query_params.get('category_type', None)
            if category_type_id is not None:
                #category_type = CategoryType.objects.get(slug = category_type_slug)
                queryset = queryset.filter(category_type=category_type_id)
            return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#End Serializer Stuff.


def home(request):
    contents = Content.objects.all().order_by('-id')[:5]
    return render(request, "main/home.html", {'categories': Category.objects.all, 'category_types': CategoryType.objects.all, 'contents': contents})


def content_details(request, id):
    content = Content.objects.get(id = id)
    return render(request, "main/content_details.html", {'content': content})


def content_list_by_category(request, category_type_slug, category_slug):
    if category_type_slug == 'difficulty':
        category_type = "Difficulty"
        category = Difficulty.objects.get(slug = category_slug)
        contents = Content.objects.filter(difficulty = category)
    elif category_type_slug == 'country':
        category_type = "Country"
        category = Country.objects.get(slug = category_slug)
        contents = Content.objects.filter(country = category)
    else:
        category_type = CategoryType.objects.get(slug=category_type_slug)
        category = Category.objects.get(slug = category_slug)
        contents = Content.objects.filter(categories=category)
    return render(request, "main/content_list_by_category.html", 
        {'category': category, 'category_type': category_type,'contents': contents})


def search_table(request):
    first_name_substring = request.GET.get('first_name', None)
    #last_name_substring = self.request.query_params.get('last_name', None)
    #difficulty_slug_substring = self.request.query_params.get('difficulty', None)
    #country_slug_substring = self.request.query_params.get('country', '')
    #title_substring = self.request.query_params.get('title', '')
    #category_slug_substring_list = self.request.query_params.get('categories', '')

    contents = Content.objects.all()
    return render(request, "main/search_table.html", {'contents': contents, 'first_name': first_name_substring})