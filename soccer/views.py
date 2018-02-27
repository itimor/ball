# -*- coding: utf-8 -*-
# author: itimor

from soccer.models import FootBallTeam, FootBallCompany, FootBallEuropean, FootBallGame, FootBallLeague
from rest_framework import viewsets
from soccer.serializers import (FootBallCompanySerializer, FootBallEuropeanSerializer, FootBallGameSerializer,
                                  FootBallLeagueSerializer, FootBallTeamSerializer)


class FootBallTeamViewSet(viewsets.ModelViewSet):
    queryset = FootBallTeam.objects.all()
    serializer_class = FootBallTeamSerializer


class FootBallCompanyViewSet(viewsets.ModelViewSet):
    queryset = FootBallCompany.objects.all()
    serializer_class = FootBallCompanySerializer


class FootBallEuropeanViewSet(viewsets.ModelViewSet):
    queryset = FootBallEuropean.objects.all()
    serializer_class = FootBallEuropeanSerializer


class FootBallGameViewSet(viewsets.ModelViewSet):
    queryset = FootBallGame.objects.all()
    serializer_class = FootBallGameSerializer


class FootBallLeagueViewSet(viewsets.ModelViewSet):
    queryset = FootBallLeague.objects.all()
    serializer_class = FootBallLeagueSerializer
