# -*- coding:utf-8 -*-
from __future__ import division
from origingroup.settings import ROOT
from django.db import models
import os
import time
from PIL import Image


#作品页面
class ArticleType(models.Model):
    article_type = models.CharField(max_length=32, null=True, verbose_name=u'作品分类')

    def __unicode__(self):
        return self.article_type

    class Meta:
        verbose_name_plural = u'作品类目'
        db_table = 'og_article_type'

#作品页面
class Article(models.Model):
    article_templates = (
        ('article_list', u'列表的形式'),
        ('article_loop', u'一张图片一段文字'),
    )
    article_type = models.ForeignKey(ArticleType, default=1, verbose_name=u'作品分类')
    sub_type = models.CharField(max_length=32, verbose_name=u'作品子分类')
    article_templates = models.CharField(choices=article_templates, max_length=20, default='article_list', verbose_name=u'模板类型')
    title = models.CharField(max_length=64, verbose_name=u'标题')
    content = models.TextField(null=True, blank=True, verbose_name=u'内容')

    def __unicode__(self):
        # return self.title
        return "%s(%s)" %(self.title, self.sub_type)

    class Meta:
        verbose_name_plural = u'作品'
        db_table = 'og_article'

#作品附件
class ArticleAttachment(models.Model):
    upload_dir = 'photos'
    attachment_type = (
        ('PI', u'图片'), 
        ('MU', u'音乐'),
        ('MO', u'视频'),
    )
    attachment_type = models.CharField(choices=attachment_type, max_length=2, default='PI', verbose_name=u'附件内容')
    url = models.FileField(max_length=200, upload_to=upload_dir, verbose_name=u'作品地址')
    article = models.ForeignKey(Article, verbose_name=u'作品')
    place = models.IntegerField(verbose_name=u'作品顺序')

    # def __unicode__(self):
        # return self.access_token

    def save(self):
        super(ArticleAttachment, self).save()
        old_filename = self.url.path
        old_name = self.url.url
        now = "/%s.jpg" %(int(time.time()*1000))     # 获取当前时间的时间戳，毫秒为单位
        new_filename = '%s%s' %(old_filename[:old_filename.rfind("/")], now)
        os.rename(old_filename, new_filename)
        self.url = "/static/upload/%s%s" %(self.upload_dir, now)
        # total_path = "%s%s" %(ROOT, self.url)
        source_image = Image.open(new_filename)
        target = (760, 350)
        source = source_image.size
        if (source[0]/target[0]) >= (source[1]/target[1]):
            rate = source[1]/target[1]
            cut = source[0] - target[0]*rate
            left = cut/2
            right = source[0]-cut/2
            new_image = source_image.crop((int(left), 0, int(right), int(source[1])))
        else:
            rate = source[0]/target[0]
            cut = source[1] - target[1]*rate
            top = cut/2
            bottom = source[1]-cut/2
            new_image = source_image.crop((0,int(top),int(source[0]), int(bottom)))
        new_image = new_image.resize(target, Image.ANTIALIAS)
        new_image.save(new_filename)
        super(ArticleAttachment, self).save()


    class Meta:
        verbose_name_plural = u'作品附件'
        db_table = 'og_article_attachment'




