#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/5/5 13:54
"""

import requests


def tmp():
    url = 'https://i.weread.qq.com/store/category?categoryId=14200&count=2&maxIdx=20&synckey=0'

    # skey: {"errcode":-2012,"errmsg":"登录超时"}
    # vid: {"errcode":-2010,"errmsg":"用户不存在"}
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

    response = requests.get(url, headers=headers,verify=False)
    content = response.content.decode()

    print(content)


def main():
    tmp()


if __name__ == '__main__':
    main()
