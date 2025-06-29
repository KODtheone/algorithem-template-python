'''
2024年11月15日09:53:39
https://www.lanqiao.cn/problems/19978/learning/?contest_id=215
5. 蓝桥派对

给出一个数轴范围.  给出长为n的二维数组, 代表n段范围的l和r, 求出每段与另外多少段有交集.
答案 O(n * logn)
题解 https://www.bilibili.com/video/BV1ZTDEYmE2a/   18分钟
记录所有l, 所有r,  排序.
然后查询一个范围, 用二分可以得出 不想交的区间数 (li 大于r的说明在本区间右边, 无相交, ri 小于l同理)  ( 也是一个 正难则反)
'''
import sys
from bisect说明 import *

input = lambda: sys.stdin.readline().rstrip()  ##一个是神奇的卡点...
il = lambda: list(map(int, input().split()))  # 单个 n = i()[0]  列表 l = i() #input_list
ix = lambda: il()[0]  # 单个数字  #input_x
iis = lambda: input().split()
# 列表输出数字串, 例子 [1,2,3] printout: 1 2 3
# pl 直接用  print(*list) 就完事了...
# pl = lambda a: print(" ".join(map(str, a)))  # print_list
en = enumerate

n, m = il()
a = []
b = []
ii = []
for i in range(n):
    aa, bb = il()
    ii.append((aa, bb))
    a.append(aa)
    b.append(bb)

a.sort()
b.sort()

ans = []
for i in range(n):
    a_i, b_i = ii[i]
    ca = bisect_right(a, b_i)
    cb = bisect_left(b, a_i)
    res = ca - cb - 1
    # ans.append(res)
    print(res)