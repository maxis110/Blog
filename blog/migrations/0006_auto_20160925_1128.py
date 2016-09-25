# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160925_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post_likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user_likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='likes',
            table='likes',
        ),
    ]