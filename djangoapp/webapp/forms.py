from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("This username is taken")
        return self.cleaned_data['username']

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("your passwords do not match")


class ProfilePictureForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_photo']
