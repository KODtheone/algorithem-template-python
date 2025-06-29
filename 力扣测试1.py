import sys
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
from typing import *

"""
code
"""


def f(m, x):
    def check(mm):
        return x * (1 + mm) * mm //2 <= m

    def bs(l, r):
        while l < r:
            mid = (l + r) >> 1
            if not check(mid):      r = mid
            else:               l = mid + 1
        return r - 1

    l , r = 0, 10**5
    return bs(l, r)



class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(m):
            s = 0
            for x in workerTimes:
                s += f(m, x)
            return s >= mountainHeight

        def bs(l, r):
            while l < r:
                mid = (l + r) >> 1
                if check(mid):      r = mid
                else:               l = mid + 1
            return r

        l , r = 0, 10**20
        return bs(l, r)



# 测试
testcases = [
        [#填入
            100000,
            [1000000]
        ],
    # [
    #
    # ],
]

s = Solution()
func_name = dir(s)[-1]  # 可以返回 fun() 的名字...
func = getattr(s, func_name) #等价于运行了 Solution里面那个fun

for args in testcases:
    print(func(*args))
