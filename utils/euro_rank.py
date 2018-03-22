# -*- coding: utf-8 -*-
# author: itimor

from soccer.models import SoccerNews, NowCompInfo, SoccerTeamJifen, SoccerShooter, SoccerMatch, SoccerMatchEurope
from utils.spf import spf
from utils.rank_socer import rank_socer

matchs = SoccerMatch.objects.all()

euro_ranks = dict()
n = 100
for match in matchs:
    spf_count = spf(match.host_goal, match.guest_goal)
    euros = SoccerMatchEurope.objects.filter(match=match.name)
    for euro in euros:
        rank_socer_count = rank_socer(euro.initial_win, euro.initial_tie, euro.initial_lost, spf_count)
        euro_ranks[euro.bookmaker] = n + rank_socer_count

sorted(euro_ranks.items(), key=lambda item: item[1])[-3:]

'''
5Dimes
Intralot
Betsson Sportsbook
'''
