from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .models import *

# Create your views here.
'''
def main_page(request):
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)
'''

def main_page(request):
    return render_to_response(
    'main_page.html',
    { 'user': request.user}
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')

    return render_to_response(
        'user_page.html',
        {'username': user.username,
          'user' : request.user,
         'accounts': Accounts.objects.all()}
    )
'''
    banks = Banks.objects.all()
    template = get_template('user_page.html')
    variables = Context({
            'username': username,
            'banks': banks
            })
    output = template.render(variables)
    return HttpResponse(output)
'''

def transactions_page(request, num_of_account):
    try:
        account = Accounts.objects.get(num_of_account=num_of_account)
#        transactions = Transactions.objects.get(account)
    except:
        raise Http404('Requested account not found', num_of_account)
#TODO: Il faut pouvoir afficher les transactions dont le numéro de compte est remonté via l'adresse "transactions/num_de_compte
    return render_to_response(
        'transactions_page.html',
        {
          #  'transactions': Transactions.objects.filter(account.num_of_account = num_of_account),
#          'transactions': Transactions.objects.get(account.num_of_account),
          'transactions': Transactions.objects.all(),
          'account': account}
    )
