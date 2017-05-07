#!/usr/bin/env python
# encoding: utf-8

# 运行爬虫
"""
@description: 

@author: BaoQiang
@time: 2017/5/2 21:06
"""

from scrapy import cmdline
import sys


def spider_run():
    arg = int(sys.argv[1])

    if arg == 1:
        cmdline.execute('scrapy crawl wxread_spider'.split())
    elif arg == 2:
        cmdline.execute('scrapy crawl huatian_spider'.split())


def main():
    spider_run()


if __name__ == '__main__':
    main()
