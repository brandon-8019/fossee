# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-15 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotmap', '0002_auto_20180615_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlfile',
            name='fileobject',
            field=models.FileField(null=True, upload_to='temp_files'),
        ),
    ]
