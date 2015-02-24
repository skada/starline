__author__ = 'jakubskaryd'

from django.conf.urls import patterns, include, url

from resources import views


urlpatterns = patterns('',
    url(r'^api/resource/(?P<pk>[0-9]+)/$', views.ResourceView.as_view()),
)
