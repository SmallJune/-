# -*-coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# admin.autodiscover()

urlpatterns = patterns('origingroup',
    # Examples:
    url(r'^$', 'views.cover'),
    url(r'^example', 'views.example'),
    url(r'^datatable', 'views.index'),
    url(r'^index/', 'views.home'),
    url(r'^waterfall/', 'article.view.waterfall'),
    url(r'^article/', include('origingroup.article.urls')),		#作品
    url(r'^jobs/', include('origingroup.jobs.urls')),			#工作
    url(r'^download/', include('origingroup.download.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include('grappelli.urls')),                  #后台
    url(r'^admin/', include(admin.site.urls)),					#后台
)
