from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.health_check, name='health_check'),
]
