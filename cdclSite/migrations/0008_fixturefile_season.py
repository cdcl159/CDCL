# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdclSite', '0007_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixtureFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixtureFile', models.FileField(upload_to='.')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
