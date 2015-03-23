# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from origingroup.article.models import ArticleType, Article, ArticleAttachment 

def get_attachmennt(article_id):
    """获取作品附件"""
    attachmennt_datas = []
    sql_datas = ArticleAttachment.objects.filter(article_id=article_id)
    if sql_datas.count() < 2:
        article_template = 'article_single'
    else:
        article_template = 'article'

    for sql_data in sql_datas:
        attachmennt_datas.append({
            'url': str(sql_data.url),
            'place': sql_data.place,
            'cover_path': sql_data.cover_path,
            'article_id': sql_data.article_id,
            'id': sql_data.id,
            'attachment_type': sql_data.attachment_type,
            'title': sql_data.article.title,
            'content': sql_data.article.content,
            'article_template': article_template,
        })

    return attachmennt_datas

def home(request, article_type=1, sub_type="", page=1):
    """获取作品详情"""
    article_datas = []
    start = (int(page)-1)*9
    end = start + 9
    sql_datas = Article.objects.filter(article_type=article_type, sub_type=sub_type).order_by('-id')[start:end]
    check_data = Article.objects.filter(article_type=article_type, sub_type=sub_type).order_by('-id')[end:end+1]
    if check_data:
        next = 1
    else:
        next = 0
    for sql_data in sql_datas:
        article_datas.append({
            'article_id': sql_data.id,
            'article_type': sql_data.article_type_id,
            'sub_type': sql_data.sub_type,
            'title': sql_data.title,
            'content': sql_data.content,
            'next': next,
            'page': int(page),
            'article_attachment': get_attachmennt(sql_data.id),
        })
    data = json.dumps(article_datas)
    return HttpResponse(data)

def article_info(request, article_id):
    """获取当个作品详情"""
    article_info_datas = []
    sql_datas = Article.objects.filter(id=article_id)
    for sql_data in sql_datas:
        article_info_datas.append({
            'article_id': sql_data.id,
            'article_type_id': sql_data.article_type_id,
            'sub_type': sql_data.sub_type,
            'title': sql_data.title,
            'content': sql_data.content,
            'article_attachment': get_attachmennt(sql_data.id),
        })
    data = json.dumps(article_info_datas)
    return HttpResponse(data)

def get_test(request):
    test = request.GET.get('test')
    data = [{"pkid":"0997","ProvinceId":"XJ","CityName":"阿克苏","CityNameEn":"Akesu","PostCode":"843000","isHotCity":False},{"pkid":"0412","ProvinceId":"LN","CityName":"鞍山","CityNameEn":"Anshan","PostCode":"114000","isHotCity":False}]
    if test:
        result = {'status':1001, 'data': data}
    else:
        result = {'status': 4004, 'data': []}
    return HttpResponse(json.dumps(result))

def post_test(request):
    test = request.POST.get('test')
    data = [{"pkid":"0997","ProvinceId":"XJ","CityName":"阿克苏","CityNameEn":"Akesu","PostCode":"843000","isHotCity":False},{"pkid":"0412","ProvinceId":"LN","CityName":"鞍山","CityNameEn":"Anshan","PostCode":"114000","isHotCity":False}]
    if test:
        result = {'status':1001, 'data': data}
    else:
        result = {'status': 4004, 'data': []}
    return HttpResponse(json.dumps(result))

def json_test(request):
    json_data = json.loads(request.GET.get('data'))
    data = json_data
    if data:
        result = {'status':1001, 'data': data}
    else:
        result = {'status': 4004, 'data': []}
    return HttpResponse(json.dumps(result))



