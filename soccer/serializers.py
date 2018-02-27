# -*- coding: utf-8 -*-
# author: itimor

from soccer.models import FootBallTeam, FootBallCompany, FootBallEuropean, FootBallGame, FootBallLeague
from rest_framework import serializers


class FootBallTeamSerializer(serializers.ModelSerializer):
    league = serializers.SlugRelatedField(queryset=FootBallLeague.objects.all(), slug_field='name')

    class Meta:
        model = FootBallTeam
        fields = ('url', 'id', 'teamId', 'name', 'cnname', 'league')


class FootBallCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = FootBallCompany
        fields = ('url', 'id', 'name', 'famous', 'exchange')


class FootBallEuropeanSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(queryset=FootBallCompany.objects.all(), slug_field='name')

    class Meta:
        model = FootBallEuropean
        fields = ('url', 'id', 'title', 'name', 'odds_ini_o1', 'odds_ini_o2', 'odds_ini_o3', 'odds_ini_return',
            'odds_ini_time', 'odds_new_o1', 'odds_new_o2', 'odds_new_o3', 'odds_new_return', 'odds_new_time',
            'kelly_ini_e1', 'kelly_ini_e2', 'kelly_ini_e3', 'kelly_ini_time', 'kelly_new_e1', 'kelly_new_e2',
            'kelly_new_e3', 'kelly_new_time',)


class FootBallGameSerializer(serializers.ModelSerializer):
    league = serializers.SlugRelatedField(queryset=FootBallLeague.objects.all(), slug_field='name')
    euro = serializers.SlugRelatedField(many=True, queryset=FootBallEuropean.objects.all(), slug_field='title')
    Team1 = serializers.SlugRelatedField(queryset=FootBallTeam.objects.all(), slug_field='cnname')
    Team2 = serializers.SlugRelatedField(queryset=FootBallTeam.objects.all(), slug_field='cnname')
    class Meta:
        model = FootBallGame
        fields = ('url', 'id', 'Team1', 'Team2', 'Score1', 'Score2', 'MatchDate', 'MatchTime', 'league', 'euro')


class FootBallLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootBallLeague
        fields = ('url', 'id', 'name')
