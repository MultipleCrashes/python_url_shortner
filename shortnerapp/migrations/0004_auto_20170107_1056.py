# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortnerapp', '0003_auto_20170107_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmapper',
            name='long_url',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='urlmapper',
            name='short_url',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
