# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from soccer.models import (SoccerNews, NowCompInfo, SoccerTeamJifen, SoccerShooter, SoccerMatch, SoccerMatchAsia,
                           SoccerMatchEurope)
from soccer.serializers import (SoccerNewsSerializer, NowCompInfoSerializer, SoccerTeamJifenSerializer,
                                SoccerShooterSerializer, SoccerMatchSerializer, SoccerMatchAsiaSerializer,
                                SoccerMatchEuropeSerializer)


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


class SoccerMatchAsiaViewSet(viewsets.ModelViewSet):
    queryset = SoccerMatchAsia.objects.all()
    serializer_class = SoccerMatchAsiaSerializer


class SoccerMatchEuropeViewSet(viewsets.ModelViewSet):
    queryset = SoccerMatchEurope.objects.all()
    serializer_class = SoccerMatchEuropeSerializer
