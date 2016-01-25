# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gesfi', '0003_auto_20151230_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount_of_transaction',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Montant de la transaction ', null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='bank_of_account',
            field=models.CharField(max_length=25, verbose_name='Compte de la transaction', default='Toto'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='create_date',
            field=models.DateField(verbose_name='Date de saisie', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='currency_of_transaction',
            field=models.CharField(max_length=3, verbose_name='Devise'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date_of_transaction',
            field=models.DateField(verbose_name='Date de la transaction', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='name_of_transaction',
            field=models.CharField(max_length=256, verbose_name='Libellé de la transaction'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='type_of_transaction',
            field=models.CharField(max_length=64, verbose_name='Type de transaction'),
        ),
    ]
