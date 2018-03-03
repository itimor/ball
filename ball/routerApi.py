# -*- coding: utf-8 -*-
# author: itimor

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
from users.views import UserViewSet, GroupViewSet, RoleViewSet

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)

from soccer.views import (SoccerNewsViewSet, NowCompInfoViewSet, SoccerTeamJifenViewSet, SoccerShooterViewSet,
                          SoccerMatchViewSet, SoccerMatchAsiaViewSet, SoccerMatchEuropeViewSet)

router.register(r'soccernews', SoccerNewsViewSet)
router.register(r'nowcompinfos', NowCompInfoViewSet)
router.register(r'soccerteamjifens', SoccerTeamJifenViewSet)
router.register(r'soccershooters', SoccerShooterViewSet)
router.register(r'soccermatchs', SoccerMatchViewSet)
router.register(r'soccermatchasias', SoccerMatchAsiaViewSet)
router.register(r'soccermatcheuros', SoccerMatchEuropeViewSet)
