#!/usr/bin/env python
# encoding: utf-8

"""
@description:  代理池api配置

@author: BaoQiang
@time: 2017/4/24 17:27
"""

import requests
from xiaoreader.pth import logging
import json

url = 'http://192.168.10.195:5000'
# url = 'http://127.0.0.1:5000'

get_url = '{}/{}/'.format(url, 'get')
get_all_url = '{}/{}/'.format(url, 'get_all')

timeout = 3


def get_proxy():
    return requests.get(get_url).content.decode()


def get_all_proxy():
    proxy_str = requests.get(get_all_url).content.decode()
    return json.loads(proxy_str)


def delete_proxy(proxy):
    requests.get("{}/delete/?proxy={}".format(url, proxy))


def test(scheme='http'):
    url = 'https://www.baidu.com/duty' if scheme == 'https' else 'http://home.baidu.com'

    while True:
        proxy = get_proxy()
        try:
            res_code = requests.get(url, proxies={scheme: '{}://{}'.format(scheme, proxy)}, timeout=timeout)
        except Exception as e:
            delete_proxy(proxy)
            print(e)
            print('[FAIL]: {} {}'.format(scheme, proxy))
            continue

        # print('{} res: {}'.format(scheme, res_code))
        print('[SUCCESS]: {} {}'.format(scheme, proxy))
        break


def tmp():
    print(requests.get(get_url).content.decode())


def main():
    test()
    # tmp()


if __name__ == '__main__':
    main()
