# -*- coding: utf-8 -*-
import scrapy
from soccer_spider.items import Match, NowCompInfo, TeamJifen


class MatchSpider(scrapy.Spider):
    name = "match_spider"

    allowed_domains = ["saishi.caipiao.163.com", "bisai.caipiao.163.com"]
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
        round_list = response.selector.xpath('//div[@class="turnTime clearfix"]/dl/dd/a')
        season = response.selector.xpath(
            '//section[@class="leftNav"]//span[@class="mcSelectBox"]/a[@class="imitateSelect"]/b/text()').extract()[0]
        jifen_url = response.selector.xpath(
            '//section[@class="leftNav"]//div[@class="matchStatBody sign"]/div[@class="lineBottom"][1]/ul/li[2]/a/@href').extract()[
            0]
        yield scrapy.http.Request(url=jifen_url,
                                  callback=lambda response,
                                                  compname=compname,
                                                  season=season: self.crawl_jifen(response, compname, season))
        now_rd = None
        for rd in round_list:
            active = rd.xpath('@class').extract()[0]
            rd_num = int(rd.xpath('text()').extract()[0])
            if active == "active":
                now_rd = rd_num
            url = response.url + "?weekId=" + str(rd_num)
            yield scrapy.http.Request(url=url,
                                      callback=lambda response,
                                                      compname=compname,
                                                      rd=rd_num: self.crawl_round(response, compname, rd))
        now_comp_info = NowCompInfo()
        now_comp_info["compname"] = compname
        now_comp_info["now_rd"] = now_rd
        now_comp_info["season"] = season
        now_comp_info["name"] = '{}-{}'.format(now_comp_info["compname"], now_comp_info["season"])
        yield now_comp_info

    def crawl_jifen(self, response, compname, season):
        jifen_list = response.selector.xpath('//div[@class="listWrap"]/table/tr')
        for j in jifen_list[1:]:
            jifen_info = []
            for info in j.xpath('td//text()').extract():
                if info.strip() != "":
                    jifen_info.append(info.strip())
            team_jifen = TeamJifen()
            # 联赛名称
            team_jifen["compname"] = compname
            # 赛季
            team_jifen["season"] = season
            # 排名
            team_jifen["rank"] = int(jifen_info[0])
            # 队名
            team_jifen["team"] = jifen_info[1]
            # 总场次
            team_jifen["total_match_num"] = int(jifen_info[2])
            # 胜场数
            team_jifen["win_match_num"] = int(jifen_info[3])
            # 平场数
            team_jifen["tie_match_num"] = int(jifen_info[4])
            # 败场数
            team_jifen["lost_match_num"] = int(jifen_info[5])
            # 进球数
            team_jifen["win_goal_num"] = int(jifen_info[6])
            # 失球数
            team_jifen["lost_goal_num"] = int(jifen_info[7])
            # 败场数
            team_jifen["score"] = int(jifen_info[14])
            team_jifen["name"] = '{}-{}-{}'.format(team_jifen["compname"], team_jifen["season"], team_jifen["team"])
            yield team_jifen

    def crawl_round(self, response, compname, rd):
        match_list = response.selector.xpath('//div[@class="listWrap"]/table/tr')
        season = response.selector.xpath(
            '//section[@class="leftNav"]//span[@class="mcSelectBox"]/a[@class="imitateSelect"]/b/text()').extract()[0]
        for m in match_list:
            match_info = m.xpath('td//text()').extract()
            url = m.xpath('td[last()]/a/@href').extract()[0]
            output = []
            for info in match_info:
                if info.strip() == "":
                    continue
                output.append(info.strip().replace("\r\n", ""))
            match = Match()
            match["compname"] = compname
            match["rd"] = rd
            match["match_date"] = "20" + output[0] + ":00"
            match["host_team"] = output[1].strip().split(')')[1].strip()
            if len(output[2].strip().split(':')) != 2:
                match["status"] = "pending"
                match["host_goal"] = ""
                match["guest_goal"] = ""
            else:
                match["status"] = "end"
                match["host_goal"] = output[2].strip().split(':')[0].strip()
                match["guest_goal"] = output[2].strip().split(':')[1].strip()
            match["guest_team"] = output[3].strip().split('(')[0].strip()
            match["season"] = season
            match["match_url"] = url
            match["name"] = '{}-{}-{}'.format(match["compname"], match["host_team"], match["guest_team"])
            yield match