# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesfi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accout',
            new_name='Account',
        ),
    ]
