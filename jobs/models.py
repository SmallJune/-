# -*- coding:utf-8 -*-
from django.db import models

# 公司名称 
class Company(models.Model):
    company = models.CharField(max_length=64, verbose_name=u'公司名称')
    address = models.CharField(max_length=64, null=True, verbose_name=u'公司地址')

    def __unicode__(self):
        return self.company

    class Meta:
        verbose_name_plural = u'公司名称'
        db_table = 'og_company'

# 入职机会页面
class Jobs(models.Model):
    JOBS_TYPE = (
        (1, u'社会招聘'),
        (2, u'校园招聘'),
    )

    GENDER = (
        ('G', u'不限'),
        ('M', u'男'),
        ('F', u'女'),
    ) 

    jobs_type = models.IntegerField(choices=JOBS_TYPE, default=1, max_length=1, verbose_name=u'招聘类型')
    jobs = models.CharField(max_length=64, verbose_name=u'职位')
    number = models.IntegerField(default=0, verbose_name=u'招聘人数')
    gender = models.CharField(choices=GENDER, max_length=1, default='G', verbose_name=u'性别')
    education = models.CharField(max_length=32, verbose_name=u'学历')
    workplace = models.CharField(max_length=32, verbose_name=u'工作地点')
    major = models.CharField(max_length=32, verbose_name=u'专业')
    description = models.TextField(verbose_name=u'职位描述')
    demand = models.TextField(verbose_name=u'任职资格')
    company = models.ForeignKey(Company, default=1, verbose_name=u'公司')


    def __unicode__(self):
        return self.jobs

    class Meta:
        verbose_name_plural = u'入职机会'
        db_table = 'og_jobs'

