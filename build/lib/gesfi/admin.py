from django.contrib import admin

# Register your models here.
from .models import Banks
from .models import Accounts
from .models import Transactions

admin.site.register(Banks)
admin.site.register(Accounts)
# admin.site.register(Transactions)

class TransactionsAdmin(admin.ModelAdmin):
#    fields = ['name', 'parent_name', 'budget', 'date_of_budget']
    fieldsets = [
        (None, {'fields': ['date_of_transaction','name_of_transaction']}),
        ('Info Genre', {'fields': ['amount_of_transaction','currency_of_transaction', 'bank_of_account','create_date','bank']}),
        ]

    list_display = ('date_of_transaction', 'name_of_transaction', 'amount_of_transaction','currency_of_transaction')
#    list_filter = ['parent_name', 'type', 'level']
    search_fields = ['name_of_transaction', 'amount_of_transaction']

admin.site.register(Transactions, TransactionsAdmin)