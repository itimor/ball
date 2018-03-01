# -*- coding: utf-8 -*-
# author: itimor

from django.db import models


class SoccerNews(models.Model):
    new_url = models.IntegerField(unique=True, verbose_name=u'链接')
    title = models.CharField(unique=True, max_length=200, blank=True, verbose_name=u'标题')
    rewritten_title = models.CharField(max_length=200, blank=True, verbose_name=u'重写后的标题')
    author = models.CharField(max_length=20, blank=True, verbose_name=u'作者')
    content = models.TextField(blank=True, verbose_name=u'正文')
    publish_time = models.DateTimeField(verbose_name=u'发布时间')
    compname = models.CharField(max_length=20, blank=True, verbose_name=u'赛事名称')

    def __str__(self):
        return self.title


class SoccerMatch(models.Model):
    name = models.CharField(u'联赛名称', unique=True, max_length=100, blank=True)

    def __str__(self):
        return self.name


class FootBallGame(models.Model):
    name = models.CharField(u'比赛名字', unique=True, max_length=100, null=True, blank=True)
    Team1 = models.ForeignKey('FootBallTeam', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'主队',
                              related_name='team1')
    Team2 = models.ForeignKey('FootBallTeam', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'客队',
                              related_name='team2')
    Score1 = models.IntegerField(u'主队得分')
    Score2 = models.IntegerField(u'客队得分')
    MatchDate = models.CharField(u'比赛日期', max_length=100, blank=True)
    MatchTime = models.CharField(u'比赛时间', max_length=100, blank=True)
    league = models.ForeignKey('FootBallLeague', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'联队')
    euro = models.ManyToManyField('FootBallEuropean', null=True, blank=True, verbose_name=u'欧洲赔率')

    def __str__(self):
        return self.name


class FootBallCompany(models.Model):
    name = models.CharField(u'欧赔公司', unique=True, max_length=100, blank=True)
    famous = models.BooleanField(u'主流公司', default=False)
    exchange = models.BooleanField(u'交易所', default=False)

    def __str__(self):
        return self.name


class FootBallEuropean(models.Model):
    title = models.CharField(u'比赛名字', unique=True, max_length=100, null=True, blank=True)
    name = models.ForeignKey('FootBallCompany', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'欧赔公司')
    odds_ini_o1 = models.FloatField(u'欧赔初胜水位', max_length=11)
    odds_ini_o2 = models.FloatField(u'欧赔初平水位', max_length=11)
    odds_ini_o3 = models.FloatField(u'欧赔初负水位', max_length=11)
    odds_ini_return = models.FloatField(u'欧赔初返还率', max_length=11)
    odds_ini_time = models.DateTimeField(u'欧赔初变盘时间', max_length=11)
    odds_new_o1 = models.FloatField(u'欧赔后胜水位', max_length=11)
    odds_new_o2 = models.FloatField(u'欧赔后平水位', max_length=11)
    odds_new_o3 = models.FloatField(u'欧赔后负水位', max_length=11)
    odds_new_return = models.FloatField(u'欧赔后返还率', max_length=11)
    odds_new_time = models.DateTimeField(u'欧赔后变盘时间', max_length=11)
    kelly_ini_e1 = models.FloatField(u'凯利指数初胜水位', max_length=11)
    kelly_ini_e2 = models.FloatField(u'凯利指数初平水位', max_length=11)
    kelly_ini_e3 = models.FloatField(u'凯利指数初负水位', max_length=11)
    kelly_ini_time = models.DateTimeField(u'欧赔初变盘时间', max_length=11)
    kelly_new_e1 = models.FloatField(u'凯利指数后胜水位', max_length=11)
    kelly_new_e2 = models.FloatField(u'凯利指数后平水位', max_length=11)
    kelly_new_e3 = models.FloatField(u'凯利指数后负水位', max_length=11)
    kelly_new_time = models.DateTimeField(u'欧赔后变盘时间', max_length=11)

    def __str__(self):
        return self.title
