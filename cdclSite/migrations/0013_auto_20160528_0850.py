# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdclSite', '0012_auto_20160521_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
