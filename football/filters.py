# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from football.models import FootBallTeam, FootBallCompany, FootBallEuropean, FootBallGame, FootBallLeague


class FootBallTeamFilter(filters.FilterSet):
    class Meta:
        model = FootBallTeam
        fields = {
            'name': ['exact', 'contains'],
            'cnname': ['exact', 'contains'],
            'league__name': ['exact']
        }


class FootBallCompanyFilter(filters.FilterSet):
    class Meta:
        model = FootBallCompany
        fields = {
            'name': ['exact', 'contains'],
        }


class FootBallLeagueFilter(filters.FilterSet):
    class Meta:
        model = FootBallLeague
        fields = {
            'name': ['exact', 'contains'],
        }


class FootBallEuropeanFilter(filters.FilterSet):
    class Meta:
        model = FootBallEuropean
        fields = {
            'title': ['exact', 'contains'],
        }


class FootBallGameFilter(filters.FilterSet):
    class Meta:
        model = FootBallGame
        fields = {
            'name': ['exact', 'contains'],
        }
