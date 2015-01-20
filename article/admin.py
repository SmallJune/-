# -*- coding:utf-8 -*-
from django.contrib import admin
from origingroup.article.models import Article, ArticleType, ArticleAttachment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_type', 'sub_type', 'title', 'content' ,'article_templates')
    ordering = ('id',)
    # 添加快速查询栏
    search_fields = ('article_type',)
    # 过滤器
    # list_filter = ('city',)
admin.site.register(Article, ArticleAdmin)

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_type',)
    ordering = ('id',)
    # 添加快速查询栏
    search_fields = ('article_type',)
    # 过滤器
    # list_filter = ('city',)
admin.site.register(ArticleType, ArticleTypeAdmin)

class ArticleAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'article', 'thumb', 'place')
    ordering = ('id', 'place')
    # 过滤器
    search_fields = ('article',)

    def thumb(self, obj):
        return u'<img src="%s" width="80">' %obj.url
    thumb.short_description = '缩略图'
    thumb.allow_tags = True

admin.site.register(ArticleAttachment, ArticleAttachmentAdmin)