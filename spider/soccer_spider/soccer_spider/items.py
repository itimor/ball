# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class News(scrapy.Item):
    # url
    url = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 重写后的标题
    rewritten_title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 正文
    content = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 赛事名称
    compname = scrapy.Field()


class Match(scrapy.Item):
    # pending running end
    status = scrapy.Field()
    # 英超、欧冠、德甲、意甲、法甲、西甲、中超
    compname = scrapy.Field()
    # 赛季
    season = scrapy.Field()
    # 轮次
    rd = scrapy.Field()
    # 比赛时间
    match_date = scrapy.Field()
    # 主队
    host_team = scrapy.Field()
    # 客队
    guest_team = scrapy.Field()
    # 主队数据
    # 进球数
    host_goal = scrapy.Field()

    # 客队数据
    # 进球数
    guest_goal = scrapy.Field()
    # url
    url = scrapy.Field()


# 当前各大比赛的状态
class NowCompInfo(scrapy.Item):
    compname = scrapy.Field()
    now_rd = scrapy.Field()
    season = scrapy.Field()


# 当前某个队伍积分
class TeamJifen(scrapy.Item):
    # 英超、意甲
    compname = scrapy.Field()
    # 赛季
    season = scrapy.Field()
    # 队名
    team = scrapy.Field()
    # 排名
    rank = scrapy.Field()
    # 总场数
    total_match_num = scrapy.Field()
    # 胜场数
    win_match_num = scrapy.Field()
    # 败场数
    lost_match_num = scrapy.Field()
    # 平场数
    tie_match_num = scrapy.Field()
    # 进球数
    win_goal_num = scrapy.Field()
    # 失球数
    lost_goal_num = scrapy.Field()
    # 积分
    score = scrapy.Field()


# 射手
class Shooter(scrapy.Item):
    # 联赛名称
    compname = scrapy.Field()
    # 赛季
    season = scrapy.Field()
    # 排名
    rank = scrapy.Field()
    # 球员名称
    player = scrapy.Field()
    # 球队
    team = scrapy.Field()
    # 出场数
    show_num = scrapy.Field()
    # 总进球数
    total_goal = scrapy.Field()
    # 主场进球
    host_goal = scrapy.Field()
    # 客场进球
    guest_goal = scrapy.Field()


class MatchAsiaLottery(scrapy.Item):
    # 英超、欧冠、德甲、意甲、法甲、西甲、中超
    compname = scrapy.Field()
    # 赛季
    season = scrapy.Field()
    # 轮次
    rd = scrapy.Field()
    # 比赛时间
    match_date = scrapy.Field()
    # 主队
    host_team = scrapy.Field()
    # 客队
    guest_team = scrapy.Field()
    # 初盘主队水位
    initial_host_shuiwei = scrapy.Field()
    # 初盘客队水位
    initial_guest_shuiwei = scrapy.Field()
    # 初盘盘口
    initial_pankou = scrapy.Field()
    # 博彩公司
    bookmaker = scrapy.Field()
    # asia europe
    lottery_type = scrapy.Field()


class MatchEuropeLottery(scrapy.Item):
    # 英超、欧冠、德甲、意甲、法甲、西甲、中超
    compname = scrapy.Field()
    # 赛季
    season = scrapy.Field()
    # 轮次
    rd = scrapy.Field()
    # 比赛时间
    match_date = scrapy.Field()
    # 主队
    host_team = scrapy.Field()
    # 客队
    guest_team = scrapy.Field()
    # 初盘胜
    initial_win = scrapy.Field()
    # 初盘平
    initial_tie = scrapy.Field()
    # 初盘负
    initial_lost = scrapy.Field()
    # 博彩公司
    bookmaker = scrapy.Field()
    # asia europe
    lottery_type = scrapy.Field()
