'''
这个类型的进阶板子: logtrick
来自https://leetcode.cn/contest/weekly-contest-400/ranking/
第400场周赛, 不造轮子  用的板子

# 注意,是子数组,  连续的!
# 和 或列表 模板 不同, logtrick 返回的是子数组的个数, 而不是长度
'''
from collections import defaultdict
from operator import and_
from typing import List

# 纯享版
# 解决问题 , 同此大类
# 参数:  nums数组, op: 计算方式  包括 and_, or_, gcd, lcm
# 得到的结果 res 是一个字典, key是值 value是值的个数(op后等于这个key的子数组个数)
def lt(nums: List[int], op):
    res = defaultdict(int)
    dp = []
    for pos, cur in enumerate(nums):
        for v in dp:
            v[2] = op(v[2], cur)
        dp.append([pos, pos + 1, cur])
        ptr = 0
        for v in dp[1:]:
            if dp[ptr][2] != v[2]:
                ptr += 1
                dp[ptr] = v
            else:
                dp[ptr][1] = v[1]
        dp = dp[: ptr + 1]
        for v in dp:
            res[v[2]] += v[1] - v[0]
    return res

t = [1,2,3]
print(lt(t, and_))




##附, 更好的测试版子:
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
You are given an array nums and an integer k. You need to find a subarray of nums such that the
absolute difference between k and the bitwise AND of the subarray elements is as small as possible.
In other words, select a subarray nums[l..r] such that |k - (nums[l] AND nums[l + 1] ... AND
nums[r])| is minimum.

Return the minimum possible value of the absolute difference.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,2,4,5], k = 3

Output: 1

Explanation:

The subarray nums[2..3] has AND value 4, which gives the minimum absolute difference |3 - 4| = 1.

Example 2:

Input: nums = [1,2,1,2], k = 2

Output: 0

Explanation:

The subarray nums[1..1] has AND value 2, which gives the minimum absolute difference |2 - 2| = 0.

Example 3:

Input: nums = [1], k = 10

Output: 9

Explanation:

There is a single subarray with AND value 1, which gives the minimum absolute difference |10 - 1| =
9.



Constraints:

 * 1 <= nums.length <= 105
 * 1 <= nums[i] <= 109
 * 1 <= k <= 109
"""

MOD = 1000000007  # 998244353


def logTrick(nums: List[int], op):
    res = defaultdict(int)
    dp = []
    for pos, cur in enumerate(nums):
        for v in dp:
            v[2] = op(v[2], cur)
        dp.append([pos, pos + 1, cur])

        ptr = 0
        for v in dp[1:]:
            if dp[ptr][2] != v[2]:
                ptr += 1
                dp[ptr] = v
            else:
                dp[ptr][1] = v[1]
        dp = dp[: ptr + 1]

        for v in dp:
            res[v[2]] += v[1] - v[0]

    return res


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = logTrick(nums, and_)
        print(res)
        ans = inf
        for x in res:
            ans = min(ans, abs(k - x))
        return ans

testcases = [
    [[1,2,4,5],
3],
    # [],
]

s = Solution()
func_name = dir(s)[-1]  # 可以返回 fun() 的名字...
print(func_name)
func = getattr(s, func_name) #等价于运行了 Solution里面那个fun

for args in testcases:
    print(func(*args))



