from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('operation.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)
