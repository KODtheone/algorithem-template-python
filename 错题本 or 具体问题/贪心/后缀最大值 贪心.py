'''
2025年1月30日11:53:37  https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/01/0130/solution/cf1257d.md
杨潇的题解
https://codeforces.com/contest/1257/problem/D



'''


'''
核心思路 1,  后缀最大值  算出连续杀n个怪 需要的最小power
2, 遍历m,  记录走过了多少怪,  贪心 ,当无法继续走时 , 就是新一天
'''



from math import sqrt, log, gcd, inf
from operator import ixor, and_
from random import randint
from string import ascii_lowercase
from typing import List
from heapq import *
from collections import *
from bisect import *
from itertools import *
from functools import cache  # 2024年7月24日08:40:49, cf可以cache了 pypy3.10
from copy import *
import sys


# from sortedcontainers import SortedList   # 2024年7月29日23:01:22, 这个mod还是没有...

sys.setrecursionlimit(5005)
# sys.setrecursionlimit(150000)  # 2024年7月27日14:34:16,  可能导致mle https://codeforces.com/contest/1996/problem/C
input = lambda: sys.stdin.readline().rstrip()
ip = input
il = lambda: list(map(int, input().split()))
ix = lambda: il()[0]
iis = lambda: input().split()
# printt = print
# print = lambda a: printt(" ".join(map(str, a))) if isinstance(a, list) or isinstance(a, tuple) else printt(a)
pl = lambda a: print(" ".join(map(str, a)))
py = lambda: print("Yes")
pn = lambda: print("No")
mod = 998244353  # ac
mod = 10 ** 9 + 7
inf = 10 ** 11
'''代码'''
# mod ↑

times = 0  # 0有t, 1无t
if not times:
    times = ix()
for _ in range(times):
    nm = ix()
    m = il()
    mx = max(m)
    nh = ix()
    ps = [0] * (nm + 1)
    for ii in range(nh):
        p, e = il()
        ps[e] = max(ps[e], p)
    for i in range(nm, 0, -1):
        ps[i - 1] = max(ps[i - 1], ps[i])
    cur = sta = ans = 0
    for i, x in enumerate(m):
        if ps[1] < x:
            print(-1)
            break
        cur = max(cur, x)
        if ps[i - sta + 1] < cur:
            ans += 1
            sta = i
            cur = x

    else:
        print(ans + 1)



# ↑ code

'''test
import os
os.system("python 这我的板子-cf-lite.py <in.in")

2
6
2 3 11 14 1 8
2
3 2
100 1
5
3 5 100 2 3
2
30 5
90 1


'''















