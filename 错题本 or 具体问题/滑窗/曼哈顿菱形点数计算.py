'''
2024年8月17日16:49:31
 E - Manhattan Multifocal Ellipse    https://atcoder.jp/contests/abc366/editorial/10653
2024年8月17日16:49:57, 不是看的非常明白,核心思想是滑窗,  有点二维偏序的意思,

'''
import sys

input = lambda: sys.stdin.readline().rstrip()  ##一个是神奇的卡点...
ip = input
il = lambda: list(map(int, input().split()))  # 单个 n = i()[0]  列表 l = i() #input_list
ix = lambda: il()[0]  # 单个数字  #input_x
iis = lambda: input().split()

n, d = il()
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = il()
m = 2 * 10 ** 6

def calc(xs):
    xsum = [0] * (2 * m + 1)
    xs.sort()
    i = 0
    xsum[-m] = sum(xs) + n * m
    for x in range(-m + 1, m + 1):
        while i < n and xs[i] < x:
            i += 1
        xsum[x] = xsum[x - 1] + 2 * i - n
    return xsum

xsum = calc(x)
ysum = calc(y)
xsum.sort()
ysum.sort()
ans = 0
j = 0
for i in range(2 * m + 1)[::-1]:
    while j < 2 * m + 1 and xsum[i] + ysum[j] <= d:
        j += 1
    ans += j
print(ans)
