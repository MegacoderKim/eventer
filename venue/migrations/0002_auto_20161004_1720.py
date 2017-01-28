# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name': 'facility', 'verbose_name_plural': 'facilities'},
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='type',
            new_name='eventype',
        ),
        migrations.AddField(
            model_name='photo',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=b'media/%Y/%D/%M'),
        ),
    ]
