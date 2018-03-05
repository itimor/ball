# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from soccer.models import *


class News(DjangoItem):
    django_model = SoccerNews


class Match(DjangoItem):
    django_model = SoccerMatch


# 当前各大比赛的状态
class NowCompInfo(DjangoItem):
    django_model = NowCompInfo


# 当前某个队伍积分
class TeamJifen(DjangoItem):
    django_model = SoccerTeamJifen


# 射手
class Shooter(DjangoItem):
    django_model = SoccerShooter


class MatchEuropeLottery(DjangoItem):
    django_model = SoccerMatchEurope
