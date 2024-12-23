from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-group'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-group'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-group'}))
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={'class': 'form-group'}))
    password1 = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-group'}))
    password2 = forms.CharField(label="Повторите пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-group'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ChangePasswordUserForm(PasswordResetForm):
    old_password = forms.CharField(label="Старый Пароль",
                                widget=forms.PasswordInput(attrs={'class': 'password-reset-container'}))
    new_password1 = forms.CharField(label="Пароль",
                                widget=forms.PasswordInput(attrs={'class': 'password-reset-container'}))
    new_password2 = forms.CharField(label="Повторите пароль",
                                widget=forms.PasswordInput(attrs={'class': 'password-reset-container'}))


class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=100, required=False, label="Город вылета")

