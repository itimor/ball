# -*- coding: utf-8 -*-
# author: itimor

class Solution(object):
    def reverse(self, x):
        if str(x)[0] == '-':
            return int('-' + str(x)[:0:-1])
        return int(str(x)[::-1])

if __name__ == '__main__':
    x = 1534236469
    aaa = Solution()
    print(aaa.reverse(x))