'''2023年12月17日14:57:16, ac上抄的'''
from operator import add

'''
2024年8月24日19:32:38, 别用exit() - 段错误 !!!!   奇怪的问题...
'''


import typing
from math import sqrt, log, gcd, inf, comb, lcm
from string import ascii_lowercase

'''cf的 py3.8 没有cache'''
# from sortedcontainers import *  #cf没有
# from math import *    #pow !
from heapq import *
from collections import *
from bisect import *
from itertools import *
from functools import lru_cache
from copy import *
import sys

# sys.setrecursionlimit(2147483647)  #2024年8月28日14:37:18,  很容易mle...

def main():
    # from math import gcd, floor, ceil, sqrt, isclose, pi, sin, cos, tan, asin, acos, atan, atan2, hypot, degrees, radians, log, log2, log10
    # from heapq import heappush, heappop, heapify, heappushpop, heapreplace, nlargest, nsmallest
    # from itertools import count, cycle, accumulate, chain, groupby, islice, product, permutations, combinations, combinations_with_replacement
    # inf = 3074457345618258602  #注意一下
    mod = 998244353  #ac

    def py():
        print("YES")  # ac严谨
    def pn():
        print("NO")

    # 按照输入的行, 一行一行的取值,每行得到的值都是列表.
    input = lambda: sys.stdin.readline().rstrip()  ##一个是神奇的卡点...
    il = lambda: list(map(int, input().split()))  # 单个 n = i()[0]  列表 l = i() #input_list
    ix = lambda: il()[0]  # 单个数字  #input_x
    iis = lambda: input().split()
    # 列表输出数字串, 例子 [1,2,3] printout: 1 2 3
    # pl 直接用  print(*list) 就完事了...
    # pl = lambda a: print(" ".join(map(str, a)))  # print_list
    en = enumerate

    def pairwise(a):
        ans = []
        n = len(a)
        for i in range(n - 1):
            ans += (a[i], a[i + 1]),
        return ans

    '''代码'''

    # mod ↑


    # 2024年7月28日18:00:39, 太原始 3.7.  无 .bit_count()
    times = 1  # 0有t, 1无t
    if not times:
        times = ix()
    for _ in range(times):
        n,m, k = il()
        S = input()
        T = input()
        s1 = list(map(int, S))
        s2 = list(map(int, T))

        cur = sum(s1[:k])
        v1mi = v1ma = cur
        for i in range(n - k):
            cur -= s1[i]
            cur+= s1[i + k]
            v1mi = min(v1mi, cur)
            v1ma = max(v1ma, cur)

        cur = sum(s2[:k])
        v2mi = v2ma = cur
        for i in range(m - k):
            cur -= s2[i]
            cur+= s2[i + k]
            v2mi = min(v2mi, cur)
            v2ma = max(v2ma, cur)

        def ff(x, y):
            return (k - x) * y + x * (k - y)

        print(max(ff(v1mi, v2mi), ff(v1ma, v2ma), ff(v1mi, v2ma), ff(v1ma, v2mi)))



        # ↑  code

    ''''''


main()

'''test

import os
os.system("python 这我的板子-蓝桥.py <in.in")

'''