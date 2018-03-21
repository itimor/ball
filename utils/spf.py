# -*- coding: utf-8 -*-
# author: itimor


def spf(h, g):
    """
    :param h: 主队进球数
    :param g: 客队进球数
    :return: s|p|f
    """
    if h > g:
        return "s"
    elif h == g:
        return "p"
    else:
        return "f"
