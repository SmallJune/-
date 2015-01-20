# -*-coding:utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('origingroup.article',
    # Examples:
    url(r'^$', 'api.home'),
    url(r'^(?P<article_type>\d+)/(?P<sub_type>\w+)/$', 'api.home'),
    url(r'^(?P<article_type>\d+)/(?P<sub_type>\w+)/(?P<page>\d+)/$', 'api.home'),
    url(r'^info/(?P<article_id>\d+)/$', 'api.article_info'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
