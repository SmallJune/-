# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from origingroup.article.models import ArticleAttachment


def waterfall(request):
    attachment = ArticleAttachment.objects.all()
    images = []
    if attachment:
        for data in attachment:
            images.append({
               'path': data.url,
               'title': data.article.title,
               'content': data.article.content,
            })
    return render_to_response('waterfall.html', {'data': images})