# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0003_venue_feature_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=b'photos/%Y/%D/%M'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='feature_photo',
            field=models.ImageField(default=b'radisson.jpg', upload_to=b'media/featured/%Y/%D/%M'),
        ),
    ]
