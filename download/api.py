# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from origingroup.download.models import Download 

def home(request, file_type=u'集团手册'):
    """获取工作详情"""
    FILE_TYPE = {
        u'集团手册', 1, 
        u'室内手册', 2,
        u'项目物料', 3,
    }
    if file_type == u'集团手册':
        file_type_id = 1
    elif file_type == u'室内手册':
        file_type_id = 2
    elif file_type == u'项目物料':
        file_type_id = 3
        
    files_data = []
    sql_datas = Download.objects.filter(file_type=file_type_id)
    for sql_data in sql_datas:
        files_data.append({
            'filename':sql_data.file_name,
            'url': str(sql_data.url),
        })
    # files_data = {'file_type': file_type}
    data = json.dumps(files_data)
    return HttpResponse(data)
