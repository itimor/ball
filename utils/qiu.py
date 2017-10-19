# -*- coding: utf-8 -*-
# author: itimor

import requests
import re
from bs4 import BeautifulSoup

dataturl = 'http://sports.sina.com.cn/data/caculator/sfc/'

s_qi = 16117
e_qi = 16198


he_url = '{}{}.html'.format(dataturl,s_qi)
html_data = requests.get(he_url).text

repr = re.compile('\?m_id=(\d+)',re.M)
s = repr.findall(html_data)

b_url = 'http://match.lottery.sina.com.cn/football/ai/europe?m_id='
b_ids = list(set(s))

b_he_url =  '{}{}'.format(b_url,3642573)
b_html = requests.get(b_he_url).text
soup = BeautifulSoup(b_html, 'html.parser')
print(soup)  #打印源码发现展示数据用的ajax
#F12查找js发现真正的数据url
#head_data
real_url = 'http://odds.sports.sina.com.cn/liveodds/getMatchInfo?m_id={}&format=json'.format(3642573)
#欧赔
ou_url = 'http://platform.sina.com.cn/sports_all/client_api?app_key=3979320659&_sport_t_=Odds&_sport_a_=euroIniNewData&id={}'.format(3642573)





