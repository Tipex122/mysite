from django.db import models
from decimal import Decimal
# Create your models here.

import datetime


class Banks(models.Model):
    pass


class Accounts(models.Model):
    pass


class Transactions(models.Model):
    date_of_transaction = models.DateField('Date de la transaction', default = datetime.datetime.now)
    type_of_transaction = models.CharField('Type de transaction', max_length=64)
    name_of_transaction = models.CharField('Libellé de la transaction', max_length=256)
    amount_of_transaction = models.DecimalField(max_digits = 12, decimal_places = 2, default = Decimal('0.00'), verbose_name = "Montant de la transaction ", blank=True, null=True)
    currency_of_transaction = models.CharField('Devise',max_length=3)
    bank_of_account = models.CharField('Compte de la transaction',default= "Toto", max_length=25)
    create_date = models.DateField('Date de saisie', default = datetime.datetime.now)
    #TODO vérifier TreeForeignKey
    bank = models.ForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return "[%s] -- %s ===>  %s" % (self.date_of_transaction, self.name_of_transaction, self.amount_of_transaction, )

    class Meta:
        ordering = ['date_of_transaction']
