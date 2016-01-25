# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151107_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, related_name='children', to='blog.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('stocks', models.IntegerField(default=0, blank=True)),
                ('priceAustria', models.DecimalField(verbose_name='Recomended Price', blank=True, decimal_places=2, null=True, max_digits=6, default=Decimal('0.00'))),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, to='blog.Category')),
            ],
        ),
    ]
