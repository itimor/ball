# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from soccer.models import *


class NewsPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["news_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.News'>":
            SoccerNews.objects.update_or_create(new_url=item["new_url"], title=item["title"], defaults=item)
        return item


class MatchPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["match_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.Match'>":
            SoccerMatch.objects.update_or_create(match_url=item["match_url"], name=item["name"], defaults=item)
        elif str(item.__class__) == "<class 'soccer_spider.items.NowCompInfo'>":
            NowCompInfo.objects.update_or_create(name=item["name"], compname=item["compname"], defaults=item)
        elif str(item.__class__) == "<class 'soccer_spider.items.TeamJifen'>":
            SoccerTeamJifen.objects.update_or_create(name=item["name"], compname=item["compname"], defaults=item)
        return item


class ShooterPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["shooter_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.Shooter'>":
            SoccerShooter.objects.update_or_create(name=item["name"], compname=item["compname"], defaults=item)


class LotteryPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["lottery_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.MatchEuropeLottery'>":
            SoccerMatchEurope.objects.update_or_create(name=item["name"], bookmaker=item["bookmaker"], defaults=item)
