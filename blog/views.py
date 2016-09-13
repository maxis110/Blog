from .models import Post
from django.views.generic import ListView, DetailView,View
from .form import PostForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

class UserView(View):
    model = User

#class RegisterFormView(FormView):
#    form_class = UserCreationForm
#    success_url = "/login/"
#    template_name = "blog/register.html"
#    def form_valid(self, form):
#        form.save()
#        return super(RegisterFormView, self).form_valid(form)


def user_new(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        return HttpResponseRedirect("./")
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', { 'form': form })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.PostListView', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
