# -*- coding:utf-8 -*-

from django.http import HttpResponse
import json
import requests
import re
import socket
import chardet
from ..randheader.randheader import get_ua
from ..whatcms.whatcms import WebPage


"""
通用函数/公共函数
"""


def success(code=200, data=[], msg='success'):
    """
    返回成功的json数据
    :param code:
    :param data:
    :param msg:
    :return:
    """
    result = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def error(code=400, data=[], msg='error'):
    """
    返回失败的json数据
    :param code:
    :param data:
    :param msg:
    :return:
    """
    result = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def addslashes(sstr):
    """
    过滤/转义字符串中的非法参数
    :param sstr:
    :return:
    """
    ss = sstr.strip().replace('\\', '\\\\').replace("'", "\\'").replace('"', '\\"').replace('<', '').replace('>', '')
    return ss


def getdomain(url=''):
    """
    获取域名
    :param url:
    :return:
    """
    url = url.rstrip('/')        # 去除末尾/，获取域名部分
    if url:
        if re.search('127.0.0.1|localhost', url):
            return 'None'
        if url.startswith('https://') or url.startswith('http://'):
            domain = url.split('/')[2]  # 获取域名
            print('[LOG GetDomain]: ', domain)
            return domain
        else:
            return None
    else:
        return None


def getdomainip(host=''):
    """
    通过域名获取IP
    :param host:
    :return:
    """
    # 如果是URL，则通过DNS解析获取其IP
    if not re.search(r'\d+\.\d+\.\d+\.\d+', host):
        host = getdomain(host)
        if host:
            socket.setdefaulttimeout(1)  # 设置默认请求超时时间为1s
            try:
                host = socket.gethostbyname(host)  # 通过域名请求解析IP，这里调用此函数一般传递的是IP
            except Exception as e:
                host = ''
                print('[LogError IsCdn-GetHostName]: ', e)
    if re.search('127.0.0.1', host):
        return '目标站点不可访问'
    if not host:
        print("[LogError IsCdn]: Host not matched!")
        return '目标站点不可访问'
    return host


if __name__ == '__main__':
    print('test')
