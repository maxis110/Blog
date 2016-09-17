from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    datatime = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/{}/" .format(self.id)

    class Meta:
        db_table = 'post'


class Comments(models.Model):

    comments_text = models.TextField(max_length=10000)
    comments_date = models.DateTimeField(default=timezone.now)
    comments_post = models.ForeignKey(Post, related_name='comments')
    autors = models.ForeignKey(User, related_name='autor')

    class Meta:
            db_table = 'comments'