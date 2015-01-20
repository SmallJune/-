# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from origingroup.jobs.models import Jobs, Company


def home(request, jobs_type='social', company_id=1):
    """获取工作详情"""
    jobs_data = []
    jobs_type = str(jobs_type)
    if not jobs_type in ['social', 'campus']:
        jobs_type = 'social'
    jobs_map = {'social':1, 'campus':2}
    jobs_type_id = jobs_map[jobs_type]
    sql_datas = Jobs.objects.filter(jobs_type=jobs_type_id, company_id=company_id)
    for sql_data in sql_datas:
        jobs_data.append({
            'id':sql_data.id,
            'jobs':sql_data.jobs,
            'number':sql_data.number,
            'company': sql_data.company.company,
            'gender': sql_data.get_gender_display(),
            'education': sql_data.education,
            'workplace': sql_data.workplace,
            'description': sql_data.description,
            'demand': sql_data.demand,
        })
    data = json.dumps(jobs_data)
    return HttpResponse(data)


def job_info(request, job_id=1):
    data = Jobs.objects.filter(id=job_id)
    if data:
       return HttpResponse(data[0])