# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='contact_no',
            field=models.IntegerField(default=9876543210),
            preserve_default=False,
        ),
    ]
