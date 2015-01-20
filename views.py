# -*-coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from origingroup.article.api import get_attachmennt
from origingroup.article.models import Article


def home(request):
    def get_article(article_type):
        articles_list = []
        if article_type:
            articles_data = Article.objects.filter(article_type=article_type)
            articles_data.query.group_by = ['sub_type']
            for data in articles_data:
                articles_list.append({
                    'article_template': data.article_templates,
                    'title': data.title,
                    'sub_type': data.sub_type,
                    'article_id': data.id,
                })
        return articles_list
    home_data = map(get_article, range(5))
    attachments=get_attachmennt(1)
    return render_to_response('index.jinja', {'home_data': home_data, 'attachments': attachments})

def cover(request):
    return render_to_response('index2.html',)



def index(request):
    return render_to_response('datatable.html',)