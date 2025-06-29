'''
2025年4月6日00:25:43，
两机流水作业调度问题

example:
https://www.lanqiao.cn/problems/20288/learning/?contest_id=253

处理方式是固定的  原理，因该就是贪心， 但是， 具体，不太清楚。。。

'''

import sys

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
inf = 10**19

'''
4
1 3 5 7
6 5 1 4
'''

N = ix()
A = il()
B = il()

chips = [(A[i], B[i], i) for i in range(N)]
group1 = [chip for chip in chips if chip[0] <= chip[1]]
group2 = [chip for chip in chips if chip[0] > chip[1]]
group1.sort(key=lambda x: x[0])
group2.sort(key=lambda x: x[1], reverse=True)
print(group1)
print(group2)
order = group1 + group2
print(order)
time1 = 0
time2 = 0
for a, b, _ in order:
    time1 += a
    time2 = max(time1, time2) + b

print(time2)
