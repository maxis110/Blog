from django import forms
from .models import Post, User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')