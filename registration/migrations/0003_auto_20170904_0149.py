# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 01:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0002_gym_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='rated_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gym',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
