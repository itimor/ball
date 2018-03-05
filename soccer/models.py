# -*- coding: utf-8 -*-
# author: itimor

from django.db import models


class SoccerNews(models.Model):
    new_url = models.CharField(unique=True, max_length=200, verbose_name=u'链接')
    title = models.CharField(unique=True, max_length=200, blank=True, verbose_name=u'标题')
    author = models.CharField(max_length=20, blank=True, verbose_name=u'作者')
    content = models.TextField(blank=True, verbose_name=u'正文')
    publish_time = models.DateTimeField(verbose_name=u'发布时间')
    compname = models.CharField(max_length=20, blank=True, verbose_name=u'联赛名称')

    def __str__(self):
        return self.title


class NowCompInfo(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    compname = models.CharField(max_length=20, blank=True, verbose_name=u'联赛名称')
    now_rd = models.CharField(max_length=20, blank=True, verbose_name=u'当前轮次')
    season = models.CharField(max_length=100, blank=True, verbose_name=u'当前赛季')

    def __str__(self):
        return self.name


class SoccerTeamJifen(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    compname = models.CharField(max_length=20, blank=True, verbose_name=u'联赛名称')
    season = models.CharField(max_length=20, blank=True, verbose_name=u'赛季')
    team = models.CharField(max_length=100, blank=True, verbose_name=u'队名')
    rank = models.IntegerField(blank=True, verbose_name=u'排名')
    total_match_num = models.IntegerField(blank=True, verbose_name=u'总场数')
    win_match_num = models.IntegerField(blank=True, null=True, verbose_name=u'胜场数')
    lost_match_num = models.IntegerField(blank=True, verbose_name=u'败场数')
    tie_match_num = models.IntegerField(blank=True, null=True, verbose_name=u'平场数')
    win_goal_num = models.IntegerField(blank=True, null=True, verbose_name=u'进球数')
    lost_goal_num = models.IntegerField(blank=True, null=True, verbose_name=u'失球数')
    score = models.IntegerField(blank=True, null=True, verbose_name=u'积分')

    def __str__(self):
        return self.name


class SoccerShooter(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    compname = models.CharField(max_length=20, blank=True, verbose_name=u'联赛名称')
    season = models.CharField(max_length=20, blank=True, verbose_name=u'赛季')
    team = models.CharField(max_length=100, blank=True, verbose_name=u'队名')
    player = models.CharField(max_length=100, blank=True, verbose_name=u'球员名称')
    rank = models.IntegerField(blank=True, verbose_name=u'排名')
    show_num = models.IntegerField(blank=True, verbose_name=u'出场数')
    total_goal = models.IntegerField(blank=True, verbose_name=u'总进球数')
    host_goal = models.IntegerField(blank=True, verbose_name=u'主场进球')
    tie_match_num = models.IntegerField(blank=True, verbose_name=u'客场进球')
    guest_goal = models.IntegerField(blank=True, verbose_name=u'进球数')

    def __str__(self):
        return self.name


Match_Status = {
    0: 'pending',
    1: 'running',
    2: 'end',
}


class SoccerMatch(models.Model):
    match_url = models.CharField(unique=True, max_length=200, verbose_name=u'链接')
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    compname = models.CharField(max_length=20, blank=True, verbose_name=u'联赛名称')
    status = models.CharField(max_length=3, choices=Match_Status.items(), default=0, verbose_name=u'状态')
    season = models.CharField(max_length=20, blank=True, verbose_name=u'赛季')
    rd = models.CharField(max_length=20, blank=True, verbose_name=u'轮次')
    match_date = models.CharField(max_length=100, blank=True, verbose_name=u'比赛时间')
    host_team = models.CharField(max_length=100, blank=True, verbose_name=u'主队')
    host_goal = models.CharField(max_length=100, blank=True, verbose_name=u'主队进球数')
    guest_team = models.CharField(max_length=100, blank=True, verbose_name=u'客队')
    guest_goal = models.CharField(max_length=100, blank=True, verbose_name=u'客队进球数')

    def __str__(self):
        return self.name


class SoccerMatchEurope(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    match = models.ForeignKey(SoccerMatch, on_delete=models.CASCADE, verbose_name=u'比赛')
    bookmaker = models.CharField(max_length=20, blank=True, verbose_name=u'博彩公司')
    lottery_type = models.CharField(default='europe', max_length=10, verbose_name=u'类型')
    initial_win = models.FloatField(u'初盘胜', max_length=11)
    initial_tie = models.FloatField(u'初盘平', max_length=11)
    initial_lost = models.FloatField(u'初盘负', max_length=11)

    def __str__(self):
        return self.name
