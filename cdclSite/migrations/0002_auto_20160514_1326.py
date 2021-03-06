# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-14 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdclSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contactName', models.CharField(max_length=50)),
                ('contactNumber', models.CharField(max_length=20)),
                ('contactEmail', models.CharField(max_length=50)),
                ('clubWebsite', models.CharField(default='', max_length=100)),
                ('clubNight', models.DateTimeField()),
                ('clubVenue', models.CharField(max_length=50)),
                ('clubAddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forenames', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('ecfCode', models.CharField(max_length=8)),
                ('rating', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdclSite.Club')),
            ],
        ),
        migrations.AddField(
            model_name='userdata',
            name='isTreasurer',
            field=models.BooleanField(default=False),
        ),
    ]
