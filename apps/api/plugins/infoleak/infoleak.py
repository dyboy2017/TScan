# -*- coding:utf-8 -*-
import os
import json
import requests
from ..randheader.randheader import get_ua

STATUS_CODES = [200, 401, 305, 407]           # HTTP响应状态码


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


def get_infoleak(url=''):
    if url:
        file_path = os.path.dirname(__file__) + '/../../database/infoleak.json'
        fp = open(file_path, 'r', encoding='utf-8')
        json_data = json.load(fp)
        result = []
        for key in json_data['data'][0]:
            payloads = json_data['data'][0][key]
            for payload in payloads:
                # 开始尝试访问
                url_payload = url + payload
                if get_html(url_payload):
                    result.append([key, url_payload])
        fp.close()
        return result


if __name__ == '__main__':
    print(get_infoleak('http://www.dyboy.cn'))
