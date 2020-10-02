from django.forms import TextInput

from .models import Task  # , Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class ProfileForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ('url', 'location', 'company')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']  # , 'date', 'likes']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            'task': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Основоной текст'
            }),
        }
