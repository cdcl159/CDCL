# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdclSite', '0010_auto_20160521_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='startDate',
        ),
        migrations.AddField(
            model_name='season',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
