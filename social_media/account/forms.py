from django.contrib.auth.models import User
from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.validationError('passwords are not match')
        return cd['password2']


class UserEditForm(forms.Form):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email')


class ProfileEditForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')