# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from . import settings
from PIL import Image
import math


class NewsPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["news_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.News'>":
            print(item["url"], dict(item))
        return item

class MatchPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["match_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.Match'>":
            print(item["url"], dict(item))
        elif str(item.__class__) == "<class 'soccer_spider.items.NowCompInfo'>":
            print(item["compname"], dict(item))
        elif str(item.__class__) == "<class 'soccer_spider.items.TeamJifen'>":
            print(item["compname"], item["team"], item["season"], dict(item))
        return item


class ShooterPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["shooter_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.Shooter'>":
            print(item["compname"], item["player"], item["season"], dict(item))


class LotteryPipeline(object):
    def process_item(self, item, spider):
        if spider.name not in ["lottery_spider"]:
            return item
        if str(item.__class__) == "<class 'soccer_spider.items.MatchAsiaLottery'>":
            print(item["compname"],
                  item["season"],
                  item["rd"],
                  item["host_team"],
                  item["guest_team"],
                  item["bookmaker"], dict(item))
        elif str(item.__class__) == "<class 'soccer_spider.items.MatchEuropeLottery'>":
            print(item["compname"],
                  item["season"],
                  item["rd"],
                  item["host_team"],
                  item["guest_team"],
                  item["bookmaker"], dict(item))
