from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Track
from django_tables2 import RequestConfig
import django_tables2 as tables
import operator
from django.db.models import Q
from django.core import serializers
from .tables import TrackTable

# Create your views here.
def index(request):
    template = loader.get_template('table.html')
    table = ClaimTable(Claim.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    context = {
        'lastest_record': table,
    }
    print("Requested Index")    
    return HttpResponse(template.render(context, request))
    
