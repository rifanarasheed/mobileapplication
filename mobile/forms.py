from django.forms import ModelForm
from mobile.models import Brands,Mobile,Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BrandCreateForm(ModelForm):
    class Meta:
        model = Brands
        fields = "__all__"

class MobileCreateform(ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class Userorder(ModelForm):
    # product = forms.CharField(max_length=120)
    class Meta:
        model = Order
        fields = ["product","address","user"]
        # widgets = {'product':forms.TextInput()}