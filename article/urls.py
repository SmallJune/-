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
    #测试数据get
    url(r'^ajax/get/test/$', 'api.get_test'),
    #post
    url(r'^ajax/post/test$', 'api.post_test'),
    #json
    url(r'^ajax/json/test$', 'api.json_test'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
