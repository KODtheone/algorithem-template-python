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

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        sl = SortedList([(0,0)])
        rebuild = [(price, beauty) for price, beauty in items]
        for p, b in rebuild:
            i = sl.bisect_left((p,b))
            print(i)
            if sl[i-1][1] < b:
                sl.add((p, b))
                while i+1 < len(sl):
                    if sl[i + 1][1] < b:
                        sl.pop(i + 1)
                        print(sl)
                    else: break
        print(sl)
        ans = []
        for q in queries:
            ans.append(sl[sl.bisect_right((q, inf)) - 1][1])
        return ans



# 测试
testcases = [
        [#填入
            [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]],
            [1, 2, 3, 4, 5, 6]
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
