from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime

# Create your views here.
from .models import Genre


def index(request):
    return render(request, 'blog/index.html', {})


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def show_genres(request):
    #    return render_to_response("genres.html",
    #                          {'nodes':Genre.objects.all()},
    #                          context_instance=RequestContext(request))
    return render(request, "blog/genres.html",
                  {'nodes': Genre.objects.all()}, )


#from django.template.loader import get_template
#from django.template import Context

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'blog/current_datetime.html', {'current_date': now})

##def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)
#    return render(request, html)
##    now = datetime.datetime.now()
##    t = get_template('current_datetime.html')
##    html = t.render(Context({'current_date': now}))
##    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False #TODO: Pour mémo ==> Utiliser "assert False" pour interrompre l'appli et afficher une page de debuggage
#    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#    return HttpResponse(html)
    return render(request, 'blog/hours_ahead.html',{'hour_offset': offset, 'next_time': dt})


#Pour afficher les META info liées à request
def display_meta(request):
    values = request.META.items()
#       values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

##########################################################################################"

from django.views.generic.list import ListView
import datetime
from .models import Category, Product
#from .forms import CategoryForm

class CategoryListView(ListView):
    template_name = 'category_list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        ##TODO créer la category_form
        #context['category_form'] = CategoryForm()
        context['products'] = Product.objects.all()
        return context

#################################### Lecture de fichier CSV ######################################################
import csv
from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="00056149140.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response