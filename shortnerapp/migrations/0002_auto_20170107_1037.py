# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortnerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmapper',
            name='long_url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='urlmapper',
            name='short_url',
            field=models.CharField(max_length=1000),
        ),
    ]
