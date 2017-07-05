

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.first_page, name='first_page'),
    url(r'^dna/(?P<pk>\d+)/final/$', views.final, name='final'),
    url(r'^dna/instructions/$', views.instructions, name='instructions'),
    url(r'^dna/how/$', views.how, name='how'),
]