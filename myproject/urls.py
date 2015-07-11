from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from myproject.views.views import ContentList, ContentDetail, DifficultyList, DifficultyDetail, CountryList, CountryDetail, CategoryTypeList, CategoryTypeDetail, CategoryList, CategoryDetail
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        #
                        url(r'^searchtable/', 'myproject.views.views.search_table'),
                        url(r'^signin/', 'myproject.views.signin_manager.signin_manager'),
                        url(r'^logout/', 'myproject.views.signin_manager.user_logout'),
                        url(r'^$', 'myproject.views.views.home', name='home'),
                        url(r'^contents/(?P<id>[0-9]+)',
                            'myproject.views.views.content_details'),
                        #forms
                        url(r'^adminforms/', 'myproject.views.form_manager.admin_forms'),
                        url(r'^contentform/', 'myproject.views.form_manager.content_manager'),
                        url(r'^categoryform/', 'myproject.views.form_manager.category_manager'),
                        url(r'^categorytypeform/', 'myproject.views.form_manager.category_type_manager'),
                        url(r'^countryform/', 'myproject.views.form_manager.country_manager'),
                        url(r'^difficultyform/', 'myproject.views.form_manager.difficulty_manager'),
                        #end forms
                        #rest links
                        url(r'^data/contents/$', ContentList.as_view()),
                        url(r'^data/contents/(?P<pk>[0-9]+)/$', ContentDetail.as_view()),
                        url(r'^data/difficulties/$', DifficultyList.as_view()),
                        url(r'^data/difficulties/(?P<pk>[0-9]+)/$', DifficultyDetail.as_view()),
                        url(r'^data/countries/$', CountryList.as_view()),
                        url(r'^data/countries/(?P<pk>[0-9]+)/$', CountryDetail.as_view()),
                        url(r'^data/categorytypes/$', CategoryTypeList.as_view()),
                        url(r'^data/categorytypes/(?P<pk>[0-9]+)/$', CategoryTypeDetail.as_view()),
                        url(r'^data/categories/$', CategoryList.as_view()),
                        url(r'^data/categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),
                        #end rest links
                        url(r'^(?P<category_type_slug>[\w-]+)/(?P<category_slug>[\w-]+)/$',
                            'myproject.views.views.content_list_by_category'),
                        )