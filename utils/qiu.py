# -*- coding: utf-8 -*-
# author: itimor

import requests
import re
import json

dataturl = 'http://sports.sina.com.cn/data/caculator/sfc/'

s_qi = 16117
e_qi = 16198

he_url = '{}{}.html'.format(dataturl, s_qi)
html_data = requests.get(he_url).text

repr = re.compile('\?m_id=(\d+)', re.M)
s = repr.findall(html_data)

b_url = 'http://match.lottery.sina.com.cn/football/ai/europe?m_id='
b_ids = list(set(s))

# head_data
head_url = 'http://odds.sports.sina.com.cn/liveodds/getMatchInfo?m_id={}&format=json'.format(3642573)
# euro_data
euro_url = 'http://platform.sina.com.cn/sports_all/client_api?app_key=3979320659&_sport_t_=Odds&_sport_a_=euroIniNewData&id={}'.format(
    3642573)

head_html = requests.get(head_url).text
euro_html = requests.get(euro_url).text

head_data = json.loads(head_html)['result']['data']
euro_data = json.loads(head_html)['result']['data']

# Team
league_url = 'http://47.90.82.112:8000/api/footballleague/'
team_url = 'http://47.90.82.112:8000/api/footballteam/'
game_url = 'http://47.90.82.112:8000/api/footballgame/'

# Euro


game_name = head_data['Team1'] + '-' + head_data['Team2'] + '-' + head_data['MatchDate']
league_data = {"name": head_data['ln']}
team_data1 = {"teamId": head_data['Team1Id'], "name": head_data['Team1en'], "cnname": head_data['Team1'],
              "league": head_data['ln']}
team_data2 = {"teamId": head_data['Team2Id'], "name": head_data['Team2en'], "cnname": head_data['Team2'],
              "league": head_data['ln']}
game_data = {"name": '', "Team1": head_data['Team1'], "Team2": head_data['Team2'], "Score1": head_data['Score1'],
             "Score2": head_data['Score2'], "MatchDate": head_data["MatchDate"], "MatchTime": head_data['MatchTime'],
             "league": head_data['ln'], "euro": [game_name]}

league = requests.post(league_url, data=league_data)
if league.status_code == 200:
    print("sucess")
else:
    print({'code':league.status_code,'msg':json.loads(league.text)['name'][0]})