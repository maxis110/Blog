# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_likes'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='likes',
            table='Likes',
        ),
    ]
