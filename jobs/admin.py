# -*- coding:utf-8 -*-
from django.contrib import admin
from origingroup.jobs.models import Jobs, Company

class JobsAdmin(admin.ModelAdmin):
	list_display = ('id', 'jobs', 'number', 'gender', 'education', 'workplace', 'major', 'description', 'demand',)
	ordering = ('-id',)
	# 添加快速查询栏
	search_fields = ('jobs',)
	# 过滤器
	# list_filter = ('city',)
	radio_fields = {"company": admin.VERTICAL}
admin.site.register(Jobs, JobsAdmin)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'company',)
	ordering = ('-id',)
	# 添加快速查询栏
	search_fields = ('company',)
	# 过滤器
	# list_filter = ('city',)
admin.site.register(Company, CompanyAdmin)