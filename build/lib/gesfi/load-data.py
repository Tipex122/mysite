# Full path and name to your csv file
csv_filepathname = "/home/xavier/Programmation/djangogirls/mysite/csv/compta3.csv"
# Full path to your django project directory
your_djangoproject_home = "/home/xavier/Programmation/djangogirls/mysite/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

#from django.core.management import setup_environ
#import settings
#setup_environ(settings)


from gesfi.models import Transactions

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

for row in dataReader:
#    if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
    transactions = Transactions()

    ddmmyyyy = row[0]
    yyyymmdd = ddmmyyyy[6:] + "-" + ddmmyyyy[3:5] + "-" + ddmmyyyy[:2]
    transactions.date_of_transaction = yyyymmdd

    transactions.type_of_transaction = row[1]
    transactions.name_of_transaction = row[2]

    transactions.amount_of_transaction = row[3].replace(',','.')
    transactions.currency_of_transaction = row[4]
#    transactions.bank_of_account = "Toto"
    transactions.save()
