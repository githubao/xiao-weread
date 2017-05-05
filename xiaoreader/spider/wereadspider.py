#!/usr/bin/env python
# encoding: utf-8

"""
@description: 微信读书app的爬虫

@author: BaoQiang
@time: 2017/5/2 20:25
"""

import json
import time

import scrapy
from scrapy import Request
from xiaoreader.spider.cookiesapi import get_random_header

from xiaoreader.pth import *

out_file = '{}/{}'.format(FILE_PATH, 'wxread.json')


class WereadSpider(scrapy.Spider):
    name = 'wxread_spider'
    allowed_domains = ['weread.qq.com']

    def start_requests(self):
        # return [Request('http://i.weread.qq.com/book/info?bookId=182590', headers=headers, callback=self.parse_cate)]
        return [Request(root_url.format(int(time.time())), headers=get_random_header(), callback=self.parse_cate)]

    def parse_cate(self, response):
        # json_cate = json.loads(open('C:\\Users\\BaoQiang\\Desktop\\cate.json', 'r', encoding='utf-8').read().strip())
        json_cate = json.loads(response.body.decode())

        for cate in json_cate['categories']:
            for subcate in cate['sublist']:
                subcateid = subcate['CategoryId']
                total_cnt = subcate['totalCount']

                for i in range(int(total_cnt / 20) + 1):
                    yield Request(cate_url.format(subcateid, i * 20), headers=get_random_header(),
                                  callback=self.parse_item)

    def parse_item(self, response):
        json_list = json.loads(response.body.decode())

        for book in json_list['books']:
            bookid = book['bookInfo']['bookId']
            yield Request(book_url.format(bookid), headers=get_random_header(), callback=self.parse_book,
                          meta={"bid": bookid})

            # break

    def parse_book(self, response):
        bookid = response.meta['bid']

        book = {}
        book['url'] = response.url
        book['id'] = bookid

        json_item = json.loads(response.body.decode())

        book['cate'] = json_item['category']
        book['title'] = json_item['title']
        book['intro'] = json_item['intro'].strip()
        book['star'] = json_item['star'] if 'star' in json_item else 0

        yield Request(rate_url.format(bookid), headers=get_random_header(), callback=self.parse_book2,
                      meta={"book": book})

    def parse_book2(self, response):
        book = response.meta['book']
        json_item = json.loads(response.body.decode())
        book['vote_cnt'] = json_item['data'][0]['totalCount']

        with open(out_file, 'a', encoding='utf-8') as fw:
            json.dump(book, fw, ensure_ascii=False, sort_keys=True)
            fw.write('\n')


def scrap():
    raise Exception('break loop')


root_url = 'https://i.weread.qq.com/store/categories?recommend=0&synckey={}'
cate_url = 'https://i.weread.qq.com/store/category?categoryId={}&count=20&maxIdx={}&synckey=0'
book_url = 'https://i.weread.qq.com/book/info?bookId={}'
rate_url = 'https://i.weread.qq.com/review/sameTimeReading?bookIds={}&onlyTotalCount=1'


def main():
    scrap()


if __name__ == '__main__':
    main()
