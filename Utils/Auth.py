# 增加一个装饰器，实现轻量验证
# decorators.py
from django.http import JsonResponse
from django.conf import settings
from Utils.Code import *


def token_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is not None and auth_header.startswith('Token '):
            token = auth_header[6:]  # Remove 'Bearer ' prefix
            if token == settings.TOKEN:
                return view_func(request, *args, **kwargs)
        return JsonResponse({'msg': 'Invalid token', 'code': FAIL_UNAUTHORIZED_CODE}, status=FAIL_UNAUTHORIZED_CODE)

    return _wrapped_view_func
