# -*- coding:utf-8 -*-

from django.shortcuts import render


def index(request):
    """
    基础信息页面
    :param request:
    :return:
    """
    return render(request, 'web_index.html')


def portscan(request):
    """
    端口扫描页面
    :param request:
    :return:
    """
    return render(request, 'web_portscan.html')


def webside(request):
    """
    旁站信息
    :param request:
    :return:
    """
    return render(request, 'web_webside.html')


def infoleak(request):
    """
    信息泄漏检查
    :param request:
    :return:
    """
    return render(request, 'web_infoleak.html')