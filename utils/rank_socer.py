# -*- coding: utf-8 -*-
# author: itimor
# desc: 计算各欧赔公司的赔率胜负概率与实际赛果有出入时，计算加分还是扣分

from .gailv import gvcount


def rank_socer(s, p, f, real):
    """
    s: 胜的赔率
    p: 胜的赔率
    z: 胜的赔率
    real: 赛果 - s|p|f
    """
    # 计算胜平负概率
    d = gvcount(s, p, f)
    dc = dict()
    dc['s'] = d[0]
    dc['p'] = d[1]
    dc['f'] = d[2]
    d_max = max(dc['s'], dc['p'], dc['f'])
    dd = dict()
    if d_max == dc['s']:
        dd['d_real'] = 's'
        dd['d_socer'] = dc['s']
    elif d_max == dc['p']:
        dd['d_real'] = 'p'
        dd['d_socer'] = dc['p']
    else:
        dd['d_real'] = 'f'
        dd['d_socer'] = dc['f']

    if dd['d_real'] == real:
        return 1
    else:
        diff = dd['d_socer'] - dc[real]
        if abs(diff) > 20.998:
            return -2
        else:
            return -1


if __name__ == '__main__':
    x = 2.10
    y = 3.40
    z = 3.90
    print(rank_socer(x, y, z, 'f'))
