# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('timestamp', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='events')),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('facebook', models.URLField(default='https://www.facebook.com/')),
                ('linkedin', models.URLField(default='https://www.linkedin.com/')),
                ('profile_pic', models.ImageField(upload_to='speakers')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('about', models.TextField()),
                ('facebook', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='speakers')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='sponsors')),
            ],
        ),
    ]
