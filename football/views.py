# -*- coding: utf-8 -*-
# author: itimor

from football.models import FootBallTeam, FootBallCompany, FootBallEuropean, FootBallGame, FootBallLeague
from rest_framework import viewsets
from football.serializers import (FootBallCompanySerializer, FootBallEuropeanSerializer, FootBallGameSerializer,
                                  FootBallLeagueSerializer, FootBallTeamSerializer)
from football.filters import (FootBallCompanyFilter, FootBallLeagueFilter, FootBallTeamFilter, FootBallEuropeanFilter,
                              FootBallGameFilter)


class FootBallTeamViewSet(viewsets.ModelViewSet):
    queryset = FootBallTeam.objects.all()
    serializer_class = FootBallTeamSerializer
    filter_class = FootBallTeamFilter


class FootBallCompanyViewSet(viewsets.ModelViewSet):
    queryset = FootBallCompany.objects.all()
    serializer_class = FootBallCompanySerializer
    filter_class = FootBallCompanyFilter


class FootBallEuropeanViewSet(viewsets.ModelViewSet):
    queryset = FootBallEuropean.objects.all()
    serializer_class = FootBallEuropeanSerializer
    filter_class = FootBallEuropeanFilter


class FootBallGameViewSet(viewsets.ModelViewSet):
    queryset = FootBallGame.objects.all()
    serializer_class = FootBallGameSerializer
    filter_class = FootBallGameFilter


class FootBallLeagueViewSet(viewsets.ModelViewSet):
    queryset = FootBallLeague.objects.all()
    serializer_class = FootBallLeagueSerializer
    filter_class = FootBallLeagueFilter
