#!/usr/bin/env python
# encoding: utf-8

"""
@description: ip代理

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: httpproxy.py
@time: 2017/1/19 16:10
"""

import random
from urllib.parse import urlparse
from collections import defaultdict

from xiaoreader.pth import logging
import time
from xiaoreader.scrapy.spider.proxyapi import get_all_proxy

# 五分钟换一次
# max_time = 5
# max_time = 300
max_time = 600


class HttpProxyMiddleware():
    def __init__(self, proxies):
        self.proxies = defaultdict(lambda: [])
        # for scheme, proxy in proxies.items():
        #     scheme = scheme.lower()
        #     self.proxies[scheme].append(proxy)
        for proxy in proxies:
            self.proxies['http'].append('http://{}'.format(proxy))
            self.proxies['https'].append('http://{}'.format(proxy))

        self.start = time.time()

    @classmethod
    def from_crawler(cls, crawler):
        # return cls(crawler.settings.get('RANDOM_PROXIES'))
        return cls(get_proxy())

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            return

        self.check_expire()

        scheme = urlparse(request.url).scheme
        if self.proxies[scheme]:
            proxy = random.choice(self.proxies[scheme])
            # logging.info('using proxy:[{}] {}'.format(request.url, proxy))
            request.meta['proxy'] = proxy

    def check_expire(self):
        end = time.time()
        if (end - self.start) > max_time:
            self.start = end
            self.update_proxy()

    def update_proxy(self):
        proxies = get_proxy()
        if not proxies:
            return

        logging.error('UPDATING PROXIES LEN: {}'.format(len(proxies)))
        logging.error('NOW AVAILABLE PROXIES: {}'.format(proxies))

        self.proxies = defaultdict(lambda: [])
        for proxy in proxies:
            self.proxies['http'].append('http://{}'.format(proxy))
            self.proxies['https'].append('http://{}'.format(proxy))




def get_proxy():
    return get_all_proxy()
    # return get_ip_list()


def main():
    print(urlparse('https://my.oschina.net/guol/blog/95699'))


if __name__ == '__main__':
    main()
