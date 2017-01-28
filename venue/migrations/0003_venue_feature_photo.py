# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0002_auto_20161004_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='feature_photo',
            field=models.ImageField(default=b'radisson.jpg', upload_to=b'media/feature/%Y/%D/%M'),
        ),
    ]
