# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-29 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plotmap', '0005_auto_20180629_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='filename',
        ),
    ]
