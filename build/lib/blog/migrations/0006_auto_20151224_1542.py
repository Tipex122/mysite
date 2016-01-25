# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='amount',
            field=models.DecimalField(blank=True, max_digits=10, verbose_name='Estimated budget', default=Decimal('0.00'), null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='priceAustria',
            field=models.DecimalField(blank=True, max_digits=10, verbose_name='Recomended Price', default=Decimal('0.00'), null=True, decimal_places=2),
        ),
    ]
