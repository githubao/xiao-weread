#!/usr/bin/env python
# encoding: utf-8

"""
@description: 请求接口，获取vid和skey参数

@author: BaoQiang
@time: 2017/5/5 15:02
"""

import requests
import json
import random

cookie_list = []


def get_random_header():
    global cookie_list

    if not cookie_list:
        cookie_list = load_cookies()

    item = random.choice(cookie_list)

    return headers.update({
        'vid': item[0],
        'skey': item[1],
    })


def load_cookies():
    res_list = []

    with open('cookies.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            json_data = json.loads(line)
            res_list.append((json_data['vid'], json_data['skey']))


def req():
    url = 'https://i.weread.qq.com/guestLogin'

    with open('cookies.txt', 'w', encoding='utf-8') as fw:
        # for i in range(100):
        for i in range(3):
            data = {
                "deviceId": "9c7daed897c9c9e441777c1a2d655e{:02}".format(i)
            }

            response = requests.post(url, json=data, verify=False)
            json_data = response.json()

            json.dump(json_data, fw, ensure_ascii=False)
            fw.write('\n')


headers = {
    'Host': 'i.weread.qq.com',
    'Accept': '*/*',
    'Proxy-Connection': 'keep-alive',
    'vid': '107802345',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    'channelId': 'AppStore',
    'User-Agent': 'WeRead/1.5.6 (iPhone; iOS 9.3; Scale/2.00)',
    'Connection': 'keep-alive',
    'skey': '7MJlQNyr',
    'Cookie': 'wr_logined=1',
    'v': '1.5.6.462'
}


def main():
    req()


if __name__ == '__main__':
    main()
