#!/usr/bin/env python
# encoding: utf-8

"""
@description: 微信读书app的爬虫

@author: BaoQiang
@time: 2017/5/2 20:25
"""

import time

import requests
import json
import scrapy
from scrapy import Request


class WereadSpider(scrapy.Spider):
    name = 'wxread_spider'
    allowed_domains = ['weread.qq.com']

    def start_requests(self):
        return [Request('http://i.weread.qq.com/book/info?bookId=182590', headers=headers, callback=self.parse_cate)]
        # return [Request(root_url.format(int(time.time())), headers=headers, callback=self.parse_cate)]

    def parse_cate(self, response):
        json_cate = json.loads(open('C:\\Users\\BaoQiang\\Desktop\\cate.json', 'r', encoding='utf-8').read().strip())
        # json_cate = json.loads(response.body.decode())

        for cate in json_cate['categories']:
            for subcate in cate['sublist']:
                subcateid = subcate['CategoryId']
                total_cnt = subcate['totalCount']

                for i in range(int(total_cnt / 20) + 1):
                    yield Request(cate_url.format(subcateid, i * 20), headers=headers, callback=self.parse_item)

                    break

    def parse_item(self, response):
        json_list = json.loads(response.body.decode())

        for book in json_list['books']:
            bookid = book['bookInfo']['bookId']
            yield Request(book_url.format(bookid), headers=headers, callback=self.parse_book)

            break

    def parse_book(self, response):
        json_item = json.loads(response.body.decode())
        print(json_item)


def scrap():
    raise Exception('break loop')


root_url = 'http://i.weread.qq.com/store/categories?recommend=0&synckey={}'
cate_url = 'http://i.weread.qq.com/store/category?categoryId={}&count=20&maxIdx={}&synckey=0'
book_url = 'http://i.weread.qq.com/book/info?bookId={}'

headers = {
    'Host': 'i.weread.qq.com',
    'Accept': '*/*',
    'Proxy-Connection': 'keep-alive',
    'vid': '17369527',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    'channelId': 'AppStore',
    'User-Agent': 'WeRead/1.5.6 (iPhone; iOS 9.3; Scale/2.00)',
    'Connection': 'keep-alive',
    'skey': '2y7ELP09',
    'Cookie': 'wr_logined=1',
    'v': '1.5.6.462'
}


def main():
    scrap()


if __name__ == '__main__':
    main()
