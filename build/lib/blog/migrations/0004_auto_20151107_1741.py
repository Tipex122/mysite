# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_genre_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='budget',
            field=models.FloatField(),
        ),
    ]
