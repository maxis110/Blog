from django import forms
from .models import Post, User, Comments
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)

#class UsersCreationForm(forms.ModelForm):

 #   class Meta:
  #      model = User
   #     fields = ('username', 'email', 'password')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comments_text',)