# -*- coding:utf-8 -*-
import os
import json
import requests
import threading
from ..randheader.randheader import get_ua

STATUS_CODES = [200, 206, 401, 305, 407]           # HTTP响应状态码，判断认为存在风险链接的状态码
RESULT = []


def get_html(url=''):
    """
    判断URL访问是否存在
    :param url:
    :return:
    """
    if url:
        try:
            response = requests.get(url, headers=get_ua(), timeout=3, allow_redirects=False)
            if response.status_code in STATUS_CODES:
                return True
        except Exception as e:
            print('[LogError infoleak]: ', e)
    else:
        return False


def get_html2(url='', key=''):
    """
    判断URL访问是否存在，用于多线程
    :param url:
    :return:
    """
    if url:
        try:
            response = requests.get(url, headers=get_ua(), timeout=3, allow_redirects=False)
            if response.status_code in STATUS_CODES:
                RESULT.append([key, url])
        except Exception as e:
            print('[LogError infoleak]: ', e)


def get_infoleak(url=''):
    """
    尝试访问风险链接
    :param url:
    :return:
    """
    global RESULT
    RESULT = []         #清空
    file_path = os.path.dirname(__file__) + '/../../database/infoleak.json'     # 配置文件 database/infoleak.json
    fp = open(file_path, 'r', encoding='utf-8')
    json_data = json.load(fp)
    fp.close()
    payload_list = []
    thread_list = []

    for key in json_data['data'][0]:
        payloads = json_data['data'][0][key]
        for payload in payloads:
            # 开始尝试访问
            url_payload = url + payload
            payload_list.append([key, url_payload])
            # if get_html(url_payload):
            #     result.append([key, url_payload])

    for item in payload_list:
        thd = threading.Thread(target=get_html2, args=(item[1], item[0], ))
        thd.start()
        thread_list.append(thd)

    for thd in thread_list:
        thd.join()

    return RESULT


if __name__ == '__main__':
    print(get_infoleak('http://www.dyboy.cn'))
