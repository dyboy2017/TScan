# -*- coding:utf-8 -*-
import requests
import json
from ..common.common import getdomain


def get_web_weight(domain):
    """
    获取网站权重
    :param domain:
    :return:
    """
    api_url = 'https://api.ooopn.com/rank/aizhan/api.php?url='
    try:
        res = requests.get(api_url+getdomain(domain), timeout=4)
        res_json = json.loads(res.text)
        result_str = '百度({})，Google({})，搜狗({})  --数据来源于aizhan.com'.format(res_json['bdm'], res_json['google'], res_json['sogou'])
    except Exception as e:
        result_str = '获取数据失败，稍后再试'
        print('[LogError WebWeight]: ', e)
    return result_str


if __name__ == '__main__':
    print(get_web_weight('https://www.dyboy.cn/'))
