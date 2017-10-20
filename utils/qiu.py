# -*- coding: utf-8 -*-
# author: itimor

import requests
import re
import json

dataturl = "http://sports.sina.com.cn/data/caculator/sfc/"

s_qi = 16117
e_qi = 16198

he_url = "{}{}.html".format(dataturl, s_qi)
html_data = requests.get(he_url).text

repr = re.compile("\?m_id=(\d+)", re.M)
s = repr.findall(html_data)

b_url = "http://match.lottery.sina.com.cn/football/ai/europe?m_id="
b_ids = list(set(s))

# head_data
head_url = "http://odds.sports.sina.com.cn/liveodds/getMatchInfo?m_id={}&format=json".format(3642573)
# euro_data
euro_url = "http://platform.sina.com.cn/sports_all/client_api?app_key=3979320659&_sport_t_=Odds&_sport_a_=euroIniNewData&id={}".format(
    3642573)

head_html = requests.get(head_url).text
euro_html = requests.get(euro_url).text

head_data = json.loads(head_html)["result"]["data"]
euro_datas = json.loads(euro_html)["result"]["data"]

# Team
league_url = "http://47.90.82.112:8000/api/footballleague/"
team_url = "http://47.90.82.112:8000/api/footballteam/"
game_url = "http://47.90.82.112:8000/api/footballgame/"

# Euro
euro_url = "http://47.90.82.112:8000/api/footballeuropean/"
company_url = "http://47.90.82.112:8000/api/footballcompany/"

league_data = {"name": head_data["ln"]}
team_data1 = {"teamId": head_data["Team1Id"], "name": head_data["Team1en"], "cnname": head_data["Team1"],
              "league": head_data["ln"]}
team_data2 = {"teamId": head_data["Team2Id"], "name": head_data["Team2en"], "cnname": head_data["Team2"],
              "league": head_data["ln"]}
game_names = []
for euro_data in euro_datas:
    #company
    is_famous = ("false","true")[euro_data["if_famous"] is "0"]      #python三元表达式，条件成立会执行第二个
    if_exchange = ("false","true")[euro_data["if_exchange"] is "0"]
    company_data = {"name":euro_data["name"],"famous":is_famous,"exchange":if_exchange,}
    company = requests.post(company_url, data=company_data)
    if company.status_code == 200:
        print("company sucess")
    else:
        print({"code": company.status_code, "msg": json.loads(company.text)["name"][0]})

    #euro
    game_name = head_data["Team1"] + "-" + head_data["Team2"] + "-" + head_data["MatchDate"] + "-" + euro_data["name"]
    game_names.append(game_name)
    euro_dat = {
    "title": game_name,
    "name": euro_data["name"],
    "odds_ini_o1": euro_data["odds"]["ini"]["ol"],
    "odds_ini_o2": euro_data["odds"]["ini"]["o2"],
    "odds_ini_o3": euro_data["odds"]["ini"]["o3"],
    "odds_ini_return": euro_data["odds"]["ini"]["return"],
    "odds_ini_time": euro_data["odds"]["ini"]["change_time"],
    "odds_new_o1": euro_data["odds"]["new"]["ol"],
    "odds_new_o2": euro_data["odds"]["new"]["o2"],
    "odds_new_o3": euro_data["odds"]["new"]["o3"],
    "odds_new_return": euro_data["odds"]["new"]["return"],
    "odds_new_time": euro_data["odds"]["new"]["change_time"],
    "kelly_ini_e1": euro_data["kelly"]["ini"]["el"],
    "kelly_ini_e2": euro_data["kelly"]["ini"]["e2"],
    "kelly_ini_e3": euro_data["kelly"]["ini"]["e33"],
    "kelly_ini_time": euro_data["kelly"]["ini"]["change_time"],
    "kelly_new_e1": euro_data["kelly"]["new"]["el"],
    "kelly_new_e2": euro_data["kelly"]["new"]["e2"],
    "kelly_new_e3": euro_data["kelly"]["new"]["e33"],
    "kelly_new_time": euro_data["kelly"]["new"]["change_time"]
}
    euro = requests.post(euro_url, data=euro_dat)
    if euro.status_code == 200:
        print("euro sucess")
    else:
        print({"code": euro.status_code, "msg": json.loads(euro.text)["name"][0]})

#
# league = requests.post(league_url, data=league_data)
# if league.status_code == 200:
#     print("league sucess")
# else:
#     print({"code":league.status_code,"msg":json.loads(league.text)["name"][0]})
#
# game_data = {"Team1": head_data["Team1"], "Team2": head_data["Team2"], "Score1": head_data["Score1"],
#              "Score2": head_data["Score2"], "MatchDate": head_data["MatchDate"], "MatchTime": head_data["MatchTime"],
#              "league": head_data["ln"], "euro": game_names}