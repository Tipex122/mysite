# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesfi', '0002_auto_20151230_1838'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Accounts',
        ),
    ]
