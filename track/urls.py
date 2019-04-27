from django.urls import path
from django.conf.urls import url


from . import views
from .models import Claim

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    url(r'^claim/([^/]+)/$', views.note, name='note'),
    url(r'^bill/([0-9]+)/$', views.bill, name='bill'),
    url(r'^note/([0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    #url(r'search/', views.search, name='search'),
    url('get_table', views.get_table, name='get_table'),

]