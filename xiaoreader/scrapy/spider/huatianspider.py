#!/usr/bin/env python
# encoding: utf-8

"""
@description: 花田爬虫

@author: BaoQiang
@time: 2017/5/7 11:59
"""

import scrapy
from scrapy import Request
import time
import requests


class HuatianSpider(scrapy.Spider):
    name = 'huatian_spider'
    allowed_domains = ['love.163.com']

    def start_requests(self):
        return [Request('https://love.163.com', headers=headers, callback=self.parse_cate)]

    def parse_cate(self, response):
        # for i in range(100):
        for i in range(1):
            yield Request(api_url.format(int(time.time() * 1000)), headers=headers, callback=self.parse_item)

    def parse_item(self, response):
        print(response.body.decode())


api_url = 'https://love.163.com/api/home/recommendList?birthCity=&birthProvince=&bothMatched=false&car=&city=1' \
          '&condition=0&constellation=&education=0&house=&industry=&latitude=40.076189&longitude=116.418808' \
          '&marriageStatus=0&nationality=&province=36&reqAgeEnd=60&reqAgeStart=18&reqHeightEnd=0&reqHeightStart=0' \
          '&reqSalaryEnd=0&reqSalaryStart=0&timeCursor={}'

headers = {
    'Host': 'love.163.com',
    'Accept': '*/*',
    'Proxy-Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    'User-Agent': 'Huatian App iOS 9.3 iPhone8,1 4.1.0',
    'Connection': 'keep-alive',
    'Cookie': 'user-from=fujin; access_token=6bee169bd35a7aa4ef288fe0b6511101; _ntes_nnid=78f4aa1f35be878fa0859160e79a7033,1493171921129; _ntes_nuid=78f4aa1f35be878fa0859160e79a7033',
}


def tmp():
    print(int(time.time() * 1000))


def tmp2():
    response = requests.get(api_url.format(int(time.time() * 1000)), headers=headers, verify=False)
    print(response.json())


def main():
    tmp2()


if __name__ == '__main__':
    main()
