from django.conf.urls import patterns, include, url
from django.contrib import admin
from operation.controllers import auth, inframe
import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', auth.login, name='login'),
    url(r'^login/$', auth.login, name='login'),
    url(r'^index/$', auth.index, name='index'),
    url(r'^regist/$', auth.regist, name='regist'),
    url(r'^logout/$', auth.logout, name='logout'),   
    url(r'^topbar/$', inframe.topbar, name='topbar'),   
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)
