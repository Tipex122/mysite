# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='budget',
            field=models.FloatField(verbose_name='100.00', default=100.0),
            preserve_default=False,
        ),
    ]
