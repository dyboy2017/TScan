# -*- coding:utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from .plugins.common.common import success, error, addslashes, getdomain, getdomainip, check_ip, check_url
import time
from .plugins.common.common import getuserip
from .plugins.loginfo.loginfo import LogHandler
MYLOGGER = LogHandler(time.strftime("%Y-%m-%d", time.localtime()) + 'log')


@csrf_exempt
def index(request):
    """
    后台API默认接口
    :param request:
    :return:
    """
    MYLOGGER.error('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
        request.POST) + ' SC:404 UIP:' + getuserip(request) + ' RDATA:' + '骚年，你想干嘛！')
    return error(404, '骚年，你想干嘛！', 'https://blog.dyboy.cn')


@csrf_exempt
def baseinfo(request):
    """
    返回网站的基本信息接口
    :param request:
    :return:
    """
    from .plugins.baseinfo.baseinfo import getbaseinfo
    url = check_url(request.POST.get('url'))
    if url:
        res = getbaseinfo(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(res))
        return success(res['code'], res, res['msg'])
    return error(400, '请填写正确的URL地址', '请输入正确的网址， 例如：http://example.cn')


@csrf_exempt
def webweight(request):
    """
    获取网站权重
    :param request:
    :return:
    """
    from .plugins.webweight.webweight import get_web_weight
    url = check_url(request.POST.get('url'))
    if url:
        result = get_web_weight(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')


@csrf_exempt
def isexistcdn(request):
    """
    判断当前域名是否使用了CDN
    :param request:
    :return:
    """
    from .plugins.cdnexist.cdnexist import iscdn
    url = check_url(request.POST.get('url'))
    if url:
        result_str = iscdn(url)
        if result_str == '目标站点不可访问':
            return success(200, result_str, '网络错误')
        if result_str:
            result_str = '存在CDN（源IP可能不正确）'
        else:
            result_str = '无CDN'
        return success(200, result_str, 'Success!')
    return error(400, '请填写正确的IP地址', 'error')


@csrf_exempt
def is_waf(request):
    """
    判断当前域名是否使用了WAF
    :param request:
    :return:
    """
    from .plugins.waf.waf import getwaf
    url = check_url(request.POST.get('url'))
    if url:
        return success(200, getwaf(url), 'ok')
    return error(400, '请填写正确的URL地址', 'error')


@csrf_exempt
def what_cms(request):
    """
    判断当前域名使用了什么框架，cms等指纹信息
    :param request:
    :return:
    """
    from .plugins.whatcms.whatcms import getwhatcms
    url = check_url(request.POST.get('url'))
    if url:
        result = getwhatcms(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')


@csrf_exempt
def port_scan(request):
    """
    获取开放端口列表
    :param request:
    :return:
    """
    from .plugins.portscan.portscan import ScanPort
    ip = request.POST.get('ip')
    if check_ip(ip):
        result = ScanPort(ip).pool()
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok!')
    return error(400, '请填写正确的IP地址', 'error')


@csrf_exempt
def getwebsideinfo(request):
    """
    获取旁站信息
    :param request:
    :return:
    """
    from .plugins.webside.webside import get_side_info
    ip = request.POST.get('ip')
    if check_ip(ip):
        result = get_side_info(ip)
        if result:
            return success(200, result, 'ok')
        return error(400, '未找到旁站信息！', 'error')
    return error(400, '请填写正确的IP地址', 'error')


@csrf_exempt
def getinfoleak(request):
    """
    信息泄漏检测
    :param request:
    :return:
    """
    from .plugins.infoleak.infoleak import get_infoleak
    url = check_url(request.POST.get('url'))
    if url:
        result = get_infoleak(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')
