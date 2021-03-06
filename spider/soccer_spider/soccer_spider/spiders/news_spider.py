# -*- coding: utf-8 -*-

import scrapy
from soccer_spider.items import News


class NewsSpider(scrapy.Spider):
    name = "news_spider"

    allowed_domains = ["ba1.win007.com", "ba2.win007.com"]
    start_urls = (
        "http://ba2.win007.com",
    )

    def parse(self, response):
        # 英超
        yingchao_url = "http://ba2.win007.com/pub/ThemePageContent?conditions=1&order=1&id=3158"
        # 西甲
        xijia_url = "http://ba2.win007.com/pub/ThemePageContent?conditions=1&order=1&id=3159"
        # 意甲
        yijia_url = "http://ba2.win007.com/pub/ThemePageContent?conditions=1&order=1&id=3161"
        # 德甲
        dejia_url = "http://ba2.win007.com/pub/ThemePageContent?conditions=1&order=1&id=3162"
        # 欧冠
        ouwin_url = "http://ba2.win007.com/pub/ThemePageContent?conditions=1&order=1&id=7454"

        compname = "英超"
        for i in range(1, 3):
            page_url = yingchao_url + "&page=" + str(i)
            yield scrapy.http.Request(url=page_url,
                                      callback=lambda response,
                                                      compname=compname: self.crawl_news_list(response, compname))

        compname = "西甲"
        for i in range(1, 3):
            page_url = xijia_url + "&page=" + str(i)
            yield scrapy.http.Request(url=page_url,
                                      callback=lambda response,
                                                      compname=compname: self.crawl_news_list(response, compname))

        compname = "意甲"
        for i in range(1, 3):
            page_url = yijia_url + "&page=" + str(i)
            yield scrapy.http.Request(url=page_url,
                                      callback=lambda response,
                                                      compname=compname: self.crawl_news_list(response, compname))

        compname = "德甲"
        for i in range(1, 3):
            page_url = dejia_url + "&page=" + str(i)
            yield scrapy.http.Request(url=page_url,
                                      callback=lambda response,
                                                      compname=compname: self.crawl_news_list(response, compname))

        compname = "欧冠"
        for i in range(1, 3):
            page_url = ouwin_url + "&page=" + str(i)
            yield scrapy.http.Request(url=page_url,
                                      callback=lambda response,
                                                      compname=compname: self.crawl_news_list(response, compname))

    def crawl_news_list(self, response, compname):
        news_url_list = response.selector.xpath('//li/div[2]/a[2]/@href').extract()
        for url in news_url_list:
            news_url = "http://ba1.win007.com" + url
            yield scrapy.http.Request(url=news_url,
                                      callback=lambda response,
                                                      compname=compname: self.crawl_news(response, compname))

    def crawl_news(self, response, compname):
        title = response.selector.xpath('//div[@class="qiuba_title"]//text()').extract()[1].strip()
        author = response.selector.xpath('//div[@class="qiuba_Info2"]/a/text()').extract()[0].strip()
        publish_time = response.selector.xpath('//div[@class="qiuba_Info"]/div[@class="huise"][1]/text()').extract()[0]
        tokens = publish_time.strip().split('于 ')
        tokens = tokens[1].strip().split(' 编辑')
        publish_time = "20" + tokens[0] + ":00"

        content = response.selector.xpath('//body/div[@id="content"]\
                                           /div[@class="context"]\
                                           /div[@id="left"]\
                                           /div[@class="qiubaBox"]\
                                           /div[@class="qiuba_Info"]\
                                           /*')
        content_list = []
        for p in content[3:]:
            line = p.xpath('string(.)').extract()[0]
            if len(line) > 0:
                if line.strip().find("看不够？戳我") != -1 or \
                                line.strip().find("本翻译文档及图片仅供吧友学习研究之用，版权归属原作者，未经许可不得转载，不得用于任何商业用途") != -1:
                    continue
                content_list.append(line)

        news = News()
        news["title"] = title
        news["author"] = author
        news["content"] = content_list
        news["publish_time"] = publish_time
        news["compname"] = compname
        news["new_url"] = response.url
        yield news
