# -*- coding: utf-8 -*-

# Scrapy settings for soccer_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os
import sys
import django


def setup_django_environment(path):
    sys.path.append(os.path.join(path))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ball.settings'
    django.setup()


setup_django_environment("/data/python/ball")  # django项目实际目录

BOT_NAME = 'soccer_spider'

SPIDER_MODULES = ['soccer_spider.spiders']
ITEM_PIPELINES = {
    'soccer_spider.pipelines.NewsPipeline': 2,
    'soccer_spider.pipelines.MatchPipeline': 3,
    'soccer_spider.pipelines.ShooterPipeline': 4,
    'soccer_spider.pipelines.LotteryPipeline': 5,
}

DOWNLOADER_MIDDLEWARES = {
    'soccer_spider.middlewares.RandomUserAgent': 1,
    # 'soccer_spider.middlewares.ProxyMiddleware': 100,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

NEWSPIDER_MODULE = 'soccer_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"

USER_AGENTS = [
    # ———————————————— Chrome ————————————————
    # Chrome 41.0.2228.0
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    # Chrome 41.0.2227.1
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    # Chrome 41.0.2227.0
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    # Chrome 41.0.2226.0
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    # Chrome 41.0.2225.0
    'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
    # Chrome 41.0.2224.3
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    # Chrome 40.0.2214.93
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    # Chrome 37.0.2062.124
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    # Chrome 37.0.2049.0
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    # Chrome 36.0.1985.67
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    # Chrome 36.0.1985.125
    'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    # Chrome 36.0.1944.0
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',

    # ———————————————— Firefox ———————————————
    # Firefox 40.1
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    # Firefox 36.0
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    # Firefox 33.0
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    # Firefox 31.0
    'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
    # Firefox 29.0
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0',
    # Firefox 28.0
    'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',

    # ———————————————— Safari ————————————————
    # Safari 9.0.2
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    # Safari 7.0.3
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
]

PROXIES = [
    {'ip_port': '221.227.250.84:21886', 'user_pass': ''},
    {'ip_port': '115.217.252.225:38249', 'user_pass': ''},
    {'ip_port': '122.114.31.177:808', 'user_pass': ''},
    {'ip_port': '61.135.217.7:80', 'user_pass': ''},
    {'ip_port': '120.92.88.202:10000', 'user_pass': ''},
    {'ip_port': '123.169.254.75:61234', 'user_pass': ''},
]

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_ITEMS = 100
