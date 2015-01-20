# -*- coding:utf-8 -*-
from django.contrib import admin
from origingroup.download.models import Download

class DownloadAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'file_type', 'url')
    ordering = ('id',)
    # 添加快速查询栏
    search_fields = ('file_name',)
    # 过滤器
    # list_filter = ('city',)
admin.site.register(Download, DownloadAdmin)

