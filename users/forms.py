from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form__input", 'placeholder': "Логин"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form__input", 'placeholder': "Пароль"
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form__input", 'placeholder': "Логин"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form__input", 'placeholder': "Email"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form__input", 'placeholder': "Пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form__input", 'placeholder': "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control", 'readonly':True
    }))
    user_city = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }))
    user_country = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }))
    about_user = forms.CharField(widget=forms.Textarea(attrs={
       'class':'form-control'
    }))

    class Meta:
        model = User
        fields = ('first_name','email','user_city','user_country', 'about_user')