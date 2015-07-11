from django.contrib import admin
from myproject.models import Content, CategoryType, Category, Country, Difficulty


admin.site.register(Content)
admin.site.register(CategoryType)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Difficulty)