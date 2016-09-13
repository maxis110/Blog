from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.shortcuts import render, redirect
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    datatime = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class User(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)
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

