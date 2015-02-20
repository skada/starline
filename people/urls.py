__author__ = 'skada'
from django.conf.urls import patterns, include, url
from django.contrib import admin

from people.views import KidCreate, KidUpdate

urlpatterns = patterns('',
    url(r'kid/add/$', KidCreate.as_view(), name='kid_add'),
    url(r'kid/(?P<pk>\d+)/$', KidUpdate.as_view(), name='kid_update'),
)