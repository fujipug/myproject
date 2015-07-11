from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myproject.models import Content, Difficulty, Country, Category, CategoryType


#class UserForm(UserCreationForm):
#    model = User
#    fields = ['username', 'password']
#
#
#class MyUserForm(forms.ModelForm):
#    class Meta:
#        model = MyUser
#        fields = ['email', 'name', 'city', 'state', 'birth', 'zipcode']
#
#
#class SignInForm(forms.Form):
#    username = forms.CharField(label='Username', max_length=30)
#    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)


class ContentForm(forms.ModelForm):
    
    class Meta:
        model = Content
        fields = ['first_name', 'last_name', 'title', 'description', 'vocab', 'video']


class DifficultyForm(forms.ModelForm):
    
    class Meta:
        model = Difficulty
        fields = ['difficulty']


class CountryForm(forms.ModelForm):
    
    class Meta:
        model = Country
        fields = ['country']


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category', 'category_type']


class CategoryTypeForm(forms.ModelForm):
    
    class Meta:
        model = CategoryType
        fields = ['category_type']
        exclude = ['slug']


class SigninForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())