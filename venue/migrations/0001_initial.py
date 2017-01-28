# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('image', models.ImageField(upload_to=b'media/%Y%M%D')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=5, choices=[(b'HOT', b'HOTEL'), (b'REST', b'RESTAURANT'), (b'RES', b'RESORT'), (b'SPCS', b'SPORTS CENTER'), (b'ACAD', b'ACADEMIC CENTER')])),
                ('description', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('facilities', models.ManyToManyField(related_name='venue_facility', to='venue.Facility')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='venue',
            field=models.ForeignKey(related_name='venue_photo', to='venue.Venue'),
        ),
    ]
