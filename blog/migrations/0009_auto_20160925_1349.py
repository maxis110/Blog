# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160925_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post_likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.Post'),
        ),
    ]