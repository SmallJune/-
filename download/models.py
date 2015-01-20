# -*- coding:utf-8 -*-
from django.db import models

#下载中心页面
class Download(models.Model):
    upload_dir = 'files'
    FILE_TYPE = (
        (1, u'集团手册'), 
        (2, u'室内手册'),
        (3, u'项目物料'),
    )
    file_type = models.IntegerField(choices=FILE_TYPE, max_length=1, verbose_name=u'附件内容')
    file_name = models.CharField(max_length=200, verbose_name=u'文件名')
    url = models.FileField(max_length=200, upload_to=upload_dir, verbose_name=u'文件地址')

    class Meta:
        verbose_name_plural = u'下载中心'
        db_table = 'og_download_file'

    def __unicode__(self):
        return self.file_name

    def save(self):
        super(Download, self).save()
        self.url = "/static/upload/%s" %(self.url)
        super(Download, self).save()

