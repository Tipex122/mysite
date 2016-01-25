# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accout',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_of_transaction', models.DateTimeField(default=datetime.datetime.now)),
                ('type_of_transaction', models.CharField(max_length=64, verbose_name='Cash')),
                ('name_of_transaction', models.CharField(max_length=256, verbose_name='Transaction designation')),
                ('amount_of_transaction', models.DecimalField(max_digits=10, null=True, default=Decimal('0.00'), decimal_places=2, blank=True, verbose_name='Amount of the transaction')),
                ('currency_of_transaction', models.CharField(max_length=3, verbose_name='EUR')),
                ('bank_of_account', models.CharField(max_length=25, default='Toto')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('bank', models.ForeignKey(null=True, blank=True, related_name='children', to='gesfi.Transactions')),
            ],
            options={
                'ordering': ['date_of_transaction'],
            },
        ),
    ]
