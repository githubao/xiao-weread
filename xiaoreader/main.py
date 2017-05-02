#!/usr/bin/env python
# encoding: utf-8

# 运行爬虫
"""
@description: 

@author: BaoQiang
@time: 2017/5/2 21:06
"""

from scrapy import cmdline


def spider_run():
    cmdline.execute('scrapy crawl wxread_spider'.split())


def main():
    spider_run()


if __name__ == '__main__':
    main()
