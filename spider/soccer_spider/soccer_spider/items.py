# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from soccer.models import *


class News(DjangoItem):
    django_model = SoccerNews


class Match(scrapy.Item):
    django_model = SoccerMatch


# 当前各大比赛的状态
class NowCompInfo(scrapy.Item):
    django_model = NowCompInfo


# 当前某个队伍积分
class TeamJifen(scrapy.Item):
    django_model = SoccerTeamJifen


# 射手
class Shooter(scrapy.Item):
    django_model = SoccerShooter


class MatchEuropeLottery(scrapy.Item):
    django_model = SoccerMatchEurope
