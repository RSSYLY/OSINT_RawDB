from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from Utils.Auth import token_required
from Utils.Code import *
from main_db.models import RawArticlesData

import json


# Create your views here.

# 爬虫写入文章数据

@api_view(['POST'])
@token_required
def add_articles(request):
    ret_data = {
        'code': SUCCESS_CODE,
        'msg': 'Add articles successfully.'
    }
    try:
        contents = request.data['content']
        for content in contents:
            date = request.data['Date']
            content = json.dumps(content)
            RawArticlesData.objects.create(date=date, content=content)
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SUCCESS_CREATED_CODE)
    except Exception as e:
        ret_data['code'] = SERVER_FAIL_CODE
        ret_data['msg'] = str(e)
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SERVER_FAIL_CODE)


# 获取所有文章数据
@api_view(['GET'])
@token_required
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
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SUCCESS_CODE)
    except Exception as e:
        ret_data['code'] = SERVER_FAIL_CODE
        ret_data['msg'] = str(e)
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SERVER_FAIL_CODE)

# 通过id删除指定文章
@api_view(['GET'])
@token_required
def delete_article(request, article_id):
    ret_data = {
        'code': SUCCESS_CODE,
        'msg': 'Delete article successfully.',
    }
    try:
        if not RawArticlesData.objects.filter(id=article_id).exists():
            ret_data['code'] = FAIL_GONE_CODE
            ret_data['msg'] = 'Article not found.'
            return HttpResponse(json.dumps(ret_data), content_type="application/json", status=FAIL_GONE_CODE)
        RawArticlesData.objects.filter(id=article_id).delete()
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SUCCESS_CODE)
    except Exception as e:
        ret_data['code'] = SERVER_FAIL_CODE
        ret_data['msg'] = str(e)
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SERVER_FAIL_CODE)

# 通过id更改指定文章
@api_view(['POST'])
@token_required
def update_article(request, article_id):
    ret_data = {
        'code': SUCCESS_CODE,
        'msg': 'Update article successfully.',
    }
    try:
        if not RawArticlesData.objects.filter(id=article_id).exists():
            ret_data['code'] = FAIL_GONE_CODE
            ret_data['msg'] = 'Article not found.'
            return HttpResponse(json.dumps(ret_data), content_type="application/json", status=FAIL_GONE_CODE)
        content = json.dumps(request.data['content'])
        RawArticlesData.objects.filter(id=article_id).update(content=content)
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SUCCESS_CODE)
    except Exception as e:
        ret_data['code'] = SERVER_FAIL_CODE
        ret_data['msg'] = str(e)
        return HttpResponse(json.dumps(ret_data), content_type="application/json", status=SERVER_FAIL_CODE)