# -*- coding:utf-8 -*-
from django.shortcuts import render


def index(request):
    """
    返回默认首页模版
    :param request:
    :return:
    """
    return render(request, 'index.html')
