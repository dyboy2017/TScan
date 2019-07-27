# -*- coding:utf-8 -*-

from django.http import HttpResponse
import json
import re
import socket

FORBIDDEN_DOMAIN = '127.*.*.*|192.168.*.*|local|gov.cn|top15.cn|dyboy'
FORBIDDEN_IP = '127.*.*.*|192.168.*.*|10.*.*.*|172.(1[6-9]|2[0-9]|31).*.*'

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
    url = check_url(url)
    if url:
        domain = url.split('/')[2]  # 获取域名
        print('[LOG GetDomain]: ', domain)
        return domain
    return None


def getdomainip(host=''):
    """
    通过域名获取IP
    :param host:
    :return: ip | 'string'
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
    if re.search('127.0.0.1|localhost|top15.cn|gov.cn|edu.cn', host):
        return '目标站点不可访问'
    if not host:
        print("[LogError IsCdn]: Host not matched!")
        return '目标站点不可访问'
    return host


def check_ip(ipaddr=''):
    """
    校验IP合法性
    :param ipaddr:
    :return: True|False
    """
    ipaddr = str(ipaddr)
    if (6 < len(ipaddr)) and (len(ipaddr) < 16):
        if re.search(FORBIDDEN_IP, ipaddr):
            return False
        # IP地址的长度范围(6, 16)
        rule = r'^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$'
        compile_ip = re.compile(rule)
        if compile_ip.match(ipaddr):
            return True
    return False


def check_url(url=''):
    """
    校验URL合法性
    :param url:
    :return: 合法的URL | False
    """
    url = (str(url)).strip().replace('"', '').replace("'", '').replace('<', '').replace('>', '').replace(';', '')\
        .replace('\\', '/')
    if (10 < len(url)) and (len(url) < 40):
        # 链接长度(10, 40)，否则认为不合法 http://a.cn
        if re.search(FORBIDDEN_DOMAIN, url):
            # 判断是否在禁止域名/IP
            return False
        if url.startswith('http://') or url.startswith('https://'):
            # URL是否以http://或https://开头
            url_params = url.split('/')
            domain = url_params[2]
            if domain.find('.') >= 0:
                # URL中的域名是否至少含有一个‘.’，返回全小写URL
                return url.lower()
    return False


if __name__ == '__main__':
    print('test')
