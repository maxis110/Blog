from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    class Meta():
        db_table = 'posts'

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    datatime = models.DateTimeField(default=timezone.now)
    autor = models.TextField(User)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/{}/" .format(self.id)

class User(AbstractBaseUser):

    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('email address', unique=True, db_index=True)
    password = models.CharField(max_length=128, default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.email

    USERNAME_FIELD = 'email'

class Comments(models.Model):

    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(max_length=10000)
    comments_post = models.ForeignKey(Post, related_name='comments')
