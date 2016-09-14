from .models import Post, Comments
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
from django.shortcuts import get_object_or_404

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
            post.datatime = timezone.now()
            post.save()
            return HttpResponseRedirect('./')
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})

def post_detail(request, pk=1):
     return render(request, 'blog/post_detail.html', {'post':Post.objects.get(id=pk), 'comments': Comments.objects.filter(comments_post_id=pk)})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.datatime = timezone.now()
                post.save()
                return redirect('/blog', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_new.html', {'form': form})