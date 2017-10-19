# -*- coding: utf-8 -*-
# author: itimor

from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, GroupViewSet, RoleViewSet
from football.views import (FootBallCompanyViewSet, FootBallEuropeanViewSet, FootBallGameViewSet, FootBallTeamViewSet,
                            FootBallLeagueViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'footballcompany', FootBallCompanyViewSet)
router.register(r'footballeuropean', FootBallEuropeanViewSet)
router.register(r'footballgame', FootBallGameViewSet)
router.register(r'footballteam', FootBallTeamViewSet)
router.register(r'footballleague', FootBallLeagueViewSet)
