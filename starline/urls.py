from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_filters.views import FilterView
# TODO: include urls from base
from planning.views import PlacementView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', PlacementView.as_view(), name='home'),
    url(r'^people/', include('people.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
