#!/usr/bin/env python
# encoding: utf-8

SPIDER_MODULES = ['xiaoreader.spider']

DOWNLOADER_MIDDLEWARES = {
    # 'xiaoreader.spider.httpproxy.HttpProxyMiddleware': 501,
}

# 使用延迟
# DOWNLOAD_DELAY = 0.2
# RANDOM_DOWNLOAD_DELAY = True