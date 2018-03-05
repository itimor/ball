# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from soccer.models import SoccerNews, NowCompInfo, SoccerTeamJifen, SoccerShooter, SoccerMatch, SoccerMatchEurope
from soccer.serializers import (SoccerNewsSerializer, NowCompInfoSerializer, SoccerTeamJifenSerializer,
                                SoccerShooterSerializer, SoccerMatchSerializer, SoccerMatchEuropeSerializer)


class SoccerNewsViewSet(viewsets.ModelViewSet):
    queryset = SoccerNews.objects.all()
    serializer_class = SoccerNewsSerializer


class NowCompInfoViewSet(viewsets.ModelViewSet):
    queryset = NowCompInfo.objects.all()
    serializer_class = NowCompInfoSerializer


class SoccerTeamJifenViewSet(viewsets.ModelViewSet):
    queryset = SoccerTeamJifen.objects.all()
    serializer_class = SoccerTeamJifenSerializer


class SoccerShooterViewSet(viewsets.ModelViewSet):
    queryset = SoccerShooter.objects.all()
    serializer_class = SoccerShooterSerializer


class SoccerMatchViewSet(viewsets.ModelViewSet):
    queryset = SoccerMatch.objects.all()
    serializer_class = SoccerMatchSerializer


class SoccerMatchEuropeViewSet(viewsets.ModelViewSet):
    queryset = SoccerMatchEurope.objects.all()
    serializer_class = SoccerMatchEuropeSerializer
