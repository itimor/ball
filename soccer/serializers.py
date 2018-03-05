# -*- coding: utf-8 -*-
# author: itimor

from soccer.models import (SoccerNews, NowCompInfo, SoccerTeamJifen, SoccerShooter, SoccerMatch, SoccerMatchAsia,
                           SoccerMatchEurope)
from rest_framework import serializers


class SoccerNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerNews
        fields = ('url', 'id', 'new_url', 'title', 'author', 'content', 'publish_time', 'compname')


class NowCompInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowCompInfo
        fields = ('url', 'id', 'name', 'compname', 'now_rd', 'season')


class SoccerTeamJifenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerTeamJifen
        fields = (
            'url', 'id', 'name', 'compname', 'season', 'team', 'total_match_num', 'win_match_num', 'lost_match_num',
            'tie_match_num', 'win_goal_num', 'lost_goal_num', 'score')


class SoccerShooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerShooter
        fields = (
            'url', 'id', 'name', 'compname', 'season', 'team', 'player', 'rank', 'show_num', 'total_goal', 'host_goal',
            'tie_match_num', 'guest_goal')


class SoccerMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerMatch
        fields = (
            'url', 'id', 'name', 'compname', 'status', 'season', 'rd', 'match_date', 'host_team', 'host_goal',
            'guest_team',
            'guest_goal', 'match_url')


class SoccerMatchAsiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerMatchAsia
        fields = (
            'url', 'id', 'name', 'match', 'bookmaker', 'lottery_type', 'initial_host_shuiwei', 'initial_guest_shuiwei',
            'initial_pankou')


class SoccerMatchEuropeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerMatchEurope
        fields = (
            'url', 'id', 'name', 'match', 'bookmaker', 'lottery_type', 'initial_win', 'initial_tie', 'initial_lost')
