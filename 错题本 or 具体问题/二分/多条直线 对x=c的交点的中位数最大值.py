'''
2024年12月3日12:49:39

蓝桥  https://www.lanqiao.cn/problems/20050/learning/?contest_id=225

题目大意:
给n条直线,  a, b 值 代表 y = ax + b 的直线,  给m个x = c
求n条直线与m个x = c 的交点的中位交点最大值
返回这个交点中位最大值 并返回是跟第几个c

方法: 二分  二分最大中位交点的值,  值域: -2 * 10^18 到 2 * 10^18 值记为mid
记录每个(c, mid) 点上面的直线条数 cnt
遍历n个直线,  计算直线与mid的交点, 将交点与 所有c进行比较
属于段修改, 因此使用差分数组优化
具体:
    如果a==0, b >= mid 则这条直线在所有(c, mid)点的上面 所有cnt上面 + 1
    如果a > 0 直线是单调递增的  则从交点x(包括) 直到末尾的(-1) c 的cnt + 1
    如果a < 0 直线是单调递减的  则从开头(0)直到 交点x(包括)的c的cnt + 1
二分列举中位数

# 注意  用 x = (mid - b) / a   带小数的计算时,  会因为经度问题 导致错误

'''

import sys
from bisect import *

# sys.setrecursionlimit(5005)
input = lambda: sys.stdin.readline().rstrip()
ip = input
il = lambda: list(map(int, input().split()))
ix = lambda: il()[0]
iis = lambda: input().split()
# printt = print
# print = lambda a: printt(" ".join(map(str, a))) if isinstance(a, list) or isinstance(a, tuple) else printt(a)
pl = lambda a: print(" ".join(map(str, a)))
py = lambda: print("Yes")
pn = lambda:  print("No")
mod = 998244353  #ac
mod = 10**9 + 7
inf = 10**11

n = ix()
aa = []
for _ in range(n):
    aa.append(il())
m = ix()
cc = il()
cs = [(x, i + 1) for (i, x) in enumerate(cc)]
cs.sort()
dc = {a: b for (a, b) in cs} # {-3: 1, -1: 4, 2: 3, 3: 2}
nn = n // 2 + 1


def check(mid):
    d = [0] * (m + 1)
    for a, b in aa:
        if a == 0:
            if b >= mid:
                d[0] += 1
        else:
            if a > 0:  # 斜率大于0，从交点后开始+1 可包含交点
                x = (mid - b + a - 1) // a
                ix = bisect_left(cc, x)
                d[ix] += 1
            else:  # 斜率小于0，从0开始+1 交点后开始-1
                x = (mid - b) // a
                ix = bisect_right(cc, x)
                d[0] += 1
                d[ix] -= 1
    s = 0
    for i in range(m):
        s += d[i]
        if s >= nn:
            ans = cc[i]
            break
    else:
        return False, -1
    return True, ans


l, r = -2 * 10 ** 18, 2 * 10 ** 18
ansi = -1
while l < r:
    mid = (l + r) >> 1
    ck, t = check(mid)
    if not ck:
        r = mid
    else:
        l = mid + 1
        ansi = t
ans = r - 1
print( dc[ansi], ans)

