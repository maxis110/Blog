from django import forms
from .models import Post, User, Comments
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)

class UsersCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comments_text',)