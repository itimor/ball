# -*- coding: utf-8 -*-
# author: itimor
# desc: 计算赔率代表的胜负概率


def gvcount(x, y, z):
    total = 1 / x + 1 / y + 1 / z
    x_ = 1 / x / total * 100
    y_ = 1 / y / total * 100
    z_ = 1 / z / total * 100
    return [x_, y_, z_]


if __name__ == '__main__':
    x = 2.10
    y = 3.40
    z = 3.90
    print(gvcount(x, y, z))
