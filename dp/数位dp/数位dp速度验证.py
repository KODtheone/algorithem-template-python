import sys
import time
from functools import cache

sys.setrecursionlimit(2147483647)
"""
最普通,当枚举用
"""
n = 10**1000
# n = 10**(10**10)   #已经太大了 n都不行
n = 10**(100)
# n = 100000000  ## 10**8 之后,可以看出明显差别
n = 99999999
# n = 10**(10**9)
# n = 1
s = str(n)    #str()是为了方便枚举每一位 int(s[i])
t = time.time()
@cache
def fun(i, is_limit):  # i:位
    if i == len(s): return 1
    res = 0
    up = int(s[i]) if is_limit else 9
    for d in range(up + 1):
        res += fun(i + 1 , is_limit and d == up)
    return res
# return fun(0, 0, True)
print(fun(0,True))
t2 = time.time()
print("数位dp运算时间:",t2 - t)

#速度测试
ans = 0
for i in range(n+1):
    ans += 1
print(ans)
t3 = time.time()
print("普通枚举运算时间:",t3 - t2)