from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from Utils.Code import *
from main_db.models import RawArticlesData

import json


# Create your views here.

# 爬虫写入文章数据

@api_view(['POST'])
def add_articles(request):
    ret_data = {
        'code': SUCCESS_CODE,
        'msg': 'Add articles successfully.'
    }
    try:
        contents = request.data['contents']
        for content in contents:
            date = request.data['date']
            content = json.dumps(content)
            RawArticlesData.objects.create(date=date, content=content)
        return HttpResponse(json.dumps(ret_data), content_type="application/json")
    except Exception as e:
        ret_data['code'] = SERVER_FAIL_CODE
        ret_data['msg'] = str(e)
        return HttpResponse(json.dumps(ret_data), content_type="application/json")

# 获取所有文章数据
@api_view(['GET'])
def get_articles(request):
    ret_data = {
        'code': SUCCESS_CODE,
        'msg': 'Get articles successfully.',
        'data': []
    }
    try:
        articles = RawArticlesData.objects.all()
        for article in articles:
            ret_data['data'].append({
                'id': article.id,
                'date': article.date.strftime('%Y-%m-%d %H:%M:%S'),
                'content': json.loads(article.content)
            })
        return HttpResponse(json.dumps(ret_data), content_type="application/json")
    except Exception as e:
        ret_data['code'] = SERVER_FAIL_CODE
        ret_data['msg'] = str(e)
        return HttpResponse(json.dumps(ret_data), content_type="application/json")

