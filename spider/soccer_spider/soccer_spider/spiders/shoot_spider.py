# -*- coding: utf-8 -*-
import scrapy
from soccer_spider.items import Shooter


class ShooterSpider(scrapy.Spider):
    name = "shooter_spider"

    allowed_domains = ["saishi.caipiao.163.com"]
    start_urls = (
        "http://saishi.caipiao.163.com/",
    )

    def parse(self, response):
        # 英超
        yingchao_match = "http://saishi.caipiao.163.com/8.html"
        yield self.crawl_comp(yingchao_match, "英超")

        # 德甲
        dejia_match = "http://saishi.caipiao.163.com/9.html"
        yield self.crawl_comp(dejia_match, "德甲")

        # 意甲
        yijia_match = "http://saishi.caipiao.163.com/13.html"
        yield self.crawl_comp(yijia_match, "意甲")

        # 西甲
        xijia_match = "http://saishi.caipiao.163.com/7.html"
        yield self.crawl_comp(xijia_match, "西甲")

    def crawl_comp(self, url, compname):
        return scrapy.http.Request(url=url,
                                   callback=lambda response,
                                                   compname=compname: self.crawl_round_list(response, compname))

    def crawl_round_list(self, response, compname):
        season = response.selector.xpath(
            '//section[@class="leftNav"]//span[@class="mcSelectBox"]/a[@class="imitateSelect"]/b/text()').extract()[0]
        shooter_url = response.selector.xpath(
            '//section[@class="leftNav"]//div[@class="matchStatBody sign"]/div[@class="lineBottom"][1]/ul/li[6]/a/@href').extract()[
            0]
        yield scrapy.http.Request(url=shooter_url,
                                  callback=lambda response,
                                                  compname=compname,
                                                  season=season: self.crawl_shooter(response, compname, season))

    def crawl_shooter(self, response, compname, season):
        shooter_list = response.selector.xpath('//div[@class="listWrap"]/table/tr')
        for s in shooter_list[1:]:
            shooter_info = []
            for info in s.xpath('td//text()').extract():
                if info.strip() != "":
                    shooter_info.append(info.strip())
            shooter = Shooter()
            print("xxxxx---%s---xxxxxx" % compname)
            shooter["compname"] = compname
            shooter["season"] = season
            # 排名
            shooter["rank"] = int(shooter_info[0])
            # 球员名称
            shooter["player"] = shooter_info[1]
            # 球队
            shooter["team"] = shooter_info[2]
            # 出场数
            shooter["show_num"] = int(shooter_info[4])
            # 总进球数
            shooter["total_goal"] = int(shooter_info[5])
            # 主场进球
            try:
                shooter["host_goal"] = int(shooter_info[8])
            except:
                shooter["host_goal"] = 0
            # 客场进球
            try:
                shooter["guest_goal"] = int(shooter_info[9])
            except:
                shooter["guest_goal"] = 0
            print(shooter["compname"])
            shooter["name"] = '{}-{}-{}-{}'.format(shooter["compname"], shooter["season"], shooter["team"], shooter["player"])
            yield shooter
