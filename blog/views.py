from .models import Post, Comments
from .form import PostForm, CommentForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .form import UsersCreationForm
from django.contrib.auth.models import User



class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/blog/"
    template_name = "blog/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

def registration(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
    else:
        args = {}
        args.update(request)
        args['form'] = UsersCreationForm()
    return render(request, 'blog/register.html', args)

@login_required
def comments_add(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comments = form.save(commit=False)
            comments.comments_post_id = post.id
            comments_date = timezone.now()
            comments.autors = request.user
            comments.save()
            return redirect('/blog/{}/'.format(pk), pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comments_add.html', {'form': form})

@login_required
def comments_remove(request, pk):
    comments = get_object_or_404(Comments, pk=pk)
    id = comments.id
    post_id = comments.comments_post_id
    comments.delete()
    return redirect('/blog/{}'.format(post_id))


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
     return render(request, 'blog/post_detail.html', {'post':Post.objects.get(id=pk),
                                                      'comments': Comments.objects.filter(comments_post_id=pk)})

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


