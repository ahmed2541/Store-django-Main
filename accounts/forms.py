
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,ProfileEdit

class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country','location','phone_number','image']
        

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         excude = ('username',)
        