# -*- coding:utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from .plugins.common.common import success, error, addslashes, getdomain, getdomainip, check_ip
import re


@csrf_exempt
def index(request):
    """
    后台API默认接口
    :param request:
    :return:
    """
    return error(404, '', 'Not Found!')


@csrf_exempt
def baseinfo(request):
    """
    返回网站的基本信息接口
    :param request:
    :return:
    """
    from .plugins.baseinfo.baseinfo import getbaseinfo
    if request.POST.get('url'):
        testurl = addslashes(request.POST.get('url'))
        res = getbaseinfo(testurl)
        return success(res['code'], res, res['msg'])
    return error(400, '', 'URL NULL!')


@csrf_exempt
def webweight(request):
    """
    获取网站权重
    :param request:
    :return:
    """
    from .plugins.webweight.webweight import get_web_weight
    if request.POST.get('url'):
        testurl = addslashes(request.POST.get('url'))
        print('[Log TargetWebsite]: ', testurl)
        return success(200, get_web_weight(testurl), 'Found!')
    else:
        return error(400, '', 'URL NULL!')


@csrf_exempt
def isexistcdn(request):
    """
    判断当前域名是否使用了CDN
    :param request:
    :return:
    """
    from .plugins.cdnexist.cdnexist import iscdn
    if request.POST.get('url'):
        testurl = addslashes(request.POST.get('url'))
        result_str = iscdn(testurl)
        if result_str == '目标站点不可访问':
            return success(200, result_str, 'Internet error!')
        if result_str:
            result_str = '存在CDN（源IP可能不正确）'
        else:
            result_str = '无CDN'
        return success(200, result_str, 'Success!')
    else:
        return error(400, '', 'URL NULL!')


@csrf_exempt
def is_waf(request):
    """
    判断当前域名是否使用了WAF
    :param request:
    :return:
    """
    from .plugins.waf.waf import getwaf
    result_str = "URL错误"
    if request.POST.get('url'):
        testurl = addslashes(request.POST.get('url'))
        result_str = getwaf(testurl)
    return success(200, result_str, '')


@csrf_exempt
def what_cms(request):
    """
    判断当前域名使用了什么框架，cms等指纹信息
    :param request:
    :return:
    """
    from .plugins.whatcms.whatcms import getwhatcms
    url = request.POST.get('url')
    if re.search('https://|http://', url):
        url = addslashes(url)
        return success(200, getwhatcms(url), 'Got')
    return error(400, 'URL错误', '')


@csrf_exempt
def port_scan(request):
    """
    获取开放端口列表
    :param request:
    :return:
    """
    from .plugins.portscan.portscan import ScanPort
    url = request.POST.get('url')
    open_port_list = []
    host = ''
    if not url:
        return error(400, '请填写正确的域名或IP', 'error')
    if re.search(r'\d+\.\d+\.\d+\.\d+', url):
        # 是IP地址则调用扫描
        host = url
    elif re.search(r'local|top15', url):
        return error(400, '目标站点不可达', 'error')
    else:
        # 如果不是IP，那么就要通过域名获取IP
        url = addslashes(url)
        domain = getdomain(url)
        if domain:
            host = getdomainip(domain)
        else:
            host = ''
    if host:
        # IP地址有效
        if not re.search(r'\d+\.\d+\.\d+\.\d+', host):
            return error(400, '请填写正确的域名或IP', 'error')
        if re.search('127.0.0.1|localhost', host):
            return error(400, '目标站点不可达', 'error')
        open_port_list = ScanPort(host).pool()
    else:
        return error(400, '请填写正确的域名或IP', 'error')
    return success(200, open_port_list, 'ok!')


@csrf_exempt
def getwebsideinfo(request):
    from .plugins.webside.webside import get_side_info
    ip = request.POST.get('ip')
    if check_ip(ip):
        result = get_side_info(ip)
        if result:
            success(200, result, 'ok')
        else:
            error(400, '未找到旁站信息！', 'error')
    else:
        return error(400, 'IP不正确', 'error')
