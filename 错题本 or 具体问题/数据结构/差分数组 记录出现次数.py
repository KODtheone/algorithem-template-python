'''
2024年8月6日22:48:28
cf题目: https://codeforces.com/contest/1993/problem/C   C. Light Switches
使用差分数组, 记录 周期内, 打开的灯数 ,  还原差分数组
还要考虑一下,是环形的
虽然遍历的多次,但每次都是 O(n)

'''
import operator
from itertools import accumulate

# 还原差分数组技巧:
nums = [1,0,0,0]
res = list(accumulate(nums))
# res = list(accumulate(nums, operator.add, initial= 0))  # 完全体
print(res)

# 答案:
import sys
from collections import deque, defaultdict, Counter
from math import gcd
t = int(sys.stdin.readline().strip())
for _ in range(t) :
    n, k = map(int,sys.stdin.readline().strip().split())
    a = [*map(int, sys.stdin.readline().strip().split())]
    Mod = [0 for i in range(4 * k + 1)]
    mod = [0 for i in range(2 * k)]
    for i in range(n) :
        x = a[i] % (2 * k)
        Mod[x] += 1
        Mod[x + k] -= 1
    mod[0] += Mod[0]
    for i in range(1, 4 * k) :
        Mod[i] += Mod[i - 1]
        mod[i % (2 * k)] += Mod[i]
    if n not in mod :
        print(-1); continue
    m = max(a)
    for i in range(m, m + 2 * k) :
        if mod[i % (2 * k)] == n :
            print(i); break

'''
2024年8月6日22:58:33, 另一题
https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal/description/   3224. 使差值相等的最少数组改动次数
因为区间不同, 加的值不同, 所以用差分数组来记录次数

'''
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # if k == 0: return 0
        n = len(nums) // 2
        d = [0] * (k + 2)
        for i in range(n):
            a = nums[i]
            b = nums[~i]
            if a > b: a,b = b,a
            v = b - a
            v2 = max(k-a, b)
            d[0] += 1
            d[v] -= 1
            d[v + 1] += 1
            d[v2 + 1] += 1
        # print(d)
        return min(accumulate(d))


